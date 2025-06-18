
// Counter
let pairs = (list) => { 
    let counter = (lst, x) => lst.reduce((a,b) => b === x ? a += 1: a, 0);
    return list.reduce((acc, curr) => acc.set(`${curr}`, counter(list, curr)), new Map());
}

// Convert a array of objects to a nested array of [[...keys], [...values]]
let convertToNest = (lst) => lst.reduce((acc, curr) =>{
     acc[0].push(curr.name); 
     acc[1].push(curr.age);
     return acc;
    }, [[], []]);


let evenAndOdd = (list) => list.reduce((acc, curr) => {
    curr % 2 === 0 ? acc.even.push(curr): acc.odd.push(curr)
    return acc;
}, {even:[], odd:[]});


console.log(pairs([1,2,4,2,1,3]));
console.log(convertToNest([{name:"Lindo", age: 27}, {name:"Hlonie", age: 26}]));
console.log(evenAndOdd([1,2,4,2,1,3, 21, 32, 76, 33, 139,22, 31]));