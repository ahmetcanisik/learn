export interface ProjectsOptions {
    id: string;
    name: string;
    version: string;
    description: string;
    author: string;
    homepage: string;
    repository: string;
}

export const projects: ProjectsOptions[] = [
    {
        id: "guessing",
        name: "Guessing",
        version: "0.1.1",
        description: "Guess the secret number and you win!",
        author: "ahmetcanisik",
        homepage: "ahmetcanisik.com",
        repository: "https://github.com/ahmetcanisik/learn/tree/main/rust/with/projects/guessing"
    }
]