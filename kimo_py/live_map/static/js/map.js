
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
    console.log( " nr afisari 1");
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
console.log("nr afisari 2");
var listp = polygons.get_list();
  console.log(listp);


  for ( l=0; l< listp.length; l++)
    {

         console.log("creeam poligoane");
         addPolygon(map, listp[l].get_coordinates() ,listp[l].get_name(), listp[l].get_description() );

       }


  $("#informatii_copii > div").each(
  function(){
    console.log("copilasul nr 1");
      var lat = $(this).find(".z-longitudine").text();
      var lng = $(this).find(".z-latitudine").text();
      var nume=$(this).find(".z-nume").text();
      var prenume=$(this).find(".z-prenume").text();
      console.log(lat + "   " + lng);
      var coord =  new google.maps.LatLng(lng,lat);

      addMarker(map,coord,nume+" "+prenume,nume+" "+prenume);
  }

  )

console.log("nr afisari 3");


});





var marker= new Marker(47.158374,27.601104, "test2", "copil2");
var marker2 = new Marker(48.158374,28.601104, "test3", "copil3");


markers.add_marker(marker);
markers.add_marker(marker2);
var list = markers.get_list();

 for (i = 0; i < list.length; i++)
        addMarker(map, list[i].googleLatLng, list[i].title, list[i].content);

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

function addPolygon(map, coordinates, title, content){

 var shape = new google.maps.Polygon({
          paths: coordinates,
          strokeColor: '#FF0000',
          strokeOpacity: 0.8,
          strokeWeight: 2,
          fillColor: '#FF0000',
          fillOpacity: 0.35,
          title:'adasdas',
          content:'dasdasdas'
        });


       // console.log(listp[l].get_description());
        var c=coordinates;
        var x= 0.0;
        var y= 0.0;
        for( j=0; j < c.length ; j++)
                {
                   x=c[j].lat +x;
                   y=c[j].lng + y;
                }

        x=x/c.length;
        y=y/c.length;

        var infoWindow=new google.maps.InfoWindow({ content: content,
	                                               title: title,
	                                               position: new google.maps.LatLng(x,y)
	                                               });

        google.maps.event.addListener(shape, "click", function(){
		infoWindow.open(map);
		console.log("listener");
	});
        shape.setMap(map);



}




