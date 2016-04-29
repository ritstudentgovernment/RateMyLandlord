/**
 * Created by Aaron on 4/23/2016.
 */
var map;
var markers = [];
var location;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: {lat: 43.084448, lng: -77.676387},
        zoom: 10,
        mapTypeControl: true,
        navigationControlOptions: {style:google.maps.NavigationControlStyle.SMALL}
    });
    //Put marker at user's location

    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position){
            markers.push(new google.maps.Marker({position: {lat: position.coords.latitude, lng: position.coords.longitude},
                map: map,
                title: "Your location"}));
        });
    }
    else{
        markers.push(new google.maps.Marker({position: {lat: 43.084448, lng: -77.676387},
                map: map,
                title: "RIT"}));
    }

    if(markerInfo) {
        for (var i = 0; i < markerInfo.length; i++) {
            markers.push(new google.maps.Marker({
                position: {lat: markerInfo[i].latitude, lng: markerInfo[i].longitude},
                map: map,
                title: markerInfo[i].title
            }));
        }
    }
    console.log(markers.length);
    markerInfo = [];
}


