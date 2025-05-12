# Linked In AWS AI Practitioner Lecture Notes

## AWS Discount for Foundational Certs

- AWS Certified Cloud Practitioner
- AI Certified Practitioner

Discount of 50 quid if you sign up for exam prior to the 21st:

https://pages.awscloud.com/GLOBAL-other-GC-Traincert-Foundational-and-Associate-Certification-Challenge-2025-reg.html?trk=75b0ff50-fc8b-4a2a-b232-9f674aa43adb&sc_channel=el

Exam Guide:

https://skillbuilder.aws/exam-prep/ai-practitioner?trk=75b0ff50-fc8b-4a2a-b232-9f674aa43adb&sc_channel=el


## Exam Preparation 

Use the Udemy learning platform to learn about how to prepare for the AWS exam

- Includes resources on Amazon Service Prep 
- Plus reviewing and practicing for the exam

Always be concious of weeding out the incorrect answers in multiple choice to narrow choices down

1. get to know the exam
2. focus on the areas with additonal resource provided 
3. review and practice for your exam - including gamified learning 
4. test skills and takeinitia pretest
5. get exam SCHEDULED

https://skillbuilder.aws/exam-prep/ai-practitioner?trk=75b0ff50-fc8b-4a2a-b232-9f674aa43adb&sc_channel=el


## Which cert to begin with

Consider commencing with the Practitioner One then moving onto the AI Practitioner Path -> the video does provide an overview of learning path for the associated certs

## Exam Content

- multiple choice
- multiple response
- ordering 
- matching
- case study 

### Content Outline

1. Domain 1 - Fundamentals of AI and ML 
2. Domain 2 - Fundamentals of Generative AI
3. Domain 3 - Applications of Foundation Models
4. Domain 4 -

## Domain One

**What is AI?**

Machine Learning is a subset of AI and relies on patterns/ inference rather than specific instructions

Deep Learning is more complex subset of Machine Learning

Inference uses model to make predictions and outputs based previously unkown data

Inferencing - batch 

analyses it all at once
better for accuracy rather than speed

Inferencing - realtime

processes data as it comes in
better for real time processing and output 

## Supervisored vs Unsupervised learning 

## reinforcement learning 

the computer is reiforced for correct outcomes/ getting the correct answer 

## Applications of AI and ML

- AUTOMATE PROCESSES
- PROVIDE SCALABLE SOLUTIONS 

Important to Consider the cost benefit analysis of AI and ML implications

## Domain Two - Fundamentals og Generative AI

Ability to explain the basic concept of GenAI 

Tokens - think of these as your input output 

Understand the advs and disadvs of GenAI and the costs associated with it for the business

Describe AWS infrastrcuture for technologies and creating foundations 

GenAI takes what it knows/ has learnt and creates new content/ ideas from this 

It can also generate images and solve problems for your businesses in different ways also 

GenAI => 

### Courses included in AWS

1. Intro to GenAI
2. GenAI for Executives 
3. GenAI for businesses 

## Domain Three (biggest section) - Applications of Foundation Models

 - generate content based on topics or even doing chat interfaces to get customer responses quicker 
 - larger the model the larger the queue the higher the inference and the more expensive the models are
 - tokens == string of characters that make up a sentnece

 RAG - retrieval augmented generation

 ### AWS Amazon Bedrock 

 Place in AWS where you can interact with generative AI 

 Playground included where you can test out different models 

 Nova Pro - one of amazons first party models 

 Once pulled up the model there's a chat inereface to conduct prompt model AI 

 Plus a selection against Randomness and Diversity 

- Temperature means the more creative the model can get for prompts (especially if you're writing production code)
- Top P also changes the output and has a scale to set against

System Prompt - is a good place to put instrcutions to append or keep in consideration to whatever the user is prompting in the field

    - For example you can put into system prompts, always put answers at a fifth grade level

System prompt can be overridden by user prompt if for example the system prompt says to answer like a 5 year old but the user prompt asks to answer like a 25 year old expert 

### Other Useful Prompt Strategies 

- Provide the comments with either negative positive or neutral 

### Fine Tuning Nova Pro 

Concept of taking a large language model and training it/ tuning it to a particular task you're looking to touch upon

Pre-training is the backbone of how the foundation model comes about 

You can connect the generation to a dataset you own to augment the output and give a more authentic response if for example you want to connect specific company answers to your company data

## Domain 4 - Repsonsbile AI  l

## Gaurd rail also to be considered - part of bedrock

A way to make sure datasets are limited based on requirements. for example if you own a software company in fifnance - you want to keep the chat bot questions limited to finance and not allow ppl to ask it what the weather is like outside

## Domain 5 - Security, Complaince and Governance for AI solutions

All crucial for privacy by design, ensuring trust and making sure users data is protected 

think about amazons shared responsbility model studied in the aws cloud practitioner prep 

Amazon sage maker model cards

threat detection. application surcity and threat edetection

Remember -> AWS is responsbile for secruity of the cloud while customers are repsonsbile for secuirty in the cloud
