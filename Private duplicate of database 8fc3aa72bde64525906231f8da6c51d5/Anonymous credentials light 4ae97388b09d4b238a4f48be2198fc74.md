# Anonymous credentials light

Abstract: We define and propose an efficient and provably secure construction of blind signatures with attributes. Prior notions of blind signatures did not yield themselves to the construction of anonymous credential systems, not even if we drop the unlinkability requirement of anonymous credentials. Our new notion in contrast is a convenient building block for anonymous credential systems. The construction we propose is efficient: it requires just a few exponentiations in a prime-order group in which the decisional Diffie-Hellman problem is hard. Thus, for the first time, we give a provably secure construction of anonymous credentials that can work in the elliptic group setting without bilinear pairings and is based on the DDH assumption. In contrast, prior provably secure constructions were based on the RSA group or on groups with pairings, which made them prohibitively inefficient for mobile devices, RFIDs and smartcards. The only prior efficient construction that could work in such elliptic curve groups, due to Brands, does not have a proof of security.
Classification: Anonymous Credentials
Labels: Anonymous Credentials, Signature scheme
Link to the paper: https://dl.acm.org/doi/10.1145/2508859.2516687
Score: no idea
Score Phase 1: Maybe relevant
Year: 2013

# Introduction

This paper defines the notion of **blind signatures with attributes** that are based on Abe’s blind signature scheme [[1]](https://www.iacr.org/cryptodb/data/paper.php?pubkey=1981) which is a modified version of Schnorr scheme.  In a blind signature with attributes, the signer and the user take a commitment $C$ to the user's attributes as input, and it outputs another (unlikable) commitment $\tilde{C}$ to the same attributes along with a signature on this commitment and a message of the user's choice. Note that taking the commitment to the user’s attributes as input gives the user the ability to prove in zero-knowledge that the committed data includes correct attributes.

Note that a blind signature with attributes can be used to construct an anonymous credential scheme as follows.

1. A user with some attributes can generate a commitment $C$ to his attributes. 
2. He can prove in zero-knowledge that the commitment $C$ is generated from correct attributes.
3. He runs a blind signature with attributes with commitment $C$. 
4. Now he can convince any verifier that he has a credential that includes the desired attributes as  follows:
    1. He presents his signature and the output commitment $\tilde{C}$, and 
    2. He proves in zero-knowledge that $\tilde{C}$ corresponds to those attributes.

# Preliminary

## OR-proof

An OR-proof is a $\Sigma$-protocol for a relation $R_L$ in which the prover and the verifier have the common inputs $h_0$ and $h_1$, and the prover knows an $x$ such that $(h_i,x) \in R_L$ for $i \in \{0,1\}$. 

The main idea of an OR-proof is that the prover completes two $\Sigma$-protocols such that the verifier will not be able to distinguish which protocol the prover knows a witness for. Recall that in a $\Sigma$-protocol the transcript between the prover and the verifier is denoted by $(a_i, c_i, r_i)$ where $a_i$ is the first message of the prover, $c_i$ is the random challenge of the verifier, and $r_i$ is the respond of the prover to the verifier. And note that the prover follows one of the protocols correctly, but for the other one he generates the transcripts by using a simulator.

An OR-proof works as follows:

- The prover
    - computes the first message $a_i$ for the protocol $\Sigma_i$ by taking $(h_i,x)$ as input
    - chooses a random $c_{1-i}$ and runs the simulator $SIM$ on input $(h_{1-i}, c_{1-i})$. The simulator $SIM$ outputs $(a_{1-i}, c_{1-i}, r_{1-i})$.
    - sends $a_0, a_1$ to the verifier.
- The verifier picks a random $e$ and sends it to the prover.
- The prover
    - computes $c_i = e \oplus c_{i-1}$
    - computes $r_i$ for the challenge $c_i$ by using $h_i, a_i,c_i,x$
    - sends $c_0, c_1, r_0, r_1$ to the verifier.
- The verifier checks
    - $e = c_0 \oplus c_1$
    - whether both $(a_0,c_0,r_0)$ and $(a_1, c_1, r_1)$ are accepting transcripts.

## Generalized Pedersen commitment

The Pedersen commitment is based on discrete logarithm assumption. This paper uses a generalized version of the Pedersen commitment scheme on the set of messages $(L_1,\dots, L_n)$  as follows:

- **Setup:**  Assume that the security parameter is $\kappa$, and the maximum number of messages is $n$. Let $G$ be a group with prime order $q=\Theta(2^{\kappa})$ with generators $h,h_1,\dots,h_n$. Let $R$ be randomness.
- **Commit:** $Commit(L_1,\dots,L_n;R) = h^R\prod_{i=1}^{n}h_i^{L_i}$, where $L_i \in \Z_q.$

Note that Pedersen commitment is information-theoretically hiding and computationally binding.

### Combined commitment scheme

Assume that we have a commitment $Commit_1$ to the set of data $(L_1\dots,L_n)$ with the randomness $R_1$. Suppose that we have a second commitment $Commit_2$ to the data $(L_0)$ with the randomness $R_2$. Then the combined commitment, i.e. $Commit$, which is a commitment to the data $(L_0,L_1,\dots,L_n)$ with the randomness $R = R_1+R_2$. 

For example, let us instantiate it with generalized Pedersen commitment. Assume that the generators are $h,h_0,\dots,h_n$. Assume we have two commitments as follows:

- $Commit_1(L_1,\dots,L_n;R_1) = h^{R_1} \prod_{i=1}^{n}h_i^{L_i}$
- $$Commit_2(L_0;R_2) = h^{R_2} h_0^{L_0}

### Blinded Pedersen commitment scheme

## Assumption

The security of the proposed scheme is based on the Decisional Diffie-Hellman assumption and the Discrete-Logarithm assumption. 

## Notation and setup

- Let $G$ be a group of order $q$
- Let $g$ be a generator of $G$
- Let $H:\{0,1\}^*\to\Z_q$ be a hash function
- Assume a trusted party $TD$ chooses $params= (q,G,g,z,h,h_0,\dots,h_n)$ as system parameters, where $z,h,h_0,\dots,h_n \in G$ and $n$ is the maximum number of attributes that a user can have.
- The signer randomly selects a private key $x\in_R\Z_q$ and computes his **real public key** $y=g^x \pmod q$.
- Given $(G,q,g,h,y)$  , the $TP$ outputs $z$ which is the **tag public key** of the signer.
- Therefore the public key of the signer is $(G,q,g,h,y,z)$, and the private key is $x$.

## Anonymous Credential Light (ACL)

In a nutshell, the protocol proceeds as follows. The user and the signer take inputs as described in the below figure. The user commits ($C$) to certain attributes that he claims he has. Then the user proves in zero-knowledge that he knows an opening of the commitment $C$. 

Then, the signer computes some one-time tag keys depending on a randomness and the commitment $C$, and sends the randomness to the user so that he can check and compute the same one-time tag key. 

The user computes another commitment $\tilde{C}$ which is a blinded Pedersen commitment to the same attributes. (See $\zeta, \zeta_1$ in the below figure)

The signer and the user perform two $\Sigma$ protocols. In the end, the user computes the blind signature with attributes $\sigma$. (see the below figure)

## Signature / Credential issuing

The signature issuing scheme is run in three phases, i.e. **registration**, **preparation**, and **validation**. The registration phase is a one-time phase that should be performed only once for each user. The preparation and validation phases may be performed simultaneously. 

### Registration

- The user inputs
    - the system parameters $params$,
    - the signer's real public key $y$, (such that $y=g^x$, where $g$ is a generator of a group $G$ included in $params$)
    - the message $m$ to be signed and
    - $(L_1, \dots, L_n, R)$ where $L_1, \dots, L_n$ is a set of attributes, and $R$ is some randomness.
- The signer inputs
    - the system parameters $params$,
    - a commitment $C = Commit(L_1,\dots, L_n, R)$ and
    - his secret key $x$.

The user and the signer participate in a standard interactive zero-knowledge proof of knowledge protocol where the user creates a proof $\pi_1$ to convince the signer that he knows an opening of the commitment $C$.

### Preparation

- The signer prepares $z_1$ and $z_2$, i.e. $z_i = g^{w_i}$ where $w_i$ is a random secret.
    - He picks $rnd \in \Z_q$ and creates the ``one-time" tag keys: $z_1 = C\cdot g^{rnd}$ and $z_2 = z/z_1$.
    - The signer sends $rnd$ to the user in order to convince him that $\log_g z_1$ is not known to him.
- The User checks
    - $rnd \ne 0$ and
    - computes $z_1 = C\cdot g^{rnd}$ and
    - picks $\gamma \in \Z_q^*$ and blinds $z, z_1, z_2$ into  $\zeta= z^{\gamma}, \zeta_1 = z_1^{\gamma}, \zeta_2 = \zeta/\zeta_1$ so that $\log_z z_1 = \log_{\zeta} \zeta_1$ holds.
- The user picks  $\tau \in \Z_q$ and computes  $\eta = z^{\tau}$.

### Validation

In this phase, parties perform two different $\Sigma$ protocols, i.e. $\Sigma_y$ and $\Sigma_z$. Note that the transcript of $\Sigma_y$ is denoted by $(a,c,r)$, and the transcript of $\Sigma_z$ is denoted by $(a',c',r')$. The protocol $\Sigma_z$ will be performed only by the signer, but the $\Sigma_y$ protocol will be performed interactively. In the end, these $\Sigma$ protocols will be combined according to the OR-proof.

- (for $\Sigma_y$) The signer
    - picks a random $u \in \Z_q$ and
    - computes $a = g^u$.
- (for $\Sigma_z$) The signer
    - picks random $c' \in \Z_q$ and $r' = \{r_1', r_2' \in \Z_q\}$, and
    - sets $a_1' = g^{r_1'}z_1^{c'}$ and $a_2' = h^{r_1'}z_2^{c'}$,
    - sends $a,a' = \{a_1', a_2'\}$  to the user.
- The user
    - checks whether $a, a_1', a_2' \in G$
    - picks random blinding factors $t_1, t_2, t_3, t_4, t_5 \in_R \Z_q$
    - blinds $a$ into $\alpha = ag^{t_1}y^{t_2}$
    - blinds $a_1', a_2'$ into $\alpha_1' = a_1'^{\gamma}g^{t_3}\zeta_1^{t_4}$ and $\alpha_2' = a_2'^{\gamma}h^{t_5}\zeta_2^{t_4}$ (note that we denote $\alpha'=\{\alpha_1',\alpha_2'\}$)
    - computes $\varepsilon = H(\zeta, \zeta_1, \alpha, \alpha',\eta,m)$, where $m$ is the message to be signed
    - sends $e = \varepsilon-t_2-t_4 \pmod{q}$  to the signer.
- The signer
    - computes $c = e - c' \pmod{q}$
    - computes $r = u - cx \pmod{q}$
    - sends $c,r,c',r'$ to the user.
- The user unblinds the received values and obtains
    - $\rho = r + t_1 \pmod{q}$
    - $\omega = c + t_2 \pmod{q}$
    - $\rho_1' = \gamma r_1' + t_3 \pmod{q}$
    - $\rho_2' = \gamma r_2' + t_5 \pmod{q}$
    - $\omega' = c' + t_4 \pmod{q}$
    - $\mu = \tau - \omega'\gamma \pmod{q}$
- The signature $\sigma$ is a 8-tuple, i.e.  $\sigma = (m, (\zeta, \zeta_1, \rho, \omega,\rho'= \{\rho_1',\rho_2'\}, \omega',\mu))$, where $\zeta_1$encodes the attributes of the user. Note that $\zeta, \zeta_1$ corresponds to the commitment $\tilde{C}$. In the below figure, one can find the entire ACL protocol.

![Source: [https://eprint.iacr.org/2012/298.pdf](https://eprint.iacr.org/2012/298.pdf)

Figure.1. This figure describes the ACL protocol explicitly. It has three phases, i.e. registration, preparation, and validation. The signer takes the system parameters $params$, his secret key $x$, and the commitment to the user’s attributes $C$ as inputs. The user takes the systems parameters $params$, the signer’s public key $y$, the message to be signed $$m$, a set of attributes $L_1, \dots, L_n$, and a randomness $R$ as inputs. ](Anonymous%20credentials%20light%204ae97388b09d4b238a4f48be2198fc74/Untitled.png)

Source: [https://eprint.iacr.org/2012/298.pdf](https://eprint.iacr.org/2012/298.pdf)

Figure.1. This figure describes the ACL protocol explicitly. It has three phases, i.e. registration, preparation, and validation. The signer takes the system parameters $params$, his secret key $x$, and the commitment to the user’s attributes $C$ as inputs. The user takes the systems parameters $params$, the signer’s public key $y$, the message to be signed $$m$, a set of attributes $L_1, \dots, L_n$, and a randomness $R$ as inputs. 

## Verification

Any verifier given a tuple $(m, \zeta_1, \sigma)$ can verify the signature by checking:

- $\zeta \ne 1$
- $\omega + \omega' = H(\zeta, \zeta_1, g^{\rho}y^{\omega},g^{\rho_1'}\zeta_1^{\omega'}, h^{\rho_2'}\zeta_2^{\omega'}, z^{\mu}\zeta^{\omega'},m) \pmod q$

### Correctness

Correctness of the ACL scheme follows from the below equations:

$$
\begin{align}
\omega + \omega' &= c + t_2  + c' +t_4 = \varepsilon \pmod q\\
g^{rho}y^{\omega} &= g^{r+t_1}y^{c+t_2}g^{r+cx}g^{t_1}y^{t_2} = \alpha \pmod q\\
g^{\rho_1'}\zeta_1^{\omega'}& = g^{\gamma r_1' +t_3}\zeta_1^{c'+t_4}=(a_1'z_1^{-\omega'})^{\gamma} g^{t_3}\zeta_1^{c'+t_4} = a_1'^{\gamma} g^{t_3}\zeta_1^{t_4} = \alpha_1'\\
g^{\rho_2'}\zeta_2^{\omega'} &= h^{\gamma r_2' +t_5}\zeta_2^{c'+t_4} = (a_2'z_2^{-\omega'})^{\gamma}h^{t_5}\zeta_2^{c'+t_4} = a_2'^{\gamma}h^{t_5}\zeta_2^{t_4}=\alpha_2'\\
z^{mu}\zeta^{\omega'}&= z^{\tau - \omega'\gamma}\zeta^{\omega'}=\zeta^{\gamma}= \eta\\
\end{align}
$$

### Single-Use Credentials

Single-use anonymous credentials avoid double use of the same credential. If a user uses the same anonymous credential with attributes twice, the verifier can reveal the user’s identity. 

Note that the first attribute in the attribute set, i.e. $L_1$, is the public key of the user. So, if a verifier can learn this attribute, he can also discover the identity of the user. 

This information, i.e. $L_1$ is used for avoiding double use of anonymous credentials for the same attributes.

## Relevancy assessment

This paper proposes an anonymous credential scheme that depends on a blind signature with attributes. Indeed the underlying signature scheme is used for proving the knowledge of some secrets with some zero-knowledge techniques. 

# References

[1] Masayuki Abe. A secure three-move blind signature scheme for polynomially many signatures. In EUROCRYPT, pages 136{151, 2001. [https://www.iacr.org/cryptodb/data/paper.php?pubkey=1981](https://www.iacr.org/cryptodb/data/paper.php?pubkey=1981)