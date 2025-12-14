definitions = """

Security  Security requirements define the protections needed for both the system’s facility (physical security) and its operations (cybersecurity), such as access control, data encryption, and threat mitigation. Examples include login authentication, audit logs, and restricted communication between system components—especially critical in safety-critical systems to prevent unauthorized access or data breaches.

Performance  Performance requirements specify the system's critical operational capabilities, including speed (e.g., response times, movement rates), endurance (e.g., lifespan, session duration), and efficiency under defined conditions. They also define performance expectations for different operational modes and phases, ensuring the system meets user needs in real-world use.

Operational  Operational Requirements define the specific conditions, constraints, and scenarios under which a system must function effectively. They describe the operational environment, expected usage patterns, and interactions with users, other systems, and external factors.

Usability  Usability requirements define how easily, effectively, efficiently, and satisfactorily users can achieve their goals with the system. They include measurable criteria for: ease of use (intuitive navigation, minimal training required, accessibility compliance); effectiveness (task completion accuracy, error rates); efficiency (time/resources required, steps to completion); user satisfaction (feedback scores, comfort, perceived usability).

"""

examples = """

Security:
- Every user of the system shall be authenticated and authorized.
- The product shall prevent its data from incorrect data being introduced.
- Only authorized users shall have access to clinical site information.
- Program Administrators/Nursing Staff Members are the only people who shall have access to clinical site details.

Performance:
- The system shall refresh the display every 60 seconds.
- The product shall respond fast to keep up-to-date data in the display.
- The product shall produce search results in an acceptable time.
- The search results shall be returned no later than 30 seconds after the user has entered the search criteria.

Operational:
- The system shall be able to operate within a business-office environment typical of the Nursing Department at DePaul University.
- The system shall be used within the specifications defined by the computers used by the Program Administrators/Nursing Staff Members.
- The system shall operate within the Windows XP Professional operating system.
- The system shall interface with CampusConnect’s central server.

Usability:
- The system shall be intuitive and self-explanatory.
- The product shall be easy for a realtor to learn.
- The product shall use symbols and words that are naturally understandable by the realtor community.
- The product shall be installed by an untrained realtor without recourse to separately printed instructions.

"""



system_prompt = f"""
As an expert system for classifying software requirements, your job is to carefully review each requirement and place it into one of these classes:

- Security
- Performance
- Operational
- Usability

Let's analyze the classification step by step.

Step 1: Understand the Definitions:
{definitions}

Step 2: Review the examples:
{examples}


Step 3: Apply this understanding to Requirement: {text}, each requirement is presented in one line.

Step 4: Provide the final label in the format: 'Requirement Number Here. Label: [Your Class Label Here]".
"""