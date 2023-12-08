#!/usr/bin/node
const request = require('request');
const URI = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(URI, function (error, _, body) {
  if (!error) {
    const charactersURI = JSON.parse(body).characters;
    getCharacters(charactersURI, 0);
  } else {
    console.error(error);
  }
});

function getCharacters (character, id) {
  request(character[id], function (error, _, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (id + 1 < character.length) {
        getCharacters(character, id + 1);
      } else {
        console.error(error);
      }
    }
  });
}
