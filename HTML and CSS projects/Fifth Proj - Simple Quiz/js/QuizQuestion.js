var com;
if(!com) {
    com = {};
}
if(!com.williamdominic) {
    com.williamdominic = {};
}

com.williamdominic.QuizQuestion = function(aQuestionNum, aQuestionText, aAnswers, aCorrectAnswerIndex) {

this.questionNum = aQuestionNum;
this.questionText = aQuestionText;
this.answers = aAnswers;
this.correctAnswerIndex = aCorrectAnswerIndex;
}

com.williamdominic.QuizQuestion.prototype.checkUserAnswer = function(answerIndex) {
    var theResult = false;
    if(this.questionAnswered) {
        alert("You've already answered this question");
    } else if(answerIndex == this.correctAnswerIndex) {
        this.answeredCorrectly = true;
        document.getElementById("q" + this.questionNum).className = "correctlyAnswered";
        theResult = true;
    } else {
        document.getElementById("q" + this.questionNum).className = "incorrectlyAnswered";
    }
    this.questionAnswered = true;
    return(theResult);
}

com.williamdominic.QuizQuestion.prototype.renderQuestion = function() {
   var questionDiv = document.createElement("div");
   questionDiv.id = "q" + this.questionNum;
   var questionHeading = document.createElement("h2");
   questionHeading.innerHTML = "QUESTION " + this.questionNum;
   questionDiv.appendChild(questionHeading);
   var questionTextPara = document.createElement("p");
   questionTextPara.innerHTML = this.questionText;
   questionDiv.appendChild(questionTextPara);
   for(var i = 0; i < this.answers.length; i++) {
    var answerPara = document.createElement("p");
    answerPara.innerHTML = this.answers[i];
    answerPara.id = "a" + i;
    questionDiv.appendChild(answerPara);
   }
   document.body.appendChild(questionDiv);
}