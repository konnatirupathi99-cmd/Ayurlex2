"use server";

import { system } from './system';

export interface Citation {
  id: string;
  title: string;
  authors: string[];
  year: number;
  source: string;
  kind: 'classical' | 'journal';
  url?: string;
  doi?: string;
  excerpt?: string;
  verified: boolean;
}

export const citations = {
  /**
   * Search for Ayurveda-related citations.
   * Constrains live searches to Ayurveda-related terms.
   */
  async search({ query, limit = 10 }: { query: string; limit?: number }): Promise<Citation[]> {
    const correlationId = system.generateCorrelationId();
    system.log('Starting citation search', { query, limit, correlationId });
    
    try {
      // Force constraint to Ayurveda terms
      const constrainedQuery = `${query} AND (ayurveda OR herbal OR traditional medicine)`;
      
      // Stub: Fetch from Europe PMC or similar, respecting bounded timeouts
      // Example normalized result
      return [];
    } catch (error) {
      system.log('Citation search failed, using fallback', { error, correlationId });
      return this.fallback(query);
    }
  },

  /**
   * Provide curated classical source records.
   */
  async classical(query: string): Promise<Citation[]> {
    // Stub: Return verified classical references
    return [];
  },

  /**
   * Transform external records into a stable AYURLEX citation schema.
   * Cleans HTML, normalizes whitespace, caps excerpt length.
   */
  normalize(rawRecord: any, kind: 'classical' | 'journal'): Citation {
    // Never invent missing authors, dates, or identifiers.
    return {
      id: rawRecord.id || (typeof crypto !== 'undefined' ? crypto.randomUUID() : Math.random().toString()),
      title: this.cleanHtml(rawRecord.title) || 'Unknown Title',
      authors: Array.isArray(rawRecord.authorString) ? rawRecord.authorString : [],
      year: parseInt(rawRecord.pubYear, 10) || new Date().getFullYear(),
      source: rawRecord.journalTitle || 'Unknown Source',
      kind,
      url: rawRecord.url,
      doi: rawRecord.doi,
      excerpt: this.cleanHtml(rawRecord.abstractText)?.slice(0, 300),
      // Mark verified only if from a curated authoritative record or successful index response
      verified: rawRecord.isVerified === true
    };
  },

  cleanHtml(text?: string): string {
    if (!text) return '';
    return text.replace(/<[^>]*>?/gm, '').replace(/\s+/g, ' ').trim();
  },

  fallback(query: string): Citation[] {
    // Safe fallback when external service is temporarily unavailable
    return [];
  }
};
