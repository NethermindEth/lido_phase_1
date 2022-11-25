# Access with Fast Batch Verifiable Anonymous Credentials

Abstract: An anonymous credential-based access control system allows the user to prove possession of credentials to a resource guard that enforce access policies on one or more resources, whereby interactions involving the same user are unlinkable by the resource guard. This paper proposes three fast batch verifiable anonymous credential schemes. With all three schemes, the user can arbitrarily choose a portion of his access rights to prove possession of credentials while the number of expensive cryptographic computations spent is independent of the number of accessx rights being chosen. Moreover, the third anonymous credential scheme is not only fast batch verifiable but also fast fine-grained revocable, which means that to verify whether an arbitrarily chosen subset of credentials is revoked entails constant computation cost.
Classification: VC
Labels: Anonymous Credentials, Not Sybil resistant
Link to the paper: https://link.springer.com/book/10.1007/978-3-540-88625-9
Score: no idea
Score Phase 1: Not relevant
Year: 2008

# TL;DR

This paper proposes three verifiable anonymous credential systems which support batch verification using pairings. 

- An **issuer** gives a set of access rights to each user.
- Then users present their credential(s) (using their pseudonyms) to a resource guard (verifier).
- And the verifier can verify all of the credentials (of the same user) at the same time (checking whether two pairings are equal).

Its approach is a derivative of the known ones. On the other hand, it **does not address the Sybil attacks.** Moreover, the proposed schemes assume two centralized parties (except the first one), i.e. pseudonym authority and resource holder. In the first scheme, a single centralized party which has the responsibilities of two parties at the same time. 

# Introduction

In this paper there are mainly four types of parties:

1. The **User**
2. The **Pseudonym Authority (**$PA$**)** is the party that issues a pseudonym to the user. 
3. The r**esource holder (**$RH$**)** is the party who is responsible for 
    - managing resources,
    - issuing credentials,
    - granting resource access rights to the user.
4. The **Resource Guard (**$RG$**)** is the party who 
    - enforces access policies on the resources of one or more $RH$s and,
    - admits or denies (by verifying the user’s pseudonym and the credential) the user access to the resources according to the $RG$’s access control policies.

# Preliminary

## Definition (Bilinear pairings)

Assume two groups additive groups $\mathbb{G}_1, \mathbb{G}_2$ with prime order $q$. Let $\mathbb{G}_T$ the multiplicative target group with same order. Let  $g_1, g_2$ be generators of the groups $\mathbb{G}_1, \mathbb{G}_2$, respectively. A bilinear pairing $e$ is a map 

$$
e:\mathbb{G}_1 \times \mathbb{G}_2 \to \mathbb{G}_T
$$

which has the following properties;

1. **Bilinearity:** $e(a\cdot A, b\cdot B) = e(A,B)^{ab}$, for all $a,b \in \Z_q$ and for all elements $A\in \mathbb{G}_1$ and $B\in \mathbb{G}_2$, 
2. **Non-degeneracy:** $e(A,B) \ne 1$, for all elements $A\in \mathbb{G}_1$ and $B\in \mathbb{G}_2$.

## Definition (q-SDH Assumption)

For all PPT adversaries $\mathcal{A}$, $adv(k)$ defined as follows is a negligible function:

$$
(p, \mathbb{G}_1, \mathbb{G}_2, \mathbb{G}_T, g_1, g_2, e:\mathbb{G}_1 \times \mathbb{G}_2 \to \mathbb{G}_T) \gets Setup(1^k), a \in_R \mathbb{Z}_p\\
Pr[(x,y)\gets \mathcal{A}(g_2^{a}, g_2^{a^2}, \dots, g_2^{a^q}) : x \in \mathbb{Z}_p \wedge y =g_1^{1/(a+x)}] = adv(k)
$$

## Protocol 1 (used as HVZK)

Protocol 1 is an Honest Verifier Zero Knowledge (HVZK) Proof of knowledge of the triple $t \in \mathbb{G}_1,\tau\in\mathbb{Z}_p$ and $z \in \mathbb{Z}_p$. The system parameters for **Protocol 1** is a bilinear map, i.e.$\{p, \mathbb{G}_1, \mathbb{G}_2, \mathbb{G}_T, g_1, g_2, e:\mathbb{G}_1 \times \mathbb{G}_2 \to \mathbb{G}_T\}$, and the value $A\in\mathbb{G}_2$. Moreover, $h \in \mathbb{G}_1$ and $T = t^{\tau} \in \mathbb{G}_1$ are the common inputs for the prover and the verifier.

The Prover’s secret input is $t \in \mathbb{G}_1,\tau\in\mathbb{Z}_p$ and $z \in \mathbb{Z}_p$.

The goal of **Protocol 1** is to prove knowledge of $(t, \tau, z)$ such that $e(T,A) = e(h^{\tau}\cdot T^{-z}, g_2)$ and $T=t^{\tau}$, i.e. $e(t^{\tau},A\cdot g_2^z) = e(h^{\tau}, g_2)$.

Protocol proceeds as follows:

- The Prover chooses $(\alpha, \beta) \in_R \mathbb{Z}_p^2$
- The Prover computes $R = e(h^{\alpha}\cdot T^{-\beta}, g_2) \in \mathbb{G}_T$, and sends $R$ to the Verifier.
- The Verifier selects a challenge $c\in_R \mathbb{Z}_p$. and sends $c$ to the Prover.
- The Prover computes $(s_{\tau} = \alpha - c \cdot \tau, s_z = \beta - c \cdot z ) \in \mathbb{Z}_p^2$, and sends the pair $(s_{\tau}, s_z)$ to the Verifier.
- Verifier is convinced if and only if $T \in \mathbb{G}_1^*$ and $R = e(h^{s_{\tau}} \cdot T^{-s_z}, g_2 ) \cdot e(T,A)^c$

# Fast Batch Verifiable Anonymous Credential

## Formal definition

The fast batch verifiable anonymous credential is defined by the following five algorithms: 

- $PAKeyGen(⋅)$: It takes security parameters as inputs and outputs secret and public keys of $PA$, i.e. $sk^{PA}$ and $pk^{PA}$.
- $RHKeyGen(⋅)$: it takes $pk^{PA}$ and access right $R_{ij}$ that is under control of $RH_i$, and outputs access right secret and public keys, i.e. $sk_{ij}^{RH}$ and $pk_{ij}^{RH}$.
- $UserEnroll(⋅)$: It takes $sk^{PA}, pk^{PA}, n_{max}$(max number of admissible user), $U_l$ (user identity, and outputs user key $x_l$ and user pseudonym $nym_l$.
- $GCred(⋅)$: The credential issuance algorithm takes $pk^{PA} , nym_l, x_l$, access right $R_{ij}$corresponding access-right public key $pk_{ij}^{RH}$ and secret key $sk_{ij}^{RH}$, outputs credential $Cred_{ijl}$.
- $VCred(⋅)$: The credential verification algorithm takes $pk^{PA} , nym_l, x_l$, a set of access rights $\{R_{ij}\}$, corresponding access right public keys $\{pk_{ij}^{RH}\}$, and purported credentials $\{cred_{ijl}\}$, and outputs TRUE or FALSE.

# Scheme 1

This scheme has 4 types of players, i.e. the user, $RH$, $RG$, and the Portal Service ($PS$) that manages pseudonyms and access rights on behalf of $RH$. 

## The Algorithm $PSKeyGen(\cdot)$

$RHKeyGen(\cdot) \text{ and } PAKeyGen(\cdot)$

- Chooses a hash function, i.e. $Hash(\cdot):\{0,1\}^* \to \mathbb{G}_2$.
- Chooses $a \in_R \mathbb{Z}_p$
- Computes $A = g_2^a \in \mathbb{G}_2$
- The $PS$’s public key is $pk^{PS} = \{p, \mathbb{G}_1, \mathbb{G}_2, \mathbb{G}_T, g_1, g_2, e:\mathbb{G}_1 \times \mathbb{G}_2 \to \mathbb{G}_T, A, Hash(\cdot)\}$ and private key is $sk^{PS} = a$

## The Algorithm $GCred(\cdot)$

includes $UserEnroll(\cdot)$

- The user sends its identity $U_a$ to the $PS$,
- $PS$ queries its database for a stored secret key $z$ of $U_a$. If it cannot find, then it chooses $z\in_R \mathbb{Z}_p$ for $U_a$, and stores $(U_a, z)$ in the database.
- $PS$ computes $t_i = Hash(R_i)^{1/(a+z)}$, and sends the pair ($z,t_i$) to the user, where $R_i$ is the access right.
- User verifies that $e(t_i, A\cdot g_2^z) = e(Hash(R_i),g_2)$

## Fast Batch Verification of Anonymous Credentials

Assume that user $U_a$ has been granted access rights $\{R_1, \dots, R_n\}$. WLOG suppose that a subset $\{r_j\} \subseteq \{R_1, \dots, R_n\}$ of the user's access rights matches one of the $RG$’s policies, i.e. 

$$
Pol = \bigg(\{r_j\}, H=\prod_j Hash(r_j), \dots \bigg).
$$

Let $t_j$ denotes the user’s credential that corresponds to the access right $r_j$.

Define $VCred(\cdot)$ as $e(\prod_j t_j, A.g_2^z) = e(\prod_j Hash(r_j), g_2)$.

To prove to $RG$ that he meets the policy $Pol$, the users and $RG$ interact as follows:

- The user $U_a$ computes $t = \prod_j t_j$
- The user chooses $\tau\in_R \mathbb{Z}_p$
- The user computes the batch verifiable anonymous credential $T = t^{\tau}$, and sends it to $RG$.
- Using **Protocol 1,** $RG$ interacts with $U_a$ for
    
    $$
    KP = \bigg\{ (t,\tau,z): e(T,A)=e(H^{\tau} \cdot T^{-z}, g_2) \wedge T = t^{\tau}  \bigg\}.
    $$
    

If it outputs TRUE, then $RG$ is convinced.

# Scheme 2

This scheme has 4 types of players the user, $PA$, $RH$, and $RG$. 

## Algorithm $PAKeyGen(·)$

- Chooses $a \in_R \mathbb{Z}_p$
- Computes $A = g_2^a \in \mathbb{G}_2$.
- The $PA$’s public key is $pk^{PA} = (p, \mathbb{G}_1 ,\mathbb{G}_2, \mathbb{G}_T,g_1 ,g_2 ,e,A)$ and private key is $sk^{PA} = a$.

## Algorithm $RHKeyGen(·)$

Given $pk^{PA}$, the resource holder $RH_i$ who controls access rights $R_{ij},~ j = 1, 2, \dots, n_i$ proceeds as follow:

- For each $R_{ij}$, chooses $b_{ij} \in_R \mathbb{Z}_p$, and computes $B_{ij} = g_2^{b_{ij}} \in \mathbb{G}_2$.
- For each $R_{ij}$, generates a signature of knowledge proof
    
    $$
    \Sigma_{ij}=SKP \Big\{(b_{ij}): B_{ij}={g_2^{b_{ij}}} \Big\}.
    $$
    
- $RH_i$’s access right public key is $pk_{ij}^{RH} = \Big\{(R_{ij},B_{ij},\Sigma_{ij}) \Big\}$, and the private key is $sk_{ij}^{RH}=b_{ij}$.

## Algorithm $UserEnroll(.)$

In order to obtain a pseudonym, **a user with the identity** $U_u$ and the $PA$ proceeds as follows:

- The user sends its identity $U_u$ to $PA$.
- $PA$ checks his storage (whether there is a stored key $z_u$ for $U_u$).
    - If not, then it picks a random $z_u \in_R \mathbb{Z}_p$ for $U_u$ and
    - stores $(U_u,z_u)$ in its storage.
- $PA$ computes a $BB$ signature [[2]](https://doi.org/10.1007/978-3-540-24676-3_4), i.e. $t_u = g_1 ^{1/(a+z_u)}$, and sends user’s key $z_u$ and pseudonym $t_u$ to the user.
- The user verifies that $e(t_u, A \cdot g_2^{z_u}) =e(g_1, g_2)$

## Algorithm $GCred(.)$

To grant a credential for the access right $R_{ij}$, the user and the $RH_i$ proceed as follows.

- The user interacts with $RH_i$ for
    
    $$
    KP \Big\{ (z): e(t_u,A)/e(g_1,g_2) = e(t_u^{-z}, g_2) \Big\}
    $$
    
- If $KP \Big\{ (z): e(t_u,A)/e(g_1,g_2) = e(t_u^{-z}, g_2) \Big\}=TRUE$,
    - The $RH_i$ computes the credential $v_{ij} = t_u^{b_{ij}}$, and sends $v_{ij}$ to the user.
- User verifies $e(t_u, B_{ij})=e(v_{ij},g_2)$,
    - if it passes the verification, the user stores his credential $v_{ij}$ for access right $R_{ij}$.

## Fast Batch Verification of Anonymous Credentials

Suppose that the user $U_u$ has been granted the pseudonym $t_u$ and credentials for access rights $\{R_{ij}\}$ whose corresponding access-right public keys are $\{B_{ij}\}$. WLOG suppose that a subset $\{r_j\} \subseteq \{R_{ij}\}$ of the user's access rights matches the one of the RG’s policies, i.e. 

$$
Pol = \bigg(\{r_j\}, B=\prod_j B_j, \dots \bigg),
$$

where $B_j$ is the access-right public key that corresponds to resource $r_j$. Let $v_j$ denotes the user’s credential that corresponds to the access right $r_j$.

Define $VCred(\cdot)$ as $e(t_u, A.g_2^z) = e(g_1, g_2)$ and $e(t_u, B_j) = e(v_j, g_2).$

In order to prove to the $RG$ that he meets policy $Pol$ , the user $U_u$ carries out the following anonymous access control protocol with the $RG$:

- User $U_u$ selects $\tau \in_R \mathbb{Z}_p$
- User computes pseudonym $T=t_u^{\tau}$, and batch verifiable anonymous credential
    
    $$
    V = v^{\tau} = \Bigg(\prod_j v_j \Bigg)^{\tau}.
    $$
    
- User $U_u$ sends $T$ and $V$ to $RG$.
- $RG$ interacts with user $U_u$ for $KP\Big\{(t_u, \tau,z): e(T,A) = e(g_1^{\tau}\cdot T^{-z},g_2) \wedge T = t_u^{\tau}\Big\}$ using **Protocol 1**.
- If $KP\Big\{(t_u, \tau,z): e(T,A) = e(g_1^{\tau}\cdot T^{-z},g_2) \wedge T = t_u^{\tau}\Big\}=TRUE$, the $RG$ next verifies that $e(T,B) \stackrel{?}{=} e(V,g_2)$. If it is satisfied, then $RG$ is convinced.

# Scheme 3

This scheme is also a fast batch verifiable anonymous credential scheme. Different from the first two schemes, this has **fast fine-grained revocation** property.

In addition to the five algorithms defined in the above formal definition part, Scheme 3 also requires a revocation algorithm, i.e. 

$Revoke(.):$ takes as input $sk^{PA},~ R_{ij},~ pk_{ij}^{RH},~ x_l,~ cred_{ijl}$, and $\tilde{x}$ for which the credential for $R_{ij}$ needs revocation, and returns the updated ${pk_{ij}^{RH}}'$ and credential $Cred_{ijl}'$. 

Scheme 2 is slightly modified as follows:

## Algorithm $RHKeyGen(·)$

Given $PA$ public key $pk^{PA}$, the resource holder $RH_i$ that controls access rights $R_{ij},~ j=1, 2, \dots , n_i$, executes the following:

- For each $R_{ij}$, it chooses $b_{ij} \in_R \mathbb{Z}_p$ and computes $B_{ij} = g_2^{b_{ij}} \in \mathbb{G}_2$.
- For each $R_{ij}$, it computes access right revocation data $h_{ij} = g_1^{b_{ij}} \in \mathbb{G}_1$ and initializes
revocation list $RL_{ij} = \{(h_{ij}, \Delta)\}$ , where $\Delta$ denotes that the two-tuple $(h_{ij}, \Delta)$ is the first row in $RL_{ij}$ , i.e., no revocation happens yet.
- For each $B_{ij}$ and $h_{ij}$, it generates a signature of knowledge proof
    
    $$
    \Sigma_{ij}=SKP\Big\{(b_{ij}):B_{ij}=g_2^{b_{ij}} \wedge h_{ij}=g_1^{b_{ij}}\Big\}.
    $$
    
    `The $RH_i$’s public key is $pk_{ij}^{RH}=\Big\{\Big(R_{ij}, B_{ij}, \Sigma_{ij}, RL_{ij}\Big) \Big\}$ and secret key is $sk_{ij}^{RH} =b_{ij}$.
    

## Algorithm $GCred(.)$

In order to be granted access right $R_{ij}$ , the user $U_u$ carries out the following access-right-granting protocol with the resource holder $RH_i$. 

- User $U_u$ interacts with the $RH_i$ for $KP\Big\{ (z) : e(t_u,A)/e(g_1,g_2) = e(t_u^{-z}, g_2)  \Big\}$.
- If $KP\Big\{ (z) : e(t_u,A)/e(g_1,g_2) = e(t_u^{-z}, g_2) \Big\}=TRUE$, the $RH_i$ computes $v_{ij} = t_u^{b_{ij}}$, and sends $v_{ij}$ to the user $U_u$.
- The $U_u$ verifies that $e(t_u, B_{ij}) = e(v_{ij}, g_2)$ holds, and
    - stores $v_{ij}$ as his credential
    - stores $w_{ij}=v_{ij}$ as his validity data for access right $R_{ij}$.

## Algorithm $Revoke(.)$

Given a misbehaving user $\tilde{U}$ that has user key $\tilde{z}$,  to revoke his credential for access right $R_{ij}$, $PA$ needs to do the followings:

- $PA$ retrieves revocation data $h_{ij}$ from the last (latest) row of $RL_{ij}$.
- $PA$ computes $\tilde{h}_{ij} = h_{ij}^{1/(a+\tilde{z})}$ and appends $(\tilde{h}_{ij}, \tilde{z})$ to $RL_{ij}$.

Consider user $U_u$ that has user key $z$. User $U_u$ has credential $v_{ij}$ and validity data $w_{ij}$ for access right $R_{ij}$ as well. As a consequence of user $\tilde{U}$’s credential for access right $R_{ij}$ being revoked, user $U_u$ needs to execute the following to update his credential:

- The user $U_u$ computes $\tilde{w}_{ij} = (\tilde{h}_{ij} / w_{ij})^{1/(z - \tilde{z})}$, and updated his credential for access right $R_{ij}$ to $(v_{ij}, \tilde{w}_{ij})$.

## Fast Batch Verification of Anonymous Credentials

Suppose the user $U_u$ has been granted credentials for access rights $R_{ij}$ whose corresponding access-right public keys are $B_{ij}$. WLOG suppose one subset $\{r_{ij}\} \subseteq \{R_{ij}\}$ of the user’s access rights matches one of the $RG$’s policies, i.e.

$$
POL = \Bigg\{ \{r_j\}, B = \prod_j B_j, \dots   \Bigg\}
$$

where $B_j$ is the access-right public key that corresponds to resource $r_j$. Since $r_j \in \{R_{ij}\}$, we have that $B_j \in \{B_{ij}\}$.

Let $v_{ij}$ denote the users credential for the access right $r_j$. Let $w_{ij}$ denote the user’s current validity data, i.e. the data has been updated to include the latest revocation, on access right $r_j$.

The user $U_u$ wants to prove to the $RG$ that he meets policy $Pol$ . Whereas, the $RG$ is curious about whether the user’s access rights on $\{r_k\} \subseteq \{r_j\}$ have been revoked. Let $h_k$ denote the access right revocation data that is retrieved from the last row of $RL_k$.

Define $VCred(.)$ as $e(t_u, A\cdot g_2^{z}) \stackrel{?}{=} e(g_1, g_2)$,   $e(t_u, B_j) \stackrel{?}{=} e(v_j, g_2)$ and $e(w_k, A\cdot g_2^{z}) \stackrel{?}{=} e(h_k, g_2)$.

In order to convince the $RG$, the user $U_u$ carries out the following anonymous access control protocol with the $RG$:

- $U_u$ selects $\tau \in_R \mathbb{Z}_p$, and computes pseudonym $T = t_u^{\tau}$.
- $U_u$ batches verifiable anonymous credential $V = v^{\tau} = \Bigg(\prod_j v_j \Bigg)^{\tau}$.
- $U_u$ computes fine-grained validity data $W = w^{\tau} = \Bigg( \prod_k w_k\Bigg)^{\tau}$.
- $U_u$ sends $T,V$ and $W$ to the $RG$.
- Using **Protocol 1,** the $RG$ interacts with $U_u$ for

$$
KP = \Bigg\{\Big(t_u, w, \tau, z\Big): e(T,A) = e(g_1^{\tau}\cdot T^{-z}, g_2)\wedge T = t_u^{\tau} \wedge e(W,A) = e((\prod_k h_k)^{\tau} \cdot W^{-z},g_2) \wedge W= w^{\tau}\Bigg\}.
$$

- If the $RG$ accepts the above knowledge proof, it further verifies that $e(T,B)\stackrel{?}{=}e(V,g_2)$. If the congruence holds, then the $RG$ is convinced.

# References

1. Zeng, K. (2008). Access with Fast Batch Verifiable Anonymous Credentials. In: Chen, L., Ryan, M.D., Wang, G. (eds) Information and Communications Security. ICICS 2008. Lecture Notes in Computer Science, vol 5308. Springer, Berlin, Heidelberg. [https://doi.org/10.1007/978-3-540-88625-9_5](https://doi.org/10.1007/978-3-540-88625-9_5)
2. Boneh, D., Boyen, X. (2004). Short Signatures Without Random Oracles. In: Cachin, C., Camenisch, J.L. (eds) Advances in Cryptology - EUROCRYPT 2004. EUROCRYPT 2004. Lecture Notes in Computer Science, vol 3027. Springer, Berlin, Heidelberg. [https://doi.org/10.1007/978-3-540-24676-3_4](https://doi.org/10.1007/978-3-540-24676-3_4)