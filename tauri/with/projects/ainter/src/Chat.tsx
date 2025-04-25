import { useState, useRef, useEffect } from 'react';
import './Chat.css';
import { generateText, generateChatResponse } from './services/genai';

type Message = {
  id: string;
  text: string;
  isUser: boolean;
};

// History for context
type ChatHistory = {
  role: 'user' | 'model';
  parts: { text: string }[];
}[];

export default function Chat() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      text: 'Hello! I\'m your AI assistant powered by Gemini. How can I help you today?',
      isUser: false,
    },
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const [chatHistory, setChatHistory] = useState<ChatHistory>([
    { role: 'model', parts: [{ text: 'Hello! I\'m your AI assistant powered by Gemini. How can I help you today?' }] }
  ]);

  // Function to get response using the new SDK
  const getGeminiResponse = async (userMessage: string): Promise<string> => {
    try {
      // Use the chat history for better context
      return await generateChatResponse([...chatHistory, { role: 'user', parts: [{ text: userMessage }] }]);
    } catch (error) {
      console.error('Error calling Gemini API:', error);
      return `Error: ${error instanceof Error ? error.message : String(error)}`;
    }
  };

  // Fallback mock response if API fails
  const getMockResponse = (userMessage: string): string => {
    if (userMessage.toLowerCase().includes('hello') || userMessage.toLowerCase().includes('hi')) {
      return 'Hello there! How can I assist you today? (Mock response - API failed)';
    } else if (userMessage.toLowerCase().includes('help')) {
      return 'I\'m here to help! Just let me know what you need assistance with. (Mock response - API failed)';
    } else {
      return `I received your message, but I'm currently in fallback mode due to API issues. Please try again later. Your message was: "${userMessage}"`;
    }
  };

  const handleSendMessage = async () => {
    if (input.trim() === '' || isLoading) return;
    
    // Add user message
    const userMessage: Message = {
      id: Date.now().toString(),
      text: input,
      isUser: true,
    };
    
    setMessages(prevMessages => [...prevMessages, userMessage]);
    setInput('');
    setIsLoading(true);
    
    // Store user message in chat history
    const userContent = { role: 'user' as const, parts: [{ text: input }] };
    setChatHistory(prev => [...prev, userContent]);
    
    // Get AI response
    try {
      // Try using the new SDK
      let aiResponseText = await getGeminiResponse(input);
      
      // If it fails, use mock response
      if (aiResponseText.startsWith('Error:')) {
        console.log('API call failed, using mock response');
        aiResponseText = getMockResponse(input);
      }
      
      const aiMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: aiResponseText,
        isUser: false,
      };
      
      // Store AI response in chat history
      const aiContent = { role: 'model' as const, parts: [{ text: aiResponseText }] };
      setChatHistory(prev => [...prev, aiContent]);
      
      setMessages(prevMessages => [...prevMessages, aiMessage]);
    } catch (error) {
      console.error('All methods failed:', error);
      const fallbackText = getMockResponse(input);
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: fallbackText,
        isUser: false,
      };
      
      setMessages(prevMessages => [...prevMessages, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  // Auto-scroll to bottom when messages change
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  return (
    <div className="chat-container">
      <div className="chat-messages">
        {messages.map(message => (
          <div 
            key={message.id} 
            className={`message ${message.isUser ? 'user-message' : 'ai-message'}`}
          >
            <div className="message-content">{message.text}</div>
          </div>
        ))}
        
        {isLoading && (
          <div className="typing-indicator">
            <div className="typing-dot"></div>
            <div className="typing-dot"></div>
            <div className="typing-dot"></div>
          </div>
        )}
        
        <div ref={messagesEndRef} />
      </div>
      
      <div className="input-container">
        <textarea
          className="message-input"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Type your message here..."
          rows={1}
          disabled={isLoading}
        />
        <button 
          className="send-button" 
          onClick={handleSendMessage}
          disabled={input.trim() === '' || isLoading}
        >
          Send
        </button>
      </div>
    </div>
  );
}