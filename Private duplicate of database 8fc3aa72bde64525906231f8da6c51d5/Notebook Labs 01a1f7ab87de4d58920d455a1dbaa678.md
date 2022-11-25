# Notebook Labs

Abstract: This technical whitepaper presents Notebook, a novel protocol for Sybil-resistant log-in and credential aggregation that preserves user anonymity. Notebook provides users with a set of fragmented identities with the following properties: with each identity, users can prove they are a human; the identities are detatched from one another; the identities are detatched from the user’s real-world identity; credentials can be aggregated across identities and each human only receives a single set of fragmented identities. This set of properties has many applications in fully anonymous credit scoring and governance. This paper also details an implementation of Notebook using the Circom and Solidity languages on the Ethereum Virtual Machine.
Classification: Data to Web3
Labels: Credential sharing prevention, Data to Web3, Decentralized identity, Self-sovereign identity, Web2 to Web3 data transfer
Link to the paper: https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf
Score: no idea
Score Phase 1: Very relevant

# Notebook Labs

## The Problem…

…is very similar to ours: creating a self-sovereign identity protocol with Sybil-resistant login and credential aggregation. 

## The Promise

Notebook fragments the identity of its users, and claims to be able to solve the following 5 key points:

1. Any fragment can be used to prove that a user is human.
2. Unless the user’s secret key is leaked, no fragment can be linked to another.
3. It is impossible to link a fragment to a real-world identity.
4. Credentials can be aggregated.
5. Each human can receive at most one set of fragmented identities. 

At a high-level, 1. is completeness, 2. is unlinkability, 3. is privacy, 4. is credential aggregation and 5. is Sybil-resistance. 

## Sybil resistance

Unfortunately it seems that the way that they plan to solve this problem is by going the  opposite way: relying on trusted third-parties **and** on a trusted entity that can make the link between private personal information and a user’s wallet. This seems like a usual Web2/real world KYC procedure. Here is their diagram for getting a KYC credential signed:

![Source: [https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf](https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf)](Notebook%20Labs%2001a1f7ab87de4d58920d455a1dbaa678/Capture_decran_2022-11-16_a_10.52.29.png)

Source: [https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf](https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf)

Initially, they say, the Compliance Entity (CE) will be the Notebook team, and that they aim to make it decentralized in the future. The idea is that the KYC third party knows the link between the PII and the hash of the PII, while the CE knows the link between the hashed PII and the wallet address using the KYC credential. 

There is no mention of:

1. How to get credentials on the platform. In the diagram it seems like a simplistic approach, we have seen protocols like DECO where we would need an interaction between all three parties in the diagram. It is mentioned that the CE and the KYC Third Party should collude, but it is not specified how. 
2. Any idea how to decentralize the Compliance Entity. 
3. How to design the unique KYC ID. 

Each time a users successfully creates a KYC credential, they publish a hash of it together with the protocol’s address, on a single *SSI Merkle tree* of depth 36. This tree is shared by all users. There is also a way to prove one holds a certain KYC credential, essentially by proving ownership over a leaf in the tree:

![Source: [https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf](https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf)](Notebook%20Labs%2001a1f7ab87de4d58920d455a1dbaa678/Capture_decran_2022-11-16_a_10.53.12.png)

Source: [https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf](https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf)

## Adding a credential

One can also add self-sovereign credentials, though we would need some further information on how these might be used for authentication with actual protocols in the ecosystem. 

![Source: [https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf](https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf)](Notebook%20Labs%2001a1f7ab87de4d58920d455a1dbaa678/Capture_decran_2022-11-16_a_10.51.52.png)

Source: [https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf](https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf)

![Source: [https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf](https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf)](Notebook%20Labs%2001a1f7ab87de4d58920d455a1dbaa678/Capture_decran_2022-11-16_a_10.52.13.png)

Source: [https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf](https://assets.website-files.com/635b21dddd46c8cddf2171fd/635b21dddd46c8be9021722c_Notebook_Whitepaper.pdf)

## How to combine score

Aggregation of credentials allows for accountability. 

The identity of users is fragmented into four pieces, all of which have different wallet addresses ($H(sk||1), \dots, H(sk||4)$). This protects users from having their activity linked with their real-world identity. Each four of these fragments are associated to four scores:

- Fraud flag - this boolean value signifies whether the identity was reported for being part of some fraud (like operating a pump-and-dump scheme).
- DAO score - this represents the activity and contributions of a user in decentralized governance.
- Social Reputation - this is a value which represents a user’s engagement in communities and forums. A high score would signify meaningful participation, whereas a lower score may demonstrate that a user harmed the communities they were a member of.
- Credit Score - this reflects a user’s engagement in DeFi.

Unfortunately there is no mention of how one might construct these scores. Essentially these four “scores” represent four additional Merke trees of depth 256, storing users’ scores in each category in the index corresponding to their identities. When interacting with a protocol, users may give permission to write to one of these trees. But because the user has four identities, there needs to be a way to link activity across all boards. This is supposedly done in the following way:

$$
ZK-SNARK(sk, r, H(sk||r),\pi_{Sybil}, O_1, \pi_1, O_2,\pi_2, O_3, \pi_3, O_4, \pi_4)
$$

Here $(O_i,π_i)$ is an opening and its proof for a leaf of the Merkle Tree. We must do an opening for each identity. Here we need the following inputs  $(sk, L, π_{Sybil}, O_i, π_i)$ to be secret. Otherwise, it would be possible for a malicious actor monitoring the execution of the contract to link the identities together. It is unclear what $r$  is. 

Also $\pi_{Sybil}$ is an opening for $H(sk||r)$ in the ************Sybil tree.************ Unfortunately there is no mention of the Sybil tree and its leaves, or how it interacts with users. The same holds true for the *permission tree* a bit later. 

## Assessment

The project seems to be a concept rather than a complete protocol. We think there are interesting ideas but the hardest problems are yet to be solved: namely the transfer of trustworthy data off-chain→on-chain, the decentralization of the Compliance Entity, and a proof of Sybil-resistance. Could it be that the whitepaper is WIP? We mark the paper as relevant since, if solved, some of the problems mentioned in this paper are directly related to ours.