/* I know this on/off function isn't required but with the frustration I am 
feeling with css I could use some fun with somehting I am more familiar with 
so.. on/off function it is */
function login(){
    let loginButton = document.getElementById("login-btn")
        if (loginButton.innerHTML === "Login"){
            loginButton.innerHTML = "Logout"
        } else {
            loginButton.innerHTML = "Login"
        }
}

function search(){
    document.getElementById("search-bar").value = ""
}

/* The next two functions are also extra stuff I did just cuz I needed the win
I thought I understood css a lot more than I did and am feeling very frustrated */
function like1(){
    alert("Ninja was liked")
    let likeClick1 = document.getElementById("like-btn1")
        let numbers1 = likeClick1.innerHTML.slice(0,2)
        likeClick1.innerHTML = (Number(numbers1) + 1 + " Likes")
}

function like2(){
    alert("Ninja was liked")
    let likeClick2 = document.getElementById("like-btn2")
        let numbers2 = likeClick2.innerHTML.slice(0,2)
        likeClick2.innerHTML = (Number(numbers2) + 1 + " Likes")
}
// Couldn't think of a way to be extra with this one lol
function addDefinition(){
    document.getElementById("add-definition-btn").style.visibility = "hidden"
}