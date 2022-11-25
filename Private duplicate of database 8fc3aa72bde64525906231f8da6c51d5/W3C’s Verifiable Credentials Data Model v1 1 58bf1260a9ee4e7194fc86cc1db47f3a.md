# W3C’s Verifiable Credentials Data Model v1.1

Abstract: https://www.w3.org/TR/vc-data-model/#dfn-credential are a part of our daily lives; driver's licenses are used to assert that we are capable of operating a motor vehicle, university degrees can be used to assert our level of education, and government-issued passports enable us to travel between countries. This specification provides a mechanism to express these sorts of https://www.w3.org/TR/vc-data-model/#dfn-credential on the Web in a way that is cryptographically secure, privacy respecting, and machine-verifiable.
Classification: VC
Labels: Standardization efforts
Link to the paper: https://www.w3.org/TR/vc-data-model/
Score: no idea
Score Phase 1: Very relevant
Year: 2019 - 2022 (updated)

## Introduction

In this note we provide an overview of the **World Wide Web Consortium (W3C)’s** specification to express and use (Verifiable) Credentials on the Web.

This is of special relevance because many projects we have examined adhere to such specification.

**Note**: W3C’s specification is quite detailed, being over 150 pages. Here we only describe some of the most relevant parts we found in it.

## Core Data Model

### Claims

A **claim** is a statement made about a **subject**. Formally it is a triple of the form (subject, property, value).
For example, the claim below states that Pat is the alumni of the well-known Example University:

![Figure 2. A claim. Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%2058bf1260a9ee4e7194fc86cc1db47f3a/Untitled.png)

Figure 2. A claim. Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)

Claims can be combined to form a graph of information:

![Figure 3: Three claims combined together to form a graph of information. Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%2058bf1260a9ee4e7194fc86cc1db47f3a/Untitled%201.png)

Figure 3: Three claims combined together to form a graph of information. Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)

### Credentials

A **credential** is a set of one or more claims made by one entity (the **Issuer**). It can also contain metadata such as:

- A credential identifier.
- Description of the issuer.
- Expiry date.
- Etc.

A **Verifiable Credential (VC)** is a credential with (cryptographic) proofs that the Issuer indeed issued the credential and agrees with its claims.

Typically, a proof is a signature of the Issuer on the whole claim.

See Figures 4 and 5, and the captions, for graphical depictions of the different components of a VC.

![
Figure 4: A basic depiction of the components of a VC. Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%2058bf1260a9ee4e7194fc86cc1db47f3a/Untitled%202.png)

Figure 4: A basic depiction of the components of a VC. Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)

![Figure 5: Detailed depiction of the components and information flow within a VC. The upper graph contains the claims and the corresponding metadata which forms the credential itself. The lower graph contains the cryptographic keys and signature which form the digital proof of the VC, together with some metadata. 
Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%2058bf1260a9ee4e7194fc86cc1db47f3a/Untitled%203.png)

Figure 5: Detailed depiction of the components and information flow within a VC. The upper graph contains the claims and the corresponding metadata which forms the credential itself. The lower graph contains the cryptographic keys and signature which form the digital proof of the VC, together with some metadata. 
Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)

In Figure 5, the **upper graph** depicts a W3C credential. In this example the credential’s metadata consists of:

- The type: AlumniCredential.
- The issuance date.
- An Id of the issuer.
- The Subject of the credential (Pat).

Furthermore, the credential contains a claim, namely that the credential’s subject, Pat, is an alumni of the university who issued the credential.

The **lower graph** contains a proof that the credential Issuer indeed issued the credential. In this example the proof consists of:

- A proof identifier: “Signature 456”.
- A proof type: RsaSignature2018. This specifies that the proof is an RSA signature on the entire credential.
- A date of creation.
- A signature.
- A nonce.

**Note**: As hinted previously, W3C’s specification also contemplates a scenario in which credentials are not verifiable. In this note we omit discussing such functionality.

The following image depicts 

![Untitled 3.png](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%2058bf1260a9ee4e7194fc86cc1db47f3a/Untitled_3.png)

![Figure 6: A VC written following JSON-LD syntax. Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%2058bf1260a9ee4e7194fc86cc1db47f3a/Untitled_4.png)

Figure 6: A VC written following JSON-LD syntax. Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)

### How would such a VC be verified? A toy example

The Holder (Pat in our case) can use the above example VC to prove to a verifier that he is an alumni of Example University, without revealing its name.

To do so, it reveals all the VC except the part of the VC where his name (Pat) appears.

Then it proves in zero knowledge that it knows a value for the “name field” such that, if added to the VC, then the `Signature 456` is valid (with respect to the public key of `Example University` ).

**Note**: W3C also contemplates the case in which there is no aim at preserving privacy. In that case the verifier can just check that the Issuer’s signature is valid.

### Presentations

**Verifiable Presentations** (VP’s) allow a user to package several VC’s together.

Additionally, the authorship of the VP is also verifiable. More precisely, a VP is signed by the entity that formed it, similarly to how the Issuer signs a VC.

The data inside a VP is often about the same subject. However, it may have been issued by multiple issuers.

For example, a VP may contain all education credentials of a subject, with each credential being issued by a different entity.

![Figure 7. A basic depiction of the components of a VP. 
Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%2058bf1260a9ee4e7194fc86cc1db47f3a/Untitled%204.png)

Figure 7. A basic depiction of the components of a VP. 
Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)

As depicted in Figure 5, a VP is composed of one or more VC’s together with some metadata around the VP. This metadata can be, e.g., the **type** of the VP, the **terms of use**, etc.

![Figure 8. Detailed depiction of an example Verifiable Presentation. Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%2058bf1260a9ee4e7194fc86cc1db47f3a/Untitled%205.png)

Figure 8. Detailed depiction of an example Verifiable Presentation. Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)

In Figure 8 we have an extension of the example in Figure 5. In this example, Pat’s alumni credential has been packaged into a Verifiable Presentation. An entity called “Example Presenter”  has signed the whole VP.

## Basic Concepts

Here we provide an overview of the most basic field types that appear in VC’s and VP’s.

- **Identifiers**: The `id` property is the identifier of an entity. It must be a single URI. In W3C’s examples, URI’s are either URL’s or Decentralized Identifiers (DID’s).
- **Types**:
    - The `type` property specifies the type of information present in the document. VC’s and VP’s must have a `type` property.
    - All credentials, presentations, and encapsulated objects must specify or be associated with more narrow `types`.
    - `types` are essential as they allow verifiers to quickly determine the contents of an associated object based on the encapsulating object `type`. This helps the verifiers during the verification stage because they know what data to expect.
    - The expectation of `types` and their associated properties should be documented somewhere.
- **Issuer**: The `id` of the issuer of a VC.
- **Issuance Date**: This property indicates when the credential becomes valid.
- **Expiration**: This property indicates when the credential expires.
- **Credential Subject**: The subject the credential refers to. This field consists of several objects —including claims— that are related to the subject. Our first JSON-type example of a VC already contains the `credentialSubject` property. Below we provide yet another example.
    
    ![Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%2058bf1260a9ee4e7194fc86cc1db47f3a/Untitled_2.png)
    
    Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)
    
- **Proofs**: At least one proof mechanism, and the details to evaluate that proof must be present inside a VC or VP.
- **Status**: It depicts the current status of the credential such as: **active, suspended or revoked**. This contains: (i) `id`; and (ii) `type` which contains information for determining the current status of the credential.
- **Contexts**: This property is used only to aid humans to understand the contents of a VC or a VP.

## Advanced Concepts

- **Lifecycle Details**: The roles and information flows in the VC ecosystem are as follows.
    1. The Issuer issues a VC to a holder.
    2. A Holder might transfer its VC to another Holder.
    3. A Holder presents one or more VC’s or VP’s to a Verifier.
    4. The Verifier checks the authenticity of of VP and VCs.
    5. An issuer might revoke a VC.
    6. A holder might delete a VC.
    
    ![Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%2058bf1260a9ee4e7194fc86cc1db47f3a/Untitled%206.png)
    
    Source: W3C’s VC specification [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)
    
- **Trust Model:** The trust model of the spec is as follows.
    1. The Verifier trusts the Issuer to have issued the credential it received.
    2. All entities trust the verifiable data registry to be tamper-evident.
    3. The Holder and the Verifier trust the Issuer to issue true credentials about the subject.
    4. The Holder trusts the repository to store the credentials securely. 
- **Data Schemas**: Data Schemas are useful when we want to enforce a specific structure to the data being stored in the system. The W3C specification considers at least two types of schemas:
    - Data verification schemas: Used to verify if the structure and contents of a VC conform to a particular schema
    - Data encoding schemas: Used to map the contents of a VC to another representation format
- **Terms of Use**: Terms of use depict the terms under which a VC or VP was issued. The Issuer puts their terms of use inside the VC and the Holder places their terms of use inside a VP. The `termsOfUse` property tells the Verifier about what tasks it has to perform, it is not allowed to perform, or it is allowed to perform. If the recipient is not willing to adhere to the specified terms of use, then they do it on their own accord and might incur legal liability if they violate the stated terms of use.
- **Evidence**: The `evidence` property depicts the additional information which can be included by the Issuer within a VC to express the credibility of the information in the VC. The `evidence` property provides different and complementary information to the `proof` property, and is not expected to be cryptographically verifiable. For example, to provide evidence for a claim about being alumni of Example University, the VC may point to the University’s official alumni list (a website).
- **Other advanced concepts**: The specification describes other advanced concepts such as:
    - **Extensibility**: The specification should be easily extendable (i.e. it should be easy to add new features on top of it, without modifying the current spec).
    - **Disputes**: Support for issuing VC’s that dispute other VC’s.
    - **Refreshing**: A VC may contain information on how to “refresh” the credential in case it expires.
    - Etc.

## Syntaxes

The specification provided on the website uses only JSON and JSON-LD (an upgraded version of JSON which supports Linked Data). However, systems can also use XML, YAML, or other types which can express data.

## Privacy Considerations

- **Spectrum of Privacy**: W3C’s specification aims to accommodate the whole “spectrum” of privacy needs. W3C does not recommend nor discourage any specific level or type of privacy.
- **Correlation of Personally Identifiable Information (PII)**: Data stored in the `credential.credentialSubject` field is susceptible to privacy violations when shared with verifiers. For example: VC’s might contain long-lived identifiers such as email addresses, government-issued identifiers, etc.  Different Verifiers may collude so as to put together this information and thus correlate individuals.
Organizations should warn users about such fields.
- **Favor Abstract Claims**: To enable users use resources without revealing more Personally Identifiable Information (PII) than needed, issuers should limit the information inside a VC. One way to do this is via using an abstract property that provides the relevant information to the verifier without actually revealing the PII.
    
    For example, if a VC is to be used to prove being over 18 years old, the Issuer may create a Claim attesting to this fact, instead of creating a claim that attests to the actual age of the Holder.
    
- **The Principle of Data Minimization**: Privacy violations occur when data revealed in one context is leaked into another. To prevent this, the amount of information requested and information received should be kept to the minimum. For issuers, the best practice would be to atomize the information in a VC. Verifiers should only request strictly necessary information.
- **Storage Providers and Data Mining**: After receiving the VC from the Issuer, the Holder needs to store it somewhere. The Holder should know that a VC contains information which is unique to them and can be used by organizations for data mining. Thus, the VC’s must be stored in a privacy-preserving manner.
- **Aggregation of Credentials**: Aggregating two separate credentials reveals more information about the holder than the two individual credentials. A possible solution may be the usage of ZKPs.
- **Other considerations about privacy**:
    - **Usage Patterns**: The way VC’s are used may leak information about the Holder.
    - **Prefer Single-Use Credentials**: Using single-use credentials has many benefits. First, the verifier knows that the information is not outdated. Secondly, it is better for the holders because there are no long-lived identifiers. Thirdly, there is nothing for attackers to steal.
    - **Sharing information with the wrong part**.
    - **Issuer Cooperation Impacts on Privacy**.
    - **Bearer Credential**: These are credentials that do not specifying the `id` property within the VC.