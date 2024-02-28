/*
  Task 4: Toggle Classes
  - Toggle the class of the <header> element when the user clicks on the tag DIV#toggle_header.
  - The <header> element must always have one class: red or green, never both and never empty.
  - Use the JQuery API.
  - Ensure the script runs after the DOM has fully loaded.
*/

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('toggle_header').addEventListener('click', function () {
    const header = document.querySelector('header');
    header.classList.toggle('red');
    header.classList.toggle('green');
  });
});
