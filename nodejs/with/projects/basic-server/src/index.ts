import express from 'express';
import { projects, ProjectsOptions } from './lib/projects';

export interface ServerOptions {
    port: number;
    hostname: string;
}

export const options: ServerOptions = {
    port: 3000,
    hostname: '127.0.0.1'
}

const app = express();

app.use(express.json());

app.get('/', (req, res) => {
    res.send('Hello, World!');
    console.log(req.body);
});

app.get('/projects', (req, res) => {
    res.send(projects);
});

app.get('/project/:id', (req, res) => {
    const project = projects.filter(p => p.id === req.params.id)[0];
    if (project) {
        res.send(project);
    } else {
        res.send("Böyle bir proje bulunamadı!");
    }
});

app.put('/projects', (req, res) => {
    res.send("KUllanıcı verileri değiştirmek için bir istek gönderdi.");
});

// postman kullanarak body olarak json verisi gönderince düzgün çalışıyor.
app.post('/projects', (req, res) => {
    const data: ProjectsOptions = req.body;
    res.send(`Kullanıcı veri eklemek için bir istek gönderdi.\n${data.name}\n${data.author}`);
});

app.delete('/projects', (req, res) => {
    res.send("Kullanıcı veri değiştirmek için bir istek gönderdi.");
});

app.listen(options.port, () => {
    console.log(`Server listening on http://${options.hostname}:${options.port}`);
});