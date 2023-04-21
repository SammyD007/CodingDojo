let milesRan = 6
let runDistance = false
let runSpeed = 5.5

if(milesRan %2 == 0 && milesRan <= 6){
    runDistance = true
}

if(runDistance == true && runSpeed >= 5.5){
    console.log("Candy dispensed.")
} else{
    console.log("No candy for you!")
}