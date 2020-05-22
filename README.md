# Issuer, Verifier and Client Controllers for the Aries Cloud Agent - Python  

Demo controllers on top of the aca-py agent for the purposes of the DEON project. In the demo folder, you can find the credential issuer (ci) controller which issues credentials to applications and users, the msp controller which is a custom MSP for Fabric that verifies DID-signed transactions and the client controller which acts on behalf of a DEON application and signs its transactions with its DID.

## Aca-py agent Info

> An easy to use Aries agent for building SSI services using any language that supports sending/receiving HTTP requests.

[Repo](https://github.com/hyperledger/aries-cloudagent-python/)

Hyperledger Aries Cloud Agent Python (ACA-Py) is a foundation for building self-sovereign identity (SSI) / decentralized identity services running in non-mobile environments using DIDcomm messaging, the did:peer DID method, and verifiable credentials. With ACA-Py, SSI developers can focus on building services using familiar web development technologies instead of trying to learn the nuts and bolts of low-level SDKs.

The "cloud" in Aries Cloud Agent - Python does **NOT** mean that ACA-Py cannot be used as an edge agent. ACA-Py is suitable for use in any non-mobile agent scenario, including as an enterprise edge agent for
issuing, verifying and holding verifiable credentials.

## Run

The running process is the default process of running the aca-py demo controllers using docker. It requires having a von-network instance running in docker locally. After running the von-network locally, clone this repository and open a terminal for each of the agents you want to deploy and execute the following commands:

```bash
# clone this repository
git clone https://github.com/off-grid-block/aca-py-controllers.git

# cd into the repository's demo directory 
cd aca-py-controllers/demo/

# Start the ci agent by issuing the following command:

  ./run_demo ci

# Start the msp agent by issuing the following command:

  ./run_demo msp
  
# Start the client agent by issuing the following command:

  ./run_demo client

# Start the ci_msp agent by issuing the following command:

  ./run_demo ci_msp
  
  ```
