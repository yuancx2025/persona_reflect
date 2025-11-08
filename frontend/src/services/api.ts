// API Service for connecting to PersonaReflect backend
// Place this file at: src/services/api.ts

import { PersonaResponse } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export interface DilemmaRequest {
  user_id?: string;
  dilemma: string;
  context?: Record<string, any>;
}

export interface DilemmaResponse {
  id: string;
  timestamp: string;
  dilemma: string;
  responses: PersonaResponse[];
  suggested_actions: string[];
}

export interface ActionPlanRequest {
  entry_id: string;
  responses: PersonaResponse[];
  user_preferences?: Record<string, any>;
}

export interface ActionPlan {
  id: string;
  entry_id: string;
  steps: string[];
  created_at: string;
}

class PersonaReflectAPI {
  private baseUrl: string;
  private isBackendAvailable: boolean = false;

  constructor() {
    this.baseUrl = API_BASE_URL;
    this.checkBackendHealth();
  }

  private async checkBackendHealth(): Promise<void> {
    try {
      const response = await fetch(`${this.baseUrl}/`, {
        method: 'GET',
        signal: AbortSignal.timeout(3000), // 3 second timeout
      });
      this.isBackendAvailable = response.ok;
      if (this.isBackendAvailable) {
        console.log('✅ Backend API connected');
      }
    } catch (error) {
      console.log('⚠️ Backend API not available, using mock data');
      this.isBackendAvailable = false;
    }
  }

  async checkHealth(): Promise<boolean> {
    await this.checkBackendHealth();
    return this.isBackendAvailable;
  }

  async getReflections(dilemma: string, userId: string = 'default_user'): Promise<DilemmaResponse> {
    // Check if backend is available
    if (!this.isBackendAvailable) {
      // Fall back to mock data
      return this.getMockReflections(dilemma);
    }

    try {
      const response = await fetch(`${this.baseUrl}/api/reflect`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: userId,
          dilemma,
          context: {},
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to get reflections');
      }

      return response.json();
    } catch (error) {
      console.error('API Error:', error);
      // Fall back to mock data
      return this.getMockReflections(dilemma);
    }
  }

  private getMockReflections(dilemma: string): DilemmaResponse {
    // Import the mock generator function
    const { generatePersonaResponses } = require('../lib/mockData');
    const responses = generatePersonaResponses(dilemma);
    
    return {
      id: `entry-${Date.now()}`,
      timestamp: new Date().toISOString(),
      dilemma,
      responses,
      suggested_actions: [
        'Start with a 5-minute meditation to center yourself',
        'Write down three specific concerns and address them one by one',
        'Schedule dedicated time blocks for focused work',
        'Practice self-compassion and acknowledge your progress',
        'Seek support from a trusted friend or mentor',
      ],
    };
  }

  async createActionPlan(
    entryId: string,
    responses: PersonaResponse[],
    preferences: Record<string, any> = {}
  ): Promise<ActionPlan> {
    if (!this.isBackendAvailable) {
      // Return mock action plan
      return {
        id: `ap-${Date.now()}`,
        entry_id: entryId,
        steps: [
          'Begin with 5-minute daily mindfulness practice',
          'Identify and challenge one negative thought pattern',
          'Create a structured daily schedule with time blocks',
          'Practice one act of self-compassion each day',
          'Track progress in a journal for accountability',
        ],
        created_at: new Date().toISOString(),
      };
    }

    try {
      const response = await fetch(`${this.baseUrl}/api/action-plan`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          entry_id: entryId,
          responses,
          user_preferences: preferences,
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to create action plan');
      }

      return response.json();
    } catch (error) {
      console.error('API Error:', error);
      // Return mock action plan
      return {
        id: `ap-${Date.now()}`,
        entry_id: entryId,
        steps: [
          'Begin with 5-minute daily mindfulness practice',
          'Identify and challenge one negative thought pattern',
          'Create a structured daily schedule with time blocks',
          'Practice one act of self-compassion each day',
          'Track progress in a journal for accountability',
        ],
        created_at: new Date().toISOString(),
      };
    }
  }

  async getPersonas() {
    if (!this.isBackendAvailable) {
      return {
        personas: [
          {
            id: 'cognitive-behavioral',
            name: 'Dr. Chen',
            icon: '🧠',
            title: 'Cognitive-Behavioral Coach',
            description: 'Helps identify thought patterns and develop practical strategies',
          },
          {
            id: 'empathetic-friend',
            name: 'Maya',
            icon: '💙',
            title: 'Empathetic Friend',
            description: 'Provides emotional support and validation',
          },
          {
            id: 'rational-analyst',
            name: 'Alex',
            icon: '📊',
            title: 'Rational Analyst',
            description: 'Offers structured, data-driven approaches',
          },
          {
            id: 'mindfulness-mentor',
            name: 'Sage',
            icon: '🧘',
            title: 'Mindfulness Mentor',
            description: 'Guides toward present-moment awareness',
          },
        ],
      };
    }

    try {
      const response = await fetch(`${this.baseUrl}/api/personas`);
      
      if (!response.ok) {
        throw new Error('Failed to get personas');
      }

      return response.json();
    } catch (error) {
      // Return default personas
      return {
        personas: [
          {
            id: 'cognitive-behavioral',
            name: 'Dr. Chen',
            icon: '🧠',
            title: 'Cognitive-Behavioral Coach',
            description: 'Helps identify thought patterns and develop practical strategies',
          },
          {
            id: 'empathetic-friend',
            name: 'Maya',
            icon: '💙',
            title: 'Empathetic Friend',
            description: 'Provides emotional support and validation',
          },
          {
            id: 'rational-analyst',
            name: 'Alex',
            icon: '📊',
            title: 'Rational Analyst',
            description: 'Offers structured, data-driven approaches',
          },
          {
            id: 'mindfulness-mentor',
            name: 'Sage',
            icon: '🧘',
            title: 'Mindfulness Mentor',
            description: 'Guides toward present-moment awareness',
          },
        ],
      };
    }
  }
}

export const api = new PersonaReflectAPI();
