$(document).ready(()=>{
  $('#btn_translate').click(()=>{
    const lan = $('#language_code').val()
    url  = 'https://www.fourtonfish.com/hellosalut/hello/' + lan
    $.get(url, (data)=>{
      $('#hello').text(data.hello)
    })
  })
})
