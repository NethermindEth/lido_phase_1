# Marinade

Abstract: Marinade is the first non-custodial liquid staking protocol built on Solana. Stake your SOL tokens with Marinade and receive mSOL (“marinated SOL”) tokens in return that can be used in decentralized finance (DeFi). mSOL is the most widely integrated collateralized version of SOL. The price of mSOL goes up relative to SOL each epoch, with rewards being accrued into your stake account.
Marinade’s delegation strategy stakes to 400+ validators that are selected automatically by an open-source, fair formula based on performance, commission, and decentralization.
Actions needed and questions: Describe how the system verifies credentials of the new coming operators                                                           @Michal Zajac There is a lack of available resources on the KYC mechanism (Marinade uses for onboarding the validators). I am still searching for the same.   Added  Marinade%2049c0362bbddd47afb2147e3f3cb93eb2/How%20Does%20the%20Validator%20Score%20V1%20Work%20b5d9e8456c5b4b63995c64a0db6e4465.md, to compute the score which is one of the eligibility criteria.

@Basireddy Swaroopa Reddy please provide an abstract                  @Michal Zajac Done
Added to deliverable?: No
Already read?: Yes
Assigned for action: Basireddy Swaroopa Reddy
Assigned readers: Basireddy Swaroopa Reddy
Labels: Liquid staking protocol
Link to the paper: https://marinade.finance/
MZ checked the note: No
Presentation date: October 19, 2022
Reviewers: Jorge Arce-Garro
Score Phase 1: Not relevant
Work Group: Blockchain projects

MArinade for Solana

# Marinade

- [Marinade.finance](http://Marinade.finance) is a liquid staking protocol built on Solana.
- It allows users to stake any amount of SOL and receive “$marinated$ SOL” ($mSOL$) tokens and use it in DeFi.
- The price of $mSOL$ goes up each epoch (approximately $2$ days) relative to SOL as rewards accrued.

$$
Price\_of\_mSOL = \dfrac{total\_staked}{tokens\_minted}
$$

      The $total\_staked$  is equal to amount of $SOL$ staked by users $+$ rewards accrued 

- Open-sourced, permissionless delegation formula with more than $450$ (currently $466$) validators.
- Unstake period -
    - **Delayed unstake** - without any fee waiting period of $1-2$ epochs
    - **Immediate unstake** - varies between $0.3\%$ and $3 \%$ and depends on the total liquidity available in the Marinade pool and the amount to unstake. Marinade’s liquidity target is set at $100,000$ $SOL$. As long as this target is maintained after unstaking, the fee will be at$0.3\%$.
    
    $$
    unstake\_fee = max\_fee - (max\_fee - min\_fee)*\dfrac{amount\_after}{ target}
    $$
    
            
    
    > The parameters are used currently, but could be changed later. The Marinade DAO will be responsible for the fee structure and will vote on the parameters.
    > 
- The players in the Marinade protocol - users/stakers, Validators and Marinade’s algorithm to spread the stake to the validators.
    - Users can deposit their stake account directly to validator (i.e. users can select thier choice of validators) subject to
        - Validator must not be delinquent (more than $256$ slots behind the tip of the blockchain)
        - Validator must have a commission lower than $30\%$
    - A validator receives stake from the Marinade through a delegation strategy specified by  **Marinade's algorithm** (which follows Solana Foundation’s stake delegation strategy).
- **MNDE** is the governance token of Marinade, a DAO operating on the Solana blockchain. Token holders who lock their MNDE to mint a Marinade Chef NFT are
    - Eligible to take part in on-chain governance of the Marinade DAO
    - Control the $10\%$ of the total Marinade stake through validator gauges.

# Stake ****Delegation Strategy****

- Marinade follows the Solana Foundation’s stake delegation strategy
- It spread the stake among the long tail of **high-performance, low-commission and non-concentrated validators** in order to increase the decentralization and censorship resistance to Solana.

      

![delegation_strategy.png](Marinade%2049c0362bbddd47afb2147e3f3cb93eb2/delegation_strategy.png)

- Delegate SOL to nodes not belongs to the **max security group**, i.e. Marinade doesn’t stake to big validators, but trying to encourage more validators.
- In order to consider for the stake delegation, a validator should maintain an average of $100$ SOL over the last $10$ epochs.

## ****Solana Foundation Delegation Strategy****

1. The foundation is committing to delegate $100$ million SOL (Over $80\%$ of the foundation’s treasury) with the following goals - 
    - To improve the network’s censorship resistant and security
    - Encourage the growth in the number of validators
2. Foundation will deploy an autonomous script that dynamically and uniformly divides and delegates a pool of $100$ million SOL in such a way to maximize the minimum number of unique nodes that constitute $33\%$ of the global stake.
3. Nodes must meet certain **eligibility criteria** (The foundation delegation will be removed to the nodes fail to satisfy the eligibility criteria until they met the delegation requirements).
4. The Foundation regularly **re-balance** it’s distribution of the delegations (Changing in the number of nodes and non-foundation stake).
5. The Foundation will automatically **re-delegate** all staking yields that are accumulated from the distributed stake (The increase in the circulation supply is limited to validator commissions).

### Technical details:

**Maximal security Group:**

- **security group:** The smallest group of unique nodes that comprises $\geq 33\%$ of the total stake on the network. The delegation strategy provides delegations  to eligible validators outside this group.
- **Maximal security group:** The largest **security group** that can be created, given the strategic delegation of the Foundation’s tokens across eligible nodes on the network outside this group.
- The Algorithm to identify this group -
    - Calculate $33\%$ of the total amount of stake on the network (Foundation stake $+$ Non-Foundation stake).
    - Identify the **minimum set of validator nodes** of which cumulative, non-Foundation stake is greater than or equal to this amount.

**How to delegate Foundation stake to validators outside this  group?**

1. Once the network’s maximal security group is identified, the Foundation’s total token pool (initially $100$ million SOL) is then divided into equal portions based on the number of eligible nodes *outside* of this group.

**Constraints:**

- The Foundation will not delegate so many tokens to any one node such that its cumulative           total stake (Foundation + non-Foundation) exceeds the total stake of any node in the security group which does not receive a Foundation delegation.
- The uniform delegation of the Foundation stake should not change the rank ordering before and after delegation of the stake.

 **Example #1:**  

![                                                   **Pre-delegation Security group**](Marinade%2049c0362bbddd47afb2147e3f3cb93eb2/Pre-delegation.png)

                                                   **Pre-delegation Security group**

 Number of validators $= 40$

 Non-Foundation tokens staked across $40$ validators $=10$ M SOL

 Foundation tokens $= 5$ M SOL

 Maximal security group = Min. number of validators comprise $\geq 5 M$ SOL  ($33\%$ of $15$ M) $= 4$         

Eligible nodes outside the Maximal security group $= 36$

Each node receives a delegation of $\dfrac{5,000,000}{36} = 138889$ SOL

![                                                 **Identify the Maximal Security Group**](Marinade%2049c0362bbddd47afb2147e3f3cb93eb2/Identify_max_sec_group.png)

                                                 **Identify the Maximal Security Group**

![                                                    **Solana Foundation Delegation** ](Marinade%2049c0362bbddd47afb2147e3f3cb93eb2/Foundation-delegation.png)

                                                    **Solana Foundation Delegation** 

1. However, the above algorithm may not be initially satisfy at the border between the security and non-security group.

**Example #2:** 

![border.png](Marinade%2049c0362bbddd47afb2147e3f3cb93eb2/border.png)

1. In this scenario, the Foundation delegations delivered to nodes $10$, $11$ and $12$, has changed the total stake rank-ordering of the validator set, violates the constraint specified by the strategy.
2. The delivery algorithm will take the following steps:
    1. Reduce the delegation to node $10$, until stake on node $10$ is equal to the stake on node $9$.
    2. Re-calculate the per-node Foundation delegation after adding the amount that was removed from node $10$ to the entire pool.
    3. Consider re-distributing the newly calculated per-node Foundation stakes to nodes with non-Foundation stake $<$ node $10$ (i.e. nodes $11+$).
    4. If the total potential delegation on node $11$ is now greater than node $10$, restart this process by reducing the delegation on node $11$ and re-calculating the per-node stake to distribute across downstream nodes (i.e. back to step a).
3. After this reduction process, in this example, the amount of delegation for nodes $13+$ has increased proportionally by the amount that was removed from nodes $10$, $11$ and $12$ in order to satisfy the design constraints.

![modified_algorithm.png](Marinade%2049c0362bbddd47afb2147e3f3cb93eb2/modified_algorithm.png)

## **Rebalancing period:**

1. The delegations will be re-assessed and re-balanced every $4$ epochs ($\approx 8$days). 
    1. No addition of delegations
    2. If a node fails, delegations will be deactivated
    3. Change in non-Foundation stake and an updated Foundation delegation spread (change in number of nodes)
2. Given an amount of the stake the foundation delegates, it may take more than $1$ epoch for rebalancing due to the Solana’s protocol limit of no more than $25\%$  should be added or removed in a single epoch.

## Re-delegation:

As result of the re-delegation of the Foundation’s staking yield, the impact on the circulating supply is limited to the amount of commissions received by the validators via Foundation’s delegations.

## Eligibility Requirements

Anyone can operate a validator and earn rewards from delegations at any time, without needing the consent of the Solana Foundation subject to the following criteria must met - 

### **Prerequisites:**

1. Node operators must pass KYC.
2. Node operators must agree to and sign Solana’s Participation Agreement.
3. Node operators must participate in at least one full stage ($\approx 1$ month in duration) of the [Tour de SOL incentivized testnet program](https://solana.com/tds). After successful participation, validators will be eligible to participate in the delegation program on Solana’s Mainnet Beta network.
4. A Validator who is eligible for Foundation’s delegation program, may choose to migrate Tour de node to mainnet or continue on the testnet and earn corresponding compensation to run their second node on the mainnet.

### **Technical Requirements:**

1. Vote on $>90\%$ on all valid blocks during the sampling window ($1$ epoch). 
2. Retain a **delinquency rate**  over the course of a $48-$hour moving average time window. 
    1. a validator that is more than $256$ slots behind the tip of the blockchain is flagged as delinquent. 
    2. Delinquency status will be polled hourly. 
    3. If a node is sampled as delinquent in more than $10\%$ of the previous $48$ hours’ checks, it is considered to have failed this requirement.
3. Propose blocks in $>90\%$ of scheduled leader slots. (This requirement will be enforced only when node receives Foundation delegation and the node enters the leader  schedule).
4. Retain a commission rate $\leq 10\%$.

**Delegation Exclusion Period:** 

- The nodes new to delegation program and that failed to maintain the above criteria are ineligible for a Foundation’s delegation for a minimum of two rebalancing periods ($\approx 8$ epochs).
- If a node maintain the delegation criteria  for the full Delegation Exclusion Period and then the node will receive a Foundation delegation at the next rebalancing period, other wise Delegation Exclusion period start over.

 

## Continue… Marinade’s delegation strategy:

1. Once the Maximal Security Group nodes are excluded, the following parameters are considered for calculating the validator score - 
    - Performance (APY)
    - Commission
    - Delinquency (As defined in Solana Foundation delegation strategy)
    - Decentralization objectives (Increase Nakamoto Coefficient)
    - Version of the node
    
    [****How Does the Validator Score V1 Work?****](Marinade%2049c0362bbddd47afb2147e3f3cb93eb2/How%20Does%20the%20Validator%20Score%20V1%20Work%20b5d9e8456c5b4b63995c64a0db6e4465.md)
    
2. Three different sources of information to gather the above data-
    - [StakeView](https://stakeview.app/)  APY data to collect the information about **current epoch** credits to determine if the validator was down for most of the current epoch
        - Assumes Epochs are of equal length. APY for previously completed epoch:
    
    $$
    EPOCH\_RETURN\_FACTOR = \dfrac{EPOCH\_REWARDS}{EPOCH\_BEGINNING\_BALANCE}
    $$
    
    $$
    EPOCHS\_PER\_YEAR = \dfrac{86400}{EPOCH\_SECONDS}
    $$
    
    $$
    APY = ((1 + EPOCH\_RETURN\_FACTOR)^{ EPOCHS\_PER\_YEAR} - 1
    $$
    
    - How to compute the estimated APY for the current epoch?
        - Taking the highest APY of the previous epoch
        - Taking the validator for which the current $vote\_credits*(1-commission)$ is highest.
        - Scales the expected APY of all other validators according to their $vote\_credits*(1-commission)$ as a fraction of the best-performing validat**or.**
        - **Example:**
            - The best APY from the previous epoch was $8.09\%$, then the validator with the highest $vote\_credits*(1-commission)$ of the current epoch is listed at $8.09\%$.
            - If the next validator has a $vote\_credits*(1-commission)$ value $99.15\%$ of that of the best performing validator, then it’s estimated APY is $(0.9915*8.09\%) = 8.02\%$.
            - All validators are assigned expected APY in this way
    - [Validators.app](http://Validators.app) for data center concentration (same as the Solana Foundation). This data will zero the score if $33\%$ of the total stake is reported in the same data-center.
    - The rest of the data (delinquency, version, etc.) is extracted from Solana.
3. According to a [change voted by the DAO](https://forum.marinade.finance/t/dao-proposal-delegation-strategy-update-fee-structure-changes/252), a bonus to score will be applied to validators running with a lower commission than $10\%$.
    - $9\%$ commission - $\times2$ to the score
    - $8\%$ commission - $\times3$ to the score
    - $7\%$ commission - $\times4$ to the score
    - $6\%$ commission - $\times5$ to the score

### Calculation details:

1. A scoring is performed on **all validators**, based on the last $10$ epochs. It takes into account *Epoch credits*, *Commission*, *Decentralization* (by analyzing the Data Center used), and *Node Version.*
    - active for $< 5$ epochs: Score will be zeroed **
    - active for $5-10$ epochs : the average will be realized on the total amount of active epoch time
    - Pick the top $430$ validators according to this score are selected  (This number corresponds to the number of validators that Marinade is trying to reach and may be modified as the total TVL (Total Value Locked) of Marinade evolves)
2. Scoring based on the performance within current epoch
    - Credits observed within epoch (relative to others as per [https://stakeview.app/help.html](https://stakeview.app/help.html))
        - $< 80\%$ of average $\rightarrow$ emergency unstake
        - $< 90\%$ of average $\rightarrow$ score is divided by $2$
    - APY (relative to others as per [https://stakeview.app/help.html](https://stakeview.app/help.html))
        - very low APY $\rightarrow$ emergency unstake
        - low APY $\rightarrow$ score set to $50 \%$
    - Delinquency based on S*olana validators*
3. Scoring adjustments
    - Blacklisted validators (cheating the system or changing the fee at the last movement) $\rightarrow$ emergency unstake
    - Adjust scores for over-staked (with the exception of validators where Marinade stake is $> 20 \%$ of their total stake)
        - If $score = 0$ (e.g. not in the top 430) and the validator's Marinade stake is $> 0.45 \%$ of all Marinade stake $\rightarrow$ emergency unstake
        - If $score != 0$ but the validator got over 250 % of what they should have  $\rightarrow$ emergency unstake
    - Partial Unstake has been implemented with a cap of $4 \%$ of the total Marinade stake for an epoch
    - A Maximum stake cap has been implemented and is set at $1.5\%$ of the total Marinade stake.
    - Validator's stake delta capping:
        - if the validator is severely under-staked (they could potentially receive more than 2x of their current Marinade stake): cap score to 80 % of their current score
        - if the validator is under-staked: cap the score so the received stake is no more than $0.1\%$ of the overall stake currently delegated to all validators
        - if the validator is over-staked: noop

## Validator Gauges

Implemented into the delegation strategy through a successful on-chain vote [https://tribeca.so/gov/mnde/proposals/5](https://tribeca.so/gov/mnde/proposals/5). 

- Gauges control the $10\%$  of the total Marinade’s stake
- These $10\%$ split among the MNDE holders (Marinade NFT’s)
- Gauges do not allow
    - To delegate stake to validators in the superminority, blacklisted or commission $>10 \%$
    - Validators having more than $1.5\%$ of the total Marinade stake

## References

1. [https://docs.marinade.finance/marinade-protocol/system-overview](https://docs.marinade.finance/marinade-protocol/system-overview#delayed-unstaked)
2. [https://docs.marinade.finance/fa](https://docs.marinade.finance/faq/faq#can-i-deposit-my-stake-account-directly)q
3. [https://medium.com/solana-labs/announcing-the-solana-foundation-delegation-strategy-5bcccf9104ab](https://medium.com/solana-labs/announcing-the-solana-foundation-delegation-strategy-5bcccf9104ab)
4. [https://docs.marinade.finance/marinade-protocol/validators](https://docs.marinade.finance/marinade-protocol/validators)
5. https://github.com/marinade-finance/delegation-strategy
6. [https://medium.com/marinade-finance/introduction-to-marinade-solanas-leading-liquid-staking-protocol-and-so-much-more-e99f3db92743](https://medium.com/marinade-finance/introduction-to-marinade-solanas-leading-liquid-staking-protocol-and-so-much-more-e99f3db92743).
7. [https://stakeview.app/help.html](https://stakeview.app/help.html).
8. [https://solana.com/news/validator-health-report-august-2022](https://solana.com/news/validator-health-report-august-2022)
9. [https://solana.org/delegation-criteria](https://solana.org/delegation-criteria)
10. [https://www.validators.app/faq#score](https://www.validators.app/faq#score)
11. [https://medium.com/@Cogent_Crypto/how-to-become-a-validator-on-solana-9dc4288107b7](https://medium.com/@Cogent_Crypto/how-to-become-a-validator-on-solana-9dc4288107b7)