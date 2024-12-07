const characterElement = document.querySelector('#character');

if (characterElement) {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
      characterElement.textContent = data.name;
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
} else {
  console.warn('Element #character not found.');
}
