# A Sybil-Resistant and Decentralized Market Place

Abstract: Existing centralised market places such as Ebay enable companies to gather large amounts of personal data that can be used to manipulate users. Furthermore, users can frequently perform fraud without severe consequence. Reputation systems only solve this problem partially as malicious users can re-join the network with a new identity if their reputation is too low. By performing a Sybil attack, i.e., joining with multiple seemingly distinct identities, malicious participants can further boost their own reputation.

In this paper, we present MarketPalace. MarketPalace relies on a peer-to-peer infrastructure to realize a decentralized market place during trading. Only when registering, users communicate with a central server to verify that they are not Sybils. More concretely, our system leverages self-sovereign identity to detect
and undermine repeated joins by the same user. We implemented MarketPalace and demonstrated its feasibility for small regional markets.
Classification: Sybil resistance
Link to the paper: https://arxiv.org/pdf/2201.10407.pdf
Score: no idea
Year: 2022

The paper describes a protocol for a partially decentralized market place.  It is not fully decentralized because it uses a central server for registration.

Identity is verified by the user providing a hash of his SSN to *I Reveal My Attributes (IRMA)*.  How the server verifies that the user provided the hash of his own SSN is not specified.  In any case the database of hashes to used to prevent Sybil attacks since MarketPlace checks the hash against the stored hashes.  If the hash is new, the MarketPlace uses its RSA key to sign the user’s key.

Storing the hash rather than the SSN is supposed to help with privacy, but it doesn’t help that much since anyone with access to the database can test potential SSN’s by hashing them.