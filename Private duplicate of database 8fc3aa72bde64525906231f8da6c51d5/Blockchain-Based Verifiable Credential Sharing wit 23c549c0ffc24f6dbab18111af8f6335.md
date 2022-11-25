# Blockchain-Based Verifiable Credential Sharing with Selective Disclosure

Abstract: Sharing credentials could raise privacy concerns. For digital credentials to be widely accepted, there is a need for an end-to-end system that provides (i) secure verification of the participant identities and credentials to increase trust, and (ii) a data minimisation mechanism to reduce the risk of oversharing the credential data. This paper proposes CredChain, a blockchain-based Self-Sovereign Identity (SSI) platform architecture that allows secure creation, sharing and verification of credentials. Beyond the verification of identities and credentials, a flexible selective disclosure solution is proposed using redactable signatures. The credentials are managed through a decentralised application/wallet which allows users to store their credential data privately under their full control and re-use as necessary. Our evaluation results show that CredChain architecture is feasible, secure and exhibits the level of performance that is within the expected benchmarks of the well-known blockchain platform, Parity Ethereum.
Classification: VC
Labels: Centralized/permissioned, Not Sybil resistant, Possible tool in larger solution
Link to the paper: https://ieeexplore.ieee.org/document/9343074
Score: no idea
Score Phase 1: Relevant
Year: 2020

Describes a verifiable credential sharing scheme.  It uses Merkle trees for Selective Disclosure.  Credentials are created by trusted third parties, the example they give is of a university issuing a degree.

### Description of protocol

A *credential* consists of a Merkle tree of *attributes*, in the case of a university degree the attributes could be the different classes the student attended and their grades.

The paper uses a redactable signature proposed by Johnson et al., basically a Merkle tree.  The Issuer signs the root node and posts it on the blockchain.  Then the Recipient reveals whichever nodes he wants to the Verifier.

Optionally, the Issuer can also include a list mandatory attributes that the Recipient must disclose to the Verifier, and stores the list in the credential header.

R. Johnson, D. Molnar, D. Song, and D. Wagner. Homomorphic signature schemes. In B. Preneel, editor, CT-RSA, LNCS, volume 2271, pages 244–262, 2002.