const form = document.querySelector(".js-form"),
    input = form.querySelector("input"),
    greeting = document.querySelector(".js-greetings");

const USER_LS = "currentUser",
    SHOWING_CN = "showing";

function paintGreeting(text){
    form.classList.remove(SHOWING_CN);
    greeting.classList.add(SHOWING_CN)
    greeting.innerText = `Hello ${text}`
}
function getUserInfo(){
    form.classList.add(SHOWING_CN);
    greeting.classListList.remove(SHOWING_CN);

}
function loadName(){
    const currentUser = localStorage.getItem(USER_LS);
    if(currentUser === null){
        // she is not 
        getUserInfo();
    } else {
        // she is 
        paintGreeting(currentUser);
    }
}

function init(){
    loadName();
}

init();