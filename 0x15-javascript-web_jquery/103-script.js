/*
  Task 13: And Press ENTER
  - Fetch and display a multilingual greeting based on user-selected language.
  - Enable the user to press ENTER to trigger the translation.
  - Use the JQuery API.
  - Ensure the script runs after the DOM has fully loaded.
*/

document.addEventListener('DOMContentLoaded', function () {
  const translateButton = document.getElementById('btn_translate');
  const languageCodeInput = document.getElementById('language_code');

  const translateHello = function () {
    const languageCode = languageCodeInput.value;
    fetch(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`)
      .then(response => response.json())
      .then(data => {
        document.querySelector('#hello').textContent = data.hello;
      });
  };

  translateButton.addEventListener('click', translateHello);
  languageCodeInput.addEventListener('keyup', function (event) {
    if (event.key === 'Enter') {
      translateHello();
    }
  });
});
