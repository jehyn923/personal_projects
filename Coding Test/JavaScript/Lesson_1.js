'use strict';

//let (added in ES6) r/w available
//global은 항상 메모리에 있음
let name = 'global name'
{
    //Block Scope 안에 있는 값은 밖에서 사용 못함
    let name = 'Frank';
    console.log(name);
    name = 'hello';
    console.log(name);
}

console.log(name);
console.log(name);

//var (dont ever use this!) 
//var hoisting(move declaration from bottom to top. 선언을 끌어올려주는 것)
//값을 선언 전에 할당할 수 있음 코드가 이상해짐
// block scope을 무시하고 사용 가능 함.


//constant, r(read only)
//favor immutable data type always 
// - security
// - thread safety
// - reduce human mistakes
const daysInWeek = 7;
const maxNumber = 5;

console.log(maxNumber);

//Note!
//Immutable data types: premitive types, frozen objects
//Mutable data types : all objects by default are mutable in JS




// variable types
// primitive, sigle item : number, string, boolean, null, undefined, symbol
// object, box container
// function, first-class function (변수처럼 함수 할당 가능, parameter로 보낼 수 있고,return type에도 넣을 수 있음 )

//primitive type
//object는 reference가 저장 object들을 가리키는 주소를 저장
//따라서 object를 const화 하면 주소 저장한 것을 잠그는 것이고, value들은 수정할 수 있게 함

//number
const infinity = 1/0;
const negativeInfinity = -1/0;
const nAn = 'not a number' /2;

console.log(infinity);
console.log(negativeInfinity);
console.log(nAn);

//string
const char = 'c';
const brendan ='brendan';
const helloBob =`hi ${brendan}!`; //template literals (스트링) 백틱(`)사용
console.log(helloBob)

// symbol, create unique identifiers for objects
// map 구조를 만들거나 식별자를 만들어야할 때 사용. 
// symbol('id') <= 문자열이 같아도 각각 식별자가 다른 형태로 나오지만
// symbol.for('id')라고 하면 'id' 문자열을 위한 식별자를 동일하게 만들어준다.

const symbol1 = Symbol('id');
const symbol2 = Symbol('id');
console.log(symbol1===symbol2);

//5 다이나믹 타이핑: dynamically typed language => 자바스크립트 
//선언할 때 어떤 타입인지 선언 안하고, Run time에서 할당할 때 
//규모 있는 프로그램 만들때는 dynamic typing이 문제가 될 수 있음
let text = 'hello';
console.log(`value: ${text}, type: ${typeof text}`);
text = '7' + 5;
console.log(`value: ${text}`)
text = '8'/'2';
console.log(`value: ${text}`)

// 이런 거 때문에, 런타임에러가 많이 생겨 타입을 지정해줘야 하니까 TypeScript가 생김