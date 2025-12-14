examples = """
Functional:
- The system shall have an MDI form that allows for the viewing of the graph and the data table.
- The system shall display Events in a vertical table by time.
- The system shall display the Events in a graph by time.
- The system shall display Events or Activities.

Non-Functional:
- The system should support a range of server operating systems.
- The system should run in a clustered server environment in an active-passive configuration.
- The system shall have a professional appearance.
- The product shall have a consistent color scheme and fonts.
"""



definitions = """
Functional: Functional requirements define the essential functions a system must perform, the services it must offer, and the behaviours it must exhibit under specified conditions. They focus on what the system should do—describing actions, operations, or transformations the system executes—without addressing implementation constraints. They typically specify the inputs (stimuli) to the system, the outputs (responses) from the system, and the behavioural relationships between them.

Non-functional: Non-functional requirements do not define the essential functions a system must perform, the services it must offer, or the behaviours it must exhibit under specified conditions. They do not focus on what the system should do—avoiding descriptions of actions, operations, or transformations the system executes—and instead address implementation constraints. They typically exclude specifications of inputs (stimuli) to the system, outputs (responses) from the system, and behavioural relationships between them.
"""


system_prompt = "As an expert system for classifying software requirements, your job is to carefully review each requirement and place it into one of these two classes: Functional or Non-functional\n\n\n"
CoT_prompt = f"Let's analyze the classification step by step. Step 1: Understand the Definitions: {definitions}. Step 2: Review the examples: {examples}, Step 3: Apply this understanding to Requirement: {text}, each requirement is presented in one line. Step 4: Provide the final label in the format: 'Requirement Number Here. Label: [Your Class Label Here]'."
