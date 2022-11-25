# Permissionless Blockchain-Based Sybil-Resistant Self-Sovereign Identity Utilizing Attested Execution Secure Processors

Abstract: The current circumstance that requires people more
online has encouraged us to address digital identity preserving
privacy. There is a momentum of research addressing Self-
Sovereign Identity (SSI); many research approach blockchain
technology as a foundation. SSI brings natural persons various
benefits such as their owning controls; on the other side, digital
identity systems in the real world require Sybil-resistance to
comply with Anti-Money-Laundering (AML) and other needs.
Our proposal in this paper is to build a secure SSI system
by utilizing permissionless blockchain and Rafael Pass et al.’s
contribution of the formal abstraction of Attested Execution
Secure Processors (AESPs). Our proposal of the AESP-based
SSI architecture and system protocols, $\Pi^{G_{}att}$ , demonstrates the
powerfulness of hardware-assisted security and the formal abstraction
of AESPs, fitting into building a proper SSI system that
satisfies Sybil-resistance. Assuming AESPs and $G_{att}$, the protocols
may eliminate the online distributed committee assumed in other
research such as CanDID; thus, $\Pi^{G_{}att}$ allows not to rely on multiparty
computation (MPC), and it brings drastic flexibility and
efficiency compared with the existing SSI systems.
Classification: DI
Link to the paper: https://ieeexplore.ieee.org/abstract/document/9881847
Score: no idea
Score Phase 1: Not relevant
Year: 2022

This article is mainly based on the following 2 articles.

- D. Maram, H. Malvai, F. Zhang, N. Jean-Louis, A. Frolov, T. Kell,
T. Lobban, C. Moy, A. Juels, and A. Miller, “CanDID: Can-Do Decentralized
Identity with Legacy Compatibility, Sybil-Resistance, and
Accountability,” in 2021 IEEE Symposium on Security and Privacy (SP),
May 2021, pp. 1348–1366.
[https://www.arijuels.com/wp-content/uploads/2020/07/Candid.pdf](https://www.arijuels.com/wp-content/uploads/2020/07/Candid.pdf)
- R. Pass, E. Shi, and F. Tram`er, “Formal Abstractions for Attested Execution
Secure Processors,” in Advances in Cryptology – EUROCRYPT
2017, vol. LNCS, volume 10210, Apr. 2017, pp. 260–289.
[https://eprint.iacr.org/2016/1027.pdf](https://eprint.iacr.org/2016/1027.pdf)

Their system’s sybil-resistancy is based on canDID. But in the article their system eliminates distributed committee used in canDID by Utilizing Attested Execution Secure Processors. So MPC is not required, it makes the system efficient. But this is not in our favor. On the contrary, it is one of our possible solutions to designate the canDID committee as operators.