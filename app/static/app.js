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

function setLocation() {
  var directionsDisplay = new google.maps.DirectionsRenderer;
  var mapElement = document.getElementById('map');

  // mapElement.addEventListener('click', function() {
  //   myFunction();
  // });

  let map = new google.maps.Map(mapElement, {
    center: {lat: 37.42, lng:  -122.08},
    zoom: 8
  });
  directionsDisplay.setMap(map);

  // var marker = new google.maps.Marker({
  //   position: {lat: 37.77, lng: -122.41},
  //   map: map,
  //   title: 'San Francisco'
  // });
  
  // return marker;
}