/*
  Task 2: Click and Turn Red
  - Update the text color of the <header> element to red (#FF0000) when the user clicks on DIV#red_header.
  - Use the JQuery API.
  - Ensure the script runs after the DOM has fully loaded.
*/

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('red_header').addEventListener('click', function () {
    document.querySelector('header').style.color = '#FF0000';
  });
});
