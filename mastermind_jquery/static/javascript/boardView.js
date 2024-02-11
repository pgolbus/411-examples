const API_URL = 'http://127.0.0.1:5000';

/**
 * API call: POST request to reset the game.
 * @returns The response JSON.
 */
async function apiReset() {
    var url = API_URL + '/reset';

    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    });

    console.log('API call: /reset');
    var data = await response.json();

    return data;
}


/**
 * API call: POST request to get the guesses.
 * @returns The response JSON.
 */
async function apiGuesses() {
    var url = API_URL + '/guesses';
    console.log(url);
    const response = await fetch(url, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    });

    console.log('API call: /guesses');
    var data = await response.json();
    console.log(data);

    return data;
}

/**
* API call: POST request to make a guess.
* @returns The response JSON.
*/
async function apiGuess() {
    var url = API_URL + '/guess?';
    
    var guessRow = $('#selectTable tr:eq(1)');
    var colors = guessRow.find('select').map(function() {
        return $(this).val();
    }).get();

    // Iterate over the colors array to append each color as a query parameter
    colors.forEach(function(color, index) {
        // Append 'color1=value', 'color2=value', etc., to the URL
        // Note: index + 1 is used because array indexes start at 0 but we want color1, color2, ...
        url += 'color' + (index + 1) + '=' + encodeURIComponent(color);
        // If not the last item, add an '&' to separate query parameters
        if (index < colors.length - 1) {
            url += '&';
        }
    });

    console.log(url);

    const response = await fetch(url, {
        method: 'GET',
        headers: {
           'Accept': 'application/json',
           'Content-Type': 'application/json'
        }
    });

   console.log('API call: /guess');
   var data = await response.json();
   console.log(data);

   return data;
}

async function guess() {
    await apiGuess();
    await updateBoard();
}

/**
 * Updates the board.
 */
async function updateBoard() {
    var data = await apiGuesses();
    console.log(data);
    var guesses = data['guesses'];

    var $tableElm = $("#guessesTable");
    // Clear all rows except the first one (assuming it's a header)
    $("tr:gt(0)", $tableElm).remove(); // Selects all tr elements greater than index 0 and removes them

    // Add all entries in the guesses array as rows to the table
    guesses.forEach(function(guess, guessIndex) {
        var rowHtml = '<tr><td>' + (guessIndex + 1) + '</td>'; // Start the row
        guess.forEach(function(color, colorIndex) {
            if (colorIndex < SIZE) {
                rowHtml += '<td style="background: ' + PATTERN_COLORS[color] + ';"></td>'; // Add cells to the row
            } else {
                rowHtml += '<td>' + color + '</td>'; // Add result cells to the row
            }
        });
        rowHtml += '</tr>'; // Close the row
        $tableElm.append(rowHtml); // Append the row
        if (data['win']) {
            $('#endGameDiv').text('You won in ' + data['guess_count'] + ' guesses!');
            $('#selectDiv').hide();
        } else if (data['lose']) {
            $('#endGameDiv').text('You lose!');
            $('#selectDiv').hide();
        }
    });
    
}

/**
 * Resets the game.
 */
async function reset() {
    $('#endGameDiv').text("");
    $('#selectDiv').show();
    await apiReset();
    await updateBoard();
}

/**
 * This function is ran when the webpage first loads.
 */
$(async function () {
    $("#resetButton").click(reset);
    $("#guessButton").click(guess);
})