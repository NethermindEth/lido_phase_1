# Burrata

Abstract: Burrata is a network of nodes that can be seen as an integration layer that allows users to bridge web2 identities and private data to web3. 
Added to deliverable?: No
Already read?: Yes
Assigned readers: Ahmet Ramazan Agirtas
BS factor: solid
Classification: DI, Data to Web3, VC
Date of publication: 2022
Labels: Implementations, Legacy compatible, Linkage of Web2 Ids, Possible tool in larger solution, Worthwile Sybil resistance insights
Link to the paper: https://www.burrata.xyz/
MZ checked the note: No
Presentation date: November 8, 2022
Reviewers: Jorge Arce-Garro
Score Phase 1: Relevant
Work Group: Blockchain projects

### DISCLAIMER

*The information in this note is taken from the [documents](https://docs.burrata.xyz/docs/getting-started/introduction) (limited) of Burrata, the call that we have with Osama Khan, co-founder of Burrata. This note is going to be updated when Burrata’s architecture details are published.* 

---

# Introduction

Burrata is a network of nodes that can be seen as an integration layer that allows users **to** **bridge web2 identity and private data to web3.** Burrata’s main aim is to **provide web3 developers necessary tools** so that they can build dApps and smart contracts by using web2 data **without building complex infrastructure like DIDs, VCs, etc.** 

Since A dAPP developer may need some information about users like financial history, consumer ID, etc,  the developer may handle lots of things to create a web3 ID. (See below figure)

![Source: [https://www.burrata.xyz/](https://www.burrata.xyz/)](Burrata%20b64a88c90bc94598bfccae66e158c137/Untitled.png)

Source: [https://www.burrata.xyz/](https://www.burrata.xyz/)

Instead, Burrata proposes an integration layer for all web2 services.

![Source: [https://www.burrata.xyz/](https://www.burrata.xyz/)](Burrata%20b64a88c90bc94598bfccae66e158c137/Untitled%201.png)

Source: [https://www.burrata.xyz/](https://www.burrata.xyz/)

Burrata’s architecture is composed of two components, i.e. 

1. on-chain contracts, and
2. off-chain “integration” nodes, which generate verifiable claims and credentials for web3 from web2 identities.

Burrata **is not a decentralized network**, but it aims to be so in the future. It is also planned to have a governance token in the future.

Using Burrata, a dAPP developer can integrate any web2 API and data sources into his smart contract in a trustless way. Here [DECO](https://arxiv.org/pdf/1909.00938.pdf) protocol comes into the scene. Burrata is one of [DECO](https://arxiv.org/pdf/1909.00938.pdf) alpha testing constructions. (**close coordination with Chainlink**) 

Note that pulling the data from web2 services by [DECO](https://arxiv.org/pdf/1909.00938.pdf) makes the data authentic. It makes the system trustless. Notice that, **the data providers (web2 services) are the trusted parties** in this construction.  

### Existing web2 integrations

The off-chain integration nodes also provide a **privacy-preserving presentation layer for selective disclosure. It is also stated in the documents that** the system will also provide a zero-knowledge proofs-based presentation layer in the future. 

### Identifying the users

Individual users will be identified by the **Know Your Customer systems.** Regarding Sybil attacks, Burrata is collaborating with some **companies focusing on biometric analysis (using very complicated techniques).** 

Institutional users will be identified by the **Know Your Business systems.** Additionally, going deep through the organization, organizations may be identified by their managers’ biometric hashes. (board of directors)

We may assume that **Burrata is an issuer or a tool for self-issuing.** After adding web2 APIs to the system, the credentials are created. Then one can use his wallet (in which a credential is defined according to a web2 ID) to transact over dApps. (See the below talk in which a house rental example is given.)

# Presentation and Demo

[Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)](https://www.youtube.com/watch?v=eJqZQ2_VBzo)

Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)

In the above video, a demo (Web3Retreat) is presented. The scenario is as follows. 

A dApp developer wants anyone to be able to rent houses in a permissionless way as long as they verify their identity and sign a temporary rental agreement.

If the dApp developer attempts to construct the system by himself, he needs to handle some issues, including

- finding an identity provider
- finding a legitimate way of signing the documents
- understanding complicated web standards like VCs, DIDs, etc.

In the demo, Burrata handles all those issues. Assume that a user wants to spend some time in the wood and decides to rent a house.

![Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)](Burrata%20b64a88c90bc94598bfccae66e158c137/Untitled%202.png)

Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)

- After choosing the house to be rented, the user connects his wallet.

![Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)](Burrata%20b64a88c90bc94598bfccae66e158c137/Untitled%203.png)

Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)

![Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)](Burrata%20b64a88c90bc94598bfccae66e158c137/Untitled%204.png)

Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)

- The user verifies his wallet.

![Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)](Burrata%20b64a88c90bc94598bfccae66e158c137/Untitled%205.png)

Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)

- After the verification is achieved, he can use his wallet to sign the temporary rental agreement. He signs the rental agreement by PandaDoc (already integrated with Burrata).

![Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)](Burrata%20b64a88c90bc94598bfccae66e158c137/Untitled%206.png)

Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)

- He performs identity verification with Stripe identity which is also integrated with Burrata.

![Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)](Burrata%20b64a88c90bc94598bfccae66e158c137/Untitled%207.png)

Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)

![Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)](Burrata%20b64a88c90bc94598bfccae66e158c137/Untitled%208.png)

Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)

- He signs for allowing Stripe to share the id with the dApp. Then by using [DECO](https://arxiv.org/pdf/1909.00938.pdf) Burrata gets the user’s attributes from Stripe and convinces the dApp that the id is authentic. Burrata forms a verifiable credential and sends it to the chain. From now on the web2 identity and the web3 identity are tied by the Burrata.

![Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)](Burrata%20b64a88c90bc94598bfccae66e158c137/Untitled%209.png)

Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)

- Then, using the credential, the user can mint a rental NFT.

![Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)](Burrata%20b64a88c90bc94598bfccae66e158c137/Untitled%2010.png)

Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)

![Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)](Burrata%20b64a88c90bc94598bfccae66e158c137/Untitled%2011.png)

Source: [https://www.youtube.com/watch?v=eJqZQ2_VBzo](https://www.youtube.com/watch?v=eJqZQ2_VBzo)

After confirming the NFT mint, it is done. (please see the above video for details)

## Supported Chains[](https://docs.burrata.xyz/docs/getting-started/contract-addresses#supported-chains)

As of now (at the time of writing) six blockchains, i.e. Ethereum (Mainnet, Goerli), Arbitrum (Mainnet, Goerli), Avalanche (Mainnet, Fuji), Fantom (Mainnet, Testnet), Optimism (Mainnet, Goerli), Polygon (Mainnet, Mumbai), are supported by Burrata, and two chains, i.e. Near and Solana, will be supported soon. 

Moreover, it is stated in the documents that three more chains (Cosmos, Sui, and Aptos) will be supported in the future.

## Deployed Contracts[](https://docs.burrata.xyz/docs/getting-started/contract-addresses#deployed-contracts)

Burrata uses consistent contract addressing (**same for all chains).** The address of the core Burrata contract is `0x00000000007e47B1524B38602ceae5c7b83E950e`.

## Roadmap and architecture details

One can find Burrata’s roadmap here: [public-roadmap](https://github.com/orgs/burrata-labs/projects/3). Architecture details with open-source nodes will be published [here](https://docs.burrata.xyz/docs/getting-started/protocol-overview) by Q1/2023.

# Detailed analysis

After getting full access to the documentation of Burrata we will analyze the system and compare it to existing web2-web3 identity bridging constructions like CanDID.

# References

- [https://www.burrata.xyz/](https://www.burrata.xyz/)
- [https://docs.burrata.xyz/docs/getting-started/introduction](https://docs.burrata.xyz/docs/getting-started/introduction)
- [https://www.coindesk.com/business/2021/12/09/burrata-raises-775m-from-stripe-variant-to-build-identity-data-bridge/](https://www.coindesk.com/business/2021/12/09/burrata-raises-775m-from-stripe-variant-to-build-identity-data-bridge/)
- [https://www.burrata.xyz/writing/seed-round-announcement](https://www.burrata.xyz/writing/seed-round-announcement)
- [https://github.com/orgs/burrata-labs/projects/3](https://github.com/orgs/burrata-labs/projects/3)
- [https://arxiv.org/pdf/1909.00938.pdf](https://arxiv.org/pdf/1909.00938.pdf)