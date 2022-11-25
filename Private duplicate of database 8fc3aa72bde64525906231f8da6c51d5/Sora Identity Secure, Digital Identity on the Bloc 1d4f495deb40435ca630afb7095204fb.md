# Sora Identity: Secure, Digital Identity on the Blockchain

Abstract: Digital identity is the cornerstone of a digital economy. However, proving identity remotely is difficult to do. To complicate things further, identity is usually not a global, absolute construct, but the information shared with different parties differs, based on the relationship to the user. Therefore, a viable solution for digital identity should enable users to have full control over their personal information and share only the information that they wish to share with each service. Blockchain technology can help to realize a self-sovereign identity that puts the user in control of her information, by enabling a decentralized way to handle public key infrastructure. In the current contribution, we present the Sora identity system, which is a mobile app that utilizes blockchain technology to create a secure protocol for storing encrypted personal information, as well as sharing verifiable claims about personal information.
Classification: DI, VC
Link to the paper: https://ieeexplore.ieee.org/document/8377927
Score: no idea
Score Phase 1: Relevant
Year: 2018

# I. Introduction

- Uses blockchain technology to augment current solutions for identity management.
- Security increased by decentralizing the structure of the system.
- Cryptography gives users control over their own data.

# II. Related work:

- First, there was public-key infrastructure (PKI). Relies on centralized certificate authorities.
- Then an alternative appeared: self-sovereign identity.
- “(…) the same technology that allows any participant in a blockchain network to verify data in the blockchain also allows the verification of other data, such as verifiable claims about identity.
- “Providing claims about users in a blockchain system functions as a notary, only instead of having designated authorities providing notarization, anyone can sign data and anyone can choose which data signatories they wish to trust.”
- In the present contribution, we propose to use key-value stores that are encrypted with a cryptographic key that is owned by the user, and hashes of the values of personal information are salted and put into a blockchain platform. The Sora mobile apps allow the user to generate their cryptographic key, input their data, encrypt it, and publish salted hashes of their data to the blockchain. Users can then share their personal information of their own volition to institutions, such as banks or other corporations, and those institutions can, in turn, cryptographically sign hashes of salted personal information, thus acting as a notary.

# III. Motivating example

- User $U$ uses Sora to manage their identity. They enter their personal info into Sora, which is then salted, digitally signed, and uploaded to a blockchain.
- They share their personal information with an institution $I$, who digitally signs a salted hash of the information and publishes the hash and signature to the blockchain. Now $I$ has seen $U$’s data and attests to its validity.

From the paper:

> In this example, the Sora identity mobile app works to realize a self-sovereign digital identity solution by giving the user, $U$, control over their personal data, as the user can encrypt their data and send it to an institution themselves. Once information is shared, institutions can then notarize the personal information by putting signed hashes on the blockchain. These digitally signed hashes can then form the basis for verifiable claims of identity.
> 

> Another example includes an issuer $I$, a user $U$, and a verifier V . I is able to create verifiable claims of any kind (issue document, health record, and many more) about $U$ without disclosing their contents by uploading signed salted hashes to a blockchain. $U$ can then share claims with $V$, which can cryptographically verify their content.
> 

# IV. Sora identity protocol

Main actors:

- User
- Mobile device
- Central server
- A blockchain (e.g. Hyperledger Iroha)

Every user has a unique DID pointing to a DID document on a decentralized DID resolver.

A user’s identity (including private information) can be seen as a set of key-value pairs. E.g. `key=birthday, value=01/01/1962`. Each of these is stored on a central server in encrypted form.

Any user with a DID is able to submit a verifiable claim about themselves or other users. The verifiable claim is split into two parts:

- Public: it is stored on the blockchain and consists of salted hashes of the claims themselves, a digital signature, and information about issuer
- Private: shared with the verifier, when requested.

For example, a user may issue 5 claims, one for every passport field, and combine them into a single verifiable claim. If a Verifier needs only the birth date, the Prover (claim subject) can provide only one, corresponding claim, and the Verifier can simply calculate the hash and make the hash lookup on a public part of claim. The Verifier can also add a signature to the public part of the claim thus attesting to its validity.

### Identity sharing and notarization

An example:

1. A publishes a verifiable claim on the blockchain.
2. B requests a certain attribute of digital identity.
3. A shares a preimage of the hash with the claim.
4. B calculates the hash and compares it with one of the hashes from the verifiable claim, found on a blockchain.
5. If a hash matches, the signature is valid, and the verifiable claim has not been revoked, identity is verified.

User B can then “notarize” this claim by creating a signature for this Verifiable Claim. The signature can be sent back to the user A, who publishes it to her account.

---

# Final remarks

- Note that the paper is from 2018. Looking at [Soramitsu’s webpage](https://soramitsu.co.jp/), we see that this self-sovereign identity solution was tested with BCA, an Asian financial group, in 2019. The solution has not seen much more public exposure since. [https://www.newswire.com/news/applications-of-soramitsus-sora-platform-and-hyperledger-iroha-for-20902012](https://www.newswire.com/news/applications-of-soramitsus-sora-platform-and-hyperledger-iroha-for-20902012)
- Also note how the solution ultimately depends on permissioned authorities working as issuers/verifiers on behalf of other users.