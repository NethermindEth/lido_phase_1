# Identifying and characterizing Sybils in the Tor network

Abstract: Being a volunteer-run, distributed anonymity network, Tor is vulnerable to Sybil attacks. Little is known about real-world Sybils in the Tor network, and we lack practical tools and methods to expose Sybil attacks. In this work, we develop sybilhunter, a system for detecting Sybil relays based on their appearance, such as configuration; and behavior, such as uptime sequences. We used sybilhunter’s diverse analysis techniques to analyze
nine years of archived Tor network data, providing us with new insights into the operation of real-world attackers. Our findings include diverse Sybils, ranging from botnets, to academic research, and relays that hijacked Bitcoin transactions. Our work shows that existing Sybil defenses do not apply to Tor, it delivers insights into real world attacks, and provides practical tools to uncoverand characterize Sybils, making the network safer for its users.
Classification: Sybil resistance
Labels: Possible tool in larger solution, Worthwile Sybil resistance insights
Link to the paper: https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf
Score: no idea
Score Phase 1: Very relevant
Year: August 2016

## Summary

The Tor network is a web of several thousand volunteer-run routers, called *relays*, which in theory allows users to connect to the Internet free of tracking and monitoring from external parties. At a high-level this is done by entering a Tor circuit, which routes traffic through different relays, encrypting the information each step of the way. These relays, and their status, is summarized in the network consensus that is voted on and published each hour by nine distributed directory authorities. 

Relays are uniquely identified by their *fingerprint*, a particular hash and truncation of their public key. They can also choose a nickname, which is easily remembered but not unique. 

Operators that control many relays are encouraged to group their relays into a ********family.******** Tor users never use more than one relay per declared family, per connection. This is because otherwise the operator controlling that family might oversee a significant portion of the traffic, called ****consensus weight****, and the following attacks become easier to perform:

- **Exit traffic tampering**: when a Tor user leaves the Tor network, the last step in the route is an *exit relay*, which connects the user to its destination server. Controlling exit relays, the attacker can eavesdrop on traffic to collect unencrypted credentials, break into TLS sessions or inject malicious content.
- **Website fingerprinting**: when entering the Tor network, Tor encryption prevents ************entry guards************ from learning their user’s online activity. Still an attacker controlling many entry guards can use packet lengths or timing to infer what website the users are visiting.
- **Bridge address harvesting**: users behind censorship systems use private Tor relays—typically called *bridges*—as hidden stepping stones into the Tor network. It is important that censors cannot obtain all bridge addresses, which is why The Tor Project rate-limits bridge distribution. However, an attacker can harvest bridge addresses by running a middle relay and looking for incoming connections that do not originate from any of the publicly known guard relays.
- **End-to-end correlation**: By running both entry guards and exit relays, an attacker can use timing analysis to link a Tor user’s identity to her activity.

![Overview of the Tor network. Source: [https://www.sciencedirect.com/topics/computer-science/onion-router](https://www.sciencedirect.com/topics/computer-science/onion-router)](Identifying%20and%20characterizing%20Sybils%20in%20the%20Tor%20n%20b8d64783eeae4235972b61d085643801/Untitled.png)

Overview of the Tor network. Source: [https://www.sciencedirect.com/topics/computer-science/onion-router](https://www.sciencedirect.com/topics/computer-science/onion-router)

Therefore, a malicious operator wanting to perform either of these attacks should control several relays and omit that they belong to a family. We call these operators ********Sybils.******** 

## Sybil heuristics

The authors acknowledge that the two methods typically used for Sybil detection and prevention are social and computational constraints, but they believe that these are ill-suited for this case. The former relies on the assumption that it is difficult for a malicious user to form trust relationships with many honest users. This is used for example in [**SYBILFUSE: Combining Local Attributes with Global Structure to Perform Robust Sybil Detection**](SYBILFUSE%20Combining%20Local%20Attributes%20with%20Global%20S%2070b5c786121547e4b8d5af90d9ab26bf.md). However, social graph based defenses do not work here because there is no trust relationship between operators. The latter is based on the simple fact that the more Sybils one runs, the more computational resources one needs. The authors claim that the operating of a Tor relay already requires a constant use of CPU and bandwidth, so that it is impossible to run 100 relays without spending the resources necessary. 

Because of the lack of Sybil detection tools, they have decided to create one -called sybilhunt- based on the heuristic observations that Sybils:

- frequently go online together
- share similarities in their configurations
- may change their identity fingerprint frequently

Their tool has been applied to roughly nine years of Tor data, specifically of consensus data, published every hour, containing all sorts of information about relays, and a pointer to each relay’s descriptor. It has uncovered several Sybil groups, which have since been reported to the Tor network and have been removed. The heuristics differ in effectiveness and sensitivity: one of them detected only a small number of Sybils, another uncovered malicious groups that no other method could. 

![Source: [https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf](https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf)](Identifying%20and%20characterizing%20Sybils%20in%20the%20Tor%20n%20b8d64783eeae4235972b61d085643801/Capture_decran_2022-11-23_a_13.20.37.png)

Source: [https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf](https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf)

Obviously the tool could be applied to new, incoming data, but this places us in an adversarial setting, in which the attacker will do everything to stay under the radar. The authors mention that their tool needs *****some***** amount of correlation, and further that an attacker with a consequent amount of resources could stay undetected by their methods. 

## Analysis techniques

### Churn

The churn rate of a distributed system captures the rate of joining and leaving network participants. In the Tor network, these participants are relays. An unexpectedly high churn rate between two subsequent consensuses means that many relays joined or left, which can reveal Sybils and other network issues because many operators start and stop their relays at the same time, to ease administration—they behave similarly.

However an unusual number of leaving relays could cancel out a sudden spike in the number of joining relays, which is undesirable. Split the time series into $(\alpha_n), (\alpha_l)$ for new relays and relays that left, respectively, as follows: let $C_t$ be the consensus at time $t$, we define  

$$
\alpha_n=\frac{|C_t\setminus C_{t-1}|}{|C_t|}\,\,,\,\, \alpha_l=\frac{|C_{t-1}\setminus C_{t}|}{|C_{t-1}|}
$$

(here $\setminus$ denotes complement)

We can now simply inspect for abnormal spikes. We can use these to obtain a rough approximation of the maximum Sybil rate, depending on a threshold for the churn values. 

![Source: [https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf](https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf)](Identifying%20and%20characterizing%20Sybils%20in%20the%20Tor%20n%20b8d64783eeae4235972b61d085643801/Capture_decran_2022-11-23_a_15.35.48.png)

Source: [https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf](https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf)

These churn values give a graphical understanding of abnormal network entries/exits. To obtain the trends, we can smooth out the data with a simple moving average window:

$$
\lambda=\frac{1}{w}\sum_{i=0}^w\alpha_w
$$

![Capture d’écran 2022-11-23 à 15.38.24.png](Identifying%20and%20characterizing%20Sybils%20in%20the%20Tor%20n%20b8d64783eeae4235972b61d085643801/Capture_decran_2022-11-23_a_15.38.24.png)

![Source: [https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf](https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf)](Identifying%20and%20characterizing%20Sybils%20in%20the%20Tor%20n%20b8d64783eeae4235972b61d085643801/Capture_decran_2022-11-23_a_15.38.42.png)

Source: [https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf](https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf)

To choose the threshold for the churn values after which there should be an alert, the authors take the pragmatic approach of adjusting for a reasonable, possible to investigate number of alerts per day. 

### Uptime matrix

An assumption the authors make is that, *****************for convenience,***************** Sybil operators are likely to operate, update, configure, or reboot (many of) their relays at the same time. 

The previous approach will detect abnormal rates of entering/exiting the network, but it will not indicate whether the relays causing the anomaly were coordinated or not. In order to visualize such synchronized events, we can analyze the uptime patterns, in the ***************uptime matrix.*************** 

![Source: [https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf](https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf)](Identifying%20and%20characterizing%20Sybils%20in%20the%20Tor%20n%20b8d64783eeae4235972b61d085643801/Capture_decran_2022-11-23_a_15.47.31.png)

Source: [https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf](https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf)

In order to get such a nice grouping of similar uptime patterns together, we need to sort the columns in a way that reflects correlation. They sort them using single linkage clustering, with distance defined as:

$$
d(r_{x,y})=1-r_{x,y}
$$

where $r_{x,y}$ is the sample correlation between columns $x$ and $y$. 

![Source: [https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf](https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf)](Identifying%20and%20characterizing%20Sybils%20in%20the%20Tor%20n%20b8d64783eeae4235972b61d085643801/Capture_decran_2022-11-23_a_15.54.58.png)

Source: [https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf](https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf)

### Fingerprint switch

Here they analyzed how often relays changed their fingerprints in order to perform a specific attack which has to do with how the Tor network stores these fingerprints. This is maybe less relevant to our case? 

### Nearest-neighbour ranking

The authors developed a script called exitmap that can detect malicious exit relays. They were left wondering if there existed “similar“ relays, close to the original malicious relay. They built a sort of identifier, concatenating information about relays (say, $\text{nickname}||\text{IP}||\text{port}$ ) and using the Levenshtein distance (minimum number of insert/delete/modify to turn one string into the other) to quantify proximity of these strings. 

This method has limited efficiency, especially if the attackers go out of their way to cover their tracks. 

![Source: [https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf](https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf)](Identifying%20and%20characterizing%20Sybils%20in%20the%20Tor%20n%20b8d64783eeae4235972b61d085643801/Capture_decran_2022-11-23_a_17.08.50.png)

Source: [https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf](https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf)

## Cost

Overall the methods are relatively simple and inexpensive to implement, except for Uptimes, because of the single-linkage clustering algorithm, for which the optimal implementation runs in $\mathcal{O}(n^2)$. This could be problematic if the system is to run continuously and the operator pool grows. The following benchmarks are for the Tor relay pool which has around $7000$ relays:

![Source: [https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf](https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf)](Identifying%20and%20characterizing%20Sybils%20in%20the%20Tor%20n%20b8d64783eeae4235972b61d085643801/Capture_decran_2022-11-23_a_17.26.26.png)

Source: [https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf](https://nymity.ch/sybilhunting/pdf/sybilhunting-sec16.pdf)

## Insights

The authors provide many operational insights on the detection of Sybils. One of them is that analyzing Sybils is usually hard to completely automatize. Many times, it is also hard to decide whether there is actual evidence of collusion or correlation, and further investigation is needed. 

The exitmap tool is particularly interesting: the injection of **************decoy traffic************** for which we know the expected output, and can allow us to detect malicious actors. 

The churn and uptime matrix seem particularly relevant and relatively easy to implement in our case. For nearest-neighbours, we can also use more complicated identifiers and more sophisticated distances (for example geographic proximity from the IP address). 

One of the crucial points is also about reducing information asymmetry: these methods are now known, but the attackers operate behind closed doors. Therefore the system should be transparent (in our case, and more generally in any decentralized permissionless system) but also not disclose the specific parameters, thresholds, or in the best case, features that we are looking for. 

As we have already discussed, the idea seems to always be the *********layering********* of security solutions, so that it becomes exceedingly difficult and costly to create Sybils, while it is disproportionately easy to behave honestly. 

Another idea, which is not developed here, is to decentralize some of the tasks in the detection. We know, however, how difficult developing these systems can be.  

It has to be verified whether in our case, *in practice*, **the heuristics which form the basis of this analysis hold.

## Assessment

This papers gives readily available methods for Sybil detection, which on **********past data********** of the Tor network has managed to identify many Sybil groups which have been removed from the network since. Some of the analysis techniques seem to apply mutatis mutandis to our setting, and some of them could be adapted to fit. One particularly interesting idea is the one of using decoy traffic. The biggest limitation is that in an adversarial setting, attackers will go out of their way to stay under every metric we can come up with. The point however, is to make it more and more expensive to create Sybils, by layering many of these methods, and by hiding some of the information used for detection. 

We mark it as very relevant.