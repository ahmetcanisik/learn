declare module '*.md' {
  import type { ComponentType } from 'react';
  const component: ComponentType;
  export default component;
} 