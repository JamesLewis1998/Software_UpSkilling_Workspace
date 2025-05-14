# Module Three: Global Infrastrcuture and Reliability

Introduction: not a good idea to have one giant data centre. Instead AWS operates in all sorts of different areas around the world called REGIONS

## AWS Global Infrastructure

Historically companies would have to run their applications on their own data centres.

> Fundamental problems with data centres: events can happen that cause you to lose connection with this building

Options: 

a. Run a second data centre --> expensive 
b. Store backups --> most businesses store backups and hope the above day never happens 

ANSWER: AWS builds regions closest to wherever the business traffic demands are --> eahc region can be connected to another region through a high speed fibre NW (all of which is done by AWS)

Note: You can choose which region you want to run out of 

_Security Consideration: each region is isolated from each other region in the sense that no data will move in and out of that region without you explicitly granting access for that data to be moved._

- For Example: You might have government compliance recquirements where your information in Frankfurt cannot leave Germany (and same with other locations across the globe)
    - Only way to overcome this is if you with the right credentials and permissions request for the data export to happen

### Selecting a Region - Four Key Factors 

1. Compliance with data governance and legal requirements
    - Is the data region speicifc and cannot be exported from it
    - not all companies have 
2. Proximity
    - How close are you to your customer base 
    - latency -> time it takes for data to be sent or recieved 
3. Feature Avaialbility
    - sometimes the closest region may not have access to the correct AWS features you require
4. Pricing
    - Even if the HW itself is exactly the same, it can cost significantly more to run the same set of services on the same set of HW in different regions
    - SOA Paula can be 50% more expensive than running out of Oregan for example

_Selecting a Region for your services, data and applications must consider all of the above factors_

### Availability Zones 

Don't want to run an application in a single building -> regions are not one location, each region comprises of multiple data centres

Single or group of data centres == availability zone

- one or more discrete data centres with redundant power, NW'ing and connectivity 


