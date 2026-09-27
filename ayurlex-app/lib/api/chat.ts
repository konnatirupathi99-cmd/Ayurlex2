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

export const sendMessage = async (
  message: string,
  history: ChatMessage[],
  onUpdate: (chunk: string) => void
): Promise<ChatMessage> => {
  // Mock API call that simulates a streaming response
  // In a real application, this would connect to the FastAPI backend using fetch or EventSource
  return new Promise((resolve) => {
    const aiResponse = "Based on the Ayurvedic texts and regulatory guidelines, this formulation appears to be well-documented. Here are the details:\n\n1. **Ashwagandha**: Known for adaptogenic properties.\n2. **Brahmi**: Used for cognitive enhancement.\n\n```python\n# Example of formulation mapping\nformulation = {\n  'Ashwagandha': '30%',\n  'Brahmi': '20%'\n}\n```\n\nIs there anything else you need help with regarding this IP?";
    
    let currentText = "";
    let currentIndex = 0;
    
    const interval = setInterval(() => {
      const chunk = aiResponse.slice(currentIndex, currentIndex + 5);
      currentText += chunk;
      currentIndex += 5;
      
      onUpdate(currentText);
      
      if (currentIndex >= aiResponse.length) {
        clearInterval(interval);
        resolve({
          id: Date.now().toString(),
          role: 'assistant',
          content: aiResponse,
          timestamp: new Date().toISOString(),
          sources: [
            {
              id: 'src-1',
              title: 'Charaka Samhita',
              confidenceScore: 0.95,
              snippet: 'Reference to Ashwagandha formulation.'
            },
            {
              id: 'src-2',
              title: 'AYUSH Guidelines 2024',
              confidenceScore: 0.88,
              snippet: 'Regulatory constraints on Brahmi.'
            }
          ]
        });
      }
    }, 50);
  });
};
