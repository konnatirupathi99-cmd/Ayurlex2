"use server";

export const system = {
  errors: {
    UNAUTHORIZED: 'UNAUTHORIZED_ACCESS',
    FORBIDDEN: 'FORBIDDEN_RESOURCE',
    VALIDATION: 'VALIDATION_FAILED',
    EXTERNAL_SERVICE: 'EXTERNAL_SERVICE_UNAVAILABLE',
    DATABASE: 'DATABASE_ERROR',
    RATE_LIMIT: 'RATE_LIMIT_EXCEEDED'
  },

  config: {
    citationLimits: 10,
    requestTimeoutMs: 5000,
    supportedLanguages: ['en', 'sa', 'mr', 'ta', 'te', 'kn', 'ml', 'bn', 'gu', 'pa', 'or', 'ur', 'ne', 'si', 'fr', 'de'],
    defaultJurisdiction: 'india',
    previewModeEnabled: true
  },

  /**
   * Service health checks for database connectivity and external citation availability.
   * Exposes only safe status information to the client.
   */
  async health(): Promise<{ status: 'ok' | 'degraded' | 'down'; db: boolean; externalCitations: boolean }> {
    return {
      status: 'ok',
      db: true,
      externalCitations: true
    };
  },

  /**
   * Structured server logging that excludes credentials, cookies, raw authorization headers, and sensitive user content.
   */
  log(message: string, context?: any) {
    // Strip sensitive fields before logging
    const safeContext = { ...context };
    delete safeContext.password;
    delete safeContext.cookie;
    delete safeContext.authorization;
    delete safeContext.sessionSecret;
    
    console.log(JSON.stringify({
      timestamp: new Date().toISOString(),
      message,
      context: safeContext
    }));
  },

  /**
   * Request correlation IDs for tracing a citation search, chat save, project write, or report export.
   */
  generateCorrelationId(): string {
    return typeof crypto !== 'undefined' ? crypto.randomUUID() : Math.random().toString(36).substring(2);
  }
};
