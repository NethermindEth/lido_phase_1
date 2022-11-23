# Vision: A Critique of Immunity Passports and W3C Decentralized Identifiers

Abstract: Due to the widespread COVID-19 pandemic, there has been a push for immunity passports' and even technical proposals. Although the debate about the medical and ethical problems of immunity passports has been widespread, there has been less inspection of the technical foundations of immunity passport schemes. These schemes are envisaged to be used for sharing COVID-19 test and vaccination results in general. The most prominent immunity passport schemes have involved a stack of little-known standards, such as Decentralized Identifiers (DIDs) and Verifiable Credentials (VCs) from the World Wide Web Consortium (W3C). Our analysis shows that this group of technical identity standards are based on under-specified and often non-standardized documents that have substantial security and privacy issues, due in part to the questionable use of blockchain technology. One concrete proposal for immunity passports is even susceptible to dictionary attacks. The use of cryptography theater' in efforts like immunity passports, where cryptography is used to allay the privacy concerns of users, should be discouraged in standardization. Deployment of these W3C standards for `self-sovereign identity' in use-cases like immunity passports could just as well lead to a dangerous form identity totalitarianism.
Actions needed and questions: Add a short discussion of what the standards lack
Added to deliverable?: No
Already read?: Yes
Assigned for action: Ahmet Ramazan Agirtas
Assigned readers: Ahmet Ramazan Agirtas
BS factor: important
Classification: DI, VC
Date of publication: 2020
Labels: Critique, Implementations, Standardization efforts
Link to the paper: https://arxiv.org/abs/2012.00136
MZ checked the note: No
Presentation date: July 27, 2022
Reviewers: Genya
Score Phase 1: Relevant
Work Group: Academic literature

# TL;DR

The main goal of this note is to explore the possible weaknesses of DIDs and VCs. We aim to import useful takeaways from these critiques on the W3C standards for Lido project. This paper criticizes three main points. 

The first critique is that the data structure and serialization method of the VC standard of W3C **is NOT injective**. Due to the fact that the underlying serialization method is not injective, an active adversary may deploy a *signature exclusion* or a *signature replacement* attack on VCs and DIDs. It is stated that there is a mitigation for this problem, i.e. using **JSON Web Token (JWT)**. 

The second point is that storing DIDs or DID documents on public blockchains may lead to vulnerabilities against correlation attacks. 

The third one is that standardization efforts on the technologies like VCs and DIDs should be reviewed by security and privacy experts before they are used in real-world implementations. 

# Introduction

Because of the COVID-19 pandemic, a notion called “immunity passports” has currently been discussed by the governments. Harry Halpin (*from K.U. Leuven*) examines and criticizes the structure of existing proposals on **Immunity  Passports** which involve some standards, that are not very well-known, such as ****Decentralized Identifiers (DIDs) and Verifiable Credentials (VCs) **from the World Wide Web Consortium (W3C)**. 

**Immunity Passports.** An immunity passport is **a digital credential** that includes some information about an individual’s disease and immunity history.

# Critique on W3C Verifiable Credentials

It is stated that all current immunity credential schemes are constructed according to **the W3C Verified Credential Data Model 1.0 standard**. 

The papers main critique for VCs is that the serialization method of the W3C standards. It recommends (at the time of writing) using JSON or Semantic Web serialization (JSON or JSON-LD). 

Two main problems with the Semantic Web:

1. The W3C Verifiable Credentials standard can depend on the **Semantic Web RDF format.  This RDF format does not have the injectivity property which is crucial for signatures.** 
    
    See the below example (taken from a [video of Dr. Harald Sack](https://www.youtube.com/watch?v=0p_xfFiJEUU))  to understand the blank nodes better. 
    
    Each component of an object is identified with a URI as depicted below.
    
    ![Source: [https://www.youtube.com/watch?v=0p_xfFiJEUU](https://www.youtube.com/watch?v=0p_xfFiJEUU)](Vision%20A%20Critique%20of%20Immunity%20Passports%20and%20W3C%20De%202d6cfdd85bd44cc08e23b0a6a4d5606f/Untitled.png)
    
    Source: [https://www.youtube.com/watch?v=0p_xfFiJEUU](https://www.youtube.com/watch?v=0p_xfFiJEUU)
    
    Sometimes it may be more complicated, i.e. having more attributes as below.
    
    ![Source: [https://www.youtube.com/watch?v=0p_xfFiJEUU](https://www.youtube.com/watch?v=0p_xfFiJEUU)](Vision%20A%20Critique%20of%20Immunity%20Passports%20and%20W3C%20De%202d6cfdd85bd44cc08e23b0a6a4d5606f/Untitled%201.png)
    
    Source: [https://www.youtube.com/watch?v=0p_xfFiJEUU](https://www.youtube.com/watch?v=0p_xfFiJEUU)
    
    ![Source: [https://www.youtube.com/watch?v=0p_xfFiJEUU](https://www.youtube.com/watch?v=0p_xfFiJEUU)](Vision%20A%20Critique%20of%20Immunity%20Passports%20and%20W3C%20De%202d6cfdd85bd44cc08e23b0a6a4d5606f/Untitled%202.png)
    
    Source: [https://www.youtube.com/watch?v=0p_xfFiJEUU](https://www.youtube.com/watch?v=0p_xfFiJEUU)
    
    So considering the above graph, how can we distinguish which classroom will be used when? (**It’s not unique**) To solve this problem, blank nodes are used. Blank nodes classify attributes without naming them. They **are anonymous by the definition and they cannot be referenced externally.**
    
    ![Source: [https://www.youtube.com/watch?v=0p_xfFiJEUU](https://www.youtube.com/watch?v=0p_xfFiJEUU)](Vision%20A%20Critique%20of%20Immunity%20Passports%20and%20W3C%20De%202d6cfdd85bd44cc08e23b0a6a4d5606f/Untitled%203.png)
    
    Source: [https://www.youtube.com/watch?v=0p_xfFiJEUU](https://www.youtube.com/watch?v=0p_xfFiJEUU)
    
    RDF uses **semantic graphs of URIs** (*Uniform Resource Identifiers*) **and the serialization of the same graph can result in different ways.** (Since the blank nodes are anonymous, the object can be translated as a bit-string in many ways.) ****
    
    Luckily **there exists a mitigation of the above issue. An object can be serialized with the [IETF JSON Web Tokens (JWT)](https://datatracker.ietf.org/doc/html/rfc7519#page-6).** The below figure depicts the structure of the JWT.
    
    ![Source: [https://research.securitum.com/jwt-json-web-token-security/](https://research.securitum.com/jwt-json-web-token-security/)](Vision%20A%20Critique%20of%20Immunity%20Passports%20and%20W3C%20De%202d6cfdd85bd44cc08e23b0a6a4d5606f/Untitled%204.png)
    
    Source: [https://research.securitum.com/jwt-json-web-token-security/](https://research.securitum.com/jwt-json-web-token-security/)
    
    Note that some **JWT implementations may also cause problems because of the misused cryptography.** Therefore, one should be careful while implementing a JWT. 
    
2. The author states that the Semantic Web also has issues with TLS support according to another [paper](https://ceur-ws.org/Vol-1951/PrivOn2017_paper_8.pdf) of him. According to the RDF specification, the URIs of HTTP and HTTPS are not identical. The use of HTTP URIs on the Semantic Web is less than 0.1% of Semantic Web URIs. (in 2017)

In conclusion, it is emphasized that the above problems can male RDF-based Verifiable Credential implementations vulnerable to some attacks. **Namely**, **this may result in some attacks (signature exclusion/replacement attacks) in which an adversary can**

- **remove the signature of a signed message,**
- **replace it with another signature,**
- **trick the verifier into falsely accepting the message.**

# Critique on W3C Decentralized Identifiers

It is stated in the paper that using blockchains to store DIDs and DID documents may cause some issues, and these **issues may be worse than in centralized or federated identity systems. Assume that the DIDs and DID documents are stored in public chains.** Not only **malicious identity providers but also anyone can deploy correlation attacks. Anyone can learn the times of changes to DIDs. They can also learn the key material if the DID documents are also stored in the public chain.**

It is criticized that **it is only stated in the W3C DID standard that** 

> ***it is strongly recommended that DID documents contain no PII* (*personally identifiable information*).**
> 

If the identifiers are stored on a public blockchain, W3C DIDs may be vulnerable to correlation attacks. And the use of one-time DIDs doesn’t solve this problem. Recall that the **W3C DID standard also states that** 

> ***the anti-correlation protections of pseudonymous DIDs are easily defeated if the data in the corresponding DID Documents can be correlated***.
> 

An example of the correlation is given in the paper. Assume that the **service endpoints for COVID-19 testing centers are added to a public blockchain.** Since it is public data, an adversary may learn from the update in the blockchain that 

- the holders of those DIDs had COVID tests,
- the approximate location,
- date of the test.

# The Abuse of Security Standardization

- According to the paper, the standardization efforts on security and privacy technologies should be studied by the community (e.g. security and privacy researchers). Most of the identity systems are constructed on the W3C DID and W3C VC standards which are not analyzed sufficiently by the community. The author asks how DIDs and VCs became W3C standards without analysis of the community.
- It is also stated that it is hard to understand what is standard and what is not in the W3C standards.
- On the other hand, the security and privacy community should focus on DIDs and VCs as they are used in constructions in various fields such as the internet of things, identity management systems, etc.

# Conclusion

In conclusion, it is emphasized that specifications like W3C VC and W3C DID are problematic if they are not reviewed by the security and privacy community. Some concrete actions are recommended for W3C:

- Until the injectivity problem is solved, all RDF-related formats can be dropped from VCs.
- Since the use of DIDs and DID documents in public blockchains are not secure, the work on DIDs at the W3C can simply be halted until security is guaranteed by the use of advanced cryptographic primitives.

# References

- [Harry Halpin, *Vision: A Critique of Immunity Passports and W3C Decentralized Identifiers,* 2020.](https://arxiv.org/pdf/2012.00136.pdf)
- [Harry Halpin, *Semantic Insecurity: Security and the Semantic Web, 2017.*](http://ceur-ws.org/Vol-1951/PrivOn2017_paper_8.pdf)
- [https://www.w3.org/2001/sw/wiki/ShEx/RDF_serialization#Overview_and_discussions](https://www.w3.org/2001/sw/wiki/ShEx/RDF_serialization#Overview_and_discussions)
- [https://www.w3.org/TR/did-core/](https://www.w3.org/TR/did-core/)
- [https://www.youtube.com/watch?v=0p_xfFiJEUU](https://www.youtube.com/watch?v=0p_xfFiJEUU)
- [https://research.securitum.com/jwt-json-web-token-security/](https://research.securitum.com/jwt-json-web-token-security/)