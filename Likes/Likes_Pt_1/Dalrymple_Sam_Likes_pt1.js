// function to increment likes
function addLike() {
    let likeCount = document.querySelector(".likes-counter")
        let likenumber = Number(likeCount.innerHTML)
        likeCount.innerHTML = likenumber + 1
}