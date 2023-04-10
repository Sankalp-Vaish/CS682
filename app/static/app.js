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

//house details map
async function setLocation(lati, lon) {
  $("#map-element").css({"height": "400px", "width": "550px"});
  console.log(lati);
  const position = { lat: lati, lng: lon };
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
    console.log(place.geometry.location.lat(), place.geometry.location.lng());
    marker.setVisible(true);
    // infowindowContent.children["place-name"].textContent = place.name;
    // infowindowContent.children["place-address"].textContent = place.formatted_address;
    // infowindow.open(map, marker);
    marker.setMap(map);
  });
}






// let slideIndex = 1
// showSlides(slideIndex);

// // Next/previous controls
// function plusSlides(n) {
//   showSlides(slideIndex += n);
// }

// // Thumbnail image controls
// function currentSlide(n) {
//   showSlides(slideIndex = n);
// }

// function showSlides(n) {
//   let i;
//   let slides = document.getElementsByClassName("mySlides");
//   let dots = document.getElementsByClassName("dot");
//   if (n > slides.length) {slideIndex = 1}
//   if (n < 1) {slideIndex = slides.length}
//   for (i = 0; i < slides.length; i++) {
//     slides[i].style.display = "none";
//   }
//   for (i = 0; i < dots.length; i++) {
//     dots[i].className = dots[i].className.replace(" active", "");
//   }
//   slides[slideIndex-1].style.display = "block";
//   dots[slideIndex-1].className += " active";
// }


$(document).ready(function(){
  console.log("in1");
  $("marquee img").mouseenter(function(){
    i=this.id;
    $("#"+String(i)).animate({height: '200px'});
    console.log("in");
  });
});


$(document).ready(function(){
  $("marquee img").mouseleave(function(){
    i=this.id;
    $("#"+String(i)).animate({height: '150px'});

  });
});


$(document).ready(function(){
  $(".result").each(function(i, obj){
    if ($(obj).text() >0){
      $(obj).css({"color": "green"})
    }
    else{
      $(obj).css({"color": "red"})
      $(obj).parent().css({"font-weight": "bold"})
    }
  });

});


// current location map
const options = {
  enableHighAccuracy: true,
  timeout: 5000,
  maximumAge: 0,
};

async function success(pos) {
  const crd = pos.coords;

  console.log("Your current position is:");
  console.log(crd.latitude);
  console.log(`Longitude: ${crd.longitude}`);
  console.log(`More or less ${crd.accuracy} meters.`);


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
