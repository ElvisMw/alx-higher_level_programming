/*
  Task 6: Change the Text
  - Update the text of the <header> element to New Header!!! when the user clicks on DIV#update_header.
  - Use the JQuery API.
  - Ensure the script runs after the DOM has fully loaded.
*/

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('update_header').addEventListener('click', function () {
    document.querySelector('header').textContent = 'New Header!!!';
  });
});
