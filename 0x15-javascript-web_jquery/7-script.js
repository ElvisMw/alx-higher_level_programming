/*
  Task 7: Star Wars Character
  - Fetch the character name from the URL: https://swapi-api.alx-tools.com/api/people/5/?format=json.
  - Display the name in the HTML tag DIV#character.
  - Use the JQuery API.
  - Ensure the script runs after the DOM has fully loaded.
*/

document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('#character').addEventListener('click', function () {
    fetch('https://swapi-api.alx-tools.com/api/people/5/?format=json')
      .then(response => response.json())
      .then(data => {
        document.querySelector('#character').textContent = data.name;
      });
  });
});
