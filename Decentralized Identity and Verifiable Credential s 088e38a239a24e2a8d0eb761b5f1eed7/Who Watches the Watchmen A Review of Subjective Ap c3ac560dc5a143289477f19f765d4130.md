# Who Watches the Watchmen? A Review of Subjective Approaches for Sybil-Resistance in Proof of Personhood Protocols

Abstract: Most self-sovereign identity systems consist of strictly objective claims, cryptographically signed by trusted third-party attestors. Lacking protocols in place to account for subjectivity, these systems do not form new sources of legitimacy that can address the central question concerning identity authentication: “Who verifies the verifier?” The legitimacy of claims is instead derived from traditional centralized institutions such as national ID issuers and KYC providers. This architecture has been employed, in part, to safeguard protocols from a vulnerability previously thought to be impossible to address in peer-to-peer identity systems: the Sybil attack, which refers to the abuse of a digital network by creating many illegitimate virtual personas. Inspired by the progress in cryptocurrencies and blockchain technology, there has recently been a surge in networked protocols that make use of subjective inputs such as voting, vouching, and interpreting to arrive at a decentralized and Sybil-resistant consensus for identity. In doing so, these projects illustrate that the best technologies do not abstract away subjectivity but instead embrace it as a necessity and strength. In this review, we will outline the approaches of these new and natively digital sources of authentication—their attributes, methodologies, strengths, and weaknesses—and sketch out possible directions for future developments.
Actions needed and questions: @Jorge Arce-Garro it may provide some discussion on Sybil resistance
Added to deliverable?: No
Already read?: No
Assigned readers: Isaac Villalobos Gutiérrez
Date of publication: 2020
Link to the paper: https://www.frontiersin.org/articles/10.3389/fbloc.2020.590171/full
MZ checked the note: No
Presentation date: November 23, 2022
Reviewers: Jorge Arce-Garro
Score Phase 1: Relevant

A system must ensure that every Identity within their domain archives

1. A unique identifier
2. Sybil-resistance
3. Self-sovereignty
4. Privacy-preserving

The last three points correspond to the "Decentralized Identity Trilema," and protocol tries to achieve each of these to a certain degree.

To achieve the components of the Trilema, some properties are to be kept in mind.

- Subjective substrate:
    - Some form of "human entropy" is a substitute for work and/or financial capabilities. e.g., interacting with others or interpreting something.
    - We look at stuff that is easy for humans but difficult for AI. Also, it needs to be easy for humans to produce once but not twice or more.
    - And involve minimal to zero personal information.
- Objective incentive:
    - An incentive for nodes to join the network.
    - The incentive must be such that it is more valuable to be a legitimate identity rather than a fake one.

# Primary Properties of PoP

- Decentralization
- Privacy preservation: anonymity, pseudonymity, unlinkability, unobservability, and plausible deniability.
- Scalability
    - Provide service to a significant fraction of the global population
    - Low bar of entry in technical, financial, and physical aspects

# Primitives of PoP

## Reverse Turing tests

A common practice is to use CAPTCHAs to differentiate between humans and AI, but at the same time, these are used to train AIs. So a solution by the Idena Network is that the images and tests must not be created algorithmically but rather by humans.

The tests created by Idena aims for AI-hard test that requires common-sense reasoning and is based on visual representation(Like forming a logical story from a set of pictures). These tests are called FLIPs; humans are accurate 95% of the time, while AI is only 60-76% accurate.

Other approaches aim for reasoning over a text,s but these fail in a standard for the globe because of language limitations.

However, the above fails at humans not being able to reproduce another test for a second time, i.e., no Sybil resistance from humans. To solve these, some protocol implement elements from Pseudonymity Parties.

## Pseudonymity Parties

"Real humans can only be in one place at one time."

Authentication comes from being physically present at a specific place and time. Attendees formalize procedures to register their presence, such as scanning each other's QR codes and, with these, generating anonymous credentials, which can be used to establish membership in an online community. This might work as long as hyper-realistic deep fakes are not available.

The engagement of physical authentication to synchronize the nodes is an apparent downside of this method.

## Web of Trust

The Web of Trust consists of users validating each other's certificates of Identity. The Web of Trust relies on the fact that although an attacker can create multiple identities, these are not validated by a trusted node, thus separating the Sybil from non-Sybil into discrete sets.

The above fails if the Sybil identities numbers are much more significant, so using a reputation system may reinforce a Web of Trust system.

SybilRank is a project with some success that aims at identifying fake accounts within bounded social media networks.

"However, it is unlikely that widely used social media networks are good candidates for large-scale identity approaches, particularly for sensitive applications like civic engagement. This is due not only to the ease with which attackers can create false "nodes" with real relationships and connections to other nodes but also because re-orienting an identity program around privately owned and centralized social network platforms are antithetical to the project of self-sovereign identity solutions."

The problems with this approach include the following: A combination of different claims and credentials may not entirely guarantee Sybil-resistance, levels of trust cannot be easily quantified, and only first-degree relationships can be trusted.

## Intersectional Identity

Intersectional Identity is a framework that closes the gap between formal verification methods and the informal mechanisms used to check the validity of identity-related claims.

Usually, these expand the Web of Trust schemes by adding accountable markers such as name or GPS history.

Sybil-resistance is achieved by taking into account the properties of Identity laid out in classical sociology by Georg Simmel: Sociality, Intersectionality, and Redundancy.

Sociality means that aspects of Identity are shared. Intersectionality means that no individual or group can serve as a central reference for identity verification. Redundancy means that the uniqueness of an individual is over-determined by the countless unique intersections of groups or sources of trust by which each person finds themselves through life.

Thus, Sybil resistance can be achieved by keeping track of a few characteristics and their intersectionalities(characteristics can be privacy-preserving).

A paper detailing this method can be found at [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3375436](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3375436)

## Token Curated Registries

In TCR, members hold a token that may increase in value if they are able to maintain quality, legitimacy, or popularity, in turn attracting new applicants to add their data to the network. Trust can be established by staking, voting, or vouching.

# Existing Efforts

## Idena Network

The idea Network has its blockchain managed by a proof-of-person consensus, with every node having an identity with equal voting power. Idena achieves Sybil-resistance by using the reverse Turing test and incorporating elements of a virtual pseudonymity party.

Participants join the network by simultaneously participating in live ceremonies, solving FLIPs tests, and creating more FLIPs. The frequency of the ceremonies depends on the size of the network. However, Sybil-resistance has a small probability of error given that a person could solve multiple FLIPs within the timeframe for these.

As an additional layer of security, Idena asks newcomers for an invite from an existing member. Also, As an incentive, Idena provides a Universal Basic Income(currently $50-60 a month), provided that members successfully attend and solve the FLIP tests.

Sybil-resistance effectiveness against advanced neural networks remains to be seen.

## Humanity DAO

Members of Humanity DAO evaluate candidates' legitimacy through consensus voting and uses TRC for PoP. The following steps run the protocol:

1. Applicants request to join the list using social media information.
2. Applicants stake a fee on their candidacy and are lost if the applicant is rejected.
3. Members vote based on their social media profiles and are incentivized to curate the list of members.

The Humanity DAO gives a Universal Social Income of 2500DAI at a rate of 1DAI per month.

The project was terminated in Jan 2020 due to attacks that changed the smart contract and prohibited it from joining the DAO.

## Kleros

An Ethereum-based protocol for dispute resolution, the project's success led to "Proof of Humanity": A TCR, Web of Trust solution that requests photos, videos, and bios for evaluation.

Each vouching is accompanied by a financial stake that serves as a bounty for other members to identify false positives and later be removed from the network.

Although proof of personhood works, it relies on subministrating personal data like biometrics.

## Upala

An Ethereum-based protocol uses verification groups that assign scores to each member. This score is related to a certain amount of currency deposited in a pool that is available for stealing. The act of stealing implies a "bot explosion," which immediately deletes the Identity.

This utilizes the concept of social responsibility, where groups are incentivized to develop efficient approval mechanisms, leading to highly trusted members.

This generates a market for identity authentication where groups try to maximize the number of users and deposits. On the other side, users are trying to get the highest scores for the lowest investment of reputation and money.

[approval mechanism and ROI in the pool? not explained in the paper, review Upala's docs [https://www.notion.so/How-Upala-works-79bd03181dc045009e727bc902a8835b](https://www.notion.so/How-Upala-works-79bd03181dc045009e727bc902a8835b)

[https://www.youtube.com/watch?v=9ekWCMQcdbc](https://www.youtube.com/watch?v=9ekWCMQcdbc) [https://docs.upala.id/_/downloads/en/latest/pdf/](https://docs.upala.id/_/downloads/en/latest/pdf/)]

## BrightID

## Duniter

Formally called uCoin, Duniter is a technical implementation of the relative theory of money of St\’ephane Laborde, where a Universal Dividend is described as having its value relative to its monetary mass.

Duniter has its blockchain that can mint G1 cryptocurrency as a Universal Dividend, and authentication is performed using a Web of Trust scheme.

To join the network, applicants are vouched for by five existing members. Vouching is only possible if the members contact the applicant on the physical plane or if they can contact the applicant through different channels remotely.

When joining a newcomer is giving(or generating?) a new key pair, newcomers must be at a maximum distance of five connections from the referent members.

A graph property defines referent members that mimic trust parameters in the real world.

The requirements above imply that emitting a new certification takes time, allowing the network to monitor for attacks manually.