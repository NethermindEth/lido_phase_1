# A Decentralized Public Key Infrastructure with Identity Retention

Abstract: Public key infrastructures (PKIs) enable users to look up and verify one another's public keys based on identities.
Current approaches to PKIs are vulnerable because they do not offer sufficiently strong guarantees of \emph{identity retention}; that is, they do not effectively prevent one user from registering a public key under another's already-registered identity.
In this paper, we leverage the consistency guarantees provided by cryptocurrencies such as Bitcoin and Namecoin to build a PKI that ensures identity retention.
Our system, called Certcoin, has no central authority and thus requires the use of secure distributed dictionary data structures to provide efficient support for key lookup.
Added to deliverable?: No
Already read?: Yes
Assigned readers: Jorge Arce-Garro
BS factor: derivative
Classification: VC
Date of publication: 2014
Link to the paper: https://eprint.iacr.org/2014/803
MZ checked the note: No
Score Phase 1: Maybe relevant

This paper is one of the first implementations of a decentralized public key infrastructure. This may be relevant for background purposes in the paper, but a PKI probably does not have all the features we need to work as decentralized identifiers do.

For example, in the context of Lido, the same party can create multiple pseudonyms as identities. 

# Introduction

Public key infrastructure: database of $(id, pk)$ pairs. Two goals of public key infrastructure:

- Accurate registration: the inability of a user to register an identity that does not belong to him or her
- Identity retention: the inability of a user to impersonate an identity already registered to someone else.

The PKI to be presented in this paper focuses on identity retention.

### Common approaches to PKI

- Certificate Authorities (CAs): CAs can fail due to centralization, and the existence of multiple standards can easily cause multiple keys to belong to the same identity, violating identity retention.
- Peer-to-peer certification, or Webs of Trust, such as PGP. Does not offer identity retention.

### Paper contributions

- Instead of having to trust a third party as in the CA system or a small set of fellow users as in the PGP system, Certcoin only requires that users trust that the majority of other users are not malicious.
- First instance of blockchain used for a PKI

Because of the decentralized nature of this PKI, there is no single authority who can maintain a local dictionary data structure for efficient public key lookup. We therefore separate the functionality of verifying a known public key from that of looking up a new public key, and leverage secure distributed data structures to support each of them efficiently. In particular, we use cryptographic accumulators to facilitate fast public key verification, and distributed hash tables to facilitate fast public key lookup.

# Overview

Three versions:

- Version 0: simply traverse the blockchain to find the most recent (id, pk) pair
- Version 1: use a cryptographic accumulator (linear lookup time)
- Version 2: use a distributed hash table (constant time)