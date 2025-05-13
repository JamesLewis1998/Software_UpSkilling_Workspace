# Module 8 - Pricing and Support

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
