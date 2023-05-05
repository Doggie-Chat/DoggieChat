
// This typing.js is used to show the typewriter effect on texts
// An array of text to display
const texts = ['Talk to Your Pooch, Anytime!','Unleash the Conversation with Your Furry Friend!','Connect with AI-Powered Doggie!'];

// Initialize variables
let count = 0;
let index = 0;
let currentSentence = '';
let currentLetter = '';

// Function to create a delay
function sleep(delay){
    return new Promise(resolve => setTimeout(resolve,delay));
}

// Function to type write the text
const typeWrite = async() => {
  // Check if all the text has been displayed, reset count if true
  if (count == texts.length) {
    count = 0;
  }

  // Get the current sentence to display
  currentSentence = texts[count];

  // Get the current letter of the word and display it
  currentLetter = currentSentence.slice(0,++index);
  document.querySelector(".typing").textContent = currentLetter;

  // Check if all letters of the word have been displayed, pause for a bit
  if(index == currentSentence.length) {
    await sleep(1500);

    // Remove the displayed letters one by one
    while(index > 0) {
      currentLetter = currentSentence.slice(0,--index);
      document.querySelector(".typing").textContent = currentLetter;
      await sleep(50);
    }

    // Move to the next word and reset the index
    count++;
    index = 0;

    // Pause for a bit before typing the next word
    await sleep(500);
  }

  // Call the function again with a random delay
  setTimeout(typeWrite, Math.random() * 200 + 50);
}

// Call the function to start typing the text
typeWrite();




/*
const texts = ['Talk to Your Pooch, Anytime!','Unleash the Conversation with Your Furry Friend!','Connect with AI-Powered Doggie!'];
var count = 0;
var index = 0;
var decrement = 0;
var currentText = '';
var letter = '';

function sleep(delay){
    return new Promise(resolve => setTimeout(resolve,delay));
}

const typeWrite = async() =>{
  if (count == texts.length)
  {
    count = 0;
  }
  currentWord = texts[count];
  currentLetter = currentWord.slice(0,++index);
  document.querySelector(".typing").textContent = currentLetter;
  if(index == currentWord.length)
  {
    await sleep(1500);
    while(index > 0)
    {
      currentLetter = currentWord.slice(0,--index);
      document.querySelector(".typing").textContent = currentLetter;
      await sleep(50);
    }
    count++;
    index = 0;
    await sleep(500);
  }
  setTimeout(typeWrite,Math.random()*200+50);
}
typeWrite();
=======
// This typing.js is used to show the typewriter effect on texts
// An array of text to display
const texts = ['Talk to Your Pooch, Anytime!','Unleash the Conversation with Your Furry Friend!','Connect with AI-Powered Doggie!'];

// Initialize variables
let count = 0;
let index = 0;
let currentSentence = '';
let currentLetter = '';

// Function to create a delay
function sleep(delay){
    return new Promise(resolve => setTimeout(resolve,delay));
}

// Function to type write the text
const typeWrite = async() => {
  // Check if all the text has been displayed, reset count if true
  if (count == texts.length) {
    count = 0;
  }

  // Get the current sentence to display
  currentSentence = texts[count];

  // Get the current letter of the word and display it
  currentLetter = currentSentence.slice(0,++index);
  document.querySelector(".typing").textContent = currentLetter;

  // Check if all letters of the word have been displayed, pause for a bit
  if(index == currentSentence.length) {
    await sleep(1500);

    // Remove the displayed letters one by one
    while(index > 0) {
      currentLetter = currentSentence.slice(0,--index);
      document.querySelector(".typing").textContent = currentLetter;
      await sleep(50);
    }

    // Move to the next word and reset the index
    count++;
    index = 0;

    // Pause for a bit before typing the next word
    await sleep(500);
  }

  // Call the function again with a random delay
  setTimeout(typeWrite, Math.random() * 200 + 50);
}

// Call the function to start typing the text
typeWrite();




/*
const texts = ['Talk to Your Pooch, Anytime!','Unleash the Conversation with Your Furry Friend!','Connect with AI-Powered Doggie!'];
var count = 0;
var index = 0;
var decrement = 0;
var currentText = '';
var letter = '';

function sleep(delay){
    return new Promise(resolve => setTimeout(resolve,delay));
}

const typeWrite = async() =>{
  if (count == texts.length)
  {
    count = 0;
  }
  currentWord = texts[count];
  currentLetter = currentWord.slice(0,++index);
  document.querySelector(".typing").textContent = currentLetter;
  if(index == currentWord.length)
  {
    await sleep(1500);
    while(index > 0)
    {
      currentLetter = currentWord.slice(0,--index);
      document.querySelector(".typing").textContent = currentLetter;
      await sleep(50);
    }
    count++;
    index = 0;
    await sleep(500);
  }
  setTimeout(typeWrite,Math.random()*200+50);
}
typeWrite();
>>>>>>> 095ad4b44631c2c0d9e04bef59bb91a44ebb4bc0
*/