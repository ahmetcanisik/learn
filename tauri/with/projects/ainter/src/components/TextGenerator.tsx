import { useState } from 'react';
import { generateText } from '../services/genai';
import './TextGenerator.css';

export default function TextGenerator() {
  const [prompt, setPrompt] = useState('');
  const [result, setResult] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleGenerateText = async () => {
    if (!prompt.trim() || isLoading) return;
    
    setIsLoading(true);
    setError('');
    
    try {
      const generatedText = await generateText(prompt);
      setResult(generatedText);
    } catch (err) {
      setError(`Failed to generate text: ${err instanceof Error ? err.message : String(err)}`);
      console.error('Text generation error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="text-generator">
      <h2>Google Gemini Text Generator</h2>
      
      <div className="input-section">
        <label htmlFor="prompt">Enter your prompt:</label>
        <textarea
          id="prompt"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Describe a futuristic city..."
          rows={4}
          disabled={isLoading}
          className="prompt-input"
        />
        
        <button 
          onClick={handleGenerateText}
          disabled={!prompt.trim() || isLoading}
          className="generate-button"
        >
          {isLoading ? 'Generating...' : 'Generate Text'}
        </button>
      </div>
      
      {error && (
        <div className="error-message">
          {error}
        </div>
      )}
      
      {result && (
        <div className="result-section">
          <h3>Generated Text:</h3>
          <div className="result-content">
            {result}
          </div>
        </div>
      )}
    </div>
  );
} 