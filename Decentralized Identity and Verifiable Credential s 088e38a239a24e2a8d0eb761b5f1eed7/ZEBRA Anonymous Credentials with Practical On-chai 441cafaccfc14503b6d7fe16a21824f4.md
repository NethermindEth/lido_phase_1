# ZEBRA: Anonymous Credentials with Practical On-chain Verification and Applications to KYC in DeFi

Abstract: ZEBRA is an Anonymous Credential (AC) scheme, supporting auditability and revocation, that provides practical on-chain verification for the first time. It realizes efficient access control on permissionless blockchains while achieving both privacy and accountability. In all prior solutions, users either pay exorbitant fees or lose privacy since authorities granting access can map users to their wallets. Hence, ZEBRA is the first to enable DeFi platforms to remain compliant with imminent regulations without compromising user privacy.
We evaluate ZEBRA and show that it reduces the gas cost incurred on the Ethereum Virtual Machine (EVM) by 11.8x when compared to Coconut [NDSS 2019], the state-of-the-art AC scheme for blockchains. This translates to a reduction in transaction fees from 94 USD to 8 USD on Ethereum in August 2022. However, 8 USD is still high for most applications, and ZEBRA further drives down credential verification costs through batched verification. For a batch of 512 layer-1 and layer-2 wallets, the gas cost is reduced by 35x and 641x on EVM, and the transaction fee is reduced to just 0.23 USD and 0.0126 USD on Ethereum, respectively. For perspective, these costs are comparable to the minimum transaction costs on Ethereum.
Added to deliverable?: No
Already read?: Yes
Assigned readers: Basireddy Swaroopa Reddy
Classification: VC
Date of publication: 2022
Link to the paper: https://eprint.iacr.org/2022/1286
MZ checked the note: Yes
Presentation date: November 15, 2022
Reviewers: Michal Zajac
Score Phase 1: Relevant
Work Group: Academic literature, Hybrid

# ZEBRA - Zero-knowledge (Anonymous), batched, revocable and auditable credentials

**ZEBRA supports -** 

1. **Auditability** - Authorized auditors identify the owner of a maliciously behaving user.
2. **Revocation** - as credentials are often lost or stolen, and credentials of malicious users need to be revoked.
3. **On-chain verification** - With the primary goal of minimizing the verification cost using ZK-SNARKs. ZEBRA further reduces the cost of credential verification through batched verification.

**Note:** Batched verification relies on an untrusted aggregator to verify many credential verification proofs and recursively prove their validity to the contract with a single SNARK proof, the cost of which is amortized across multiple users.

## System Model

![Verification.png](ZEBRA%20Anonymous%20Credentials%20with%20Practical%20On-chai%20441cafaccfc14503b6d7fe16a21824f4/Verification.png)

Source: This paper

- **Credential Verification Smart Contract:**
    - This smart contract is responsible for **verifying a credential** (protocols 2A and 2B) and issuing an **on-chain access token** to the nominated wallet corresponding to the user.
    - These tokens can then be efficiently checked by the smart contract of the **access-controlled application** before granting access to the wallet.
    - It also stores the list of approved CAs and their revocation lists.
- **Users:**
    - Users can obtain a credential cred associated with their public-key $pk^U$ from any  $CA$ approved by the access-controlled application if the user satisfies the issuance
    policy (protocol $1$).
    - They can then prove on-chain that they hold a valid credential in a privacy-preserving way
    by providing a proof $\pi$ to get an access token for their wallet $pk^W$ (protocol $2A$).
    - We assume users are malicious and can act arbitrarily to get verified without holding a valid credential.
- **Certificate Authorities (CAs):**
    - CAs are organizations trusted to **issue** credentials to users if they satisfy the
    application’s credential issuance policy (protocol 1).
    - A  CA can **revoke** a credential it issued by adding its unique identifier $id$ to the revocation list (protocol $5$).
    - They also help auditors in **deanonymizing** malicious users of their issued credentials (protocol $4$).
    - We assume the $CA$s are **trusted** for integrity since they are reputed organizations authorized by the application.
- **Aggregator/Rollup Server:**
    - The aggregator/rollup server is an untrusted party that **batches** credential verification transactions for $L1$ and $L2$ wallets, respectively, to reduce on-chain verification costs.
    - By sending a short proof $\Pi$ to the contract which ensures that the server knows a valid credential verification proof $\pi_i$ for each $pk^W_i$ in the batch (protocol $2B$).
    
    ![Audit.png](ZEBRA%20Anonymous%20Credentials%20with%20Practical%20On-chai%20441cafaccfc14503b6d7fe16a21824f4/Audit.png)
    

Source: This paper

- **Auditors:**
    - Auditors can audit a credential verification transaction via its associated audit token $ψ$ if a majority of them agree to it (protocol $3$).
    - The audit reveals a unique credential identifier $id$ that embeds the CA that issued it.
    - Auditors then share $id$ with the issuing CA, and the CA deanonymizes the user by sending its user’s public key $pk^U$ or any other identity information to the auditors (protocol $4$).
    - ZEBRA can handle a minority of malicious auditors.
- **Contract Coordinator:**
    - The coordinator is responsible for managing the credential verification contract.
    - Its responsibilities are updating the list of approved CAs according to the access policy.
    - Batched updates to revocation lists of all CAs.
    - No need to trust the coordinator to post correct updates to the revocation list and require that it provide a proof $π_{rvk}$ ensuring that it knows a valid signature from the CA associated with the credential identifier $id$ it is adding to the revocation list (protocol $6$).
    
    ## Preliminaries
    
    - **zk-SNARKs:** zk-SNARK is a tuple of three algorithms:
        - **Setup$(1^λ , R) \rightarrow crs_R$** : On input security parameter $\lambda$ and relation  , outputs a common reference string $crs_R$ .
        - **Prove$(crs_R , x, w) \rightarrow \pi$** : On input $crs_R$  and a statement-witness pair $(x, w) \in R$, outputs a proof $\pi$.
        - **Verify$(crs_R , x, \pi) → \{0, 1\}$** : On input $crs_R$ , statement $x$ and proof $\pi$, outputs a bit to indicate if the proof is valid.
        
        Authors also use **simdSNARK** to denote a “data-parallel” SNARK which takes as input multiple statement-witness pairs and outputs a single succinct proof $\pi$.
        
    
    - **Digital Signature:** The signature schemes that are existentially un-forgeable under chosen message attacks (EUF-CMA). They consists of three algorithms $SIG = (Gen, Sign, Verify)$
        - **Gen$(1^\lambda) \rightarrow (sk, vk)$** : on input security parameter $\lambda$, outputs a secret key $sk$ and a public verification key $vk$.
        - **Sign$(sk, m) \rightarrow \sigma$** : on input sk and message $m$, output signature $\sigma$.
        - **Verify$(vk, m, \sigma) → \{0, 1\}$** : on input $vk$, $m$ and $\sigma$, outputs $1$ if $\sigma$ is a valid signature for $m$  w.r.t. $vk$.
    
    - **Threshold Public-Key Encryption (TKPE)**:  Use threshold public key encryption (TPKE) satisfying the simulation based **IND-CCA2** security notion defined in [TKPE](https://link.springer.com/content/pdf/10.1007/3-540-48910-X_7.pdf).
        - **Setup$(1^\lambda , n, t) → \{pk, vk, (sk_1, \dots, sk_n )\}$** : on input threshold $t$ for $n$ parties, outputs the public key $pk$ and verification key $vk$, along with secret keys $sk_i$ for each party.
        - **Enc$(pk, m; ρ) \rightarrow ct$** : encrypts message $m$ under public key $pk$ using randomness $\rho$.
        - **Dec$(ct, sk_i) \rightarrow m_i$** : computes a partial decryption of $ct$.
        - **Verify$(pk, vk, m_i) \rightarrow \{0, 1\}$**: checks whether $m_i$ was correctly computed using $pk$ and $vk$.
        - **Combine$(pk, vk, \{m_i\}_{i\in S \subseteq [n] s.t. |S| \geq t+1}) \rightarrow m$** : recovers message $m$ given $t+1$ partial decryptions which verify successfully.
    
    - **Merkle Trees** : The sparse merkle trees [SMT](https://eprint.iacr.org/2016/683.pdf?ref=hackernoon.com) are authenticated data structures MT on key-value pairs $(k, v)$ supporting the following operations -
        - **Add**$(k, v)$ : inserts a key-value pair $(k, v)$ in MT . If the key already exists, the value is updated.
        - **Root** : outputs the current merkle-root of MT.
        - **MProve$(k) \rightarrow P$ :** outputs a membership proof for key $k$.
        - **MVerify$(rt, k, v, P ) \rightarrow \{0, 1\}$** : on inputs root $rt$, key $k$, value $v$ and proof $P$, outputs $1$ if $(k,v)$ exists in $rt$.
        - **NMProve$(k) \rightarrow P$** : outputs a non-membership proof for key $k$.
        - **NMVerify$(rt, k, P) \rightarrow \{0, 1\}$** : on inputs root $rt$, key $k$ and proof $P$, outputs $1$ if $k$ does not exist in $rt$.
    
    ## Definitions
    
    ![Ideal Functionality.png](ZEBRA%20Anonymous%20Credentials%20with%20Practical%20On-chai%20441cafaccfc14503b6d7fe16a21824f4/Ideal_Functionality.png)
    
    ## Anonymous Credential Scheme
    
    ### 1. Credential Generation
    
    ![Cred_gen.png](ZEBRA%20Anonymous%20Credentials%20with%20Practical%20On-chai%20441cafaccfc14503b6d7fe16a21824f4/Cred_gen.png)
    
    **Example:** A user provides a identity document (Driver’s Licence or Passport, etc) issued by a Government authority and his/her public key $pk^U$ to get a credential  $cred = (\sigma, id, e)$  from CA.
    
    **Note:** In a real system there are far fewer users than the number of public keys. We leverage this by using compact 40 -bit identifiers as opposed to 256 -bit public keys, which in turn reduces the credential verification circuit size and also leads to smaller on-chain storage costs during revocation.
    
    ### 2. Credential Revocation
    
    - $MT_g^{rl}$ : stores credential identifiers revoked by $CA_g$
    - $MT_g^{rr}$  : stores merkle-roots of each CA’s revocation list
    
    The coordinator then locally updates $MT_g^{rr}$ and creates a proof $\pi$ attesting to the correctness of new revocation root  $rt^{rr}$:
    
    - $rt^{rr}_{old}$, known by the contract, is the old root of revocation merkle tree with $(g, rt^{rl}_{old},g)$ as leaves.
    - $rt^{rr}$, provided by the coordinator, is the new root of revocation merkle tree with $(g, rt^{rl}_g)$ as leaves.
    - $rt^{vk}$, known by the contract, is the root of CA’s verification key merkle tree with $(g, vk^{CA}_g )$ as leaves.
    - $∀g ∈ G$  s.t. $rt^{rl}_{old, g} \neq rt^{rl}_g$ , I know a signature $σ_{rv,g}$ on $(rt^{rl}_g , E)$ w.r.t. $vk^{CA}_g$ , where $E$ is the current epoch number.
    
    ![cred_revoke.png](ZEBRA%20Anonymous%20Credentials%20with%20Practical%20On-chai%20441cafaccfc14503b6d7fe16a21824f4/cred_revoke.png)
    
    ### 3.  Credential Verification
    
    - A user owning a credential cred from a CA, say $CA_g$ , can use it to issue an **ephemeral access token** $\psi$ for any wallet $pk^W$ it owns.
    - The audit token is simply an encryption of the unique credential identifier $id = g || u$ corresponding to the credential used for verification.
    - These tokens are checked by the access-controlled application before granting access and they are only valid for one epoch.
    - Epoch number incremented when revocation list updated.
    - Access token verification is done by checking if the epoch identifier matches the current epoch.
    - The contract maintains a hash-map $LV$ that maps wallet addresses to the epoch when they are last verified, i.e. $LV(pk^{w}) = E$.
    
    ![Cred_Ver.png](ZEBRA%20Anonymous%20Credentials%20with%20Practical%20On-chai%20441cafaccfc14503b6d7fe16a21824f4/Cred_Ver.png)
    
    ### 4. Transaction Audit
    
    - A threshold number $( t + 1$ out-of- $n)$ of auditors can **deanonymize** the user associated with a wallet, if they deem the wallet has displayed malicious behaviour.
    - Since access token $\psi$ encrypts $id = g || u$ using the public key $pk^A$ of the auditors,  t+1 of them can collaboratively decrypt $\psi$ to recover $id$.
    - When this $id$ points the auditors to the issuing $CA_g$,  who can then reveal user’s identity and revoke the corresponding credential if required.
    
    ![Trans_Audit.png](ZEBRA%20Anonymous%20Credentials%20with%20Practical%20On-chai%20441cafaccfc14503b6d7fe16a21824f4/Trans_Audit.png)
    

## 5. Batched Verification

- Authors instantiate $SNARK^1$ with pairing-based [Groth16](https://eprint.iacr.org/2016/260.pdf)  (over BN254)
- $simdSNARK^2$ with discrete-log-based [Spartan](https://eprint.iacr.org/2019/550.pdf) (over Grumpkin) optimized for data-parallelism.
- Both of these SNARKs use R1CS arithmetization.

![Batched_Ver_workflow.png](ZEBRA%20Anonymous%20Credentials%20with%20Practical%20On-chai%20441cafaccfc14503b6d7fe16a21824f4/Batched_Ver_workflow.png)

Source: This paper

Batching solution works as follows with two layers of recursion - 

- A batch of $N$ users independently create credential verification proofs $\{π_i^1\}_{i∈[N ]}$ using $SNARK^1$ , and send them along with transaction data $\{TX_i = (pk^W_i , ψ_i )\}_{i \in [N ]}$ to
the aggregator.
- First, the aggregator verifies the proofs $\{π_i^1\}_{i∈[N ]}$ using $simdSNARK^2$ to output  $\Pi^2$.
- Then the aggregator verifies $\Pi^2$ using $SNARK^1$ to output $\Pi^1$, which is then sent to the contract for batched verification along with $\{TX_i\}_{i∈[N]}$ .
- Finally, the contract processes $\{TX_i\}_{i∈[N]}$  and verifies $\Pi^1$ to ensure the validity of user proofs $\{π_i^1\}_{i∈[N ]}$ before updating access tokens for $\{pk^W_i\}_{i\in[N ]}$, i.e,  $LV(pk^{w}) = E$.

![Batched_Ver.png](ZEBRA%20Anonymous%20Credentials%20with%20Practical%20On-chai%20441cafaccfc14503b6d7fe16a21824f4/Batched_Ver.png)

## Conclusion

1. ZEBRA supports auditability and revocation
2. ZEBRA relies on ZK-SNARKs for reducing the on-chain verification costs and batch credential verifications.

## References

1. ****ZEBRA: Anonymous Credentials with Practical On-chain Verification and Applications to KYC in DeFi,**** [https://eprint.iacr.org/2022/1286](https://eprint.iacr.org/2022/1286).