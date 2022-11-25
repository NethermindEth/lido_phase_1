# W3C’s Decentralized Identifiers data model v1.0

Abstract: https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers (DIDs) are a new type of identifier that enables verifiable, decentralized digital identity. A https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers refers to any subject (e.g., a person, organization, thing, data model, abstract entity, etc.) as determined by the controller of the https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers. In contrast to typical, federated identifiers, https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers have been designed so that they may be decoupled from centralized registries, identity providers, and certificate authorities. Specifically, while other parties might be used to help enable the discovery of information related to a https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers, the design enables the controller of a https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers to prove control over it without requiring permission from any other party. https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers are https://www.w3.org/TR/did-core/#dfn-uri that associate a https://www.w3.org/TR/did-core/#dfn-did-subjects with a https://www.w3.org/TR/did-core/#dfn-did-documents allowing trustable interactions associated with that subject.
Each https://www.w3.org/TR/did-core/#dfn-did-documents can express cryptographic material, https://www.w3.org/TR/did-core/#dfn-verification-method, or https://www.w3.org/TR/did-core/#dfn-service, which provide a set of mechanisms enabling a https://www.w3.org/TR/did-core/#dfn-did-controllers to prove control of the https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers. https://www.w3.org/TR/did-core/#dfn-service enable trusted interactions associated with the https://www.w3.org/TR/did-core/#dfn-did-subjects. A https://www.w3.org/TR/did-core/#dfn-decentralized-identifiers might provide the means to return the https://www.w3.org/TR/did-core/#dfn-did-subjects itself, if the https://www.w3.org/TR/did-core/#dfn-did-subjects is an information resource such as a data model.
Classification: DI
Labels: Standardization efforts
Link to the paper: https://www.w3.org/TR/did-core/
Score: no idea
Score Phase 1: Very relevant
Year: 2019 - 2022 (updated)

## Introduction

In this note we provide an overview of the **World Wide Web Consortium (W3C)’s** specification to express and use **Decentralized Identifiers** (DID’s).

This is of special relevance because many projects we have examined adhere to such specification.

**Note**: W3C’s specification is highly detailed, being over 100 pages. In these notes we only describe some of the most relevant parts we found in it.

## Decentralized Identifiers

**Decentralized Identifiers (DID’s)** are a new type of globally unique identifiers. They are designed to enable entities to generate their own identifiers, and to prove control over them using tools such as digital signatures.

They contrast with traditional identifiers (e.g. national Id, driver license number, URL’s, …) in that these are issued by an external authority or party. As such, their validity and usefulness depends on the external party. For example, such party may make the identifier invalid, or the party may disappear together with all associated identity verification mechanisms.

A DID is a string of characters consisting of the following components:

1. The DID URI scheme identifier.
2. The identifier for the DID method.
3. The DID method-specific identifier.

![                                                   Figure 1: How a DID looks like](W3C%E2%80%99s%20Decentralized%20Identifiers%20data%20model%20v1%200%20857c783035bd4b56bdfe7edef8cf474b/Untitled.png)

                                                   Figure 1: How a DID looks like

### DID Architecture

Figure 2 depicts the overall architecture of a Decentralised Identifier Infrastructure.

![                                         Figure 2: Overview of DID architecture and the relationship of its basic components. Source: [https://www.w3.org/TR/did-core/](https://www.w3.org/TR/did-core/)](W3C%E2%80%99s%20Decentralized%20Identifiers%20data%20model%20v1%200%20857c783035bd4b56bdfe7edef8cf474b/Untitled%201.png)

                                         Figure 2: Overview of DID architecture and the relationship of its basic components. Source: [https://www.w3.org/TR/did-core/](https://www.w3.org/TR/did-core/)

- A **Uniform Resource Identifier (URI)** is a unique sequence of characters that identifies a logical or physical resource used by web technologies.
    
    URL’s are a particular type of URI’s.
    
    DID’s are also URI’s.
    
- A **DID** is a URI composed of the three main parts mentioned above. Each DID resolves to a DID Document.
- The **DID subject** is the entity identified by the DID. 
The DID Subject might be the DID Controller.
- The **DID controller** is an entity that has the ability to make changes to the DID Document. This ability is asserted by the possession of cryptographic keys. 
A DID may have more than one controller.
- **DID Documents** contain information associated with a DIDs. They typically express **verification methods** such as public keys, and information on how to interact with the DID subject.
    
    ![Figure 3: A simple example of a DID document. This document exposes a method by which someone can authenticate itself as the DID did:example:123456789abcdefghi. The authentication consists in proving possession of the private key associated to the public key in `publicKeyMultibase`. Possession is proved using the protocol indicated in the `type` field (typically, this is some kind of digital signature scheme). The field `controller` provides a DID that indicates who is allowed to modify all this data.](W3C%E2%80%99s%20Decentralized%20Identifiers%20data%20model%20v1%200%20857c783035bd4b56bdfe7edef8cf474b/F0EE95F2-E484-4E08-92D7-F32CE112939E.jpeg)
    
    Figure 3: A simple example of a DID document. This document exposes a method by which someone can authenticate itself as the DID did:example:123456789abcdefghi. The authentication consists in proving possession of the private key associated to the public key in `publicKeyMultibase`. Possession is proved using the protocol indicated in the `type` field (typically, this is some kind of digital signature scheme). The field `controller` provides a DID that indicates who is allowed to modify all this data.
    
- DIDs need to be stored on some network in a way that non-authorized parties cannot modify or remove such DIDs. Such network is called **Verifiable Data Registry** and it may be realized by means of blockchain technology.
- A **DID URL** extends the basic syntax of a DID to incorporate other standard URI components such as paths, queries, and fragment in order to locate a particular resource.
- **DID methods** are the mechanism by which a particular type of DID and its associated DID document are created, resolved, updated, and deactivated.
Each DID contains a reference to a DID method.
- **Contexts**: As in VC’s, the context field provides (links to) human readable information about the DID in use.

### DID documents and their authentication methods

DID documents can have a wide variety of properties. Probably the most relevant of them is the  `verificationMethod`.

The data in this property can be used to verify, authenticate, or authorize interactions with the DID subject (or with associated parties). 

**Example 1**: A `verificationMethod` may expose a cryptographic public key. Then the holder of the associated secret key can verify the DID by proving possession of such key.

**Example 2**: Another example may be a verification method that exposes 5 public keys, corresponding to 5 different id’s, from which any three are required to contribute to a cryptographic threshold signature.

Each `verificationMethod` consists of at least the following:

- **Id**: A DID indicating the entity that indicates the subject of the verificaiton method. Typically, this is the DID subject itself. 
More complex scenarios may include: a DID that contains several verification methods, each one with a different id. E.g. if the DID represents the id’s of a whole team, and any threshold number of  members of the team is allowed to verify possession of the DID.
- **Type:** The type of verification method, e.g. the digitial signature scheme being used.
- **Controller:** An entity that has the ability to make changes to the authentication method. The value is a DID.
    
    For example, imagine the case where a DID is controlled by a child, but the DID verification method is controlled by an adult. In this case, the `controller` property in the `verificationMethod` will be the DID of the adult. Such DID can be resolved to the adult’s DID document. The latter contains information on how the adult can authenticate itself. Now, the adult can authenticate itself and modify the verification method of the child.
    

Usually, a public key will also be provided.

![Untitled.png](W3C%E2%80%99s%20Decentralized%20Identifiers%20data%20model%20v1%200%20857c783035bd4b56bdfe7edef8cf474b/Untitled%202.png)

Verification methods can be included inside other fields. For example, the `authentication` field we saw in Figure 3 contains a verification method. This indicates that the verification method inside the authentication field can only be used so as to authenticate oneself as the DID in the `id` field.

Other examples:

- `capabilityInvocation`. This is used to specify a verification method that may be used by the DID subject to invoke a cryptographic capability (e.g. authorization to update the DID document).
- `capabilityDelegation`. Used by the DID Subject to delegate the cryptographic capability to another entity.