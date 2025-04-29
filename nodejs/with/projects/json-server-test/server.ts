import jsonServer from 'json-server';
import type { Request, Response, NextFunction } from 'express';

interface Homework {
  id: string;
  owner_id: string;
  subject: string;
  content: string;
}

const server = jsonServer.create();
const router = jsonServer.router<{ homeworks: Homework[] }>('test.json');
const middlewares = jsonServer.defaults();

// Custom authorization middleware with TypeScript types
const authMiddleware = (req: Request, res: Response, next: NextFunction): void => {
  if (req.method === 'POST') {
    const authHeader = req.headers.authorization;
    
    if (!authHeader) {
      res.status(401).json({ error: 'Authorization header is required' });
      return;
    }

    const token = authHeader.split(' ')[1];
    if (!token) {
      res.status(401).json({ error: 'Invalid authorization format. Use Bearer token' });
      return;
    }

    // You can implement your token validation logic here
    // For example, using JWT or your own token validation
    if (token !== 'your-secret-token') {
      res.status(403).json({ error: 'Invalid token' });
      return;
    }
  }
  next();
};

server.use(middlewares);
server.use(authMiddleware);
server.use(router);

const port = 3000;
server.listen(port, () => {
  console.log(`JSON Server is running on port ${port}`);
}); 