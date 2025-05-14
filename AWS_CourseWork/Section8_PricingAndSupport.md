# Module 8 - Pricing and Support

# Module 8 - Pricing and Support

Introduction: 

- Pricing and Support Models
- AWS Free Tier
- Benefits of Consolidated Billing
- Benefits of Cost Explorer
- Benefits of pricing calculator
- distinguish between support plans
- Benefits of AWS Market Place

## AWS Free Tier

AWS Free tier enables you to begin using certain services without having to worry about incurring costs for a specified period

Three Types:
1. Always Free -> Eg AWS Lamdba allows limited free requests
2. 12 months Free -> These offers are free for 12 months following your initial sign-up date to AWS
3. Trials -> Short-term free trial offers start from the date you activate a particular service

For 12 months after you first sign up for an AWS account, you can take advantage of offers in the 12 Months Free category.

Some other services that qualify under the free tier: 

- Sage Maker 
- Comprehend Medical
- Dynamo DB
- SNS 
- Cognito

Comprehend Medical: Amazon Comprehend Medical is a HIPAA-eligible natural language processing (NLP) service that uses machine learning that has been pre-trained to understand and extract health data from medical text, such as prescriptions, procedures, or diagnoses.

## AWS Pricing Concepts 

AWS offers a range of cloud computing services with pay-as-you-go pricing.

1. Pay for what you use
- For each service pay for the amount of resource you actually use
2. Pay less when you reserve
- some services offer reservation options that provide significant discounts compared to on-demand instance pricing
3. Pay with less Volume - volume based discounts when you reserve
- some services provide tiered pricing so the per unit cost is lower with increased usage

### AWS Pricing Calculator

Explore AWS Services and create an estimate for the cost of your UCs on AWS

 In the AWS Pricing Calculator, you can enter details, such as
 
 - the kind of operating system you need
 - memory requirements
 - input/output (I/O) requirements. 
 
 By using the AWS Pricing Calculator, you can review an estimated comparison of different EC2 instance types across AWS Regions.

### AWS Pricing Examples 

#### AWS Lambda
AWS Lambda charges you based on the number of requests for your functions and the time it takes for them to run 

Allows: 
- 1 million free requests 
- 3.2 million seconds of compute time per month

Can save on AWS Lamdba costs by signing up for a Compute Savings Plan

Savings Plan offers lower compute costs in exchange for committing to a consistent amount of usage over a 1 yr or 3 yr term [ Example of Paying less when you reserve]

Example of Pricing Under One Region below Payment Thresholds:

![AWS Pricing Example](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1747213200/1Ltag26Y2ZAD33ahESXuCg/tincan/fe470bc5add63f94f005d3da17a6db8131e78b9e/assets/CPE%20Digital%20-%20Module%208%20-%20AWS%20Lambda%20pricing%20example.png)

#### Amazon EC2

EC2 -> pay for compute time you use whilst instances are running

For some workloads you can reduce EC2 costs by using Spot Instances: only works if your business case can withstand interuptions whilst running the instances

Pricing Example where EBS and ELB are below cost limits:

![ELB and EBS Prices Below Threshold](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1747213200/1Ltag26Y2ZAD33ahESXuCg/tincan/fe470bc5add63f94f005d3da17a6db8131e78b9e/assets/CPE%20Digital%20-%20Module%208%20-%20Amazon%20EC2%20pricing%20example.png)

#### Amazon S3

S3 Pricing Consider the following: 

1. Storage - pay for only the storage you use
2. Requests and Data Retrievals - Pay for requests made to Amazon S3 objects and buckets
3. Data Transfer - No data transfer costs betwen S3 and other services within the same AWS Region
4. Management and Replication -> Pay for storage management features you've enabled on your accounts S3 buckets
    - These features include Amazon S3 inventory, analytics, and object tagging

## Billing Dashboard

Billing and Cost management dashboard allows you to pay your AWS bill, monitor your usage and analyse and control your costs

- Compare your current month to date balance with the previous month
- view month to date spending by service
- view free tier usage by service 
- access cost explorer and create budgets
- purchase and manage savings plans
- publish cost and usage reports 

## Consolidated Billing

- AWS Organisations contains consolidated billing 
- roll the bills up into one bill sent to the owner of the organisation
- easier for company to manage
- you can still view bill in itemised fashion but all goes into one central location for ease of viewing 
- AWS Offers bulk pricing where each individual account is only given small usage
- savings plan or reserved instances for ec2 can be shared across accounts in orgnaisation

Pricing Consolidation Example:

![Consolidated Billing - Pricing](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1747144800/qRJJ8nUs-r7lqLOaD3ZlIQ/tincan/fe470bc5add63f94f005d3da17a6db8131e78b9e/assets/Consolidated%20billing%202.png)

TB Consolidation Example:

![TB Example](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1747144800/qRJJ8nUs-r7lqLOaD3ZlIQ/tincan/fe470bc5add63f94f005d3da17a6db8131e78b9e/assets/Consolidated%20billing%204.png)

## Budgeting 

Track costs and keep within your limits 

- Custom Budgets for costs and usage 
- recieve alerts when you're forcasted to over use your budeget/ exceed it
- say if you want to be notified when you exceed 80% of your capacity

Types: 

1. Cost 
2. Usage
3. Savings Plans 
4. Reservation

Amount against each field and then configure alerts plus alters thresholds and add email address to recieve

Confirm and create budget -

You can also review comparisons of your current vs. budgeted usage, and forecasted vs. budgeted usage

## AWS Cost Explorer

AWS varaible cost model - only pay for what you use

Cost model allows you to drill down into your bill to explore how you spend money through AWS Cost Explore 

- 12 months of historical data
- bumps in spending over 12 month period easily analysed 
- can group the data based on services, region or tag

Tags are user defined key value pairs so you can define an EC2 instances with a specific project name 

then go into aws explorer and search through tags for projects to understand how much a project might be costing you

reports can be saved and come back to as and when needed

_Cost optimisation is a priority you should be paying close attention to_

Example of Monthly Costs for EC2 Instances Over 6 mo period: 

![EC2 Instance Cost](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1747144800/qRJJ8nUs-r7lqLOaD3ZlIQ/tincan/fe470bc5add63f94f005d3da17a6db8131e78b9e/assets/CPE%20Digital%20-%20AWS%20Cost%20Explorer.png)

By analyzing your AWS costs over time, you can make informed decisions about future costs and how to plan your budgets. 

## AWS Support Plans

From small start ups to large entirpises in both public and private sector, support is avaialble

- support forums 
- aws personal health dashboard
- etc 

Higher levels of support available:

- response time of less than 12 hours for urgent issue 
- direct phone access to support team  - 4 hour support time if production system is impaired

Extra fee can also:

- prepare for new launches 

AWS Enteripise Support on ramp:

- Basic, developer and business support
- Access to TAMs 
- 30 min response time

You can choose from the following Support plans to meet your company’s needs: 

1. Basic
    - Limited Selection of Trusted Advisor checks 
    - Onw Personal Health Dashboard
    - Documentation and support communities
2. Developer
    - Best practice guidance
    - Client-side diagnostic tools
    - Building-block architecture support -> including guidance on how to use features and services with one another
3. Business
    - Use Case Guidance and what features/ services support your UC best
    - All AWS Trusted Advisor checks
    - Limited support for third-party software, such as common operating systems and application stack components
4. Enterprise On-Ramp
   - A pool of Technical Account Managers to provide proactive guidance and coordinate access to programs and AWS experts
   - A Cost Optimization workshop (one per year)
   - A Concierge support team for billing and account assistance
   - Tools to monitor costs and performance through Trusted Advisor and Health API/Dashboard
5. Enterprise
    - A designated Technical Account Manager to provide proactive guidance and coordinate access to programs and AWS experts
    - A Concierge support team for billing and account assistance
    - Operations Reviews and tools to monitor health
    - Training and Game Days to drive innovation
    - Tools to monitor costs and performance through Trusted Advisor and Health API/Dashboard
    -
    -
### TAMS

- Provide infrastrcutre event management 
- architecture reviews

Six Pillars that are followed in architecture reviews

- Operation Excellence 
- Security 
- Reliability
- Performance Efficiency 
- Cost Optimisation
- Sustainability

TAMs look at customers holistically and question, how can we make them successful?

## AWS Market Place 

Curated digital catalogue
Allows acceleration of inovaton 
reduce cost of ownership

helps to improve speed and agility with aws
aws market place allows you to access options like one click deployment 

some third party vendors have annual contracts for third party services

alomost all will allow them to use licenses you already own and credit them for aws deployment

many vendors offer trials or quick start plans to allow customers to experiment with their offerings to see if its for them 

market place offers
- custom terms and pricing 
 - private market place 
 - integration into your procurement systems 

AWS Marketplace(opens in a new tab) is a digital catalog that includes thousands of software listings from independent software vendors. You can use AWS Marketplace to find, test, and buy software that runs on AWS. 

AWS Market Place Categories:

![Market Place Categories](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1747152000/49fHHUYsEzg3SsazR3qadQ/tincan/fe470bc5add63f94f005d3da17a6db8131e78b9e/assets/CPE%20Digital%20-%20Module%208%20-%20AWS%20Marketplace.png)

## Module 8 Summary

In Module 8, you learned about the following concepts:

1. Three types of offers included in the AWS Free Tier: 12 months free, Always free, and Trials
2. Benefits of consolidated billing in AWS Organizations
3. Tools for planning, estimating, and reviewing AWS costs
4. Differences between the five AWS Support plans: Basic, Developer Business, Enterprise On-Ramp, and Enterprise
5. How to discover software in AWS Marketplace
