//Function Naming
//1 function === one thing
//naming : doSomething, command, verb
//e.g. createCardAndPoint -> createCard, createPoint
//이름 짓기에 너무 많은 수행을 한다면 해당 function 세분화
//function은 object 야(in js)
"use strict"
function printHello(){
    console.log('Hello');
}
printHello();

//3. Default Parameters (added in ES6)
function showMessage(message, from = 'unknown'){
    console.log(`${message} by ${from}`);
}

//Rest Parameters
// ... 으로 전달하면 array로 전달되는 것을 알고 있어라!

function printAll(...args){
    for (let i = 0; i<args.length;i++){
        console.log(args[i]);
    }

    for (const arg of args) {
        console.log(arg);
    }

    args.forEach((arg) => console.log(arg));

}
// Javascript의 Scope란 
//밖에서는 안이 보이지 않지만, 안에서만 밖을 볼 수 있는 것
let globalMessage = 'global';
function printMessage(){
    let message = 'hello';
    console.log(message);
    console.log(globalmessage);
    function printAnother(){
        console.log(message);
        let childMessage = 'hello';
    }
    console.log(childMessage);
}

//7. Early return, early exit 원
//if문안에 많은 로직들을 넣어 두면 좋지 효율적이지 않음
//그래서 해당 대상이 아닐 경우 빠르게 return 하고, 로직을 작성
function upgradeUser(user){
    if (user.point <= 10){
        return;
    }
    //
}

//fuction expression이란?
//function declartion은 function hoisting이 가능함
//function expression은 function hoisting이 불가능함
const print = function () {//anonymous function
    console.log('print');
};
print();
const printAgain = print;
printAgain();

//callback function
function randomQuiz(answer, printYes, printNo){
    if(answer === 'love you'){
        printYes();
    } else{
        printNo();
    }
}

//anonymous function
const printYes = function() {
    console.log('yes!');
};

//named function
//디버깅 stack trace할 때
//recursion을 할 때
const printNo = function print(){
    console.log('no');
};
randomQuiz('wrong',printYes,printNo);
randomQuiz('love you',printYes,printNo);

let a = 2;
let b = 3;
//Arrow Function
//always anonymous function
const simplePrint = () => console.log('simplePrint');
const add = (a,b) => a+b;

//IIFE : Immediately Invoked Function Expression
(function hello(){
    console.log('IIFE');
})();