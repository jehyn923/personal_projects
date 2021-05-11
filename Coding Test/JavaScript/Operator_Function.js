//1. String concatenation

console.log('my' + 'cat');
console.log('1'+2);
console.log(`string literals:1+2=${1+2}`);

//Logical Operators: || (or), && (and), ! (not)
const value1 = false;
const value2 = 4 < 2;

console.log(`or: ${value1 || value2 || check()}`);
//simple한 value 들을 앞에다 두고 heavy computation function들을 뒤에 넣어야 효율적
//이하 동문
console.log(`and: ${value1 && value2 && check()}`);

function check(){
    for(let i =0 ; i<10;i++){
        console.log('');
    }
    return true;
}

//object equality by references
const ellie1 = {name:'ellie'};
const ellie2 = {name:'ellie'};
const ellie3=ellie1;

console.log(ellie1 == ellie2); //False
console.log(ellie1 === ellie2); //False
console.log(ellie1 === ellie3); //ellie 1의 reference ellie3에 할당한 형태니 True

//Ternary operator:?
console.log(name==='ellie'?'yes':'no');