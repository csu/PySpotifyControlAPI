$( document ).ready(function() {
    'use strict';

    var $context = $('#wrapper');
    var $recommendations = $context.find('#content');
    $recommendations = $recommendations.find('#lower');
    $recommendations = $recommendations.find('#recommendations');
    var $artist = $context.find('#artist');
    var $findTracks = $context.find('#findTracks');
    var $artistSearch = $context.find('#artistSearch');

    $artist.focus();

    $('#artist').on('input', function(e) {
      $recommendations.empty();
      var text = $(this).val();
      console.log(text);
      $.getJSON("http://ws.spotify.com/search/1/track.json?q="+text,function(result) {
        if (result.tracks.length > 0) {
          var tracksLength = result.tracks.length,
              html = '';
          for (var i=0;i<tracksLength;i++) { 
            if ((result.tracks[i].album.availability.territories.indexOf(' US ') !== -1) || (result.tracks[i].album.availability.territories.indexOf('MX US') !== -1) || (result.tracks[i].album.availability.territories.indexOf('US') !== -1)) {
              html+='<li class="results"><a href="/play/' + result.tracks[i].href + '">' + result.tracks[i].artists[0].name + ' - ' + result.tracks[i].name + '</a></li>';
            }
          }
          $recommendations.append(html);
        } else {
          $recommendations.append('<li>No matches returned for \'' + text + '\'</li>');
        }
      });
    });
});