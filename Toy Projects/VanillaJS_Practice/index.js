const title = document.querySelector("#title");


const CLICKED_CLASS = "clicked";
//JavaScript은 html, css를 변경하려고 만들어진 게 아닌, 웹사이트의 이벤트에 반응 위해 만들어짐
//Javascript로 이벤트를 가로챌 수 있음


function handleResize(event){
    console.log(event)
}

function handleClick(){
    const currentClass = title.className;
    if(currentClass !== CLICKED_CLASS){
        title.className = CLICKED_CLASS;
    } else {
        title.className = "";
    }
}

function handleOffline(){
    console.log("lalalalalala");
}

function handleOnline(){
    console.log("Welcome Back!");
}

function init(){

    //title.style.color = BASE_COLOR;
    //parameter에 handleResize()가 아닌 handleResize로 보낸 것이 중요 
    //handleResize()면 지금 당장 실행하라, handleResize면 필요할 때 실행하라가 됨
    //자바스크립트에서 이벤트를 다루는 함수를 만들 때, 이벤트 객체를 같이 붙임
    window.addEventListener("resize",handleResize);

    title.addEventListener("click", handleClick);

}

init();