const movies = [
    { id: 1, title: "Interstellar", genre: "Sci-Fi", year: 2014, rating: 8.7 },
    { id: 2, title: "Inception", genre: "Sci-Fi", year: 2010, rating: 8.8 },
    { id: 3, title: "The Batman", genre: "Action", year: 2022, rating: 7.9 },
    { id: 4, title: "Titanic", genre: "Drama", year: 1997, rating: 7.8 },
    { id: 5, title: "Oppenheimer", genre: "Biography", year: 2023, rating: 8.5 }
];

const newMovie = { id: 6, title: "Dune", genre: "Sci-Fi", year: 2021, rating: 8.0 };
const updatedMovies = [...movies, newMovie]; 
const topMovies = updatedMovies.filter(movie => movie.rating >= 8);
const firstMovie = movies[0];
const displayText = `${firstMovie.title} (${firstMovie.year}) - Rating: ${firstMovie.rating}`;