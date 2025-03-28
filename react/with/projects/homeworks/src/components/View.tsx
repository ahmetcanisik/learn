'use client';
import { MarkdownRenderer } from './MarkdownRenderer';
import {
    getREADMEForGithub,
    getAllGithubRepositories,
    type GitHubRepo
} from '@/server/fetch';
import { useEffect, useState } from 'react';
import Pagination from './Pagination';

export function ViewGithubRepos({ username }: { username: string; }) {
    const [activeRepo, setActiveRepo] = useState<string | null>(null);
    const [repos, setRepos] = useState<GitHubRepo[] | null>(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        getAllGithubRepositories(username)
            .then((repoitories) => {
                if (repoitories) {
                    setActiveRepo(repoitories[0].full_name);
                    setRepos(repoitories);
                } else {
                    setError(`${username}'s github repositories are not found!`);
                }
                setLoading(false);
            })
            .catch((err) => {
                setError(err);
                setLoading(false);
            });
    }, [username]);

    if (loading) {
        return (
            <div>Loading...</div>
        );
    }

    if (error && !activeRepo) {
        return (
            <div style={{ color: 'red', padding: '1rem' }}>{error}</div>
        );
    }

    return (
        <div style={{ display: 'flex', minHeight: '100vh' }}>
            <div style={{ width: '30%' }}>
                <h2>{username} repos</h2>
                {(repos && repos.length) && <h3>total repositories: {repos.length}</h3>}
                <input type="text" placeholder='Search repositories' />
                <div className='list-repos' key="user-repos-list-1">
                    {
                        repos && repos.map((repo: GitHubRepo) => (
                            <button className={repo.full_name === activeRepo ? 'active' : ''} onClick={() => setActiveRepo(repo.full_name)} key={repo.full_name}>{repo.name}</button>
                        ))
                    }
                </div>
            </div>
            {
                activeRepo && (
                    <div style={{ width: '70%', padding: '0 40px' }}>
                        <ViewGithubREADME repo={activeRepo} />
                        <Pagination onRepoChange={setActiveRepo} activeRepo={activeRepo} data={repos} />
                    </div>
                )
            }
        </div>
    );
}

export function ViewGithubREADME({ repo }: { repo: string; }) {
    const [baseUrl, setBaseUrl] = useState<string | null>(null);
    const [content, setContent] = useState<string>("");
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        getREADMEForGithub(repo)
            .then((data) => {
                if (data) {
                    setContent(data.README);
                    setBaseUrl(data.baseUrl);
                } else {
                    setError("README.md file was not found!");
                }
                setLoading(false);
            })
            .catch((err) => {
                setError(err instanceof Error ? err.message : "Something went wrong!");
                setLoading(false);
            });
    }, [repo]);

    if (loading) {
        return (
            <div>Loading...</div>
        );
    }

    if (error && !content) {
        return (
            <div style={{ color: 'red', padding: '1rem' }}>{error}</div>
        );
    }

    return (
        <MarkdownRenderer baseUrl={baseUrl ?? ""}>
            {content}
        </MarkdownRenderer>
    );
}