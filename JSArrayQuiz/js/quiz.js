// 1. Create a multidimensional array to hold quiz questions and answers
let quizAns = [ ['What is Clara\'s favorite color?','purple'], 
               ['What is Clara\'s favorite animal?','elephant'], 
               ['Who is Clara\'s favorite person?','logan'],
               ['When did Clara find the love of her life?','2015'],
               ['How old is Clara?','28'] ];

// 2. Store the number of questions answered correctly
let correct = 0;

/* 
  3. Use a loop to cycle through each question
      - Present each question to the user
      - Compare the user's response to answer in the array
      - If the response matches the answer, the number of correctly
        answered questions increments by 1
*/
let correctQ = [] ;
let incorrectQ = [];
var ans;
for (let i = 0; i < quizAns.length; i++) {
  ans = prompt(`${quizAns[i][0]}`);
  if (ans.toLowerCase() === quizAns[i][1]) {
    correct++;
    correctQ.push(quizAns[i][0]);
  } else {
    incorrectQ.push(quizAns[i][0]);
  }
}

// 4. Display the number of correct answers to the user
// let correctList ='';
// for ( let i = 0; i < correctQ.length; i++ ) {
//      correctList += `<li>${correctQ[i]}</li>`;
// }
// let incorrectList='';
// for (let i = 0; i < incorrectQ.length; i++) {
//   incorrectList += `<li>${incorrectQ[i]}</li>`;
// }

function createList(arr) {
  let newHTML = '';
  for (let i = 0; i < arr.length; i++) {
    newHTML +=`<li>${arr[i]}</li>`;
  }
  return newHTML;
}

const allCorrect = '<h1>Congratulations! You got ALL the questions correct.</h1>';
let main = document.querySelector('main');
if (incorrectQ.length === 0) {
  main.innerHTML = allCorrect + `<h2>Question Review</h2><br><p>You got these questions right:<ol> ${createList(correctQ)}</ol></p>`;
} else { main.innerHTML = `<h2>You got ${correct} question(s) correct.</h2><br><p>You got these questions right:<ol> ${createList(correctQ)}</ol></p><br><p>You got these questions wrong:<ol>${createList(incorrectQ)}</ol></p>`;
}
