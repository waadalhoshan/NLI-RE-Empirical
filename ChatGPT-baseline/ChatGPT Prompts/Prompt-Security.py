examples = """
Security:
- On receipt of a valid (i.e. authorized) request for data stored in the CNG the CNG shall return the requested data to the requesting user.
- On receipt of a valid (i.e. authorized) request for access to a CNG-hosted service or application the CNG shall provide the requested service or application to the requesting user.
- On detection of any system failure or discontinuity not specifically handled by other mechanisms the CNG shall revert to a known safe state.
- The CNG shall support mechanisms to authenticate itself to the NGN for connectivity purposes.

Non-security:
- The CNG shall be equipped with a WAN interface towards the NGN, implementing layer 1 and 2 functionalities ("one-box" solution).
- LAN interfaces. The CNG shall be equipped with at least one Ethernet (minimum 100 Mbit/s) interface. Optional interfaces could be present, e.g., wireless LAN Wi-Fi Alliance certified, Powerlines, Plastic Optical Fiber, USB device and/or host, one or more FXS for analog telephony, DECT Cat-iq.
- The CNG shall support both routed and bridged modes of operation.
- The CNG shall support direct intra-LAN connectivity between any appropriate pair of devices on the Customer Premises Network.
"""



definitions = """
Security: Security requirements are prescriptive constraints imposed on a system’s functional behaviour to operationalize its security goals. They are not functional requirements themselves but restrict how functions are performed to prevent, detect, or recover from harm. Security requirements are derived from business and functional goals and may be categorized as primary—directly supporting fundamental security objectives—or secondary—enabling the fulfilment of primary goals when direct enforcement is infeasible or costly. They can be manifestations of high-level organizational policies into specific system requirements and are deeply tied to the broader system context, which may include non-software components or processes. Security requirements can define and specify security policies and must address risks, threats, and assets while influencing and being influenced by security mechanisms, vulnerabilities, and attacks. They can be categorised according to the following classes.
Confidentiality Requirements: Protect sensitive information from unauthorized access or disclosure.
Integrity Requirements: Ensure data and systems are accurate and protected from unauthorized modifications.
Availability Requirements: Guarantee that systems and data are accessible when needed, mitigating risks like denial-of-service attacks.
Authentication Requirements: Verify the identity of users or systems accessing resources.
Authorization Requirements: Define and enforce what actions users or systems are permitted to perform.
Non-repudiation Requirements: Ensure actions or transactions cannot be denied by the parties involved.
Physical Security Requirements: Safeguard physical infrastructure and assets from threats.
Regulatory Compliance Requirements: Adhere to legal, industry, or contractual obligations related to security.

Non-security: Non-security requirements refer to constraints or specifications that govern a system’s behavior, performance, and structure without being directly tied to security goals. Unlike security requirements, they do not aim to prevent, detect, or recover from harm, and do not operationalize security policies. These requirements may include functional requirements (which define what the system should do) and other non-functional requirements such as Availability, Fault Tolerance, Legal, Look & Feel, Maintainability, Operational, Performance, Portability, Scalability, Usability. Non-security requirements are typically derived from business needs and user expectations but are not intended to address risks, threats, or vulnerabilities. While they may influence the system design and operation, they do not explicitly enforce security mechanisms or aim to mitigate security concerns. Non-security requirements do not include the following types of requirements.
Confidentiality Requirements: Protect sensitive information from unauthorized access or disclosure.
Integrity Requirements: Ensure data and systems are accurate and protected from unauthorized modifications.
Availability Requirements: Guarantee that systems and data are accessible when needed, mitigating risks like denial-of-service attacks.
Authentication Requirements: Verify the identity of users or systems accessing resources.
Authorization Requirements: Define and enforce what actions users or systems are permitted to perform.
Non-repudiation Requirements: Ensure actions or transactions cannot be denied by the parties involved.
Physical Security Requirements: Safeguard physical infrastructure and assets from threats.
Regulatory Compliance Requirements: Adhere to legal, industry, or contractual obligations related to security.
"""


text = ""
system_prompt = "As an expert system for classifying software requirements, your job is to carefully review each requirement and place it into one of these two classes: Security or Non-security\n"
CoT_prompt = f"Let's analyze the classification step by step. Step 1: Understand the Definitions: {definitions}. Step 2: Review the examples: {examples}, Step 3: Apply this understanding to Requirement: {text}, each requirement is presented in one line. Step 4: Provide the final label in the format: 'Requirement Number Here. Label: [Your Class Label Here]'."
