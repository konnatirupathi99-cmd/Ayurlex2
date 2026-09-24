"use server";

import { system } from './system';

export interface UserSession {
  id: string; // internal ID
  externalId: string; // external open ID
  name: string;
  email: string;
  loginMethod: 'oauth' | 'credentials';
  role: 'user' | 'admin';
  createdAt: string;
  updatedAt: string;
  lastSignInAt: string;
}

export const auth = {
  /**
   * Return the current authenticated user or null.
   * Handles missing cookies, expired sessions, and failed callbacks safely.
   */
  async me(): Promise<UserSession | null> {
    try {
      // Stub: in a real implementation, read session cookie and verify token
      return null; 
    } catch (error) {
      system.log('Error in auth.me', { error });
      return null;
    }
  },

  /**
   * Clear the session cookie and invalidate the client session.
   */
  async logout(): Promise<{ success: boolean; error?: string }> {
    try {
      // Stub: delete cookie, invalidate session
      return { success: true };
    } catch (error) {
      system.log('Logout failed', { error });
      return { success: false, error: system.errors.UNAUTHORIZED };
    }
  },

  /**
   * Protect private workspace procedures.
   * Returns consistent unauthorized error if no session exists.
   */
  async requireUser(): Promise<UserSession> {
    const user = await this.me();
    if (!user) {
      throw new Error(system.errors.UNAUTHORIZED);
    }
    return user;
  },

  /**
   * Permit read-only preview content without exposing private records.
   */
  async preview(): Promise<boolean> {
    // Stub: returns true if preview mode is active based on config/session
    return system.config.previewModeEnabled;
  }
};
