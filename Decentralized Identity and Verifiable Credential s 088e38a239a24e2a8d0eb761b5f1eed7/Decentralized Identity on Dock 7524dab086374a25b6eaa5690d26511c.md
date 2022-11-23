# Decentralized Identity on Dock

Abstract: Dock is a company that has been building Verifiable Credentials and Decentralised Identity Technologies. In their VC system both the issuer and the user (or holder) hold DIDs on the dock ledger. The issuer is trusted and signs a verifiable credential that is stored in the digital wallet of the user. The user can present this certificate to a verifier. Some ``fingerprints'' of the credentials can be stored on the blockchain for revocation or timestamp reasons. Moreover, the company provides Web 3 ID that can be used as an alternative way to e.g google account in order for the users to sign in applications and prove claims about their identity. The disadvantage of the latter for our case is that a user can create multiple DIDs.
Actions needed and questions: @Aikaterini-Panagiota Stouka could you provide an abstract? @Michal Zajac Done
Added to deliverable?: No
Already read?: Yes
Assigned readers: Aikaterini-Panagiota Stouka
Classification: Anonymous Credentials, DI, VC
Labels: Implementations, Management of credentials
Link to the paper: https://www.dock.io/
MZ checked the note: Yes
Presentation date: November 11, 2022
Reviewers: Isaac Villalobos Gutiérrez
Score Phase 1: Relevant
Work Group: Blockchain projects, Hybrid

I will talk about this when I present a summary of ``Decentralized Identity: The Ultimate Guide 2022'', a blog post written by the same company. Please check this presentation first for definitions.

 I put the score ``relevant'', because Dock is a company that has been building Verifiable Credentials and Decentralised Identity Technologies. Also, the company provides Web 3 ID that can be used as an alternative way to e.g google account in order for the users to sign into applications and prove claims about their identity. The disadvantage of their VC construction for our case is that the issuer needs to sign and is considered trusted. The disadvantage of the Web3 ID for our case is that the user can create multiple DIDs.

## Dock Company

 Dock is a company that has been building Verifiable Credentials and Decentralised Identity Technologies. 

  

- **Dock Cert**: With this product, a client can issue or verify Verifiable Credentials and DIDs. Dock Cert uses its own blockchain that uses the same consensus as [Polkadot](https://polkadot.network/).
- **Web 3 ID** This is a blockchain-based authentication system that allows you to create as many DIDs as you want and to prove or verify specific claims about these DIDs.  (Selective Disclosure and Zero-Knowledge Proofs are coming soon) . For example, a user can register in an application that supports this way of authentication using its Web 3 ID instead of its Web 2 credentials (Github, Google, etc).
- **A digital wallet** that stores verifiable credentials.

The main disadvantage of their VC construction for our case is that the issuer needs to sign the credential and it is trusted.

The main disadvantage of the Web 3ID for our case is that you can create multiple DIDs.

## Dock Cert

Both the issuer and the holder hold DIDs stored on the blockchain.

**The issuer**:

1.  creates an account on Dock Certs.
2.  selects  ``*Create Verifiable Credentials''* 
3. selects ``*Create DID*'' (it can use a description) 
4. selects ``*Template and Issuer DID*''. 
5.  imports recipients one by one or by using CSV (comma-separated values***)*** files. 
6. optionally selects ``*Persist the credential*''. If it selects this option then the credential is stored on the Docks database (not on their blockchain) and a QR code is created. The verifier can take the certificate in its wallet by scanning the QR code.
7. There is the option to add a record of the credentials on the blockchain so that the issuer can revoke the credentials. 
8. There is the option to add a hash of the credential on the blockchain as a timestamp (proof of when and by whom this credential was issued).
9. can download the credential as a JSON file (a file that stores simple data structures in JavaScript Object Notation) or as a PDF file. The issuer can email this credential to the holder. The file will have a QR code if the issuer had selected to persist the credential.

**The holder** imports its credential to its digital wallet by:

- scanning the QR code if the issuer has selected to persist the credential
- receiving by email the PDF or JSON file with the certificate.

The company has announced that in the future a relay service will send the certificate directly to the user’s wallet without the need of scanning or downloading.

The **verifier** can connect to the wallet of the holder and certify the credential or a claim about the credential.

## References

- Dock [https://www.dock.io/](https://www.dock.io/)
- Polkadot [https://polkadot.network/](https://polkadot.network/)