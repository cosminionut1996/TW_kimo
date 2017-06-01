
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
     this.name='';
     this.description='';

     }
     add_points(latlong, name2 , desc){
     this.pointList=latlong;
     this.name=name2;
     this.description=desc;
     }
     get_coordinates(){
     return this.pointList;
     }
     get_name(){
     return this.name;
     }
     get_description(){
     return this.description;
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
    //console.log("in jquery");
      var name = $(this).find(".z-name").text();
      var description = $(this).find(".z-description").text();
      var coordinates3 = $(this).find(".z-coordinates").text();
      var coordinates2 = coordinates3.replace(/[\[\]\\\/]/gi, '');
      var coordinates3 = coordinates2.replace(new RegExp(", {", "g"),'@{');
      var coordinates2 = coordinates3.replace(/'/g,'"');
      //console.log(coordinates2);
      var array = coordinates2.split("@");
      //console.log(name + description + coordinates);
      //console.log(coordinates3+ " aici ne uitam");
      var coordinates = new Array();
      for ( k=0; k<array.length;k++){
            console.log(array[k] + "   "+ k);
            var obj=JSON.parse(array[k]);
            coordinates.push(obj);
        }

     // console.log(coordinates3);
      var polygon=new Polygon();
      polygon.add_points(coordinates, name, description);
      //console.log(polygon.get_description()+"   "+ polygon.get_coordinates());
      polygons.add_area(polygon);
      console.log("gata iteratia");
    }
  );

  var listp = polygons.get_list();
  console.log(listp);
  //console.log(list_puncte);
 // for (k =0; k<list_puncte.length;k ++)
   //     console.log(list_puncte[k]);




  for ( l=0; l< listp.length; l++)
    {
          var shape = new google.maps.Polygon({
          paths: listp[l].get_coordinates(),
          strokeColor: '#FF0000',
          strokeOpacity: 0.8,
          strokeWeight: 2,
          fillColor: '#FF0000',
          fillOpacity: 0.35,
          title:'adasdas',
          content:'dasdasdas'
        });
        console.log("am trecut pe aici");
        var infoWindow=new google.maps.InfoWindow({ content: 'sadasdas',
	                                               title: 'dsadasd',
	                                               //aici se pun coordonatele
	                                               });

        google.maps.event.addListener(shape, "click", function(){
		infoWindow.open(map);
	});
        shape.setMap(map);

       }

});


var marker= new Marker(47.158374,27.601104, "test2", "copil2");
var marker2 = new Marker(48.158374,28.601104, "test3", "copil3");

var p1= new Polygon();
var p2= new Polygon();

p1.add_points([
          {lat: 47.16707628945532 , lng: 27.611045837402344},
          {lat: 47.15190231842864, lng: 27.611560821533203},
          {lat: 47.16334156019606, lng: 27.630271911621094}
        ],"zona1","pericol");
 polygons.add_area(p1);



 //for ( j=0; j<list2.length;j++)
 //   console.log(list2[j].get_coordinates());
//console.log(list2[0].get_coordinates() + "aici");

markers.add_marker(marker);
markers.add_marker(marker2);
var list = markers.get_list();

 for (i = 0; i < list.length; i++)
        addMarker(map, list[i].googleLatLng, list[i].title, list[i].content);

//addShape(map);
/*
var string = "[{lat: 47.16707628945532 , lng: 27.611045837402344},{lat: 47.15190231842864, lng: 27.611560821533203},{lat: 47.16334156019606, lng: 27.630271911621094}] ";
var array = string.split("},");
if(array.isArray==1)
    console.log("este array1");
alert(array[0]);*/

var list2= polygons.get_list();
console.log("ala bun");
console.log(list2);
console.log("ala bun");
var arr = new Array();
arr.push("buna");
for ( l=0; l< list2.length; l++)
    {
          var shape = new google.maps.Polygon({
          paths: list2[l].get_coordinates(),
          strokeColor: '#FF0000',
          strokeOpacity: 0.8,
          strokeWeight: 2,
          fillColor: '#FF0000',
          fillOpacity: 0.35,
          title:'adasdas',
          content:'dasdasdas'
        });
        console.log("am trecut pe aici");
        var infoWindow=new google.maps.InfoWindow({ content: 'sadasdas',
	                                               title: 'dsadasd',
	                                               //aici se pun coordonatele
	                                               });

        google.maps.event.addListener(shape, "click", function(){
		infoWindow.open(map);
	});
        shape.setMap(map);

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
