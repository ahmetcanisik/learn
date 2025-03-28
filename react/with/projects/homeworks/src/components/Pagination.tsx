'use client';
import '@/styles/pagination.css';
import { GitHubRepo } from '@/server/fetch';
import { useEffect, useState } from 'react';

interface PaginationType {
    data: GitHubRepo[] | null;
    activeRepo: string;
    onRepoChange: (repo: string) => void;
}

function Pagination({
    activeRepo,
    data,
    onRepoChange
}: PaginationType) {
    const [prev, setPrev] = useState<GitHubRepo | undefined>(undefined);
    const [next, setNext] = useState<GitHubRepo | undefined>(undefined);

    useEffect(() => {
        if (data && activeRepo) {
            const activeIndex = data.findIndex(repo => repo.full_name.toLowerCase() === activeRepo);
            setPrev(activeIndex > 0 ? data[activeIndex - 1] : undefined);
            setNext(activeIndex < (data.length - 1) ? data[activeIndex + 1] : undefined);
        }
    }, [data, activeRepo]);

    return (
        <div className="pagination">
            {prev && <button className='pagination-btn prev' onClick={() => onRepoChange(prev.full_name)}>{prev.name}</button>}
            {next && <button className='pagination-btn next' onClick={() => onRepoChange(next.full_name)}>{next.name}</button>}
        </div>
    );
}

export default Pagination;