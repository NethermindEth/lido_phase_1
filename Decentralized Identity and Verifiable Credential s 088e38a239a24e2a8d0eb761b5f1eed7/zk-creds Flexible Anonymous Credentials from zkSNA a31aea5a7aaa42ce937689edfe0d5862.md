# zk-creds: Flexible Anonymous Credentials from zkSNARKs and Existing Identity Infrastructure

Abstract: Frequently, users on the web need to show that they are, for example, not a robot, old enough to access an age restricted video, or eligible to download an ebook from their local public library without being tracked. Anonymous credentials were developed to address these concerns. However, existing schemes do not handle the realities of deployment or the complexities of real world identity. Instead, they make (often incorrect) assumptions, e.g., that the local department of motor vehicles will issue sophisticated cryptographic tokens to show users are over 18. In reality, there are multiple trust sources for a given identity attribute, their credentials have distinctively different formats, and many, if not all, issuers are unwilling to adopt new protocols. We present and build zk-creds, a protocol that uses general-purpose zero-knowledge proofs to 1) remove the need for credential issuers to hold signing keys: credentials can be issued via a transparency log, Byzantine system, or even a blockchain; 2) convert existing identity documents into anonymous credentials without modifying documents or coordinating with their issuing authority; 3) allow for flexible, composable, and complex identity statements over multiple credentials. Concretely, identity assertions using zk-creds take less than 300ms in a real-world scenario of using a passport to anonymously access age-restricted videos.
Actions needed and questions: @Ahmet Ramazan Agirtas could you describe how the credential can be issued by a blockchain? Does the paper discuss how to get meatspace/Web2 data in to blockchain?
Added to deliverable?: No
Already read?: Yes
Assigned for action: Ahmet Ramazan Agirtas
Assigned readers: Ahmet Ramazan Agirtas
BS factor: important
Classification: Anonymous Credentials
Date of publication: 2022
Labels: Cryptographic primitive (Anonymous Credential), Legacy compatible, Possible tool in larger solution, Worthwile Sybil resistance insights
Link to the paper: https://eprint.iacr.org/2022/878.pdf
MZ checked the note: Yes
Presentation date: August 26, 2022
Reviewers: Michal Zajac
Score Phase 1: Relevant
Work Group: Hybrid

# TL;DR

In this note we summarize the $zk-creds$ scheme which is an anonymous credential scheme based on zkSNARKs. 

$zk-creds$ is an anonymous credential system in which a user can create a credential based on digitally signed real-world information, and convince an issuer that the credential is valid. Moreover, if a user behaves maliciously, the issuer can revoke the malicious user’s credentials. **It assumes that the credential list is maintained by a trusted party, a Byzantine system, or a public blockchain.** The main cryptographic primitive used in the $zk-cred$ is GROTH16. 

## How does it work?

In this system, it is assumed that every issuer has some issuance criteria, and the user who wants to have a valid (issued) credential $cred$ must meet them. (E.g., *the birth date in a $cred$ matches a digitally signed driver's license.)*  

**Issuance.** The user sends his credential $cred$ to the issuer along with a zk-supporting documentation that convinces the issuer about the validity of the $cred$. (E.g*, a Groth16 proof or a digital signature)* If the issuer is convinced by the zk-supporting documentation of the user, then the issuer adds $cred$ to his list and returns a proof (a Merkle authentication path) to the user. We say that the $cred$ is issued by an issuer $I$ if the $cred$ is included by $I$’s credential list. In this paper two issuance methods are given 

- first, an operator sends an issuance request to a smart contract (the credential list is maintained by the smart contract)
- the other alternative stated in the paper is to support on-chain proof verification.

**Show.** After the issuance of the credential $cred$, the user can use $zk-cred$ to convince a verifier that his credential $cred$ meets the access criteria of the verifier. Note that a verifier has a list of access criteria for an application using $zk-creds$. The user can convince the verifier by presenting a zero-knowledge proof that 

- his credential $cred$ is in the issuer’s list and
- the attributes in the $cred$ meet the verifier’s access criteria.

The verifier verifies the proof, and access is granted or rejected.

**Revoke.** If an issuer wants to revoke a credential of a user, then he simply deletes the credential from his list.

### Sybil resistance

The paper emphasizes that the primary method of Web2 services for preventing Sybil attacks is to consume a limited resource, i.e. 

- money (payment)
- attention (CAPTCHA)
- identity (proof of possession of governmental data (ID), mobile phone number, etc.)

This paper states that credentials can be generated and issued according to 

- legally signed identity information (such as passports with digital signatures)
- a payment, (i.e. a smart contract issues credentials only if a small fee is paid)
- the users’ valid email addresses (for example having Gmail in the credential generation)

### Oracle and self-issued credentials

The paper also discusses the so-called “oracle problem”: how can the nodes of a blockchain reach a consensus about an off-chain phenomenon? Two types of solutions are discussed:

1. The first one utilizes incentive systems (like Chainlink) to issue credentials that are based on public Web2 data (e.g., GitHub stars, Twitter follower count, etc.). 
2. The second one is the attestation on the authenticity of the data pulled from third-party data providers (web2 servers). The paper describes DECO (also Town Crier, implicitly). 

It is stated that the schemes with the second approach rely on some vulnerable assumptions. **DECO assumes that the verifier and the prover do not collude. On the other hand, the system utilizing Town Crier assumes that the hardware (TEE) is trusted.** However, it is also stated that those two can be used as a simple Sybil prevention.

### How does the $zk-creds$ get meatspace data into the blockchain?

The system is constructed with the following idea. It takes **an existing identity document that is signed by a real-world authority.** Then it converts the signed identity document **(e.g. passport)** into anonymous credentials **without any interaction with the issuer (e.g. US State department).**

The paper gives an example implementation for $zk-creds$. In this example, they use US passports that contain digitally signed data in an NFC-readable chip of a passport.

- The user prepares a zk-supporting document which proves in zero knowledge that the attributes in the credential match the signed data in the chip of the passport.
- The issuer verifies the zk-supporting document by using
    - the credential, which is a commitment to attributes from the passport,
    - econtent hash of the data in the passport,
    - the signature of US State Department on the econtent.