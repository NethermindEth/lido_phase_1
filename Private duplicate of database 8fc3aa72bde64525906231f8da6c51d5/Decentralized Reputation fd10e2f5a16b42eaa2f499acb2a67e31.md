# Decentralized Reputation

Abstract: In this work we develop a privacy-preserving reputation scheme for collaborative systems such as P2P networks in which peers can represent themselves with different pseudonyms when interacting with others. All these pseudonyms, however, are bound to the same reputation token, allowing honest peers to maintain their good record even when switching to a new pseudonym while preventing malicious ones from making a fresh start.
Our system is truly decentralized. Using an append-only distributed ledger such as Bitcoin's blockchain, we show how participants can make anonymous yet verifiable assertions about their own reputation. In particular, reputation can be demonstrated and updated effectively using efficient zkSNARK proofs. The system maintains soundness, peer-pseudonym unlinkability as well as unlinkability among pseudonyms of the same peer. We formally prove these properties and we evaluate the efficiency of the various operations, demonstrating the viability of our approach.
Classification: DI
Link to the paper: https://dl.acm.org/doi/abs/10.1145/3422337.3447839?casa_token=hGiXRI7wPxYAAAAA:9viHlmcKCzKnIhtO0hZ50QWLgreDxW7cJUGQGJ5bfDqoClcPpFIqMJ9JWUTVb2bp1p1TD7Yzw60
Score: no idea
Score Phase 1: Not relevant
Year: 2021

# Abstract

The work introduces a reputation scheme that:

- Preserves privacy. A user can use different pseudonyms to make claims about his reputation, all of which are privately bound to the same reputation token, “allowing honest peers to maintain their good record even when switching to a new pseudonym while preventing malicious ones from making a fresh start.”
- Is decentralized, can run on any append-only distributed ledger, such as Bitcoin. In particular, reputation can be demonstrated and updated effectively using efficient zkSNARK proofs.

# Introduction

- Reputation systems vulnerable to Sybil attacks.
- Inspired in the work of Androulaki et al., “Reputation systems for anonymous networks."
- Proposal: *reputation tokens* maintained by the peers themselves.
- Reveal only approximate reputations to mitigate de-anonymization attacks across pseudonyms.
- “Our system requires a single offline phase in which the identity of the peer has to be verified, since otherwise it would be impossible to offer protection against Sybil attacks as shown in J.R. Douceur. ‘The sybil attack.’(2002) ”
- “However, we show that even this phase can be decentralized in a privacy-preserving manner so that “identity” remains unlinkable to subsequent user actions.”

# Remaining sections

- The paper needs a decentralized identity system to already be in place in order to establish a reputation system. In fact, they suggest CanDID as the ideal approach.
- The paper also suggests to look into Namecoin and Certcoin as blockchain variants of the identity problem.

Since the paper defers to other projects, we can look into those instead.