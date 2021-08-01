var com;
if(!com) {
    com = {};
}
if(!com.williamdominic) {
    com.williamdominic = {};
}

com.williamdominic.SimpleQuiz = function() {
    this.questions = [];
    this.loadQuestions();
}

com.williamdominic.SimpleQuiz.prototype.loadQuestions = function() {
    this.questions.push(
        new com.williamdominic.QuizQuestion(
            1,
            "Where did we go to eat on our first date?",
            ["Olive Garden", "Original Pancake House", "Panara Bread", "Thai food"],
            1
        )
    );
    
    this.questions.push(
        new com.williamdominic.QuizQuestion(
            2,
            "Where did we go with Beatrice and eat Cinnabon?",
            ["Hy-Vee", "Oiginal Pancake House", "Brueggers", "Mall of America"],
            3
        )
    );
    
    this.questions.push(
        new com.williamdominic.QuizQuestion(
            3,
            "On a scale of 0 to 10, how incredibly smart and fucking adorable is Jeremy Krovitz?",
            ["0", "5", "10", "11"],
            3
        )
    );
    
    this.questions.push(
        new com.williamdominic.QuizQuestion(
            4,
            "When is William's Birthday?",
            ["October 2nd", "October 3rd", "October 4th", "October 5th"],
            2
        )
    );
    
    this.questions.push(
        new com.williamdominic.QuizQuestion(
            5,
            "What is one of Jeremy's favorite dishes that William makes for him?",
            ["Spaghetti pie", "Stirfry", "Hotdogs Mashed Potatoes 'N' Cheese", "Frozen Pizza"],
            0
        )
    );
}

com.williamdominic.SimpleQuiz.prototype.renderAllQuestions = function() {
    for(var i = 0; i < this.questions.length; i++) {
        this.questions[i].renderQuestion();
    }
}