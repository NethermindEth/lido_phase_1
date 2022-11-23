# P-signatures and Noninteractive Anonymous Credentials

Added to deliverable?: No
Already read?: Yes
Assigned readers: Ignacio, Albert Garreta
Classification: Anonymous Credentials
Date of publication: 2008
Link to the paper: https://link.springer.com/chapter/10.1007/978-3-540-78524-8_20
MZ checked the note: No
Score Phase 1: Maybe relevant
Work Group: Academic literature

Cited in the paper from [Zero-knowledge credentials with deferred revocation checks](Zero-knowledge%20credentials%20with%20deferred%20revocatio%201635b695adcf48efb5db40ee4dcb9387.md) 

## **Summary**

Paper by Mira Belenkiy,  Melissa Chase, Markulf Kohlweiss &  Anna Lysyanskaya (a name we have seen a few times already). They introduce P-signatures with two efficient constructions of such. A P-signature is the combination of a signature scheme, a commitment scheme, and (1) an interactive protocol for obtaining a signature on a committed value; (2) a *non*− *interactive* proof system for proving that the contents of a commitment has been signed; (3) a non-interactive proof system for proving that a pair of commitments are commitments to the same value. They need DH-type assumptions on groups with bilinear mappings. 

## **Assessment**

There are interesting ideas and references to “Groth-Sahai” type of techniques, the paper is centered around Anonymous Credentials, and not Verifiable credentials. The introduction of zero-knowledge in the definition of a secure P-signature scheme is also something that could be relevant to us.

The paper also introduces a new signature scheme over groups with bilinear pairings (+ some DH assumptions).

## Highlight

![Capture d’écran 2022-10-07 à 15.36.06.png](P-signatures%20and%20Noninteractive%20Anonymous%20Credenti%20bbc01367fe2449ecbe4f2e505b74d9da/Capture_decran_2022-10-07_a_15.36.06.png)

### Addendum by @Albert Garreta

The paper builds upon so-called CT-signatures. These are P-signatures, with the difference that the *Prove* protocol is interactive in CT-signatures.

Such protocol can be easily made non-interactive by using the Fiat-Shamir transformation, which assumes the random oracle model.

The main contribution of the paper is to make the Prove protocol non-interactive without relying on the random oracle model.

Currently many protocols assume the RO model without much fuss. Given our goals and context, I believe this paper does not need further examining, though it is good that we have reviewed it.