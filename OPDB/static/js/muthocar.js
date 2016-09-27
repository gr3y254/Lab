jQuery(function($) {
    // Asynchronously Load the map API 
    var script = document.createElement('script');
    script.src = "//maps.googleapis.com/maps/api/js?key=AIzaSyCtbktESE9MzMSsqpOvFyk_seI1GbAoVEQ &callback=myMap";
    document.body.appendChild(script);
});

