# A Survey on Blockchain-based Identity Management and Decentralized Privacy for Personal Data

Abstract: In the digital revolution, even secure
communication between individuals, services and devices
through centralized digital entities presents considerable risks.
Service providers collect and store information that is used
for data mining, profiling and exploitation without users'
knowledge or consent. Having service providers continue to
offer their centric solutions is inefficient in terms of
duplication, has serious security lacunae and is cumbersome
to the users. The Self-sovereign Identity (SSI) concept, which
includes the individual's consolidated digital identity and
verified attributes, enables the users of data to exert their
ownership and gain insights from their data’s usage. The
authentication and verification of digital identity is essential
to achieve the privacy and security of distributed digital
identities. However, the current literature still lacks the
comprehensive study on components of identity management
as well as user privacy and data protection mechanisms in
identity management architecture. In this paper, we provide a
coherent view of the central concepts of SSI, including the
components of identity proofing and authentication solutions
for different SSI solutions. Firstly, we discussed an overview
of Identity management approaches, introducing an
architecture overview as well as the relevant actors in such a
system and blockchain technology as solution for distributed
user-centric identity. Then we analyzed the authentication
and verification mechanisms in the context of digital identity.
Finally, we discuss the existing solutions and point out the
research gaps and elaborate challenges and trade-offs towards
building a complete identity management system (IdMs).
Actions needed and questions: @Jorge Arce-Garro isn’t that uber-relevant? 
Added to deliverable?: No
Already read?: No
Assigned readers: Jorge Arce-Garro
BS factor: derivative
Classification: DI, Data to Web3, VC
Date of publication: 2020
Link to the paper: https://hal.archives-ouvertes.fr/hal-02650705/document
MZ checked the note: No
Score Phase 1: Maybe relevant

(Caveat:  this paper has grammar issues throughout that complicate its reading)

# Introduction

Mention of problems behind the current state of affairs regarding data: centralized entities handling users’ data makes the user have no control over it. Self-sovereign identities are a way to combat this.

Technological challenges behind implementing SSIs:

- Blockchain for identity management
- Authentication and user data privacy
- Analysis of existing solutions based on SSI architecture.

# Identity management approach with blockchain

Four phases: enrollment, authentication, issuance, verification.

Three types of identity management systems:

- Centralized identity: same entity enrolls and validates.
- Federated identity:  a single enrollment process, can use the same identity to access a number of services from different entities.
- Self-sovereign identity: allows for the ownership of data. User need not reveal all of his information.

Using blockchain technology solves many technical issues related to SSIs. A few basic blockchain definitions are given. References to projects like [TrustChain](https://devos50.github.io/assets/pdf/1-s2.0-S0167739X17318988-main.pdf) and [Iota/The Tangle](http://www.descryptions.com/Iota.pdf) are given.

# Blockchain for identity and data management (authentication)

### User data privacy.

How do we guarantee that sensitive information will not be leaked? Approaches like k-anonimity and minimization of data disclosure are discussed. Perturbing data and encryption are seen as inefficient for large-scale applications.

With regards to blockchain:

> The existing blockchain based solutions have either utilized the permissioned blockchain access to ensure privacy or authentication is bind to decentralized identifier (DID) and sensitive information is stored on user’s device.
> 

The process of distinguishing between identities is discussed.

> The subject presents the identity evidence to registration authority that inspect the identifiable information by identification information and provided identity information. The identity proofing often relies on various attributes (PII) ID, driving license, financial or telecommunication account, address etc.
>