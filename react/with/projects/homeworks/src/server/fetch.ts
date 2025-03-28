export interface GitHubRepo {
    name: string;
    full_name: string;
}

export async function getREADMEForGithub(githubRepo: string): Promise<{ README: string; baseUrl: string; } | null> {
    try {
        const [repo, branch] = githubRepo.trim().indexOf(":") !== -1 ? githubRepo.trim().split(":") : [githubRepo.trim(), "main"];

        if (!branch || !repo) {
            throw new Error("Please specify the <owner>/<repo>:<branch> like this cli/cli:main");
        }

        const file = "README.md";
        const url = `https://raw.githubusercontent.com/${repo}/refs/heads/${branch}`;

        let res = await fetch(`${url}/${file}`);

        if (res.status === 404) {
            res = await fetch(`${url}/${file.toLowerCase()}`);
        }

        if (!res.ok) {
            throw new Error(`${repo} response status is ${res.status}, ${res.statusText}`);
        }

        const README = await res.text();

        if (!README) {
            throw new Error("README.md file was not found!");
        }

        return {
            README: README,
            baseUrl: url
        };
    } catch (err: unknown) {
        if (err instanceof Error) {
            throw err;
        }
        throw new Error("Failed to fetch README.md");
    }
}

export async function getAllGithubRepositories(username: string): Promise<GitHubRepo[]> {
    try {
        const res = await fetch(`https://api.github.com/users/${username}/repos`);

        if (!res.ok) {
            throw new Error(`Response status is ${res.status}, ${res.statusText}`);
        }

        const repos = await res.json();

        if (!repos) {
            throw new Error("README.md file was not found!");
        }

        const collectRepos = repos.filter((repo: GitHubRepo) => ({
            name: repo.name,
            full_name: repo.full_name,
        }));

        return collectRepos;
    } catch (err: unknown) {
        if (err instanceof Error) {
            throw err;
        }
        throw new Error("Failed to fetch README.md");
    }
}