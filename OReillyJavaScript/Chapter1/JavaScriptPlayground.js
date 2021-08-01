let adventurer = {
    name: 'Alice',
    cat: {
        name: 'Dinah'
    }
};

const catName = adventurer.cat?.name;
console.log(catName);

//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining 
//The above correlates with a comment on page 6, section 1.3.

