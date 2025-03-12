function getCheckedBoxes(){
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

function setAllDisasterCheckedBoxes() {
  /*
  Arguments: None
  Returns: None
  Purpose: Sets all disaster checkboxes as checked or unchecked
  */
  if (isAllDisastersChecked()) {
    setUncheckAllDisasterCheckedBoxes();
  }

  else {
    document.querySelectorAll('[name = "disaster"]').forEach(item =>{
    item.checked = true
    })
  }
}

function getTotalSelectedCheckboxes() {
  /*
  Arguments: None
  Returns: Integer
  Purpose: Counts total number of disaster checkboxes that are checked
  */
  let totalSelectedDisasters = 0

  document.querySelectorAll('[name = "disaster"]').forEach(item =>{
    if (item.checked === true){
      totalSelectedDisasters++;
    }
  })
  return totalSelectedDisasters;
}

function isAllDisastersChecked() {
  /*
  Arguments: None
  Returns: Boolean
  Purpose: Determines if all disaster checkboxes are checked
  */
  let totalDisasterCheckboxes = 18
  let totalSelectedDisasters = getTotalSelectedCheckboxes();
  if (totalSelectedDisasters === totalDisasterCheckboxes){
    return true;
  }
  else {
    return false;
  }
}

function setUncheckAllDisasterCheckedBoxes() {
  /*
  Arguments: None
  Returns: None
  Purpose: If "check all disasters" checkbox is unchecked by user, then all disaster checkboxes will be unchecked
  */
  document.querySelectorAll('[name = "disaster"]').forEach(item =>{
    item.checked = false
  })
}

function getCurrentLocation() {
  /*
  Arguments: None
  Returns: None
  Purpose: Retrieves user geographical location from browser geolocation API if supported.
            Calls showPosition and passes API position data into it
  */
  if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(getUserPositionData);
  }
  else{
      let text = document.getElementById("UserCoordinates");
      text.textContent = "Geolocation is not being supported."
  }
}

function getUserPositionData (position) {
  /*
  Arguments: position data from geolocation API
  Returns: None
  Purpose: Stores user coordinates from position data and passes onto showUserPosition
  */
  let user_latitude = position.coords.latitude;
  let user_longitude = position.coords.longitude;
  showUserPosition(user_latitude, user_longitude);
}

function showUserPosition(user_latitude, user_longitude) {
  /*
  Arguments: User latitude and longitude in long data types
  Returns: None
  Purpose: Displays user position in a Google Map and Text from coordinates (Reverse Geocoding)
  */
  setUserCoord(user_latitude, user_longitude);
  createUniqueUserMap(user_latitude, user_longitude);
}

function setUserCoord (user_latitude, user_longitude) {
  /*
  Arguments: User latitude and longitude in long data types
  Returns: None
  Purpose: Sets html text to display user coordinates
  */
  let text = document.getElementById("UserCoordinates");
  text.innerHTML = "If you were curious, your coordinates are:<br> Latitude: " + user_latitude + "<br> Longitude: " + user_longitude
}


async function createUniqueUserMap(user_latitude, user_longitude) {
  /*
  Arguments: User latitude and longitude in long data types
  Returns: None
  Purpose: Creates a unique Google Map centered around the User's location while providing the user's county name
  */
  showMapBlock();
  setMapText();
  const position = setUserPositionData(user_latitude, user_longitude);
  let map = await setUserLocationCenteredMap(position);
  const marker = await setMapMarker(map, position);
  const countyName = await getUserCounty(position);
  setMapInfoWindow(map, marker, countyName);
}

function setMapText() {
  /*
  Arguments: None
  Returns: None
  Purpose: Updates supporting instructional text when user map is generated
  */
  let text = document.getElementById("HelpfulTextAboveSearchInput");
  text.innerHTML = "&#128073 Please click on the center red pin to get the name of your county! &#128072"
}

function showMapBlock() {
  /*
  Arguments: None
  Returns: None
  Purpose: Allows Map html block to be visible
  */
  document.getElementById("GoogleMap").style.display = "block";
}

async function setMapMarker(given_map, user_position) {
  /*
  Arguments: user map of Google Maps type and user latitude and longtitude coordinates
  Returns: Marker of AdvancedMarkerElement type
  Purpose: Creates a marker on generated Google Map to highlight user location
  */
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    // The marker, positioned at User Location
    const marker = new AdvancedMarkerElement({
      map: given_map,
      position: user_position,
      title: "Your Location",
    });

    return marker;
}

function setUserPositionData(user_latitude, user_longitude) {
  /*
  Arguments: User latitude and longtitude coordinates
  Returns: User position object
  Purpose: Coverts user coordinates into single position object
  */
  const position = { lat: user_latitude, lng: user_longitude };
  return position
}

async function setUserLocationCenteredMap(position) {
  /*
  Arguments: User position object
  Returns: Google Maps map
  Purpose: Centers the generated map at user location
  */
  const { Map } = await google.maps.importLibrary("maps");

  // The map, centered at Uluru
  let map = new Map(document.getElementById("GoogleMap"), {
    zoom: 15,
    center: position,
    mapId: "GoogleMap",
  });

  return map;
}

function setMapInfoWindow(map, marker, countyName){
  /*
  Arguments: Google Maps map, AdvancedMarkerElement marker, and String of user county
  Returns: None
  Purpose: Displays pop-up of user county when marker is clicked on
  */
  const infowindow = new google.maps.InfoWindow();

  google.maps.event.addListener(marker, "click", () => {
    infowindow.setContent(`<h3>Your County: ${countyName}</h3>`);
    infowindow.open(map, marker);
  });
}

async function getUserCounty(position) {
  /*
  Arguments: user position object
  Returns: String of user county
  Purpose: Retrieves user county by making a request through Google Maps API searching for county info (administrative_area_level_2)
  */
  const geocoder = new google.maps.Geocoder();

  return new Promise((resolve) => {
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

        resolve(countyName);
      } else {
        console.error("Geocoder failed due to: " + status);
        resolve("Unknown County");
      }
    });
  });
}

// function colorblindMode() {
//   const isChecked = document.getElementById("colorblind-mode").checked;

//   localStorage.setItem("colorblindmode", isChecked ? "enabled" : "disabled");

//   applyColorblindMode(isChecked);
// }

/* Uses the IBM color palette that is color-blind friendly */
function colorblindMode() {

  /* Apply colorblind mode to the page */
  if (document.getElementById("colorblind-mode").checked) {
    document.body.style.background = "#FFB000";
    document.getElementById("navigationBar_ul").style.backgroundColor = "#785EF0";
    document.getElementById("navigationBar_ul").style.boxShadow = "none";
    document.getElementById("project-title").style.backgroundColor = "#DC267F";
    document.getElementById("project-title").style.borderColor = "#785EF0";

    if (document.getElementById("input")) {
      document.getElementById("input").style.backgroundColor = "#FE6100";
    }

    if (document.getElementById("CheckAllDisasters")) {
      document.getElementById("CheckAllDisasters").style.backgroundColor = "#DC267F";
    }

    if (document.getElementById("ALLDS")) {
      document.getElementById("ALLDS").style.backgroundColor = "#DC267F";
    }

    if (document.getElementById("top5box")) {
      document.getElementById("top5box").style.backgroundColor = "#DC267F";
    }

    if (document.getElementById("countyResults")) {
      document.getElementById("countyResults").style.backgroundColor = "#DC267F";
    }

    /* WILL BE CHANGED AFTER CLASS WORKSHOP */
    if (document.getElementById("HelpfulTextAboveSearchInput")) {
      document.getElementById("HelpfulTextAboveSearchInput").style.color = "#648FFF";
      document.getElementById("HelpfulTextAboveSearchInput").style.textShadow = "none";
    }

    if (document.getElementById("HelpfulTextAboveSearchInput2")) {
      document.getElementById("HelpfulTextAboveSearchInput2").style.color = "#648FFF";
      document.getElementById("HelpfulTextAboveSearchInput2").style.textShadow = "none";
    }

    if (document.getElementById("HelpfulTextAboveSearchInput3")) {
      document.getElementById("HelpfulTextAboveSearchInput3").style.color = "#648FFF";
      document.getElementById("HelpfulTextAboveSearchInput3").style.textShadow = "none";
    }

    if (document.getElementById("HelpfulTextAboveSearchInput4")) {
      document.getElementById("HelpfulTextAboveSearchInput4").style.color = "#648FFF";
      document.getElementById("HelpfulTextAboveSearchInput4").style.textShadow = "none";
    }
  /* Revert back to the normal styling */
  } else {
    document.body.style.background = "#F5F5DC";
    document.getElementById("navigationBar_ul").style.backgroundColor = "#2E8B57";
    document.getElementById("navigationBar_ul").style.boxShadow = "0 5px 5px 0 #296b46";
    document.getElementById("project-title").style.backgroundColor = "#afe38c";
    document.getElementById("project-title").style.borderColor = "#2E8B57";

    if (document.getElementById("input")) {
      document.getElementById("input").style.backgroundColor = "#FFC107";
    }

    if (document.getElementById("CheckAllDisasters")) {
      document.getElementById("CheckAllDisasters").style.backgroundColor = "#afe38c";
    }

    if (document.getElementById("ALLDS")) {
      document.getElementById("ALLDS").style.backgroundColor = "#afe38c";
    }

    if (document.getElementById("top5box")) {
      document.getElementById("top5box").style.backgroundColor = "#afe38c";
    }

    if (document.getElementById("countyResults")) {
      document.getElementById("countyResults").style.backgroundColor = "#afe38c";
    }

    /* WILL BE CHANGED AFTER CLASS WORKSHOP */
    if (document.getElementById("HelpfulTextAboveSearchInput")) {
      document.getElementById("HelpfulTextAboveSearchInput").style.color = "#2E8B57";
      document.getElementById("HelpfulTextAboveSearchInput").style.textShadow = "2px 2px 3px #afe38c";
    }

    if (document.getElementById("HelpfulTextAboveSearchInput2")) {
      document.getElementById("HelpfulTextAboveSearchInput2").style.color = "#2E8B57";
      document.getElementById("HelpfulTextAboveSearchInput2").style.textShadow = "2px 2px 3px #afe38c";
    }

    if (document.getElementById("HelpfulTextAboveSearchInput3")) {
      document.getElementById("HelpfulTextAboveSearchInput3").style.color = "#2E8B57";
      document.getElementById("HelpfulTextAboveSearchInput3").style.textShadow = "2px 2px 3px #afe38c";
    }

    if (document.getElementById("HelpfulTextAboveSearchInput4")) {
      document.getElementById("HelpfulTextAboveSearchInput4").style.color = "#2E8B57";
      document.getElementById("HelpfulTextAboveSearchInput4").style.textShadow = "2px 2px 3px #afe38c";
    }
  }
}

// window.onload = function() {
//   const storedPreference = localStorage.getItem("colorblindMode");
//   const isEnabled = storedPreference === "enabled";

//   document.getElementById("colorblind-mode").checked = isEnabled;
//   applyColorblindMode(isEnabled);
// }