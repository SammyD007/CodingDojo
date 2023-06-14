/* alright, alrightI know what you are thinking, there is three functions... WHY
 the whole point is to make it one function so that it can be reused BUT, I think
 that I did the naming of things a little incorrectly so it would only change the 
 number on the very first box and so I did it this way just because it works this way.
 */
function addLike1() {
    let likeCount = document.querySelector(".likes-counter1")
        let likenumber = Number(likeCount.innerHTML)
        likeCount.innerHTML = likenumber + 1
}

function addLike2() {
    let likeCount = document.querySelector(".likes-counter2")
        let likenumber = Number(likeCount.innerHTML)
        likeCount.innerHTML = likenumber + 1
}

function addLike3() {
    let likeCount = document.querySelector(".likes-counter3")
        let likenumber = Number(likeCount.innerHTML)
        likeCount.innerHTML = likenumber + 1
}