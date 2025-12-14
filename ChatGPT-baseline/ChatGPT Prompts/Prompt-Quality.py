examples = """Quality:
-   The top 1/4 of the table will hold events that are to occur sequentially.
-   The bottom 3/4 of the table will hold events that occur according to their relevance to the current time.
-   The system shall color-code events according to their variance from the current time.
-   The system shall display data from the Sync Matrix 1.0 and Exercise Management Tool 1.0 applications.

Non-quality:
-   User shall be able to update the attachment.
-   User shall be able to create a directed link between requirements in the same document.
-   User shall be able to clear the history of all requirements in the document.
-   User shall be able to print the current document.
"""


definitions = """Quality: A quality requirement expresses how well a system or service should execute an intended function. They include attributes or constraints that address product quality aspects and quality-in-use aspects. Product quality aspects are:
- Functional Suitability (Functional Completeness, Functional Correctness, Functional Appropriateness)
- Reliability (Maturity, Availability, Fault Tolerance, Recoverability)
- Performance Efficiency (Time Behaviour, Resource Utilization, Capacity)
- Usability (Appropriateness Recognisability, Learnability, Operability, User Error Protection, User Interface Aesthetics, Accessibility)
- Maintainability (Modularity, Reusability, Analysability, Modifiability, Testability)
- Security (Confidentiality, Integrity, Non-repudiation, Accountability, Authenticity)
- Compatibility (Co-existence, Interoperability)
- Portability (Adaptability, Installability, Replaceability)
Quality requirements often address the global properties or characteristics of the system rather than those of specific functions.

Non-quality: A non-quality requirement does not express how well a system or service should execute an intended function. They exclude attributes or constraints that address any of the product quality aspects listed above. Non-quality requirements focus on the specific behavior or functionality of the system and do not address global properties or characteristics.
"""

system_prompt = "As an expert system for classifying software requirements, your job is to carefully review each requirement and place it into one of these two classes: Quality or Non-quality\n\n\n"
CoT_prompt = f"Let's analyze the classification step by step. Step 1: Understand the Definitions: {definitions}. Step 2: Review the examples: {examples}, Step 3: Apply this understanding to Requirement: {text}, each requirement is presented in one line. Step 4: Provide the final label in the format: 'Requirement Number Here. Label: [Your Class Label Here]'."
