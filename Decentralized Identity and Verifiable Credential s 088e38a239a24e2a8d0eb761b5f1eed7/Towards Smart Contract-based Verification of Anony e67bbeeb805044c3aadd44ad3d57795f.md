# Towards Smart Contract-based Verification of Anonymous Credentials

Abstract: Smart contracts often need to verify identity-related information of
their users. However, such information is typically confidential, and its verification requires access to off-chain resources. Given the isolation and privacy limitations of blockchain technologies, this presents a problem for on-chain verification. In this paper, we show how CL-signature-based anonymous credentials can
be verified in smart contracts using the example of Hyperledger Indy, a decentralized credential management platform, and Ethereum, a smart contract-enabled
blockchain. Therefore, we first outline how smart contract-based verification can
be integrated in the Hyperledger Indy credential management routine and, then,
provide a technical evaluation based on a proof-of-concept implementation of
CL-signature verification on Ethereum. While our results demonstrate technical
feasibility of smart contract-based verification of anonymous credentials, they
also reveal technical barriers for its real-world usage.
Actions needed and questions: @Albert Garreta any opinion on that piece?

@Michal Zajac For now, the piece is interesting. It explains how to combine Hyperledger Indy with on-chain verification of the credentials managed by Hyperledger Indy. In abstract terms, we can think of Hyperledger as a permissioned oracle service. 

I want to know more about Hyperledger (and similar solutions like Sovrin) before reaching a conclusion. I am planning to propose revisiting the and similar projects: they rely on permissioned “validators”, but still, we have been working precisely on how to remove the “permission” part in this type of projects, so maybe we can use a solution based on them. Additionally, these two projects (Hyperledger and Sovrin), appear often in the literature, so even if they are not interesting for Lido we should discuss that in the SoK IMO.

@Albert Garreta, thanks. Please provide an abstract

@Michal Zajac Done! I also have elaborated on my evaluation of the paper throughout the note (to be presented tomorrow)
Added to deliverable?: No
Already read?: No
Assigned readers: Albert Garreta
BS factor: weak
Classification: Anonymous Credentials
Date of publication: 2022
Labels: Possible tool in larger solution, Smart Contracts instead of oracles, Trustless verification of credentials, Worthwile Sybil resistance insights
Link to the paper: https://eprint.iacr.org/2022/492.pdf
MZ checked the note: No
Presentation date: November 23, 2022
Score Phase 1: Maybe relevant
Work Group: Academic literature

## Summary of the paper’s contents

The goal of the paper is to remove the trust placed upon the Verifiers in a SSI system. 

The approach consists in verifying Verifiable Credentials with a Smart Contract.

Privacy must be preserved, and no further trust assumptions can be made. In particular, using oracles is not allowed.

The authors propose a mechanism for smart contract-based verification of Anonymous Credentials. The credentials used follow [Camenisch’s and Lysyanskaya’s so called CL-signature approach](W3C%E2%80%99s%20Decentralized%20Identifiers%20data%20model%20v1%200%20f6b6cebed5644423a89829cf10b7a6f7.md). 

These AC’s are the ones used in Hyperledger Indy, and indeed the authors use Hyperledger-Indy as a component of their solution. 

Incidentally, the authors discuss a possibly interesting idea for achieving Sybil resistance. The goodness of the idea needs to be evaluated, but at least it is different than what we have seen in many papers.

## Concepts

### **Anonymous Credentials (AC)**

There is not a clear consensus on what the concept of AC exactly means. 

In [W3C’s specification](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%20474fc1e0e0e249dea8a96c0d4433c697.md)s, the concept of AC does not exist, and what they call a Verifiable Credential is precisely what other references call Anonymous Credential: namely, a VC whose verification mechanism does not leak unnecessary information about the attributes in the credential (there are further privacy-related attributes one asks of an AC, see [here](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%20474fc1e0e0e249dea8a96c0d4433c697.md)).

Other references separate the two concepts, with AC’s being a subclass of VC’s that possess privacy-preserving properties. An example is the paper discussed in this note. 

**Note**: It is also reasonable to understand that, in W3C, AC’s are the so-called **Verifiable Presentations,** which are derived from VC’s.

In this note we follow W3C’s approach because:

- In our experience W3C is a commonly used standard.
- W3C’s approach is the simplest and most unambiguous of all.

Consequently, our presentation has some minor technical differences with respect to the paper. 

### **Hyperledger Indy**

[Hyperledger Indy](Hyperledger%20Indy%2009792507d4e940ea8c05574c3f955b5d.md) is a (permissioned) decentralized credential management system. In particular, it allows to create and store Anonymous Credentials (AC) based on methods due to Camenisch and Lysyanskaya (see below).

In general terms, Hyperledger Indy is simply a public ledger that specializes on the management of DID’s and VC’s. Theoretically, it could be replaced by any other public ledger (however, in terms of implementation, Hyperledger may provide already existing infrastructure that is not available on other ledgers).

### **Camenisch and Lysyanskaya’s CL-signatures**

These two authors are central in the AC literature published 1990-2005 (approximately). Their methods are usually variations of the same idea

[vey briefly explain the idea]

Details of these ideas are provided in our review note on the paper [Signature Schemes and Anonymous Credentials from Bilinear Maps](Signature%20Schemes%20and%20Anonymous%20Credentials%20from%20B%20768f7a435f484142aa27ef60eab34cba.md).

![PNG image.png](Towards%20Smart%20Contract-based%20Verification%20of%20Anony%20e67bbeeb805044c3aadd44ad3d57795f/PNG_image.png)

[ the specific scheme of this paper is described in “signature schemes with efficient protocols”, a classic reference. this has a nice informal explanation of how one gets AC’s “a la Camenisch and Lysyanskaya”]

## The approach

The workflow of the proposed approach is the following:

- The Issuer generates a **credential definition** and registers it on the ledger (namely, Hyperledger Indy). This definition contains:
    - the set of attributes to be verified,
    - the issuer’s public key, and
    - a reference to the applicable signature algorithm (the CL-signature scheme).
- The Holder requests the Issuer to issue a credential and the latter sends the credential to the Holder (provided the Issuer believes such credential is legit). 
Note: Hyperledger Indy provides infrastructure for this process.
- A Developer creates a Smart Contract that runs the CL-signature verification algorithm. To do so, it uses the information (parameters) contained in the credential definition.
- The Holder can prove that its VC is legitimate by:
    - Submitting the proof in its VC (together with any necessary metadata) to the Smart Contract.
    - The proof validity of the VC is stored on the Smart Contract, and any 3rd party can see that indeed the VC is valid.
- **Predicates**: The Smart Contract also allows to prove that some predicates involving the VC attributes are true.
    
    **Note**: The only predicates supported in the paper are equality and inequality. 
    

![Figure taken from the paper discussed in this note. [https://eprint.iacr.org/2022/492.pdf](https://eprint.iacr.org/2022/492.pdf)
Our description of the workflow has slight technical differences with that of the figure, but in essence, the workflow is the same.](Towards%20Smart%20Contract-based%20Verification%20of%20Anony%20e67bbeeb805044c3aadd44ad3d57795f/Untitled.png)

Figure taken from the paper discussed in this note. [https://eprint.iacr.org/2022/492.pdf](https://eprint.iacr.org/2022/492.pdf)
Our description of the workflow has slight technical differences with that of the figure, but in essence, the workflow is the same.

Something the authors note is that:

- the approach does not require any changes to Hyperledger Indy, and
- no extra trust assumptions are made, i.e. the trust assumptions are the same as the ones made by Hyperledger Indy: namely, the issuer is trusted by the verifier.

### **Implementation and gas costs**

The authors provide a proof-of-concept of their method. They implement a verification Smart Contract. In their experiments thy verifying the validity of one AC, together with an equality predicate between two attributes.

The cost was of 32M gas. With today’s (21/11/22) gas price of 16.4 gwei, **this amounts to about 0.5ETH**. 

The authors mention that their implementation is just a proof of concept and that there is much room for optimization, but they say that this gas cost is a serious obstacle to their approach.

### Discussion about Sybil attacks

The authors discuss two approaches in regards to achieving Sybil resistance:

1. Delegate this problem to the Issuers. This is a common approach that we have seen in many other projects. Basically, Sybil resistance is left as out of scope.
2. The authors propose “turning off unlinkability in the VC’s proofs”. The default construction in the paper features unlinkability of proofs: this means that proving twice that a VC is valid will produce two different proofs.  
    
    Turning off unlinkability would allow the Smart Contract to detect when the same credential has been verified by two different Eth accounts. 
    

## Evaluation

- **Good**: The [paper contains an interesting idea for increasing Sybil resistance](Towards%20Smart%20Contract-based%20Verification%20of%20Anony%20e67bbeeb805044c3aadd44ad3d57795f.md). The robustness of the approach depends on the rest of the credential system in use (it depends on how difficult it is for one entity to obtain two different valid VC’s, even if the difference is tiny).
Nevertheless the idea is “fresh” while not being unreasonable. This is of significant value.
- **Not too good**: The paper is from 2022, yet the authors don’t mention some relevant technology:
    - **Layer 2’s**: a possible solution to the gas cost problem is to run the Verification Smart Contracts  on an L2 instead of on Ethereum’s mainnet. However there is no mention of this.
    - **More general predicates**: Together with L2’s it sounds quite possible to prove somewhat arbitrary predicates between VC’s attributes (recall that the authors only discuss equality and inequality predicates).
    - **More modern approaches to VC verification**: When Camenisch and Lysyanskaya published many of their papers on Anonymous Credentials, zk-SNARK technology did not exist (or was basically unusable). Hence, their methods do not make use of all the recent developments around zk-SNARKs.

<aside>
💡 Another project that allows for private on-chain verification of credentials is [Polygon Id](Polygon%20Id%20985c35465c5c464480c0d50cf71edb29.md). 
The latter allows for much more, and it seems better technology than the one presented here, especially taking into account that both projects are from 2022.
Note that Polygon Id does not have gas cost issues (at least no concerns on this regard are raised in the documentation).

</aside>

- **Interesting information:** An interesting point of this paper is the high gas cost their proof-of-concept has. Generally speaking, this demonstrates that deploying a solution that relies on Smart Contracts on mainnet probably is not the best idea.
    
    It also gives us a benchmark of how much VC verification may cost.