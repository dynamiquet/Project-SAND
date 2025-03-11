document.addEventListener("DOMContentLoaded", function setCollapsibles() {
    /*
    Arguments: None
    Returns: None
    Purpose: Waits for a button with class "collapsible" to be clicked on and displays content
    */
    var coll = document.querySelectorAll(".collapsible");

    coll.forEach(function (button) { // Loop through each collapsible button
        button.addEventListener("click", function () {
            this.classList.toggle("active");
            
            var content = this.nextElementSibling;
            
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    });
});