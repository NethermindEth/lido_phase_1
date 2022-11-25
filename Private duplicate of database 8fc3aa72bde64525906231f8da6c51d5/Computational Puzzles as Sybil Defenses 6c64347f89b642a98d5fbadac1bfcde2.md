# Computational Puzzles as Sybil Defenses

Abstract: We consider the problem of defending against Sybil
attacks using computational puzzles. A fundamental difﬁculty in
such defenses is enforcing that puzzle solutions not be reused by
attackers over time. We propose a fully decentralized scheme
to enforce this by continually distributing locally generated
challenges that are then incorporated into the puzzle solutions.
Our approach consists of an all-to-all broadcast of challenges,
with a combining function to ensure this can be done efﬁciently.
The combining function generates certiﬁcates that can be used
to prove that each node’s challenge was delivered to and used by
each other node, therefore proving the freshness of each puzzle.
We show how our distribution and veriﬁcation mechanisms can
be implemented on top of the the Chord overlay.
Link to the paper: https://ieeexplore.ieee.org/document/1698607
Score: no idea
Score Phase 1: Maybe relevant

I rate this paper may be revevant for sybil resiliance.

The authors proposed a fully decentralized mechanism to defend against the sybil attacks using the computation puzzles. To address the puzzle pre-computation through the distribution of the  fresh challenges. This mechanism allows each participant to verify that its challenge was delivered to each other participant and therefore locally verify the freshness of the puzzle solution.