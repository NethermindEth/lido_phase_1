# Isaac’s write-up

Polygon ID is a self-sovereign, decentralize and private identity powered by zero-knowledge cryptography

Properties

- Blockchain-based ID for decentralized and self-sovereign models
- Zero-Knowledge protocols for privacy
- Scalable and private on-chain verification to boost decentralized apps and DeFi
- Open to existing standards and ecosystem development

Polygon ID makes use of the projects iden3 and Circom-Iden3 for managing identities with zero knowledge

Polygon ID allows for the construction of new forms of reputations. Some examples include decentralized credit score for financial primitives and social payments in DeFi; decentralized sybil score, voting power / delegation and domain-expertise reputation for DAOs to enable new decision-making and governance models; player reputation profile for Web3 games; private and censorship-resistant P2P communication and interactions for social applications.

- Identity reputation cryptographically verified
- No middle-man to interact with users
- Compose validation using smart contracts(with privacy?)

Polygon ID can be used to construct identity and trust services

- dAccess-as-a-Service
- Environment for existing solutions and new ones to come
- KYC,  KYB, attestation

# Iden3

- Anything can be an identity. (can be a person, a company, an organization, a DAO, or a government.)
- One person can define and have many identities.
- In Ethereum, an identity is an account or a smart contract.

An identity can provide a claim. A claim is a statement, and claims usually create relations between identities.

If an identity wants to create many claims, it can put all the claims in a database, construct a Merkle tree of that database(specifically iden3 uses sparse Merkle trees), and just publish (with a transaction) the root of the Merkle tree on-chain.

While direct claims scale really well for identities that make a lot of claims (since millions of claims can be batched in a single transaction), an average user will probably only need to make a few claims a day, and so won't benefit from this batching.

Indirect claims make use of relayers to spend zero gas. since the relayer is responsible for batching the claims and publishing the transactions.

Also using zk-proofs, we can ensure that the relayer is trustless. The worst a relayer can do is to not publish them.

zk-proofs are useful to prove a claim without revealing any more information. Also, it can make use of non-reusable proofs that are not valid to send to a third party.

<aside>
💡 At iden3, one of our major goals is scalability. Specifically, we believe that anybody should be able to create as many identities as they want. And that any identity should be able to generate as many claims as it wants.

</aside>

## Basis

- Issuer
- Holder
- Verifier
- Credential

For Merkle trees Poseidon algorithm is used, while the zkSNARK used is Groth16