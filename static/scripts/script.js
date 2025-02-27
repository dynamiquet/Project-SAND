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

function GetCurrentLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    }
    else{
        text.textContent = "Geolocation is not being supported."
    }
}

function showPosition(position) {
    let text = document.getElementById("UserCoordinates");
    let user_latitude = position.coords.latitude
    let user_longitude = position.coords.longitude
    text.textContent = "Your Coordinates are: Latitude: " + user_latitude + "Longitude: " + user_longitude
    initMap(user_latitude, user_longitude)
}

// Initialize and add the map
let map;

async function initMap(user_latitude, user_longitude) {
  // The location of the User
  const position = { lat: user_latitude, lng: user_longitude };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at Uluru
  map = new Map(document.getElementById("GoogleMap"), {
    zoom: 10,
    center: position,
    mapId: "GoogleMap",
  });

  // The marker, positioned at Uluru
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "Your Location",
  });
}