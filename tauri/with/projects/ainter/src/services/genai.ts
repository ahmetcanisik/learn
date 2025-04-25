import { GoogleGenAI } from '@google/genai';

// Initialize the Google GenAI with API key
// You should use environment variables in production
const API_KEY = 'AIzaSyAggpOPvNdQLYVKEFuwUGdUQR3GxVILWL4'; // Using the key from the existing code
const genAI = new GoogleGenAI({ apiKey: API_KEY });

// Function to generate text from prompt
export const generateText = async (prompt: string) => {
  try {
    const response = await genAI.models.generateContent({
      model: "gemini-2.0-flash",
      contents: prompt,
    });
    
    return response.text;
  } catch (error) {
    console.error('Error generating text:', error);
    throw error;
  }
};

// Function to generate text with chat history
export const generateChatResponse = async (
  chatHistory: { role: 'user' | 'model'; parts: { text: string }[] }[]
) => {
  try {
    // Format chat history for the API
    const formattedHistory = chatHistory.map(message => {
      return {
        role: message.role === 'user' ? 'user' : 'model',
        content: message.parts[0].text
      };
    });
    
    // Get the last user message
    const lastUserMessage = chatHistory
      .filter(msg => msg.role === 'user')
      .pop();
      
    if (!lastUserMessage) {
      return 'No user message found in the chat history.';
    }
    
    // Send request to the chat model
    const response = await genAI.models.generateContent({
      model: "gemini-2.0-flash",
      contents: [
        ...formattedHistory.map(msg => ({
          role: msg.role,
          parts: [{ text: msg.content }]
        }))
      ],
    });
    
    return response.text;
  } catch (error) {
    console.error('Error generating chat response:', error);
    throw error;
  }
}; 