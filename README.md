# Arbitrage
***Flash loan arbitrage contract***

## Setup
* Install Brownie 
  ```shell
  python3 -m pip install --user pipx
  python3 -m pipx ensurepath
  # restart your terminal
  pipx install eth-brownie
  ```
* Install requirements 
  ```shell
  pip install -r requirements.txt
  ```
* Install `ganache-cli`
  * using npm:
  ```shell
  npm install -g ganache-cli
  ```
  * or, if you are using Yarn:
  ```shell
  yarn global add ganache-cli
  ```
* Create `.env` file with the following values:
  * `PRIVATE_KEY` - Private key of the wallet account 
  * `WEB3_INFURA_PROJECT_ID` - Project ID of the Infura project
  * `POLYGONSCAN_TOKEN` - API key for the polygonscan account


## Deploy 
### Local environment
Deploy the contract to a local development network: 
```shell
brownie deploy scripts/deploy.py --network development
```
This will initialize a local ganache environment, which will be cleaned 
when the script finishes.

### Polygon test
Deploy the contract to the *Mumbai testnet*: 
```shell
brownie deploy scripts/deploy.py --network polygon-test
```
The contract can be seen at https://mumbai.polygonscan.com/address/<contract_address>

### Polygon main
Deploy the contract to the *polygon mainnet*: 
```shell
brownie deploy scripts/deploy.py --network polygon-main
```
**Note**: This will remove real money from the account (gas fees)

## Test
For running tests, run the following command:
```shell
brownie test -s
```
Note: 
  * For running on a different network from what's configured as default, 
  the `--network` flag can be passed.
  * The `-s` flag allow us to get the output printed while running the tests.  
