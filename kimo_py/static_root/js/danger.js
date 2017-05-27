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





function dangerMap() {
var mapProp= {
    center:new google.maps.LatLng(47.158374,27.601104),
    zoom:13,
};
var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);

addShape(map);
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