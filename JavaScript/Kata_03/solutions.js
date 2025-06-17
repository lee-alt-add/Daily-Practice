/**
 * @param {Number} a
 * @param {Number} b
 * @returns {Number}
 */
function addTwoNumbers(a,b) {
    return a+b;
}

/**
 * 
 * @param {String} s 
 * @returns {String}
 */
function reverseString(s) {
    return s.split("").reverse().join("");
}

/**
 * @param {Array}
 * @returns {Number}
 */
function calculateAverage(numbers) {
    return numbers.reduce((a,b) => a+b ,0) / numbers.length;
}

/**
 * @param {Array}
 * @returns {Array}
 */
function flattenList(array) {
    return array.flat(Infinity);
}

/**
 * @param {String} text
 * @returns {Map}
 */
function wordCount(text) {
    let numOfWords = (list,e) => list.filter((a) => a === e).length;
    return text.split(" ").reduce((acc, curr) => 
        acc.set(curr, numOfWords(text.split(" "),curr)),new Map());
}

