/*
  Task 5: List of Elements
  - Add a <li> element to a list when the user clicks on the tag DIV#add_item.
  - The new element must be: <li>Item</li>.
  - The new element must be added to UL.my_list.
  - Use the JQuery API.
  - Ensure the script runs after the DOM has fully loaded.
*/

document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('add_item').addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    document.querySelector('.my_list').appendChild(newItem);
  });
});
