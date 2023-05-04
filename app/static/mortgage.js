let popup, Popup;

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

      /**
      * A customized popup on the map.
      */
      class Popup extends google.maps.OverlayView {
        position;
        containerDiv;
        constructor(position, content, betterValue) {
          super();
          this.position = position;
          content.classList.add("popup-bubble");

          // This zero-height div is positioned at the bottom of the bubble.
          const bubbleAnchor = document.createElement("div");

          bubbleAnchor.classList.add("popup-bubble-anchor");
          bubbleAnchor.appendChild(content);
          // This zero-height div is positioned at the bottom of the tip.
          this.containerDiv = document.createElement("div");
          this.containerDiv.classList.add("popup-container");
          this.containerDiv.appendChild(bubbleAnchor);

          // Adding classes for color
          if (betterValue == true) {
            content.classList.add("real-good");
            bubbleAnchor.classList.add("real-good");
          } else {
            content.classList.add("real-bad");
            bubbleAnchor.classList.add("real-bad");
          }

          // Optionally stop clicks, etc., from bubbling up to the map.
          Popup.preventMapHitsAndGesturesFrom(this.containerDiv);
        }
        /** Called when the popup is added to the map. */
        onAdd() {
          this.getPanes().floatPane.appendChild(this.containerDiv);
        }
        /** Called when the popup is removed from the map. */
        onRemove() {
          if (this.containerDiv.parentElement) {
            this.containerDiv.parentElement.removeChild(this.containerDiv);
          }
        }
        /** Called each frame when the popup needs to draw itself. */
        draw() {
          const divPosition = this.getProjection().fromLatLngToDivPixel(
            this.position
          );
          // Hide the popup when it is far out of view.
          const display =
            Math.abs(divPosition.x) < 4000 && Math.abs(divPosition.y) < 4000
              ? "block"
              : "none";

          if (display === "block") {
            this.containerDiv.style.left = divPosition.x + "px";
            this.containerDiv.style.top = divPosition.y + "px";
          }

          if (this.containerDiv.style.display !== display) {
            this.containerDiv.style.display = display;
          }
        }
      }

      // const marker = new google.maps.Marker({
      //   map,
      //   anchorPoint: new google.maps.Point(0, -29),
      // });
      for (let i = 0; i < coordinates.length; i++) {
        const coordinate = coordinates[i];
        // console.log(coordinate);

        // const contentString =
        //   '<div id="content">' +
        //   '<div id="bodyContent">' +
        //   "<p><b>Cash on Cash ROI: " + (cash[i].attributes.value.value).toString() + "</b></p>" +
        //   "</div>" +
        //   "</div>";

        const valueString = document.createElement("p");
        valueString.textContent = "$ : " + (cash[i].attributes.value.value).toString();
        const contentString = document.createElement("div");
        contentString.appendChild(valueString);

        const domElement = new DOMParser().parseFromString(contentString, "text/xml");

        const infowindow = new google.maps.InfoWindow({
          content: contentString,
          ariaLabel: "Uluru",
        });

        let betterValue = false;
        if (cash[i].attributes.value.value > 0) {
          betterValue = true;
        }

        popup = new Popup(
          new google.maps.LatLng(parseFloat(coordinate[0]), parseFloat(coordinate[1])),
          contentString, betterValue
        );
        popup.setMap(map);

        console.log(popup);

        // const marker = new google.maps.Marker({
        //   map,
        //   //anchorPoint: new google.maps.Point(0, -29),
        //   position: { lat: parseFloat(coordinate[0]), lng: parseFloat(coordinate[1]) },
        //   //title: i.toString(),
        //   //label: (cash[i].attributes.value.value).toString(),
        // });

        // marker.addListener("click", () => {
        //   infowindow.open({
        //     anchor: marker,
        //     map,
        //   });
        // });
        // map.setZoom(13);
        //var myLatlng = new google.maps.LatLng(parseFloat(coordinate[0]),parseFloat(coordinate[1]));
        //marker.setPosition(myLatlng);
        //marker.setVisible(true);
        //marker.setMap(map);
      }

      autocomplete.addListener("place_changed", () => {
        const marker = new google.maps.Marker({
          map,
        });
        //marker.setVisible(false);
    
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