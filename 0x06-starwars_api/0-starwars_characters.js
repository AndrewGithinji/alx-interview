#!/usr/bin/node
// Star Wars Characters
const request = require('request-promise');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

async function getCharacterName(url) {
try {
const characterData = await request(url);
const characterName = JSON.parse(characterData).name;
console.log(characterName);
} catch (error) {
console.log(error);
}
}

async function getFilmCharacters(url) {
try {
const filmData = await request(url);
const film = JSON.parse(filmData);
const characters = film.characters;
for (const characterUrl of characters) {
await getCharacterName(characterUrl);
}
} catch (error) {
console.log(error);
}
}

getFilmCharacters(url);