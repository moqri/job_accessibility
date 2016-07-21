The backend directory contains the graph generating codes and data.
The data required to generate the graph should be stored under otp/graphs/. Two main pice of data are OpenStreetMap data and GTFS data.
If you have only one GTFS agency, you can put the GTFS data under otp/graphs/1.
All the codes to create the graph is packaged inside the otp-0.19.0-shaded.jar by Open Trip Planner.
The code is written in Jython (Python for Java framework). Therefore you need to use Jython IDE which is included in jython-standalone-2.7.0.jar.

When you use a command like java -Xmx2G -jar otp-0.19.0-shaded.jar --build otp --inMemory, you run the whole OTP Jar package.
When you use a command like java -cp otp-0.19.0-shaded.jar org.opentripplanner.standalone.OTPMain --graphs otp/graphs/ --router 1 --server --analyst, you run a specific class (here org.opentripplanner.standalone.OTPMain) from the Jar package which makes it faster.

