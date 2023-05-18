$(document).ready(function(){
    //console.log("in1");
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

// image slideshow
let slideIndex = 1;
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
  //let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
    slides[i].style.opacity = "0";
  }
  // for (i = 0; i < dots.length; i++) {
  //   dots[i].className = dots[i].className.replace(" active", "");
  // }
  slides[slideIndex-1].style.display = "block";
  slides[slideIndex-1].style.opacity = "1";
  // dots[slideIndex-1].className += " active";
}


//house details map
async function setLocation(lati, lon) {
  $("#map-element").css({"height": "200px", "width": "400px"});
  console.log(lati);
  const position = { lat: lati, lng: lon };
  // Request needed libraries.
  const { Map } = await google.maps.importLibrary("maps");
  const { Marker } = await google.maps.importLibrary("marker");

  let map = new Map(document.getElementById("map-element"), {
    zoom: 15,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  const marker = new Marker({
    position: position,
    map: map,
  });

  marker.setMap(map);
}