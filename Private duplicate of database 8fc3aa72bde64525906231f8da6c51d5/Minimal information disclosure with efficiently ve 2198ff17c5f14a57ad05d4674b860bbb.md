# Minimal information disclosure with efficiently verifiable credentials

Abstract: Public-key based certificates provide a standard way to prove one's identity, as attested by some certificate authority (CA). However, plain certificates provide a binary identification: either the whole identity of the subject is known, or nothing is known. We propose using a Merkle hash tree structure, whereby it is possible for a single certificate to contain many separate claims or attributes, each of which may be proved independently, without revealing the others. Additionally, we demonstrate how trees from multiple sources can be combined together by modifying the tree structure. This allows claims by different authorities, such as an employer or professional organization, to be combined under a single certificate, without the CA needing to know (or to verify) all of the claims. In addition to describing the hash tree structure and protocols for constructing and verifying our proposed credential, we formally prove that it provides unforgeability and privacy and we present performance results demonstrating its efficiency. As services move from user names and passwords to attribute-based identity verification, efficiency and scalability of claims verification will become a major issue. We have implemented a prototype client-server system, deployed the prototype in Emulab, and evaluated the server-side throughput for attribute-based identity verification. The results show that our approach can perform about 200 identity verifications per second, while the best competing approach can perform only about 2--5 verifications per second. Our approach is, therefore, better suited to today's high-volume Web-based services that demand the highest possible throughput.
Classification: VC
Link to the paper: https://dl.acm.org/doi/10.1145/1456424.1456428
Score: no idea
Score Phase 1: Not relevant
Year: 2008

Referenced by [A Verifiable Credentials System with Privacy-Preserving Based on Blockchain](A%20Verifiable%20Credentials%20System%20with%20Privacy-Prese%20b4f3c3de2c9e4f6f80b7ab952cd2677f.md) 

## **Summary**

by David Bauer, Douglas M. Blough and David Cash. They use Merkle trees to reveal partial information certifying claims, and show how to combine trees together to obtain a single Merkle tree that can be used to prove claims from multiple sources.  

## **Assessment**

The approach seems simplistic probably not suited for the application we have in mind, despite the efficiency and throughput claims they made at that time. We mark the paper as not relevant.