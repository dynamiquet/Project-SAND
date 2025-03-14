document.addEventListener("DOMContentLoaded", function setColorblindListener() {
    /*
    Arguments: None
    Returns: None
    Purpose: Update
    */
    var colorblind_checkbox = document.getElementById("colorblind-mode");
    
    let isColorblindOnPrevPage = localStorage.getItem("colorblind-mode") === "true";

    if (isColorblindOnPrevPage) {
        colorblind_checkbox.checked = true;
        setColorblindMode(colorblind_checkbox);
    }

    
    colorblind_checkbox.addEventListener("click", function() {
        setColorblindMode(colorblind_checkbox);
    });
});

// localStorage is pretty cool! 
// https://www.sitepoint.com/quick-tip-persist-checkbox-checked-state-after-page-reload/
function setColorblindMode(colorblind_checkbox) {
    if (colorblind_checkbox.checked) {
        setColorblindOn();
        localStorage.setItem("colorblind-mode", "true");
    } else {
        setColorblindOff();
        localStorage.setItem("colorblind-mode", "false");
    }
}

function setColorblindOn() {
    allColorblindElements = getAllColorblindElements();
    setBackgroundColors(allColorblindElements);
    setTextShadowsOff(allColorblindElements);
}

function setColorblindOff() {
    document.body.style.background = ""; // Apparently "" sets the style back to the default (whatever we have on datastyle)!!!

    allColorblindElements.forEach(element => {
        element.style.backgroundColor = "";
        element.style.color = "";
        element.style.textShadow = "";
        element.style.boxShadow = "";
        element.style.borderColor = "";
    })
}

function setBackgroundColors (allColorblindElements) {
    document.body.style.background = "#FFB000";
    document.getElementById("project-title").style.borderColor = "#785EF0";
    document.getElementById("navigationBar_ul").style.backgroundColor = "#785EF0";
    document.getElementById("navigationBar_ul").style.boxShadow = "none";
    setBackgroundColorBrightPink(allColorblindElements);
    setBackgroundColorOrange(allColorblindElements);
    setColorLightBlue(allColorblindElements);
    setTextOrange(allColorblindElements);
    setBackgroundColorLightBlue(allColorblindElements);
    setColorLavender(allColorblindElements);
}

function setTextShadowsOff (allColorblindElements){
    allColorblindElements.forEach(element =>{
        element.style.textShadow = "none";
    });
}

function getAllColorblindElements () {
    var allColorblindElements = document.querySelectorAll(".ColorblindElement");
    return allColorblindElements
}

function setBackgroundColorBrightPink (allColorblindElements){
    allColorblindElements.forEach(function (element) {
        if (element.classList.contains('BPink')){
            element.style.backgroundColor = "#DC267F"
        }
    });
}

function setBackgroundColorLightBlue (allColorblindElements){
    allColorblindElements.forEach(function (element) {
        if (element.classList.contains('BackgroundLBlue')){
            element.style.backgroundColor = "#98B1F3"
        }
    });
}

function setColorLightBlue (allColorblindElements){
    allColorblindElements.forEach(function (element) {
        if (element.classList.contains('LBlue')){
            element.style.color = "#648FFF"
        }
    });
}

function setColorLavender(allColorblindElements){
    allColorblindElements.forEach(function (element) {
        if (element.classList.contains('Lavender')){
            element.style.color = "#785EF0"
        }
    });
}

function setBackgroundColorOrange (allColorblindElements){
    allColorblindElements.forEach(function (element) {
        if (element.classList.contains('Orange')){
            element.style.backgroundColor = "#FE6100"
        }
    });
}

function setTextOrange (allColorblindElements){
    allColorblindElements.forEach(function (element) {
        if (element.classList.contains('Text')){
            element.style.color = "#FE6100"
        }
    });
}