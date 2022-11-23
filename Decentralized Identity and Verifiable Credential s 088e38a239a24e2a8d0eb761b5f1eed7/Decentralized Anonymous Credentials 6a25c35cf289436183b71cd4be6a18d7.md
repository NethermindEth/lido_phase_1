# Decentralized Anonymous Credentials

Abstract: Anonymous credentials provide a powerful tool for making assertions about identity while maintaining privacy. However, a limitation of today’s anonymous credential systems is the need for a trusted credential issuer — which is both a single point of failure and a target for compromise. Furthermore, the need for such a trusted issuer can make it challenging to deploy credential systems in practice, particularly in the ad hoc network setting (e.g., anonymous peer-to-peer networks) where no single party can be trusted with this responsibility. In this work we propose a novel anonymous credential scheme that eliminates the need for a trusted credential issuer. Our approach builds on recent results in the area of electronic cash that, given a public append-only ledger, do not need a trusted credential issuer. Furthermore, given a distributed public ledger, as in, e.g., Bitcoin, our system requires no credential issuer at all and hence is decentralized. Using such a public ledger and standard cryptographic primitives, we propose and provide a proof of security for a basic anonymous credential system that allows users to make flexible identity assertions with strong privacy guarantees without relying on trusted parties. Finally, we discuss a number of practical applications for our techniques, including resource management in ad hoc networks and prevention of Sybil attacks. We implement our scheme and measure its efficiency.
Added to deliverable?: No
Already read?: Yes
Assigned readers: Basireddy Swaroopa Reddy
Classification: Anonymous Credentials, VC
Date of publication: 2014
Labels: Cryptographic primitive (Anonymous Credential), Decentralized Issuer
Link to the paper: https://www.cs.purdue.edu/homes/clg/files/NDSS14.pdf
MZ checked the note: Yes
Presentation date: October 10, 2022
Reviewers: Jorge Arce-Garro
Score Phase 1: Very relevant
Work Group: Academic literature

## Introduction

Anonymous credentials provide a powerful tool for making assertions about identity while maintaining privacy. However, a limitation of anonymous credential systems is the need for a trusted credential issuer — which is both a single point of failure and a target for compromise.

In this paper, the authors propose a novel anonymous credential scheme that eliminates the need for a trusted credential issuer. Given an append-only decentralized ledger (e.g., Bitcoin), this scheme requires **no credential issuer** at all and hence it is decentralized.

## Paper’s Contribution

- **Decentralized Anonymous Credential System:** Propose anonymous credential systems without needing a trusted and central credential issuer. To achieve this goal, the protocol requires existence of a *public append-only ledger*.
    - This ledger be maintained in a distributed manner that need not require a trusted party or parties. (Best possible implementation is **blockchain**)
    - The  identity claims used in issuing credentials must be verifiable by everyone participating in the system.
- The paper shows how to extend proposed credential scheme to create updatable (e.g., stateful) anonymous credentials in which users obtain new credentials based on changing properties of their identity.
- Authors also show several immediate applications of Decentralized Anonymous Credentials
    - **Decentralized Direct Anonymous Attestation (dDAA)**: To decentralize the Direct Anonymous Attestation protocol, allowing individual collections of nodes in an ad hoc or distributed system to securely assert properties of their system state.
    - **Anonymous resource management in ad hoc networks:** Peer-to-peer networks are vulnerable to impersonation attacks, where a single party simulates many different peers in order to gain advantage against the network. The basic approach to mitigate those attacks is to construct an **anonymous subscription service** where parties may establish unique or costly pseudonyms (for example by submitting a valid TPM (Trusted Platform Module) credential or paying a sum of digital currency). They can then assert possession on their identity under a specific set of restrictions, e.g., a limit to the number of requests they can make in each time period (k-show credentials).
    - **Auditable credentials:** These techniques may also be used to extend existing centralized credential systems by allowing for public audit of issued credentials. This helps to guard against compromised credential issuers and allows the network to easily detect and revoke inappropriate credential grants. For example, in Direct Anonymous Attestation (DAA) one might want to prevent a malicious DAA authority from granting certificates to users who do not have a TPM or whose TPM did not attest.

## Overview of the Construction

### Issuing the credentials:

- The user establishes an identity and corresponding attributes
- The user attaches a vector commitment to her secret key $sk_U$,  along with the identity and attribute strings contained in its identity assertion.

       Example: 

  **Identity:** Validator public key or validator index

       **Attributes:** missed_attestations, missed_blocks, etc.

       **Identity assertion:** To show Authenticity proofs obtained from Oracles for accessing attributes 

- User includes a non-interactive proof that the credential is correctly constructed. The network will accept the identity assertion iff the assertion is considered correct and the proof is valid.

### Showing Credentials:

The user proves the following statements in Zero-Knowledge - 

1. User knows a commitment $C_i$ in the set  $(C_1, C_2, \dots  , C_N)$ of all credentials previously accept
2. User knows the opening (randomness) for the commitment.
3. User prove additional statements about the identity and attributes contained within the commitment $C_i$.

## DECENTRALIZED ANONYMOUS CREDENTIALS

A traditional anonymous credential system has two types of participants: **users** and **organizations.** 

**Notations:**

1. User secret key: $sk_U$
2. The pseudonym of user $A$  to organization $O$: $Nym^O_A$
3. Credential: $c$
4. Set of the credentials issued by the Organization: $C_O$
5. The auxiliary information (for example, identity assertion, organization name, etc): $aux$

**Note:** In decentralized anonymous credentials no single party represents the organization. Instead, a **quorum of  users** who enforce a specific credential issuing policy and collaboratively maintain a list of credentials issued so far.

The distributed anonymous credentials consists of a global distributed ledger, a list of transaction semantics and the following algorithms (possibly probabilistic) - 

- $Setup(1^{\lambda}) \rightarrow params$ : Generates the system parameters.
- $KeyGen(params) \rightarrow sk_U$: Run by a user to generate her secret key.
- $FormNym(params, U, E, sk_U ) \rightarrow (Nym^E_U, sk_{Nym^E_U}, U, E
)$: Run by a user to generate a pseudonym $Nym^E_U$ and an authentication key  $sk_{Nym^E_U}$ between a user U and some entity (either a user or an organization) E.
- $MintCred(params, sk_U, Nym^O_U, sk_{Nym^O_U}, U, aux) \rightarrow (c, sk_c, \pi_M)$:
    - Run by a user to generate a request for a credential from organization $O$.
    - The request consists of a candidate credential $c$ containing public attributes $attrs$; the user’s key $sk_U$; auxiliary data $aux$ justifying the granting of the credential (e.g., authenticity proofs from Oracles)
    - a proof $\pi_M$ that (1) $Nym^O_U$ was issued to the same $sk_U$ and (2) the credential embeds $attrs$.
- $MintVerify(params, c, Nym^O_U , aux, π_M) \rightarrow \{0, 1\}$: Run by nodes in the organization to validate a credential. Returns $1$ if $\pi_M$ is valid,  $0$ otherwise.
- $Show(params, sk_U , Nym^V_U , sk_{ Nym^V_U} , c, sk_c , C_O ) \rightarrow \pi_S$ :  Run by a user to non -interactively prove that a given set of attributes are in a credential $c$ in the set of issued
credentials $C_O$ and that $c$ was issued to the same person who owns $Nym^V_U$ . Generates and returns a proof $\pi_S$.
- $ShowVerify(params, Nym^V_U , \pi_S , C_O ) \rightarrow \{0, 1\}$:  Run by a verifier to validate a shown credential. Return $1$ if $\pi_S$ is valid for $Nym^V_U$ , $0$ otherwise.

The description for how these algorithms are used in the decentralized anonymous credentials

### A. Overview of the Protocol Semantics

In this system,  authors integrate the above algorithms with a decentralized hash chain network (Blockchain)  as follows. 

**Formulating a pseudonym:** Generated by user offline

- The user $U$ generates it’s secret key $sk_U$.
- A pseudonym $Nym^O_U$ for use with an organization $O$.

**Obtaining a credential:** 

- The user includes the public identity assertion into the $aux$
- She executes the $MintCred$ routine to obtain a credential and a signature of knowledge (SoK) on $aux$.
- She then formulates a transaction including both the resulting credential and the auxiliary data and broadcasts it into blockchain network.
- The network nodes verify the correctness of the credential and the identity assertion using the $MintVerify$ routine and auxiliary data.

**Showing a credential:** 

- User collects a set  of credentials $C_O$  and verify them using $MintVerify$  routine and validates auxiliary identity certification contained in $aux$ (e.g., authenticity proofs from oracles for proving the performance of validator). She runs the $Show$ routine.
- The Verifier also collects the set of credentials in $C_O$ and validates the credential using the $ShowVerify$ routine.

### B. Trusting the Ledger

Why the append-only transaction ledger necessary?

If the list of valid credentials can be evaluated by a set of untrusted nodes, then a user (Prover) could simply maintain a credential list compiled from network broadcasts and provide this list to the Verifier during a credential show. Although the credentials are valid by issuing party (not broadcast to any one else),  a malicious Verifier manipulates the Prover’s view of the network to include a poisoned-pill credential. Since the distributed ledgers (e.g., Bitcoin, Namecoin, etc) provides a shared view among the large number of nodes (users) can solve the above problem.

## Preliminaries

### A. Complexity Assumption**s**

1. **Strong RSA Assumption:**  Given a randomly generated RSA modulus $n$ and a random element $y \in \mathbb{Z}_n^{*}$, it is hard to compute  $x \in \mathbb{Z}_n^{*}$ and $e > 1$,  s.t. $x^e \equiv y$  (mod $n$).  The RSA modulus can be restricted to the form $n =pq$, where $p = 2p'+ 1$ and $q = 2q'+ 1$ are safe
primes.
2. **Discrete Logarithmic (DL) Assumption:**  Let $G$ be a cyclic group with generator $g$. Given $h \in G$, it is hard to compute $x$ such that $h = g^x$.

### B. Cryptographic Building Blocks

1. **Zero-knowledge Proofs:**  
    - The notation $NIZKPoK\{(x, y) :h = g^x ∧ c = g^y \}$ denotes a non-interactive zero-knowledge proof of knowledge of the elements $x$ and $y$ that satisfy both  $h = g^x$, $c = g^y$.
    - When  these proofs are used  to authenticate auxiliary data, the resulting non-interactive           proofs are called *signatures of knowledge. The* signature of knowledge on message $m$ is denoted as  $ZKSoK[m]\{(x, y) :h = g^x ∧ c = g^y \}$.

1. **Accumulators:** The construction of this decentralized anonymous credentials use accumulators on string RSA assumption. 
    - $AccumSetup(λ) \rightarrow params$: On  input a security parameter, it outputs $params$ $(N,u)$. First samples primes $p, q$ (polynomial dependence on the $\lambda$) and compute $N=pq$. Second, samples $u \in QR_N$, $u \neq 1$.
    - $Accumulate(params, C) \rightarrow A$:  On input $params$ $(N,u)$ and a set of prime numbers  $C = \{c_1, c_2, \dots, c_n | c_i \in [A, B]\}$, compute the accumulator $A = u^{c_1c_2\dots c_n}$ mod $N$.
    - $GenWitness(params, v, C) \rightarrow w$: On input $(N,u)$ and a set of prime numbers  $C$, and  a value $v \in C$, the witness $w = Accumulate(params, C\diagdown\{v\})$.
    - $AccVerify(params, A, v, ω) \rightarrow \{0, 1\}$:  compute $A' = w^v$  mod $N$  and output $1$ iff $A' = A$.
    
    Camenisch and Lysyanskaya  [https://cs.brown.edu/people/alysyans/papers/camlys02.pdf](https://cs.brown.edu/people/alysyans/papers/camlys02.pdf) paper show the following - 
    
    - **Incrementally updated:** Given an existing accumulator $A_n$ it is possible to add an element $x$ and produce $A_{n+1} = A^x_n$ mod $N$.
    - **Collision-resistance:** Under strong RSA assumption, no PPT adversary can produce a pair $(v,w)$ such that $v \notin C$ and yet $AccVerify$ is satisfied.
    - **zero-knowledge proof of knowledge:** To prove a committed value is in an accumulator (Accumulator membership proof).
    
    $$
    NI-ZKPoK\{(v, ω) : AccVerify((N, u), A, v, ω) = 1\}
    $$
    
    1. **Verifiable Random Functions (VRF):**  A pseudorandom function (PRF) [https://dl.acm.org/doi/10.1145/6490.6503](https://dl.acm.org/doi/10.1145/6490.6503) is an efficiently computable function whose output cannot be distinguished (with non-negligible advantage) from random by a computationally bounded adversary. Authors denote the pseudorandom function as $f_k(·)$, where $k$ is a randomly chosen key.  VRFs possess efficient proofs that a value is the output of a VRF on a set of related public parameters. 
    2. **Pedersen Commitments:** The public parameters are a group $G$ of prime order $q$, and set of generators $(g_0,g_1, g_2,\dots,g_m)$.  ****In order to commit to the values $(v_1,v_2,\dots, v_m)$, pick a random $r \in \mathbb{Z}_q^{*}$ and compute 
    
    $$
    C = PedComm(v_1,v_2,\dots,v_m;r) = g^{r}_0\prod_{i=1}^{m}g_i^{v_i}
    $$
    
    ## A CONCRETE INSTANTIATION
    
    - $Setup(1^λ) \rightarrow params$: On input a security parameter, $AccumSetup(λ)$ and generate $(N,u)$.  Next generate primes $p,q$ such that $p = 2^wq + 1$ for $w \geq 1$.  Let $\mathbb{G}$ be an order-$q$ subgroup of $\mathbb{Z}^*_p$ , and select random generators $(g_0,\dots, g_n)$ such that $\mathbb{G} = <g_0> = \dots = <g_n>$.  Output $params = (N, u, p, q, g_0 ,\dots, g_n)$.
    - $KeyGen(params) \rightarrow sk$: On input a set of parameters $params$, select and output a random master secret $sk \in Z_q$.
    - $FormNym(params, sk ) \rightarrow (Nym , sk_{Nym} )$: Given user’s secret key $sk$, select a random $r \in \mathbb{Z}_q^*$. Compute $Nym = g_0^rg_1^{sk}$ and set $sk_{Nym} = r$. Output $(Nym, sk_{Nym})$.
    - $MintCred(params, sk , Nym^O_U, sk_ {Nym^O_U},attrs, aux) \rightarrow (c, sk_c , \pi_M )$:   Given a nym $Nym^O_U$ and its secret key $sk_{Nym^O_U}$; attributes $attrs = (a_0,a_1,\dots,a_m) \in \mathbb{Z}_q^m$; and auxiliary data $aux$, select a random $r' \in Z_q$ and compute $c = g_0^{r'}g_1^{sk} \prod_{i=0}^{m}g_{i+2}^{a_i}$ s.t. $\{c| c\in [A,B]\}$, set $sk_c = r'$ and output $(c,sk_c,\pi_M)$. Where $\pi_M$ is a signature of knowledge on $\pi_M$ that the *nym* and the *credential* both belong to the same master secret $sk$ , i.e.:
    
    $$
    \pi_M = ZKSoK[aux]\{(sk , r , r') : c = g_0^{r'}g_1^{sk} \prod_{i=0}^{m}g_{i+2}^{a_i} ∧ Nym = g_0^rg_1^{sk}\}
    $$
    
           submit $(c, \pi_M , attrs, Nym^O_U , aux)$ to the public transaction ledger.
    
    - $MintVerify(params, c, attrs, Nym^O_U,aux,\pi_M)→\{0,1\}$: verify that $\pi_M$ is the signature of knowledge on $aux$. If the proof verifies successfully, output $1$, otherwise output $0$. The organization nodes should accept the credential to the ledger iff this algorithm returns $1$.
    - $Show(params, sk , Nym^V_U , sk_{Nym^ V_U} , c, attrs, sk_c , C_O ) \rightarrow \pi_S$ : Compute $A = Accumulate(params, C_O)$ and  $w = GenWitness(params, c, C_O)$. Output the following proof of knowledge:
    
    $$
    \pi_S = NIZKPoK\{(sk , r', r): AccVerify(params, A, c, w) = 1\\ ∧ c = g_0^{r'}g_1^{sk} \prod_{i=0}^{m}g_{i+2}^{a_i} ∧ Nym^V_U = g_0^rg_1^{sk}\}
    $$
    
    - $ShowVerify(params, Nym^V_U , \pi_S , C_O) \rightarrow \{0, 1\}$:
        - First compute $A = Accumulate(params, C_O)$.
        - Then, verify that $\pi_S$ is the aforementioned proof of knowledge on $c, C_O$ , and $Nym^V_U$ using the known public values. If the proof verifies successfully, output $1$, otherwise output $0$.
    
    ### Extensions:
    
    1. **k-show Credentials:**  In the system of [https://eprint.iacr.org/2006/454.pdf](https://eprint.iacr.org/2006/454.pdf),  authority issues a credential on a user’s secret seed $s$.  To show a credential for the $i^{th}$ time in validity period $t$, 
        1. User generates a serial number $S$ using a verifiable random function (VRF) as $S = f_s(0||t||i)$ along with NIZKP for the correctness of $S$.
        2. **Application to the above construction:** The user simply generates a random seed $s$and includes this value in the commitment to be included in the transaction ledger.  For $k-show$, the user provably evaluates the VRF on the seed $s$ plus a secret counter $i$.
    
    **How this extension reveal the user’s identity in the event of $(k+1)-show$  of the        credential?** (The intution taken from the paper [https://eprint.iacr.org/2006/454.pdf](https://eprint.iacr.org/2006/454.pdf) is as follows)
    
    - In $i^{th}- show$ in time period $t$, the user  releases serial number $S = f_s(0, t, i)$, a double-show tag $E = pk_U · f_s(1, t, i)^R$  (for a random R supplied by the verifier).
    - If a user shows $k+1$ e-tokens during the same time interval, then two of the e-tokens must use the same $S$.
    - The issuer (network nodes) can easily detect the violation and compute $pk_U$ from the two double-show tags, $E = pk_U · f_s(1, t, i)^R$ and $E' = pk_U · f_s(1, t, i)^{R'}$.
    
          since, from the above two $f_s(1, t, i) = (E/E')^{\frac{1}{(R−R')}}$ and $pk_U = E/fs(1,t,i)$
    
    1. **Credentials with Hidden Attributes:** The user might wish to conceal the attributes requested or shown, instead prove statements about them, e.g. proving the knowledge of a private key or proving the attribute is with in a certain range. 
    
          This can be achieved in two ways - 
    
    - Use of multi-message commitments where each message is an attribute. This increases the size of the  zero-knowledge proofs (linearly with the number of messages)
    - To encode the attributes in one single value and then prove statements about that committed value rather than reveal it. For example, given  a bit for particular attribute is set to one, use first $x$ bits of attribute one, use next $x$ bits of attribute two, etc., and use range proofs for attributes.
    1. **Stateful Credentials:** A stateful anonymous credential system is a variant of an anonymous credential system where credential attributes encode some **state** that can be updated by issuing new credentials. 
        
        For example, an operator can update it’s validator performance credential based on the latest state of attributes (missed_attestation and missed_blocks, etc.).
        
        This credential issuance is typically conditioned on the user showing a previous credential and offering proof  that the new credential should be updated as a function of the original.
        
        - $Update(params, sk, c, sk_c, C_O, update\_relation, state') \rightarrow (c', sk_c^{'}, \pi_u)$: Given the previous credential information and new state $state' = (s_0', s_1', \dots, s_m') \in \mathbb{Z}_q^m$, and an update relation $update\_relation$,  generate a fresh random serial number $S' \in Z_q$, and random value $r' \in Z_q$, compute the following and construct the proof $\pi_u$
        
        $$
        c' = g_0^{r'}g_1^{sk}g_2^{S'} \prod_{i=0}^{m}g_{i+3}^{s'_i}, \\A = Accumulate(params, C_O), 
        w = GenWitness(params, c, C_O)
        $$
        
    
                   $output = (c', sk_c', \pi_u)$, where $sk_c' = (S', state', r')$ and 
    
    $$
    \pi_u = NIZKPoK\{(sk, w, c, state, r, c', S', state', r'): AccVerify(params, A, c, w) = 1\\ ∧ c = g_0^{r}g_1^{sk}g_2^{S} \prod_{i=0}^{m}g_{i+3}^{s_i} ∧ c' = g_0^{r'}g_1^{sk}g_2^{S'} \prod_{i=0}^{m}g_{i+3}^{s'_i}  ∧ update\_relation(state, state') = 1\}
    $$
    
                 
    
    - $UpdateVerify(params, c, C_O, \pi_u) \rightarrow \{0, 1\}$:  Given a stateful credential $c$, a credential set $C_O$, and proof $\pi_u$, output $1$ if $\pi_u$ is correct, the proved state transition is a legal one, and the serial number $S$ was not previously used. Otherwise $0$.
    
    ## Integrating with Proof-of-work Bulletin Boards
    
    ### Integration:
    
    Namecoin provides a built-in storing of key-value pair and scan the list of existing list of names. Thus, we can scan credentials, validate and then accumulate them.
    
    For Alice to obtain a credential, she:
    
    1. Purchase some name from the name space by registering a public key
    
           $1$      $665a\dots$   $OP\_2D$
    
            $OP\_DUP$    $OP\_HASH160$   $6c1abe34$
    
       $OP\_EQUALVERIFY$    $OP\_CHECKSIG$
    
    1. Prepares a fresh credential with some attributes ($attrs$) and any supporting documentation necessary for her identity claim ($aux$) and stores the private portion of the credential $(sk, r, r')$.
    2. Updates, using the public key from step 1, her registered name to contain a credential and its supporting documentation.
    
          $2$     $642f7\dots$    $7b\dots$
    
          $OP\_2DROP$    $OP\_2DROP$
    
    $OP\_DUP$     $OP\_HASH160$
    
    $14d\dots$    $OP\_EQUALVERIFY$    $OP\_CHECKSIG$
    
    To show the credential to Bob, Alice:
    
    1. Scans the list of added names and retrieves all candidate credentials
    2. Checks the supporting documentation for each candidate and puts valid ones in $C$.
    3. Runs $show$ and sends the result to Bob.
    4. Bob does steps $1$ and $2$ and compute $C$.
    5. Bob runs $ShowVerify$ on Alice’s supplied credential and $C$ to verify it
    
    ### Supporting documentation and verification:
    
    - registration fee, no verification is necessary.
    - Digital signature to be verified.
    - Some assertion about resource management,  e.g. proof of storage/proof of retrievability to be verified in the case of TPM (Trusted Platform Module).
    - Authentication proofs for accessing off-chain data from Oracles.
    
    ### Operating cost:
    
    - Fee for purchasing the names $($$< 0.01$ USD as on $7/31/2013$$)$.
    - A small fee for posting data on the blockchain (e.g., double spend tags and serial numbers in $k-show$ credentials).
    
    ### **Latency:**
    
    *Depends on the block creation rate and number of confirmations of the Blockchain network.*
    
    ## Applications
    
    **Mitigating Sybil attacks in ad hoc networks:**  One common approach is to require that clients solve **proof-of-work (**resource-consuming challenges) that typically involve either storage or computation. This allows clients to re-use the single proof-of-work in anonymous fashion. One solution to this problem is to use $k-show$ anonymous credentials. This allows the peer to obtain a credential that can be used a limited number of times or a limited number of times within a given time period. When a peer exceeds the $k-show$ threshold (e.g., by cloning the credential for a Sybil attack), the credential can be identified and revoked. The paper [https://ieeexplore.ieee.org/document/1698607](https://ieeexplore.ieee.org/document/1698607) describes the computational puzzales as sybil defenses.
    
    ### Performance:
    
    There are four underlying operations: 
    
    - Minting a credential
    - Verifying that the mint is correct
    - Showing a credential
    - Verifying that show.
    
    Showing and verifying credentials also entail computing the accumulation of all or all but one of the current credentials. For each new credential added, the user update both accumulator and witness for which it intend to show credential. 
    
    1. The experiments we measured in *seconds* and were repeated for $500$ iterations.
    2. The complexity of the proof of knowledge generated during the credential show reduced by parallelizing the  independent computations.
    
    ![a_b.png](Decentralized%20Anonymous%20Credentials%206a25c35cf289436183b71cd4be6a18d7/a_b.png)
    
    ![c.png](Decentralized%20Anonymous%20Credentials%206a25c35cf289436183b71cd4be6a18d7/c.png)
    
    [Security of the Decentralized Anonymous Credentials](Decentralized%20Anonymous%20Credentials%206a25c35cf289436183b71cd4be6a18d7/Security%20of%20the%20Decentralized%20Anonymous%20Credential%207eb41c2ded4d4ba5b5750da18fa84793.md)
    
    ## References:
    
    1. Decentrlized Anonymous Credentials, [https://eprint.iacr.org/2013/622.pdf](https://eprint.iacr.org/2013/622.pdf)
    2. “Dynamic accumulators and application to efficient revocation of anonymous credentials,” in CRYPTO, 2002, [http://cs.brown.edu/~anna/papers/camlys02.pdf](https://cs.brown.edu/people/alysyans/papers/camlys02.pdf).
    3. O. Goldreich, S. Goldwasser, and S. Micali, “How to construct random functions,” Journal of the ACM, 1986, [https://dl.acm.org/doi/10.1145/6490.6503](https://dl.acm.org/doi/10.1145/6490.6503).
    4. Y. Dodis and A. Yampolskiy, “A verifiable random function with short proofs and keys,” ser. PKC, 2005, [https://eprint.iacr.org/2004/310.pdf](https://eprint.iacr.org/2004/310.pdf).
    
-