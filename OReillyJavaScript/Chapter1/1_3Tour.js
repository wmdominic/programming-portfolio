// Anything following double slashes is an English-language comment.
// Read the comments carefully: they explain the JavaScript code.

// A variable is a symbolic name for a value
// Variables are declared with the 'let' keyword:
let x;                  // Declare a variable names x.
// Values can be assigned to variables with an = sign
x = 0;                  // Now the variable x has a value of 0.
x                       // => 0: A variable evaluates to its value.

// JavaScript supports several types of values:
x = 1;               //Numbers.
x = 0.01;            //Numbers can be integers or reals.
x = "hello world";   //Strings of text in quotation marks.
x = 'JavaScript';    //Single quote marks can also delimit strings.
x = true;            //A boolean value.
x = false;           //Another boolean value.
x = null;            //Null is a special value that means "no value."
x = undefined;       //Undefined is another special value like null.

// JavaScript's most important datatype is the object.
// An object is a collection of name/value pairs, or a string to value map.
let book = {                    //Objects are enclosed in curly braces.
    topic: "JavaScript",        //The property "topic" has the value "JavaScript"
    edition: 7                  //the property "edition" has the value 7.
};

//Access properties of an object with . or []:
book.topic
book["edition"]
book.author = "Flannegan";      //Create new properies by assignment.
book.contents = {};             //{} is an empty object with no properties.

//Conditionally access properties with ?. (ES2020):
book.contents?.ch01?.sect1 // => undefined: book.contents has no ch01 preperty.

//JavaScript also supports arrays (numerically indexed lists) of values.
let primes = [2, 3, 5, 7]; //An array of 4 values, delimited with [ and ].
primes[0]                   //=> 2: the first element (index 0) of the array.
primes.length               //=> 4: how many elements in the array.
primes[primes.length-1]     //=> 7: the last element of the array.
primes[4] = 9;              //Add a new element by assignment.
primes[4] = 11;             //Or alter an existing element by assignment.
let empty = [];             //[] is an empty array with no elements.
empty.length                //=> 0

//Arrays and objects can hold other arrays and objects:
let points = [
    {x: 0, y: 0},           //An array with 2 elements.
    {x: 1, y: 1}            //Each element is an object.
];
let data = {                //An object with 2 properties  
    trial1: [[1,2], [3,4]], //The value of each property is an array.
    trial2: [[2,3], [4,5]]  //The elements of the arrays are arrays.
}                                   //You have an object, "let data," with two properties, "trial1 and trial2," which are both arrays, within each of the arrays, the elements of the arrays are more arrays ([1,2] and [3,4] are arrays within an array.)

//An expression is a phrase of Javascript than can be evaluated to produce a value.
//For example, the use of . and [] to refer to the value of an object property or array element is an expression

_____________________________________________________________________________________________________________________________
//OPERATORS:

//Operators act on values (the operands) to produce a new value.
// Arithmatic operators are some of the simplest:
3 + 2
3 - 2
3 * 2
3 / 2
points[1].x - points[0].x  //=> 1: more complicated operands also work
"3" + "2"                   //=> "32": + adds numbers, concatenates strings

//JavaScript defines some shorthand atrithmetic operators
let count = 5;
count++;            //increment
count--;            //decrement
count += 2;         //add 2: same as count = count + 2; 
count *= 3;         //multiply by 3: same as count = count * 3;
count               //variable names are expressions too

//Equality and relational operators test whether two values are equal, unequal, less than, greater than, and so on. They evaluate to true or false.
let x = 1, y = 5;
x === y                 //equality
x !== y                 //inequality
x < y                   //less-than
x <= y                  //less-than or equal to
x > y                   //greater-than
x >= y                  //greater-than or equal to
"two" === "three"       //false: the two strings are different
"two" > "three"         //true: "tw" is alphabetically greater than "th"
false === (x > y)       //true: false is equal to false

//expressions : phrases :: statements : sentences