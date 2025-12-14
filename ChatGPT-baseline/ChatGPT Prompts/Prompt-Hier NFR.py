definitions_level1 = """

  Definitions for Root Classes:

  Functional: Functional requirements define the essential functions a system must perform, the services it must offer, and the behaviours it must exhibit under specified conditions. They focus on what the system should do—describing actions, operations, or transformations the system executes—without addressing implementation constraints. They typically specify the inputs (stimuli) to the system, the outputs (responses) from the system, and the behavioural relationships between them.

  Non-functional: Non-functional requirements identify any property, characteristic, attribute, quality, constraint, or performance aspect of a system. These requirements are not specifically concerned with the functionality of a system. They place restrictions on the product being developed and the development process and specify criteria that can be used to judge the operation of a system, rather than specific behaviours. Non-functional requirements include Performance, which is concerned with responsiveness and efficient processing; Scalability, which is concerned with the ability of the system to handle growth in users or data; Portability, which is concerned with operation across different platforms and environments; Compatibility, which is concerned with smooth interaction with other systems; Reliability, which is concerned with guaranteeing consistent and failure-free operation; Maintainability, which refers to the ease of updating and modifying the system; Availability, which measures the system's uptime and accessibility; Security, which is concerned with protection measures against unauthorized access and threats; Usability, which ensures the system is intuitive and user-friendly; Fault Tolerance, which refers to the system’s ability to continue operating correctly even when faults occur; Legal, which involves compliance with laws, regulations, and licensing; Look & Feel, which relates to the visual appearance and user interface consistency; and Operational, which covers system operations."""


definitions_level2 = """
  Definitions for Subclass (Only for Non-functional):

  Security – Security requirements define the protections needed for both the system’s facility (physical security) and its operations (cybersecurity), such as access control, data encryption, and threat mitigation. Examples include login authentication, audit logs, and restricted communication between system components—especially critical in safety-critical systems to prevent unauthorized access or data breaches.

  Performance – Performance requirements specify the system's critical operational capabilities, including speed (e.g., response times, movement rates), endurance (e.g., lifespan, session duration), and efficiency under defined conditions. They also define performance expectations for different operational modes and phases, ensuring the system meets user needs in real-world use.

  Operational – Operational requirements define the specific conditions, constraints, and scenarios under which a system must function effectively. They describe the operational environment, expected usage patterns, and interactions with users, other systems, and external factors.

  Scalability – Scalability requirements define the capability of a system to expand and adapt to the changing size and needs of the client and the environment in which the system is deployed. They ensure the system can handle increased workloads (e.g., more users, higher data volumes) without sacrificing performance, often through modular design or elastic resource allocation.

  Usability – Usability requirements define how easily, effectively, efficiently, and satisfactorily users can achieve their goals with the system. They include measurable criteria for: ease of use (intuitive navigation, minimal training required, accessibility compliance); effectiveness (task completion accuracy, error rates); efficiency (time/resources required, steps to completion); user satisfaction (feedback scores, comfort, perceived usability).

  Maintainability – Maintainability requirements define measurable targets for keeping the system operational, including downtime limits (e.g., mean time to repair, MTTR), resource efficiency (e.g., staff hours per repair), and logistical factors like component accessibility. They cover metrics such as repair rates, maintenance frequency, cost-per-operation, and the complexity of tasks (e.g., tools or skills needed). These requirements ensure the system can be sustained efficiently in its planned support environment.

  Availability – Availability requirements define the degree to which a system, service, or component must be operational and accessible during specified periods and under defined conditions. These requirements establish measurable expectations for uptime (e.g., 99.9% availability), scheduled operational windows (e.g., 24/7 or business hours), and permissible downtime (e.g., no more than 10 minutes per year). They may also specify recovery timelines after outages, dependency-based availability (e.g., subject to network accessibility), and varying thresholds for critical operational periods. Availability requirements ensure consistent service delivery, align with user expectations, and support continuity of operations—especially important in systems requiring round-the-clock access or those with time-sensitive functions.

  Look and Feel – Look and feel requirements are quality requirements that consider all static and dynamic aspects of the user interface, including colors, shapes, layout, typefaces, buttons, boxes, and menus. They ensure visual consistency, branding alignment, and intuitive interaction patterns across the system. These requirements may also define responsiveness (e.g., animations, transitions) and accessibility standards (e.g., contrast ratios, font sizes).

  Legal – Legal requirements define a system's conformity with data privacy laws, industry regulations, and technical standards. They ensure compliance with frameworks like GDPR, HIPAA, or ISO certifications, covering: data protection (storage, processing, user consent); auditability (logging, documentation); jurisdictional rules (regional/industry-specific mandates).

  Fault Tolerance – Fault tolerance requirements define the system’s capability to detect, isolate, and recover from failures while maintaining continuous operation. They ensure: automatic fault detection (e.g., checksums, heartbeat signals); redundancy (backup components, failover mechanisms); graceful degradation (preserving critical functions during partial failures).
"""

examples_level1 = """

Examples of Root Classes:

Functional:
-The system shall allow modification of the display.
-	The system shall offer a display of all the Events in the exercise.
-	The system shall filter data by Venues and Key Events.
-	The system shall allow a user to define the time segments.

Non-functional:
-	90% of untrained realtors shall be able to install the product on their device without printed instructions.
-	The product is expected to run on Windows CE and Palm operating systems.
-	Only registered realtors shall be able to access the system.
-	Every user of the system shall be authenticated and authorized.

"""

examples_level2 = """
Examples for Subclasses:

Security:
-	'Every user of the system shall be authenticated and authorized.'
-	'The product shall prevent its data from incorrect data being introduced.'
-	'Only authorized users shall have access to clinical site information.'
-	'Program Administrators/Nursing Staff Members are the only people who shall have access to clinical site details.'

Performance:
-	'The system shall refresh the display every 60 seconds.'
-	'The product shall respond fast to keep up-to-date data in the display.'
-	'The product shall produce search results in an acceptable time'
-	'The search results shall be returned no later 30 seconds after the user has entered the search criteria'

Operational:
-	'The system shall able to operate within a business office environment typical of the Nursing Department at DePaul University.'
-	'The system shall be used within the specifications defined by the computers used by the Program Administrators/Nursing Staff Members.'
-	'The system shall operate within the Windows XP Professional operating system.'
-	'The system shall interface with CampusConnect’s central server'

Scalability:
-	'The product shall be able to support multiple remote users'
-	'The product shall be able support 1000 simultaneous users.'
-	'The product shall be capable of handling the existing 1000 users. This number is expected to grow 5 times within the next year.'
-	'system shall be able to handle all of the user requests/usage during business hours.'

Usability:
-	'The system shall be intuitive and self explanatory.'
-	'The product shall be easy for a realtor to learn.'
-	'The product shall use symbols and words that are naturally understandable by the realtor community.'
-	'The product shall be installed by an untrained realtor without recourse to separately-printed instructions.'

Maintainability:
-	'Washing parameters will be updated during scheduled maintenance hours.'
-	The product shall be internet browser independent.The product must run using Internet Explorer and Netscape Navigator.'
-	'Application updates shall occur between 3AM and 6 AM CST on Wednesday morning during the middle of the NFL season.'
-	'New System version releases shall be released at the beginning of each NFL season.'


Availability:
-	'The application shall have a downtime of at most 10 minutes per year.'
-	'All movies shall be streamed on demand at any time of the day.'
-	'The system shall achieve 95% up time.'
-	'The website shall be available for use 24 hours per day 365 days per year.'

Look and Feel:
-	'The application shall match the color of the schema set forth by Department of Homeland Security'
-	'The look and feel of the system shall conform to the user interface standards of the smart device.'
-	'The user interface shall have standard menus buttons for navigation'
-	'The system shall have a professional appearance'

Legal:
-	'The product must comply with Sarbanes-Oxley.'
-	'The product shall comply with the estimatics laws relating to recycled parts usage.'
-	'The product shall comply with insurance regulations regarding claims processing.'
-	'The website will comply with W3C standards.'

Fault Tolerance:
-	'The product shall operate in offline mode whenever internet connection is unavailable.'
-	'The product shall allow the user to view previously downloaded search results CMA reports and appointments.'
-	'The product shall retain user preferences in the event of a failure.'
-	'100% of saved user preferences shall be restored when system comes back online.'

"""


system_prompt = f"""As an expert system for classifying software requirements using a hierarchical classification approach, your job is to carefully review each requirement and classify it through two levels:

Level 1 – Root Classification
Classify the requirement as either:
• Functional
• Non-functional

Level 2 – Subclass (only for Non-functional)
If the requirement is Non-functional, assign it to one of these specific subclasses:
- Security
- Performance
- Operational
- Scalability
- Usability
- Maintainability
- Availability
- Look and Feel
- Legal
- Fault Tolerance

Let’s proceed step by step:
Step 1 – Understand the Definitions of level 1 and level 2 classes:
{definitions_level1}
{definitions_level2}

Step 2 – Review the Examples:
{examples_level1}
{examples_level2}

Step 3 – Each requirement is presented in one line, review that requirement carefully.

Step 4 - Apply your understanding of defintions and examples presented eariler to Requirement: {text}.

Step 5 - For each Requirement , apply this hierarchical classification:
• Step 5.1 – Classify as either Functional or Non-functional (level 1)
• Step 5.2 – If Non-functional, classify further into one of the subclasses listed above (level 2)
• Step 5.3 – If Functional, put 'NA'

Step 6 – Provide the final label in this format, do not put extra text:
Level 1 Label: [Your Class Label Here] --> Level 2 Label: [Your Subclass Label Here]

The definitions for these classes are provided in the following."""