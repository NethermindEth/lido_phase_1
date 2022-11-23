# Decentralized Identity on Tezos

Abstract: Tezos is an open-source blockchain protocol that has a formalized process for upgrades and uses a virtual machine language called Michelson, which is designed to support formal verification using proof assistants. It can be used for DID creation and management compatible with the issuance, storage, and verification of Verifiable Credentials, achieving a pragmatic balance across privacy, decentralization, and accessibility for general purpose use in Internet scale consumer and B2B applications.
Actions needed and questions: @Aikaterini-Panagiota Stouka I think that may be very relevant, what do you think? @Michal Zajac it seems that they do not prevent Sybil attacks, because they say that it is important that each entity to can have different DID to use for different use cases. However it is important they use Ethereum accounts for DID. Maybe I can present it (after my scheduled presentations) the same day with Sora because I have not found yet much documentation. I changed it to relevant.

@Aikaterini-Panagiota Stouka do they discuss how to get Web2/real-life data to Web3? 

@Aikaterini-Panagiota Stouka please provide an abstract
Added to deliverable?: No
Already read?: Yes
Assigned readers: Jorge Arce-Garro
BS factor: N/A
Classification: DI
Labels: Cryptographic primitive (Anonymous Credential), Decentralized Issuer, Implementations, Management of credentials, Not Sybil resistant, Standardization efforts
Link to the paper: https://did-tezos.spruceid.com/
MZ checked the note: No
Presentation date: November 17, 2022
Reviewers: Ahmet Ramazan Agirtas
Score Phase 1: Maybe relevant
Work Group: Blockchain projects, Hybrid

This paper is an implementation of a DID method (that is, an instance of the DID standard with all the relevant functions) on the Tezos blockchain. See [W3C’s ****Decentralized Identifiers data model v1.0****](W3C%E2%80%99s%20Decentralized%20Identifiers%20data%20model%20v1%200%20f6b6cebed5644423a89829cf10b7a6f7.md) for the relevant background. 

As it is usual with DID implementations, we have no native Sybil-resistance mechanism.

Project led by SpruceId.

**Important: This implementation seems deprecated**. It relies on TZIP-19, which [has been withdrawn](https://tzip.tezosagora.org/proposal/tzip-19/). Furthermore, this document—an unofficial draft—[has not been updated since March 2021.](https://github.com/spruceid/did-tezos/blob/main/index.html)

Regardless—and as a practical exercise in understanding the DID standard—, let us point out the general features behind this implementation.

---

# Introduction

We seek to specify a DID method with pragmatic trade-offs across privacy, decentralization, and accessibility, suitable for use in Internet scale consumer and B2B applications. To accomplish this, the DID method resolves across tiered layers of data storage, each with different characteristics, but all at the ultimate control of the user.

### Why Tezos?

- Public and highly available
- Permissionless
- Censorship resistant
- Upgradable
- Up to date (60s block time)

These are all relatively common features of a quality blockchain. But we also have:

- Formally verifiable: Michelson, the virtual machine language used by Tezos, is designed to facilitate formal verification using proof assistant frameworks, such as Mi-Cho-Coq. It is possible to formally verify some properties of software used for DID management, or even to create a full specification.

# An example

`did:tz:tz1TzrmTBSuiVHV2VfMnGRMYvTEPCP42oSM8`

tz, in lowercase, is the DID method. The method-specific identifier may begin with tz1, tz2, or tz3 (in which case they refer to user accounts of different types) or KT1 (in which case they refer to a smart contract).

# Architecture

![Untitled](Decentralized%20Identity%20on%20Tezos%2064aeb7e899dc43d389d760d3f35baf5b/Untitled.png)

(Source: current paper)

DID resolution occurs sequentially across the following ordered layers of data sources, known as resolution layers:

1. Implied DID Document.
2. Corresponding on-chain smart contract known as a DID Manager.
3. Corresponding off-chain DID document signed updates.

DID resolvers must move sequentially through all resolution layers to incrementally build a DID document, and they fail upon the first encountered inconsistency, producing an error result and no DID document. Success can only be achieved after processing all resolution layers.

Let us describe all three layers:

### First layer: implied DID document

For Tezos account address-based DIDs with addresses starting with`tz1`, `tz2`, or `tz3`, DID document resolution is possible without committing any Tezos blockchain transactions to preserve privacy and save costs. Because all `mainnet` blockchain transactions are public, immutable, and fee-based, it is recommended to exercise extreme caution and store the absolute minimum amount of information on-chain.

An example:

```json
{
  "@context": "https://www.w3.org/ns/did/v1",
  "id": "did:tz:mainnet:tz1TzrmTBSuiVHV2VfMnGRMYvTEPCP42oSM8",
  "authentication": [{
    "id": "did:tz:mainnet:tz1TzrmTBSuiVHV2VfMnGRMYvTEPCP42oSM8#blockchainAccountId",
    "type": "Ed25519PublicKeyBLAKE2BDigestSize20Base58CheckEncoded2021",
    "controller": "did:tz:mainnet:tz1TzrmTBSuiVHV2VfMnGRMYvTEPCP42oSM8",
    "blockchainAccountId": "tz1TzrmTBSuiVHV2VfMnGRMYvTEPCP42oSM8@tezos:mainnet"
  }]
}
```

### Second layer: DID managers

DID Managers are smart contracts on the Tezos blockchain that implement TZIP-19. That is, they implement DID authentication methods and point to service endpoints. 

**What are these service endpoints?** They correspond to the `service` property in a DID document. From the DID specification:

> [Services](https://www.w3.org/TR/did-core/#dfn-service) are used in [DID documents](https://www.w3.org/TR/did-core/#dfn-did-documents) to express ways of communicating with the [DID subject](https://www.w3.org/TR/did-core/#dfn-did-subjects) or associated entities. A [service](https://www.w3.org/TR/did-core/#dfn-service) can be any type of service the [DID subject](https://www.w3.org/TR/did-core/#dfn-did-subjects) wants to advertise, including [decentralized identity management](https://www.w3.org/TR/did-core/#dfn-decentralized-identity-management) services for further discovery, authentication, authorization, or interaction.
> 

> Due to privacy concerns, revealing public information through [services](https://www.w3.org/TR/did-core/#dfn-service),
such as social media accounts, personal websites, and email addresses, is discouraged.
> 

**Note: One smart contract must be deployed per DID.** 

**Account address-based DIDs**: In the case of an account address, the DID Manager smart contract is defined as the first smart contract that (1) is deployed by the account and (2) implements TZIP-19. 

**Smart contract address-based DIDs**: In the case of a smart contract address, the smart contract itself is the DID Manager, and must therefore implement TZIP-19. If it does not implement TZIP-19, then resolution will fail.

### Third layer: off-chain updated DID

Off-chain updates to the DID document are possible by specifying one or more signed patches in the DID resolution input metadata property named `updates` containing an array. If updates are present, they must all be of the same type.

The two allowed types for updates are (1) unsigned Tezos transactions with valid `RotationSignature` parameter values that would correctly update the DID Manager if signed and cleared in a block and (2)`[signed-ietf-json-patch](https://github.com/decentralized-identity/did-spec-extensions/blob/master/parameters/signed-ietf-json-patch.md)`restricted to changes possible through the DID Manager abstract function interface. These two types of updates have different privacy and security implications.

# Operations

This standard implements the usual CRUD operations (create, read or resolve, update, delete).