
function GetCheckedBoxes(){
    /*
    Arguments: None
    Returns: List of Strings of selected disasters
    Purpose: Retrieve all checked disasters in the form of a list
    */
    const displaydata = document.getElementById("getData");
    let selectedDisasters = [];

    document.querySelectorAll('[name = "disaster"]').forEach(item =>{
        if(item.checked === true){
            selectedDisasters.push(item.value);
        }
    })
    let disasterlist = document.getElementById("hiddenSelectedDisasters");
    disasterlist.value = selectedDisasters;
}