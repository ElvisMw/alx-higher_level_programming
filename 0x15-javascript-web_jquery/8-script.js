/*
  Task 8: Star Wars Movies
  - Fetch and list the title for all movies using the URL: https://swapi-api.alx-tools.com/api/films/?format=json.
  - All movie titles must be listed in the HTML tag UL#list_movies.
  - Use the JQuery API.
  - Ensure the script runs after the DOM has fully loaded.
*/

document.addEventListener('DOMContentLoaded', function () {
  fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      const moviesList = document.querySelector('#list_movies');
      data.results.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        moviesList.appendChild(listItem);
      });
    });
});
