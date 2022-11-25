# Decentralized Identity on Dock

Abstract: Dock is a company that has been building Verifiable Credentials and Decentralised Identity Technologies since 2017. In their Verifiable Credential tool both the issuer and the user (or holder) hold DIDs on the dock ledger. The issuer digitally signs a verifiable credential that is stored in the digital wallet of the user. The user can present this certificate to a verifier. Some ``fingerprints'' of the credentials can be stored on the blockchain for revocation or timestamp reasons. Moreover, the company provides Web3 ID, a blockchain-based authentication system, which can be used as an alternative to Web 2 credentials in order for the users to sign in to applications; the users can prove claims about their identity using zero-knowledge proofs. The disadvantage of the latter for our case is that a user can create multiple DIDs.
Classification: Anonymous Credentials, DI, VC
Labels: Anonymous Credentials, Decentralized identity, Implementations, Management of credentials, Self-sovereign identity, Verifiable Credentials
Link to the paper: https://www.dock.io/
Score: no idea
Score Phase 1: Relevant

I put the score ``relevant'', because Dock is a company that has been building Verifiable Credentials and Decentralised Identity Technologies. Also, the company provides Web 3 ID, an open-source blockchain-based authentication system, which can be used as an alternative to Web 2 credentials (such as Google account or Github) in order for the users to sign in to applications; the users can also prove claims about their identity using zero-knowledge proofs. 

The disadvantage of their construction for our case is that the issuer needs to digitally sign (so it cannot be a smart contract). The disadvantage of the Web3 ID for our case is that the user can create multiple DIDs.

## Dock company and its products

 Dock is a company that has been building Verifiable Credentials and Decentralised Identity Technologies since 2017. They provide a tool that can be used by organizations in order to be able to issue certificates that are audible, digital, and fraud-proof. They provide also an open-source blockchain-based authentication system that allows users to prove claims about themselves using a non-custodial identity wallet app. Moreover, the company retains its own blockchain and its own token, called Dock token. A user can earn Dock tokens if it contributes to the maintenance of the Dock blockchain by becoming a validator. The products of the company are the following:

   

- **Dock Cert**: With this product, a client can issue or verify Verifiable Credentials and DIDs. Dock Cert uses its own blockchain that uses the same consensus mechanism as [Polkadot](https://polkadot.network/).
- **Web3 ID** This is a blockchain-based authentication system that allows you to create as many DIDs as you want and to prove or verify specific claims about these DIDs.  (Selective Disclosure and Zero-Knowledge Proofs are coming soon) . For example, a user can register in an application that supports this way of authentication using its Web 3 ID instead of its Web 2 credentials (Github, Google, etc).
- **A digital wallet** that stores verifiable credentials. You can import your credential via QR code or JSON file. It is going to support zero-knowledge proofs soon.

The main disadvantage of their Verifiable Credential (VC) tool for our case is that the issuer needs to sign the credential so it seems that it cannot be a smart contract.

The main disadvantage of the Web3 ID for our case is that you can create multiple DIDs.

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

The company has announced that in the future a relay service will send the certificate directly to the user’s wallet without the need for scanning or downloading.

The **verifier** can connect to the wallet of the holder and certify the credential or a claim about the credential.

The company claims that it will support zero-knowledge proofs and selective disclosure soon. This means that the holder will be able to prove claims about themselves without revealing the actual data.

## Web3 ID

Web3 ID is an open-source blockchain-based authentication system.

- The user can create a DID (or multiple DIDs) using its Dock wallet and sign in to web pages  (instead of using Web 2 credentials such as a Google account).
- The user will be able to prove some claims about itself without revealing its actual data. Some use cases discussed on the web page are the following:
1. The user will be able to prove that it owns at least X Ether without revealing the actual amount of Ether it owns.
2. The user will be able to prove that it is over 18 in order to join Web 3 gaming without revealing its age.
- The user can scan a QR code that encodes the request of the verifier (for example to prove that it is over 18) using its wallet.

The disadvantage of this tool for our case is that each user can create multiple DIDs.

![Untitled](Decentralized%20Identity%20on%20Dock%2076e191c71e304ae792759c8d0e371f83/Untitled.png)

Image from [https://www.dock.io/web3id](https://www.dock.io/web3id)

![Untitled](Decentralized%20Identity%20on%20Dock%2076e191c71e304ae792759c8d0e371f83/Untitled%201.png)

Image from [https://certs.dock.io/?_ga=2.18517177.1867176398.1669201052-1812075406.1662940082](https://certs.dock.io/?_ga=2.18517177.1867176398.1669201052-1812075406.1662940082).

## References

- Dock [https://www.dock.io/](https://www.dock.io/)
- Polkadot [https://polkadot.network/](https://polkadot.network/)