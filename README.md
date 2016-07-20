#Atlanta Transit Tool

The transit tool allows users to explore accessibility to jobs through public transit and walking in the Atlanta region. Click on the map or search for your address to see how many jobs are within range and what types of jobs they are.

#Run the tool

To run the tool, you must use one terminal window to start up the OTP graph engine, located in the backend directory. You can locally host the tool from another terminal window in the main directory.

##Start up OTP (Graph Engine)

### Quick Start

For user to be able to run the OTP tool, the steps mentioned below should be followed in the given order:

1) Put your open-street-map data here under otp folder:
    example: backend/otp/atlanta_georgia.osm.pbf

2) Put your GTFS data under otp folder:
    example: backend/otp/google_transit.zip

3) When in the backend folder, run the following Java command to build the graph in memory and run the server (it takes a few minutes to build the graph):

  java -Xmx2G -jar otp-0.19.0-shaded.jar --build otp --inMemory

### Make it faster!

To do a quicker run of the tool, build the graph only the first time and run load from the graph afterward. 
Put your graph object under backend/otp/graphs/1 and run this:

java -cp otp-0.19.0-shaded.jar org.opentripplanner.standalone.OTPMain --graphs otp/graphs/ --router 1 --server --analyst

To see a full list of options, add --help to the end of the command.

##Host the transit tool

1) Start a local server to access the tool:
	using Python 2: `python -m SimpleHTTPServer`
	using Python 3: `python -m http.server 8000`

2) Browse to http://localhost:8000/ and have fun!

