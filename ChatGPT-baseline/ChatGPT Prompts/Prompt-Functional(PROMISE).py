examples = """
Functional:
● The system shall allow modification of the display.
● The system shall offer a display of all the Events in the exercise.
● The system shall filter data by Venues and Key Events.
● The system shall allow a user to define the time segments.

Non-functional:
● 90% of untrained realtors shall be able to install the product on their device without printed instructions.
● The product is expected to run on Windows CE and Palm operating systems.
● Only registered realtors shall be able to access the system.
● Every user of the system shall be authenticated and authorized.
"""

definitions =  """
Definitions

Functional: Functional requirements define the essential functions a system must perform, the services it must offer, and the behaviours it must exhibit under specified conditions. They focus on what the system should do—describing actions, operations, or transformations the system executes—without addressing implementation constraints. They typically specify the inputs (stimuli) to the system, the outputs (responses) from the system, and the behavioural relationships between them.

Non-functional: Non-functional requirements identify any property, characteristic, attribute, quality, constraint, or performance aspect of a system. These requirements are not specifically concerned with the functionality of a system. They place restrictions on the product being developed and the development process and specify criteria that can be used to judge the operation of a system, rather than specific behaviours. Non-functional requirements include Performance (concerned with responsiveness and efficient processing); Scalability (ability of the system to handle growth in users or data); Portability (operation across different platforms and environments); Compatibility (smooth interaction with other systems); Reliability (guaranteeing consistent and failure-free operation); Maintainability (ease of updating and modifying the system); Availability (measuring the system's uptime and accessibility); Security (protection measures against unauthorized access and threats); Usability (ensuring the system is intuitive and user-friendly); Fault Tolerance (system’s ability to continue operating correctly even when faults occur); Legal (compliance with laws, regulations, and licensing); Look & Feel (visual appearance and user-interface consistency); and Operational (covering system operations).
"""



system_prompt = "As an expert system for classifying software requirements, your job is to carefully review each requirement and place it into one of these two classes: Functional or Non-functional\n\n\n"
CoT_prompt = f"Let's analyze the classification step by step. Step 1: Understand the Definitions: {definitions}. Step 2: Review the examples: {examples}, Step 3: Apply this understanding to Requirement: {text}, each requirement is presented in one line. Step 4: Provide the final label in the format: 'Requirement Number Here. Label: [Your Class Label Here]'."
