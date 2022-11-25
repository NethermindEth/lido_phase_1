# Towards Smart Contract-based Verification of Anonymous Credentials

Abstract: Smart contracts often need to verify identity-related information of their users. However, such information is typically confidential, and its verification requires access to off-chain resources. Given the isolation and privacy limitations of blockchain technologies, this presents a problem for on-chain verification. In this paper, we show how CL-signature-based anonymous credentials can
be verified in smart contracts using the example of Hyperledger Indy, a decentralized credential management platform, and Ethereum, a smart contract-enabled
blockchain. Therefore, we first outline how smart contract-based verification can be integrated in the Hyperledger Indy credential management routine and, then, provide a technical evaluation based on a proof-of-concept implementation of CL-signature verification on Ethereum. While our results demonstrate technical feasibility of smart contract-based verification of anonymous credentials, they also reveal technical barriers for its real-world usage.
Classification: Anonymous Credentials
Labels: Possible tool in larger solution, Smart Contracts instead of oracles, Worthwile Sybil resistance insights
Link to the paper: https://eprint.iacr.org/2022/492.pdf
Score: no idea
Score Phase 1: Maybe relevant
Year: 2022

## Summary of the paper’s contents

The authors propose an Anonymous Credential (AC) system in which verification is performed on-chain by a Smart Contract. In particular, this allows to remove trust from the verifier (one of the goals of the authors).

Other than that, the project follows the usual workflows between Issuer, Holder, and Verifier. It relies on Hyperledger-Indy as a decentralized ledger to store credential definitions and metadata, though any other public ledger could be used.

They follow an Anonymous Credential scheme due to [Camenisch’s and Lysyanskaya’s](Work%20of%20Camenisch%20and%20Lysyanskaya%20on%20Anonymous%20Cre%20dc28c53317b1437c82160ed403cbf9fc.md), which is a scheme that is natively supported in Hyperledger Indy.

The authors discuss a mechanism for achieving Sybil resistance. However the mechanism is more suited to only preventing the sharing of credentials. The idea is still interesting, if anything because it is not commonplace.

## Concepts

### **Anonymous Credentials (AC)**

In the literature, there is not a clear consensus on what the concept of AC exactly means. 

In [W3C’s specification](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%2058bf1260a9ee4e7194fc86cc1db47f3a.md)s, the concept of AC does not exist, and what they call a Verifiable Credential is precisely what other references call Anonymous Credential: namely, a VC whose verification mechanism does not leak unnecessary information about the attributes in the credential (there are further privacy-related attributes one asks of an AC, see [here](W3C%E2%80%99s%20Verifiable%20Credentials%20Data%20Model%20v1%201%2058bf1260a9ee4e7194fc86cc1db47f3a.md)).

Other references separate the two concepts, with AC’s being a subclass of VC’s that possess privacy-preserving properties. An example is the paper discussed in this note. 

Additionally, an AC may be required to preserve the Holder’s privacy both during verification **and issuance**. W3C neither recommends nor discourages privacy during issuance time.

In this note we follow the latter notion of AC.

### **Hyperledger Indy**

[Hyperledger Indy](Hyperledger%20Indy%206ca56848c73a4a3a821c82813af6241d.md) is a (permissioned) decentralized credential management system. In particular, it allows to create and store Anonymous Credentials (AC) based on methods due to Camenisch and Lysyanskaya (see below).

In general terms, Hyperledger Indy is simply a public ledger that specializes on the management of DID’s and VC’s. Theoretically, it could be replaced by any other public ledger. However, in terms of implementation, Hyperledger may provide already existing infrastructure that is not available on other ledgers.

### **Camenisch and Lysyanskaya’s CL-signatures**

These two authors are central in the AC literature published between the years 1990-2005 (approx.) Some of their methods revolve around the following ideas:

An AC is defined to be an Issuer’s signature on the Holder’s secret key $sk$ (and possibly some extra attributes). 

The goal is then to:

1. Enable the Issuer to create such signature without discovering anything about $sk$.
2. Enable the Holder to prove that the Issuer signed $sk$, without revealing $sk$, and in a way that certifies that the Holder knows $sk$.

To achieve these goals the following primitives are used:

- A signature scheme.
- A protocol that allows a party H (the holder, in our case) to commit to a value $v$, and another party S (the Issuer) to sign $v$. This must occur without S learning anything about $v$.
- Another protocol that allows to prove knowledge of a signature on a committed value.

We discuss these in much more detail in the note [Work of Camenisch and Lysyanskaya on Anonymous Credentials](Work%20of%20Camenisch%20and%20Lysyanskaya%20on%20Anonymous%20Cre%20dc28c53317b1437c82160ed403cbf9fc.md) 

## The approach

The workflow of the proposed approach is the following:

- The Issuer generates a **credential definition** and registers it on the ledger (namely, Hyperledger Indy). This definition contains:
    - The set of attributes to be verified.
    - The issuer’s public key.
    - A reference to the applicable signature algorithm (the CL-signature scheme).
- The Holder requests the Issuer to issue a credential and the latter sends the credential to the Holder (provided the Issuer agrees to issue such credential).
- A Developer creates a Smart Contract that runs the CL-signature verification algorithm. To do so, it uses the information (parameters) contained in the credential definition.
- The Holder submits the proof in its AC (together with any necessary metadata) to the Smart Contract, which verifies the validity of such proof.
- The proof validity of the AC is stored on the Smart Contract, and any 3rd party can see that indeed the AC is valid.
- **Predicates**: The Smart Contract also allows to prove that some predicates involving the AC’s attributes are true.
    
    **Note**: The only predicates supported in the paper are equality and inequality. 
    

![Figure taken from the paper discussed in this note. [https://eprint.iacr.org/2022/492.pdf](https://eprint.iacr.org/2022/492.pdf)
Our description of the workflow has slight technical differences with that of the figure, but in essence, the workflow is the same.](Towards%20Smart%20Contract-based%20Verification%20of%20Anony%202b002bb58dc44774a64a4f7c76c56b5f/Untitled.png)

Figure taken from the paper discussed in this note. [https://eprint.iacr.org/2022/492.pdf](https://eprint.iacr.org/2022/492.pdf)
Our description of the workflow has slight technical differences with that of the figure, but in essence, the workflow is the same.

### **Implementation and gas costs**

The authors provide a proof-of-concept of their method. They implement a CL-verification Smart Contract. In their experiments they verify the validity of one AC, together with an equality predicate between two attributes.

The cost is of 32M gas. With today’s (21/11/22) gas price of 16.4 gwei, **this amounts to about 0.5ETH**. 

The authors mention that their implementation is has much room for optimization, but they say that this gas cost is a serious obstacle to their approach.

### Discussion about Sybil attacks

The authors discuss two approaches in regards to achieving Sybil resistance:

1. Delegate this problem to the Issuers. This is a common approach that we have seen in many other projects. Basically, Sybil resistance is left as out of scope.
2. The authors propose “turning off unlinkability in the VC’s proofs”. The default construction in the paper features unlinkability of proofs: this means that proving twice that a VC is valid will produce two different proofs.  
    
    Turning off unlinkability would allow the Smart Contract to detect when the same credential has been verified by two different Eth accounts. 
    
    **Note**: This does not seem to fully address the Sybils problem. It is more a mechanism that prevents sharing credentials.
    

## Evaluation

- **Ok**: The [paper contains an ok discussion on Sybil resistance](Towards%20Smart%20Contract-based%20Verification%20of%20Anony%202b002bb58dc44774a64a4f7c76c56b5f.md). Their ideas ultimately only address the problem of preventing Holders from sharing credentials between them. A similar mechanism may be a piece in a bigger solution for achieving Sybil resistance.
- **Not too good**: The paper is from 2022 but the authors don’t mention some relevant technology:
    - **Layer 2’s**: a possible solution to the gas cost problem is to run the Verification Smart Contracts  on an L2 instead of on Ethereum’s mainnet. The paper does not mention this.
    - **More general predicates**: Together with L2’s, it would be possible to prove basically arbitrary predicates between AC’s attributes (recall that the authors only discuss equality and inequality predicates).
    - **More modern approaches to AC verification**: When Camenisch and Lysyanskaya published many of their papers on Anonymous Credentials, efficient zk-SNARKs did not exist. Hence, their methods do not make use of all the recent developments around zk-SNARKs.
        
        Another project that allows for private on-chain verification of credentials is [Polygon Id](Polygon%20Id%2046505e46892d4010801f49b1114a8450.md). 
        The latter allows for much more, and it seems better technology than the one presented here, especially taking into account that both projects are from 2022.
        Note that Polygon Id does not have gas cost issues (at least no concerns on this regard are raised in the documentation).
        
        Other projects we reviewed with on-chain verification are … 
        
- **Interesting information:** An interesting piece of information is the high gas cost their proof-of-concept has. This demonstrates that deploying a solution that relies on Smart Contracts on mainnet may not be the best idea.
    
    It also gives us a benchmark of how much VC verification may cost.