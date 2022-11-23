# W3C’s Verifiable Credentials Data Model v1.1

Abstract: https://www.w3.org/TR/vc-data-model/#dfn-credential are a part of our daily lives; driver's licenses are used to assert that we are capable of operating a motor vehicle, university degrees can be used to assert our level of education, and government-issued passports enable us to travel between countries. This specification provides a mechanism to express these sorts of https://www.w3.org/TR/vc-data-model/#dfn-credential on the Web in a way that is cryptographically secure, privacy respecting, and machine-verifiable.
Actions needed and questions: Describe in preliminaries
Added to deliverable?: No
Already read?: Yes
Assigned readers: Albert Garreta
BS factor: important
Classification: VC
Date of publication: 2019 - 2022 (updated)
Labels: Standardization efforts
Link to the paper: https://www.w3.org/TR/vc-data-model/
MZ checked the note: No
Presentation date: November 24, 2022
Reviewers: Isaac Villalobos Gutiérrez
Score Phase 1: Very relevant
Work Group: Blockchain projects

## Introduction

In this note we provide an overview of the **World Wide Web Consortium (W3C)’s** specification to express and use (Verifiable) Credentials on the Web.

This is of special relevance because many projects we have examined adhere to such specification.

## Main definitions

A credential consists of (copied as is):

1. Information related to identifying the subject of the credential (for example, a photo, name, or identification number)
2. Information related to the issuing authority (for example, a city government, national agency, or certification body)
3. Information related to the type of credential this is (for example, a Dutch passport, an American driving license, or a health insurance card)
4. Information related to specific attributes or properties being asserted by the issuing authority about the subject (for example, nationality, the classes of vehicle entitled to drive, or date of birth)
5. Evidence related to how the credential was derived
6. Information related to constraints on the credential (for example, expiration date, or terms of use).

![Figure 1.
Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%20474fc1e0e0e249dea8a96c0d4433c697/Untitled.png)

Figure 1.
Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)

1. **Verifiable Credential:** A Verifiable Credential (VC) can represent all the information that a physical credential represents. By combining it with cryptographic tools, VC’s become more tamper-evident and trustworthy.
2. **Holder**: An entity that possesses one or more VC’s and generating verifiable presentations (VPs) from them.
3. **Issuer**: The body which asserts claims about subjects, creates VC’s for them, and sends the VC to a holder. In our case, issuer will be Lido. 
4. **Subject**: The entity about which a claims are made. In most of the cases, the holder is the subject.
5. **Verifier**: The entity that receives one or more VC’s for processing.
6. **Verifiable Data Registry**: A system that mediates the creation and verification of identifiers, keys, and other relevant data, such as verifiable credential schemas, revocation registries, issuer public keys, and so on, which might be required to use verifiable credentials.

## Core Data Model

### Claims

A claim is a statement made about a subject. A subject is a body about which a claim can be made. An example of a claim is shown below which states that Pat is the alumni of the Example University:

Multiple claims about a user can be combined to form a graph of information:

![Untitled](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%20474fc1e0e0e249dea8a96c0d4433c697/Untitled%201.png)

![Figure 2. 
Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%20474fc1e0e0e249dea8a96c0d4433c697/Untitled%202.png)

Figure 2. 
Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)

### Credentials

A **credential** is a set of one or more claims made by the same entity. It can also contain metadata such as:

- A credential identifier.
- Description of the issuer.
- Expiry date.
- Public key to be used for verification purposes.
- Etc.

A **verifiable credential** is a credential with (cryptographic) proofs that the issuer indeed issued the credential and its claims.

See Figures 3 and 4, and their captions, for  graphical depictions of the different components that constitute a VC.

![
Figure 3: A basic depiction of the components of a VC. Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%20474fc1e0e0e249dea8a96c0d4433c697/Untitled%203.png)

Figure 3: A basic depiction of the components of a VC. Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)

![Figure 4: Detailed depiction of the components and information flow within a VC. The upper graph contains the claims and the corresponding metadata which forms the credential itself. The lower graph contains the cryptographic keys and signature which form the digital proof of the verifiable credential. 
Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%20474fc1e0e0e249dea8a96c0d4433c697/Untitled%204.png)

Figure 4: Detailed depiction of the components and information flow within a VC. The upper graph contains the claims and the corresponding metadata which forms the credential itself. The lower graph contains the cryptographic keys and signature which form the digital proof of the verifiable credential. 
Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)

In Figure 4, the **upper graph** depicts a Credential. In this example the credential’s metadata is:

- The type: AlumniCredential.
- The issuance date.
- An Id of the issuer.
- The Subject of the credential (Pat).

Furthermore, the credential contains a claim, namely that the credential’s subject, Pat, is an alumni of the university who issued the credential.

The **lower graph** contains a proof that the credential Issuer indeed issued the credential. In this example the proof consists of:

- A proof identifier: “Signature 456”.
- A proof type: RsaSignature2018.
- A date of creation.
- A signature.
- A nonce.

**Note**: As hinted previously, W3C’s specification also contemplates a scenario in which credentials are not verifiable. In this note we omit discussing such functionality.

### Presentations

**Verifiable Presentations** (VPs) allow a user to portray only the subset of data in its VC’s which is required for a particular situation. 

A verifiable presentation expresses data from one or more verifiable credentials, and is packaged in such a way that the authorship of the data is verifiable. More precisely, it is possible to verify the cre 

The data inside a verifiable presentation is often about the same subject but might have been issued by multiple issuers. 

**Note:** As with credentials, W3C’s also specifies presentations which are not verifiable. In this note we will only deal with *verifiable* presentations though.

![Figure 5. A basic depiction of the components of a VP. 
Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%20474fc1e0e0e249dea8a96c0d4433c697/Untitled%205.png)

Figure 5. A basic depiction of the components of a VP. 
Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)

As depicted in Figure 5, a VP is composed of one or more VC’s together with some metadata around the VP. Some of this metadata can be…

![Figure 6.
Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%20474fc1e0e0e249dea8a96c0d4433c697/Untitled%206.png)

Figure 6.
Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)

The figure above depicts a more complete picture of a verifiable presentation. A verifiable presentation consists of four main graphs. The first one is the presentation graph which contains the verifiable presentation property. Each verifiable presentation property points to a verifiable credential graph. Second graph is the verifiable credential graph; the third is the proof for the verifiable credential. The fourth graph is the proof for the presentation. (Proof implies digital signatures).

## Basic Concepts

1. Contexts: Verifiable Credentials and Verifiable Presentations have many entities which are defined by URIs. The URIs can be long and tough to read. The `@context` property is meant for mapping the short human-readable form to long machine-readable URIs. According to the w3c specifications, the value of the `@context` property must be an ordered set where the first item is URI with the value `https://www.w3.org/2018/credentials/v1` .
2. Identifiers: The `id` property is the identifier of an entity. The `id` property is intended to unambiguously refer to an object. Using the `id` property allows for the expression of statements about specific things in a verifiable credential. According to the w3c specification, `id` property must be a single URI. Once the `id` is dereferenced, it leads to machine-readable document. It should be noted that the `id` property can contain a DID to reference to particular entity. DIDs and VCs are independent of each other. However, the combination of the two is really powerful.
3. Types: The `type` property specifies the type of information present in the document. Verifiable credentials and verifiable presentations must have a `type` property. All credentials, presentations, and encapsulated objects must specify or be associated with more narrow `types` . An encapsulating object convey the associated object `types` so that verifiers can quickly determine the contents of an associated object based on the encapsulating object `type` . This helps the verifiers during the verification stage because they know what data to expect. The expectation of `types` and their associated properties should be documented somewhere.
4. Credential Subject: A VC contains claims about one or more subjects. `credentialSubject` property is used for defining claims about one or more subjects. That is the `credentialSubject` contains one or more properties which are related to a subject of the verifiable credential. A VC must have the property `credentialSubject`. 
5. Issuer: This depicts the issuer of a VC. The value of the `issuer` property is a URI or a object containing the `id` property.
6. Issuance Date: This property depicts when the credential becomes valid. It is a necessary property.
7. Proofs (Signatures): At least one proof mechanism, and the details to evaluate that proof must be present inside a VC or VP. Two classes of proofs: (i) external proofs: wraps an expression of this data model; (ii) embedded proof: proof is included in the data.
8. Expiration: It depicts when the credential expires.
9. Status: It depicts the current status of the credential such as: active, suspended or revoked. This contains: (i) `id` which is a URI; and (ii) `type` which contains information to determine the current status of the credential.
10. Presentations: Presentations may be used to combine and present credentials. They can be packaged in such a way that the authorship of the data is verifiable.
    1. Presentations using derived credentials: Zero-knowledge cryptography schemes might enable holders to indirectly prove they hold claims from a verifiable credential without revealing the verifiable credential itself. 

## Advanced Concepts

1. Lifecycle Details: This depicts the steps that are involved in the verifiable credential ecosystem.
    1. Issuer issues a VC to a holder.
    2. Holder might transfer it VC to another holder.
    3. Holder presents VC to a verifier.
    4. Verifier checks the authenticity of of VP and VCs.
    5. An issuer might revoke a VC.
    6. A holder might delete a VC.
2. Trust Model
    1. Verifier trusts the issuer to issue the credential it received.
    2. All entities trust the verifiable data registry to be tamper-evident.
    3. Holder and verifier trust the issuer to issue true credentials about the subject.
    4. Holder trusts the repository to store the credentials securely. 
3. Extensibility: The idea is to enable permissionless innovation. To achieve this, the data model needs extensibility in various ways. This property is about extending the credential with more information. The challenge with extensibility is achieving the appropriate balance between extensibility and program correctness.
4. Data Schemas: Data Schemas are useful when we want to enforce a specific structure to the data being stored in the system. The W3C specification considers at least two types of schemas:
    1. Data verification schemas: Used to verify if the structure and contents of a VC conform to a particular schema
    2. Data encoding schemas: Used to map the contents of a VC to another representation format
    
    It should be noted that data schemas play a completely different role from the `@context` property. The value of the `credentialSchema` property must be one or more data schemas which is used by the verifiers to determine if the provided data conforms to the provided schema.
    
5. Refreshing: Systems need to enable manual or automatic refresh of an expired VC. This service is only expected to be used when the credentials has expired or if the issuer does not publish credential status information. Issuers should not include the `refreshService` if the VC contains some information which is not public or whose refresh service is not protected in some way.
6. Terms of Use: Terms of use depict the terms under which a VC or VP was issued. The issuer puts their terms of use inside the VC and the holder places their terms of use inside a VP. The `termsOfUse` property tells the verifier about what tasks it has to perform, it is not allowed to perform, or it is allowed to perform. If the recipient is not willing to adhere to the specified terms of use, then they do it on their own accord and might incur legal liability if they violate the stated terms of use.
7. Evidence: The `evidence` property depicts the additional information which can be included by the issuer within a VC to express the credibility of the information in the VC. The `evidence` property provides different and complementary information to the `proof` property. The `evidence` property is used to express supporting information related to the integrity of the VC. The `proof` property is used to express cryptographic proofs related to the authenticity of the issuer and the integrity of the VC.
8. Zero-Knowledge Proofs: A zero-knowledge proof (ZKP) is a cryptographic method where a prover can prove to a verifier that they are the owner of `x` without actually disclosing `x`. For ZKP to work, a few key capabilities have to be provided to the holder:
    1. Combine multiple VCs from different issuers to make a VP without revealing VCs to the verifiers. This makes it more difficult for the verifier to collude with issuers to gain information about VCs.
    2. Selectively disclose relevant information in a VC to verifier instead of having multiple VCs.
    3. Generate a derived VC according to the schema without involving the issuer in this step.
    
    There are two requirements for VCs when they are to be used in ZKP systems:
    
    1. VC must contain the `proof` property so that the holder can reveal only required information.
    2. If a credential definition is used, then the credential must include `credentialSchema` property where the definition is provided.
9. Disputes: Two cases have been mentioned in the specification where an entity may want to dispute a credential issued by an issuer:
    1. A subject disputes a claim made by the issuer.
    2. An entity disputes a possible false claim made by the issuer about a subject.
10. Authorization: VCs are meant for identifying subjects reliably. However, as of yet, authorization isn’t an appropriate use case of this specification without an authorization framework deployed along with it.

## Syntaxes

The specification provided on the website uses only JSON and JSON-LD. However, systems can also use XML, YAML, or other types which can express data.

1. JSON - It is like the generic JSON objects that we have used.
2. JSON-LD - It is an upgraded version of JSON and it supports Linked Data.

## Privacy Considerations

1. Spectrum of Privacy: It should be noted that data presented belong to spectrum of privacy ranging from pseudonymous to strongly identified. Different types of data are needed for different use cases and therefore, privacy solutions are specific to use cases. 
    
    ![Untitled](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%20474fc1e0e0e249dea8a96c0d4433c697/Untitled%207.png)
    
    The VC Data Model aims to support the full privacy spectrum.
    
2. Personally Identified Information: Data stored in the `credential.credentialSubject` field is susceptible to privacy violations when shared with verifiers. Personally Identifiable Information (PII) can be used to figure out the actual identity of an entity. Implementers should try to warn the holders from sharing data that reveal more information about a user. Since VCs will most likely contain PIIs, implementers should ensure safeguarding the data while it is being transferred and where it is stored.
3. Identifier-Based Correlation: Subjects are identified by the `credential.credentialSubject.id` field. The identifiers used to identify a subject can lead to greater risks via correlation. This can happen when the identifiers are long-lived or when the identifiers are from more than one web sources. Similarly, verifiers or an issuer and a verifier can collude to correlate the holder using the `credential.id` property of the VC. To prevent this, a holder should use VC schemes that allow hiding the `credential.id` field in the VP. If the system requires strong anti-correlation properties, then the identifiers should be either of these:
    1. Bound to a single origin
    2. Single-use
    3. Not used at all, but instead replaced by short-lived, single-use bearer tokens.
4. Signature-Based Correlation: Just like the `credential.id` , the `credential.proof` can be used by malicious verifiers for correlating the user. If strong anti-correlation property is needed, it is advised that signature and metadata are generated using technologies like third-party pairwise signatures, zero-knowledge proofs, or group signatures.
5. Long-Lived Identifier-Based Correlation: VCs might contain long-lived identifiers such as email addresses, government-issued identifiers, and these identifiers can be used to correlate individuals. Organizations should warn users about such fields.
6. Device Fingerprinting: These mechanisms are external to VCs that can be used to track and correlate individuals on the Web. These include internet IP addresses, in-application GPS APIs, etc. It should be noted that the usage of VCs does not prevent the usage of tracking technologies mentioned above. Therefore, care must be taken while using such information along with VCs because the conjunction of these two can reveal a lot of sensitive information.
7. Favor Abstract Claims: To enable users use resources without revealing more PII than needed, issuers should limit the information inside a VC. One way to do it is via using an abstract property that provides the relevant information to the verifier without actually revealing the PII.
8. The Principle of Data Minimization: Privacy violations occur when data revealed in one context is leaked into another. To prevent this, the amount of information requested and information received should be kept to the minimum. For issuers, the best practice would be to atomize the information in a VC or use a signature scheme that allows selective disclosure. For verifiers, they should request the information which is necessary.
9. Bearer Credential: A bearer credential is a privacy-enhancing piece of information, such as a concert ticket, which entitles the holder to a certain resource without revealing any information about the holder. This credential is used where sharing or transferring of the bearer credential is not dangerous. Bearer credential are made possible by not specifying the `id` property within the VC. The implementers must ensure that bearer credentials do not reveal more information than necessary.
10. Validity Checks: When processing VCs, verifiers are expected to perform many validity checks as well as business specific checks. The process of performing these checks might lead to information leakage which in turn may violate the holder.
11. Storage Providers and Data Mining: After receiving the VC from the issuer, a holder needs to store it somewhere. The holder should know that a VC contains information which is unique to them and can be used by organizations for data mining. Thus, the VCs must be stored in a privacy-preserving manner.
12. Aggregation of Credentials: Aggregating two separate credentials reveals more information about the holder than the two individual credentials. A possible solution maybe via the usage of ZKPs. In addition, policies maybe defined by the holder for their credentials. However, dealing with this challenge is still quite intricate.
13. Usage Patterns: Usage of VCs can potentially lead to de-anonymization and a loss of privacy during the following scenarios:
    1. Same VC is presented to the same verifier and hence, the verifier can infer that it is the same individual.
    2. Same VC is presented to different verifiers and they collude to figure out that it is the same individual.
    3. The `id` of the subject refers to the same individual.
    4. Underlying information in a VC can be used to identify the individual across services.
    
    This phenomena of de-anonymization and loss of privacy can be prevented by:
    
    1. Not re-using the `id` of the subject.
    2. If the credential supports revocation, then a globally-distributed service for revocation must be deployed.
    3. Designing revocations that do not depend on ID
    4. Avoiding PII with any long-lived `id`
    
    However, it should be also kept in mind that correlation might be important in some services where we may need to control the usage of some resource.
    
14. Sharing information with the wrong party: A holder shares their information with the verifier to access some service. It might be possible that the verifier is malicious and may ask information to tarnish the holder’s reputation. To prevent this, the idea is that an issuer atomizes the information inside a VC. This mitigates the damage that can occur.
15. Frequency of Claim Issuance: Usage patterns can be correlated into certain types of behavior. This can be mitigated by the holder by generating the VCs without the knowledge of the issuer. However, this solution can be nullified by the issuers by issuing credentials with short lifespans. Therefore, the system designers should ensure that very short-lived credentials aren’t issued.
16. Prefer Single-Use Credentials: Using single-use credentials has many benefits. First, the verifier knows that the information isn’t outdated. Secondly, it’s better for the holders because there are n long-lived identifiers. Thirdly, there is nothing for attackers to steal.
17. Private Browsing: In ideal private browsing scenario, no PII will be revealed. This feature might not available everywhere and hence, the implementers must verify if this feature should be included.
18. Issuer Cooperation Impacts on Privacy: VCs rely on the fact that issuers are trusted to a great extent. To enhance privacy of the system, an issuer should support privacy-preserving techniques which can be availed by the holders.

## Security Considerations

There are multiple security consideration which issuers, holders and verifiers must consider.

1. Cryptography Suites and Libraries: Cryptography suites and libraries are used to create and process VCs and VPs. Care must be taken while designing the cryptographic tools used in the identity system.
2. Content Integrity Protection: VCs contain links which are outside the VC. The links which exist outside the VC are not tamper-proof. The designers should enforce the usage of links which support integrity such as Hashlink and IPFS.
3. Unsigned Claims: Credentials can contain information which do not contain any proofs. Such information is useful for intermediate storage or self-asserted information.
4. Token Binding: A verifier might need to ensure that they are intended recipient and not a man-in-the-middle. Token binding ties the request for a VP to a response can help to secure the protocol.
5. Bundling Dependent Claims: Atomization of information is desired within VCs. If not done securely, a holder might bundle the credentials in a way that it was not intended by the issuer.
6. Highly Dynamic Information: In case of highly dynamic information, expiration time must be set securely.
7. Device Theft and Impersonation: If the device containing the VCs is stolen, then the attacker may get access to VCs. To mitigate this type of attack, the holder may use passwords or pins in various components of VCs.

## Accessibility Considerations

The implementers should consider various parameters while designing accessibility considerations for the credentials. While designing the system, the data model designers should have the data-first approach so that the information is portrayed correctly by the various components of the credentials.

# Scratch

### Privacy

The specification discusses several ways in which privacy around a Verifiable Credential could be breached. Some examples are (cf. Section 7):

- Signature-Based Correlation (cf. Section 7.4)
- VC’s might contain long-lived identifiers that may be used to correlate different individuals. These could be, for example, e-mails, government-issued identifiers, addresses, healthcare vitals, etc. (cf. Section 7.5)
- Tracking technologies when moving VC’s around (cf Section 7.6).

The specification provides some vague recommendations as to how to avoid such breaches.

In any case, the spec only provides a list of possible concerns and corresponding solutions, but “does not take philosophical positions on the correct level of anonymity for any specific transaction”.