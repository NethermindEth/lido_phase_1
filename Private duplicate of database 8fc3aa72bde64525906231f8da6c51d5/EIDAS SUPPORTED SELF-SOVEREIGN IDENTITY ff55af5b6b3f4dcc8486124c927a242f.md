# EIDAS SUPPORTED SELF-SOVEREIGN IDENTITY

Abstract: The purpose of this document is to stimulate the discussion on how identity management solutions based on the Decentralised Identity / Self-Sovereign Identity (SSI) paradigms can benefit from the trust framework created by the eIDAS Regulation.
Classification: DI, VC
Link to the paper: https://ec.europa.eu/futurium/en/system/files/ged/eidas_supported_ssi_may_2019_0.pdf
Score: no idea
Score Phase 1: Relevant
Year: 2019

The paper discusses how DIDs can be created using the eIDAS regulation (in the EU) as a supporting trusted entity. It is relevant with regards to porting information from the physical world (in this case, citizenship from an EU country) to Web3, in the form of a DID.

The approach is pretty straightforward: either use an eIDAS node as a verifier, or leverage the electronic certificates used for signing amongst EU citizens (aka digital signatures) to associate a public-private key pair to the DID. This is all possible due to the fact that the centralized eIDAS framework is 

We have seen solutions that use government-level information in order to generate DIDs and achieve Sybil resistance (CanDID being a notable example). This paper extends the feasibility of this approach to all other countries in the EU.

---

# The eIDAS Regulation

What is eIDAS?

> **eIDAS** (**e**lectronic **ID**entification, **A**uthentication and trust **S**ervices) is an EU regulation on electronic identification and trust services for electronic transactions in the European Single Market.
> 
- The eIDAS Regulation (…) ensures that people and businesses can use their own national electronic identification schemes (eIDs) to access public services in other EU countries where eIDs are available.
- The eIDAS regulation legally protects using blocks in a blockchain as electronic evidence in legal proceedings.

### eIDAS electronic identification

Member States of the EU achieve mutual recognition of electronic credentials via the eIDAS Interoperability framework, “based on the deployment of national eIDAS nodes managing the cross-border exchange of information”

![Untitled](EIDAS%20SUPPORTED%20SELF-SOVEREIGN%20IDENTITY%20ff55af5b6b3f4dcc8486124c927a242f/Untitled.png)

# The need for verified identities

- (…) a comprehensive approach to identity management should consider those use cases in which a strong verification of the actual identities of the parties intervening is needed. Under the the DID / SSI approach, the trust on the actual identities of the parties necessary for those use cases is built out of the system, as the specifications does not foreseen mechanisms for binding the digital identifiers to real-world entities.
- Usually, the problem is solved by relying on known entities (e.g. companies with which there is already a business relationship), who can act as endorsers of others. However, this poses some difficulties if the system intends to be scaled up to a large dimension (internationally or even globally) as many of the entities participating in the system will be unknown because there is no record of previous interactions.
- That eIDAS Regulation can play the role of endorser of the real-world identity of others.

# Linking the DID with the identity provided by eIDAS

There are two ways to do this:

### Method 1: **Linking the DID with the identity provided by a notified eID scheme**

- Under eIDAS, providers of online services can authenticate their users by means of their notified eID schemes; for doing that, they need to be connected to an eIDAS node that will transfer their authentication request to the eIDAS node of the country issuing the eID means associated to the eID scheme used by the users. In the authentication response, together with the result of the authentication, service providers can receive a set of data identifying uniquely the user (the eIDAS Minimum Data Set, which includes name, date of birth, national ID, etc)
- The link of the DID with the eIDAS Minimum Data Set can be done by allowing the user agent managing the DID to perform an eIDAS authentication, acting as a service provider.

![Untitled](EIDAS%20SUPPORTED%20SELF-SOVEREIGN%20IDENTITY%20ff55af5b6b3f4dcc8486124c927a242f/Untitled%201.png)

- In order to ensure the trustworthiness of the link, the user agent needs to guarantee that the legitimate owner of the DID is the same person that is authenticating via eIDAS.
- After creating the link, the identification data coming from the eIDAS Minimum Data Set would become part of the attributes that the user could disclose to third parties. However, it must be noted that, from the point of view of those third parties, these identification data would be self-asserted, as they cannot rely on the eIDAS node to verify them. This is because eIDAS eID is meant to be used for authenticating when accessing to services, but not for providing claims about identity that can be verified by others different from those who are requesting the authentication.

### Method 2: **Linking the DID with the identity provided by an electronic certificate**

- Under eIDAS, natural persons can obtain electronic qualified certificates for signing. (…) Together with the certificate, the user receives the pair of keys associated to it; the private key for signing, and the public key for verifying the signature.
- The link between the DID and the actual identity can be easily achieved by using the pair of keys corresponding to a qualified certificate as the pair of keys associated to the DID (instead of keys self-generated in the user agent), thus creating a cryptographic connection between the DID and the certificate.

![Untitled](EIDAS%20SUPPORTED%20SELF-SOVEREIGN%20IDENTITY%20ff55af5b6b3f4dcc8486124c927a242f/Untitled%202.png)

*A critique: where does the private key come from? Do I generate it myself, or does the government give me my private key? How do we know the government is not keeping my private key?* 

# **Applying eIDAS to the Verifiable Claims lifecycle**

The paper concludes by emphasizing how these links between DIDs and eIDs from eIDAS facilitate the issuance and resolution of verifiable credentials associated to the user’s real-world identity. In particular, these links help the issuer and the verifier authenticate that the relevant requests in the VC lifecycle indeed come from the DID holder.