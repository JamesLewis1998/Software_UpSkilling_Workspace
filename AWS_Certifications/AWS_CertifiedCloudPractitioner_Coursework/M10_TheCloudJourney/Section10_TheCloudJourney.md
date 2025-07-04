# Module 10: The Cloud Journey

## Section Objectives

1. Summarize the six pillars of the Well-Architected Framework.  

2. Explain the six benefits of cloud computing.

## Six Pillars of a Well Architected Framework

1. Operational Excellence
    - Operational excellence is the ability to run and monitor systems to deliver business value and to continually improve supporting processes and procedures
    - Key principles include operations as code, annotating documentation, anticipating failure, and frequently making small, reversible changes
2. Security
    - This pillar captures the ability to protect information, systems, and assets while delivering business value through risk assessments and mitigation strategies
    - Automate Security Best Practices where possible
    - Apply Security at all Layers
    - Protect data in transit and at rest
3. Reliability
    - This is the ability for a system to do the following
        - Recover from infrastrcuture or service disruptions
        - Dynamically aquire computing resources to meet demand 
        - Mitigate disruptions such as misconfigurations or transient NW issues
    - It includes:
        - includes testing recovery procedures
        - scaling horizontally to increase aggregate system availability
        - automatically recovering from failure
4. Performance Efficiency
    - Performance efficiency is the ability to use computing resources efficiently to meet system requirements and to maintain that efficiency as demand changes and technologies evolve
    - Ways to test this include: 
        - experimenting more often
        - using serverless architectures
        - designing systems to be able to go global in minutes
5. Cost Optimisation
    - Cost optimization is the ability to run systems to deliver business value at the lowest price point
    - Optimisations include: 
        - adopting a consumption model
        - analyzing and attributing expenditure
        - using managed services to reduce the cost of ownership
6. Sustainability
    - Ability to continually improve sustainability impacts by reducing energy consumption and increasing efficiency across all components of a workload by maximizing the benefits from the provisioned resources and minimizing the total resources required
    - To facilitate good design consider the following:
        - Understand your impact
        - Establish sustainability goals
        - Maximize utilization 
        - Anticipate and adopt new, more efficient hardware and software offerings
        - Use managed services
        - Reduce the downstream impact of your cloud workloads

The framework provides a way to consistently measure your architecture against best practices and design principles and identify areas for improvement

## Benefits of the AWS Cloud

Six Advantages of the AWS Cloud: 

1. Trade upfront expense for variable expense.
    - Upfront expenses include data centers, physical servers, and other resources that you would need to invest in before using computing resources
    - you can pay only when you consume computing resources
2. Benefit from massive economies of scale.
    - By using cloud computing, you can achieve a lower variable cost than you can get on your own
    - Usage from hundreds of thousands of customers aggregates in the cloud, providers such as AWS can achieve higher economies of scale. Economies of scale translate into lower pay-as-you-go prices
3. Stop guessing capacity.
    - With cloud computing, you don’t have to predict how much infrastructure capacity you will need before deploying an application
    - Can launch Amazon EC2 instances when needed and pay only for the compute time you use. Instead of paying for resources that are unused or dealing with limited capacity, you can access only the capacity that you need, and scale in or out in response to demand
4. Increase speed and agility.
    - flexibility of cloud computing makes it easier for you to develop and deploy applications
    - also provides your development teams with more time to experiment and innovate
5. Stop spending money running and maintaining data centers.
    - Cloud computing in data centers often requires you to spend more money and time managing infrastructure and servers
    - ability to focus less on these tasks and more on your applications and customers
6. Go global in minutes.
    - enables you to quickly deploy applications to customers around the world, while providing them with low latency

## Module 10 Summary

The six pillars of the AWS Well-Architected Framework:
   - Operational excellence
   - Security
   - Reliability
   - Performance efficiency
   - Cost optimization
   - Sustainability

Six advantages of cloud computing:
   - Trade upfront expense for variable expense.
   - Benefit from massive economies of scale.
   - Stop guessing capacity.
   - Increase speed and agility.
   - Stop spending money running and maintaining data centers.
   - Go global in minutes.