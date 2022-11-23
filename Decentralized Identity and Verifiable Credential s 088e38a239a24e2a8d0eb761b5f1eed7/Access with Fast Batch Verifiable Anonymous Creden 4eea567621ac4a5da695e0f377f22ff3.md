# Access with Fast Batch Verifiable Anonymous Credentials

Abstract: An anonymous credential-based access control system allows the user to prove possession of credentials to a resource guard that enforce access policies on one or more resources, whereby interactions involving the same user are unlinkable by the resource guard. This paper proposes three fast batch verifiable anonymous credential schemes. With all three schemes, the user can arbitrarily choose a portion of his access rights to prove possession of credentials while the number of expensive cryptographic computations spent is independent of the number of accessx rights being chosen. Moreover, the third anonymous credential scheme is not only fast batch verifiable but also fast fine-grained revocable, which means that to verify whether an arbitrarily chosen subset of credentials is revoked entails constant computation cost.
Actions needed and questions: @Ahmet Ramazan Agirtas I think that paper may be not relevant for the first phase of the project
Added to deliverable?: No
Already read?: Yes
Assigned readers: Ahmet Ramazan Agirtas
BS factor: derivative
Classification: VC
Date of publication: 2008
Labels: Cryptographic primitive (Anonymous Credential), Not Sybil resistant
Link to the paper: https://link.springer.com/book/10.1007/978-3-540-88625-9
MZ checked the note: No
Reviewers: Basireddy Swaroopa Reddy
Score Phase 1: Not relevant
Work Group: Academic literature

![Untitled](Access%20with%20Fast%20Batch%20Verifiable%20Anonymous%20Creden%204eea567621ac4a5da695e0f377f22ff3/Untitled.png)

I changed the score to **“Maybe relevant”** because when I read the details, I saw that 

- the paper **does not give a novel approach** to the problem,
- it **does not address the Sybil attacks.**
- And it has more than 2 centralized parties, i.e. pseudonym authority and resource holder. It is not easy to make them decentralized as we see in CanDID case. But in their first scheme, they assume a single centralized party instead of the above two. That’s why I did not tag it as “not relevant”.

**Note:** $0$ **citations from 2008.**

This paper proposes three verifiable anonymous credential systems which support batch verification using pairings. 

- An **issuer** gives a set of access rights (in our case this will be only one) to each user.
- Then users present their credential(s) (using their pseudonyms) to a resource guard (verifier).
- And the verifier can verify all of the credentials at the same time (checking whether two pairings are equal).

In this paper there are mainly four types of parties:

1. The **User**
2. The **Pseudonym Authority (**$PA$**)** is the party that 
    - issues a pseudonym to the user.
3. The r**esource holder (**$RH$**)** is the party who is responsible for 
    - managing resources,
    - issuing credentials,
    - granting resource access rights to the user.
4. The **Resource Guard (**$RG$**)** is the party who 
    - enforces access policies on the resources of one or more $RH$s and,
    - admits or denies (by verifying the user’s pseudonym and the credential) the user access to the resources according to the $RG$’s access control policies.

One can find the details on the below page:

[(Details) **Access with Fast Batch Verifiable Anonymous Credentials**](Access%20with%20Fast%20Batch%20Verifiable%20Anonymous%20Creden%204eea567621ac4a5da695e0f377f22ff3/(Details)%20Access%20with%20Fast%20Batch%20Verifiable%20Anonym%20719c621d1bc14865bf706fda0eb08dea.md)

# References

- Zeng, K. (2008). Access with Fast Batch Verifiable Anonymous Credentials. In: Chen, L., Ryan, M.D., Wang, G. (eds) Information and Communications Security. ICICS 2008. Lecture Notes in Computer Science, vol 5308. Springer, Berlin, Heidelberg. [https://doi.org/10.1007/978-3-540-88625-9_5](https://doi.org/10.1007/978-3-540-88625-9_5)
- Boneh, D., Boyen, X. (2004). Short Signatures Without Random Oracles. In: Cachin, C., Camenisch, J.L. (eds) Advances in Cryptology - EUROCRYPT 2004. EUROCRYPT 2004. Lecture Notes in Computer Science, vol 3027. Springer, Berlin, Heidelberg. [https://doi.org/10.1007/978-3-540-24676-3_4](https://doi.org/10.1007/978-3-540-24676-3_4)