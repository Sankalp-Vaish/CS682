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