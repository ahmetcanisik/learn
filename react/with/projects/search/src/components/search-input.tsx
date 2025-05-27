'use client';
import { useState } from "react";
import { streams, searchStream, type StreamsType } from "../data/streams";

export default function SearchInput({
    items
}: {
    items?: StreamsType[];
}) {
    const [contents, setContents] = useState(items || streams);

    const handleSearch = (e: React.ChangeEvent<HTMLInputElement>) => {
        const searchTerm = e.target.value.toLowerCase();
        const filteredContents = streams.filter((content) => {
            return (
                content.title.toLowerCase().includes(searchTerm) ||
                content.directors.some((director) =>
                    director.toLowerCase().includes(searchTerm)
                ) ||
                content.release_year.toString().includes(searchTerm) ||
                content.genre.toLowerCase().includes(searchTerm) ||
                content.rating.toString().includes(searchTerm) ||
                content.type.toLowerCase().includes(searchTerm)
            );
        });

        if (filteredContents.length === 0) {
            searchStream(searchTerm)
                .then((omdbResponse) => {
                    if (omdbResponse) {
                        const omdbData: StreamsType = {
                            title: omdbResponse.Title,
                            directors: [omdbResponse.Director],
                            release_year: parseInt(omdbResponse.Year),
                            genre: omdbResponse.Genre,
                            rating: parseFloat(omdbResponse.imdbRating),
                            type: omdbResponse.Type
                        };
                        setContents([omdbData]);
                    } else {
                        setContents([]);
                    }
                })
                .catch(() => {
                    setContents([]); // Handle API errors gracefully
                });
        } else {
            setContents(filteredContents);
        }
    }

    return (
        <div>
            <input type="text" id="search" onChange={handleSearch} />
            <div>
                {
                    contents.map((content, index) => (
                        <div key={index}>
                            <h2>{content.title}</h2>
                            <p>Directors: {content.directors.join(", ")}</p>
                            <p>Release Year: {content.release_year}</p>
                            <p>Genre: {content.genre}</p>
                            <p>Rating: {content.rating}</p>
                            <p>Type: {content.type}</p>
                        </div>
                    ))
                }
            </div>
        </div>
    )
}