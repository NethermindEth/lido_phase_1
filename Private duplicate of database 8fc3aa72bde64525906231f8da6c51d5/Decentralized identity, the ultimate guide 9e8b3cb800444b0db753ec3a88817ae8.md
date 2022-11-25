# Decentralized identity, the ultimate guide

Abstract: This is a guide that explains what decentralised identity is, how it works and its benefits. It is written by the team of Dock, a company that has been building Verifiable Credentials and Decentralised Identity since 2017.
Classification: DI
Labels: Decentralized identity, Good reference source, Self-sovereign identity
Link to the paper: https://blog.dock.io/decentralized-identity/
Score: no idea
Score Phase 1: Very relevant

# Definitions related to Decentralised Identity

(discussed in the Decentralized Identity: The Ultimate Guide 2022  [https://blog.dock.io/decentralized-identity/](https://blog.dock.io/decentralized-identity/) .)

### Self-Sovereign Identity  (SSI)

*Self-Sovereign Identity*  (SSI) is used interchangeably with the term *Decentralised Identity*.

SSI consists of the following three parts :

 

- Blockchain.
- Verifiable Credentials: a cryptographically secure, digital version of credentials (paper or digital) that users can present to possible verifiers. This digital version should comply with ****[Verifiable Credentials Data Model v1.1](https://www.w3.org/TR/vc-data-model/).**
- Decentralized Identifiers (DIDs): an identifier that is cryptographically verifiable and is created and managed by the user.
- Decentralized Identity Wallet: an application that allows users to create their DIDs and store their verifiable credentials.

### **Centralized Identity Management**

Every user creates a username and a password for each service.

**Disadvantage:**  Single point of failure for data breaches. Some examples of such incidents are described in this paper: ``[Digital Identities and Verifiable Credentials](https://link.springer.com/article/10.1007/s12599-021-00722-y)''. 

### **Federated Identity Management**

Users can access multiple applications by using a single set of credentials. An example is when the user signs in to multiple applications using its Google or Facebook account.

**Disadvantage:**  There is no [*unlinkability](https://github.com/decentralized-identity/snark-credentials/blob/master/whitepaper.pdf) :* if multiple applications collude could possibly detect if the same user has registered to all of them using the same account. 

### Decentralized Identity

Users store the data in their digital wallets and they have the option to choose when and which part of this data they want to reveal. 

### Standards For Decentralised Identity

- [World Wide Web Consortium (W3C)](https://decentralized-id.com/web-standards/w3c/)
- [Internet Engineering Task Force (IETF)](https://www.ietf.org/)
- [Decentralized Identity Foundation (DIF)](https://identity.foundation/)

### Decentralized Identity on the Blockchain

There is an issuer, a holder, and a verifier. 

- Both the issuer and the holder hold a DID that is possibly stored on the blockchain and it may be associated with a public key (this depends on the generation method). Some examples of DID methods can be found also here **[EBSI DID Method](https://ec.europa.eu/digital-building-blocks/wikis/display/EBSIDOC/EBSI+DID+Method).**
- The issuer signs a claim for the holder (e.g the issuer is a university and signs a degree) using its private key. This will constitute a verifiable credential.
- The holder holds this credential in a *digital wallet* and presents it to the verifier.
- The verifier checks which DID and public key corresponds to the issuer and verifies the signature.

**What can be stored on the blockchain:**

- All the DIDs
- Public Keys
- Proof of credentials (in case the issuer wants to timestamp a credential)
- Revocation Registry (in case the issuer wants to have the option to retrieve the certificates that it has issued).

### DIDs in Dock

**Example** : did:dock:GhkJkjhertFlkiid

- Globally unique identifiers that are associated with one or multiple private/public key pairs.
- They do not contain any private information
- The owner can cryptographically prove that it owns this DID.
- They can enable secure and private communication between two parties.
- Each person can create multiple DIDs for different purposes. Note: many applications (e.g [Decentralised Identity in Tezos](https://sprucesystems.medium.com/decentralized-identity-with-the-tezos-did-method-d9cf6676dd64)) consider this as an advantage and they do not seem to take into account the [Sybil problem](https://en.wikipedia.org/wiki/Sybil_attack) at this point, because it offers [pairwise privacy](https://eprint.iacr.org/2020/934.pdf) (there is no correlation of identities among several web pages or services).

## Layers in the decentralized Identity Ecosystem

Layer 1 **Standards**: They ensure interoperability, standardization, portability

Layer 2 **Infrastructure**: Interaction between applications and with the verifiable data registries (e.g blockchain).

Layer 3 **Identifiers and VC**:   authentication of DIDs and the presentation of the credentials. 

Layer 4 **apps, wallets, products**: Use cases

## References

- Decentralized Identity: The Ultimate Guide 2022   [https://blog.dock.io/decentralized-identity/](https://blog.dock.io/decentralized-identity/)
- Verifiable Credentials Data Model v1.1 : W3C recommendation [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)
- Decentralized Identity Foundation (DIF) [https://identity.foundation/](https://identity.foundation/)
- Internet Engineering Task Force (IETF) [https://www.ietf.org/](https://www.ietf.org/)
- Sedlmeir, J., Smethurst, R., Rieger, A. *et al.* Digital Identities and Verifiable Credentials. *Bus Inf Syst Eng* **63**, 603–613 (2021). https://doi.org/10.1007/s12599-021-00722-y
- Zero-knowledge credentials with deferred revocation checks [https://github.com/decentralized-identity/snark-credentials/blob/master/whitepaper.pdf](https://github.com/decentralized-identity/snark-credentials/blob/master/whitepaper.pdf)
- EBSI DID Method**:** [https://ec.europa.eu/digital-building-blocks/wikis/display/EBSIDOC/EBSI+DID+Method](https://ec.europa.eu/digital-building-blocks/wikis/display/EBSIDOC/EBSI+DID+Method)
- D. Maram *et al*., "CanDID: Can-Do Decentralized Identity with Legacy Compatibility, Sybil-Resistance, and Accountability," *2021 IEEE Symposium on Security and Privacy (SP)*
, 2021, pp. 1348-1366, doi: 10.1109/SP40001.2021.00038.
- Decentralized Identity with the Tezos DID Method [https://sprucesystems.medium.com/decentralized-identity-with-the-tezos-did-method-d9cf6676dd64](https://sprucesystems.medium.com/decentralized-identity-with-the-tezos-did-method-d9cf6676dd64)
- World Wide Web Consortium ********[https://decentralized-id.com/web-standards/w3c/](https://decentralized-id.com/web-standards/w3c/)