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

var elem = document.getElementById("divform");
//elem.style.display = "none";
//elem.style.visibility = "hidden";
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
            var p=0;
            polygon = new Polygon();
            polygon.add_points(coordinatesArray);
            for(i=0; i<coordinatesArray.length;i++)
             {
                 console.log( coordinatesArray[i]+ '   ');
             }
            console.log(',')
            elem.style.visibility = "visible";

            document.getElementById("submitbt").addEventListener("click", function(){
                 var name = document.getElementById("name").value;
                 var description = document.getElementById("description").value;
                 console.log(name);
                 console.log(description);

              //  document.name.value='';
                // description.value='';
                p=p+1
                console.log(p);
                var obj= new Object();
                obj.name=name;
                obj.description=description;
                obj.coordinates=polygon.get_list();

                var jsonString= JSON.stringify(obj);

               // post('http://127.0.0.1:8000/live_map/', jsonString);
                console.log(jsonString);
                document.getElementById("json").value=jsonString;
                console.log(document.getElementById("json").value);
                 elem.style.visibility = "hidden";
                });


            //var name = document.getElementById("name").value;
           // var description = document.getElementById("description").value;
           // console.log(name);



});

        drawingManager.setMap(map);

}




function post(path, params, method) {
    method = method || "post"; // Set method to post by default if not specified.

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
         }
    }

    document.body.appendChild(form);
    form.submit();
}