# taxivgml
This Python script converts Montreal taxi station XML file to KML (Keyhole Markup Language). KML is an OSM (Open Street Map) readable format (Ref. https://wiki.openstreetmap.org/wiki/KML)

The source file taxi_vgml.asp.xml was downloaded from the following link http://applicatif.ville.montreal.qc.ca/e-cite/kml/taxi_vgml.asp

Once the KML file is generated we upload the data to OSM to contribute to the Open Geospacial Data of Montreal area.

In order to contribute we need to respect a list of guidelines found in the OSM Wiki: https://wiki.openstreetmap.org/wiki/Import/Guidelines

Below is the email that was sent to the imports@openstreetmap.org mailing list.

Hi,

At la Fabrique des mobilités Québec we would like to upload the Montreal Taxi stations which are available in an XML format on http://applicatif.ville.montreal.qc.ca/e-cite/kml/taxi_vgml.asp

According to the community guidelines we created a OSM account for this upload using the email address taxivdml@gmail.com and we ask for approval from the community on the necessity to add this data to the OSM database.

Taxi stations are identified with a unique id in the name field and a service status in the iconID (example value public_actif can be related to the corresponding icon in the icons feature within the same file). More information about the station is available in the description section within the placemark, location address, type, status, number of places and operation time. The geolocation coordinates are available in the coordinates section.

<Placemark>
<name>27-474</name>
<info_side_bar>
</info_side_bar>
<visibility>0</visibility>
<description>
<table id='description_carte'><tr><td><div id="localisation"><p>Chabanel O. / St-Urbain</p> <p>Situ&#233; au nord-est de l'intersection sur Chabanel O.</p></div><div id="type"><b>Type</b> : Public</div><div id="statut"></div><div id="statut_texte"></div><div id="nb_place"><b>Nombre de places :</b> 4</div><div id="heure_operation"><b>Heure d'operations : </b></div></td></tr></table>
</description>
<iconID>public_actif</iconID>
<Point>
<coordinates>-73.65204925767212,45.54302132777408</coordinates>
</Point>
</Placemark>

We understand that we should convert data to a more suitable format such as JOSM format and upload data using a tool such as https://wiki.openstreetmap.org/wiki/JOSM or Upload.py https://wiki.openstreetmap.org/wiki/Upload.py.

Please let us know if there are any advices we should follow.

Regards,

La Fabrique des mobilités Québec

We created a sample map by importing the data using KML format. The icons are not correcté.
https://umap.openstreetmap.fr/en/map/postes-dattente-ville-de-montreal_738554#14/45.5238/-73.5810

## Taxi tag
https://wiki.openstreetmap.org/wiki/Tag:amenity=taxi?uselang=en

## Montreal Open Data

Taxi waiting stations are also available in CSV, GeoJSON and SHP formats

https://donnees.montreal.ca/bureau-du-taxi-de-montreal/postes-attente-taxi


## Modified fiels

We kept fiels MTM8_X and MTM8_Y as reference to the NAD83(CSRS98) / MTM zone 8  https://epsg.io/2145