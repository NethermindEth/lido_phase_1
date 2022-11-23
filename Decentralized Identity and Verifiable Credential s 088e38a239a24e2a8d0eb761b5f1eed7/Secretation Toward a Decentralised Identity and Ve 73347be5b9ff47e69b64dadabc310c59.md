# Secretation: Toward a Decentralised Identity and Verifiable Credentials Based Scalable and Decentralised Secret Management Solution

Abstract: Secrets such as passwords, encryption keys, and certificates are used to assist in protecting access to resources such as computing devices, customer data and other information. Unauthorised access to resources can cause significant disruption and/or disastrous consequences. Given the importance of protecting these secrets to the security and privacy of many software systems, many solutions have been proposed. These solutions take two main directions: either securely store the secret and implement an access control mechanism, or divide the secret into a set of shares and distribute them in different machines (such as the Shamir’s secret sharing approach or multi-party computation MPC). However, apart from the MPC approach, they all share the same limitation: once the consumer receives the secret, it can be leaked and be used by any malicious actor. We believe that the secret management should not be centralised and that the secret should never be sent to the receiver. Therefore, in this paper we propose, Secretation, a new approach for managing the secrets in a decentralised way by leveraging decentralised identity concepts such as verifiable credential technologies, password-authenticated key exchange protocols and multi-party computation. The result is a more scalable and secure solution that significantly reduces the risk of leaking the secrets.
Added to deliverable?: No
Already read?: No
Assigned readers: Aikaterini-Panagiota Stouka
Classification: DI, VC
Date of publication: 2021
Link to the paper: https://ieeexplore.ieee.org/document/9461144
MZ checked the note: No
Score Phase 1: Not relevant

I rated this paper not relevant for now. The paper suggests a construction for decentralized secret management using verifiable credentials and DID. 

In more detail, the construction is related to a central database to which users with a specified set of privileges have access.
The paper claims that If we give the database credential(secret) to the users then they can leak it. It suggests that the secret should never be sent to the users. Instead, there should be an agent who will certify that a user can access the database via verifiable credentials. In more detail, a trusted authority signs a certificate that the user has the appropriate attribute to access the database (e.g it is over 18). Both the trusted authority and the user should have previously created DIDs.

One use case I find is a scenario where the operators do not hold the secret that is related to their credentials (so that they cannot share it or lose it). However in that case we should replace the trusted agent with a committee as Candid.