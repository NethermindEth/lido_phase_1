# ION by Microsoft and DIF

Abstract: “ION is a public, permissionless, Decentralized Identifier (DID) network
that implements the blockchain-agnostic Sidetree protocol on top of
Bitcoin (as a ’Layer 2’ overlay) to support DIDs/DPKI (Decentralized
Public Key Infrastructure) at scale”
Classification: DI
Labels: Management of credentials, Not Sybil resistant
Link to the paper: https://github.com/decentralized-identity/ion
Score: no idea
Score Phase 1: Maybe relevant

Ion is a distributed identity system anchored to the Bitcoin blockchain.  The data itself is stored in the IPFS.

Each user is responsible for updating the state of his own identity, thus it isn’t useful for Sybil resistance.

## Operations

The owner of the DID document can perform four types of operations on it:

- Create
- Update
- Recover, i.e., reset the document
- Deactivate

There are separate Update and Recovery keys so users can delegate their ability to update documents while reserving the ability to reset the document if their proxy goes rogue.

The Update and Recovery keys must be regenerated after each operation of the corresponding type.

The hash of the public key will be used as a *reveal value*, which will be hashed again to produce the *public key commitment*.  Each operation must include the commitment value to be used for the next operation of the same type.  The next operation will include the reveal value, so that the logic can filter out invalid operations without needing to perform signature verification.

## Transactions

Up to 10,000 operations can be grouped together into a single transaction, whose hash is then put on the Bitcoin blockchain.  This appears to be done by (volunteer!?) node operators, who are also responsible for paying the transaction fees.  There is also a minimum transaction fee and mandatory value locking to prevent spam.  In practice this will probably mean only the ION team runs a node.

The operations themselves are stored in the IPFS (InterPlanetary File System).

## Network Topology

The following diagram illustrates the primary components of the Sidetree-based network.

1. The anchoring blockchain.  (Bitcoin)
2. The nodes which interact with the system to perform operations.
3. The Content-Addressable Storage (IPFS) the stores and replicates the data.

![Untitled](ION%20by%20Microsoft%20and%20DIF%20df04127fffb840cc94d66a4e23fc7ddb/Untitled.png)

Source of picture: [https://identity.foundation/sidetree/spec/#network-topology](https://identity.foundation/sidetree/spec/#network-topology)