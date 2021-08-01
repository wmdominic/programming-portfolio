var com;
if(!com) {
    com = {};
}
if(!com.williamdominic) {
    com.williamdominic = {};
}

com.williamdominic.renderQuestionAtIndex = function(questionIndex) {
    document.write("<h2>QUESTION " + (questionIndex + 1) + "</h2>");
    var questionObject = com.williamdominic.questions[questionIndex];
    document.write("<p>" + questionObject.questionText + "</p>");
    document.write("<p>a. " + questionObject.answers[0] + "</p>");
    document.write("<p>b. " + questionObject.answers[1] + "</p>");
    document.write("<p>c. " + questionObject.answers[2] + "</p>");
    document.write("<p>d. " + questionObject.answers[3] + "</p>");
}

com.williamdominic.checkUserAnswer = function(questionIndex, answerIndex) {
    var questionObject = com.williamdominic.questions[questionIndex];
    var theResult;
    if(questionObject.correctAnswerIndex == answerIndex) {
        theResult = true;
    } else {
        theResult = false;
    }
    return(theResult);
}