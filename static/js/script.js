
function search_url() {
  var search_str = $('#search').val()
  if( ( search_str == '0' || search_str == '' || search_str == 'undefined' || search_str == null ) ){
    alert("Please provide search string");
  }else{
    $.ajax({
          url: 'http://localhost:5000/search',
           dataType: 'json',
           type: 'post',
           contentType: 'application/json',
           data: JSON.stringify({ "query_str" :  search_str}),
           success: function( data, textStatus, jQxhr ){
                for (var item = 0; item < data['urls'].length; item++) {
                  $('table>tbody').append(`<tr><td> <a href="${data['urls'][item]['url']}">${data['urls'][item]['url']}</a></td><td>${data['urls'][item]['creation_date']}</td><td>${data['urls'][item]['visited']}</td></tr>`)
                }
                $('table').show()
           },
           error: function( jqXhr, textStatus, errorThrown ){
               console.log( errorThrown );
           }
       });
  }
}

$("#url_forn").submit(function(e) {
    $('#orgurlp').html($('#url').val())
    e.preventDefault();
});
