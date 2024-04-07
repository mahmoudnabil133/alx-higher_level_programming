$(document).ready(function() {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data)=>{
    const hello = data.hello;
    $('#hello').text(hello)
  })
})
