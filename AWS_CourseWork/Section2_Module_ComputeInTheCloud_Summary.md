# AWS Computing in the Cloud Module Two #

## Module Two Summary:

Cloud Computing: the on-demand delivery of IT resources over the internet with pay as you go pricing.

- Make requests for IT Resources
    - Compute
    - Storage 
    - Analytics
- No upfront cost you just provision and pay @ end of the month 

EC2: Dynamically spin up and spin down virtual servers known as instances --> instance family == HW instance runs on

- Instances broken down into the following:
    - General purpose
    - compute optimised
    - memory optimised 
    - Accelerate Computing
    - Storage Optimised

Note:

1. vertical scaling is resizing of instances 
2. horizontal scaling is adding or subtracting instances

EC2 Scaling: ELB (Elastic Load Balancing) is distributing the incoming traffic across the instances 

Amazon EC2 Billing Options:

a. On-Demand -> most flexible and has no contract 
b. Spot-pricing -> utilise unused capacity @ a discounted rate
c. Reserved instances -> contract with aws in which you commit to certain level of usage
d. Saving Plans -> AWS Lambda, AWS Fargate

Microservice Development

- SQS: simple queue service
- sns: simple notification service

Types of Compute Service beyond EC2:

- Amazon Elastic Container Services (ECS)
- Amazon Kubernetes Servicees (EKS)

(both of which are container orchestration tools)

Both ECS and EKS can be used with EC2 instances BUT, if you don't want to manage this you don't need to -> use AWS Fargate where in which you can run containers on top of a serverless platform 

OR -> use AWS Lambda where you can upload code and configur to run on triggers (only get charged when code is actually running)

Compute optimised instances are ideal or computer bound application that benefit from high performnace processes

Kubernetes == open service SW that enables you to deploy and manage containersied applciations @ scale (where as AWS Lambda lets you run code without provisioning or manning servers)