# Privacy-preserving Identity Management System

Abstract: Abstract. Recently, a self-sovereign identity model has been researched actively as an alternative to the existing identity models such as a centralized identity model, federated identity model, and user-centric model.  The self-sovereign identity model allows a user to have complete control of his identity. Meanwhile, the core component of the self-sovereign identity model is data minimization. The data minimization signifies that the extent of the exposure of user private identity should be minimized. As a solution to data minimization, zero-knowledge proofs can be grafted to the self-sovereign identity model. Specifically, zero-knowledge Succinct Non-interactive ARgument of Knowledges(zk-SNARKs) enables proving the truth of the statement on an arbitrary relation. In this paper, we propose a privacy-preserving self-sovereign identity model based on zkSNARKs to allow any type of data minimization beyond the selective disclosure and range proof. The security of proposed model is formally proven under the security of the zero-knowledge proof and the unforgeability of the signature in the random oracle model. Furthermore, we optimize the proving time by checking the correctness of the commitment outside of the proof relation for practical use. The resulting scheme improves proving time for hash computation (to verify a commitment input) from 0.5 s to about 0.1 ms on a 32-bit input.
Added to deliverable?: No
Already read?: Yes
Assigned readers: Genya
Classification: Anonymous Credentials
Date of publication: 2021
Link to the paper: https://eprint.iacr.org/2021/1459.pdf
MZ checked the note: No
Score Phase 1: Maybe relevant
Work Group: Academic literature

Describes a zkSNARK based algorithm for distributed credentials.  However, its model is still based on the Issuer being trusted.  As such it doesn’t really address our main problem.