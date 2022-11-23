# Security of the Decentralized Anonymous Credentials

Authors define their system in terms of an ideal functionality implemented by a trusted party $T_P$ that plays the role that system’s cryptographic constructions play in the real system. All communication takes place through this ideal trusted party. Security and correctness for the system come from a proof that this ideal model is indistinguishable from the real model provided the cryptographic assumptions hold.

- $RegNym(Nym^O_U , U, O$): $U$ logs into $T_P$ with $sk_U$ to register a nym with organization $O$. If she does not have an account, she first creates one. She gives $T_P$ a unique random string $Nym^O_U$. $T_P$ checks that the string is indeed unique and if so stores $(Nym^O_U , U, O)$ and informs $U$.
- $M intCred(Nym^O_U , O, attrs, aux)$: $U$ logs into $T_P$ with $sk_U$. If Nym $Nym^O_U$  is not $U's$ nym with $O$ or $sk_U$ is wrong, reject. Otherwise, $T_P$ checks that $aux$ justifies issuing a credential under $O's$ issuing policy and if so generates a unique random id $ID$ and stores $(Nym^O_U , U, ID, attrs)$. It then adds ID to its public list of issued credentials for $O$.
- $ShowOnNym(Nym^O_U,Nym^V_U,O,V,attrs,C)$: $U$ logs into $T_P$ with $sk_U$ . If $Nym^O_U$ is not $U's$ nym with $O$ or $Nym^V_U$ is not $U's$ nym with $V$, reject. Else, $T_P$ checks if the tuple $(Nym^O_U , U)$ exists, if $ID$ associated with that tuple is in the set of credentials $C$ that $U$provided, and if the given attributes $attr$ match the attributes associated with that tuple. If all
conditions hold, $T_P$ informs V that $Nym^V_U$ has a credential from $O$ in the set $C$. $V$ then retrieves the set of credentials $C_O$ issued by $O$ from $T_P$ and accepts $T_P^{'}s$ assertion if and only if $C \subseteq C_O$ and $O's$ issuing policy is valid  $\forall c  \in C_O$.
- $GetCredList(O)$: $T_P$ retrieves the list of credentials for organization $O$ and returns it.

**Theorem 6.1** The basic distributed anonymous credential system described above is secure in the random oracle model under the Strong RSA and the Discrete Logarithm (DL) assumptions.

The approach is to show that for every real-world adversary $\mathcal{A}$ against the credential system, we can construct an ideal-world adversary $\mathcal{S}$ against the ideal-world system such that the transcript of $\mathcal{A}$ interacting with the real system is computationally indistinguishable from the transcript produced by $\mathcal{A}$ interacting with $\mathcal{S}$.

**A. Description of the Simulator:**

**Minting a credential:**

- When a user controlled by the adversary $\mathcal{A}$ wants a credential, she generates $(c,\pi_M , attrs)$.
- When a simulator $\mathcal{S}$ receives the notification, verifies it and extract $(sk, aux)$ from the knowledge extractor for the SoK on $\pi_M$. $\mathcal{S}$ then checks if it has the record of $(U, sk , Nym^O_U)$ and extracts $sk_U$ (authentication key with $T_P$) . If $\mathcal{S}$ doesn’t hold this record, create it with $RegNym(Nym^O_U ,U,O)$ by interacting with $T_P$.
- $\mathcal{S}$ runs $MintCred(Nym^O_U , O, attrs, aux)$ and then transmit to the trusted store and stores $(sk , Nym^O_U , attrs, aux, c, \pi_M )$ in its list of granted credentials.
- When an honest user, through $T_P$ , wants to establish a credential, the simulator creates a credential $c$ (using the publicly available $attrs$) and uses the simulator for the signature of knowledge $\pi_M$ to simulate the associated proof. It then transmits the credential information $(c, \pi_M, attrs)$ to the trusted store.

**Showing a credential:**

The simulation works in similar to the Minting a credential, instead, the simulator $\mathcal{S}$ runs $ShowOnNym(Nym^O_U , Nym^V_U , O, V, C)$, where $C$ is generated through a call to $GetCredList(O)$. Here, $\mathcal{S}$ extracts the private information from the knowledge extractor to the $\pi_S$ created by the user (who was controlled by the adversary $\mathcal{A}$)

**Proof (sketch) of a successful simulation:**

Under the Discrete Logarithm assumption, $\pi_M$ is a computational ZKSoK on $aux$ of the values $(sk, r, r')$ such that the nym $Nym^O_U$ and the credential $c$ both belong to the same master secret $sk$. An attacker might forge this message by identifying a collision on the commitments, which occurs with negligible probability under DL assumption. 

Under the Strong RSA and Discrete Logarithm assumptions, $\pi_S$ is a statistical NI-ZKPoK of the values $(sk , w, c, Nym^V_U , r, r')$ s.t. $w$ is a witness that $c$ is in the accumulator $A$ and nym $Nym^V_U$ and the credential $c$ both belong to the same master secret $sk$. An attacker might forge this, by finding a collision on the commitment which occurs with negligible probability under DL assumption or forging the accumulator membership proof which occurs with negligible probability under the strong RSA assumption (collision-resistant property of the accumulator).

The simulator will fail at most with negligible property, as it deals with the ZKSoK and ZKPoK which have efficient extractors and simulators. The proofs $\pi_M$ and $\pi_S$ have knowledge extractors that succeed with probability $1 - negl(\lambda)$. Since signatures and proofs are the sole point of failure for our simulator $\mathcal{S}$ described above, it fails with negligible probability.