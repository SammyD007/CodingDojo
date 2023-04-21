//Minimum Height Variable - rider must be at least 42 inches
const minHeight = 42
//Minimum Age Variable - rider must be at least 10 years of age
const minAge = 10
//values for the test
let isOldEnough = false
let isTallEnough = false
//Set the variables for age and height
let kidAge = 10
let kidHeight = 42
//if the child is old enough this will set the isOldEnough variable to true
if(kidAge >= minAge){
    isOldEnough = true
} else {

}

//if the child is tall enough this will set the isTallEnough variable to true
if(kidHeight >= minHeight){
    isTallEnough = true
} else {

}

//tests if the user is old enough or tall enough and uses that to determine if they can get on the ride
if(isOldEnough == true || isTallEnough == true){
    console.log("Get on that ride kiddo!")
} else {
    console.log("Sorry kiddo maybe next year.")
}