/*
  Task 3: Add `.red` Class
  - Add the class red to the <header> element when the user clicks on the tag DIV#red_header.
  - Use the JQuery API.
  - Ensure the script runs after the DOM has fully loaded.
*/

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('red_header').addEventListener('click', function () {
    document.querySelector('header').classList.add('red');
  });
});
