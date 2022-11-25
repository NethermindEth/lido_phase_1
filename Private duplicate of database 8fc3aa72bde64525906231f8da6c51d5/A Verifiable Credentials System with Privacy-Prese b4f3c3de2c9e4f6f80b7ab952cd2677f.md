# A Verifiable Credentials System with Privacy-Preserving Based on Blockchain

Abstract: Decentralized identity authentication is generally based on blockchain, with the protection of user privacy as the core appeal. But traditional decentralized credential system requires users to show all the information of the entire credential to the verifier, resulting in unnecessary overexposure of personal information. From the perspective of user privacy, this paper proposed a verifiable credential scheme with selective disclosure based on BLS (Bohen- Lynn-Shacham) aggregate signature. Instead of signing the credentials, we sign the claims in the credentials. When the user needs to present the credential to verifier, the user can select a part of but not all claims to be presented. To reduce the number of signatures of claims after selective disclosure, BLS aggregate signature is achieved to aggregate signatures of claims into one signature. In addition, our scheme also supports the aggregation of credentials from different users. As a result, verifier only needs to verify one signature in the credential to achieve the purpose of batch verification of credentials. We analyze the security of our aggregate signature scheme, which can effectively resist aggregate signature forgery attack and credential theft attack. The simulation results show that our selective disclosure scheme based on BLS aggregate signature is acceptable in terms of verification efficiency, and can reduce the storage cost and communication overhead. As a result, our scheme is suitable for blockchain, which is strict on bandwidth and storage overhead.
Classification: Anonymous Credentials, VC
Labels: Anonymous Credentials, Verifiable Credentials
Link to the paper: https://www.scirp.org/journal/paperinformation.aspx?paperid=115526
Score: no idea
Score Phase 1: Maybe relevant
Year: 2022

This paper proposes a BLS-based verifiable credentials aggregation scheme on a blockchain. Credentials are aggregated, and users can choose which credentials they want to disclose, preserving user privacy.
More precisely, a user can choose a part of claims from different credentials to disclose, and the verifier won't get the full information.
The paper highlights the importance of aggregating claims signatures, taking less blockchain storage space.
For testing proposes, there are two smart contracts implemented a DID contract and a Verifiable Credentials contract.
DID contract is in charge of managing DID, validating, and updating DID. While Verifiable Credentials contract takes care of creating credentials and signing and credential verification