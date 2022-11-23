# Towards a standardized model for privacy-preserving Verifiable Credentials

Abstract: Lack of standardization and the subsequent difficulty of integration has been one of the main reasons for the scarce adoption of privacy-preserving Attribute-Based Credentials (p-ABC). Integration with the W3C’s Verifiable Credentials (VC) specification would help by encouraging homogenization between different p-ABC schemes and bringing them all closer to other digital credentials. What is more, p-ABCs can help to solve privacy issues that have been identified in applications of VCs to use cases like vaccination passports. However, there has not been much work focusing on the collaboration between p-ABCs and VCs. We address this topic by establishing initial steps for extra standardization of elements that will help with the integration of p-ABCs into the standard. Namely, we propose a data model for predicates, which are a staple of p-ABC systems, and tools and guidelines to ease the adaptation process like a validation meta-schema. These ideas have been applied in a proof-of-concept implementation of the OLYMPUS distributed p-ABC scheme paired with serialization following the VC data model.
Actions needed and questions: @Jorge Arce-Garro any opinion on this piece?
Added to deliverable?: No
Already read?: Yes
Assigned readers: Jorge Arce-Garro
BS factor: weak
Classification: VC
Date of publication: 2021
Link to the paper: https://dl.acm.org/doi/abs/10.1145/3465481.3469204
MZ checked the note: No
Presentation date: November 24, 2022
Reviewers: Michal Zajac
Score Phase 1: Relevant
Work Group: Hybrid

The paper talks about a spec for privacy-preserving attribute-based credentials (p-ABC) that will be compatible with W3C’s verifiable-credential standard. (See definition of p-ABC below). In other words, this proposal can be seen as a way to add privacy to verifiable credentials in a standardized way.

While the idea of combining p-ABCs with VCs in a canonical way is well-received and relevant, the contributions of the paper look rather minor—they consist mostly of recommendations of how to modify the existing standard.

**Remark: p-ABCs = anonymous credentials.**

---

# I. Introduction

### What is a p-ABC?

- In a nutshell, the user receives a credential that contains a set of certified attributes (e.g. date of birth, nationality, etc).
- When she wants to access a service, which specifies an access policy P, she can generate a presentation token using her credential.
- The presentation token contains only the minimal attributes requested by the policy and is even capable of including predicate proofs which allow avoiding data disclosure to a further extent (i.e. the user is over 18 instead of being exactly 20 years old).

### The problem:

- Adoption of p-ABCs has been scarce because of multiple reasons like:
    - lack of efficiency of existing solutions
    - difficulty of integration with existing technologies because of the complexity and particularity of the processes and structures involved.
- The integration of p-ABCs with the structures proposed in the [W3C’s verifiable credentials] specification is not trivial. There is room for improvement on actually ensuring privacy is attained and on extra devices and definitions to encourage adoption of the data model by p-ABC systems.
- No work in the literature considers the application of p-ABCs along with the VC specification.
    - From the Related Work section: “This issue is especially jarring because proper usage of p-ABCs while avoiding identifiers (which, admittedly, are optional as per the specification) would solve most or all of the privacy concerns that have been pointed in the existing literature.”

### The paper’s contribution:

- (…) providing tools useful for all p-ABC systems that want to follow the specification. Chiefly, we propose a data model for representing predicates over attributes in Verifiable Credentials and Presentations and materials and guidelines facilitating integration like a validation meta-schema.
- A description of how we have applied the results to distributed p-ABCs implemented in the H2020 OLYMPUS project is also provided.

# III. Verifiable credentials specification

Key concepts: verifiable credentials and verifiable presentations (sharing data from credentials to a third party)

Roles: Issuers generate verifiable credentials to holders, which use them to present information to verifiers. Process supported by a verifiable data registry—can be a blockchain.

Other definitions and constraints:

- The context property is used to map short and human-readable property names to the URIs that define those elements.
- Schemas (credentialSchema) are used for imposing the structure and content of the credential, verifying that they conform to a predefined format or even transforming it into a different encoding.
- The proof property introduces the necessary details to evaluate a credential.
    - Embedded proofs are particularly relevant because they are necessary to embody p-ABC specific proof formats. The specification takes into account the variability for proofs and leaves the set of name-value pairs that are expected inside a proof open.

The discussion on potential privacy concerns affecting the specification and possible solutions is somewhat lacking for particular topics.

- For instance, to limit the Personal Identifiable Information (PII) revealed in the usage of Verifiable Credentials, the specification proposes using abstract claims like “ageOver”. This is a band-aid solution—it would require generating many “ageOver” attributes: ageOver18, ageOver21, increasing credential size and complexity unnecessarily. With p-ABCs, predicates over the original attributes can simply be proven during the presentation phase, avoiding these issues.
- Single-use credentials are also proposed to maintain privacy of attributes that need not be disclosed. This is unnecessary with p-ABCs.

# IV. Towards a data model for p-ABCs in verifiable credentials

Main goal: establishing a model for representing the predicates over attributes that characterize p-ABCs

- The key idea is representing the predicates as simple JSON objects so there are two possibilities for attributes (JSON properties) when doing a presentation: a valid value or a predicate. Example:

![Untitled](Towards%20a%20standardized%20model%20for%20privacy-preservin%2057577cf2dcd341909101f39b7f7afe2a/Untitled.png)

(Source: present document)

- Furthermore, we define a validation schema for this model, to facilitate verification of the credential. This schema will assist when parsing the predicates.

![Untitled](Towards%20a%20standardized%20model%20for%20privacy-preservin%2057577cf2dcd341909101f39b7f7afe2a/Untitled%201.png)

(Source: present document)

- The specification also points to the need for an encoding schema that manages the transformation of the content into the formats needed for zero-knowledge computations. (Note: no mention of how this could happen, specifically)