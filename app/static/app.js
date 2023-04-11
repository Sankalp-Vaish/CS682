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

async function setLocation() {
  const position = { lat: 37.42, lng: -122.08 };
  // Request needed libraries.
  const { Map } = await google.maps.importLibrary("maps");
  const { Marker } = await google.maps.importLibrary("marker");

  let map = new Map(document.getElementById("map-element"), {
    zoom: 8,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  const marker = new Marker({
    position: position,
    map: map,
    title: "San Jose",
  });

  marker.setMap(map);
}


let map, infoWindow;

async function initMap_cp() {
  const { Map } = await google.maps.importLibrary("maps");
  const { Marker } = await google.maps.importLibrary("marker");
  map = new google.maps.Map(document.getElementById("map-element"), {
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

function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 40.749933, lng: -73.98633 },
    zoom: 13,
    mapTypeControl: false,
  });
  const input = document.getElementById("pac-input");
  const options = {
    fields: ["formatted_address", "geometry", "name"],
    strictBounds: false,
    types: ["address"],
  };
  const autocomplete = new google.maps.places.Autocomplete(input, options);

  const marker = new google.maps.Marker({
    map,
    anchorPoint: new google.maps.Point(0, -29),
  });

  autocomplete.addListener("place_changed", () => {
    marker.setVisible(false);

    const place = autocomplete.getPlace();

    if (!place.geometry || !place.geometry.location) {
      // User entered the name of a Place that was not suggested and
      // pressed the Enter key, or the Place Details request failed.
      window.alert("No details available for input: '" + place.name + "'");
      return;
    }

    // If the place has a geometry, then present it on a map.
    if (place.geometry.viewport) {
      map.fitBounds(place.geometry.viewport);
    } else {
      map.setCenter(place.geometry.location);
      map.setZoom(17);
    }

    marker.setPosition(place.geometry.location);
    marker.setVisible(true);
    // infowindowContent.children["place-name"].textContent = place.name;
    // infowindowContent.children["place-address"].textContent = place.formatted_address;
    // infowindow.open(map, marker);
    marker.setMap(map);
  });
}






let slideIndex = 1
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

function initMapHomeEstimate() {
  const latvalues = document.getElementsByClassName("lat-value");
  const lonvalues = document.getElementsByClassName("lon-value");

  let coordinates = [];

  for (let i=0; i<latvalues.length; i++) {
    coordinates.push([latvalues[i].attributes.value.value, lonvalues[i].attributes.value.value]);
  }

  console.log(coordinates);

  const map = new google.maps.Map(document.getElementById("map-home-estimate"), {
    center: { lat: parseInt(coordinates[0][0]), lng: parseInt(coordinates[0][1]) },
    zoom: 15,
    mapTypeControl: false,
  });
  //const input = document.getElementById("pac-input");
  const options = {
    fields: ["formatted_address", "geometry", "name"],
    strictBounds: false,
    types: ["address"],
  };
  //const autocomplete = new google.maps.places.Autocomplete(input, options);

  setMarkers(map, coordinates);

}

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

window.initMapHomeEstimate = initMapHomeEstimate;