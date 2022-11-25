# An Efficient System for Non-transferable Anonymous Credentials with Optional Anonymity Revocation

Abstract: A credential system is a system in which users can obtain credentials from organizations and demonstrate possession of these credentials. Such a system is anonymous when transactions carried out by the same user cannot be linked. An anonymous credential system is of significant practical relevance because it is the best means of providing privacy for users. In this paper we propose a practical anonymous credential system that is based on the strong RSA assumption and the decisional Diffie-Hellman assumption modulo a safe prime product and is considerably superior to existing ones: (1) We give the first practical solution that allows a user to unlinkably demonstrate possession of a credential as many times as necessary without involving the issuing organization. (2) To prevent misuse of anonymity, our scheme is the first to offer optional anonymity revocation for particular transactions. (3) Our scheme offers separability: all organizations can choose their cryptographic keys independently of each other. Moreover, we suggest more effective means of preventing users from sharing their credentials, by introducing all-or-nothing
 sharing: a user who allows a friend to use one of her credentials once, gives him the ability to use all of her credentials, i.e., taking over her identity. This is implemented by a new primitive, called circular encryption, which is of independent interest, and can be realized from any semantically secure cryptosystem in the random oracle model.
Classification: Anonymous Credentials
Labels: Anonymity revocation, Anonymous Credentials, Credential sharing prevention
Link to the paper: https://link.springer.com/chapter/10.1007/3-540-44987-6_7
Score: no idea
Score Phase 1: Maybe relevant
Year: 2001

Cited in the paper from Zero knowledge credentials with deferred revocation checks.

Cited in [Towards Smart Contract-based Verification of Anonymous Credentials](Towards%20Smart%20Contract-based%20Verification%20of%20Anony%202b002bb58dc44774a64a4f7c76c56b5f.md) 

Referred to as a “traditional anonymous credential system”

One of the properties of this construction is unlinkability meaning that the verifier cannot detect if the user has used the same credential twice or more times. I think that in our case this property is not of interest, because it seems that it makes Sybil attacks more feasible.  I think that for our case reuse protection presented in [Zero knowledge credentials with deferred revocation checks](https://www.notion.so/Zero-knowledge-credentials-with-deferred-revocation-checks-1d573b0208e3495ca5a95f423bf072e1) is more useful.

One interesting property of this construction is mitigating credential sharing; if the user shares its credential once with a friend then it allows him to use all of its credentials. The primitive that they use is called *circular encryption* and they implement it in the random oracle model. The authors claim that it is not obvious how this primitive can be implemented without the random oracle.