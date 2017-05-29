
class Marker {

  constructor(lat, long, title, content) {
    this.googleLatLng =  new google.maps.LatLng(lat,long);
    this.title= title;
    this.content = content;
  }

}




class Markers {

     constructor(){
     this.markerList= new Array();

     }
     add_marker(marker){
     this.markerList.push(marker);
     }
     get_list(){
     return this.markerList;
     }


}



class Polygon {

     constructor(){
     this.pointList= new Array();

     }
     add_points(latlong){
     this.pointList=latlong;
     }
     get_list(){
     return this.pointList;
     }


}

class Polygons {

    constructor(){
    this.dangerArea= new Array();
    }
    add_area( area){
    this.dangerArea.push(area);
    }
    get_list(){
    return this.dangerArea;
    }
}



var markers = new Markers();

var polygons = new Polygons();


function myMap() {
var mapProp= {
    center:new google.maps.LatLng(47.158374,27.601104),
    zoom:13,
};
var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);
var lat=new google.maps.LatLng(47.158374,27.601104);

//var informatii=new google.maps.Map(document.getElementById("informatii"),mapProp);
//var informatii = document.getElementById("name").value;
//console.log(informatii);
//var MyDiv1 = document.getElementById("informatii");


$(document).ready(function(){
console.log($("#informatii").size());
  $("#informatii > div").each(
    function() {
      var name = $(this).find(".z-name").text();
      var description = $(this).find(".z-description").text();
      var coordinates = $(this).find(".z-coordinates").text();
      console.log(name + description + coordinates);
    }
  );
});


var marker= new Marker(47.158374,27.601104, "test2", "copil2");
var marker2 = new Marker(48.158374,28.601104, "test3", "copil3");

var p1= new Polygon();
var p2= new Polygon();

p1.add_points([
          {lat: 47.16707628945532 , lng: 27.611045837402344},
          {lat: 47.15190231842864, lng: 27.611560821533203},
          {lat: 47.16334156019606, lng: 27.630271911621094}
        ]);
 polygons.add_area(p1);

 var list2=polygons.get_list();

console.log(list2.length);
markers.add_marker(marker);
markers.add_marker(marker2);
var list = markers.get_list();

 for (i = 0; i < list.length; i++)
        addMarker(map, list[i].googleLatLng, list[i].title, list[i].content);

//addShape(map);

for( j=0; j<list2.length; j++)
    {
        var shape = new google.maps.Polygon({
          paths: list2[j].get_list(),
          strokeColor: '#FF0000',
          strokeOpacity: 0.8,
          strokeWeight: 2,
          fillColor: '#FF0000',
          fillOpacity: 0.35,
          title:'adasdas',
          content:'dasdasdas'
        });
        var coord=0;
        var puncte = list2[j].get_list();

        var infoWindow=new google.maps.InfoWindow({ content: 'sadasdas',
	                                               title: 'dsadasd',
	                                               //aici se pun coordonatele
	                                               });

        google.maps.event.addListener(shape, "click", function(){
		infoWindow.open(map);
	});
        shape.setMap(map);
        console.log('asdasdas');
    }


}



function addMarker(map, googleLatLng, title, content){

	var markerOptn={
position:googleLatLng,
map:map,
title:title,
animation:google.maps.Animation.DROP
	};

	var marker=new google.maps.Marker(markerOptn);

	var infoWindow=new google.maps.InfoWindow({ content: content,
	                                               position: googleLatLng});
    google.maps.event.addListener(marker, "click", function(){
		infoWindow.open(map);
	});
}






function addShape(map){

var drawingManager = new google.maps.drawing.DrawingManager({

          drawingControl: true,
          drawingControlOptions: {
            position: google.maps.ControlPosition.TOP_CENTER,
            drawingModes: [ 'polygon']
          },
          polygonOptions:{
           fillColor: '#FF0000',
           strokeWeight: 2,
           strokeColor: '#FF0000',

          }
        });
       google.maps.event.addListener(drawingManager, 'overlaycomplete', function(polygon) {
    var coordinatesArray = polygon.overlay.getPath().getArray();
    polygon = new Polygon();
    polygon.add_points(coordinatesArray);
    for(i=0; i<coordinatesArray.length;i++)
    {
       console.log( coordinatesArray[i]+ '   ');
    }
    console.log(',')
});

        drawingManager.setMap(map);

}
