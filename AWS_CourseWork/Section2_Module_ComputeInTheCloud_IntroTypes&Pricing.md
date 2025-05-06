# AWS Computing in the Cloud Module Two #

**EC2**: Elastic Compute Cloud is:
1. Highly Flexible
2. Cost Effective 
3. Quick

## Hardware vs AWS 

_HARDWARE_
> Hardware for server set up: Costs Money and is time consuming to set up -> need servers to host your applications and provide the required compute capacity + a lot of time and effort to set up

_AWS_
> AWS has already built the data centres andcsecured the data centres in conjunction with already provisioning and installing the servers 

## Multi-Tenancy and Hypervisor 

_Multi-tenancy_ is shared underlying HW between virtual modules 

- Hypervisor is responsble for coordinating this multitenancy and is solely managed by AWS 
- Isolating VMs from each other is done as they share resources from the host meaning EC2 instances are secure 

## EC2 Instances 

- EC2 instances can be requested to be launched within minutes and Amazon only charges you for running instances, not stopped or terminated ones
- EC2 instances are resizable -> this means vertically scaling on instances (and whether they are publically or pirvately accessible)
- EC2 provides secure resizable compute capacity in the cloud as amazon ec2 instances 

### On-Premise vs EC2 

| On-Premise | EC2 |
|------------|-----|
|1. HW Purchase | 1. Povision and launch instances in numbers|
|2. Server Delivery | 2. Stop once finished running work load|
| 3. Server Information | 3. Pay only for runtime |
| 4. Config set up | 4. Scalable server capacity vs cost |

_Favourable Solution is the EC2 instances_

## EC2 Three Step Approach 

**Step One**

Launch an instance -> select template of basic configs 

1. _Launch_: Security settings -> control traffic flowing in and out of your instances 
2. _Instance_: Instance type -> specific HW config of your instance 
3. _Config_: OS, App Server and Applications

**Step Two**

Connect -> programmes and applications have different ways to connect directly to instances and exchange data 

- Note for users this could be logging into a computer desktop

**Step Three**

Use -> after connecting your instance you can begin using it

- Including running commands to install SW, add storage, copy and organise files and much more

## Amazon EC2 Instance Types 

Instances families can be optimised for certain types of tasks and are broken down into the following: 

- General Purpose: balance of compute memory and new resources 
- Compute Optimised: Gaming Servers high performance computing
- Memory Optimised
- Accelerate Comptuing: graphics processing
- Storage Optimised: workloads requiring high performance on locally stored data 

Here we need to assess clients specific needs of:

1. Compute 
2. Memory
3. Storage Capabilities

### General Instances 

Useful for application servers, gaming servers and small/ medium databases (DBs) 

### Compute Optimised Instances 

Ideal for compute bound applications benefitting from high-perofrmance processes:

- High performance web servers 
- compute intensive application server
- dedidcated gaming servers 

### Memory Optimised Instances 

1. Fast performance for workloads that process large datasets in memory 
2. In computing memory -> temporary storage area 
    - Holds all the data and instrcutiuons that a CPU needs to be able to compute actions
    - ie before a computer program or application is able to run it is loaded from storage into memory
    -(Preloading process gives the CPU driver access to the computer programme)

### Accelerated Computing Instances 

Uses HW accelrators or co-processors to perform the same function more efficiently than is possible in SW running on CPUs

Used for floating point number calculations n, graphics processing and big data analytics

Note a HW accelerator is a component that can expedite data processing

### Storage Optimised Instances 

- Workloads that require high sequential capabilities/ write access to large datasets on local storage
- distirbuted file systems, data warehousing applications and OLTP (online transaction processing systems)
- IOPS = input/ output operations per second
    - metric to measure performance of storage device

A storage optimised instance is designed to deliver 10,000s of low latency, random IOPS to Applications

## EC2 Billing Options  

1. On Demand
2. Savings Plan
3. Reserved Instances
    - Standard
    - Convertible
4. Spot Instances 
5. Dedicated Hosts

### On Demand Instances 
- Ideal for short term irregular workloads that cannot be interupted
- instance can run continuously until we stop them and only pay for the compute time you use

### Reserved Instances (Standard) 

- 1 or 3 year purchase option 
- when you know your EC2 instance type, size you need and which AWS region you plan to run in 
- Considerations
    - Instance Type and Sie 
    - Platform Description (OS)
    - Tenancy -> model for how EC2 instances are occupied and the HW they run on

### Reserved Instances (Convertible) 

- Designed for 1 or 3 year contracts 
- If you need to run instances in different availability zones or different instance types

### EC2 Instance Saving Plans 

- Hourly spend commitment on a 1 to 3 year contract
- Good if you need flexibility in your usage over the duration of the committed term 
- Unlike reserved instances you do not need to specify up front what EC2 instance type you need, or the OS to run it on and the size or latency requirements with it

### Spot Instances  

- Unused EC2 instance capacity and offer up to 90% for on demand prices 
- HOWEVER
    - you might need to wait until a spot opens up 
    - you wil lose your spot if there's higher demand from else where 

### Dedicated Hosts 

- Physical servers with EC2 instance capacity that is fully dedicated to your use
- Most expensive out of all of the options for EC2 instances 