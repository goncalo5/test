var myInput = document.getELementById("input"),
    myDiv = document.getELementById("div");

myInput.onkeyup = function () {
    "use strict";
    myDiv.innerHTML = myInput.value * 3.75;
}
