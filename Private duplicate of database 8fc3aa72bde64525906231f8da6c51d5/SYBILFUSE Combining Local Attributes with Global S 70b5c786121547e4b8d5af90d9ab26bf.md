# SYBILFUSE: Combining Local Attributes with Global Structure to Perform Robust Sybil Detection

Abstract: Sybil attacks are becoming increasingly widespread and pose a significant threat to online social systems; a single adversary can inject multiple colluding identities in the system to compromise security and privacy. Recent works have leveraged social network-based trust relationships to defend against Sybil attacks. However, existing defenses are based on oversimplified assumptions about network structure, which do not necessarily hold in real-world social networks. Recognizing these limitations, we propose SYBILFUSE, a defense-in-depth framework for Sybil detection when the oversimplified assumptions are relaxed. SYBILFUSE adopts a collective classification approach by first training local classifiers to compute local trust scores for nodes and edges, and then propagating the local scores through the global network structure via weighted random walk and loopy belief propagation mechanisms. We evaluate our framework on both synthetic and real-world network topologies, including a large-scale, labeled Twitter network comprising 20M nodes and 265M edges, and demonstrate that SYBILFUSE outperforms state-of-the-art approaches significantly. In particular, SYBILFUSE achieves 98% of Sybil coverage among top-ranked nodes.
Classification: Sybil resistance
Link to the paper: https://ieeexplore.ieee.org/document/8433147
Score: no idea
Score Phase 1: Relevant
Year: 2018

# SYBILFUSE

**Sybil Attack:** In social networks like Facebook or Twittter, a single adversary can inject multiple identities in the system to compromise security and privacy.

**Example:** The attacker can leverage Sybil accounts to disrupt democratic election and influence financial market via spreading fake news, as well as compromise system security and
privacy via propagating social malware, disseminating scams, and learning users’ private data.

**SYBILFUSE:** A defense-in-depth framework for Sybil detection, which adopts a collective classification (which uses both structure and attributes of the network topology) approach by 

- First training local classifiers to compute local trust scores for nodes (identities) and edges (trust relationship between the identities).
- Then propagating the local scores through the global network structure via weighted random walk and loopy belief propagation mechanisms.

## Introduction

### Overview

**Input:** Social network data

**Output:** Trust scores of accounts used for sybil classification

1. Leverages the local attributes to train the local classifiers
    1. Local node classifier predicts the trust score for each node (probability of that node to be benign).
    2. Local edge classifier predicts the trust score for each edge.
2. These trust scores are combined with the global structure through the weighted trust score propagation
    1. SYBIL FUSE captures local account information in **node trust scores**, and propagates these scores through the global structure. 
    2. SYBIL FUSE leverages **edge trust scores** to enforce unequal weights, so that attack edges (edges between the benign and sybil nodes) will have reduced impacts on the propagation.
3. After the propagation completes, final trust scores of accounts are used for Sybil classification and ranking.

## Background and Related work

### A. Sybil Attack Scenario

- Consider a network topology $G = (V, E)$, comprising a set $V$ of nodes (i.e., user accounts) and a set $E$ of edges (i.e.,friendship relationships).
- To model real-world social networks, graph G can be either directed or undirected.

       **Examples:** A **directed graph** models the follower-following topology (e.g., Twitter), in which                                                          

   $(u,v) ∈ E$  denotes that $u$ follows $v$. An **undirected graph** models the mutual relationship     

    topology (e.g., Facebook), in which $(u,v) ∈ E$ is equivalent to $(v,u) ∈ E$.

- **Attack Edges:** The number of edges between the benign users and sybil identities

![attack.png](SYBILFUSE%20Combining%20Local%20Attributes%20with%20Global%20S%2070b5c786121547e4b8d5af90d9ab26bf/attack.png)

                Source: From this paper

- **Victim Prediction:** Benign accounts that connect to Sybil identities

### B. Limitations in State-of-the-art Sybil Defenses

- **Local attribute-based approaches:**
    - Local attribute-based approaches seek to detect Sybil accounts by analyzing local
    account attributes (e.g., posts, status updates, connections).
    - [Blocklisting](https://dl.acm.org/doi/10.1145/1315245.1315288), [whitelisting](https://firstmonday.org/article/view/2793/2431), [URL spam filtering](https://ieeexplore.ieee.org/document/5958045), [Bayesian classification](https://ieeexplore.ieee.org/abstract/document/5741690), [Support Vector Machines (SVM)](http://users.eecs.northwestern.edu/~kml649/publication/GaoChe12.pdf), [clustering](https://dl.acm.org/doi/10.1145/1920261.1920263).
    - **Limitation:** Sybils can easily evade the detection by mimicking the local behaviors of
    benign users via manipulating their profiles and connections.
- **Global structure-based approaches:**
    - Global structure-based approaches seek to exploit the global graph-theoretic differences between the benign region and sybil region (e.g., attack edges, victim prediction)
    - Most global structure-based approaches leverage either random walks or loopy belief propagation.
    - [SybilGuard](https://dl.acm.org/doi/pdf/10.1145/1159913.1159945), [SybilBelief](https://arxiv.org/pdf/1312.5035.pdf), [SybilLimit](https://ieeexplore.ieee.org/document/4531141), [SybilInfer](https://www.researchgate.net/publication/221655356_SybilInfer_Detecting_Sybil_Nodes_using_Social_Networks#:~:text=SybilInfer%20is%20an%20algorithm%20for,potential%20regions%20of%20dishonest%20nodes), [SybilSCAR](https://ieeexplore.ieee.org/document/8057066).
    - **Limitations:** Assume a strong trust network, where the number of attack edges is limited. Assume that the benign region is fast mixing, which presumes the existence of a well-connected, giant community structure of benign users.

## THE SYBILFUSE FRAMEWORK

Recognizing the limitations in existing approaches, authors propose SYBILFUSE , a defense-in-
depth framework that leverages heterogeneous sources of information to perform robust Sybil detection.  SYBILFUSE combines local attributes with global structure by adopting a collective classification scheme.

![sybilFuse.png](SYBILFUSE%20Combining%20Local%20Attributes%20with%20Global%20S%2070b5c786121547e4b8d5af90d9ab26bf/sybilFuse.png)

Source: From this paper

### A. SybilFuse Overview

- **Local classifiers:**
    - **Local Node classifier:** Predicts the score for each node - Probability of node to be benign
    - **Local Edge classifier:** Predicts the score for each edge - Probability of edge to be not an attack edge
- SYBILFUSE captures local account information in node trust scores, and propagates these scores through the global structure.
- SYBILFUSE furthermore leverages edge trust scores to enforce unequal weights for the propagation, so that attack edges will have reduced impacts.

### B. Local Trust Score Computation

- **Notation:** Given a social graph $G = (V, E)$
    - $S_v$: The trust score of node $v \in V$ - quantifies the probability that $v$ is benign.
    - $S_{u,v}$: The trust score of edge $(u, v) \in E$ - quantifies the probability that node $u$ and node $v$ take the same label (i.e., homophily strength). (label means either benign or sybil).
- To compute $S_v$ , authors leverage local node attributes (e.g., Structural attributes - degree, local clustering coefficient;  Content attributes - profile, posts) and train a machine learning classifier (e.g., SVM - Support Vector Machine, logistic regression) that outputs probabilistic estimates.
- To compute $S_{u,v}$, similarly build an edge classifier. In addition, the similarity between node  $u$ and $v$ using various metrics (e.g., Cosine, Jaccard, Adamic-Adar [Adamic-Adar similarity score](https://www.cs.cornell.edu/home/kleinber/link-pred.pdf)).
    
    $$
    score(u,v) = \frac{|\Gamma(u) \cap \Gamma(v)|}{|\Gamma(u) \cup \Gamma(v)|}
    $$
    
    Where, $\Gamma(x)$   is set of neighbours of $x$ in $G$.
    

**Note:** The scores $S_{v}$ and $S_{u,v}$ are restricted in the range [0.1, 0.9] through normalization, 

since scoring zero would invalidate our weighted score propagation.

### C. Weighted Trust Score Propagation

- **Weighted random walk:**
    - **$S^{(i)} (v)$** denote the score of node $v$ after $i$-th power iteration.
    - Set the initial score of every node $S^{(0)} (v) = S_v$ (excluding training data). For the nodes in the training data set initial scores as $0.1$ for sybil nodes and $0.9$ to benign nodes.
    - The weighted random walk using the update equation -
    
    $$
    S^{(i)}(v)  = \sum_{(u,v) \in E} S^{(i-1)}(u) \frac{S_{(u,v)}}{\sum_{(u,w)\in E} S_{(u,w)}}
    $$
    
    - $u$ will distribute more of its round $(i-1)$ trust to a close friend $v$ (i.e., $S_{(u,v)}$ is high) rather than an unfamiliar connection $w$. In this way, attack edges that have low trust scores will have reduced impacts on the propagation.
    - After $d = \mathcal{O}(log(n))$ steps ($n$ = number of nodes), the final score
    
    $$
    S^{F}(v) = S^{(d)}(v) 
    $$
    
- **Weighted loopy belief propagation:**
    - Authors model the graph G as a pairwise Markov Random Field ([MRF](https://ieeexplore.ieee.org/document/4767341) is a graphical model of a joint probability distribution). For each node $v$, associate it with a binary random variable $X_v \in \{1, −1\}$ ($X_v = 1$ for benign and $X_v = −1$ for Sybil).
    - $\psi_v(X_v)$: Node potential function for node $v$
    - $\psi_{u,v}(X_u, X_v)$: Edge potential function for edge $(u,v)$
    - Initial values for these functions are predicted trust scores from local classifiers
    
          
    
    $$
     \psi_v(X_v) = \begin{cases}    S_v & if \hspace{0.1cm}   X_v = 1.\\    1-S_v  & if \hspace{0.1cm} X_v = -1.  \end{cases}
    $$
    
     
    
    $$
     \psi_{u,v}(X_u, X_v) = \begin{cases}    S_{u,v} & if \hspace{0.1cm}   X_uX_v = 1.\\    1-S_{u,v} & if \hspace{0.1cm} X_uX_v = -1.  \end{cases}
    $$
    
    - Given a pairwise $MRF (G, \psi)$,  propagate local trust scores through the global structure using Loopy Belief Propagation [LBP](https://arxiv.org/abs/1301.6725)
    
    $$
    m_{u→v} (X_v) = \sum_{X_u} \left(\psi_v(X_v)\psi_{u,v}(X_u,X_v) \prod_{s \in neighbours(u)\diagdown{v}} m_{s→u} (X_s)\right)
    $$
    
    **Note:** where $m_{u→v} (X_v)$ is initially set to $1$ for all edges $u → v$ and  edge potentials enforce unequal contribution of edges to the propagation
    
    - After $d = 5 ∼ 10$ rounds of iteration, the belief score of node $v$ with label $X_v = x_v$ is
    
    $$
    bel_v (X_v = x_v) ∝ ψ_v (X_v = x_v) \prod_{v \in neighbours(u)\diagdown{v}} m_{u\rightarrow v}(X_v)
    $$
    
    - Final score
    
    $$
    S_v^F = \frac{bel_v(X_v = 1)}{{bel_v(X_v = 1)} + bel_v(X_v = -1)}
    $$
    

### D. Sybil Account Prediction and Ranking

- **Sybil account prediction:** For a node $v$, we predict its label $L_v$ by comparing its final score $S_v^F$ with a threshold value:

$$
L_v = sign(S_v^F − threshold)
$$

          where $L_v = 1$ indicates a benign label and $L_v = −1$ indicates a Sybil label $threshold$ can be calculated from the cross-validation of the training data.

 

- **Sybil ranking:** We can also surface Sybil accounts by ranking all nodes in an ascending order of their final scores. Sybils with low scores will be ranked upfront.

## LABELED TWITTER EVALUATION

### A. Network Preprocessing and Measurement

- Preprocessed it to an undirected network by retaining an undirected edge if both directions exist.
- After preprocessing, the network consists of $8,167$ nodes and $54,146$ edges, with verified $7,358$ benign nodes and $809$ Sybil nodes
    - Sybil nodes emit a large number of attack edges $(40,010)$, with $49.5$ attack edges on
    average per Sybil
    - $53.4\%$ of Sybils are isolated (i.e., they only connect to benign nodes)
    - The number of victims is large ($5,546$; $75.4\%$ of benign nodes). Thus, the benign region and the Sybil region can hardly be viewed as separate communities.

### B. Local Trust Score Computation

- **Feature Extraction:**
    - **Incoming requests accepted ratio:** $Req_{in}(v) = \frac{|In(v) \cap Out(v)|}{|In(v)|}$,  where $In(v) = in-degree$  and $Out(v) = out-degree$    The insight is that Sybils are more likely to accept incoming requests than benign users in order to quickly propagate spam, resulting in a higher $Req_{in}$ .
    - **Outgoing requests accepted ratio:** $Req_{out}(v) = \frac{|In(v) \cap Out(v)|}{|Out(v)|}$.   The insight is that Sybils are less reliable  than benign users and hence their outgoing friend requests are less likely to be accepted, resulting in a lower $Req_{out}$.
    - **Local clustering coefficient: $CC(v)= \frac{|(i,j): i, j \in Nei(v); (i,j)\in E|}{|Nei(v)||1-Nei(v)|}$.** The insight is that benign users often have well-connected social cliques, and users in such cliques are often friends, resulting in to a high $CC$.
- **Training a SVM classifier:** Authors randomly sample $50$  benign nodes and $50$  Sybil nodes as the training set and train a SVM classifier [LIBSVM](https://www.csie.ntu.edu.tw/~cjlin/papers/libsvm.pdf), then output probabilistic estimates as local node scores.

### C. Evaluated Approaches

For SYBIL FUSE , authors propagate local scores through weighted random walk (RW) and weighted loopy belief propagation (LBP) to compute the final scores for identifying the labels (benign or sybil).

## Remarks

Feature Extraction plays an important role to use this scheme to classify the sybil identities in the case of Lido.

## References

1. SybilFuse: Combining Local Attributes with Global Structure to Perform Robust Sybil Detection, [https://arxiv.org/abs/1803.06772](https://arxiv.org/abs/1803.06772).
2. The Link Prediction Problem for Social Networks, [https://www.cs.cornell.edu/home/kleinber/link-pred.pdf](https://www.cs.cornell.edu/home/kleinber/link-pred.pdf)