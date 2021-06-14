/*
  Create an array of 'pet' objects.
  Each object should have the following properties: 
  name, type, breed, age, and photo
*/

let pets = [
  {name: 'Abby', type: 'dog', breed: 'Australian Shepherd' , age: 2, photo: 'img/aussie.jpg'},
  {name: 'Georgia', type: 'dog', breed: 'Dachshund' , age: 7, photo: 'img/dachshund.jpg'},
  {name: 'Bully', type: 'dog', breed: 'Golden Retriever' , age: 5, photo: 'img/golden.jpg'},
  {name: 'Ben', type: 'cat', breed: 'Persian' , age: 2, photo: 'img/persian.jpg'},
  {name: 'Tom', type: 'dog', breed: 'Pug' , age: 12, photo: 'img/pug.jpg'},
  {name: 'Tatl', type: 'cat', breed: 'Tabby' , age: 4, photo: 'img/tabby.jpg'}
];

let html = '';

for (let i=0; i < pets.length; i++) {
 
  html += `<h2>${pets[i].name}</h2><h3>${pets[i].type} | ${pets[i].breed}</h3<p>Age: ${pets[i].age}</p><img src="${pets[i].photo}" alt="${pets[i].breed}">`;

}

document.querySelector('main').innerHTML = html;