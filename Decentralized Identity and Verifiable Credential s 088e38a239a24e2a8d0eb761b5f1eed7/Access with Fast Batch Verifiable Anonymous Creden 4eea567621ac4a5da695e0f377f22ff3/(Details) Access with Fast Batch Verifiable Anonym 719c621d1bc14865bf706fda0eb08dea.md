# (Details) Access with Fast Batch Verifiable Anonymous Credentials

### q-SDH Assumption.

For all PPT adversaries $\mathcal{A}$, $adv(k)$ defined as follows is a negligible function:

$$
(p, \mathbb{G}_1, \mathbb{G}_2, \mathbb{G}_T, g_1, g_2, e:\mathbb{G}_1 \times \mathbb{G}_2 \to \mathbb{G}_T) \gets Setup(1^k), a \in_R \mathbb{Z}_p\\
Pr[(x,y)\gets \mathcal{A}(g_2^{a}, g_2^{a^2}, \dots, g_2^{a^q}) : x \in \mathbb{Z}_p \wedge y =g_1^{1/(a+x)}] = adv(k)
$$

### Protocol 1 (used as HVZK)

Protocol 1 is an Honest Verifier Zero Knowledge (HVZK) Proof of knowledge of $t \in \mathbb{G}_1,\tau\in\mathbb{Z}_p$ and $z \in \mathbb{Z}_p$.

The system parameters for **Protocol 1** is a bilinear map $\{p, \mathbb{G}_1, \mathbb{G}_2, \mathbb{G}_T, g_1, g_2, e:\mathbb{G}_1 \times \mathbb{G}_2 \to \mathbb{G}_T\}$ and the value $A\in\mathbb{G}_2$. Moreover, $h \in \mathbb{G}_1$ and $T = t^{\tau} \in \mathbb{G}_1$ are the common inputs for the prover and the verifier.

The Prover’s secret input is $t \in \mathbb{G}_1,\tau\in\mathbb{Z}_p$ and $z \in \mathbb{Z}_p$.

The goal of **Protocol 1** is to prove knowledge of $(t, \tau, z)$ such that $e(T,A) = e(h^{\tau}\cdot T^{-z}, g_2)$ and $T=t^{\tau}$, i.e. $e(t^{\tau},A\cdot g_2^z) = e(h^{\tau}, g_2)$.

Protocol proceeds as follows:

- The Prover chooses $(\alpha, \beta) \in_R \mathbb{Z}_p^2$
- The Prover computes $R = e(h^{\alpha}\cdot T^{-\beta}, g_2) \in \mathbb{G}_T$, and sends $R$ to the Verifier.
- The Verifier selects a challenge $c\in_R \mathbb{Z}_p$. and sends $c$ to the Prover.
- The Prover computes $(s_{\tau} = \alpha - c \cdot \tau, s_z = \beta - c \cdot z ) \in \mathbb{Z}_p^2$, and sends the pair $(s_{\tau}, s_z)$ to the Verifier.
- Verifier is convinced if and only if $T \in \mathbb{G}_1^*$ and $R = e(h^{s_{\tau}} \cdot T^{-s_z}, g_2 ) \cdot e(T,A)^c$

# Fast Batch Verifiable Anonymous Credential

### Formal definition

Fast batch verifiable anonymous credential is defined as five algorithms: 

- $PAKeyGen(⋅)$: It takes security parameter as input and outputs secret and public keys of $PA$, i.e. $sk^{PA}$ and $pk^{PA}$.
- $RHKeyGen(⋅)$: it takes $pk^{PA}$ and access right $R_{ij}$ that is under control of $RH_i$, and outputs access right secret and public keys, i.e. $sk_{ij}^{RH}$ and $pk_{ij}^{RH}$.
- $UserEnroll(⋅)$: It takes $sk^{PA}, pk^{PA}, n_{max}$(max number of admissible user), $U_l$ (user identity, and outputs user key $x_l$ and user pseudonym $nym_l$.
- $GCred(⋅)$: The credential issuance algorithm takes $pk^{PA} , nym_l, x_l$, access right $R_{ij}$corresponding access-right public key $pk_{ij}^{RH}$ and secret key $sk_{ij}^{RH}$, outputs credential $Cred_{ijl}$.
- $VCred(⋅)$: The credential verification algorithm takes $pk^{PA} , nym_l, x_l$, a set of access rights $\{R_{ij}\}$, corresponding access right public keys $\{pk_{ij}^{RH}\}$, and purported credentials $\{cred_{ijl}\}$, and outputs TRUE or FALSE.

# Scheme 1

This scheme has 4 types of players, i.e. user, $RH$, $RG$, and Portal Service ($PS$) who manages pseudonyms and access rights on behalf of $RH$. Secure in the Random Oracle Model (ROM).

### The Algorithm $PSKeyGen(\cdot)$

$RHKeyGen(\cdot) + PAKeyGen(\cdot)$

- Chooses a hash function $Hash(\cdot):\{0,1\}^* \to \mathbb{G}_2$.
- Chooses $a \in_R \mathbb{Z}_p$
- Computes $A = g_2^a \in \mathbb{G}_2$
- The $PS$’s public key is $pk^{PS} = \{p, \mathbb{G}_1, \mathbb{G}_2, \mathbb{G}_T, g_1, g_2, e:\mathbb{G}_1 \times \mathbb{G}_2 \to \mathbb{G}_T, A, Hash(\cdot)\}$ and private key is $sk^{PS} = a$

### The Algorithm $GCred(\cdot)$

includes $UserEnroll(\cdot)$

- The user sends its identity $U_a$ to the $PS$,
- $PS$ queries its database for a stored secret key $z$ of $U_a$. If it cannot find, then it chooses $z\in_R \mathbb{Z}_p$ for $U_a$, and stores $(U_a, z)$ in the database.
- $PS$ computes $t_i = Hash(R_i)^{1/(a+z)}$, and sends the pair ($z,t_i$) to the user, where $R_i$ is the access right.
- User verifies that $e(t_i, A\cdot g_2^z) = e(Hash(R_i),g_2)$

### Fast Batch Verification of Anonymous Credentials

Assume that user $U_a$ has been granted access rights $\{R_1, \dots, R_n\}$. WLOG suppose that a subset $\{r_j\} \subseteq \{R_1, \dots, R_n\}$ of the users access rights matches the one of the $RG$’s policies, i.e. 

$$
Pol = \bigg(\{r_j\}, H=\prod_j Hash(r_j), \dots \bigg).
$$

Let $t_j$ denotes the user’s credential that corresponds to the access right $r_j$.

Define $VCred(\cdot)$ as $e(\prod_j t_j, A.g_2^z) = e(\prod_j Hash(r_j), g_2)$.

To prove to $RG$ that he meets the policy $Pol$, the users and $RG$ interact as follows:

- The user $U_a$ computes $t = \prod_j t_j$
- The user chooses $\tau\in_R \mathbb{Z}_p$
- The user computes the batch verifiable anonymous credential $T = t^{\tau}$, and sends it to $RG$.
- $RG$ interacts with $U_a$ for
    
    $$
    KP = \bigg\{ (t,\tau,z): e(T,A)=e(H^{\tau} \cdot T^{-z}, g_2) \wedge T = t^{\tau}  \bigg\}
    $$
    

using **Protocol 1.** If it outputs TRUE, then RG is convinced.

# Scheme 2

This scheme has 4 types of players the user, $PA$, $RH$ and $RG$. Security of the Scheme 2 does not rely on the ROM.

### Algorithm $PAKeyGen(·)$

- Chooses $a \in_R \mathbb{Z}_p$
- Computes $A = g_2^a \in \mathbb{G}_2$.
- The $PA$’s public key is $pk^{PA} = (p, \mathbb{G}_1 ,\mathbb{G}_2, \mathbb{G}_T,g_1 ,g_2 ,e,A)$ and private key is $sk^{PA} = a$.

### Algorithm $RHKeyGen(·)$

Given $pk^{PA}$, the resource holder $RH_i$ who controls access rights $R_{ij},~ j = 1, 2, \dots, n_i$ proceeds as follow:

- For each $R_{ij}$, chooses $b_{ij} \in_R \mathbb{Z}_p$, and computes $B_{ij} = g_2^{b_{ij}} \in \mathbb{G}_2$.
- For each $R_{ij}$, generates a signature of knowledge proof
    
    $$
    \Sigma_{ij}=SKP \Big\{(b_{ij}): B_{ij}={g_2^{b_{ij}}} \Big\}.
    $$
    
- $RH_i$’s access right public key is $pk_{ij}^{RH} = \Big\{(R_{ij},B_{ij},\Sigma_{ij}) \Big\}$, and the private key is $sk_{ij}^{RH}=b_{ij}$.

### Algorithm $UserEnroll(.)$

In order to obtain a pseudonym, **a user who has trustworthy identity** $U_u$ carries out the following with the $PA$:

- User sends its identity $U_u$ to $PA$.
- $PA$ check whether there is a stored key $z_u$ in its database for $U_u$.
    - If it cannot find a stored key, then it chooses $z_u \in_R \mathbb{Z}_p$ for $U_u$.
    - Stores $(U_u,z_u)$ in its database.
- $PA$ computes a $BB$ signature [Boneh-Boyen,2004], i.e. $t_u = g_1 ^{1/(a+z_u)}$, and sends user key $z_u$ and pseudonym $t_u$ to $U_u$.
- User $U_u$ verifies that $e(t_u, A \cdot g_2^{z_u}) =e(g_1, g_2)$

### Algorithm $GCred(.)$

The user $U_u$ interacts with the resource holder $RH_i$ to grant a credential for the access right $R_{ij}$ as follows.

- $U_u$ interacts with $RH_i$ for
    
    $$
    KP \Big\{ (z): e(t_u,A)/e(g_1,g_2) = e(t_u^{-z}, g_2) \Big\}
    $$
    
- If $KP \Big\{ (z): e(t_u,A)/e(g_1,g_2) = e(t_u^{-z}, g_2) \Big\}=TRUE$, resource holder $RH_i$ computes $v_{ij} = t_u^{b_{ij}}$, and sends $v_{ij}$ to the user.
- User verifies $e(t_u, B_{ij})=e(v_{ij},g_2)$, and if it holds he stores $v_{ij}$ as his credential for access right $R_{ij}$.

### Fast Batch Verification of Anonymous Credentials

Suppose that the user $U_u$ has been granted pseudonym $t_u$ and credentials for access rights $\{R_{ij}\}$ whose corresponding access-right public keys are $\{B_{ij}\}$. WLOG suppose that a subset $\{r_j\} \subseteq \{R_{ij}\}$ of the users access rights matches the one of the RG’s policies, i.e. 

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

### Algorithm $RHKeyGen(·)$

Given $PA$ public key $pk^{PA}$, the resource holder $RH_i$ that controls access rights $R_{ij},~ j=1, 2, \dots , n_i$, executes the following:

- For each $R_{ij}$, it chooses $b_{ij} \in_R \mathbb{Z}_p$ and computes $B_{ij} = g_2^{b_{ij}} \in \mathbb{G}_2$.
- For each $R_{ij}$, it computes access right revocation data $h_{ij} = g_1^{b_{ij}} \in \mathbb{G}_1$ and initializes
revocation list $RL_{ij} = \{(h_{ij}, \Delta)\}$ , where $\Delta$ denotes that the two-tuple $(h_{ij}, \Delta)$ is the first row in $RL_{ij}$ , i.e., no revocation happens yet.
- For each $B_{ij}$ and $h_{ij}$, it generates a signature of knowledge proof
    
    $$
    \Sigma_{ij}=SKP\Big\{(b_{ij}):B_{ij}=g_2^{b_{ij}} \wedge h_{ij}=g_1^{b_{ij}}\Big\}.
    $$
    
    `The $RH_i$’s public key is $pk_{ij}^{RH}=\Big\{\Big(R_{ij}, B_{ij}, \Sigma_{ij}, RL_{ij}\Big) \Big\}$ and secret key is $sk_{ij}^{RH} =b_{ij}$.
    

### Algorithm $GCred(.)$

In order to be granted access right $R_{ij}$ , the user $U_u$ carries out the following access-right-granting protocol with the resource holder $RH_i$. 

- User $U_u$ interacts with the $RH_i$ for $KP\Big\{ (z) : e(t_u,A)/e(g_1,g_2) = e(t_u^{-z}, g_2)  \Big\}$.
- If $KP\Big\{ (z) : e(t_u,A)/e(g_1,g_2) = e(t_u^{-z}, g_2) \Big\}=TRUE$, the $RH_i$ computes $v_{ij} = t_u^{b_{ij}}$, and sends $v_{ij}$ to the user $U_u$.
- The $U_u$ verifies that $e(t_u, B_{ij}) = e(v_{ij}, g_2)$ holds, and
    - stores $v_{ij}$ as his credential
    - stores $w_{ij}=v_{ij}$ as his validity data for access right $R_{ij}$.

### Algorithm $Revoke(.)$

Given a misbehaving user $\tilde{U}$ that has user key $\tilde{z}$,  to revoke his credential for access right $R_{ij}$, $PA$ needs to do the followings:

- $PA$ retrieves revocation data $h_{ij}$ from the last (latest) row of $RL_{ij}$.
- $PA$ computes $\tilde{h}_{ij} = h_{ij}^{1/(a+\tilde{z})}$ and appends $(\tilde{h}_{ij}, \tilde{z})$ to $RL_{ij}$.

Consider user $U_u$ that has user key $z$. User $U_u$ has credential $v_{ij}$ and validity data $w_{ij}$ for access right $R_{ij}$ as well. As a consequence of user $\tilde{U}$’s credential for access right $R_{ij}$ being revoked, user $U_u$ needs to execute the following to update his credential:

- The user $U_u$ computes $\tilde{w}_{ij} = (\tilde{h}_{ij} / w_{ij})^{1/(z - \tilde{z})}$, and updated his credential for access right $R_{ij}$ to $(v_{ij}, \tilde{w}_{ij})$.

### Fast Batch Verification of Anonymous Credentials

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