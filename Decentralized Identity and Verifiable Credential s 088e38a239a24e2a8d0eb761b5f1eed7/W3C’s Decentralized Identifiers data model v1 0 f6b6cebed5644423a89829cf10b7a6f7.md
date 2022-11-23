# W3C’s Decentralized Identifiers data model v1.0

Abstract: https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers (DIDs) are a new type of identifier that enables verifiable, decentralized digital identity. A https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers refers to any subject (e.g., a person, organization, thing, data model, abstract entity, etc.) as determined by the controller of the https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers. In contrast to typical, federated identifiers, https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers have been designed so that they may be decoupled from centralized registries, identity providers, and certificate authorities. Specifically, while other parties might be used to help enable the discovery of information related to a https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers, the design enables the controller of a https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers to prove control over it without requiring permission from any other party. https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers are https://www.w3.org/TR/did-core/#dfn-uri that associate a https://www.w3.org/TR/did-core/#dfn-did-subjects with a https://www.w3.org/TR/did-core/#dfn-did-documents allowing trustable interactions associated with that subject.
Each https://www.w3.org/TR/did-core/#dfn-did-documents can express cryptographic material, https://www.w3.org/TR/did-core/#dfn-verification-method, or https://www.w3.org/TR/did-core/#dfn-service, which provide a set of mechanisms enabling a https://www.w3.org/TR/did-core/#dfn-did-controllers to prove control of the https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers. https://www.w3.org/TR/did-core/#dfn-service enable trusted interactions associated with the https://www.w3.org/TR/did-core/#dfn-did-subjects. A https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers might provide the means to return the https://www.w3.org/TR/did-core/#dfn-did-subjects itself, if the https://www.w3.org/TR/did-core/#dfn-did-subjects is an information resource such as a data model.
Actions needed and questions: Describe DID in preliminaries
Added to deliverable?: No
Already read?: Yes
Assigned for action: Isaac Villalobos Gutiérrez
Assigned readers: Albert Garreta
BS factor: important
Classification: DI
Date of publication: 2019 - 2022 (updated)
Labels: Standardization efforts
Link to the paper: https://www.w3.org/TR/did-core/
MZ checked the note: No
Presentation date: November 24, 2022
Reviewers: Genya
Score Phase 1: Very relevant
Work Group: Blockchain projects

> Since the generation and assertion of Decentralized Identifiers is entity-controlled, each entity can have as many DIDs as necessary to maintain their desired separation of identities, personas, and interactions. The use of these identifiers can be scoped appropriately to different contexts. They support interactions with other people, institutions, or systems that require entities to identify themselves, or things they control, while providing control over how much personal or private data should be revealed, all without depending on a central authority to guarantee the continued existence of the identifier. These ideas are explored in the DID Use Cases document [[DID-USE-CASES](https://www.w3.org/TR/did-core/#bib-did-use-cases)].
> 

Not quite the same approach as the one we want, since our goal is to prevent Sybil attacks.

---

## Decentralised Identities

A DID refers to any subject (e.g., a person, organization, thing, data model, abstract entity, etc.) as determined by the controller of the DID.

1. DIDs decouple identity management from centralized registries, identity provider, and certificate authorities.
2. DID enables its controller to control it without any permission of a third-party.
3. DIDs are URIs that connect a DID Subject with a DID Document allowing trustable interactions with the subject.

### Intro

URIs (Uniform Resource Identifiers) are used for resources on the Web and each web page viewed in a browser has a globally unique URL (Uniform Resource Locator). Most of these identifiers are not controlled by us and have been issued to us by some third party. 

DIDs aim to resolve the issues posed by such identifiers. They are designed so that users can generate identifiers using systems they trust. These new identifiers enable entities to prove control over them by using cryptographic tools such as digital signatures. 

### What is a DID?

A DID is simply a string of characters consisting of the following components:

1. the DID URI scheme identifier
2. the identifier for the DID method
3. the DID method-specific identifier

![                                                   Fig 1: What a DID looks like](W3C%E2%80%99s%20Decentralized%20Identifiers%20data%20model%20v1%200%20f6b6cebed5644423a89829cf10b7a6f7/Untitled.png)

                                                   Fig 1: What a DID looks like

### DID Architecture

Fig 2 depicts the overall architecture of a Decentralised Identifier Infrastructure.

![                                         Fig 2: Overview of Decentralised Identifier Infrastructure](W3C%E2%80%99s%20Decentralized%20Identifiers%20data%20model%20v1%200%20f6b6cebed5644423a89829cf10b7a6f7/Untitled%201.png)

                                         Fig 2: Overview of Decentralised Identifier Infrastructure

1. DIDs and DID URLs: DID can be defined as a globally unique persistent identifier that does not require a centralised registration authority and is often generated and/or registered cryptographically. DID is a URI composed of three main parts mentioned above. Each DID resolves to a DID Document. A DID URL extends the basic syntax of a DID to incorporate other standard URI components such as paths, queries, and fragment in order to locate a particular resource.
2. DID Subject: DID subject is the entity identified by the DID. The DID Subject might be the DID Controller.
3. DID Controller: The controller of DID is the entity that has the ability to make changes to the DID Document. This ability is asserted by the possession of cryptographic keys. A DID may have more than one controller and this property is defined by the controller attribute of the DID Document.
4. Verifiable Data Registries: In order to resolve the DIDs to DID Documents, DIDs need to be stored on some network or system. The system that supports the storage of DIDs and return data necessary to acquire DID documents is described as Verifiable Data Registry. This is where blockchain comes into picture.
5. DID Documents: DID Documents contain information corresponding to DIDs. The information consists of verification methods and services relevant to interactions with the DID Subject.
6. DID methods: DID methods are the mechanism by which a particular type of DID and its associated DID document are created, resolved, updated, and deactivated.
7. DID Resolver and DID Resolution: A DID Resolver takes a DID as an input and gives the DID Document as the output. This process is called DID Resolution.
8. DID URL dereferencers and DID URL dereferencing: DRL deferencer takes a DID URL as input and produces a DID Resource as output. This process is called DID dereferencing.

More terminologies:

1. DID Delegate: DID delegate is a body who has been granted permission by the DID controller to use a verification method associated with a DID via a DID document.
2. DID Fragment: The portion of a DID URL that follows the first hash sign character (#). DID fragment syntax is identical to URI fragment syntax.
3. DID Path: The portion of a DID URL that begins with and includes the first forward slash (/) character and ends with either a question mark (?) character, a fragment hash sign (#) character, or the end of the DID URL.
4. public key description: A data object contained inside a DID document that contains all the metadata necessary to use a public key or a verification key.
5. Services: Means of communicating with a DID Subject or associated entities via one or more service endpoints.
6. Service endpoint: An HTTP URL at which entities operate on behalf of a DID subject.

### Data Model

A DID Document consists of a map of entries, where each entry consists of a key/value pairs. The DID Document consists of at least two classes of entries - (i) properties; and (ii) representation specific entries.

![Untitled](W3C%E2%80%99s%20Decentralized%20Identifiers%20data%20model%20v1%200%20f6b6cebed5644423a89829cf10b7a6f7/Untitled%202.png)

Keys - strings

Values - map, list, set, datetime, string, integer, double, boolean, null

### Core Properties

A DID is associated with a DID document. DID documents are expressed using the data model and can be serialized into a representation. There can be many properties in a DID document out of which some would are required and some aren’t. Broadly, there are three main types of core properties: 

1. DID document properties - here we have information related to the identifiers of the DID subject, DID controllers and other features corresponding to the DID
    
    Among the DID document properties, `id` is the one that is required. This property depicts the identifier of the DID subject.
    
2. Verification method properties - here we have various verification methods which can include the public keys that can be used to authenticate or authorize interactions with DID subject. Note that the verification methods can be used for threshold signature scheme. This method is OPTIONAL. If this property is present, then the value must be a set of verification methods, where each verification method is represented using a map.
    1. Verification Material: This represents a piece of information which is used by a process that applies a verification method. The `type` property is used to determine the compatibility. A cryptographic suite is used for defining the `type` .
    2. Referring to Verification Methods: Verification Methods can be embedded in or referenced with Verification Relationships (which has been discussed next). If the Verification Method is a map, then verification method has been embedded and can be referenced directly. If the Verification Method is a URL string, then the verification method is accessed from another section of the same DID Document or from another DID Document.
3. Verification Relationships: A verification relationship specifies the relationship between the DID subject and a verification method. Different verification relationships enable the associated verification methods to be used for various purposes. This relationship is explicitly mentioned inside a DID Document. If a particular relationship is present in a DID Document, then relationship is either considered invalid or revoked.
    1. Authentication: This relationship depicts how the DID subject is expected to be authenticated. Once authentication is done, it is then up to the DID method if other application to decide what to do with the information. This field is necessary for the verifiers for evaluating if the identity is indeed valid.
    2. Assertion: The `assertionMethod` verification relationship is used to specify how the DID subject is expected to express claims. This property is extremely useful while processing of a VC. During verification, a verifier if a proof is included with the `assertionMethod` property. This proof is the one which is asserted by the user for the corresponding VC.
    3. Key Agreement: The `keyAgreement` verification relationship depicts how an entity can generate encryption material for sending confidential information intended for the DID Subject. For example, an entity can include the public key within this method for depicting the decrypting key for the recipient.
    4. Capability Invocation: The `capabilityInvocation` verification relationship depicts a verification method that might be used by the DID Subject to invoke a cryptographic capability. Example - this property is useful when a DID subject needs to access a protected HTTP API that requires authorization in order to use it. The server providing the HTTP API would be the verifier of the capability.
    5. Capability Delegation: The `capabilityDelegation` relationship is used by the DID Subject to delegate the cryptographic capability to another entity.
4. Service Properties - Services express the ways of communicating with the DID subject or associated entities. A service is some information that a DID subject wants to advertise for further discovery, authentication. Care must be taken that not too much information is revealed in the services. 

### Representations

A concrete serialization of a DID document in this specification is called a representation. A representation is created by serializing the data model through a process called production. A representation is converted back into the data model via a process called consumption. In the W3C specification, the representations for JSON and JSON-LD have been defined. 

The requirements for production and consumption are perhaps obvious and they can be found [here](https://www.w3.org/TR/did-core/#production-and-consumption).

---

---

## Reading Material

1. [https://www.w3.org/TR/did-core/](https://www.w3.org/TR/did-core/)
2. [https://www.w3.org/TR/did-use-cases/](https://www.w3.org/TR/did-use-cases/)
3. [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)
4. [https://www.w3.org/TR/vc-use-cases/](https://www.w3.org/TR/vc-use-cases/)
5. [https://ieeexplore.ieee.org/document/9519473](https://ieeexplore.ieee.org/document/9519473)
6. [https://dl.acm.org/doi/fullHtml/10.1145/3446983.3446992](https://dl.acm.org/doi/fullHtml/10.1145/3446983.3446992)