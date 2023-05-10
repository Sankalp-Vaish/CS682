// This example creates a 2-pixel-wide red polyline showing the path of
// the first trans-Pacific flight between Oakland, CA, and Brisbane,
// Australia which was made by Charles Kingsford Smith.
// let poly;
// function initMap_test() {
//     console.log(5);
//     $("#map_test").css({"height": "400px", "width": "550px"});
//     const map = new google.maps.Map(document.getElementById("map_test"), {
//       zoom: 3,
//       center: { lat: 0, lng: -180 },
//       mapTypeId: "terrain",
//     });
//     console.log(11);
//     const flightPlanCoordinates = [
//       { lat: 37.772, lng: -122.214 },
//       { lat: 21.291, lng: -157.821 },
//       { lat: -18.142, lng: 178.431 },
//       { lat: -27.467, lng: 153.027 },
//     ];
//     const flightPath = new google.maps.Polyline({
//       path: flightPlanCoordinates,
//       geodesic: true,
//       strokeColor: "#FF0000",
//       strokeOpacity: 1.0,
//       strokeWeight: 2,
//     });
//     console.log(25);
  
//     flightPath.setMap(map);
//     console.log(29);
//     map.addListener("click", addLatLng);
// }

// // Handles click events on a map, and adds a new point to the Polyline.
// function addLatLng(event) {
//   const path = poly.getPath();

//   // Because path is an MVCArray, we can simply append a new coordinate
//   // and it will automatically appear.
//   path.push(event.latLng);
//   // Add a new marker at the new plotted point on the polyline.
//   new google.maps.Marker({
//     position: event.latLng,
//     title: "#" + path.getLength(),
//     map: map,
//   });
// }
// This example creates an interactive map which constructs a polyline based on
// user clicks. Note that the polyline only appears once its path property
// contains two LatLng coordinates.
let poly;
let map_main;

async function initMap_test() {
  $("#map_test").css({"height": "450px", "width": "1000px"});
  // console.log(55);
  const { Map } = await google.maps.importLibrary("maps");
  map_main = new Map(document.getElementById("map_test"), {
    zoom: 13,
    center: { lat: 41.879, lng: -87.624 }, // Center the map on Chicago, USA.
  });
  poly = new google.maps.Polyline({
    strokeColor: "#000000",
    strokeOpacity: 1.0,
    strokeWeight: 3,
  });
  poly.setMap(map_main);
  // Add a listener for the click event
  map_main.addListener("click", addLatLng);
  console.log(69);
}

// Handles click events on a map, and adds a new point to the Polyline.
async function addLatLng(event) {
  // console.log(74);
  const path = poly.getPath();

  // Because path is an MVCArray, we can simply append a new coordinate
  // and it will automatically appear.
  path.push(event.latLng);
  // console.log(JSON.stringify(event.latLng.toJSON(), null, 2));
  console.log(event.latLng.lat());
  console.log(event.latLng.lng());
  // Add a new marker at the new plotted point on the polyline.
  const { Marker } = await google.maps.importLibrary("marker");
  new Marker({
    position: event.latLng,
    title: "#" + path.getLength(),
    map: map_main,
  });
  // console.log(85);
}

// window.initMap = initMap;
 window.initMap_test = initMap_test;


//let map, infoWindow;

// async function initMap_test() {
//   const { Map } = await google.maps.importLibrary("maps");
//   const { Marker } = await google.maps.importLibrary("marker");
//   map = new google.maps.Map(document.getElementById("map_test"), {
//     center: { lat: -34.397, lng: 150.644 },
//     zoom: 6,
//   });
//   infoWindow = new google.maps.InfoWindow();

//   const locationButton = document.createElement("button");

//   locationButton.textContent = "Pan to Current Location";
//   locationButton.classList.add("custom-map-control-button");
//   map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
//   locationButton.addEventListener("click", () => {
//     // Try HTML5 geolocation.
//     if (navigator.geolocation) {
//       navigator.geolocation.getCurrentPosition(
//         (position) => {
//           const pos = {
//             lat: position.coords.latitude,
//             lng: position.coords.longitude,
//           };

//           infoWindow.setPosition(pos);
//           console.log(pos);
//           infoWindow.setContent("Location found.");
//           infoWindow.open(map);
//           map.setCenter(pos);
//         },
//         () => {
//           handleLocationError(true, infoWindow, map.getCenter());
//         }
//       );
//     } else {
//       // Browser doesn't support Geolocation
//       handleLocationError(false, infoWindow, map.getCenter());
//     }
//   });
// }

// function handleLocationError(browserHasGeolocation, infoWindow, pos) {
//   infoWindow.setPosition(pos);
//   infoWindow.setContent(
//     browserHasGeolocation
//       ? "Error: The Geolocation service failed."
//       : "Error: Your browser doesn't support geolocation."
//   );
//   infoWindow.open(map);
// }

// window.initMap_test = initMap_test;

