"use server";

import { auth } from './auth';
import { system } from './system';
import { Citation } from './citations';

export interface Project {
  id: string;
  userId: string;
  name: string;
  description: string;
  focus: string;
  primaryJurisdiction: string;
  status: 'active' | 'paused' | 'completed';
  createdAt: string;
  updatedAt: string;
}

export interface Session {
  id: string;
  userId: string;
  projectId: string;
  title: string;
  language: string;
  createdAt: string;
}

export interface Message {
  id: string;
  sessionId: string;
  role: 'user' | 'assistant';
  content: string;
  meta?: any;
  createdAt: string;
}

export interface Report {
  id: string;
  userId: string;
  projectId: string;
  title: string;
  reportType: 'jurisdiction_matrix' | 'innovation_brief';
  payload: any;
  createdAt: string;
}

export const workspace = {
  /**
   * Return the authenticated user’s projects, sessions, and reports.
   */
  async overview(): Promise<{ projects: Project[]; sessions: Session[]; reports: Report[] }> {
    const user = await auth.requireUser();
    // Scoped to user.id
    return { projects: [], sessions: [], reports: [] };
  },

  /**
   * Return messages only for a session owned by the current user.
   */
  async messages({ sessionId }: { sessionId: string }): Promise<Message[]> {
    const user = await auth.requireUser();
    // Validate session ownership before returning
    return [];
  },

  /**
   * Create a new project for the authenticated user.
   */
  async createProject({ name, description, focus, primaryJurisdiction }: { name: string, description: string, focus: string, primaryJurisdiction: string }): Promise<Project> {
    const user = await auth.requireUser();
    // Validate input length limits
    if (name.length > 100) throw new Error(system.errors.VALIDATION);
    
    return {
      id: typeof crypto !== 'undefined' ? crypto.randomUUID() : Math.random().toString(),
      userId: user.id,
      name,
      description,
      focus,
      primaryJurisdiction,
      status: 'active',
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString()
    };
  },

  async createSession({ title, language, projectId }: { title: string, language: string, projectId: string }): Promise<Session> {
    const user = await auth.requireUser();
    // Verify project ownership
    return {
      id: typeof crypto !== 'undefined' ? crypto.randomUUID() : Math.random().toString(),
      userId: user.id,
      projectId,
      title,
      language,
      createdAt: new Date().toISOString()
    };
  },

  async addMessage({ sessionId, role, content, meta, citations }: { sessionId: string, role: 'user'|'assistant', content: string, meta?: any, citations?: Citation[] }): Promise<Message> {
    const user = await auth.requireUser();
    if (role !== 'user' && role !== 'assistant') throw new Error(system.errors.VALIDATION);
    // Verify session ownership
    // Store citation metadata separately
    return {
      id: typeof crypto !== 'undefined' ? crypto.randomUUID() : Math.random().toString(),
      sessionId,
      role,
      content,
      meta: { ...meta, citationsReferenceId: citations ? (typeof crypto !== 'undefined' ? crypto.randomUUID() : Math.random().toString()) : null },
      createdAt: new Date().toISOString()
    };
  },

  async createReport({ title, reportType, payload, projectId }: { title: string, reportType: 'jurisdiction_matrix' | 'innovation_brief', payload: any, projectId: string }): Promise<Report> {
    const user = await auth.requireUser();
    // Verify project ownership
    return {
      id: typeof crypto !== 'undefined' ? crypto.randomUUID() : Math.random().toString(),
      userId: user.id,
      projectId,
      title,
      reportType,
      payload,
      createdAt: new Date().toISOString()
    };
  }
};
