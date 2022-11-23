# Zero-knowledge credentials with deferred revocation checks

Abstract: This whitepaper (written by authors affiliated with Microsoft Research and Microsoft Identity) presents zero-knowledge credentials in the setting where the issuer and the holder of the credential hold DIDs. Some interesting properties of this construction are: 1) Deferred revocation property: the verifier can check the revocation status of the holder’s credential in an asynchronous way without the holder’s participation. 2) The verifier can check if the credential of a holder has been reused in the past, even if the holder used the credential for different DIDs. The main limitation of this paper for our case is that the issuer is considered trusted and it needs to sign a message or retain a private state.
Added to deliverable?: Yes
Already read?: Yes
Assigned readers: Aikaterini-Panagiota Stouka
BS factor: solid
Classification: DI, VC
Date of publication: 2020
Labels: Centralized/permissioned, Cryptographic primitive (Anonymous Credential), Worthwile Sybil resistance insights
Link to the paper: https://github.com/decentralized-identity/snark-credentials/blob/master/whitepaper.pdf
MZ checked the note: No
Presentation date: October 14, 2022
Reviewers: Albert Garreta
Score Phase 1: Relevant
Work Group: Hybrid

A highlight from the introduction:

(screenshot from the paper)

![Untitled.png](Zero-knowledge%20credentials%20with%20deferred%20revocatio%201635b695adcf48efb5db40ee4dcb9387/Untitled.png)

Another highlight: Deferred and offline revocation forces making the following assumption:

> The parties issuing credentials and the parties that request their verification to not collude.
> 

---

**Melissa Chase, Esha Ghosh, and Srinath Setty, Microsoft Research**

**Daniel Buchner, Microsoft Identity**

**July 2020**

[https://github.com/decentralized-identity/snark-credentials/blob/master/whitepaper.pdf](https://github.com/decentralized-identity/snark-credentials/blob/master/whitepaper.pdf)

This paper presents a construction for zero-knowledge credentials in the decentralized identity (DID) setting, where the holder can establish different DIDs with the issuer and the verifier. The main contribution of this construction, compared to related work such as this one of  [Sovrin](https://github.com/hyperledger-archives/indy-crypto/blob/master/libindy-crypto/docs/AnonCred.pdf), is that the verifier can check if a credential is revoked without the user’s participation (by contacting the issuer in an asynchronous way). Moreover, one interesting property of this construction is that the verifier can check if the credential of a holder has been reused in the past, even if the holder used the credential for different DIDs. The main limitation of this paper for our case is that the issuer is considered trusted and it needs to sign a message or retain a private state.

## Terms

**issuer**: issues a credential

**holder** or **user**: acquires credentials from one or multiple issuers

**verifier** or **relying party (RP)**: verify claims about users’ credentials made by users 

## Examples discussed in the paper

1)  credentials related to CV on a career networking app.

The holders of the credentials do **not** care about disclosing their work history.  The verifiers should be able to verify signed statements by the issuers (Unforgeability property) and the status of the credentials e.g. if they are active or revoked :

- even if the holder is offline
- without disclosing information about the holder to the issuer (Privacy against issuer).

*If the operators do not care about disclosing their actual performance or reputation and correlating it with their DID, then this case would be of interest to our case.*  

2)  proving age to gain access to services (e.g. online purchases or alcohol ).

The holders want to prove that they are over 18:

- without disclosing their age or address (Minimal Disclosure).
- without being tracked (Unlinkability).
- even when there is no internet connection e.g. the holder buys alcohol in a remote local store without internet access (Deferred and offline revocation checks).
- the verifier has the option to avoid the duplicate provision of services in the case the holder uses its credential multiple times to gain access to the services (Protection against credential reuse).

3)  Banks make automated and recurring checks that loan holders maintain home insurance. 

## Credential

It is a set of key-values tuples (*name of the attribute*, *value of the attribute*) 

e.g.  (Date of Birth, 5/10/2000). A claim for this credential could be that the holder is over 18.

## Desired Properties

1. **Unforgeability**. The user cannot forge a credential created by the issuer. *For example, a pool operator cannot create a fake certification for good performance.*
2. **Unlinkability**: A coalition of RPs is not able to correlate the activities of a user across multiple RPs.  
3. **Minimal Disclosure**: The user reveals to the RP only what is necessary (e.g. only that it is older than 18). *For example, a pool operator can reveal that it has a good reputation without revealing actual data.*
4. **Privacy against issuer**: The issuer cannot learn if the user has used its credential and to which RP.  *For example, the issuer cannot track if/when the operators have used the performance certificate to join a pool.*
5. **Revocability:** The issuer can anytime revoke a credential (and make it invalid) without the cooperation of the user. *For example, the issuer can revoke a certificate of good performance or good reputation when the operator does not have good stats for an extended period.*
6. **Deferred and offline revocation checks**: The RP can check if a credential is active (has not been revoked) or that a credential of a new user is valid in an asynchronous way *without demanding the user to participate*. 

*Asynchronously* means that RP does not need to contact the issuer at exactly the time it wants to check the status of the credential. In this case, the revocation status is according to the last time the RP contacted the issuer.

**Example.** *Assume that an operator wants to prove to Lido that it has good performance certified by an issuer.  Then Lido could check if the credential of good performance has been revoked based on the last time it contacted the issuer. If later Lido contacts the issuer again and realizes that the credential of this operator has been revoked, then it can revoke the right of the operator to run a validator in an asynchronous way.  This reduces the cost because Lido could contact the issuer only at regular intervals and not each time new operators join. Also, Lido could check if the performance credentials of the operators have been revoked without contacting the operators.  **Please note that in this construction the issuer holds a private state and/or needs to digitally sign which means that it is not obvious how an issuer can be replaced by a performance oracle.***

1. **Protection against credential reuse**: An RP can check if the same credential has been used by different DIDs. Also, RP can prevent users from using a credential related to a DID twice. 

So if Bob gives the credential (and his secret key) that corresponds to his DID to Kevin, and Kevin uses this credential, then Bob loses the right to use this credential again. 

*This property can be useful to prevent an entity from creating multiple validators with the same DID  or using the same performance or reputation credential with different DIDs. If we could guarantee that each DID corresponds to a single entity then we could mitigate Sybil attacks. One solution to this could be using [Proof of Work puzzles for each DID](https://arxiv.org/abs/1904.05845))* 

## Assumptions

- The paper assumes that the issuer and the RPs do **not** collude to track users.
- The scheme does not offer unlinkability across multiple interactions with the same RP. The RP can detect when a user presents twice or more times the same credential to the same RP. In order to provide a stronger unlinkability, the paper suggests another variant that uses an anonymous credential scheme such as [here](https://link.springer.com/chapter/10.1007/3-540-44987-6_7). However, this variant does **not** satisfy deferred revocation and reuse protection.

## Cryptographic Tools

Zero-knowledge Proofs, Digital Signatures (ECDSA), Hash Functions, e.g. SHA-256, SNARK [Spartan](https://link.springer.com/chapter/10.1007/978-3-030-56877-1_25) (CRYPTO 2020).

## Overview (A simplified construction)

The construction has two options:

1. The RP does not need to contact the issuer at all, but it cannot check if the credential has been revoked. *This could be of interest to our case if the performance certificates are valid only for a specific period, so they do not have to be revoked when the operator misbehaves. However, in this case, the pool operator has to resubmit its credentials at regular intervals.*
2. In this option, the RP should contact the issuer in an asynchronous way, but the scheme provides **Deferred and offline revocation checks.** 

The user authenticates a DID with the issuer. It will retain the same DID when it interacts with the issuer, but it can change the public key that corresponds to this DID. Moreover, the user can use different DID to interact with RP.

### Issuing credentials

The issuer picks a random $r$ and signs a credential $c=$ (Date of Birth, 5/10/2000), with its private key. It sends the signature and $r$ to the user.

Then the RP (e.g. Lido) can download a digest $d=H(DID_{Lido}||c||r)$ from the issuer. 

- $r$ is a random nonce that is known only to the issuer and the user and prevents RP from learning $c$ with a brute-force attack. It will also be used to offer reuse protection and unlinkability.
- Also, digests are RP-specific in order to have unlinkability.

***Comments: the issuer should retain a private state, so it cannot be a smart contract.***  

  **

### Presenting credentials and verifying their validity

The user sends to the RP the following:

- $d=H(DID_{Lido}||c||r)$
- a zero-knowledge proof of knowledge of $c$ and $r$ such that $d=H(DID_{Lido}||c||r)$.

RP will :

- verify the  zero-knowledge proof
- check if $d$ is active. In more detail, it will download from the issuer a list with all the active digests and check if $d$ is included in this list. Note that this can happen in an asynchronous way.

**If RP cannot access the issuer and/or does not care about deferred and offline revocation checks** then:

the user will send a zero-knowledge proof that it knows a credential $c$ and a digital signature $\sigma$ such that $Verify(PK_I,c,\sigma)=1$, where: 

- $PK_I$ is the public key of the issuer
- $Verify$ is a digital signature verification algorithm, e.g. ECDSA’s verify.

### Presenting claims about credentials and verifying their validity.

The user provides a ZK SNARK to prove that $c$  included in $d$ satisfies certain claims.

*For example, if c is the exact stats of the pool operator, the claim would be that the pool operator has a good reputation.* 

### Reuse protection

If we want reuse protection then each user has a pseudonym for each RP. This pseudonym will be equal to $H(DID_{RP},r)$, where $r$ is the randomness that was used in $d=H(DID_{Lido}||c||r)$. the user proves with zero knowledge that indeed it used $r$ in $d$  to construct its pseudonym.

## Full Construction

(screenshot from the paper [https://github.com/decentralized-identity/snark-credentials/blob/master/whitepaper.pdf](https://github.com/decentralized-identity/snark-credentials/blob/master/whitepaper.pdf))

![Untitled](Zero-knowledge%20credentials%20with%20deferred%20revocatio%201635b695adcf48efb5db40ee4dcb9387/Untitled%201.png)

![Untitled](Zero-knowledge%20credentials%20with%20deferred%20revocatio%201635b695adcf48efb5db40ee4dcb9387/Untitled%202.png)

![Untitled](Zero-knowledge%20credentials%20with%20deferred%20revocatio%201635b695adcf48efb5db40ee4dcb9387/Untitled%203.png)

![Untitled](Zero-knowledge%20credentials%20with%20deferred%20revocatio%201635b695adcf48efb5db40ee4dcb9387/Untitled%204.png)

![Untitled](Zero-knowledge%20credentials%20with%20deferred%20revocatio%201635b695adcf48efb5db40ee4dcb9387/Untitled%205.png)

    (screenshot from the paper [https://github.com/decentralized-identity/snark-credentials/blob/master/whitepaper.pdf](https://github.com/decentralized-identity/snark-credentials/blob/master/whitepaper.pdf)) 

*Note that if we remove DID and public key from the issuer state and the digest,  then a user could share its credential with a friend without disclosing private information to his friend such as its private key.*            

Moreover, the paper discusses the following inherent limitations in credential systems and also presents the weaknesses of their construction. In addition, it provides a comparison with Sovrin. 

## Inherent in any credential system

- if the issuer is corrupted, it can create false credentials.
- the user can share its private key and its credential with a friend.
- if we make no assumptions about the way DIDs are created with the issuer we cannot tell whether two DIDs belong to the same person.

## Inherent in any system that supports deferred revocation

- if the issuer’s state leaks, then the RP can try to find the DIDs that correspond to the users from whom it has received digests (the DID that the users have authenticated with the issuers). In more detail, the RP in this scenario could revoke the credential that corresponds to a DID that is included in the issuer’s state and after that check, if a digest $d$ appears as revoked. If this happens, this means that the specific DID corresponds to $d$.

In the above construction,  if Bob gives a credential $d$ to the RP, the RP can try to find Bob’s DID from the issuer’s stake (if it has been leaked) in the following way: the RP can compute the digest that corresponds to a DID and if this digest is equal to $d$, then this DID corresponds to Bob. However, in the above scheme, this attack cannot reveal the attributes of the users, because the issuer’s state includes only the salted hashes.

- If RP and the issuer collude they can identify which DID has accessed the RP (using option 2 or 3).

## Inherent in any system with reuse protection and offline representation

If the credentials of the user are compromised and $r$ is leaked, then RP can identify all the times the user accessed the RP (using options 2,3) with the same $r$.

## Weaknesses

- If the issuer states leaks, then an attacker may learn the DID that corresponds to a credential.
- bad randomness: If the randomness in $r$ and $salt$ are not selected at random, then RP could identify the user behind an authentication or learn the attributes of the credential if the issuer state leaks.
- RP can learn when the user updated their public key.
- If RPs collude, they may check when new entries were added to the list of hashes and learn if the same person authenticated with them.

## Performance

The paper presents an estimation of the proof system’s cost in the case of Spartan over a credential with 1KB of encoded attributes. The R1CS program in their test had $2^{15}$ constraints and on a single CPU core of a Microsoft Surface laptop3 took under 170 ms to produce a proof of size 15KB. The proof could be verified in 17ms.

## Comparison with the construction of [Sovrin](https://github.com/hyperledger-archives/indy-crypto/blob/master/libindy-crypto/docs/AnonCred.pdf)

In Sovrin’s construction, the issuer publishes a list of the users who have active certificates in a cryptographic accumulator on the blockchain. The user and the RP should download the latest version of the accumulator. The user proves with zero knowledge to RP that its DID is included in the accumulator.

The disadvantage of Sovrin compared to this paper is that the user should participate in order to prove that its certificate is not revoked and also it needs to download the latest version of the accumulator. Also, the RP has to download the latest version of the accumulator every time a new user appears.

On the other hand, the advantage of the construction of Sovrin is that the accumulator can be public.

**As a final comment, I think that for our case the following part of the construction could be helpful in order to mitigate Sybil attacks: 
each credential is connected with a specific random value $r$. When the operators try to register with a verifier or RP, they provide a pseudonym that is the hash value of $r$ and the RP’s DID. With this technique, an RP can check that every operator uses once a single credential, even if it tries to reregister with the same credential using different DIDs.** 

## References

1)  Zero-knowledge credentials with deferred revocation checks

Melissa Chase, Esha Ghosh, and Srinath Setty, Microsoft Research, Daniel Buchner, Microsoft Identity, July 2020

[https://github.com/decentralized-identity/snark-credentials/blob/master/whitepaper.pdf](https://github.com/decentralized-identity/snark-credentials/blob/master/whitepaper.pdf)

2) Lodder, DK Michael, and Dmitry Khovratovich. "Anonymous credentials 2.0." (2019).Lodder, DK Michael, and Dmitry Khovratovich. "Anonymous credentials 2.0." (2019).

3) Anoncreds design. [https://github.com/hyperledger/indy-crypto/blob/master/libindy crypto/docs/AnonCred.pdf](https://github.com/hyperledger-archives/indy-crypto/blob/master/libindy-crypto/docs/AnonCred.pdf)

4) M. Baza, et al.,"Detecting Sybil Attacks Using Proofs of Work and Location in VANETs" in IEEE Transactions on Dependable and Secure Computing, vol. 19, no. 01, pp. 39-53, 2022. 

doi: 10.1109/TDSC.2020.2993769

5) Camenisch, J., Lysyanskaya, A. (2001). An Efficient System for Non-transferable Anonymous Credentials with Optional Anonymity Revocation. In: Pfitzmann, B. (eds) Advances in Cryptology — EUROCRYPT 2001. EUROCRYPT 2001. Lecture Notes in Computer Science, vol 2045. Springer, Berlin, Heidelberg. [https://doi.org/10.1007/3-540-44987-6_7](https://doi.org/10.1007/3-540-44987-6_7)

6) Setty, S. (2020). Spartan: Efficient and General-Purpose zkSNARKs Without Trusted Setup. In: Micciancio, D., Ristenpart, T. (eds) Advances in Cryptology – CRYPTO 2020. CRYPTO 2020. Lecture Notes in Computer Science(), vol 12172. Springer, Cham. [https://doi.org/10.1007/978-3-030-56877-1_25](https://doi.org/10.1007/978-3-030-56877-1_25)