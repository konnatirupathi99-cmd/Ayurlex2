export interface ChatMessage {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  timestamp: string;
  sources?: Source[];
}

export interface Source {
  id: string;
  title: string;
  url?: string;
  snippet?: string;
  confidenceScore?: number;
}

type ResearchResponse = {
  answer?: string;
  sources?: Source[];
  error?: string;
};

export const sendMessage = async (
  message: string,
  history: ChatMessage[],
  onUpdate: (content: string) => void
): Promise<ChatMessage> => {
  const response = await fetch('/api/research', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      message,
      history: history.slice(-8).map(({ role, content }) => ({ role, content })),
    }),
  });

  const result = await response.json() as ResearchResponse;
  if (!response.ok || !result.answer) {
    throw new Error(result.error || 'AYURLEX could not complete this research request.');
  }

  // Reveal the completed, server-validated report in readable chunks.
  const answer = result.answer;
  const chunkSize = 28;
  for (let index = chunkSize; index < answer.length; index += chunkSize) {
    onUpdate(answer.slice(0, index));
    await new Promise((resolve) => setTimeout(resolve, 8));
  }
  onUpdate(answer);

  return {
    id: crypto.randomUUID(),
    role: 'assistant',
    content: answer,
    timestamp: new Date().toISOString(),
    sources: result.sources || [],
  };
};
