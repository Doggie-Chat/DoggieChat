// generate a random number between 1 and 100
const randomNumber = Math.floor(Math.random() * 100) + 1;

// get elements from the HTML document
const guessInput = document.getElementById('guessInput');
const guessButton = document.getElementById('guessButton');
const resultMessage = document.createElement('p');
resultMessage.className = 'resultMessage'; // add a class name
const guessGame = document.querySelector('.guess-game');
guessGame.appendChild(resultMessage);


// add an event listener to the guess button
guessButton.addEventListener('click', function() {
	// get the user's guess
	const userGuess = parseInt(guessInput.value);

	// check if the user's guess is correct
	if (userGuess === randomNumber) {
		resultMessage.textContent = 'Congratulations! Correct.';
		resultMessage.style.color = '#32CD32'; // LimeGreen
	} else if (userGuess < randomNumber) {
		resultMessage.textContent = 'Too low! Guess again.';
		resultMessage.style.color = '#ff00bb'; // Pink
	} else if (userGuess > randomNumber) {
		resultMessage.textContent = 'Too high! Guess again.';
		resultMessage.style.color = '#ff00bb'; // Pink
	}

	// clear the input field
	guessInput.value = '';
});
