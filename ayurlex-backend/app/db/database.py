import sqlite3
import json
import logging
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)

# DB path
DB_PATH = Path("ayurlex.db")

def get_db_connection() -> sqlite3.Connection:
    """Get a connected sqlite3 instance with row factory."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    # Enforce foreign keys
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    """Initialize database schemas from migration files."""
    migrations_dir = Path(__file__).parent / "migrations"
    if not migrations_dir.exists():
        logger.warning(f"Migrations directory not found at {migrations_dir}")
        return

    migration_files = sorted(migrations_dir.glob("*.sql"))
    
    with get_db_connection() as conn:
        for m_file in migration_files:
            logger.info(f"Applying migration: {m_file.name}")
            with open(m_file, 'r', encoding='utf-8') as f:
                script = f.read()
                conn.executescript(script)
        conn.commit()

def now_utc() -> str:
    """Store timestamps in a consistent timezone."""
    return datetime.now(timezone.utc).isoformat()

class DatabaseInterface:
    """
    Database interface ensuring strict user ownership boundaries.
    All operations must take user_id and strictly bind it to parameter queries.
    Never concatenate user input into SQL.
    """
    
    # ------------------ USERS ------------------
    @staticmethod
    def get_user_by_openid(open_id: str) -> Optional[dict]:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE openId = ?", (open_id,))
            row = cursor.fetchone()
            return dict(row) if row else None
            
    # ------------------ PROJECTS ------------------
    @staticmethod
    def create_project(id: str, user_id: str, name: str, description: str, focus: str, primary_jurisdiction: str) -> dict:
        with get_db_connection() as conn:
            now = now_utc()
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO innovationProjects 
                (id, userId, name, description, focus, primaryJurisdiction, status, createdAt, updatedAt) 
                VALUES (?, ?, ?, ?, ?, ?, 'active', ?, ?)
                """,
                (id, user_id, name, description, focus, primary_jurisdiction, now, now)
            )
            conn.commit()
            return DatabaseInterface.get_project(id, user_id)

    @staticmethod
    def get_project(project_id: str, user_id: str) -> Optional[dict]:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            # Enforce ownership in every query
            cursor.execute("SELECT * FROM innovationProjects WHERE id = ? AND userId = ?", (project_id, user_id))
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def get_projects_by_user(user_id: str) -> List[dict]:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM innovationProjects WHERE userId = ? ORDER BY updatedAt DESC", (user_id,))
            return [dict(r) for r in cursor.fetchall()]

    # ------------------ SESSIONS ------------------
    @staticmethod
    def create_session(id: str, user_id: str, project_id: Optional[str], title: str, language: str) -> dict:
        with get_db_connection() as conn:
            now = now_utc()
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO chatSessions 
                (id, userId, projectId, title, language, createdAt, updatedAt) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (id, user_id, project_id, title, language, now, now)
            )
            conn.commit()
            return DatabaseInterface.get_session(id, user_id)

    @staticmethod
    def get_session(session_id: str, user_id: str) -> Optional[dict]:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM chatSessions WHERE id = ? AND userId = ?", (session_id, user_id))
            row = cursor.fetchone()
            return dict(row) if row else None

    @staticmethod
    def get_sessions_by_user(user_id: str) -> List[dict]:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM chatSessions WHERE userId = ? ORDER BY updatedAt DESC", (user_id,))
            return [dict(r) for r in cursor.fetchall()]

    # ------------------ MESSAGES ------------------
    @staticmethod
    def add_message(id: str, user_id: str, session_id: str, role: str, content: str, meta: dict, citations: list) -> dict:
        with get_db_connection() as conn:
            now = now_utc()
            cursor = conn.cursor()
            # Preserve citation JSON as structured data
            meta_json = json.dumps(meta) if meta else None
            citations_json = json.dumps(citations) if citations else None
            
            cursor.execute(
                """
                INSERT INTO chatMessages 
                (id, userId, sessionId, role, content, meta, citations, createdAt) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (id, user_id, session_id, role, content, meta_json, citations_json, now)
            )
            
            # Update session timestamp
            cursor.execute("UPDATE chatSessions SET updatedAt = ? WHERE id = ? AND userId = ?", (now, session_id, user_id))
            conn.commit()
            
            cursor.execute("SELECT * FROM chatMessages WHERE id = ? AND userId = ?", (id, user_id))
            row = cursor.fetchone()
            return dict(row)

    @staticmethod
    def get_messages_by_session(session_id: str, user_id: str) -> List[dict]:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            # Enforce ownership mapping by verifying session belongs to user
            cursor.execute(
                """
                SELECT m.* FROM chatMessages m
                JOIN chatSessions s ON m.sessionId = s.id
                WHERE m.sessionId = ? AND m.userId = ? AND s.userId = ?
                ORDER BY m.createdAt ASC
                """,
                (session_id, user_id, user_id)
            )
            results = []
            for r in cursor.fetchall():
                d = dict(r)
                d['meta'] = json.loads(d['meta']) if d['meta'] else {}
                d['citations'] = json.loads(d['citations']) if d['citations'] else []
                results.append(d)
            return results

    # ------------------ REPORTS ------------------
    @staticmethod
    def create_report(id: str, user_id: str, project_id: Optional[str], title: str, report_type: str, payload: dict) -> dict:
        with get_db_connection() as conn:
            now = now_utc()
            cursor = conn.cursor()
            payload_json = json.dumps(payload)
            cursor.execute(
                """
                INSERT INTO workspaceReports 
                (id, userId, projectId, title, reportType, payload, createdAt) 
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (id, user_id, project_id, title, report_type, payload_json, now)
            )
            conn.commit()
            
            cursor.execute("SELECT * FROM workspaceReports WHERE id = ? AND userId = ?", (id, user_id))
            row = dict(cursor.fetchone())
            row['payload'] = json.loads(row['payload'])
            return row

    @staticmethod
    def get_reports_by_user(user_id: str) -> List[dict]:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM workspaceReports WHERE userId = ? ORDER BY createdAt DESC", (user_id,))
            results = []
            for r in cursor.fetchall():
                d = dict(r)
                d['payload'] = json.loads(d['payload']) if d['payload'] else {}
                results.append(d)
            return results
