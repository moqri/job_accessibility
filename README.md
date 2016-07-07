#Start up OTP (Graph Engine)
## Quick Start

For user to be able to run the OTP tool, the steps mentioned below should be followed in the given order:

1) Put your open-street-map data here under otp folder:
    example: backend/otp/atlanta_georgia.osm.pbf

2) Put your GTFS data under otp folder:
    example: backend/otp/google_transit.zip

3) When in the backend folder, run the following Java command to build the graph in memory and run the server (it takes a few minutes to build the graph):

  java -Xmx2G -jar otp-0.19.0-shaded.jar --build otp --inMemory

4) The server runs on port 8080 on default. Browse to http://localhost:8080/ and enjoy!

## Make it faster!

To do a quicker run of the tool, build the graph only the first time and run load from the graph afterward. 
Put your graph object under backend/otp/graphs/1 and run this:

java -cp otp-0.19.0-shaded.jar org.opentripplanner.standalone.OTPMain --graphs otp/graphs/ --router 1 --server --analyst

To see a full list of options, add --help to the end of the command.

More detail instructions coming soon!

