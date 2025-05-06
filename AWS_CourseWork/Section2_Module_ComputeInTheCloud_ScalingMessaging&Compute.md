# AWS Computing in the Cloud Module Two #

## Module Two Scaling EC2 Instances  

Scaling and Elasticity are key components to the benefits of EC2

**Key Question**: _What is the right amount of HW to provide?_

Similar to that of load levelling from the grid, if you buy the max you'll have happy customers but ver low data utilisation

AWS can however scale based on fluctuations in demand 

>"Everything fails all the time so plan for failure and nothing fails" 

Ie the quote refers to building in redundancy -> high operating system with no single point of failure

- Scaling involves beginning with only the resources you need and designing the architecture to automatically respond to changing demand by scaling in and out
    - As a result you only pay for the instances you use
    - -> Don't need to worry about the lack of computing capacity to meet your customers needs 

_AWS Provides AWS Auto-Scaling to enable this to be done automtically 

### AWS Auto Scaling 

1. Dynamic Scaling -> responds to change
2. Predictive Scaling -> predicts change to respond to and does this according
    - Scheduling based on demand

Enabling Decoupling of the System via: 

- Scaling up == More power to existing instances 
- Scaling out == adding more instances 

Autoscaling adds instances on demand and decomissions instances when no longer needed

In cloud computing, power is a programmatic resource

When setting an auto scaling group you can set the minimum number of EC2 instances 
    - Minimum capacity == no. of Amazon EC2 instances that launch after creating the auto scaling group 

All of this enables -> Pay only for the instances you use when you use them [ KEY PRINCIPLE OF EC2 and AWS] -> All promoting a Cost Effective Architecture 

## Module Two Direct Traffic with Elastic Load Balancing (ELB)

_For AWS environment, if you have multiple EC2 instances (all of which are running the same programme), how does that request know which EC2 instances to go to?_

Answer: Load balancing, this is used to route requests to instances 

- ELB is a high performing, cost efficient mechanism engineered to manage load balancing and is automatically scalable
- Note: ELB is NOT used for external traffic
- ELB is regional, single URL each front instance uses and it creates a true decoupled architecture 

![Alt text](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1744902000/wQAkh04MjL-dzNf6ttJZ6A/tincan/fe470bc5add63f94f005d3da17a6db8131e78b9e/assets/CPE%20Digital%20-%20Low%20demand.png "Elastic Load Balancing and Auto Scaling AWS")

ELB is the AWS Service that automatically distributes incoming application traffic across multiple resources

The Load Balancer acts as a single point of contact for all incoming web traffic to your auto scaling group -> therefore as you add or remove EC2 instances in response to incoming traffic, these requests route through thr load balancer first 
    - EC2 ensures even distribution actoss instances to avoid one instance doing the bulk of the work

> Note, ELB and EC2 Auto Scaling are separate servicers which work together tro ensure applications running in Amazon EC2 can provide high performance and scalability

## Module Two Messaging and Queuing 

Definitions: 
- Queing is defined as placing messaged into a buffer 
- Tightly coupled architecture: if a signle component fails or changes, this causes issues for other components in the whole system [See example below]

_Example_: If you have two applications (A and B), with A sending messages to B, if B fails, A will fail as well 

Alternative Approach: loosly coupling architecture where a single failure will not cause cascading failures 

![Alt text](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F44eb88f9-3d87-46ea-9f4a-1c778307bda8_1590x728.png)

If from the example above, Consumer One fails, Producer One  does not experience any disruption via the use of the MSG Q

_**A loosly coupled architecture is exactly what AWS tries to achieve**_

1. **SQS** -> Amazon Simple Queue Service
    - Allows you to send/ store or recieve messages between SWCs in AWS Architecture at any time without requiring other services to be available
2. **SNS** -> Amazon Simple Notification Service

**Note**: Data contained within a message == a payload and is packeted until delivery

**SQS** Queue == where messages are placed until they are processed 

- AWS managers underlying infrastrcuture for you to host these queues

Amazon **SNS** sends out messages to services but also sends out notification to end users (publish and subscribe model)

### Amazon SNS Topic 

- A channel for messages to be delivered
- Then you configure the subscribers to that topic and publishe messages for those subscribes 
    - therefore in practice can send one message to a topic which will then fan out to all the subscribers in a single go
        - these subscribers can also be end points such as SQS Queues, AWS Lambda Functions, HTTPS  or HTTP web blocks

_Plus SNS can be used to fan out notifications to end users (using mobile push, sms and email)_

### Monolithic Applications vs Microservices 

Made up of multiple components -> they communicate with each other to transmit data, fulfill request and keep an application running 

Components include: 
- Databases
- Servers
- User Interfaces 
- Business Login

#### Monolithic 

Monolithic Architecture: when all of these components above are tightly coupled

- In this instance if a single component fails, other components fails and the entire application may fail as a result

![Alt Text](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1745438400/u51dbVyPQVZ_KqeedhQRWw/tincan/fe470bc5add63f94f005d3da17a6db8131e78b9e/assets/CPE%20Digital%20-%20Monolithic%20application.png)

#### Microservices 

Therefore to help maintain application availability, when a single component fails, you can design your application through the use of micro services --> LOOSLY COUPLING APPLICATION COMPONENTS

Here -> if a single component fails, the other continue to work because they are communicating with each other 

Loose coupling prevents entire application from failing 

![Alt Text](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1745438400/u51dbVyPQVZ_KqeedhQRWw/tincan/fe470bc5add63f94f005d3da17a6db8131e78b9e/assets/CPE%20Digital%20-%20Microservices.png)

**IMPORTANT** : Two different services in AWS facilitate application integration

- Amazon SQS
- Amazon SNS

_**SNS** subscribers can be web servers, email addresses, AWS Lambda Functions and others_

_**SQS** sends store and recieve messages btwn SWCs without losing messages or requireing other servicers to be available_

#### Flow of Events 

App --> sends message into queue --> service or user retrieves message from queue --> processes it then deletes it from the queue

## Module Two Additional Compute Services

EC2 instances == virtual machines 

You can use these virtual machines on everything from Basic web servers to high performing compute clusters 

When setting up EC2 instances, you are responsible for:
- ensuring sw updates 
- Architecting solutions in a highly available manner
- Managing scaling of those instances

### Serverless Computing 

Serverless solutions means you cannot see or access the underlying infrastructure of your application -> all of this management is taken care for you 

_One option of serverless computing is AWS Lambda_

### AWS Lambda 

AWS Lambda is a servier that lets you run code without needing to provision or manage servers 

Upload your code into a Lamdba Function, configure a trigger and from there the service waits for this trigger to be met to action off of it

Offers the following:
1. Quick processing 
2. Web backend 
3. each invocation <15 mins for completion

**Example of Serverless Event-driven E-commerce microserices architecture:**
![Alt Text](https://miro.medium.com/v2/resize:fit:1100/format:webp/1*WK_-gPDoCp29u8_MfStF7g.png)

_however if you're still not ready for serverless and want control of the underlying environment, consider Amazon ECS and EKS, both of which are container application tools_

### Containers 

Containers provide you with a standard way to package your applications code and dependencies into a single object

Note these containers run on top of EC2 instances and run in isolation from each other similar to how virtual machines work

Both ECS and EKS can run on top of EC2 instances

**Example One: One Host and Multiple Containers**

![Alt Text](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1745492400/TOq2kE4-V8tghdWQq9FchA/tincan/fe470bc5add63f94f005d3da17a6db8131e78b9e/assets/CPE%20Digital%20-%20Containers%201.png)

**Example Two: Tens of hosts with hundreds of containers**
![Alt Text](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1745492400/TOq2kE4-V8tghdWQq9FchA/tincan/fe470bc5add63f94f005d3da17a6db8131e78b9e/assets/CPE%20Digital%20-%20Containers%202.png)

### Amazon Elastic Container Service

ECS is a highly scalable, high-performance container management system that enables you to run and scale containerized apps on AWS

Also supports **Docker** containers -> Docker is a sw platform that enables you to build test and deploy your apps quickly 

ECS allows you to use API calls to launch and stop Docker-enabled Apps

_Docker is a widely used platform that uses operating system level virtualization to deliver software in containers_

#### Container Orchestration 

When using docker containers on AWS, processes need to start, stop, restart and be monitored across all EC2 instances in the architecture 

Process of managing these tasks above == container orchestration.

ECS is designed to help you run your containerized applications at scale without the hassle of managing your own container orchestration software. 

_Note number of instances running together is called a cluster_

### Amazon Elastic Kubernetes Service

EKS is a fully managed service that you can use to run Kubernetes on AWS

Note: Kubernetes is an open-source container orchestration platform used to automate the deployment, scaling, and management of containerized applications

In essence, Kubernetes allows you to deploy and manage containerized applications at scale

**Example of Kubernetes Architecture**
![Alt Text](https://newrelic.com/sites/default/files/styles/1200w/public/2021-05/kubernetes_architecture-1024x649.webp?itok=224Yqhs6)

### AWS Fargate

AWS Fargate is a serverless compute platform for EC2 and ECS (Elastic Container Service)

- When using AWS Fargate, AWS manages your server infrastructure for you. 

## AWS Compute Services Comparison 

| EC2 | AWS Lamdba | ECS/ EKS |
|---|---|---|
|1. Host Traditional Applications  | 1. Host Short Running Functions | 1. Run Docker-container based workloads on AWS |
|2. Full Access to OS (Linux or Windows) | 2. Service Orientated Applications | 2. Choose your Orchestration Tool: ECS or EKS |
|3. - | 3. Event Driven Applications | 3. Then choose your Platform - either run your containers on EC2 Instances (You Manage) or Serverless (Fargate) that's managed for you |
|4. - | 4. No provisioning or managing servers | 4. - |

