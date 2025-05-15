# AWS Module Nine: Migration and Innovation

## Course Introduction

Learning Objectives: 

1. Understand migration and innovation in the AWS Cloud.
2. Summarize the AWS Cloud Adoption Framework (AWS CAF). 
3. Summarize the six key factors of a cloud migration strategy.
4. Describe the benefits of AWS data migration solutions, such as AWS Snowcone, AWS Snowball, and AWS Snowmobile.
5. Summarize the broad scope of innovative solutions that AWS offers.

## AWS Cloud Adoption Framework

- Cloud migration is a process
- takes effort to get apps migrated to aws 
- Need perspectives from various experts for AWS migration
- aws professional services -> Created CAF allowing you to manage this framework through this to enable quick migration 

Six Different Areas:

1. Business - Business Perspective
    - Ensures that IT aigns with business needs and that the investments into IT links into the key business results
    - Includes Business Managers, Finance Managers, Budget Owners and strategy stakeholders
2. People - Business Perspective
    - Evaluates organisations structures and roles, new skills and process requirements and identifies potential gaps to be addressed
    - Includes HR, staffing and mid level management
3. Governance - Business Perspective
    - Focuses on skills/ prcoesses to aign IT strategy with business strategy
    - Manage and measre cloud investments to evaluate business outcomes
    - Common roles include CIO (Cheif Information Officer), Program Managers, Enterprise Architects, Business Analysts and Portfolio Managers
4. Platform - Technical Perspective 
    - Includes principles and patterns for implementing new solutions in the cloud and migrate on premise workloads to the cloud
    - Uses variety of architectural models to understand and communicate the strcuture of IT systems and their relationships.
    - CTOS, IT Managers and Solution Architects
5. Sercurity - Technical Perspective  
    - Security Perspective ensures organisation meets security objectives for visibility, auditability, control and agility
    - AWS CAF used to strcuture the selection and implementaton of security controls that meet the organisatons needs
6. Operations - Technical Perspective
    - enables you to run use operate and recover IT worksloads to hte level agreed upon with oyur business stakeholders
    - Common with IT Operations Managers and IT Support Managers

HR would fall under the people perspective 
Cloud architect would fall under the platform perspective
Business or Finance Analyst would fall under business perspective

AWS CAF Action Plan: Helps guide your organisation for cloud migration

## Migration Strategies

Once you've gone through the discovery phase based on what you have in your existing environment you decide which option within the Six R's is the best fit

### Six Strategies for Migration

1. Rehosting
    - aka lift and shift
    - no changes made, pick up apps and move them onto aws
    - You can save up to 30% of your total costs just by rehosting
    - Also easier to optiomise applications later once they already live in the cloud
2. Replatforming
    - lift, tinker and shift
    - a few cloud optimisations made
    - but not touchin sny core code in the process, no new dev efforts involved
    - eg take existing mySQL DB and replatform it onto RDS mySQL without any code changes at all
3. Refactoring/ re-architecting
    - strong business need to add features or improved performance 
    - highest initial cost re planning and human effort
    - new code involved
    -  reimagining how an application is architected and developed by using cloud-native features
4. Repurchasing
    - common for companies looking to abandon legacy sw vendors and get a fresh start as part of migration
    - For example moving from an out of date database vendor to cloud native databse options 
    - note some new sw packages are easy to implement whereas others can take time
5. Retaining
    - about to be deprecated but not just yet 
    - they're left to run for another 3-8 months
    - apps could be migrated to aws but why?
    - over time these apps can be deprecated where they live and utlimately retired
6. Retiring
    - some parts of your enterpirse IT portfolio are just no longer needed
    - 10-20% of companies apps you'll find are longer in use
    - sometimes you "just have to turn off the lights"

### AWS Snow Family

Note, a dedicated network with 1 Gb per second moves 1 PB of data in about 100 days and in the real world, likely longer with a higher cost

AWS Snow Family is a collection of physical devices that help to physically trasnport up to exabytes of data into and out of AWS

AWS Snow Family is Composed of AWS Snowcone, AWS Snowball and AWS Snowmobile. These three devices offer different capacity points with most including built in computing capabilities

AWS owns and manages the devices, plus integrates them with AWS Security, monitoring, storage management and computing capabilities 

![AWS Snow Family](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1747332000/_EtHZB05wimF2RkvXDUD-A/tincan/fe470bc5add63f94f005d3da17a6db8131e78b9e/assets/snow%20family.jpg)

DEFINITIONS: 

**AWS Snowcone**: AWS Snowcone is a small, rugged, and secure edge computing and data transfer device. 

**AWS Snowball**: Two types of devices

Snowball Edge Storage Optimized is a device that enables you to transfer large amounts of data into and out of AWS. It provides 80 TB of usable HDD storage.

- Snow Edge Storage Optimised: suited for large scale data migrations and recurring transfer workflows
    - Storage: 80TB of HDD capacity and 1TB of SATA SSD block volumes 
    - Compute: 40 vCPUs and 80 GiB of Memory to support EC2 instances (equiv to C5)

- Snowball Edge Compute Optimised: pwoerful computing resources  for use cases such as ML, full motion video analysis, analytics and local computing stacks
    - Storage: 80 TB usable HDD capacity for S3 compatible object storage or EVS copatible block volumes and 28 TB of usable SSD capacity
    - Compute: 104 vCPUs, 416GiB of memory and optional NVIDIA tELSA v100 gpu

**AWS Snowmobile**:
AWS Snowmobile is an exabyte-scale data transfer service used to move large amounts of data to AWS.

## Innovation with AWS

### Innovate with AWS Services

You are properly equipped to drive innovation in the cloud if you can clearly articulate the following conditions: 

- The current state
- The desired state
- The problems you are trying to solve

### Serverless Applications

Applications that don't require you to provision, maintain or adminsiter services -> AWS handles capabilities such as fault tolerance or availabliltiy 

AWS Lambda is an example of a Service you can run serverless applications  with -> designing your architecture to trigger lambda functions to run yout code and ,mitigate the need to manage a fleet of servers

### AI 

Examples include:
1. Convert speech to text with Amazon Transcribe.
2. Discover patterns in text with Amazon Comprehend.
3. Identify potentially fraudulent online activities with Amazon Fraud Detector.
4. Build voice and text chatbots with Amazon Lex.

### ML 

SageMaker to remove difficult work from the process of using ML and empower you to build, train and deploy ML models quickly to analyse data, solve complex provlems and predict outcomes before they happen

### Amazon Q Developer

AI powered code generator for IDEs and code editors includong
1. AI Coding Companion 
2. AI Security Scanner

Amazon Q developer learns from open source projects 

Note:

- Amazon Textract is a machine learning service that automatically extracts text and data from scanned documents
- Amazon Lex is a service that enables you to build conversational interfaces using voice and text.
- AWS DeepRacer is an autonomous 1/18 scale race car that you can use to test reinforcement learning models

## Module Nine Summary

a. The AWS Cloud Adoption Framework
    - BP Business
    - BP Ppl 
    - BP Governance
    - TP Platform
    - TP Operations
    - TP Security
b. The six strategies for migration
    - Rehost
    - Replaform 
    - Repurchase
    - Refactor 
    - Retire
    - Retain
c. The AWS Snow Family
    - AWS Snowball
    - AWS Snowmobile
d. Innovation with AWS services
    - Serverless Applications
    - ML and AI