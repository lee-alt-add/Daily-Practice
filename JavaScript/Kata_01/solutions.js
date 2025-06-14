let swap = (a,b) => { return {a:b, b:a} };

let evenOrOdd = (n) => { return (n % 2 == 0) ? "Even" : "Odd"; }

let maxNum = (lst) => {return Math.max(...lst)};

let sum = (lst) => { return lst.reduce((a,b) => a + b, 0); }

let vowels = (str) => { return str.split("").filter((a) => "aeiou".includes(a.toLowerCase())).length; }

let reversed = (str) => { return str.split("").reverse().join(""); }

let fizzbuzz = (n) => {
	let out = [];

	for (let a = 1; a < n + 1; a++) {
		out.push(a % 3 == 0 && a % 5 == 0 ? "FizzBuzz" :
				 a % 3 == 0 ? "Fizz" :
				 a % 5 == 0 ? "Buzz" :
				 `${a}`);
	}
	return out.join(" ");
}

let isPalindrome = (str) => { return str.toLowerCase().split("").reverse().join("") == str.toLowerCase(); }

console.log(swap(5,56).b);
console.log(evenOrOdd(10));
console.log(maxNum([1,2,453,657,200,123]));
console.log(sum([1,2,453,657,200,123]));
console.log(vowels("lindokuhle"));
console.log(reversed("lindokuhle"));
console.log(fizzbuzz(20));
console.log(isPalindrome("racecar"));