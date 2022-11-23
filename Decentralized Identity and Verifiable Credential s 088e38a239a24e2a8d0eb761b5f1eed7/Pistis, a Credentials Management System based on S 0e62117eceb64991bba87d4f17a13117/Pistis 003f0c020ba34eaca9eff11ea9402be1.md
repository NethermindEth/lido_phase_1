# Pistis

Pistis is a master thesis in Computer Science and Engineering, Politecnico di Milano, in 2019.

It provides quite a good literature search. It gave us useful references on both the theoretical and applied sides. 

But it doesn’t discuss **Sybil-resistancy** and **decentralized credential issuance** which may be seen as the core problems for our projects. 

Also, it allows the delegation of an identity, i.e. one can perform an operation on behalf of another identity, which we don’t want it.

# Introduction

- This thesis focuses on the existing SSI projects, particularly **uPort,** which is believed to be the most mature one. (it uses the Ethereum network)
- **Pistis** is a credential management system based on the Ethereum blockchain.

### Building blocks

- DIDs and DDOs (DID Documents)
- VCs
- Blockchain
    - It is used as a global decentralized authority to allow revocations of Verifiable Credentials alongside revocation of public keys associated with a DID.
- Smart Contracts
    - Operation executor
    - Permission registry
    - Trusted contact management
    - Credential status registry
    - DID registry
    - MultiSig operations
    - Revocation
- Actors (All need to have Ethereum key pairs)
    - User(s)
    - Issuer(s)
    - Verifier(s)

# Architecture

![Untitled](Pistis%20003f0c020ba34eaca9eff11ea9402be1/Untitled.png)

## DID management

### **DID Creation**

Any user who has a key pair for Ethereum can create a DID to use it in Pistis. Assume that a user has an Ethereum address **0xAB**, then his DID will be of the form **did:pistis:0xAB.**

### **DID Read and Verify**

**This is achieved through the DID Resolver** which is a software component with an API designed to accept requests for DID lookups and execute the corresponding DID method to retrieve the authoritative DID Document.

![Untitled](Pistis%20003f0c020ba34eaca9eff11ea9402be1/Untitled%201.png)

**DDO contains a list of addresses that are authorized to sign on behalf of that DID**, thus allowing a verifier to check authenticity by applying the asymmetric keys algorithm and checking whether the signing key is amongst the ones who have authorization permissions.

### DID update

**It is done by updating the DID Registry Smart Contract** that holds the mapping between DIDs and the relative addresses with their specific permission for that DID.

### DID deactivate

**It is achieved by revoking all addresses for a certain DID.** This makes the DID unusable and non-retrievable from that point onward.

# Processes

### Issue Verifiable Credentials

![Untitled](Pistis%20003f0c020ba34eaca9eff11ea9402be1/Untitled%202.png)

- Upon receiving a credential request, the web app
    - generates the Verifiable Credential,
    - signs it with its own private key,
    - wraps it into a verifiable presentation,
    - produces a JWT of type “Attestation”,
    - renders it as a QR code.
- The mobile app (user) checks the credential it received. If it is valid,
    - The mobile application verifies if the issuer is a trusted one, which means that the issuer’s DID is associated with a contact already stored in the list of trusted contacts of the application.
    - If not, the application asks the user if he wants to add the new issuer to the trusted contacts list with the information attached in the VC field of the Verifiable Credential.
    - Verifiable Credential is stored in the application's local storage.

### Share Verifiable Credentials

Sharing a VC happens when some service requires the user to be eligible for that service. In order to do so, **the user must prove he matches the service requirements.**

- A QR code is shown on the screen for the user to scan using the mobile application. The QR code carries a JWT which is a share request.
- If the user accepts, the requested Verifiable Credentials are packed inside a Verifiable Presentation which is signed by the user and sent to the callback URL inside a JWT.
- Then, the verifiable presentation needs to be verified,
    - first, for the verifiable presentation
    - second, for each of the credentials inside the presentation.

![Untitled](Pistis%20003f0c020ba34eaca9eff11ea9402be1/Untitled%203.png)

- After that, the verifier needs to perform verification about the issuer of the Verifiable Presentation and Credential. These are done using Trusted Contact Management.

### Revoke Verifiable Credentials

- A revocation list held by the Credential Status List Smart contract.
- An alternative may be an URL that publicly exposes a revocation list.
- In order to revoke a verifiable credential and verify its status, the W3C standard is applied. It proposes to insert a pointer to a claim revocation list inside the VC itself.
- This pointer points to the Credential Status List Smart contract.
- A function accepts as parameters the credential issuer, the credential id, the status, and the status reason. It then updates the smart contract storage.

### Entity Resolution (Trusted Contacts)

- Just the way it happens with mobile phones in which you choose whose number belongs to depending on your knowledge and on who you trust. In the same way, in Pistis, the user has a Trusted Contacts List (TC List) which simply associates an Entity to a DID.

# An example implementation

### **Who is involved?**

![Untitled](Pistis%20003f0c020ba34eaca9eff11ea9402be1/Untitled%204.png)

### User onboarding

![Untitled](Pistis%20003f0c020ba34eaca9eff11ea9402be1/Untitled%205.png)

### Book x-ray scan

![Untitled](Pistis%20003f0c020ba34eaca9eff11ea9402be1/Untitled%206.png)

### Perform x-ray scan

![Untitled](Pistis%20003f0c020ba34eaca9eff11ea9402be1/Untitled%207.png)

### Receive scan by e-mail

![Untitled](Pistis%20003f0c020ba34eaca9eff11ea9402be1/Untitled%208.png)

### Show the scan to the doctor

![Untitled](Pistis%20003f0c020ba34eaca9eff11ea9402be1/Untitled%209.png)