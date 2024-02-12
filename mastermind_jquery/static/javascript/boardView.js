const API_URL = 'http://127.0.0.1:5000';

/**
 * API call: POST request to reset the game.
 * @returns The response JSON.
 */
async function apiReset() {

}


/**
 * API call: POST request to get the guesses.
 * @returns The response JSON.
 */
async function apiGuesses() {

}

/**
* API call: POST request to make a guess.
* @returns The response JSON.
*/
async function apiGuess() {

async function guess() {

}

/**
 * Updates the board.
 */
async function updateBoard() {
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
}

/**
 * This function is ran when the webpage first loads.
 */
$(async function () {

})