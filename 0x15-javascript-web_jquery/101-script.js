$(document).ready(()=>{
  const list = '<li>item</li>'
  $('#add_item').click(()=>{
    $('.my_list').append(list)
  })
  $('#remove_item').click(()=>{
    $('.my_list li:last-child').remove()
  })
  $('#clear_list').click(()=>{
    $('.my_list').empty()
  })
})
