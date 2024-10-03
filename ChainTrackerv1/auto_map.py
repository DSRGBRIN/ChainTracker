"""
Modul to generate map with trajectory
"""
HEADER0 = """<html>
<head>
<meta http-equiv="refresh" content=\""""
# 6
HEADER1 = """\">
<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
<title>BIoV Tracker</title>


<script type="text/javascript">
    function addScript( url, callback ) {
        var script = document.createElement( 'script' );
        if( callback ) script.onload = callback;
        script.type = 'text/javascript';
        script.src = url;
        document.body.appendChild( script );
    }
    function initLoad() {
        addScript( 'https://maps.googleapis.com/maps/api/js?key=AIzaSyDpnuP0pRGFFN9agYXHWrpRWuAHG79ai5E&loading=async&callback=initMap&v=weekly&libraries=marker' );
    };
    function initMap() {
        var map = new google.maps.Map(document.getElementById("map_canvas"), {
            zoom: 18,
            center: new google.maps.LatLng("""
# -6.906158, 107.612273
HEADER2 = """),
            mapId: 'DEMO_MAP_ID'
        });

        new google.maps.marker.AdvancedMarkerElement({
            map,
            position: new google.maps.LatLng("""
# -6.906158, 107.612273
HEADER3 = """)
            //title: 'Uluru',
        });

        new google.maps.Polyline({
            clickable: false,
            geodesic: true,
            strokeColor: "#6495ED",
            strokeOpacity: 1.000000,
            strokeWeight: 2,
            map: map,
            path: ["""
# new google.maps.LatLng(-6.912475, 107.606012),
FOOTER1 = """            ]
        });

    }
</script>
</head>
<body style="margin:0px; padding:0px;" onload="initLoad()">
    <div id="map_canvas" style="width: 100%; height: 100%;" />
</body>
</html>"""
