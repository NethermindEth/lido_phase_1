# A Truth-Inducing Sybil Resistant Decentralized Blockchain Oracle

Abstract: Many blockchain applications use decentralized oracles to trustlessly retrieve external information as those platforms are agnostic to real-world information. Some existing decentralized oracle protocols make use of majority-voting schemes to determine the outcomes and/or rewards to participants. In these cases, the awards (or penalties) grow linearly to the participant stakes, therefore voters are indifferent between voting through a single or multiple identities. Furthermore, the voters receive a reward only when they agree with the majority outcome, a tactic that may lead to herd behavior. This paper proposes an oracle protocol based on peer prediction mechanisms with non-linear staking rules. In the proposed approach, instead of being rewarded when agreeing with a majority outcome, a voter receives awards when their report achieves a relatively high score based on a peer prediction scoring scheme. The scoring scheme is designed to be incentive compatible so that the maximized expected score is achieved only with honest reporting. A non-linear stake scaling rule is proposed to discourage Sybil attacks. This paper also provides a theoretical analysis and guidelines for implementation as reference.
Classification: Oracles
Labels: Collusion prevention, Worthwile Sybil resistance insights
Link to the paper: https://ieeexplore.ieee.org/abstract/document/9223272
Score: no idea
Score Phase 1: Very relevant
Year: 2020

This paper describes a distributed oracle scheme designed to help alleviate the problem of herd behavior, i.e., in an oracle scheme where voters are rewarded for giving the “right”, that is majority, answer it is in a voter’s interest to vote for the answer he things will win, not necessarily the correct one.

## Setup and Assumptions

The scheme uses a *Decentralized Oracle Model*, that is to say there a bunch of independent participants, called *voters* in the paper, that independently present their information which is then aggregated into the result.  The voters are then rewarded according to the protocol. The naive version of this leads to a Keynesian beauty contest where voters are motivated to go with what they think is the majority opinion.  The paper presents a more sophisticated protocol that seeks to address this problem. 

### The *Common Prior Assumption* model

The protocol relies on a so-called *Common Prior Assumption*.  This is explained somewhat poorly in the paper, so I’m basing my description on [1].  The model is that all the voters have a common Bayesian prior consisting of a random variable $T$ that can be in one of $m$ states, labeled $1,\ldots,m$, and that they all agree on the prior probabilities $P(T=t)$ for all $t\in\{1,\ldots,m\}$.

In addition, each voter receives a one-bit *private signal,* $S_i$ for voter $i$, that can be either $0$ or $1$.  The paper somewhat misleadingly calls this a *private opinion*.  The assumption is that the voters all agree on the conditional probabilities $P(S_i=1\mid T=t)$ which are independent of $i$, and that the events $S_i$ are all independent after conditioning on $T=t$.

The point of the protocol is to motivate voters to truthfully report their private signals $S_i$.  Note: this is not the same thing as their belief about the underlying truth value if any.  Observe, the CPA model itself doesn’t include an underlying truth value for $S$.

The protocol is supposed to make truthfully reporting one’s private signal a Nash equilibrium.  Unfortunately, it obviously can’t make it the only Nash equilibrium.

## Description of the Protocol

### Submitting questions

At any time a submitter can add a Yes/No question to the active questions list.  The submitter actually submits two questions which should be inverses of each other.  This is to avoid the Nash equilibrium where all voters vote $0$.

**Comment:** This won’t necessarily work if it’s obvious from the wording whether a question is an original question or an inverse.

Questions are randomly assigned to voters to help prevent collusion.  In particular, the two inverse questions will get assigned to different groups of voters and the results compared.

As described in the paper, in addition to the questions the submitter submits:

- A bounty $B$ which will be used to reward voters as described later, it will be returned to the submitter if the two inverse questions don’t return opposite answers.
- A bond which will be returned to the submitter if they return opposite answers.  Otherwise, it’ll be split equally among the other participants.
- A duration for how long voting will last.

**Comment:** The purpose of the Bond appears to be to punish the submitter for submitting poorly formed questions, or pairs of questions which aren’t necessarily inverses.  Unfortunately, this doesn’t actually work.  If the bond is less than the bounty, the submitter getting his bounty back counteracts the punishment effect.  If the bond is greater than the bounty, then voters are incentivized to misbehave, e.g., by simply voting $0$ to obtain their share of the bond.

### Voting

To participate a voter posts a stake $s_{min}\le s_i\le s_{max}$, and receives a random question.

The voter then submits a sealed response consisting of a *private opinion* $PO_i\in\{0,1\}$ (although calling it a private signal would be less misleading), which should be the same as the $S_i$ discussed above, and a *private prediction* $0\le PP_i\le1$, which should the voter’s prediction about the probability that a random voter’s private signal $S_j$ will be $1$.

Once the voting period ends all the responses are unsealed.

### Outcome

The outcome is determined by a weighted majority of the voters.  The weights used will be discussed below.

Depending on the outcome for the two inverse questions, either the bond or stake is returned to the submitter.  If the inverse questions have different answers the voters receive their payoffs as described below.

## Reward Rule

Each voter will be assigned a score $u_i=u_{i,{\rm IR}}+u_{i,{\rm PR}}$ consisting of two components, a *prediction score* $u_{i,{\rm PR}}$ that evaluates the voter’s private prediction $PP_i$, and an *information score* $u_{i,{\rm IR}}$ that evaluates the voter’s private opinion $PO_i$.

**Comment:** The paper gives formulas for these scores that are supposed to make it so that a voter maximizes his expected score by truthful reporting his private prediction if all other voters are honest.  However, the formula for the information score given in the paper doesn’t actually have this property, the given proof is flawed, and is additionally not well-defined in some circumstances.  Thus we will be using the information score from [1] instead.

### Binary scoring rule

A *binary scoring rule* is a function that assigns a score to a prediction $0\le q\le1$ of a binary outcome $w\in\{0,1\}$.  A binary scoring rule is *strictly proper* if the voter uniquely maximizes his expected score by honestly reporting his prediction.  It isn’t hard to prove that the rule given by ($R_q$) below is strictly proper.

$$
R_q(q,w)=\begin{cases}2q-q^2, &\text{if } w=1\\1-q^2, &\text{if } w=0 \end{cases}
$$

### Prediction score

To compute voter $i$’s prediction score, apply the binary scoring rule to the voter $i$’s prediction and the private information of a randomly chosen reference voter $i'$.  Thus,

$$
u_{i,{\rm PR}}=R_q(PP_i,PO_{i'}).
$$

### Information score

In addition, the reference voter above selects an addition peer voter $i''$.  Now define the *shadow prediction* to be

$$
SPP_i=\begin{cases}\min(2PP_{i'},1),&\text{if }PO_i=1\\\max(0,2PP_{i'}-1),&\text{if }PO_i=0 \end{cases}.
$$

Now define

$$
u_{i,{\rm IR}}=R_q(SPP_i,PO_{i''}).
$$

### Calculating the reward

The paper recommends rewarding voters who have submitted high-scoring responses, presumably using a threshold.  However, since the scores were designed so that honest voting maximizing the *expected* score, assuming other voters are honest, it makes sense to have the reward linear in the score.

## Weighing stake for Sybil resistance

Of more interest to us is the anti-Sybil mechanism the scheme includes, namely weighing stake sub-linearly when voting, but giving out rewards super-linearly.  Thus since the rewards grow super-linearly, a user is incentivized to put all his stake under a single identity.  And since voting power scales sub-linearly this decreases his voting power.  Thus someone wishing to launch a Sybil attack must forfeit potential rewards to do so.  The downside to this approach is that it contributes to the “rich get richer” effect.

## References

[1] J. Witkowski and D. C. Parkes, “A robust bayesian truth serum for small populations,” in Proceedings of the Twenty-Sixth AAAI Conference on Artificial Intelligence. AAAI, 2014, pp. 1492–1498.  [https://viterbi-web.usc.edu/~shaddin/cs699fa17/docs/BTS_robust.pdf](https://viterbi-web.usc.edu/~shaddin/cs699fa17/docs/BTS_robust.pdf)

## Conclusion

The paper puts together a bunch of pieces into a distributed oracle protocol for binary questions.  Unfortunately, it also mangles the description of some of the pieces, but at least it puts them all in one place.