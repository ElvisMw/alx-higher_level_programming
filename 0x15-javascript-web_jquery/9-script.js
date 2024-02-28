/*
  Task 9: Say Hello!
  - Fetch and display a greeting from the URL: https://hellosalut.stefanbohacek.dev/?lang=fr.
  - Display the greeting in the HTML tag DIV#hello.
  - Use the JQuery API.
  - Ensure the script runs after the DOM has fully loaded.
*/

document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      document.querySelector('#hello').textContent = data.hello;
    });
});
