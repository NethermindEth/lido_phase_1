# Zero-Knowledge Proof-of-Identity: Sybil-Resistant, Anonymous Authentication on Permissionless Blockchains and Incentive Compatible, Strictly Dominant Cryptocurrencies

Abstract: Zero-Knowledge Proof-of-Identity from trusted public certificates (e.g.,
national identity cards and/or ePassports; eSIM) is introduced here to
permissionless blockchains in order to remove the inefficiencies of Sybil-
resistant mechanisms such as Proof-of-Work (i.e., high energy and en-
vironmental costs) and Proof-of-Stake (i.e., capital hoarding and lower
transaction volume). The proposed solution effectively limits the number
of mining nodes a single individual would be able to run while keeping
membership open to everyone, circumventing the impossibility of full de-
centralization and the blockchain scalability trilemma when instantiated
on a blockchain with a consensus protocol based on the cryptographic
random selection of nodes. Resistance to collusion is also considered.
Solving one of the most pressing problems in blockchains, a zk-PoI
cryptocurrency is proved to have the following advantageous properties:
- an incentive-compatible protocol for the issuing of cryptocurrency
rewards based on a unique Nash equilibrium
- strict domination of mining over all other PoW/PoS cryptocurrencies,
thus the zk-PoI cryptocurrency becoming the preferred choice by miners
is proved to be a Nash equilibrium and the Evolutionarily Stable Strategy
- PoW/PoS cryptocurrencies are condemned to pay the Price of Crypto-
Anarchy, redeemed by the optimal efficiency of zk-PoI as it implements
the social optimum
- the circulation of a zk-PoI cryptocurrency Pareto dominates other
PoW/PoS cryptocurrencies
- the network effects arising from the social networks inherent to na-
tional identity cards and ePassports dominate PoW/PoS cryptocurrencies
- the lower costs of its infrastructure imply the existence of a unique
equilibrium where it dominates other forms of payment
Link to the paper: https://arxiv.org/pdf/1905.09093.pdf
Score: no idea
Score Phase 1: Not relevant
Year: 2020

**Paper Link:** [here](https://arxiv.org/pdf/1905.09093.pdf)

**Abstract**

- Paper represents the concept of ZK-PoI (Proof Of Identity) blockchains
- The proposed solution effectively limits the number of mining nodes a single individual would be able to run while keeping membership open to everyone
- The idea is to remove the inefficiencies of **Sybil resistant** mechanisms in PoW and PoS i.e chains i.e energy and capital and design a new ZK-PoI chain

**X.509**

- **X.509** is an [International Telecommunication Union (ITU)](https://en.wikipedia.org/wiki/International_Telecommunication_Union) standard defining the format of [public key certificates](https://en.wikipedia.org/wiki/Public_key_certificate)
- An X.509 certificate binds an identity to a public key using a digital signature. A certificate contains an identity (a hostname, an organization, or an individual) and a public key
- An X.509v3 certificate has the following structure:
    
    ![Screen Shot 2022-10-10 at 08.35.32.png](Zero-Knowledge%20Proof-of-Identity%20Sybil-Resistant,%20%20a07bcefd389342c38495cd13c1a94d49/Screen_Shot_2022-10-10_at_08.35.32.png)
    
- To obtain a signed certificate, the entity creates a key pair and signs a Certificate Signing Request (CSR) with the private key
- CSR contains the applicant’s public key which is used to verify the signature of the CSR and a unique Distinguished Name within the organization.
- Then, one of the intermediate certificate authorities issues a certificate binding a public key to the requested Distinguished Name and that also contains information identifying the certificate authority that vouches for this binding.

**Verifiable Validation of X.509 Certificates as Anonymous Credentials**

- the idea is to turn X.509 certificates into anonymous credentials.
- use of zk-SNARKS to obtain a verifiable computation protocol so that a certificate
the holder is able to prove that he holds a valid X.509 certificate chain with a
unique Distinguished Name

**Authentication Protocol**

- protocol generates a unique pseudonym for each miner
- along with pseudonym protocol attaches verifiable proof that the new public key to be stored on-chain is signed with a valid public certificate included on a recognized certification authorities list
- the new public key is linked to the pseudonym that is uniquely linked to the citizen’s public key certificate

Miners holding a public key certificate must execute the following steps

- Create a deterministic public/secret key pair based on a secret passphrase

```jsx
pk, sk = Det_KeyPairGen (KDF (passphrase, hash(publicCert)))
```

- Obtain a signature of the previously generated public key pk with the
miner’s public key certificate

```jsx
signPK = PKCS_Sign (secretKeypublicCert, pk)
```

- Check the validity of the certificate chain of the miner’s public key certificate and verify that the miner’s public key certificate is contained on a list of trusted certification authorities.
- Obtain the unique identifier from the miner’s public key: `uniqueID = getID(publicCert)`
- Generate a deterministic pseudonym using the blockchain identifier:

```jsx
signatureSecret = PKCS_Sign (secretKeypublicCert,”PREFIXED_COMMON_STRING”)

pseudonym = Hash (signatureSecret||BlockchainIdentif ier||uniqueID) ||”REG”
```

- Verify the signature signPK on the miner’s public key certificate pk:

```jsx
PKCS_Verify (publicCert, signPK)
```

- As the signatureSecret is calculated offline so its necessary to verify it using the miner’s public key certificate publicCert:

```jsx
PKCS_Verify (publicCert, signatureSecret)
```

- Generate the zero-knowledge proof π  of the miner’s public key certificate **pk**, the generated **pseudonym,** and signature **signPK** such that all the previous conditions hold
- Anonymously contact the permissionless blockchain:
    - register the generated **pseudonym**, the new public key **pk**, the signature
    **signPK** and **π**
    - actual **publicCert**, **uniqueID,** and **signatureSecret** are not revealed
    - permissionless blockchain verifies π before adding the **pseudonym, pk** & **signPK**
    
    > Note: here the miner is unable to register multiple pseudonyms so he can only use one running node that would be signing messages with the generated secret key **sk**. Other nodes would be able to efficiently verify **π** to confirm that the public key **pk** is signed by someone from an allowed certificate authority and that the pseudonym is the miner’s unique alias for the blockchain
    > 
    

**Zero-Knowledge Protocols ePassports**

- analogous to the zero-knowledge protocols for X.509
- considers the  details of ePassports
    
    ![Screen Shot 2022-10-11 at 12.12.09.png](Zero-Knowledge%20Proof-of-Identity%20Sybil-Resistant,%20%20a07bcefd389342c38495cd13c1a94d49/Screen_Shot_2022-10-11_at_12.12.09.png)
    
- contains a unique keypair with the public key on Data Group 15 and the private key hidden within the chip
- with the key-pair, the Active Authentication protocol can be used to sign random challenges
- **Anonymous miner registration**
    - protocol generates a unique pseudonym for each miner
    - along with pseudonym protocol attaches verifiable proof that the new public key to be stored on-chain is signed with a valid public certificate included on the list of Country Signing Certificate Authorities
    - the new public key is linked to the pseudonym that is uniquely linked to the citizen’s public key certificate of the passport holder

Then the authentication protocol will be the same as [above](Zero-Knowledge%20Proof-of-Identity%20Sybil-Resistant,%20%20a07bcefd389342c38495cd13c1a94d49.md).