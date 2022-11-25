# How Does the Validator Score V1 Work?

## Definitions:

**Root Distance:** Measures the median & average distance in block height between the validator and the tower's highest block. Smaller numbers mean that the validator is near the top of the tower.

**Vote Distance:** Is very similar to the Root Block Distance score above.

**Skipped Slot %:** Measures the percent of the time that a leader fails to produce a block during their allocated slots.

****Delinquency:**** If the validator is not active in the solana network it is considered to be delinquent. Short-time delinquencies are considered acceptable, since it occurs while software updates or temporary internet outages.

**Cluster:** A Solana cluster is a set of validators working together to serve client transactions and maintain the integrity of the ledger.

validator performance is computed over several dimensions and assign a score in the range of $(0..2)$ for each**.**

1. **Root Block Distance:**
    1. (2 points) - the validator median block distance is at, or below, the cluster median.
    2. (1 point) - the validator average block distance is at, or below, the cluster average.
    3. (0 points) - the validator average is higher than the cluster average.
    
    The medians and averages are calculated over a trailing $2$-day period and do not reset with each epoch.
    
2. **Vote Distance: T**he scoring rules are the same as Root Block Distance above.
3. **Skipped Slot %:** For this metric, a trailing 24-hour moving average of the skip rate is considered.
    1. (2 points) - the validator skipped slot % is at, or below, the cluster median.
    2. (1 point) - the skipped slot % is at, or below, the cluster average.
    3. (0 points) - the validator average is higher than the cluster average.

The moving averages reflect the previous 24-hours, and the spot reading resets with each new epoch.

1. **Published Information:** Investors or delegators want to know who is running a node. The Published Information Score measures the contact information that the validator has posted to the blockchain using the `solana validator-info` feature.
    1. (2 points) - the validator has published all four data elements (Name, Keybase ID, Website URL, and Details). 
    2. (1 point) - the validator has published two or three parts. 
    3. (0 points) - the validator has published only one, or zero, pieces of contact data.
2. **Software Version:**
    1. (2 points) - the validator is using the correct major, minor, & patch versions.
    2. (1 point) - the validator is using the correct major, & minor versions (but not patch).
    3. (0 points) - the validator is only using the current major version (or less).
    
    This score is updated as soon as the validator starts voting with a new software update.
    
3. **Bonus Point:**
    1. (1 point) - the validator has provided a valid URL.
    2. (0 points) - the validator has not published a description of their security policies, or validator uses software modifications.
4. **Stake Concentration:** is a contra-score and will DEDUCT points from a validator's total score
    1. (-2 points) - this validator is one of the top 33% active stake holders.
5. **Data Center Concentration:** This is another contra-score that will DEDUCT points from validators located in data centers that host a high percentage of other Solana validators
    1. (-2 points) - this validator is in a data center with a very high percent of the active stake.
    2. (-1 point) - this validator is in a data center with a high percent of the active stake.
6. **Authorized Withdrawer Score:** Validator identity matching authorized withdrawer is a serious security risk, eg. if someone hacks into your validator, they can steal from the vote account. Keep the withdraw authority key offline to minimize the risk. 
    1. (-2 points) - this validator identity is the same as the authorized withdrawer identity.
7. **Consensus Mods Score:** This is another contra-score that will DEDUCT points from validators that appear to use software modifications with an unproven effect on consensus. A validator's most important job is to form an agreement about the validity of the blockchain. If over 34% of validators are using non-standard consensus logic, the cluster can stall if the validators cannot reach a majority consensus. In such an event, the only way to resume is to restart after slashing the stake of the validators with modified software. Stakeholders who delegate to these validators should be aware of a small risk that they can lose funds. 
    1. (-2 points) - this validator appears to use unproven software modifications. Validators that use mods with an unproven effect on consensus are also assigned with bonus point $0$.

### References:

1. [https://www.validators.app/faq#score](https://www.validators.app/faq#score)