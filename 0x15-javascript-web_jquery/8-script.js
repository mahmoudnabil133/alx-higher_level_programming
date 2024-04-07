$(document).ready(function() {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data)=>{
    felms = data.results;
    for (felm of felms) {
      const tit = felm.title;
      $('#list_movies').append(`<li>${tit}</li>`)
    }
  })
})
