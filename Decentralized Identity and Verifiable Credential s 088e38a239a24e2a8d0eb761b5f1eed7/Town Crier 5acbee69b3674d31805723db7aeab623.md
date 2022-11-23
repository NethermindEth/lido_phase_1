# Town Crier

Abstract: Smart contracts are programs that execute autonomously on blockchains. Their key envisioned uses (e.g. financial instruments) require them to consume data from outside the blockchain (e.g. stock quotes). Trustworthy data feeds that support a broad range of data requests will thus be critical to smart contract ecosystems.
We present an authenticated data feed system called Town Crier (TC). TC acts as a bridge between smart contracts and existing web sites, which are already commonly trusted for non-blockchain applications. It combines a blockchain front end with a trusted hardware back end to scrape HTTPS-enabled websites and serve source-authenticated data to relying smart contracts. 
TC also supports confidentiality. It enables private data requests with encrypted parameters. Additionally, in a generalization that executes smart-contract logic within TC, the system permits secure use of user credentials to scrape access-controlled online data sources. 
We describe TC’s design principles and architecture and report on an implementation that uses Intel’s recently introduced Software Guard Extensions (SGX) to furnish data to the Ethereum smart contract system. We formally model TC and define and prove its basic security properties in the Universal Composability (UC) framework. Our results include definitions and techniques of general interest relating to resource consumption (Ethereum’s “gas” fee system) and TCB minimization. We also report on experiments with three example applications. We plan to launch TC soon as an online public service.
Added to deliverable?: No
Already read?: Yes
BS factor: important
Classification: Oracles
Link to the paper: https://www.town-crier.org/files/2016/168.pdf
MZ checked the note: No
Score Phase 1: Maybe relevant
Work Group: Hybrid

# Town Crier

### Components

- **On Chain**
    - **User Contract ($C_U$)**: Contract or account requests datagram from Town Crier.
    - **Town Crier Contract ($C_{TC}$**): Front end of TC, accepts request form $C_U$, returns corresponding datagrams from Town Crier off-chain server.
- **Off-Chain**
    - **Relay ($R$)**: Receives the request from $C_{TC}$, sends command to Enclave, relays HTTPS traffic to Enclave, emits the datagram from Enclave to $C_{TC}$.
    - **Enclave**: A safe and isolated code running environment, provides an attestation for the Enclave instance to prove that the Enclave is executing correct code.
    - $prog_{encl}$: A program run in Enclave that get and proceess data.
- **Data Source**
    - HTTPS websites

### Procedure

1. $C_U$ **requests a datagram** by calling $C_{TC}$, with enough gas. 
2. $C_{TC}$ **deliver the request to Off-Chain server**, $R$ receives the **request**, **id**, and **parameter**.
    - $C_{TC}$ will generate an id for every request.
    - $C_{TC}$ will send the parameters to Off-Chain server and store `SHA3-256(requestType||timestamp||paramArray)`, and recheck when it receives the response to prevent from $R$ tampering parameters.
    - Town Crier supports private datagrame requests by encrypting the parameters with the public key of Town Crier.
3. $R$ calls $prog_{encl}$ from Enclave, and transfers **HTTPS traffic** to Enclave. Enclave processes the data, and returns to $C_{TC}$.
    - Enclave will generate a signature of $prog_{encl}$ with **SGX private key** when initialized, which is hardcoded in SGX.
    - $prog_{encl}$ needs to use **same signature scheme** with **Ethereum**.
    - Enclave does not have direct access to host network functionality, thus $R$ acts as a **network interface**.
    - Enclave performs all **cryptographic operations** **internally**.
4. $C_{TC}$ return data to $C_U$. 
    - Signature verified by **Ethereum client** with **hardcoded public key** in $C_{TC}$
        
        > Since Ethereum itself already verifies signatures on transactions (i.e., users interact with Ethereum through an authenticated channel), **we can piggyback verification of $T_{Off}$ signatures on top of the existing transaction signature verification mechanism**. Simply put, the $T_{Off}$ creates $W_{TC}$ with a fresh public key $pk_{Off}$ whose secret is known only to $T_{Off}$. To make this idea work fully, the public key $pk_{Off}$ must be hardcoded into $T_{On}$. A client creating or relying on a contract that uses $T_{On}$ is responsible for ensuring that this hardcoded $pk_{Off}$ has an appropriate $SGX$ attestation before interacting with $T_{On}$.
        > 
    
    ![Untitled](Town%20Crier%205acbee69b3674d31805723db7aeab623/Untitled.png)
    

![Untitled](Town%20Crier%205acbee69b3674d31805723db7aeab623/Untitled%201.png)

### Attack-Resistant Mechanism

- **SGX**
    
    > Intel Software Guard Extensions (Intel SGX) offers **hardware-based** memory encryption that isolates specific application code and data in memory. Intel SGX allows **user-level** code to allocate private regions of memory, called **enclaves**, which are designed to be protected from processes running at higher privilege levels.
    > 
- **HTTP over TLS**: Message transferred by $R$ is encrypted HTTPS data, and decryption process is executed inside SGX.
- **Enhanced Robustness**: Town Crier can request data from multiple data sources for the same data, $C_{TC}$ can also request data from multiple Town Crier SGX nodes.

### Potential Risks

- **Freeloading**: in the current design, TW could not provide a freeloading protection.
- **DoS attack**: $R$ could start a DoS attack by analyzing traffic, intercepting the HTTPS data, so that $prog_{encl}$ will believe data source is offline and return a empty datagram.
- **Attack against SGX**: The safety mechanism is based on the safety of SGX, a vulnerability in SGX itself would be devastating for Twon Cirer.
    
    > [Foreshadow: Extracting the Keys to the Intel SGX Kingdom with Transient Out-of-Order Execution.](https://www.usenix.org/system/files/conference/usenixsecurity18/sec18-van_bulck.pdf)
    >