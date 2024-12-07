const listMoviesElement = document.querySelector('#list_movies');

if (listMoviesElement) {
  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok.');
      }
      return response.json();
    })
    .then(data => {
      const movies = data.results;

      if (Array.isArray(movies)) {
        movies.forEach(movie => {
          const listItem = document.createElement('li');
          listItem.textContent = movie.title;
          listMoviesElement.appendChild(listItem);
        });
      } else {
        console.warn('No movies found in the response.');
      }
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
} else {
  console.warn('Element #list_movies not found.');
}
