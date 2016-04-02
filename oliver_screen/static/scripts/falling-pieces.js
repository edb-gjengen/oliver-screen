/* */
function is_tetris_song() {
    var test;
    $("#now_playing").filter(function(){
        test = /Tetris|Korobeiniki/i.test( $(this).text() );
    });
    return test;
}

function play_tetris() {
    /* http://www.webkit.org/blog-files/bricks/ and kak-logos */
    $("#gameContainer").show();
}
function dont_play_tetris() {
    $("#gameContainer").hide();
}

/* Define the number of bricks to be used in the animation */
const NUMBER_OF_BRICKS = 15;

/* 
    Called when the "Falling Bricks" page is completely loaded.
*/
function init()
{
    /* Get a reference to the element that will contain the bricks */
    var container = document.getElementById('brickContainer');
    /* Fill the empty container with new bricks */
    for (var i = 0; i < NUMBER_OF_BRICKS; i++) 
    {
        container.appendChild(createABrick());
    }
}

function randomRotation() {
    var draw = Math.random();
    if(draw <= 0.25) {
        return "deg0";
    } else if(draw <= 0.5) {
        return "deg90";
    } else if(draw <= 0.75) {
        return "deg180";
    } else {
        return "deg270";
    }
}

/*
    Receives the lowest and highest values of a range and
    returns a random integer that falls within that range.
*/
function randomInteger(low, high)
{
    return low + Math.floor(Math.random() * (high - low));
}


/*
   Receives the lowest and highest values of a range and
   returns a random float that falls within that range.
*/
function randomFloat(low, high)
{
    return low + Math.random() * (high - low);
}


/* Receives a number and returns its CSS pixel value. */
function pixelValue(value)
{
    return value + 'px';
}


/* Returns a duration value for the falling animation. */

function durationValue(value)
{
    return value + 's';
}


/* Uses an img element to create each brick. */
function createABrick()
{
    /* Start by creating a wrapper div, and an empty img element */
    var brickDiv = document.createElement('div');
    var image = document.createElement('img');
    
    /* Randomly choose a brick image and assign it to the newly created element */
    /* FIXME: this url should be dynamic */
    image.src = '/static/images/brick' + randomInteger(1, 5) + '.png';
    
    brickDiv.style.top = "-150px";

    /* Position the brick at a random location along the screen */
    brickDiv.style.left = pixelValue(randomInteger(0, 450));

    /* Set a random rotation for the brick */
    /* FIXME: this does'nt work */
    //brickDiv.style.webkitTranslateRotate = randomRotation();
    //brickDiv.className = randomRotation();
    //console.log(brickDiv.style);
    
    /* Set the -webkit-animation-name property with these values */
    brickDiv.style.webkitAnimationName = 'fade, drop';
    
    /* Set the duration for the fade and drop animations */
    var fadeAndDropDuration = durationValue(10.0);
    
    /* Set the -webkit-animation-duration property with these values */
    brickDiv.style.webkitAnimationDuration = fadeAndDropDuration + ', ' + fadeAndDropDuration;

    var brickDelay = durationValue(randomFloat(0, 10));
    brickDiv.style.webkitAnimationDelay = brickDelay + ', ' + brickDelay;

    // add the <img> to the <div>
    brickDiv.appendChild(image);

    /* Return this img element so it can be added to the document */
    return brickDiv;
}


/* Calls the init function when the "Falling Bricks" page is full loaded */
window.addEventListener('load', init, false);
