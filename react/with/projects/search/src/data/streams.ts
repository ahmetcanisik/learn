export interface StreamsType {
  title: string;
  directors: string[];
  release_year: number;
  genre: string;
  rating: number;
  type: string;
}

interface RatingType {
  Source: string;
  Value: string;
}

export interface OMDBResponseType {
  Title: string;
  Year: string;
  Rated: string;
  Released: string;
  Runtime: string;
  Genre: string;
  Director: string;
  Writer: string;
  Actors: string;
  Plot: string;
  Language: string;
  Country: string;
  Awards: string;
  Poster: string;
  Ratings: RatingType[];
  Metascore: string;
  imdbRating: string;
  imdbVotes: string;
  imdbID: string;
  Type: string;
  DVD: string;
  BoxOffice: string;
  Production: string;
  Website: string;
  Response: string;
}

export async function searchStream(q: string): Promise<OMDBResponseType | undefined> {
  const apiKey = "831e14b7";
  const res = await fetch(`https://www.omdbapi.com/?t=${q}&apikey=${apiKey}`);

  if (res.ok) {
    const data: OMDBResponseType = await res.json();

    return data;
  }

  return undefined;
}

export const streams: StreamsType[] = [
  {
    title: "Inception",
    directors: ["Christopher Nolan"],
    release_year: 2010,
    genre: "Science Fiction",
    rating: 8.8,
    type: "movie",
  },
  {
    title: "The Godfather",
    directors: ["Francis Ford Coppola"],
    release_year: 1972,
    genre: "Crime",
    rating: 9.2,
    type: "movie",
  },
  {
    title: "The Dark Knight",
    directors: ["Christopher Nolan"],
    release_year: 2008,
    genre: "Action",
    rating: 9.0,
    type: "movie",
  },
  {
    title: "Pulp Fiction",
    directors: ["Quentin Tarantino"],
    release_year: 1994,
    genre: "Crime",
    rating: 8.9,
    type: "movie",
  },
  {
    title: "The Shawshank Redemption",
    directors: ["Frank Darabont"],
    release_year: 1994,
    genre: "Drama",
    rating: 9.3,
    type: "movie",
  },
  {
    title: "Friends",
    directors: ["David Crane", "Marta Kauffman"],
    release_year: 1994,
    genre: "Comedy",
    rating: 8.9,
    type: "series",
  },
  {
    title: "Breaking Bad",
    directors: ["Vince Gilligan"],
    release_year: 2008,
    genre: "Crime",
    rating: 9.5,
    type: "series",
  },
  {
    title: "Game of Thrones",
    directors: ["David Benioff", "D.B. Weiss"],
    release_year: 2011,
    genre: "Fantasy",
    rating: 9.3,
    type: "series",
  },
  {
    title: "The Office",
    directors: ["Greg Daniels"],
    release_year: 2005,
    genre: "Comedy",
    rating: 8.8,
    type: "series",
  },
];
