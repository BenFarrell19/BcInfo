const hamburger = document.getElementById('hamburger')
hamburger.addEventListener('click', function(e) {
    const ul = document.querySelector('nav > ul');
    ul.classList.toggle('menu-slide');
    hamburger.classList.toggle('cross')
});

document.querySelectorAll('.nav-link').forEach(
  link => {
    if(link.href===window.location.href){
      link.setAttribute('aria-current', 'page')
    }
  }
)

mapboxgl.accessToken = 'pk.eyJ1IjoiYmVuZjc5NyIsImEiOiJjbGNlYmhsdzQycmkzM3FsN3UwbGdidDJjIn0.4mBRr3Jfb7xYo9mjYwgvOg';
var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/satellite-v9',
  center: [-110.9621, 45.4387],
  zoom: 9
});


/*
var route_arr = ['10602.geojson', 'LickCreek.json', 'Zipper.json']

for (let i = 0; i < route_arr.length; i++) {
  map.on('load', () => {

    map.addSource(route_arr[i], {
    'type': 'geojson',
    'data': route_arr[i]
    });
    map.addLayer({
    'id': route_arr[i],
    'type': 'line',
    'source': route_arr[i],
    'layout': {
    'line-join': 'round',
    'line-cap': 'round'
    },
    'paint': {
    'line-color': '#888',
    'line-width': 4
    }
    });
    });
}
*/

var total = 'Collective.json';

map.on('load', () => {

  map.addSource('total', {
  'type': 'geojson',
  'data': total
  });
  map.addLayer({
  'id': 'total',
  'type': 'line',
  'source': 'total',
  'layout': {
  'line-join': 'round',
  'line-cap': 'round'
  },
  'paint': {
  'line-color': '#888',
  'line-width': 4
  }
  });
  });




var geojson = {
    "type": "FeatureCollection",
    "name": "mapbox",
    "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
    "features": [
    { "type": "Feature", "properties": { "Name": "Zipper", "description": null }, "geometry": { "type": "Point", "coordinates": [ -110.973304519905795, 45.469400517959222 ] } },
    { "type": "Feature", "properties": { "Name": "Blackmore", "description": null }, "geometry": { "type": "Point", "coordinates": [ -111.001350899051403, 45.445741476949998 ] } },
    { "type": "Feature", "properties": { "Name": "History Rock", "description": null }, "geometry": { "type": "Point", "coordinates": [ -111.0102053425246, 45.486700809788637 ] } },
    { "type": "Feature", "properties": { "Name": "Lick Creek", "description": null }, "geometry": { "type": "Point", "coordinates": [ -110.958456310067703, 45.521250500414737 ] } },
    { "type": "Feature", "properties": { "Name": "Hyalite Peak", "description": "Hyalite Peak" }, "geometry": { "type": "Point", "coordinates": [ -110.9610, 45.382 ] } },
    ]
    }

// working on removing routes on zoom as well
    
var currentMarkers=[];
// add markers to map
for (const feature of geojson.features) {
  // create a HTML element for each feature
  const el = document.createElement('div');
  el.className = 'marker';
  

  // make a marker for each feature and add to the map
  var oneMarker= new mapboxgl.Marker(el).setLngLat(feature.geometry.coordinates).addTo(map);
  currentMarkers.push(oneMarker);
}

const that = this;
      map.on('zoom', () => {
  const zoom = map.getZoom();
  if (zoom <=9.5) {
    for (var i = currentMarkers.length - 1; i >= 0; i--) {
      currentMarkers[i].remove();
    }
  }
  if (zoom >9.5) {
    for (var i = currentMarkers.length - 1; i >= 0; i--) {
      currentMarkers[i].addTo(map);
    }
  }
});





var slider = document.getElementById("slider");
var output = document.getElementById("distance");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value;
}

var sliderv = document.getElementById("sliderv");
var outputt = document.getElementById("vert");
outputt.innerHTML = sliderv.value;

sliderv.oninput = function() {
  outputt.innerHTML = this.value;
}