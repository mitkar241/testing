# Functional Testing
---
Let’s explore these types of functional tests with examples:
- [Unit testing](#unit-testing)
- [Component testing / Module testing](#component-testing--module-testing)
- [Smoke testing](#smoke-testing)
- [Sanity testing](#sanity-testing)
- [Regression testing](#regression-testing)
- [Integration testing](#integration-testing)
- [API testing](#api-testing)
- [UI testing](#ui-testing)
- [System testing](#system-testing)
- [White-box testing](#white-box-testing)
- [Black-box testing](#black-box-testing)
- [Acceptance testing](#acceptance-testing)
- [Alpha testing](#alpha-testing)
- [Beta testing](#beta-testing)
- [Production testing](#production-testing)

## Unit testing
---
Before you can test an entire software program, make sure the individual parts work properly on their own. Unit testing validates the function of a unit, ensuring that the inputs (one to a few) result in the lone desired output. This testing type provides the foundation for more complex integrated software. When done right, unit testing drives higher quality application code and speeds up the development process. Developers often execute unit tests through test automation.
#### Example:
A developer builds a calculator app. A unit test would check whether the user can input two numbers and receive an accurate sum. Separate unit tests would validate other calculator functionality, such as subtraction, multiplication and division.

## Component testing / Module testing
---
component testing checks individual parts of an application. Similar to unit testing, component testing assesses a part of the software in isolation from the broader system. The difference between unit testing and component testing is that the former is done by developers in a white-box format to verify that program modules execute, while the latter is done by testers in a black-box format to validate individual objects or parts of the software. If other software components rely on the component under test, the QA professional might use a stub and driver to simulate interactions between those dependent components.
#### Example:
A banking mobile app includes an option to schedule an appointment with a banking professional. The stub provides a simulated user profile, and the driver provides a simulated schedule of available appointment times. In this functional testing example, the middle component — the one under test — finds the user’s location via GPS and displays local banking centers from which they can choose. By testing this component in isolation, the tester can ensure that the geolocation service works correctly and displays an accurate list of nearby locations.

## Smoke testing
---
Smoke testing, a type of acceptance testing, provides an initial check that a new software build and its critical functionality are stable. If the smoke tests pass, the build can undergo further testing. Smoke testing, also called build verification testing, often checks whether new or critical functionality meets its objective. If the tests don’t pass, as the saying goes, “where there’s smoke, there’s fire,” and additional dev work is required.
#### Example:
A web app for an insurance company adds a claims status page. Testers would apply smoke tests to verify that the existing build works on a fundamental level, such as whether a user can successfully log in, navigate to the claims status page and retrieve the status of a specific claim without the app crashing or malfunctioning.

## Sanity testing
---
A type of regression testing, QA professionals perform sanity testing on new versions of stable builds to validate either new functionality or bug fixes. While similar to smoke testing in that both provide a gate check that a build is ready for more testing, sanity testing is unscripted and specifically targets the area that has undergone a code change.
#### Example:
A web page for a telehealth provider returns a 404 error for its mental health page. The developers fix the issue, then commit the build for testing. The QA professional performs a sanity check to determine whether the basic functionality and navigation for that specific page work as intended.

## Regression testing
---
Just because functional tests pass once doesn’t mean they’ll always pass. When developers commit new code or change a feature, you run regression tests to make sure the software still functions as expected. Regression testing helps maintain a stable product while changes are made to it. Regression tests are often automated.
#### Example:
A clothing retailer adds the ability to pay with customer rewards points on their mobile app. Testers might perform regression tests on other existing functionality, such as the ability to pay with credit cards and gift cards, to make sure all forms of payment work correctly.

## Integration testing
---
Integration testing is often done in concert with unit testing. Through integration testing, QA professionals verify that individual modules of code work together properly as a group. Many modern applications run on microservices, self-contained applications that are designed to handle a specific task. These microservices must be able to communicate with each other, or the application won’t work as intended. Through integration testing, testers ensure these components operate and communicate together seamlessly.
#### Example:
A credit card company includes a page where a customer can request a credit increase, which is a separate code base from login functionality. Testers might perform integration tests to make sure the system remembers the user after they navigate to the credit increase page, and again after a successful request.

## API testing
---
Application programming interfaces connect different applications or systems, and they are growing in popularity as consumers expect apps to interoperate. With API testing, testers validate that API connections and responses function as intended, including how they handle data and user permissions.
#### Example:
A travel booking site might pull pricing data from an airline company’s database via APIs. Through API testing, QA professionals can verify that the correct data type is returned in the local currency and responsive to changes in date and location.

## UI testing
---
With UI testing, QA professionals interact with the graphical interface of a software program. This includes testing of UI controls like buttons, menus and text input to ensure that the experience flow and features chosen are optimal for the user experience.
#### Example:
A wearables maker creates a mobile app for product setup and maintenance. As part of UI testing, the team would make sure that required fields function as expected, images display correctly and maintenance information appears in the app dashboard after use.

## System testing
---
With system testing, QA professionals test the software in its entirety, as a complete product. With this type of functional testing, testers validate the complete and integrated software package to make sure it meets requirements. Where necessary, testers can provide feedback on the functionality and performance of the app or website without prior knowledge of how it was programmed. This helps teams develop test cases to be used moving forward. System testing is also referred to as end-to-end testing.
#### Example:
An automobile manufacturer produces an in-car entertainment system that gives users functionality for voice control, GPS, a video player, Bluetooth connectivity, mobile phone pairing, touch-screen support and climate control. Testers would assess all of these features individually, but they must also test them as a complete system to ensure interoperability and a good user experience.

## White-box testing
---
When the software’s internal infrastructure, code and design are visible to the developer or tester, that refers to white-box testing. This approach incorporates various functional testing types, including unit, integration and system testing. In a white-box testing approach, the organization tests several aspects of the software, such as predefined inputs and expected outputs, as well as decision branches, loops and statements in the code.
#### Example:
In this functional testing example, consider an end-to-end test for a customer who adds payment information to a retailer’s app. Developers and testers would conduct tests in a white-box format to ensure that sensitive data, such as a credit card number, is stored in a PCI-compliant manner. White-box tests might also ensure that purchase information flows to a machine learning algorithm to generate predictions, the purchase correctly generates rewards points, and the inventory system deducts the items from the stock count.

## Black-box testing
---
Contrary to white-box testing, black-box testing involves testing against a system where the internal code, paths and infrastructure are not visible. Thus, testers use this method to validate expected outputs against specific inputs. Any time where a QA professional doesn’t look into the code before testing can be considered black box. With black-box testing, the organization can test the software in the same way a customer would experience it. Black-box testing encompasses a variety of non-functional and functional testing types, depending on the objective of the test.
#### Example:
On a streaming television platform, the tester toggles the search functionality and executes a search for a specific actor. The tester then verifies that the search feature returns logical (expected) outputs, including television shows that the actor appeared in, or suggested titles similar to that actor’s well-known works.

## Acceptance testing
---
The purpose of acceptance testing is purely to ensure that the end user can achieve the goals set in the business requirements. Rather than focus on functionality of specific features, acceptance testing involves reviewing the feature-complete application flow and end-to-end experience. User acceptance testing (UAT) and beta testing, subsets of acceptance testing, involve end users to conduct their analysis of the finished product. From there, the organization can evaluate that feedback and make changes.
#### Example:
A software company releases a product that enables its users to manage big data. Upon release of a new version of the software, a group of that company’s most significant users conducts user acceptance testing to determine whether the new version meets their primary needs and how the product can be improved.

## Alpha testing
---
Another subset of acceptance testing, alpha testing uses internal team members to evaluate the product. These team members should be knowledgeable of the project but not directly involved in its development or testing. Where some builds might still be somewhat unstable, alpha testing provides an immediate subset of testers to root out major bugs before the software is seen by external users.
#### Example:
In this functional testing example, a casino games provider releases a new version of its app that includes video poker. The organization compiles a cross-functional group of internal users that test whether the app functions correctly on their devices and how the user experience can improve.

## Beta testing
---
After the internal team tests the product and fixes bugs, beta testing occurs with a select group of end users. Beta testing serves as a soft launch, enabling you to get feedback from real users who have no prior knowledge of the app. Beta testing enables you to gather feedback from unbiased users who may interact with the product differently than you intended, perhaps identifying critical unknown bugs before release to a wide user base.
#### Example:
A restaurant chain releases a new mobile order and pickup system. Before the company releases the functionality to all of its mobile app users, it tests the app with a small number of dedicated customers and provides them with rewards for participating.

## Production testing
---
Once the product goes public, it is in a live production environment where any user can interact with it in any way — you no longer can control everything from the testing environment to the number of people using the product. Production testing is part of continuous testing and shift-right testing, which attempts to discover and triage user-reported defects as quickly as possible. By testing in production, the organization can test beyond the scripted test cases in a varied environment. With production testing, the organization can confirm product functionality and stability.
#### Example:
A fitness equipment manufacturer can monitor user-reported defects and device metrics to make sure its internet-connected treadmills, elliptical and stair-climbing machines function as they should — upon delivery and continuously.
