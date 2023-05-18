function myFunction() {
    alert("Hello from a static file!");
  }

function search(){

  var s=$("input[name=state]").val();
  var c=$("input[name=city]").val();
  alert("State- "+s+" City-"+ c)
}



function myFunction2() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  console.log(filter);
  table = document.getElementById("myTable");
  console.log(table);
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[0];
    if (td) {
      txtValue = td.textContent || td.innerText;
      console.log(txtValue);
      
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}





let map, infoWindow;

async function initMap_cp() {
  const { Map } = await google.maps.importLibrary("maps");
  const { Marker } = await google.maps.importLibrary("marker");
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 6,
  });
  infoWindow = new google.maps.InfoWindow();

  const locationButton = document.createElement("button");

  locationButton.textContent = "Pan to Current Location";
  locationButton.classList.add("custom-map-control-button");
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
  locationButton.addEventListener("click", () => {
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          };

          infoWindow.setPosition(pos);
          console.log(pos);
          infoWindow.setContent("Location found.");
          infoWindow.open(map);
          map.setCenter(pos);
        },
        () => {
          handleLocationError(true, infoWindow, map.getCenter());
        }
      );
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, map.getCenter());
    }
  });
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(
    browserHasGeolocation
      ? "Error: The Geolocation service failed."
      : "Error: Your browser doesn't support geolocation."
  );
  infoWindow.open(map);
}

window.initMap_cp = initMap_cp;



function functionx(){
  console.log("ITs Here");
  window.location.href = "http://www.w3schools.com";
}






// current location map
const options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0,
};

async function success(pos) {
  const crd = pos.coords;

  // console.log("Your current position is:");
  // console.log(crd.latitude);
  // console.log(`Longitude: ${crd.longitude}`);
  // console.log(`More or less ${crd.accuracy} meters.`);


  const position = { lat: crd.latitude, lng: crd.longitude };
  // Request needed libraries.
  const { Map } = await google.maps.importLibrary("maps");
  const { Marker } = await google.maps.importLibrary("marker");

  let map = new Map(document.getElementById("map-element-main"), {
    zoom: 8,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  const marker = new Marker({
    position: position,
    map: map,
  });

  marker.setMap(map);
}

function error(err) {
  console.warn(`ERROR(${err.code}): ${err.message}`);
}

function test(){
  navigator.geolocation.getCurrentPosition(success, error, options);
}

// function initMapHomeEstimate() {
//   console.log("blue");
//   const latvalues = document.getElementsByClassName("lat-value");
//   const lonvalues = document.getElementsByClassName("lon-value");

//   let coordinates = [];

//   for (let i=0; i<latvalues.length; i++) {
//     coordinates.push([latvalues[i].attributes.value.value, lonvalues[i].attributes.value.value]);
//     console.log([latvalues[i].attributes.value.value, lonvalues[i].attributes.value.value]);
//   }

//   console.log(coordinates);

//   const map = new google.maps.Map(document.getElementById("map-home-estimate"), {
//     center: { lat: parseInt(coordinates[0][0]), lng: parseInt(coordinates[0][1]) },
//     zoom: 15,
//     mapTypeControl: false,
//   });
//   //const input = document.getElementById("pac-input");
//   const options = {
//     fields: ["formatted_address", "geometry", "name"],
//     strictBounds: false,
//     types: ["address"],
//   };
//   //const autocomplete = new google.maps.places.Autocomplete(input, options);

//   setMarkers(map, coordinates);

// }

function setMarkers(map, coordinates) {

  for (let i = 0; i < coordinates.length; i++) {
    const coordinate = coordinates[i];
    new google.maps.Marker({
      map,
      //anchorPoint: new google.maps.Point(0, -29),
      position: { lat: parseInt(coordinate[0]), lng: parseInt(coordinate[1]) },
      title: i.toString(),
      label: i.toString(),
    });
  }
}

//window.initMapHomeEstimate = initMapHomeEstimate;