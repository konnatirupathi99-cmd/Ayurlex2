-- Migration: 001_initial_schema
-- Description: Creates initial relational schema for AYURLEX workspace

CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    openId TEXT UNIQUE NOT NULL,
    name TEXT,
    email TEXT,
    loginMethod TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('user', 'admin')),
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    lastSignedIn DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS innovationProjects (
    id TEXT PRIMARY KEY,
    userId TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    focus TEXT,
    primaryJurisdiction TEXT,
    status TEXT NOT NULL CHECK(status IN ('active', 'paused', 'completed')),
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    FOREIGN KEY(userId) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_projects_user_id ON innovationProjects(userId);
CREATE INDEX IF NOT EXISTS idx_projects_created_at ON innovationProjects(createdAt);
CREATE INDEX IF NOT EXISTS idx_projects_updated_at ON innovationProjects(updatedAt);

CREATE TABLE IF NOT EXISTS chatSessions (
    id TEXT PRIMARY KEY,
    userId TEXT NOT NULL,
    projectId TEXT,
    title TEXT NOT NULL,
    language TEXT,
    createdAt DATETIME NOT NULL,
    updatedAt DATETIME NOT NULL,
    FOREIGN KEY(userId) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY(projectId) REFERENCES innovationProjects(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_sessions_user_id ON chatSessions(userId);
CREATE INDEX IF NOT EXISTS idx_sessions_project_id ON chatSessions(projectId);
CREATE INDEX IF NOT EXISTS idx_sessions_created_at ON chatSessions(createdAt);
CREATE INDEX IF NOT EXISTS idx_sessions_updated_at ON chatSessions(updatedAt);

CREATE TABLE IF NOT EXISTS chatMessages (
    id TEXT PRIMARY KEY,
    userId TEXT NOT NULL,
    sessionId TEXT NOT NULL,
    role TEXT NOT NULL CHECK(role IN ('user', 'assistant')),
    content TEXT NOT NULL,
    meta TEXT,
    citations TEXT,
    createdAt DATETIME NOT NULL,
    FOREIGN KEY(userId) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY(sessionId) REFERENCES chatSessions(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_messages_user_id ON chatMessages(userId);
CREATE INDEX IF NOT EXISTS idx_messages_session_id ON chatMessages(sessionId);
CREATE INDEX IF NOT EXISTS idx_messages_created_at ON chatMessages(createdAt);

CREATE TABLE IF NOT EXISTS workspaceReports (
    id TEXT PRIMARY KEY,
    userId TEXT NOT NULL,
    projectId TEXT,
    title TEXT NOT NULL,
    reportType TEXT NOT NULL,
    payload TEXT NOT NULL,
    createdAt DATETIME NOT NULL,
    FOREIGN KEY(userId) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY(projectId) REFERENCES innovationProjects(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_reports_user_id ON workspaceReports(userId);
CREATE INDEX IF NOT EXISTS idx_reports_project_id ON workspaceReports(projectId);
CREATE INDEX IF NOT EXISTS idx_reports_created_at ON workspaceReports(createdAt);
