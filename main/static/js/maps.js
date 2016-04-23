/**
 * Created by Aaron on 4/23/2016.
 */
var map;
var marker;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: {lat: -34.397, lng: 150.644},
        zoom: 8,
        mapTypeControl: true,
        navigationControlOptions: {style:google.maps.NavigationControlStyle.SMALL}
    });

    marker = new google.maps.Marker({position:{lat: -34.397, lng: 150.644}, map:map, title:"Look a marker!"});
}
