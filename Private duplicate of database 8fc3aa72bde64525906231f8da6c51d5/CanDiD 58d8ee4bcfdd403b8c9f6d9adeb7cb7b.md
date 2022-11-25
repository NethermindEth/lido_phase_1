# CanDiD

Abstract: We present CanDID, a platform for practical, user friendly realization of decentralized identity, the idea of empowering end users with management of their own credentials. While decentralized identity promises to give users greater
control over their private data, it burdens users with management of private keys, creating a significant risk of key loss. Existing and proposed approaches also presume the spontaneous availability of a credential-issuance ecosystem, creating a bootstrapping problem. They also omit essential functionality, like resistance to Sybil attacks and the ability to detect misbehaving or sanctioned users while preserving user privacy. CanDID addresses these challenges by issuing credentials
in a user-friendly way that draws securely and privately on data from existing, unmodified web service providers. Such legacy compatibility similarly enables CanDID users to leverage their existing online accounts for recovery of lost keys. Using a decentralized committee of nodes, CanDID provides strong confidentiality for user’s keys, real-world identities, and data, yet prevents users from spawning multiple identities and allows identification (and blacklisting) of sanctioned users. We present the CanDID architecture and its technical innovations and report on experiments demonstrating its practical performance.
Classification: DI, VC
Labels: Legacy compatible, Management of credentials, Worthwile Sybil resistance insights
Link to the paper: https://www.arijuels.com/wp-content/uploads/2020/07/Candid.pdf
Score: no idea
Score Phase 1: Very relevant
Year: 2020

# TL;DR

CanDID attempts to address four main issues in decentralized identity:

1. Legacy Compatibility
2. Sybil resistance
3. Accountability
4. Key recovery

In the identity system for Lido, CanDID will play a key role in Sybil-resistance. In other words, CanDID would try to ensure that an operator does not try to act as more than one operator to accrue more rewards. The idea of accountability and key recovery may also be useful but only after some modifications (this is because if we use the system for maintaining accountability and key recovery as is, then the dependency on the CanDID committee is huge.).

# Short description

1. **Identity System:** CanDID uses services such as DECO or [Town Crier](https://eprint.iacr.org/2016/168) to port identities and credentials from web services. These services enable the users to generate trustworthy credentials without issuers generating credentials for them.
    1. **Credential Privacy:** 
        1. *Selective disclosure* - using zero-knowledge arguments. 
        2. *Membership privacy* - committee members and web service providers cannot obtain the identity of the users as well as the membership of the user (if the user is using CanDID or not). 
        3. *Pairwise credentials* - CanDID enables users to use different credentials for different services and the credential is unlinkable to any other credential for another service.
    2. **Sybil Resistance:** Supports deduplication of identities using a privacy-preserving MPC method.
    3. **Accountability:** CanDID can screen users of the system so as to identify the identity of the suspect user. This functionality is privacy-preserving and the committee uses fuzzy matching for finding the identity.
2. **Key Recovery System:** Leverage existing web authentication schemes to recover keys. Users may store the keys in their local devices and backup with the CanDID committee, prespecify recovery accounts on the web services, and define the recovery policy. To recover the keys, a user has to prove successful logins based on the recovery policy.

# Oracles

**An oracle relays and provides assurance that the retrieved data is authentic.** It allows users to prove that the origin of the data is authentic. CanDID uses oracles to allow users to pull data from existing systems. **CanDID proposes that either [DECO](https://arxiv.org/abs/1909.00938) or [Town Crier](https://eprint.iacr.org/2016/168) can be used for this purpose.**

# System Overview

## Identity System

**Goal: To convert already existing legacy data to decentralized identity.**

CanDID relies on decentralized oracles such as [DECO](https://arxiv.org/abs/1909.00938) or [Town Crier](https://eprint.iacr.org/2016/168) to port credentials from legacy web services. The CanDID committee acts as the verifier for the ported data.

![Source: [https://eprint.iacr.org/2020/934.pdf](https://eprint.iacr.org/2020/934.pdf)

Figure.1. This figure depicts the overview of general workflow of CanDID system. A user ports his legacy data as a pre-credential to the CanDID committee. The committee deduplicates the pre-crdential according to a unique legacy data, and obtains a master credential. Using the master credential and a context information, the committee generates a context-based credential which can be used by the user only in that context.  Later on those credentials can be revoked by the committee. To that end, the committee maintains a revocation list.](CanDiD%2058d8ee4bcfdd403b8c9f6d9adeb7cb7b/Untitled.png)

Source: [https://eprint.iacr.org/2020/934.pdf](https://eprint.iacr.org/2020/934.pdf)

Figure.1. This figure depicts the overview of general workflow of CanDID system. A user ports his legacy data as a pre-credential to the CanDID committee. The committee deduplicates the pre-crdential according to a unique legacy data, and obtains a master credential. Using the master credential and a context information, the committee generates a context-based credential which can be used by the user only in that context.  Later on those credentials can be revoked by the committee. To that end, the committee maintains a revocation list.

CanDID pulls data from web services using oracles to create credentials. A committee called the “CanDID Committee” acts as the verifier for the data ported. 

**There are four common requirements:** *uniqueness, non-transferability, accountability,* and *privacy*.

1. **Uniqueness and Non-transferability:** Uniqueness implies the inclusion of mechanisms to ensure the deduplication of user identities. Non-transferability refers to the integration of preventive measures that prevent users from transferring credentials.
    
    CanDID achieves uniqueness and non-transferability by making the system Sybil-resistant. Sybil resistance is achieved by deduplicating based on one or more attributes. To achieve deduplication, the CanDID committee maintains a secret-shared table of attributes (attributes such as SSNs or Aadhar numbers which are unique to every person). The steps in joining of a new user:
    
    1. The user presents one or more *pre-credentials* asserting various attributes. A pre-credential refers to a credential that has not been deduplicated in CanDID.
    2. After this, the CanDID committee performs a privacy-preserving MPC deduplication protocol to check the table if the attributes presented in the pre-credential exist. Once it’s confirmed that the attributes presented are unique, then the system issues a master credential.
    
    **Making the system Sybil-resistant helps discourage credential transfer.** 
    
    - Each user can obtain only one master credential in CanDID, disincentivizing sale or transfer.
    - Other deterrents such as
        - temporary revocation of misused credentials, and
        - revocation of stolen credentials
    
    can be effective for the same reason.
    
    **CanDID focuses only on truly unique identifiers for deduplication** - SSNs, Aadhar number, etc. For the countries that do not have such a unique identifier - they have proposed another method that would prevent the dependency on unique identifiers (discussed later).
    
    The master credential may not contain all attributes for all use cases. Therefore, a user can add more credentials for this purpose. This credential has to be related to the master credential (because it has to be for some person). To do this, the user has to put some information in the context-based credential that is common with the master credential.
    
2. **Accountability:** CanDID enables the identification of malicious users based on their real-world identities and permits the subsequent listing of such users on a committee-maintained public revocation list. **Any verifying party can check this list to see if a user’s credential has been revoked**. CanDID supports pulling data from real-world revocation lists as well as handling the case where a user is added newly to the revocation lists. 
3. **Privacy:** Privacy is one of the major properties of CanDID. 
    1. Users’ attributes are hidden from committee nodes.
    2. *Attribute-membership privacy:* committee members cannot determine if a credential containing a certain attribute exists in the system.

## Key Recovery System

**Goal: Prevent identity loss**

![Source: [https://eprint.iacr.org/2020/934.pdf](https://eprint.iacr.org/2020/934.pdf)

Figure.2. This figure depicts the key recovery system in CanDID.](CanDiD%2058d8ee4bcfdd403b8c9f6d9adeb7cb7b/Untitled%201.png)

Source: [https://eprint.iacr.org/2020/934.pdf](https://eprint.iacr.org/2020/934.pdf)

Figure.2. This figure depicts the key recovery system in CanDID.

For key recovery - a user provides the key along with a recovery policy. The CanDID committee stores the key in a privacy-preserving manner and releases it when the user meets the criteria mentioned in the recovery policy.

# System Model

Three main parties: users, credential issuers, and credential verifiers. CanDID supports the use of DID by relying on a PKI-like architecture where a mapping between DIDs and public keys is stored. The CanDID committee acts as the credential issuer. The CanDID committee stores a joint private key-public key pair. The private key is used for issuing credentials and the public key is used for verifying credentials.

**Credential:** CanDID uses the [W3C specifications](https://www.w3.org/TR/vc-data-model/) for structuring the credential.

A credential contains the following parameters:

| User Identifier (⁍) | Pseudonymous identifier of subject of the credential. Also referred to as pseudonym. |
| --- | --- |
| Context (⁍) | Denotes the circumstances where credential is used. |
| Claims (⁍) | ⁍ where,
1. ⁍ represents the attribute that tells what the claim is about.
2. ⁍ represents the value of the attribute.
3. ⁍ represents the provider which denotes the legacy web provider.
⁍ |
| Signature (⁍) | Signature by the issuer |

If there are $k$ claims, then $CS={\{claim_i\}}_{i=1}^k$ and $\sigma = Sig_{sk^c}(\{pk, ctx, CS\})$, where $sk^c$ is the secret key generated by the CanDID issuer committee. The representation is very similar to the W3C specification. The only difference is the inclusion of the providers in the claim. Each credential contains a $\mathrm{dedupOver}$ property which depicts the attribute used for deduplication. The figure depicts how a credential looks like in CanDID (note that they have used JSON).

![Source: [https://eprint.iacr.org/2020/934.pdf](https://eprint.iacr.org/2020/934.pdf)

Figure.3. This figure depicts a master credential that is deduplicated over SSNs. The grey boxes show the commitments to sensitive data.](CanDiD%2058d8ee4bcfdd403b8c9f6d9adeb7cb7b/Untitled%202.png)

Source: [https://eprint.iacr.org/2020/934.pdf](https://eprint.iacr.org/2020/934.pdf)

Figure.3. This figure depicts a master credential that is deduplicated over SSNs. The grey boxes show the commitments to sensitive data.

# Security Model

**Adversarial Model:** 

Adversary can corrupt up to $t$ out of $n$ committee nodes, where $t < n/3$. The adversary can corrupt any number of users and applications. CanDID committee nodes hold a $(t, n)$-Shamir secret sharing of the private key $sk^c$.

**Communication Model:** 

The communication in the network is asynchronous. However, the DKG needed for $(pk^c, sk^c)$ generation requires weak synchrony in the network for liveness.

**Security Properties:** 

CanDID aims to satisfy certain security properties (since these are definitions, they have been put here as is):

1. **Sybil resistance:** An adversary cannot obtain credentials associated with a larger number of distinct identities than the number of users which are controlled by the adversary.
2. **Unforgeability:** An adversary cannot forge the credentials of the honest user or impersonate them.
3. **Privacy in Credential issuance and key recovery:** It is infeasible for an adversary to learn about the attributes from observation of credential issuance and key recovery.
4. **Credential Validity:** An adversary can obtain credentials only for real-world identities it controls.
5. **Unlinkability:** The entities that deploy applications using CanDID cannot collude and link the respective transactions of any given user. This definition applies only in a weakened adversarial model that rules out malicious committee nodes.
6. **Privacy in Credential verification:** An adversary can learn about a user no more than the information presented by the user using their credentials. 

**Assumptions on users’ legacy credentials:** Some of the security properties depend on some assumptions. 

- The credential validity property assumes that an adversary can corrupt as many users as he wants but cannot obtain the credentials of users who haven’t been corrupted.
- The Sybil resistance property assumes that each user has a unique identifier.

# Identity System

This system converts legacy data to verifiable credentials. This is done in two steps. 

1. CanDID converts a set of pre-credentials to a master credential using a privacy-preserving, deduplication protocol. A user has only one master credential and the user does not use this credential with applications.
2. Users create context-based credentials which are created for corresponding applications. Context-based credentials are created in a way that they cannot be linked to extract more information about a user.

## From legacy data to pre-credentials

A pre-credential is defined as:

$$
PC = (claim, \pi),
$$

where $claim = \{a, v, P\}$ and $\pi$ is the proof for the claim which depicts that the $v$ is indeed the value corresponding to the attribute $a$ according to the provider $P$. **Pre-credentials are used for the creation of both master credentials and context-based credentials**. CanDID uses Town Crier or DECO for creating pre-credentials:

1. DECO: Here, $\pi$ is the signature over the claim made by the CanDID Committee.
    1. The user $U$ picks at least $t$ out of $n$ committee members ($\{C_1, C_2, C_3, …, C_t\}$) who would verify the claim and proof generated by DECO ($t$ is the threshold required in the threshold signature scheme used for generating the $(pk^c, sk^c)$).
    2. Each committee member selected by the user verifies the proof generated by DECO and therefore, the committee member is convinced that the claim generated is authentic.
    3. Then, committee member $C_i$ generates the partial proof $\pi_i = Sig_{sk_i}(claim)$. 
    4. $U$ obtains $\pi$ by combining $\{\pi_i\}$.
2. Town Crier: Here, a TEE is used to obtain $\pi = Sig_{sk_{TEE}}(claim)$, which is generated only if the claim is authentic. 

To prevent replay attacks, users associate their $PC$ with the $pk$. (such as $PC = (claim, pk, \pi)$)

## Master credential issuance

Deduplication: CanDID committee stores registered users’ attributes in a table which is called the $\mathrm{IDTable}$. 

- $U$ presents a set of pre-credentials ($PCS_U$) to the committee.
- The committee checks if $PCS_U$ matches any entry in the $\mathrm{IDTable}$.
- If no information is there, then the committee issues a master credential and adds the user information to the $\mathrm{IDTable}$.
1. **Deduplication Process:** 
    
    In CanDID, we have to use some attributes using which deduplication can be done. The authors have achieved this by using unique identifiers such as SSNs. This method provides strong Sybil-resistance within a given population. Each committee node stores locally $\mathrm{IDTable} = \{PRF(sk^c, v_U)\}$, where $v_U$ is a unique identifier and $sk^c$ is a secret key distributed across committee members. When a new user wants to join CanDID, the committee members evaluate and check if $\bar{v} = PRF(sk^c, v_U)$ is inside the $\mathrm{IDTable}$. If it is not present, then a master credential for $U$ is created. To ensure that the committee members do not learn about the value $v_U$, $PRF$ is evaluated using MPC (discussed later). 
    
    A limitation of this approach is that it requires users to have unique identifiers which might not be present in many countries. Another way of doing it is by obtaining deduplication parameters using common identifiers such as names and addresses. In addition, this approach poses some threats when implemented. For example, if the system needs multiple pre-credentials from the user for accepting an attribute, then this provides an opportunity for an adversary to compromise multiple accounts of a user.
    
2. **Protocol Details:** $\alpha$ is the attribute over which deduplication has been done.
    1. **System Setup:** 
        1. $n$ nodes - $\{C_1, C_2, C_3, …, C_n\}$
        2. Committee members use a threshold signature scheme $TS = (KGen, Sig, Comb, Vf)$
        3. This scheme generates $(pk^c, sk^c)$ where $pk^c = (pk^c_{sig}, pk^c_{prf})$ and $sk^c = (sk^c_{sig}, sk^c_{prf})$. Each of the $n$ nodes knows $pk^c_{sig}$ and $pk^c_{prf}$. For the secret key, committee member $C_i$ holds $sk^c_{sig, i}$ and $sk^c_{prf, i}$ where these keys form a share of the corresponding secret keys.
        4. Each committee node initializes a local table $\mathrm{IDTable} := \empty$.
        5. $[v]$ denotes a sharing of $v$ and $C_i$ has $v_i$ such that $v = \sum_i{\lambda_iv_i}$, where $\lambda_i$ depicts the Lagrange’s coefficients.
        6. $y \leftarrow f([x])$ depicts the MPC evaluation of $f$ over secret-shared input $x$.
        7. CanDID uses a secure MPC protocol based on **Beaver triples** to evaluate $PRF([sk^C_{prf}], .)$.
        8. Committee generates secret-shared random blinding factors and commitments $\{[b_i], g^{b_i}\}$.
        9. They have used MP-SPDZ framework for implementation.
    2. **Pre-credential generation:** Let $v$ denote the ideal value for $\alpha$ for $U$. Let $claim = (\alpha, \mathrm{C}_v)$, where $\mathrm{C}_v = com(v, r)$ is a commitment to $v$ with a witness $r$. 
        
        $**U$ generates a pre-credential $PC = (claim, pk^U, \pi^{oracle})$.**
        
    3. **Deduplication:** Next step is to evaluate $\bar{v} = PRF(sk^c, v)$:
        1. $U$ sends $[v]$ to committee members. 
        2. Committee members send shares of a fresh blinding factor $([b], B = g^b)$ to $U$ from which $U$ reconstructs $b$. 
        3. $U$ blinds $v$ by: $v' = b + v$ and a proof of correct blinding
            
              
            
            $$
            \pi^{blind}_i = Zk-PoK\{b, v, r: v' = b + v \wedge (g^b = B) \wedge (com(v, r) = \mathrm(C)_v)\}
            $$
            
            $U$ sends $(pk^U, v', \pi^{blind}, claim, \pi^{oracle})$ to all committee nodes.
            
        4. Each $C_i$ verifies the received proofs and computes $v_i = v'/n\lambda_i - b_i$.
        5. Committee nodes execute an MPC protocol to compute $\bar{v} = PRF([sk^c_{prf}], [v])$ and each of them asserts that $\bar{v} \notin \mathrm{IDTable}$. $C_i$ adds $(pk_U, \bar{v})$ to the $\mathrm{IDTable}$. 
    4. **Credential issuance:** 
        - Each committee node $C_i$ evaluates
            
            $$
            m=\{pk^U, \mathrm{``master”}, claim, \{\mathrm{``dedupOver”}, \{\alpha\}\}\}
            $$
            
            and generates a partial signature $\sigma^c_i = TS.Sig(sk^c_{sig, i}, m)$. 
            
        - $C_i$ sends $\mathrm{Enc}_{pk^U}(\sigma_i^c)$ to $U$.
        - After decrypting $t$ partial signatures, $U$ obtains the full signature $\sigma^c = TS.Comb(\{\sigma^c_i\})$ and constructs the master credential.
            
            $$
            cred_{master} = \{pk^U, \mathrm{``master"}, claim, \{\mathrm{``dedupOver"}, \{\alpha\}\}, \sigma^c\}
            $$
            

## Context-based credential issuance

Master credentials are not used for making interactions with applications because of the resulting linkability and their limited claims. Therefore, users create context-based credentials.

- Each application specifies a unique context $\mathrm{ctx}$.
- For getting a credential for $\mathrm{ctx}$, a user submits the $cred_{master}$ and a set of claims $\{claim_i\}$ required by $\mathrm{ctx}$.
- The committee verifies the claims and issues a credential for $\mathrm{ctx}$ **in the same way as the master credential.**

For this to work efficiently, two more challenges must be addressed: (i) it needs to be ensured that the new claims belong to the user holding the master credential else users can buy stolen accounts to add false claims; (ii) make pairwise DIDs, i.e., make credentials for different contexts independent.

- **Claim validity:** This is achieved by matching attributes in the new claim with the ones in the master credential. They have proposed the usage of linking attributes instead of using the attributes used for deduplication because the unique identifier (like SSNs) may not be used in all the services. In their implementation, they have used $name$ as the linking attribute. Users attach a ZKP to prove that the name used in the new claim is the same as that in the case of master credential. **They have developed a fuzzy matching mechanism for matching names.**
- **Sybil-resistance within a context:** A context-based credential should include the property $\mathrm{ctx}$ to ensure that a user can issue only one credential per $\mathrm{ctx}$.
- **Context-based credential issuance protocol:** Each application specifies a $\mathrm{ctx}$.
    - Let the user have a master credential $cred_{master}$.
    - $U$ submits $(pk_{new}^U, cred_{master}, \{PC_{new}\})$.
    - The committee maintains a set of identifiers $\mathrm{Issued}_\mathrm{ctx}$ that have already received a credential.
    - Finally, $pk^U_{new}$ is added to the $\mathrm{Issued}_\mathrm{ctx}$.

The usual issue of VCs is the applications colluding to figure out users’ usage patterns. The authors have mentioned that CanDID can be extended with suitable anonymous credentials for solving this purpose.

## Credential verification

Any party using CanDID can verify user $U$’s context-based credential $cred$ with associated $pk$ and associated opened commitments. The verifying party makes three checks:

1. $cred$ is properly signed by the committee.
2. $pk$ does not appear in the public revocation list.
3. Any commitment openings are valid.

## Security arguments

1. **Sybil resistance:** This follows from the integrity properties of oracle protocols.
2. **Unforgeability:** Follows from the unforgeability of signatures.
3. **Privacy in credential issuance:** From the privacy of oracle protocols, generating a pre-credential $claim = (a, \mathrm{C}_v)$ does not leak information about $v$. In addition, since the commitment is hiding, and MPC evaluation of $\bar{v} = PRF([sk_{prf}^c], [v])$ guarantees privacy, $A$ does not learn $v$ during issuance.
4. **Credential validity:** Follows from the integrity of oracle protocols
5. **Unlinkability across applications:** The only linkage between the master credential and context-based credentials lies in the $\mathrm{Issued}_\mathrm{ctx}$. This property holds from the fact that an adversary cannot corrupt the committee members.
6. **Privacy in credential verification:** Firstly, unopened commitments do not leak any information due to the hiding property. Secondly, commitments hide the result of a ZKP. 

# Accountability

**CanDID enforces accountability by identifying misbehaving individuals in a privacy-preserving manner.** In their implementation, they have used sanction lists for this purpose. There are two related problems corresponding to this:

- **Registration time compliance:** When $cred_{master}$ is created, the user has to show that their name is not in the sanctions list. The user produces a SNARK proof for solving this issue.
- **Periodic Screening:** If a new name is added to the revocation list, then CanDID must find out if a credential for the newly-added name exists in the sanction list. This implies that the whole $\mathrm{IDTable}$ and $\mathrm{Issued}_\mathrm{ctx}$ needs to be searched to find the names and their pseudonyms.

For both of them, the system must be able to detect potential alternate spellings of names. This is normally done by using fuzzy matching. The challenge in the case of CanDID is to do this in a secure manner.

For achieving this goal, they deployed a fuzzy matching algorithm based on edit distance and c-shingles. Evaluating edit distance requires a dynamic programming approach which has a large constant factor due to the size of the alphabet. Therefore, an approximation of edit distance has been used which is called c-shingles. The c-shingles of a word $w$ is the set of length $c$ consecutive substrings of $w$ (ignoring order, repetition). Let $sh_c(w)$ be the set of c-shingles of $w \in C^n$. We have $|sh_c(w)| \leq n - c + 1$ from the c-shingles paper. If $u = \mathrm{edit}(w, w')$ is the edit distance between $w, w' \in C^n$, then the distance between $sh_c(w)$ and $sh_c(w')$ is given by:

$$
\mathrm{dist}(sh_c(w), sh_c(w')) := |sh_c(w)\setminus sh_c(w')| + |sh_c(w')\setminus sh_c(w)| \leq (2c-1)u
$$

c-shingles has been used as a filtering mechanism in this architecture. First, the intersection between c-shingles with every element is computed to obtain a set of matches, and then, the distance is computed on these. It should be noted that given $sh_c(w)$ and $sh_c(w')$, the evaluation of edit distance is simply computing the intersection between two sets. Therefore, this process can be sped up by storing the c-shingles of every name in the dataset and the sanctions list. To do this securely, an oblivious sorting network is used to sort the dataset using the shingle distance, and then, the edit distance is computed only on a fixed number of candidates. For implementing this, the parameters chosen are as follows:

Max. length of name = 30

Edit distance threshold ($t$) = 3

c-shingles are used for removing the cases which cannot be matched. After setting the value of $c$ as 2, the number of candidates chosen for calculating the edit distance was 15 ($numCandidates$). Next, the edit distance is calculated.

Computation using SNARK and MPC:

1. For a client input string $x$, compute the $sh_c(x)$ and provide a SNARK proof for the same.
2. A boolean list is computed: $\mathrm{candidates} = [(y < < 1|1)*(\mathrm{dist}(sh_c(x), sh_c(y)) < (2c - 1))]$
3. Bitonic sort is used to sort $\mathrm{candidates}$ using the condition $comp(a, b) = a == 0? a:b$. This pushes all the zero values to the back. The ones with the zero value are the ones that cannot have a distance less than $t$.
4. Retrieve the first $numCandidates$ elements from the $\mathrm{Candidates}$. This gives the $\mathrm{finalCandidates}$.
5. Then, check if $\mathrm{Edit}(x, y) < t$ for $y \in \mathrm{finalCandidates}$.

In the end, a set is returned. If the set is empty, then nothing needs to be done. If that’s not the case, then: (i) the user may not be registered; (ii) the user may be expelled.

This procedure can be implemented as an arithmetic circuit which can then be compiled into either a R1CS for use with a SNARK (for the registration time screening) or as an MPC program (for periodic screening).

# Key Recovery System

The standard DID and VC systems require users to store private key securely and reliably. This burdens the users. CanDID has a key-recovery subsystem that solves this issue. It deploys mechanisms similar to that in the identity system.

Users can store their DID keys with CanDID committee which stores users’ keys in a secret sharing manner. **Users can employ legacy web authentication schemes to retrieve their backed-up keys.** The users can choose their preferred authentication policies for recovery. The committee enforces the policy for key release.

This could have been done by using OAuth but this would bring up a major privacy issue - leakage of information to the CanDID committee members. Instead, CanDID uses privacy-preserving proof of account ownership, just like in the case of the identity system.

**Enrollment:** This is for backing up of key.

1. $U$ picks a random ephemeral identifier $pk_{eph}^U$ and generates a pre-credential $PC = ((\mathrm{``account id"}, \mathrm{C}_{id^U_p}), pk^U_{eph}, \pi)$ containing a commitment to $U$’s account identifier associated with the authentication provider ($id^U_P$). The only difference here is that the $PC$ contains a $pk^U_{eph}$ which prevents the correlation between the two systems.
2. Pre-credentials are verified by using a verification protocol where the user proves knowledge of $sk^U_{eph}$.
3. The committee nodes run MPC to compute private key $\mathrm{pid}^U_P = PRF([sk_{epf}^C], [id_P^U])$.
4. The user then shares the secret shares of $sk^U$across the committee.
5. $C_i$ stores $(pid^U_p, sk_i^U)$.

**Recovery:** 

To retrieve, the enrollment process is replicated to compute $pid^U_P$. $C_i$ fetches the $(pid^U_P, sk_i^U)$ and then, shares $sk_i$ with the user.

**Security Arguments:** 

- Unforgeability: This is followed because the committee nodes never get to know the backed-up private key.
- Key recovery privacy: Same as the credential privacy in the identity system.

# Results

## Pre-credential generation

![Source: [https://eprint.iacr.org/2020/934.pdf](https://eprint.iacr.org/2020/934.pdf)](CanDiD%2058d8ee4bcfdd403b8c9f6d9adeb7cb7b/Untitled%203.png)

Source: [https://eprint.iacr.org/2020/934.pdf](https://eprint.iacr.org/2020/934.pdf)

## Master Credential Generation

1. **Proof of name matching across pre-credentials:** Over 100 runs, the proof generation took 1.2 seconds, while verification took 0.006 seconds on average.
2. **Proof of non-existence in the sanctions list:**

![Source: [https://eprint.iacr.org/2020/934.pdf](https://eprint.iacr.org/2020/934.pdf)](CanDiD%2058d8ee4bcfdd403b8c9f6d9adeb7cb7b/Untitled%204.png)

Source: [https://eprint.iacr.org/2020/934.pdf](https://eprint.iacr.org/2020/934.pdf)

1. **Distributed PRF:** 38 ± 1ms of CPU-time across four nodes in MP-SPDZ, as averaged over 10 trials of 10 runs each

## Privacy-preserving screening via MPC

![Source: [https://eprint.iacr.org/2020/934.pdf](https://eprint.iacr.org/2020/934.pdf)](CanDiD%2058d8ee4bcfdd403b8c9f6d9adeb7cb7b/Untitled%205.png)

Source: [https://eprint.iacr.org/2020/934.pdf](https://eprint.iacr.org/2020/934.pdf)

# References

- [https://eprint.iacr.org/2020/934.pdf](https://eprint.iacr.org/2020/934.pdf)
- [https://arxiv.org/abs/1909.00938](https://arxiv.org/abs/1909.00938)
- [https://eprint.iacr.org/2016/168](https://eprint.iacr.org/2016/168)
- [https://www.w3.org/TR/vc-data-model/](https://www.w3.org/TR/vc-data-model/)