import ReactMarkdown from 'react-markdown';
import rehypeRaw from 'rehype-raw';
import { HTMLAttributes } from 'react';

interface MarkdownRendererProps {
  children: string;
  baseUrl?: string;
}

interface ImageProps extends HTMLAttributes<HTMLImageElement> {
  src?: string;
  alt?: string;
}

const components = {
  h1: ({ children, ...props }: HTMLAttributes<HTMLHeadingElement>) => <h1 style={{ color: '#2c3e50', fontSize: '2.5em' }} {...props}>{children}</h1>,
  h2: ({ children, ...props }: HTMLAttributes<HTMLHeadingElement>) => <h2 style={{ color: '#34495e', fontSize: '2em', marginTop: '1.5em' }} {...props}>{children}</h2>,
  p: ({ children, ...props }: HTMLAttributes<HTMLParagraphElement>) => <p style={{ lineHeight: '1.6', marginBottom: '1em' }} {...props}>{children}</p>,
  ul: ({ children, ...props }: HTMLAttributes<HTMLUListElement>) => <ul style={{ paddingLeft: '1.5em', marginBottom: '1em' }} {...props}>{children}</ul>,
  li: ({ children, ...props }: HTMLAttributes<HTMLLIElement>) => <li style={{ marginBottom: '0.5em' }} {...props}>{children}</li>,
  code: ({ children, ...props }: HTMLAttributes<HTMLElement>) => <code style={{ backgroundColor: '#f8f9fa', padding: '0.2em 0.4em', borderRadius: '3px' }} {...props}>{children}</code>,
  pre: ({ children, ...props }: HTMLAttributes<HTMLPreElement>) => <pre style={{ backgroundColor: '#f8f9fa', padding: '1em', borderRadius: '5px', overflow: 'auto' }} {...props}>{children}</pre>,
  // HTML elementleri için varsayılan stiller
  div: ({ children, ...props }: HTMLAttributes<HTMLDivElement>) => <div style={{ marginBottom: '1em' }} {...props}>{children}</div>,
  span: ({ children, ...props }: HTMLAttributes<HTMLSpanElement>) => <span {...props}>{children}</span>,
  a: ({ children, ...props }: HTMLAttributes<HTMLAnchorElement>) => <a style={{ color: '#0366d6', textDecoration: 'none' }} {...props}>{children}</a>,
  table: ({ children, ...props }: HTMLAttributes<HTMLTableElement>) => <table style={{ borderCollapse: 'collapse', width: '100%', marginBottom: '1em' }} {...props}>{children}</table>,
  th: ({ children, ...props }: HTMLAttributes<HTMLTableCellElement>) => <th style={{ border: '1px solid #ddd', padding: '8px', backgroundColor: '#f8f9fa' }} {...props}>{children}</th>,
  td: ({ children, ...props }: HTMLAttributes<HTMLTableCellElement>) => <td style={{ border: '1px solid #ddd', padding: '8px' }} {...props}>{children}</td>,
};

export function MarkdownRenderer({ children, baseUrl }: MarkdownRendererProps) {
  const getImageUrl = (src?: string) => {
    if (!src) return '';
    if (src.startsWith('http://') || src.startsWith('https://')) {
      return src;
    }
    return baseUrl ? `${baseUrl}/${src}` : src;
  };

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '2em' }}>
      <ReactMarkdown 
        components={{
          ...components,
          img: ({ src, alt, ...props }: ImageProps) => (
            <img 
              src={getImageUrl(src)} 
              alt={alt || ''} 
              style={{ maxWidth: '100%', height: 'auto', borderRadius: '4px' }} 
              {...props} 
            />
          ),
        }}
        rehypePlugins={[rehypeRaw]}
      >
        {children}
      </ReactMarkdown>
    </div>
  );
} 