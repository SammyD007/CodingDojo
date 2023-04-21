function howMuchLeftOverCake(){
//declares the valuse of the variables
    let numberOfPieces = 12
    let numberOfPeople = 5
//runs the conditional tests
    if (numberOfPieces % numberOfPeople === 0){
        console.log("No leftovers for you!")}
    if (numberOfPieces % numberOfPeople >0 && numberOfPieces % numberOfPeople <= 2){
        console.log("You have some leftovers")}
    if (numberOfPieces % numberOfPeople >=3 && numberOfPieces % numberOfPeople <= 5){
        console.log("You have leftovers to share")}
    if (numberOfPieces % numberOfPeople >5){
        console.log("Hold another party!")}
}

//Prints the output of the function to the console
howMuchLeftOverCake()