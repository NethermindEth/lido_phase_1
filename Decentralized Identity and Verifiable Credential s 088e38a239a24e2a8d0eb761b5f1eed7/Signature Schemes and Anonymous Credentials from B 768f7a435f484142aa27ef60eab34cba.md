# Signature Schemes and Anonymous Credentials from Bilinear Maps

Abstract: We propose a new and efficient signature scheme that is provably secure in the plain model. The security of our scheme is based on a discrete-logarithm-based assumption put forth by Lysyanskaya, Rivest, Sahai, and Wolf (LRSW) who also showed that it holds for generic groups and is independent of the decisional Diffie-Hellman assumption. We prove security of our scheme under the LRSW assumption for groups with bilinear maps. We then show how our scheme can be used to construct efficient anonymous credential systems as well as group signature and identity escrow schemes. To this end, we provide efficient protocols that allow one to prove in zero-knowledge the knowledge of a signature on a committed (or encrypted) message and to obtain a signature on a committed message.
Added to deliverable?: No
Already read?: No
Assigned readers: Albert Garreta
BS factor: solid
Classification: Anonymous Credentials
Date of publication: 2004
Labels: Classic reference, Cryptographic primitive (Anonymous Credential), Good reference source
Link to the paper: https://link.springer.com/chapter/10.1007/978-3-540-28628-8_4
MZ checked the note: Yes
Presentation date: November 25, 2022
Reviewers: Jorge Arce-Garro
Score Phase 1: Relevant
Work Group: Academic literature

**Summary**: Likely a good foundational paper, referencing other possibly good foundational paper. Relevant at least for bibliographic purposes.

**Further action**:

- The paper needs to be only understood from a high-level
- Other works referenced here should be checked out.
- We could take a look at which papers cite this one so as to find more modern solutions.

**Assessment:**

This is a paper from 2004 with 432 citations, by the prolific Jan Camenisch and Anna Lysyanskaya.

Its contributions are:

- Description of a signature scheme based on the “LRSW assumption”.
- Scheme for proving knowledge of a signature on a committed message.
- Scheme for obtaining a signature on a committed message.
- Anonymous credential system.

I have marked it as relevant because:

- It looks like a good paper. Given its number of citations (432) and the publication date (2004), it could be a “standard reference” in this area, and so we may want to cite it.
- It also references several other works on “anonymous credential systems”, which, as this paper, may be standard references, and which we should check out.
- On the other hand, the paper is relatively old (2004). It is likely that better approaches have been found subsequently.

Highlight:

![Untitled.png](Signature%20Schemes%20and%20Anonymous%20Credentials%20from%20B%20768f7a435f484142aa27ef60eab34cba/Untitled.png)