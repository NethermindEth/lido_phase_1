# Hyperledger Indy

Abstract: https://wiki.hyperledger.org/display/indy/Hyperledger+Indy provides tools, libraries, and reusable components for providing digital identities that are rooted in blockchains or other distributed ledgers so they are interoperable across administrative domains, applications, and any silo. Indy is interoperable with other blockchains or can be used standalone, powering identity's decentralization.
They use a “blockchain” just as a Database. It is important to note that this “blockchains” are in a permissioned setting
Labels: Centralized/permissioned
Link to the paper: https://indy.readthedocs.io/en/latest/
Score: no idea

[https://wiki.hyperledger.org/display/indy/Hyperledger+Indy](https://wiki.hyperledger.org/display/indy/Hyperledger+Indy)

[Hyperledger Indy](https://wiki.hyperledger.org/display/indy/Hyperledger+Indy) provides tools, libraries, and reusable components for providing digital identities that are rooted in blockchains or other distributed ledgers so they are interoperable across administrative domains, applications, and any silo. Indy is interoperable with other blockchains or can be used standalone, powering identity's decentralization.

Indy has its own distributed ledger not depending on any other blockchain. It also has its own PBFT consensus called RBFT.

Indy has been deployed on Sovrin, Findy, Kiva, etc.

Key Characteristics

- Distributed ledger purpose-built for decentralized identity
- Correlation-resistant by design
- DIDs (Decentralized Identifiers) are globally unique and resolvable (via a ledger) without requiring any centralized resolution authority.
- Pairwise Identifiers create secure, 1:1 relationships between any two entities.
- [Verifiable Credentials](https://w3c.github.io/vc-data-model/) in an interoperable format for the exchange of digital identity attributes and relationships, currently in the standardization pipeline at the W3C
- Zero Knowledge Proofs which prove that some or all of the data in a set of Claims is true without revealing any additional information, including the identity of the Prover

![Taken from [https://www.youtube.com/watch?v=ncdvaJrOm_Q](https://www.youtube.com/watch?v=ncdvaJrOm_Q)](Hyperledger%20Indy%206ca56848c73a4a3a821c82813af6241d/Wed_Nov__9_100812_PM_CST_2022.png)

Taken from [https://www.youtube.com/watch?v=ncdvaJrOm_Q](https://www.youtube.com/watch?v=ncdvaJrOm_Q)

Indy looks for a decentralized source of trust(blockchain) in which data is publicly available.

- What is on-chain
    - Public DID and DID-docs
    - Issuer’s public keys
    - Credential’s schemas
    - information about revocation
- What is off-chain
    - Credentials
    - Proves
    - Private Keys

Hyperledger Indy is built over Indy-plenum(A ledger and consensus protocol) and Indy-node(Identity-specific tx built on Indy-plenum).

# Architecture

![Taken from [https://www.youtube.com/watch?v=ncdvaJrOm_Q](https://www.youtube.com/watch?v=ncdvaJrOm_Q)](Hyperledger%20Indy%206ca56848c73a4a3a821c82813af6241d/Wed_Nov__9_103042_PM_CST_2022.png)

Taken from [https://www.youtube.com/watch?v=ncdvaJrOm_Q](https://www.youtube.com/watch?v=ncdvaJrOm_Q)

There are two pools in Hyperledger Indy, a validator pool and an observer pool. Validators pool handles `writes` and `reads` with the help of the consensus protocol, and observers stay in sync with the validators pools and handle the reads of identities data on-chain.

### Write requests

Ledger is permission, so every request must be signed by the user using Ed25519. The `write` request is sent to all the nodes, and it is expected to receive $F+1$ replies.
Signatures are verified against a public key stored in the Ledger, and every transaction author must have a DID in the Ledger.

### Read requests

Users can request only one node, and they can trust this one node because it provides replies with BLS signatures and corresponding proof.

Anyone can read, no authentication is required.

# Ledger

- Ordered log of transactions
- Merkle tree of the whole ledger
- No real blocks

There is a Ledger catch-up procedure for new or lagging behind nodes, implying that all ledger information is recoverable.

There are actually multiple layers and new Ledgers can be introduced via plugins

 

- Audit Ledger
    - This introduces the ordering across all ledger
    - Every audit tx can be considered as a block
- Pool Ledger
    - Can be thought of as information about the current state of the pool
    - Adding, editing, and removing nodes
    - **Only a `TRUSTEE` can update the pool ledger**
- Config Ledger
    - Pool ledger config parameters for all the nodes to come to a consensus
- Domain Ledger
    - Application-specific txs
    - identity-specific txs

# RBFT consensus

- Redundant BFT
- Improves on PBFT by running several protocol instances in parallel
- Better throughput and lower latency than proof-of-work
- Claims that it performs better than its predecessors(which ones?) under dynamic load and under attack
- RBFT is a 3-phase commit protocol
- View change is the same as in PBFT
- if the master instance degrades in performance the other parallel instances initiate a view change of the primary execution

# Indy use cases

- **Digital Documents** — Have secure and versatile digital forms of your important documents. (passport, driver’s license, birth certificate, medical records, etc.)
- **Secure Password**-**less Authentication (SPA)** — Easily sign in to a secure site by simply clicking “login” and providing a fingerprint (or other biometric) with your mobile device.
- **End of Spam** — No more ‘junk emails’ or changing phone numbers. Spam doesn’t get through without your permission or without your current gate code.
- **Membership management** — Your agent becomes your membership card for ALL your memberships and can be used everywhere. Ski pass, subway card, rewards member, etc.
- **Enforce age restrictions** — Devices, websites, and services could more effectively require a person to be of a certain age.
- **Software Development Pipeline** — Verify development builds were completed properly and officially signed by the developers for consumers of the software. This could also be useful because build credentials could be revoked if the software has a vulnerability informing consumers of the software, leading to a very powerful decentralized security alert system.
- **Exchange of Business Documents** — e.g. exchange of a Purchase Order or Invoice between two parties
- **Games** — Game publishers could rely on identity providers to prevent minors from playing their games, restrict content, make in-game purchases, etc...without having to manage the identity themselves.  See “Membership Management/Enforce Age Restrictions” above.
- **Employment Verification** — A third party could seek out VCs (names of previous employers)  as previous employers of a potential job candidate, and then in turn these VCs could be vetted by other third-party verifiers for higher certainty and veracity as to the employment.  This would differ from governmental verification for employment and rather seek the social element of employment references and veracity of employment.
- **Supply Chain Provenance** — When a complex widget is built that involves multiple organizational identities handing them off between them, different forms of credentials could be passed that would help efforts such as batch #, materials used, cost, and others to help do QA, analysis of inefficiencies, and other cases where such widgets are needed to be securely transferred between parties marked by decentralized identifiers and transferred with agents.

[https://www.hyperledger.org/learn/white-papers](https://www.hyperledger.org/learn/white-papers)

Marked as non-relevant because most of the solutions that uses Hyperledger Indy rely on a centralized authority

Other projects

Decentralize Identity Foundation: [https://identity.foundation/](https://identity.foundation/)

Check [https://www.youtube.com/watch?v=P_9N-Kt1nFs](https://www.youtube.com/watch?v=P_9N-Kt1nFs) for more

[https://www.hyperledger.org/wp-content/uploads/2018/04/Hyperledger_Arch_WG_Paper_2_SmartContracts.pdf](https://www.hyperledger.org/wp-content/uploads/2018/04/Hyperledger_Arch_WG_Paper_2_SmartContracts.pdf)

[https://github.com/hyperledger/indy-plenum/blob/main/docs/source/main.md](https://github.com/hyperledger/indy-plenum/blob/main/docs/source/main.md)

[https://github.com/hyperledger/indy-node/tree/main/docs/source](https://github.com/hyperledger/indy-node/tree/main/docs/source)

[https://www.hyperledger.org/use/hyperledger-indy](https://www.hyperledger.org/use/hyperledger-indy)