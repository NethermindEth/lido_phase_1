# Work of Camenisch and Lysyanskaya on Anonymous Credentials

Abstract: [From the paper “Signature Schemes with Efficient Protocols” by Camenisch and Lysyanskaya]
Digital signature schemes are a fundamental cryptographic primitive, of use both in its own right, and as a building block in cryp-tographic protocol design. In this paper, we propose a practical and provably secure signature scheme and show protocols (1) for issuing a signature on a committed value (so the signer has no information about the signed value), and (2) for proving knowledge of a signature on a committed value. This signature scheme and corresponding protocols are a building block for the design of anonymity-enhancing cryptographic sys-tems, such as electronic cash, group signatures, and anonymous creden-tial systems. The security of our signature scheme and protocols relies on the Strong RSA assumption. These results are a generalization of the anonymous credential system of Camenisch and Lysyanskaya.
Classification: Anonymous Credentials
Labels: Anonymous Credentials, Classic reference, Good reference source, Signature scheme, Verifiable Credentials
Link to the paper: https://link.springer.com/chapter/10.1007/978-3-540-28628-8_4
Score: no idea
Score Phase 1: Relevant
Year: 1990-2005

In this note we provide a brief overview of some classical work on Anonymous Credentials. The motivation for doing so is due to:

- Some of these works are used as a primitive of some bigger credential system.
- For completeness of the database.
- For academic and literary purposes.

# Introduction

Camenisch and Lysyanskaya are central authors in the Anonymous Credential (AC) literature published 1990-2005 (approximately). Their methods for constructing AC’s have appeared as a primitive in several other papers and projects we have reviewed (see below).

Sometimes they are referred to as “classical Anonymous Credential systems” (see, e.g. the paper from [Zero-knowledge credentials with deferred revocation checks](Zero-knowledge%20credentials%20with%20deferred%20revocatio%20e3684d2933e7499a8757a1c8c77e0e9b.md))

Next we list some papers of these two authors. We also mention other projects where such references have been used.

- **A signature Scheme with Efficient Protocols**  and **Efficient Attributes for Anonymous Credentials** (Camenisch and Gross): The AC scheme presented there is used in [Towards Smart Contract-based Verification of Anonymous Credentials](Towards%20Smart%20Contract-based%20Verification%20of%20Anony%202b002bb58dc44774a64a4f7c76c56b5f.md). They are also natively supported in [Hyperledger Indy](Hyperledger%20Indy%206ca56848c73a4a3a821c82813af6241d.md).
    
    The primitives are based on the strong RSA assumption.
    
- **Signature Schemes and Anonymous Credentials from Bilinear Maps.** Primitives are based on a variation of the Discrete Log assumption. This variation holds generically in the plain model.
- **An Efficient System for Non-transferable Anonymous Credentials with Optional Anonymity Revocation**, used (a variation) in [Zero-knowledge credentials with deferred revocation checks](Zero-knowledge%20credentials%20with%20deferred%20revocatio%20e3684d2933e7499a8757a1c8c77e0e9b.md) (Microsoft’s paper)

# Abstract primitives

The authors define an AC to be an Issuer’s signature on the Holder’s private key $sk$, and perhaps some further attributes.

To create and use such AC’s, they build the following primitives:

- A signature scheme.
- A **Protocol A** that allows a party H (the holder, in our case) to commit to a value $v$, and another party S (the issuer) to sign $v$. This must occur without S learning anything about $v$.
- Another **Protocol B** that allows to prove knowledge of a signature on a committed value.

With these, the Holder can obtain a signature on its secret key $sk$, with the Issuer never learning $sk$. This allows the Holder to remain anonymous. 

Additionally, the Holder can now prove to a Verifier that it knows a signature from the Issuer on $sk$. Again, no private data is leaked.

**Remark 1 — Strong privacy goals**

This emphasis on the Holder remaining anonymous to the Issuer is stronger than in other projects we have reviewed, such as W3C’s specification (where it is not discouraged nor recommended).

**Remark 2 — Why sign the secret key**

Why sign $sk$ and not the Holder’s public key $pk$? If the AC was a signature on, say, $pk$, anyone could impersonate the Holder.

**Remark 3 — Efficiency constraints**

In principle, Protocol A could be realized by a 2-party computation protocol; and Protocol B could be realized by a ZK proof of knowledge.

However around 1990-2005 these primitives where not efficient enough. As a result, part of the two author’s work is motivated by the need of circumventing these two technical limitations. As a result, the authors designed several efficient signature schemes together with the special protocols described previously.

# Anonymous Credential system from the paper “A signature scheme with efficient protocols”

In this section we describe a variation of the AC scheme presented in the paper “A signature scheme with efficient protocols” by Camenisch and Lysyanskaya.

The variation appears in the paper “Efficient Attributes for Anonymous Credentials” by Camenisch and Gross. It is the scheme used in the paper [Towards Smart Contract-based Verification of Anonymous Credentials](Towards%20Smart%20Contract-based%20Verification%20of%20Anony%202b002bb58dc44774a64a4f7c76c56b5f.md) 

The variation defines an AC as an Issuer’s signature on the Holder’s secret key $sk$, together with some attributes $A_1, \ldots, A_k$. The scheme allows for efficient selective disclosure of attributes during verification time.

The original scheme of Camenisch and Lysyanskaya did not support usage of attributes.

## Strong RSA assumption

The security of the scheme relies on the following assumption:

> **Strong RSA assumption** 
Given an RSA modulus $n=pq$ (with $p,q$ being “safe primes”)  and a random element $g\in\mathbb{Z}_n^*$, it is hard to compute $h\in  \mathbb{Z}_n^*$  and an integer $e> 1$ such that $h^e \equiv g \mod n$,
> 

It differs from the usual RSA assumption in that the adversary is able to choose the exponent $e$.

It holds “generically” in the plain model.

- **Plain model**: Does not assume existence of random oracles.
- **Genericity**: Roughly, this is a scenario where algorithms are only allowed to use group operations and equality checks. Elements are represented with a bit-string encoding that leak no information.

## Camenisch-Lysyanskaya (CL)-signatures

**Parameters**: $\ell_m, \ell_e, \ell_n, \lambda, L$. The parameter $\lambda$ is the security parameter.

**Key generation:** Choose an $\ell_n$-bit RSA modulus $n=pq$. Choose uniformly random $R_0, \ldots, R_{L-1}, S, Z \in QR_n$, where…

The public key is $pk= (n, R_0, \ldots, R_{L-1}, S, Z)$.

The secret key is $sk=p$.

**Message space**: $\{ (m_0, \ldots, m_{L-1}) \mid m_i \in \pm \{0,1\}^{\ell_m} \}$

Here $\pm \{0,1\}^{\ell_m}$ denotes the set of all positive integers of up to $\ell_m$ bits, together with all their additive inverses.

In the AC scheme, $m_0$ is the Holder’s secret key, and $m_1, \ldots, m_{L-1}$ are Holder’s attributes.

**Signing algorithm**:

On input $(m_0, \ldots, m_{L-1})$, choose a random prime $e$ and a random integer $v$ of sufficient bit length ( $\ell_e > \ell_m+2$ and $\ell_v=\ell_n + \ell_m + \lambda, respectively)$.

Compute

$$
\begin{equation}A:= \left(\frac{Z}{R_0^{m_0} \cdots R_{L-1}^{m_{L-1}}S^v }\right)^{1/e} \mod n.\end{equation}
$$

(this is done by finding $d$ such that $ed \equiv 1 \mod (p-1)(q-1)$ and taking $A= \left(\frac{Z}{R_0^{m_0} \cdots R_{L-1}^{m_{L-1}} }\right)^d$)

The signature is $(e, A, v)$.

**Verification algorithm**

To verify that $(e,A,v)$ is a signature on $(m_0,\ldots, m_{L-1})$, one checks that Equation (1) holds by asserting:

$$
Z\equiv A^e R_0^{m_0} \cdots R_{L-1}^{m_{L-1}}S^v \mod n\\
$$

Additionally one also checks that $m_i\in \pm \{0,1\}^{\ell_m}$ for all $i$ (i.e. the message has the correct shape) and that  $2^{\ell_e} > e > 2^{\ell_e -1}$ (i.e. $e$ is in the correct range).

**Theorem [Camenisch and Lysyanskaya]** Under the strong RSA assumption, this signature scheme is secure against an attacker with adaptive chosen messages 

(i.e., that’s an attacker $\mathcal{A}$ that has an oracle for generating signatures on messages of $\mathcal{A}$’s choice, and its goal is to create valid signatures without the use of the oracle (I don’t know if it is secure for existential forgeries or selective forgeries)).

## Protocol B: Proving ownership of a CL signature

The goal is to allow a signature holder to prove it has a valid signature from the signature issuer without revealing the message signed, **nor the signature** (this is for unlinkability purposes).

We will use zero knowledge proofs of knowledge of discrete logarithms. I.e. a protocol that allows to, given $z, g_1,\ldots, g_m$, prove in ZK that one knows $\gamma_1, \ldots, \gamma_m$ such that

$z= g_1^{\gamma_1}\ldots g_m^{\gamma_m}$.

With such a proof of knowledge, the signature holder could revel $A$, and then prove in ZK that it knows $(e, v, m_0, \ldots, m_{L-1})$ such that 

$$
Z\equiv A^e R_0^{m_0} \cdots R_{L-1}^{m_{L-1}}S^v \mod n.\\
$$

Recall that in our AC scheme the signature $(e,A,v)$ is treated as an Anonymous Credential. The protocol just described would be used to verify a credential without revealing its contents (= the signed message). 

However, as is, each time the same credential is verified, the same value $A$ is revealed. This makes  verification of credentials **linkable**.

Below we see how to avoid revealing $A$.

(**Note**: For simplicity we omit some technicalities, such as the fact that the elements $m_i$ and $e$ need to be “range-checked”)

Other than that, it can be seen that proving knowledge of such tuple $(e, v, m_0, \ldots, m_{L-1})$ essentially implies that someone who knows the secret key $p$ has provided the holder with $(A, e, v).$

 

**How to avoid revealing $A$?**

Notice that if $(e, A, v)$ is a valid signature on $(m_0, \ldots, m_{L-1})$, then for any integer $s$,

$$
(e, A':= AS^{-r} \mod n, v':= v+er) 
$$

is also a valid signature. Indeed:

$$
A'{}^{e} R_0^{m_0} \cdots R_{L-1}^{m_{L-1}}S^{v'} \equiv A^eR_0^{m_0} \cdots R_{L-1}^{m_{L-1}} S^{-re} S^{v+er} \equiv Z \mod n\\
$$

Hence, instead of revealing $A$, the signature holder can choose a random $s$, reveal $A' : AS^{-r} \mod n$, and follow the strategy outlined previously to prove that it knows $(e, v’, m_0, \ldots, m_{L-1})$ such that $A'{}^{e} R_0^{m_0} \cdots R_{L-1}^{m_{L-1}}S^{v'} \equiv Z \mod n$.

In this case, the information revealed will be different each time this subprotocol is executed, making credential verification unlinkable.

**Note**: to switch on linkability, simply stop sampling reveal $A$ during verification.

This can be interesting to prevent double usage of the same credential.

## Protocol A: Signing a committed message with the signer not learning the message

Let $\vec{m}:=(m_0, \ldots, m_{L-1})$ be a message held by the **Holder**.

**Commitment**

To commit $\vec{m}$ we use a Pedersen-type commitment. Namely, we take parameters $g_0,\ldots, g_m, h\in \mathbb{Z}_n^*$ be random elements. Then, to commit $\vec{m}$, the Holder chooses a random integer $r$ and sets

$$
Com(\vec{m}; r):= h^r \prod_{i=0}^{L-1} g_i^{m_i} \mod n
$$

(Note: This commitment scheme is normally used in groups where the Discrete Log is hard, and not in RSA groups, but ****[Damgard and Fujisaki showed](https://eprint.iacr.org/2001/064) that it can be used on an RSA group to commit integers of arbitrary size).

**Signing on the committed message**

Suppose the Holder has published a commitment $C$ to its message $\vec{m}$.

Then the Holder chooses a random integer $u$ and publishes

$$
C'= R_0^{m_0} \cdots R_{L-1}^{m_{L-1}} S^u
$$

Next the Holder proves in zero-knowledge that $C$ and $C'$ are Pedersen commitments to the same message using a dedicated subprotocol. 

Now the Signer proceeds as in the original signing algorithm, computing

$$
A:= \left(\frac{Z}{C' S^{v} }\right)^{1/e} \mod n.
$$

for some random $v'$, $e>1$, and publishing $(e,A,v)$ as the signature.