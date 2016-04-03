function format_last_track(track) {
    return track.artist + ' - ' + track.title + ' <span class="small">' + track.time_since + ' ago.</span><br />';
}

function format_current_track(track) {
    if($.isEmptyObject(track)) {
        return '<img src="'+ staticFiles.notrack +'" /><br />';
    }

    var html = '';
    if(track.image) {
        html += '<img src="' + track.image +'" class="now_playing" /><br />';
    }
    html += '<img src="'+ staticFiles.spectrumAnalyzer +'" />' + track.artist + ' - ' + track.title +' ♪♫<br />';

    return html;

}

function update_last_track(track) {
    $('#last_track').html(format_last_track(track));
}

function update_current_track(track) {
    $('#now_playing').html(format_current_track(track));

    if( is_tetris_song() ) {
        play_tetris();
    } else {
        dont_play_tetris();
    }
}

/* Update track and now playing */
function get_last_track() {
    $.getJSON(urls.trackLast, function(data) {
        update_last_track(data.track);
    });
}
function get_now_playing() {
    $.getJSON(urls.trackCurrent, function(data) {
        update_current_track(data.track);
    });
}


/***********
 * YOUTUBE *
 ***********/

function other_video_playing(video) {
    var now_playing_pattern = /video.videoId/;

    return ! now_playing_pattern.test( ytplayer.getVideoUrl() );
}

function playVideo(video) {
    if(ytplayer) {
        // start the video (if we have'nt allready)
        if( other_video_playing(video) ) {
            // show the player
            $("#player").show();
            ytplayer.loadVideoById(video.videoId, video.start , "hd720");
        }
    }
}

function showOrHidePlayer(track) {
    if(track.artist == '') {
        $("#player").delay(1000).hide();
    } else {
        if( track.video != '') {
            $("#player").show();
            playVideo(track.video);
        }
    }
}

function onYouTubePlayerAPIReady() {
    /* Initial player */
    new YT.Player('player', {
        width: '1200',
        height: '675',
        videoId: 'dQw4w9WgXcQ', // Mr. Astley?
        playerVars: {
            controls: 0, // no controls
            iv_load_policy: 3, // no annotations
            start: 215 // offset into video (last 2 seconds)
        },
        /* Attach to these events. */
        events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
        }
    });
}

/* The API will call this function when the video player is ready. */
function onPlayerReady(event) {
    ytplayer = event.target;
    event.target.playVideo();
    event.target.mute();
    event.target.setPlaybackQuality("hd720");
}

/* The API calls this function when the player's state changes. */
function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.ENDED) {
        /* Could do something on this state or others... */
    }
}

function createYoutubePlayer() {
    /* Loads the YouTube IFrame Player API code asynchronously. */
    var tag = document.createElement('script');
    tag.src = "https://www.youtube.com/player_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
}

/*********
 * Start *
 *********/
/* Creates an <iframe> (and YouTube player) after the API code downloads. */
var ytplayer;
var urls = {
    trackLast: '/api/track/last/', // {% url 'track-last' %}
    trackCurrent: '/api/track/current/'  // {% url 'track-current' %}
};
var screen_uuid;

/* Initial update */
$( document ).ready( function() {

    // get_last_track();
    // get_now_playing();

    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var socket = new ReconnectingWebSocket(ws_scheme + '://'+ window.location.host +'/screens/');
    socket.onmessage = function(e) {
        console.log(e);
        var data = JSON.parse(e.data);
        if(data && data.track !== undefined) {
            update_current_track(data.track);
        } else if(data && data.screen_consumer !== undefined) {
            console.log(data);
            screen_uuid = data.screen_consumer.uuid;
        }
    };
    socket.onopen = function() {
        // socket.send("hello world");
        console.log("websocket OPEN");
    };
    socket.onclose = function() {
        console.log("websocket closed.");
    };
    socket.onerror = function(e) {
        console.error(e);
    };
    // createYoutubePlayer();
});

/* Start timers updating a screen resource. */
// setInterval(get_last_track, 10000);
// setInterval(get_now_playing, 10000);

/* Ajax spinner */
$( document )
    .ajaxStart(function() {
        $('#spinner').show();
    })
    .ajaxStop( function() {
        $('#spinner').hide();
});
