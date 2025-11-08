// Frontend API Service - Add this to your React app
// Location: frontend/AI Self-Reflection Coach/src/services/api.ts

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export interface DilemmaRequest {
  user_id?: string;
  dilemma: string;
  context?: Record<string, any>;
}

export interface PersonaResponse {
  persona: string;
  name: string;
  icon: string;
  response: string;
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

  constructor() {
    this.baseUrl = API_BASE_URL;
  }

  async checkHealth(): Promise<boolean> {
    try {
      const response = await fetch(`${this.baseUrl}/`);
      return response.ok;
    } catch {
      return false;
    }
  }

  async getReflections(dilemma: string, userId: string = 'default_user'): Promise<DilemmaResponse> {
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
  }

  async createActionPlan(
    entryId: string,
    responses: PersonaResponse[],
    preferences: Record<string, any> = {}
  ): Promise<ActionPlan> {
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
  }

  async getPersonas() {
    const response = await fetch(`${this.baseUrl}/api/personas`);
    
    if (!response.ok) {
      throw new Error('Failed to get personas');
    }

    return response.json();
  }
}

export const api = new PersonaReflectAPI();

// Hook for React components
export function usePersonaReflect() {
  const [isLoading, setIsLoading] = React.useState(false);
  const [error, setError] = React.useState<string | null>(null);

  const getInsights = async (dilemma: string) => {
    setIsLoading(true);
    setError(null);
    try {
      const response = await api.getReflections(dilemma);
      return response;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setIsLoading(false);
    }
  };

  const generateActionPlan = async (
    entryId: string,
    responses: PersonaResponse[]
  ) => {
    setIsLoading(true);
    setError(null);
    try {
      const plan = await api.createActionPlan(entryId, responses);
      return plan;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setIsLoading(false);
    }
  };

  return {
    isLoading,
    error,
    getInsights,
    generateActionPlan,
  };
}

// Example usage in React component:
/*
import { usePersonaReflect } from '@/services/api';

function YourComponent() {
  const { getInsights, generateActionPlan, isLoading } = usePersonaReflect();
  
  const handleSubmit = async (dilemma: string) => {
    const insights = await getInsights(dilemma);
    // Process insights...
  };
}
*/
