# Interep (by PSE)

Abstract: Interep provides an Anti-Sybil service. It uses data from Twitter, Github and Reddit to score and classify identities. And later organize these identities in groups based on an entity that provides identities. Serve as a mild tool for creating identities but is not a full solution.
Labels: Implementations, Possible tool in larger solution, Web2 to Web3 data transfer, Worthwile Sybil resistance insights
Link to the paper: https://interep.link/
Score: no idea
Score Phase 1: Very relevant

Interep is an Anti-Sybil as a Service project.

For Interep, reputation is key to building trust in a system and it can often be used as a guarantee of authenticity. 

Giving people the opportunity to export their reputation across platforms (e.g. social networks) without exposing their personal data would expand the compounding benefits of trusted human interactions across the web, while making it much more difficult to create fake accounts.

Interep provides special groups that can be used by DApps or services to verify users' reputations without exposing their identities. Users can join these groups based on their Web2 reputation (e.g Twitter groups) or via other specific user properties. **Interep only checks if the users met the criteria to join the groups, without storing any sensitive data.** In order to join groups each user must create a unique identifier using an Ethereum account and Semaphore. Semaphore, then, allows users to prove that their identifier is part of a specific group.

> Semaphore is a zero-knowledge protocol that allows you to cast a signal (for example, a vote or endorsement) as a provable group member without revealing your identity. Additionally, it provides a simple mechanism to prevent double-signaling. Use cases include private voting, whistleblowing, anonymous DAOs and mixers.
> 

Interep consists mainly of four components:

- **Web application** ([reputation-service](https://github.com/interep-project/reputation-service)): A simple web app to allow users to join or leave groups supported by Interep.
- **APIs** ([reputation-service](https://github.com/interep-project/reputation-service), [subgraph](https://github.com/interep-project/subgraph)): A set of APIs for interacting with Interep. Developers can use them to integrate groups into their applications.
- **Smart contracts** ([contracts](https://github.com/interep-project/contracts)): A set of Solidity smart contracts which allow users to verify their proofs onchain.
- **JS libraries** ([interep.js](https://github.com/interep-project/interep.js)): A monorepo of JavaScript libraries, some used by our backend, and others created to make Interep integration easier.

# Reputation

Calculating reputation is not an easy task, at least as far as social networks are concerned. Some parameters are easier to fake and others do not offer an objective representation of the user's reputation. Our methods try to select the most suitable parameters and calculate a score that falls into one of the following categories (or reputation levels): `gold`, `silver`, `bronze`. Parameters such as `followers`, `likes`, `stars` can then be used to obtain a score that can best represent the authenticity of a user.

## Github parameters

- **Followers**: number of the user's followers;
- **Received stars**: sum of the number of stars received in the user's repositories;
- **Plan**: true if the user has subscribed to a pro plan, false otherwise.

Levels

- Gold
    - Folowers: $\geq 500$
    - recievedStars: $\geq 200$
- Silver
    - Folowers: $\geq 100$
    - recievedStars: $\geq 80$
- Bronze
    - Folowers: $\geq 50$
    - recievedStars: $\geq40$
    - proPlan: $true$

## Reddit parameters

- **Premium subscription**: true if the user has subscribed to a premium plan, false otherwise;
- **Karma**: amount of user's karma;
- **Coins**: amount of user's coins;
- **Linked identities**: number of identities linked to the account (e.g. Twitter, Google).

Levels

- Gold
    - premiumSubscription: $true$
    - karma: $\geq 10000$
    - coins: $\geq 5000$
    - linkedIdentities: $\leq 3$
- Silver
    - karma: $\geq 5000$
    - coins: $\geq 2000$
    - linkedIdentities: $\leq 2$
- Bronze
    - karma: $\geq 1000$
    - coins: $\geq 500$

## Twitter parameters

- **Followers**: number of the user's followers;
- **Botometer overall score**: score obtained with [Botometer](https://botometer.osome.iu.edu/);
- **Verified profile**: true if the user has a verifier profile, false otherwise.

Levels

- Gold
    - verifiedProfile: $true$
    - followers: $\geq 7000$
    - botometerOverallScore: $>1$
- Silver
    - followers: $\geq 2000$
    - botometerOverallScore: $\geq 1.5$
- Bronze
    - followers: $\geq 500$
    - botometerOverallScore: $\geq 2$

# Groups

Groups are sets of users organized in Merkle trees, and users can join this groups based on their reputation. So users  can prove that they belong to a group using zero-knowledge and Semaphore

There are different Group Types, these are defined by identities providers, i.e. the services from which the information necessary to certify a certain reputation or certain properties is obtained.

Interep generate identities with Semaphore, and then a reputation service takes care of adding the commitments in the Merkle tree associated with a certain group.

## OAuth

Users who have Reddit, Twitter or Github accounts can access Interep with OAuth authentication. Interep will then be able to obtain the parameters needed to calculate their reputation on the platform, and depending on this reputation users will be able to join, and then possibly leave, the related Interep groups.

### Flow

1. The user logins to one of our supported OAuth providers and Interep calculates their reputation on that platform;
2. the user connect their Metamask wallet;
3. the user generates an identity commitment for the OAuth provider;
4. the user joins or leaves the group related to their reputation on the platform where they are authenticated.

## POAP

Interep allows POAP badge holders to join groups related to the events of the badges held, in order to allow them to prove anonymously that they participated in an event.

### Flow

1. The user connect the Metamask wallet;
2. if the user has participated in one or more of the events supported by Interep then they can select the event related to the group they wish to join;
3. the user generates an identity commitment for the POAP provider;
4. the user joins the Interep group or leaves it if they have previously joined.

# Semaphore

In order to join a Semaphore group, a user must first create a Semaphore identity. A Semaphore identity contains two values generated with the identity:

- Identity trapdoor
- identity nullifier

A Semaphore group contains identity commitments of group members. Example uses of groups include the following:

- Poll question that attendees join to rate an event.
- Ballot that members join to vote on a proposal.
- Whistleblowers who are verified employees of an organization.

A Semaphore group is an incremental Merkle tree, and group members (i.e., identity commitments) are tree leaves. Semaphore groups set the following tree parameters:

- **Tree depth**: the maximum number of members a group can contain (`max size = 2 ^ tree depth`).
- **Zero value**: the value used to calculate the zero nodes of the incremental Merkle tree.

### Generate a proof off-chain[](https://semaphore.appliedzkp.org/docs/guides/proofs#generate-a-proof-off-chain)

To generate a proof, pass the following properties to the `generateProof` function:

- `identity`: The Semaphore identity of the user broadcasting the signal and generating the proof.
- `group`: The group to which the user belongs.
- `externalNullifier`: The value that prevents double-signaling.
- `signal`: The signal the user wants to send anonymously.
- `snarkArtifacts`: The `zkey` and `wasm` [trusted setup files](https://semaphore.appliedzkp.org/docs/glossary#trusted-setup-files).