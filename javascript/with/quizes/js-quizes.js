function quiz(quesiton, callback = () => {}) {
    console.log(quesiton);

    

    callback();
}

quiz(`
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   Question: Do you know what will be the output of this code?   │
│      │   ┌──────────────────────────────┐                       │
│      │   │                              │                       │
│      │   │    let array = [1, 2, 3];    │                       │
│      └──►│    array[6] = 9;             │                       │
│          │    console.log(array[5]);    │                       │
│          │                              │                       │
│          └──────────────────────────────┘                       │
└─────────────────────────────────────────────────────────────────┘
`,
() => {

});

console.log(
  
    // quiz 1: Why is result false?
    "This is a string." instanceof String, // false
    
    // explain quiz 1
    typeof "This is a string.", // "string"
    typeof String, // "object"
    new String("This is a string.") === String, // true
    new String("This is a string.") === Object, // true
    
    // -------
  
    // quiz 2: Why is result false?
    0.1 + 0.2 === 0.3, // false
    
    // explain quiz 2:
    (0.1 + 0.2), // 0.30000000000000004
    (0.1 + 0.2).toFixed(1), // '0.3'
    Number((0.1 + 0.2).toFixed(1)) === 0.3, // true
    
    // -------
    
    // quiz 3: Result?
    String.raw`HelloTwitter\nworld`, // HelloTwitter\nworld
    // Because the raw method prints exactly what it sees.
    
    // -------
    
    // quiz 4: Result?
    ('b' + 'a' + + 'a' + 'a').toLowerCase(), // banana
  
    // explain quiz 4
    (+ 'a'), // NaN
    ('a' + + 'a'), // aNaN
    ('b' + 'a' + + 'a' + 'a'), // baNaNa
  
    // -------
    
    // quiz 5: Why typeof NaN is equal to 'number'?
    typeof NaN === 'number', // true
    
    // explain quiz 5: not a number(NaN) is number but is fake number.
    isNaN(NaN), // true
    isNaN(5), // false
    
    // -------
    
    // quiz 6: Result?
    3 > 2 > 1, // false
    
    // explain quiz 6: Any compiler always starts reading left to right.
    3 > 2, // true
    true > 1, // false because true is equal to 1
    true === 1, // true
    
    // -------
    
    // quiz 7: Explain for Why?
    (() => {
        let arr = [1, 2, 3];
        
        arr[6] = 9; // [1, 2, 3, <3 empty item>, 9]
    
        return arr[5]
    })() // undefined
    
  )