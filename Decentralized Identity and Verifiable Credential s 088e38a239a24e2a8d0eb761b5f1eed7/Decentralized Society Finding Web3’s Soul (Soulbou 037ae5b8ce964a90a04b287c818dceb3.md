# Decentralized Society: Finding Web3’s Soul (Soulbound tokens)

Abstract: Web3 today centers around expressing transferable, financialized assets, rather than encoding social relationships of trust. Yet many core economic activities—such as uncollateralized lending and building personal brands—are built on persistent, non-transferable relationships. In this paper, we illustrate how non-transferable “soulbound” tokens (SBTs) representing the commitments, credentials, and affiliations of “Souls” can encode the trust networks of the real economy to establish provenance and reputation. More importantly, SBTs enable other applications of increasing ambition, such as community wallet recovery, sybil-resistant governance, mechanisms for decentralization, and novel markets with decomposable, shared rights. We call this richer, pluralistic ecosystem “Decentralized Society” (DeSoc)—a co-determined sociality, where Souls and communities come together bottom-up, as emergent properties of each other to co-create plural network goods and intelligences, at a range of scales. Key to this sociality is decomposable property rights and enhanced governance mechanisms—such as quadratic funding discounted by correlation scores—that reward trust and cooperation while protecting networks from capture, extraction, and domination. With such augmented sociality, web3 can eschew today’s hyper-financialization in favor of a more transformative, pluralist future of increasing returns across social distance.
Added to deliverable?: No
Already read?: No
BS factor: solid
Classification: DI
Link to the paper: https://papers.ssrn.com/sol3/Delivery.cfm/SSRN_ID4105763_code1186331.pdf?abstractid=4105763&mirid=1
MZ checked the note: No
Reviewers: Jorge Arce-Garro
Score Phase 1: Relevant
Work Group: Hybrid

## Soulbound Tokens

1. Web3 concentrates mainly on the asset transfer, instead of encoding social relationships.
2. Uncollateralized lending and building personal brands are built on social relationships.
3. To address this - SoulBound Tokens (SBTs) have been proposed. SBTs would be used to represent social identity and this would solve the issues in web3 around wealth concentration and vulnerability to financial attacks. SBTs would also lead to numerous applications which would pave the way to what would be called a "Decentralised Society".

## Souls

Souls are wallets or accounts that hold publicly visible, non-transferable tokens. The tokens held by Souls are known as SoulBound Tokens (SBTs). Note that they have talked about Souls being publicly visible (unlike the case of DIDs).

Tokens - (i) can be self attested by the soul itself; (ii) can be attested by other souls which makes the SBTs more credible. (A university can be a soul that issues tokens to graduates. This is like the issuers and holders as in the case of VCs).

## Stairway to DeSoc

### Arts and Souls

Souls are the natural way for artists to stake their reputations on their works. When trading a tradeable NFT, an artist would be able to issue the NFT from their Soul. The more SBTs the artist’s Soul carries, the easier it becomes for the buyers to know that the Soul belongs to the artist and thus, confirm that the NFT is legitimate. To improve this, an artist can create a linker SBT that would associate all the NFTs issued by the artist.

With the progress in the deep fake technology, it would keep getting more difficult systems for evaluating legitimacy of various entities. While blockchain keeps a track of time when a token was made, SBTs would enable tracking of the social provenance. Thus, SBTs provide us the social picture of a soul. Blockchain together with SBTs would help in preventing “Deep Fakes” as we would know when actually the token originated and we would also know the social context of the token issuer. 

### Soul Lending

web3 cannot replicate uncollateralized lending because all assets are transferable and saleable. Traditional financial systems support many forms of uncollateralized lending but they depend upon centralized credit scores to evaluate the creditworthiness of borrowers. 

An ecosystem of SBTs could unlock a censorship-resistant, bottom-up alternative to top-down
commercial and “social” credit systems. For example, SBTs representing the education history, work history, and rental contracts could serve as a persistent record of credit-relevant history. Loans and credit lines can be represented a s non-transferable but revocable SBTs which can be burnt once they have been repaid. SBTs can provide many other security properties: (i) non-transferability - prevents transferring or hiding loans; (ii) a rich ecosystem of SBTs would prevent borrowers from escaping their loans because bringing up a new Soul would hamper their reputation.

SBTs can bring about open-sourcing of the lending markets. SBTs would enable lending within social connections. SBTs would offer a substrate for lending practices where members of a social network to support one another’s liabilities. The idea is that a Soul’s constellation would have multiple connections and this would enable a Soul to find multiple co-participants for lending.

How it would start? - Souls would have SBTs that would contain information, which a Soul is comfortable to share publicly. This information would be limited in scope but this can certainly kickstart lending as this can make the information within SBTs credible.

### Not Losing Your Soul

There are some key SBTs which are unique to a user and a Soul would not want to lose them. Therefore, not losing a soul becomes very important in the design of SBTs.

1. Possible ways - multi-signature recovery, mnemonics, social recovery (relies on a person’s relationships)
2. Social recovery - A user curates a set of “guardians'' and gives them the power, by majority, to change the keys of their wallet. However, relationships may get sour, or guardians may pass away. Guardians can be a mix of individuals, institutions or other wallets. Firstly, a user must maintain an optimum number of guardians so that the guardians aren’t entirely discrete and neither should they be small enough to collude. Therefore, the user must make efforts maintain healthy relationships with all of them. 
3. Solution - Community Recovery - tie Soul recovery to a soul’s involvement in communities instead of curating. The relationships over time will be the factor which would decide the guardians for the souls. However the issue with this mechanism is that the communication between users occurs on two scales - off-chain and on-chain. To build a community of guardians, we need a community that encompasses individuals from both the categories. Like social recovery, it is assumed Soul has access to secure, off-chain communications (such as conversation, meeting in person, or confirming a shared secret) which require greater bandwidth.

Community recovery emerges from the idea that individuality emerges from the intersection of communities just as communities emerge from the intersection of individuals. By integrating security in sociality, a Soul can regenerate their keys through community recovery.

### Souldrops

SBTs can portray their individualities and reflect their unique traits as they acquire SBTs from various aspects. Such individuation helps to build reputation and identity aco The idea here is to instead of dropping of SBTs among random nodes in the network, the tokens are “airdropped” to souls that satisfy some conditions in SBTs. This can lead to novel incentive mechanism that lead to community engagements.

### DAO of Souls

Current architecture of DAOs can have instances of sybil attacks. This can eventually lead to 51% attacks. SBTs can help mitigate the chances of sybil attacks in multiple ways:

1. Computing over a Soul’s set of SBTs to differentiate between unique souls and sybils
2. Giving more power to those souls which have reputable SBTs
3. Issuing specialized proof-of-personhoods SBTs
4. Checking for correlations between SBTs held by Souls who support a particular vote, and applying a lower vote weight to voters who are highly correlated

The last idea is novel. The last case can be a Sybil attack or a vote from a group of Souls sharing the same bias or making the same error in the judgement. Therefore, such a vote must be weighted mush less.

DAOs can use SBTs to prevent forms of strategic behaviors such as vampire attacks. DAOs can also use SBTs to make leadership and governance programmatively responsive to their communities.

### Measuring Decentralization through Pluralism

It is important to evaluate how decentralized an ecosystem is. Two popular decentralization metrics are:

- Nakamoto coefficient: This measures how many distinct entities need to be combined to gather 51% of some resource
- Herfindahl-Hirschman index: This is for measuring market concentration of antitrust purposes and it is calculated by summing the squares of the market shares of the market participants.

However, there are open key questions with these two parameters: what are the correct resources to measure, how to deal with partial coordination and the question about what constitutes a “distinct entity”.

The methods proposed for measuring decentralization/pluralism in a DAO, protocol, or network are:

1. Protocol can limit token voting to reasonably sybil-resistant (SBT rich) Souls.
2. Protocol can evaluate the correlations between SBTs held by different Souls and discount votes if they share a large number of SBTs.
3. Protocol can measure the correlations between SBTs held by Souls among and across different layers of network stack.

This would enable the measurement of the decentralization of an interoperating and layered ecosystem. However, the formulas and models need to be exacted. This would also require a concrete definition of relationships of SBTs.

### Plural Property

Till now, web3 has mainly consisted of entities which are wholly transferable: tokens, NFTs, artworks, etc. Due to this reason, web3 has failed to represent the simplest and ubiquitous property contracts. Therefore, SBTs will help to attain the flexibility to bring up various property rights in the forthcoming systems. Few examples are:

- **Permissioning access** to privately or publicly controlled resources. Note that using transferable NFTs is not same as this.
- **Data Cooperatives** where different access rights is given to different sections of society.
- **Experiments with local currencies** with rules that make them more valuable to hold and spend those tokens by Souls who live in a particular area.
- **Experiments in participation** where SBTs create a platform for less contextualized Souls (such as immigrants, adolescents) to gain influence within novel and broader networks.

### From Private and Public Goods to Plural Network Goods

SBTs would enable management of assets that are between being fully private and fully public. The current infrastructure either assumes selfish agents without pre-existing cooperation, at best and intentional collusion, at worst, by groups who are already cooperating. In such a scenario, funding models such as Quadratic Funding can’t scale.

For this scenario, SBTs would encourage cooperation across different communities so as to support diversity. This in turn would depict a broader interest across networks and this would be done by evaluated using shared SBTs. This would also bring up discounting the pre-existng cooperation and quadratically scale up plural goods that confer benefits widely across emergent networks - agreed upon by the most diverse members.

## Plural Sensemaking

AI - working with data feeds and synthesizing them into predictions through proprietary large-scale, non-linear models.
Prediction - people bet on outcome in the hopes of financial gains relying entirely on financial gains

SBT’s paradigm - get the best out of both the models - combine non-linear AI models with the market incentives of prediction markets to convert the data laborers to active data creator.

### Prediction Markets to Prediction Plurality

1. Current design - survival of the fittest - gain of one leads to loss of another - this is not desirable
2. Prediction market has been attached to the people who are prone to gambling and where the winner takes all and the rest of them suffer. 
3. Solution - sophisticated team prediction polling where people have incentives to share information. Members can be weighted based on various factors like past performance and peer evaluation, and then the team works collectively to better decisions.

### Artificial Intelligence to Plural Intelligence

Large scale non-linear neural network models can also be transformed by SBTs. Such models require large amount of data aggregated by people. Thus, data creators are not incentivized for doing this. SBTs would enable economic incentives for provenance-rich data while providing data creators with residual governance rights over their data. In addition, SBTs can also bring about cooperation among data creators to create better data sources. This would lead to explosively constructed plural intelligences rooted in social provenance and governed by Souls.

Therefore, the convergence of prediction market and AI paradigms to form a plural sense-making. This would lead to distributed incentives and careful tracking of social context to create a diversity of models.

### Programmable Plural Privacy

Plural intelligence raises the question about data privacy because building powerful models would require pooling of sensitive data. Self-sovereign identity treats data as private property. However, the issue is not actually the data privacy. Rather it is the lack of integrity to context in the sharing of information.

Instead, the authors of SBTs have proposed that privacy should be treated as “a programmable, loosely coupled bundle of rights to permission access, alter or profit from information”. In this design, every SBT would represent a credential or access to a data store.  

## Decentralized Society

<aside>
💡 “Decentralized Society (DeSoc)”: a co-determined sociality, where Souls and Communities convene bottom-up, as emergent properties of each other to produce plural network goods across different scales.

</aside>

Plural network goods have been emphasized as a feature of DeSoc because networks are the main source of economic growth, ye the most susceptible to dystopian capture by private actors and powerful governments. Most significant economic growth is possible when there is increasing network returns. The greatest strength of DeSoc is its network composability - enabling growth of all the societies via cooperation. 

Networks with increasing returns become most efficient when they are neither treated as purely public nor treated as purely private - but rather as partial and plural goods. 

1. web2 - centralized; souls have very less control (authoritarianism)
2. DeFi - although decentralized, can have internal collusion (anarcho-capitalism); if not made sybil-resistant, then DeFi can finally lead to the biggies owning larger shares
3. DeSoc - stochastic social pluralism - a network of individuals and communities that come together, as emergent properties of each other, co-determining their own future

## Implementation Challenges

Privacy is a key challenge - making too much of data public could reveal too much while allowing a large amount of data to be private could lead to collusion. 

### Private Souls

1. Data on blockchains are public by default. One possible way could be by having multiple pseudonyms - medical soul, school soul, work soul, etc. But, an attacker could quite easily associate them to figure out the individual. Thus, putting all the data on chain with different pseudonyms is not a great solution.
2. Solution - store SBT (where the SBTs store all the relevant information) off-chain and the hash on-chain. User can choose any off-chain technology: (i) local storage; (ii) cloud service; (iii) decentralized networks such as IPFS.
3. Partially reveal data and prove the statements - zk proofs. zk proofs can be computed over SBTs to prove characteristics about a soul.
4. zk proofs can be used prove characteristics of a soul. zk proofs can be extended to MPC techniques such as garbled circuits, which could make the technique doubly private.
5. Another technique - designated verifier proofs - only the designated entity can verify. This can be enhanced using verifiable delay functions (VDFs).

The idea of off-chain data and zero-knowledge techniques are compatible with negative reputations - SBTs that are made visible even if the user doesn’t want them to be visible. Examples of negative reputation are credit history, data about unpaid loans, negative reviews, and complaints from business partners. Therefore, it should be noted that the information provided by negative reputation is essential to be public. Therefore, smart contracts can be designed in a way that Souls would need to incorporate negative SBTs into data structure.

### Cheating Souls

Souls will try to trick or cheat their way into communities to gain access to governance or property rights. One can argue that the varying incentives to cheat may cancel out. That is a Soul trying to get SBTs to gain control over a particular community will end up possessing less diverse SBTs which in turn would lead to losing influence over other communities. However, it would be naive to assume that the influences may cancel out somehow. Thus, to prevent this “gaming” issue, the authors have proposed the following methods:

1. Bootstrap off thick community channels
2. Nested communities could require SBTs to force context on potential collusion vectors “just below” them
3. Use the openness and cryptographic provability of the SBT ecosystem to actively detect collusive patterns and penalize inauthentic behavior
4. Encourage whistleblowers to make collusion of significant size unstable
5. Using ZK technology (such as MACI) to prevent some attestations made by a Soul being provable. This would make attempts to sell certain kinds of attestations non-credible because the briber won’t be able to tell if the bribe recipient actually did the job.
6. Use mechanisms from peer-prediction theory to encourage honest reporting in all cases except when the collusion is very large
7. Use correlation scores that would focus on correlations where there is a large incentive to be honest.

## Comparison

1. Legacy - Rely on pieces of papers. Requires confirmation from 3rd party for verification.
2. Pseudonymous Economy - combining reputation systems with ZKP to preserve privacy. A person splits ZK attestations into multiple wallets to prevent themselves from being identified. Difference - pseudonymous economy greatly emphasizes on privacy protection via identity separation, while SBT does not. Prevention in DeSoc - by contextualizing the attackers. Cancellation occurs when the data travels to the communities that are not closely related to the person. Victim can launch defensive mechanisms and provenance can help the user prove that the SBTs wasn’t generated by them. 
3. Proof of Personhood - Provide tokens for uniqueness. because PoP protocols seek to represent individual identities - PoP protocols are limited to applications that treat all humans the same. 
4. VCs: VC implementations have struggled with a recovery paradigm that could be addressed with community recovery. In addition, the way VC has been built, it supports unilateral privacy. These features are very incorporated in SBTs. Thus, if VCs and SBTs are combined, then it would pave the way to an efficient solution.

## Soul Birth

The Souls can be brought to existence in one of the following ways:

1. Proto SBTs: SBTs may also have the property of revocability which can prove to be very useful in bootstrapping. A token is revocable if an issuer can burn the token and re-issue it to a new wallet. Revocable, transferable tokens are a kind of proto-SBT - which would enable community recovery and allow users to collect revocable SBTs. These revocable SBTs would then be burnt and then, transferred to wallets to form non-transferrable SBT.
2. Community Recovery Wallets: Custodial wallets do the job for not-so-technical users. Once community recovery is introduced into the market, the custodial wallets could decentralize into community recovery and the custodians move on to provide other services in DeSoc. For more technical web3 users, decentralized non-custodial wallets can prove to be the starting point for community recovery mechanisms.
3. Proto-Souls: Norms can also bring Souls into existence. A norm can be introduced of not transferring NFTs and POAPs issued by reputable institutions.

## Conclusion

The ideas presented in the paper are just the start of DeSoc. There are many open questions which still need to be answered, multiple design choices which still need to be made precise and the implementation which needs to be started.

## Resources

1. [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4105763)