
function myMap() {
var mapProp= {
    center:new google.maps.LatLng(47.158374,27.601104),
    zoom:13,
};
var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);



var marker= new Marker(47.158374,27.601104, "test2", "copil2");
var marker2 = new Marker(48.158374,28.601104, "test3", "copil3");


var markers = new Markers();
markers.add_marker(marker);
markers.add_marker(marker2);
var list = markers.get_list();

 for (i = 0; i < list.length; i++)
        addMarker(map, list[i].googleLatLng, list[i].title, list[i].content);

var polygon = addShape(map);


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
		infoWindow.open();
	});
}


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
           strokeColor: '#FF0000'
          }
        });
       google.maps.event.addListener(drawingManager, 'overlaycomplete', function(polygon) {
    var coordinatesArray = polygon.overlay.getPath().getArray();
    polygon = new Polygon();
    polygon.add_points(coordinatesArray);
    console.log(',')
});

        drawingManager.setMap(map);

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
    this.dangerArea= are;
    }
    get_list(){
    return this.dangerArea;
    }
}