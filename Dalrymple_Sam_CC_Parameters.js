//The following two lines are used to pull the time (hour) of the day 0-23
let day = new Date();
let time = day.getHours()
/*this function uses the name input as well as the time of day to enter the
console log output for the greeting UNLESS the user inputs "Count Dooku"
then it will return the I am coming for you output
*/
let greet = function (name) {
    if (name == "Count Dooku"){
        return "I am coming for you Count Dooku"
    }
        if (time <= 8){
            return "Good morning, " + name
        }
        if (time > 8 && time <= 17){
            return "Good day, " + name
        } 
        if (time > 17 && time <= 23){
            return "Good night, " + name
        };
}
//console log to see output
console.log(greet("Anakin"))