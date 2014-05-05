$( document ).ready(function() {
  $.getJSON("http://embed.spotify.com/oembed/?url={{ songURI }}", function(result) {
    var album_art_id = result['thumbnail_url'].substr(href.lastIndexOf('/') + 1);
    var album_art_url = "https://d3rt1990lpmkn.cloudfront.net/unbranded/" + album_art_id;
    $("#album_art").attr("src", album_art_url);
  });
});