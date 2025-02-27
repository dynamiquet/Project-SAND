
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
    text.innerHTML = "Your Coordinates are:<br> Latitude: " + user_latitude + "<br> Longitude: " + user_longitude
    initMap(user_latitude, user_longitude)
}

// Initialize and add the map
let map;

async function initMap(user_latitude, user_longitude) {
  document.getElementById("GoogleMap").style.display = "block";
  text = document.getElementById("HelpfulTextAboveMaps");
  text.innerHTML = "Please click on the pin to get the name of your county!"

  // The location of the User
  const position = { lat: user_latitude, lng: user_longitude };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at Uluru
  map = new Map(document.getElementById("GoogleMap"), {
    zoom: 15,
    center: position,
    mapId: "GoogleMap",
  });

  // The marker, positioned at User Location
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "Your Location",
  });

 // Info window for displaying county
 const infowindow = new google.maps.InfoWindow();

 // Reverse Geocode to get county name
 const geocoder = new google.maps.Geocoder();
 geocoder.geocode({ location: position }, (results, status) => {
   if (status === "OK" && results[0]) {
     let countyName = "Unknown County";
     
     // Extract county from address components
     for (const component of results[0].address_components) {
       if (component.types.includes("administrative_area_level_2")) {
         countyName = component.long_name;
         break;
       }
     }

     // Set click event to display county name
     google.maps.event.addListener(marker, "click", () => {
       infowindow.setContent(`<h3>Your County: ${countyName}</h3>`);
       infowindow.open(map, marker);
     });
   } else {
     console.error("Geocoder failed due to: " + status);
   }
 });
}