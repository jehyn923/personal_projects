function stack(yes){
    const arry =[];
    for (let i = 0; i<10; i++){
        arry.push(i);
    }

    //arry.forEach(element=>console.log(element));
    let length = arry.length;
    
    
    for (let i =0; i<length; i++){
        console.log(arry);
        console.log(arry.pop());
    }
    console.log(arry);
}

stack("yes");


function queue(yes){
    const arry=[];
    for (let i = 0; i<10; i++){
        arry.push(i);
    }

    let length = arry.length;

    for (let i = 0; i < length; i++){
        console.log(arry.shift());
    }
}
queue("yes");

function stringify(yes){
    const arry=[];
    for (let i=0;i<10;i++){
        arry.push(i);
    }
    let length = arry.length;
    
    console.log(arry.toString(),typeof arry.toString(), typeof arry)
    
}
stringify("yes");

temp = {1:[1,2,3,4], 2:'two', 3:'three'};

temp[5] = 'good';
temp [9] = 'getthis';

console.log(temp[3]);
console.log(temp[1][2]);
console.log(temp);