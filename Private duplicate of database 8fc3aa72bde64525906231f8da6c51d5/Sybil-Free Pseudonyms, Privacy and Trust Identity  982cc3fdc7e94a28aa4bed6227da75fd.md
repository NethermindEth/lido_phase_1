# Sybil-Free Pseudonyms, Privacy and Trust: Identity Management in the Internet of Services

Abstract: We propose an identity management system that supports role-based pseudonyms that are bound to a given set of services (service contexts) and support the use of reputation systems. Our proposal offers a solution for the problem of providing privacy protection and reputation mechanisms concurrently. The trust information used to evaluate the reputation of users is dynamic and associated to their pseudonyms. In particular, our solution does not require the support or assistance from central authorities during the operation phase. Moreover, the presented scheme provides inherent detection and mitigation of Sybil attacks. Finally, we present an attacker model and evaluate the security and privacy properties and robustness of our solution.
Labels: Anonymity revocation, Classic reference, Management of credentials, Possible tool in larger solution, Worthwile Sybil resistance insights
Link to the paper: https://www.researchgate.net/publication/220586747_Sybil-Free_Pseudonyms_Privacy_and_Trust_Identity_Management_in_the_Internet_of_Services
Score: no idea
Score Phase 1: Relevant
Year: 2011

# Scenario and notation

An arbitrary number of service providers $s_i \in \mathcal{S} |1\leq i \leq |\mathcal{S}|$ offers services to a set of users $u_i\in \mathcal{U}|1\leq i \leq |\mathcal{U}|$ . Also, a set of similar services is grouped in a service context set $\mathcal{C}^i \in \mathcal{C}|1\leq i \leq |\mathcal{C}|$.

There exist two sets of identifiers within each service context. The set $\mathcal{S}^i$ refers to the identifiers of the service providers and the set $\mathcal{P}^i$ refers to the identifiers of the customers that want to use services in a specific context($|\mathcal{P}^i|\leq |\mathcal{U}|$).

For customers in $\mathcal{U}$, an identity management scheme is created so that users can create a pseudonym $p_u^{C^i}$ per service context.

![Relation between users and service providers within the context of the services. Taken from [https://www.researchgate.net/publication/220586747_Sybil-Free_Pseudonyms_Privacy_and_Trust_Identity_Management_in_the_Internet_of_Services](https://www.researchgate.net/publication/220586747_Sybil-Free_Pseudonyms_Privacy_and_Trust_Identity_Management_in_the_Internet_of_Services)](Sybil-Free%20Pseudonyms,%20Privacy%20and%20Trust%20Identity%20%20982cc3fdc7e94a28aa4bed6227da75fd/Mon_Nov_14_082843_PM_CST_2022.png)

Relation between users and service providers within the context of the services. Taken from [https://www.researchgate.net/publication/220586747_Sybil-Free_Pseudonyms_Privacy_and_Trust_Identity_Management_in_the_Internet_of_Services](https://www.researchgate.net/publication/220586747_Sybil-Free_Pseudonyms_Privacy_and_Trust_Identity_Management_in_the_Internet_of_Services)

| ⁍ | service provider i  |
| --- | --- |
| ⁍ | User(customer) j |
| ⁍ | Set of service providers |
| ⁍ | Set of users |
| ⁍ | Service context |
| ⁍ | pseudonym of user ⁍ in context ⁍ |
| ⁍ | service providers within a service context ⁍ |
| ⁍ | set of pseudonyms within a service context ⁍ |

The protocol uses pseudonyms to prevent histories from being linked to a user's real identity, the pseudonyms provide an establishment of trust in a way that knowing a pseudonym is only possible within a service context.

## Objectives

1. Provide a unique long-term identifier as a basis of trust or reputation
2. Providing unlinkability between users’ behaviors in different service contexts.
3. Being able to detect Sybil identifiers

# Algorithms for Pseudonym Construction

- $IKg(1^k)\rightarrow (pk_{TTP},sk_{TTP})$: Algorithm for creating the key pair of a Trusted Party Issuer.
- $UKg(1^k,pk_{TTP})\rightarrow (pk_u,sk_u)$: Algorithm for creating the user’s key pair
- $(Obtain(pk_{TTP},sk_u), Issue(pk_u,sk_{TTP}))\rightarrow (u,r_u)$: $u$ is an e-token that serves as an identifier and $r_u$ is the revocation information
- $Sign(pk_{u,C^i},u,pk_{TTP},C^i)\rightarrow (S,\tau,u’)$
    - $S$: pseudorandom pseudonym(a token serial number)
    - $\tau$: Pseudonym certificate(NIZK proof that values computed in this algorithm correspond to sign values from TTP)
    - $u’$: Updated token dispenser
    - $(pk_{u,C^i},S,\tau)$ corresponds to self certified Sybil-free pseudonym for context $C^i$
- $Verify(pk_{u,C^i},S,\tau,pk_{TTP},C^i)\rightarrow (true,false)$
- $Identity(pk_{TTP},S,\tau,\tau ‘,pk_{u,C^i},pk’_{u,C^i})\rightarrow pk_u$: If a user $u$ generates more than one pseudonym for a given service context it is possible to compute the public key that was used when requesting its initial identifier from TTP
- $Revoke(sk_{TTP},pk_{TTP},r_u)\rightarrow pk’_{TTP}$: The user $u$ is revoked by generating and updated public key of the issuer TTP

More info on algorithms in the papers: [https://link.springer.com/chapter/10.1007/978-3-540-24676-3_34](https://link.springer.com/chapter/10.1007/978-3-540-24676-3_34) and [https://dl.acm.org/doi/10.1145/1352533.1352558](https://dl.acm.org/doi/10.1145/1352533.1352558)

# Identity Management Scheme

### Bootstrapping

Each user and service provider in the system has its own unique identifier(Maybe implementing a DID). 

### Setting up service context

Anyone can create a service context. A tag is provided that specifies the service name, region of availability, etc. This tag is later hashed to a unique value that is used as input for the creation of pseudonyms that uses the service context.

![Taken from [https://www.researchgate.net/publication/220586747_Sybil-Free_Pseudonyms_Privacy_and_Trust_Identity_Management_in_the_Internet_of_Services](https://www.researchgate.net/publication/220586747_Sybil-Free_Pseudonyms_Privacy_and_Trust_Identity_Management_in_the_Internet_of_Services)](Sybil-Free%20Pseudonyms,%20Privacy%20and%20Trust%20Identity%20%20982cc3fdc7e94a28aa4bed6227da75fd/Sun_Nov_20_093601_PM_CST_2022.png)

Taken from [https://www.researchgate.net/publication/220586747_Sybil-Free_Pseudonyms_Privacy_and_Trust_Identity_Management_in_the_Internet_of_Services](https://www.researchgate.net/publication/220586747_Sybil-Free_Pseudonyms_Privacy_and_Trust_Identity_Management_in_the_Internet_of_Services)

### Creating user pseudonyms

Pseudonyms are created by the user and are bound to a service context. This is created from the identifier issued by a trusted party, the tag of the service context, and a key pair(from the user?). 

The pseudonym is just a new key pair, a serial number, and a zk proof of the correctness of the pseudonym generation.

### Using the pseudonyms

Pseudonyms can be used for reputation scores among other things.

### Expiration of pseudonyms and service context

A service context is valid over the time frame that it was specified to work on, when this happens all pseudonyms bound to it become invalid. 

A user can delete its’s pseudonym but because the identifier is used for the creation it cannot create a new one from an identifier. The pseudonym must be restored if the user wants to use the service context again.

# Security

Whitewashing is not possible because users can only create one pseudonym per service context. A user that creates another pseudonym can be detected under the cryptographic construction above by comparing the pseudonym with an already-known pseudonym.

The above requires $\binom{n-1}{2}$ pairwise comparisons.

## Dealing with Sybil attacks efficiently.

A user $A$ evaluates the trustworthiness of a service provider $C$ and receives recommendations from other recommenders $R_0,R_1,\dots ,R_m$

![Sun Nov 20 10:18:10 PM CST 2022.png](Sybil-Free%20Pseudonyms,%20Privacy%20and%20Trust%20Identity%20%20982cc3fdc7e94a28aa4bed6227da75fd/Sun_Nov_20_101810_PM_CST_2022.png)

Recommendations from $R_i$ are given as a tuple of positive and negative evidence $(r_i,s_i)$, and $A$ has information about the trustworthiness of each $R_i$ denoted as $t_i^A\in[0,1]$. The sub-index of a recommender represents the rank of trustworthiness, where rank $1$ means most trusted, i.e. $R_i$ is sorted such that $t_i^A\geq t_{i+1}^A$. 

Thus the evidence can be aggregated in the following manner

$$
(r_{agg},s_{agg})=\left(\sum_{i=0}^m min\left\{ t_i^A\cdot r_i,\, (1-t_s)\cdot (t_i^A)^i\cdot\frac{N_R}{r_i+s_i}\cdot r_i\right\},
\sum_{i=0}^m min\left\{ t_i^A\cdot s_i,\, (1-t_s)\cdot (t_i^A)^i\cdot\frac{N_R}{r_i+s_i}\cdot s_i\right\}
\right)
$$

Where $t_s\in [0,1]$ is the threshold for Sybil attacks and $N_R$ is the maximum number of evidence that $A$ would ask for so that it believes is enough to be a good representation for the future.

The final trust value of $C$ would be

$$
\frac{r_{agg}+1}{r_{agg}+s_{agg}+2}
$$

Furthermore, the impact of recommender $j$ can be evaluated as 

$$
imp(j)=\sum_{i=j}^mmin\left\{t_i^A\cdot r_i,\, (1-t_s)\cdot (t_i^A)^i\cdot \frac{N_R}{r_i+s_i}\cdot r_i\right\}\\
+
\sum_{i=j}^mmin\left\{t_i^A\cdot s_i,\, (1-t_s)\cdot (t_i^A)^i\cdot \frac{N_R}{r_i+s_i}\cdot s_i\right\}
$$

Which has a bound of $(1-t_s)\cdot N_R\sum_{i=j}^m(t_i^A)^i\leq (1-t_s)\frac{(t_i^A)^i}{1-t_i^A}$.

Next a threshold for relevance is define as $t_{imp}=\frac{(1-t_s)N_R}{f}$ for a parameter $f$.

Then a negligent rank $j_{neg}$ where the recommenders stop to be relevant for calculations, can be defined as

$$
j_{neg}=min\left\{j\in\mathbb{N}\bigg|\frac{1}{f}\geq\frac{(t_i^A)^i}{1-t_i^A}\right\}
$$

So for making the pair-wise comparisons of each pseudonym, only the recommendations from $1$ until $j_{neg}$ are taken into account, alleviating the computation burden.