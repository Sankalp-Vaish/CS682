//$(document).ready(function myFunction3(){
function myFunction3() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    console.log(filter);
    tr = document.getElementsByClassName("head");
    console.log("63");
    console.log(tr);
    //tr = table.getElementsByTagName("span");
    //console.log(tr.length)
  
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
      //console.log(tr[1].innerText);
      //console.log(tr[1].firstChild);
      //h4 = tr[i].getElementsByTagName("h4");
      //console.log(h4.textContent, h4.innerText, h4.value, h4.txtValue);
      td = tr[i];
      if (td) {
        txtValue = td.textContent || td.innerText;
        
        disp=tr[i].parentElement.parentElement.parentElement.parentElement.parentElement;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          console.log(tr[i].parentElement.parentElement.parentElement.parentElement.parentElement);
          
          disp.style.display = "";
        } else {
          disp.style.display = "none";
        }
      }
    }
  }
//});

// $(document).ready(function myFunction3(){
// $("#myInput").onk
// });

// function sort_ascending(){
//   var i,j;
//   const tr = document.getElementsByClassName("head");
//   for (i = 0; i < (tr.length-1); i++) {
//     //tr = document.getElementsByClassName("head");
//     min=tr[i];
//     for (j=1; j< tr.length; j++){
//       td=tr[j];
//       if (td.innerText.toUpperCase() < min.innerText.toUpperCase()) {
//         d1=td.parentElement.parentElement.parentElement.parentElement.parentElement;
//         d2=min.parentElement.parentElement.parentElement.parentElement.parentElement;
//         console.log(tr[i].parentElement.parentElement.parentElement.parentElement.parentElement);
//         d1.parentNode.insertBefore(d1,d2)
//         min=td
//       }
//     }
//     // d1=tr[i].parentElement.parentElement.parentElement.parentElement.parentElement;
//     // d2=min.parentElement.parentElement.parentElement.parentElement.parentElement;
//     // console.log(d1);
//     // //console.log(d1.parentNode);
//     // d1.parentNode.insertBefore(d1,d2)
//   }
// }

function sort_ascending(){
  var j;
  const tr = document.getElementsByClassName("head");
  switching = true;
  while (switching) {
    switching = false;
    for (j=0; j< tr.length-1; j++){
      if (tr[j].innerText.toUpperCase() > tr[j+1].innerText.toUpperCase()) {
        switching = true;
        break;
      }
    }
    if (switching){
      d1=tr[j+1].parentElement.parentElement.parentElement.parentElement.parentElement;
      d2=tr[j].parentElement.parentElement.parentElement.parentElement.parentElement;
      d1.parentNode.insertBefore(d1,d2)
    }
  }
}

function sort_descending(){
  var j;
  const tr = document.getElementsByClassName("head");
  switching = true;
  while (switching) {
    switching = false;
    for (j=0; j< tr.length-1; j++){
      if (tr[j].innerText.toUpperCase() < tr[j+1].innerText.toUpperCase()) {
        switching = true;
        break;
      }
    }
    if (switching){
      d1=tr[j+1].parentElement.parentElement.parentElement.parentElement.parentElement;
      d2=tr[j].parentElement.parentElement.parentElement.parentElement.parentElement;
      d1.parentNode.insertBefore(d1,d2)
    }
  }
}

// function sort_descending(){
//   tr = document.getElementsByClassName("head");
//   min=tr[0];
//   for (i = 1; i < tr.length; i++) {
//     td=tr[i];
//     if (td.innerText.toUpperCase() > min.innerText.toUpperCase()) {
//       d1=td.parentElement.parentElement.parentElement.parentElement.parentElement;
//       d2=min.parentElement.parentElement.parentElement.parentElement.parentElement;
//       console.log(d1.parentNode);
//       d1.parentNode.insertBefore(d1,d2)
//       min=td;
//     }
//   }
// }

// function sort_price(){
//   tr = document.getElementsByClassName("list_price");
//   min=tr[0];
//   for (i = 1; i < tr.length; i++) {
//     td=tr[i];
//     if (td.innerText.toUpperCase() > min.innerText.toUpperCase()) {
//       d1=td.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
//       d2=min.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
//       console.log(d1.parentNode);
//       d1.parentNode.insertBefore(d1,d2)
//       min=td;
//     }
//   }
// }
let flag=false;
function sort_price(){
  flag=!flag
  var j;
  const tr = document.getElementsByClassName("list_price");
  switching = true;
  while (switching) {
    switching = false;
    for (j=0; j< tr.length-1; j++){
      if (flag){
        if (parseInt(tr[j].innerText.toUpperCase()) > parseInt(tr[j+1].innerText.toUpperCase())) {
          switching = true;
          break;
        }
      }
      else{
        if (parseInt(tr[j].innerText.toUpperCase()) < parseInt(tr[j+1].innerText.toUpperCase())) {
          switching = true;
          break;
        }
      }
    }
    if (switching){
      d1=tr[j+1].parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
      d2=tr[j].parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
      d1.parentNode.insertBefore(d1,d2)
    }
  }
}

// let flag_year=false;
// function sort_year(){
//   flag_year=!flag_year
//   var j;
//   const tr = document.getElementsByClassName("list_year");
//   //console.log(tr);
//   switching = true;
//   while (switching) {
//     switching = false;
//     for (j=0; j< tr.length-1; j++){
//       if (flag_year){
//         if (parseInt(tr[j].innerText.toUpperCase()) > parseInt(tr[j+1].innerText.toUpperCase())) {
//           console.log(parseInt(tr[j].innerText.toUpperCase())) ;
//           switching = true;
//           break;
//         }
//       }
//       else{
//         if (parseInt(tr[j].innerText.toUpperCase()) < parseInt(tr[j+1].innerText.toUpperCase())) {
//           console.log(parseInt(tr[j].innerText.toUpperCase())) ;
//           switching = true;
//           break;
//         }
//       }
//     }
//     if (switching){
//       console.log("switch");
//       d1=tr[j+1].parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
//       d2=tr[j].parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
//       console.log(d1);
//       d1.parentNode.insertBefore(d1,d2)
//     }
//   }
// }