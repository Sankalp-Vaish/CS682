function initMap() {
    const cash =document.getElementsByClassName("cashflow");
    for (let i=0; i<cash.length; i++) {
      console.log(cash[i].attributes.value.value);
    }
    const latvalues = document.getElementsByClassName("lat-value");
    const lonvalues = document.getElementsByClassName("lon-value");
    console.log("2");
    let coordinates = [];
  
    for (let i=0; i<latvalues.length; i++) {
      coordinates.push([latvalues[i].attributes.value.value, lonvalues[i].attributes.value.value]);
      // console.log([latvalues[i].attributes.value.value, lonvalues[i].attributes.value.value]);
    }
    // console.log(coordinates);
    const mapElement = document.getElementById("map-home-estimate");

    if (mapElement) {
      const map = new google.maps.Map(document.getElementById("map-home-estimate"), {
        center: { lat: parseFloat(coordinates[0][0]), lng: parseFloat(coordinates[0][1]) },
        zoom: 10,
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
      for (let i = 0; i < coordinates.length; i++) {
        const coordinate = coordinates[i];
        // console.log(coordinate);

        const contentString =
          '<div id="content">' +
          '<div id="bodyContent">' +
          "<p><b>Cash on Cash ROI: " + (cash[i].attributes.value.value).toString() + "</b></p>" +
          "</div>" +
          "</div>";

        const infowindow = new google.maps.InfoWindow({
          content: contentString,
          ariaLabel: "Uluru",
        });

        const marker = new google.maps.Marker({
          map,
          //anchorPoint: new google.maps.Point(0, -29),
          position: { lat: parseFloat(coordinate[0]), lng: parseFloat(coordinate[1]) },
          //title: i.toString(),
          //label: (cash[i].attributes.value.value).toString(),
        });

        marker.addListener("click", () => {
          infowindow.open({
            anchor: marker,
            map,
          });
        });
        map.setZoom(13);
        //var myLatlng = new google.maps.LatLng(parseFloat(coordinate[0]),parseFloat(coordinate[1]));
        //marker.setPosition(myLatlng);
        //marker.setVisible(true);
        //marker.setMap(map);
      }

      autocomplete.addListener("place_changed", () => {
        marker.setVisible(false);
    
        const place = autocomplete.getPlace();
    
        if (!place.geometry || !place.geometry.location) {
          // User entered the name of a Place that was not suggested and
          // pressed the Enter key, or the Place Details request failed.
          window.alert("No details available for input: '" + place.name + "'");
          return;
        }
        console.log("149");
        // If the place has a geometry, then present it on a map.
        if (place.geometry.viewport) {
          map.fitBounds(place.geometry.viewport);
        } else {
          map.setCenter(place.geometry.location);
          map.setZoom(10);
        }
    
    
        marker.setPosition(place.geometry.location);
        // console.log(place.geometry.location.lat(), place.geometry.location.lng());
        marker.setVisible(true);
        // infowindowContent.children["place-name"].textContent = place.name;
        // infowindowContent.children["place-address"].textContent = place.formatted_address;
        // infowindow.open(map, marker);
        //marker.setMap(map);
        //initMapHomeEstimate()
      });
    }   
  }

  //window.initMap = initMap;