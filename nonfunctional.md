# Non-Functional Testing
---
This is the type of testing for which every organization has a separate team which is usually called a Non-Functional Test (NFT) team or Performance team.

Non-Functional Testing involves testing of non-functional requirements such as Load Testing, Stress Testing, Security, Volume, Recovery Testing, etc. The objective of NFT testing is to ensure whether the response time of software or application is quick enough as per the business requirement.

It should not take much time to load any page or system and should be sustained during peak load.

- Performance Testing
- Load Testing
- Stress Testing
- Volume Testing
- Security Testing
- Compatibility Testing
- Install / Uninstall Testing
- Recovery Testing
- Usability Testing
- Reliability Testing
- Compliance Testing / Conformance Testing
- Localization Testing

## Performance Testing
---
This term is often used interchangeably with `stress` and `load` testing.

Performance Testing is done to check whether the system meets the performance requirements. Different performance and load tools are used to do this testing.

## Load Testing
---
It is a type of Non-Functional Testing and the objective of Load Testing is to check how much load or maximum workload a system can handle without any performance degradation.

Load Testing helps to find the maximum capacity of the system under specific load and any issues that cause software performance degradation. Load testing is performed using tools like JMeter, LoadRunner, WebLoad, Silk performer, etc.

## Stress Testing
---
This testing is done when a system is stressed beyond its specifications in order to check how and when it fails.

This is performed under heavy load like putting large number beyond storage capacity, complex database queries, continuous input to the system or database load.

## Volume Testing
---
Volume Testing is a type of Non-Functional Testing performed by the Performance Testing team.

The software or application undergoes a huge amount of data and Volume Testing checks the system behavior and response time of the application when the system came across such a high volume of data.

This high volume of data may impact the system’s performance and speed of processing time.

## Security Testing
---
It is a type of testing performed by a special team of testers. A system can be penetrated by any hacking method.

Security Testing is done to check how the software, application or website is secure from internal and external threats. This testing includes how much software is secure from malicious programs, viruses and how secure & strong the authorization and authentication processes are.

It also checks how software behaves for any hackers attack & malicious programs and how software is maintained for data security after such a hacker attack.

## Browser Compatibility Testing
---
This is a sub-type of Compatibility Testing (which is explained below) and is performed by the testing team.

Browser Compatibility Testing is performed for web applications and ensures that the software can run with a combination of different browsers and operating systems. This type of testing also validates whether a web application runs on all versions of all browsers or not.

## Backward Compatibility Testing
---
It is a type of testing which validates whether the newly developed software or updated software works well with the older version of the environment or not.

Backward Compatibility Testing checks whether the new version of the software works properly with the file format created by an older version of the software; it also works well with data tables, data files, and data structure created by the older version of that software.

If any of the software is updated then it should work well on top of the previous version of that software.

## Compatibility Testing
---
This is a testing type in which it validates how software behaves and runs in a different environment, web servers, hardware, and network environment.

Compatibility testing ensures that software can run on a different configuration, different databases, different browsers, and their versions. Compatibility testing is performed by the testing team.

## Install / Uninstall Testing
---
Installation and Uninstallation Testing is done on full, partial, or upgraded install/uninstall processes on different operating systems under different hardware or software environments.

## Recovery Testing
---
It is a type of testing which validates how well the application or system recovers from crashes or disasters.

Recovery Testing determines if the system is able to continue its operation after a disaster. Assume that the application is receiving data through a network cable and suddenly that network cable has been unplugged.

Sometime later, plug in the network cable; then the system should start receiving data from where it lost the connection due to network cable being unplugged.

## Usability Testing
---
Under Usability Testing, the User-Friendliness Check is done.

The application flow is tested to see if a new user can understand the application easily or not. Proper help is documented if a user gets stuck at any point. Basically, system navigation is checked in this testing.

## Reliability Testing
---
[Resource](www.guru99.com)

Reliability Testing is a software testing process that checks whether the software can perform a failure-free operation for a specified time period in a particular environment. The purpose of Reliability testing is to assure that the software product is bug free and reliable enough for its expected purpose.

Reliability means “yielding the same,” in other terms, the word “reliable” means something is dependable and that it will give the same outcome every time. The same is true for Reliability testing.

#### Example
The probability that a PC in a store is up and running for eight hours without crashing is 99%; this is referred as reliability.
Reliability Testing can be categorized into three segments,
Modeling
Measurement
Improvement
The following formula is for calculating the probability of failure.
```
Probability = Number of failing cases/ Total number of cases under consideration
```

#### Factors Influencing Software Reliability
- The number of faults presents in the software
- The way users operate the system

- Reliability Testing is one of the key to better software quality. This testing helps discover many problems in the software design and functionality.
- The main purpose of reliability testing is to check whether the software meets the requirement of customer’s reliability.
- Reliability testing will be performed at several levels. Complex systems will be tested at unit,assembly,subsystem and system levels.

#### Why to do Reliability Testing
Reliability testing is done to test the software performance under the given conditions.

The objective behind performing reliability testing are,

- To find the structure of repeating failures.
- To find the number of failures occurring is the specified amount of time.
- To discover the main cause of failure
- To conduct Performance Testing of various modules of software application after fixing defect

After the release of the product too,we can minimize the possibility of occurrence of defects and thereby improve the software reliability. Some of the tools useful for this are- Trend Analysis,Orthogonal Defect Classification and formal methods, etc..

#### Types of reliability Testing
Software reliability testing includes Feature Testing, Load Testing and Regression Testing

#### Feature Testing

Featured Testing check the feature provided by the software and is conducted in the following steps:-

- Each operation in the software is executed at least once.
- Interaction between the two operations is reduced.
- Each operation have to be checked for its proper execution.

#### Load Testing

Usually, the software will perform better at the beginning of the process and after that, it will start degrading. Load Testing is conducted to check the performance of the software under maximum work load.

#### Regression Test

Regression testing is mainly used to check whether any new bugs have been introduced because of the fixing of previous bugs. Regression Testing is conducted after every change or updation of the software features and their functionalities.

## Compliance Testing / Conformance Testing
---
Conformance Testing is a software testing technique used to certify that the software system complies with the standards and regulations as defined by IEEE, W3C or ETSI. The purpose of conformance testing is to determine how a system under test confirms to meet the individual requirements of a particular standard. Conformance Testing is also called Compliance Testing.

It may deal with some technical aspect but intentionally it includes:

- Performance
- Functions
- Robustness
- Interoperability
- Behavior of system

#### Types of Conformance Testing
Conformance Testing can be logical or physical, and it comprises following types of testing;

- Compliance Testing
- Load Testing
- Stress Testing
- Volume Testing

#### Why do we need Conformance Testing?
To check for the system’s requirements fulfillment
To check whether the system documentation is complete with needful
To check the development, design and evaluation as per specifications

#### What do we need to test?
- The standards through which the implementation takes place
- The call of the system that is to be developed
- Scope of specifications
- Specification objectives

Conformance Testing is initiated by the management with total assurance about the team and their understanding of standards, specifications, and procedures.

To build an efficient application, standards and specifications should be clearly mentioned to avoid ambiguities. If not then conformance testing is itself useful to take the necessary steps to make it relevant and reliable.

## Localization Testing
---
Localization Testing is a software testing technique in which the behavior of a software is tested for a specific region, locale or culture. The purpose of doing localization testing for a software is to test appropriate linguistic and cultural aspects for a particular locale. It is the process of customizing the software as per the targeted language and country.

The major area affected by localization testing includes content and UI.

It is a process of testing a globalized application whose UI, default language, currency, date, time format, and documentation are designed as per the targeted country or region. It ensures that the application is capable enough for using in that particular country.

#### Example
- If the project is designed for Tamil Nadu State in India, The designed project should be in Tamil language, Tamil virtual keyboard should be present, etc.
- If the project is designed for the USA, then the time format should be changed according to the USA Standard time. Also, language and money format should follow USA standards.
