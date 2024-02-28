/*
  Task 12: Say Hello to Everybody!
  - Fetch and display a multilingual greeting based on user-selected language.
  - Use the JQuery API.
  - Ensure the script runs after the DOM has fully loaded.
*/

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('btn_translate').addEventListener('click', function () {
    const languageCode = document.getElementById('language_code').value;
    fetch(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`)
      .then(response => response.json())
      .then(data => {
        document.querySelector('#hello').textContent = data.hello;
      });
  });
});
