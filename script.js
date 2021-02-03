// Global Variables

var VIEW = 0;
var NUMBER_OF_JOKES = jokes['joke'].length;
var RANDOM_VALUE = Math.round(Math.random() * (NUMBER_OF_JOKES - 1) + 0);

// Initial Set-up

var JOKES_ARRAY = shuffleArray(jokes['joke']);
var JOKE = JOKES_ARRAY[RANDOM_VALUE];

var LINE_1 = document.getElementById('LINE_1');
var LINE_2 = document.getElementById('LINE_2');
var LINE_3 = document.getElementById('LINE_3');
var LINE_4 = document.getElementById('LINE_4');

var BUTTON_1 = document.getElementById('VIEW_1_BUTTON');
var BUTTON_2 = document.getElementById('VIEW_2_BUTTON');

var CONTAINER_1 = document.getElementById('CONTAINER_1');
var CONTAINER_2 = document.getElementById('CONTAINER_2');

LINE_1.innerHTML = JOKE['setup'];
LINE_2.innerHTML = JOKE['punchline'];

var VIEW_1 = document.getElementById('VIEW_1');
var VIEW_2 = document.getElementById('VIEW_2');
var SECTION = document.getElementById('SECTION');

// Refresh Content

function refreshContent() 
{

    if(VIEW == 0)
    {

        RANDOM_VALUE = Math.round(Math.random() * (NUMBER_OF_JOKES - 1) + 0);
        JOKES_ARRAY = shuffleArray(jokes['joke']);
        JOKE = JOKES_ARRAY[RANDOM_VALUE];

        CONTAINER_1.style.opacity = '0';

        var MILLISECONDS = 500;
        
        setTimeout(function() {

            LINE_1.innerHTML = JOKE['setup'];
            LINE_2.innerHTML = JOKE['punchline'];

            CONTAINER_1.style.opacity = '1';

        }, MILLISECONDS);

    }

    if(VIEW == 1)
    {

        VIEW_2.style.opacity = '0';

        var MILLISECONDS = 500;
        
        setTimeout(function() {

            JOKES_ARRAY = shuffleArray(JOKES_ARRAY);

            for(var i = 0; i < NUMBER_OF_JOKES; i += 1)
            {

                JOKE = JOKES_ARRAY[i];

                var CARD = document.createElement('DIV');
                var DIV = document.createElement('DIV');
                var NEW_LINE_1 = document.createElement('SPAN');
                var NEW_LINE_2 = document.createElement('SPAN');

                CARD.setAttribute('id', 'CARD');
                NEW_LINE_1.setAttribute('id', 'LINE_3');
                NEW_LINE_2.setAttribute('id', 'LINE_4');

                DIV.appendChild(NEW_LINE_1);
                DIV.appendChild(NEW_LINE_2);
                CARD.appendChild(DIV);

                NEW_LINE_1.innerHTML = JOKE['setup'];
                NEW_LINE_2.innerHTML = `  ${JOKE['punchline']}`;

                CONTAINER_2.appendChild(CARD);

            }

            VIEW_2.style.opacity = '1';

        }, MILLISECONDS);


    }

}

function changeToView1()
{
    if(VIEW != 0)
    {

        VIEW = 0;

        BUTTON_1.style.color = '#21222775';
        BUTTON_2.style.color = '#21222725';

        refreshContent();

        VIEW_2.style.opacity = '0.0';

        var MILLISECONDS = 500;
        
        setTimeout(function() {

            SECTION.style.overflow = 'hidden';
            SECTION.style.height = 'calc(100vh)';

            VIEW_1.style.opacity = '1.0';

        }, MILLISECONDS);

    }
}

// Change to View 2

function changeToView2()
{
    if(VIEW != 1)
    {

        VIEW = 1;

        BUTTON_1.style.color = '#21222725';
        BUTTON_2.style.color = '#21222775';

        refreshContent();

        VIEW_1.style.opacity = '0.0';

        var MILLISECONDS = 500;
        
        setTimeout(function() {

            SECTION.style.overflow = 'auto';
            SECTION.style.height = 'calc(100vh + 125px)';

            VIEW_2.style.opacity = '1.0';

        }, MILLISECONDS);

    }
}

function shuffleArray(array) {

    var current_index = array.length, temporary_value, random_index;
  
    while (0 !== current_index) {
  
        random_index = Math.floor(Math.random() * current_index);
        current_index -= 1;
  
        temporary_value = array[current_index];
        array[current_index] = array[random_index];
        array[random_index] = temporary_value;

    }
  
    return array;

}