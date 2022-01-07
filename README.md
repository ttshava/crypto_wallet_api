# Simple Django REST API Cryptocurrency wallet
REST API for generating valid cryptocurrency addresses BTC and ETH.


## Project Requirements
1. Python 3.8
2. Django 3.1
3. Django REST Framework

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command
```
python -m venv env
```

After this, it is necessary to activate the virtual environment.

You can install all the required dependencies by running
```
pip install -r requirements.txt
```
## Structure
The crytocurrency RESTful API, endpoints (URLs):<br>
  >1. Generate <b>valid</b> BTC / Ethereum address<br>
  >2. List addresses (BTC/ETH) <br>
  >3. Retrieve address (BTC/ETH)<br>

```
http://127.0.0.1:8000/wallet/
```

Endpoint |HTTP Method | API Method | Result
-- | -- |-- |--
BITCOIN |  |  | 
`btc-address-list/` | GET | READ | Get all bitcoin addresses
`btc-detail/:id` | GET | READ |Get bitcoin address details
`btc-create/`| POST | CREATE | Generate new bitcoin address
ETHEREUM |  |  |
`eth-address-list/` | GET | READ |  Get all eth addresses
`eth-detail/:id` | GET | READ | Get eth address details
`eth-create/`| POST | CREATE |Generate new eth address


## Use & Testing Bitcoin addresses in blockchain

![Btc Addresses Generated](https://user-images.githubusercontent.com/7104155/148570677-3313cffe-9d49-47df-bc31-8b431c58ea27.PNG)


BTC Address : 14riWFbcN8pZP8o1Z78mWRDwsQT5fzCaTr


Use this link to test https://www.blockchain.com/btc-testnet/address/2N3oefVeg6stiTb5Kh3ozCSkaqmx91FDbsm

## How to generate BTC Address

```
http://127.0.0.1:8000/wallet/btc-create
```

To generate bitcoin address you need to enter id number and click post

{  
        "id": "9"    
    }

![generate](https://user-images.githubusercontent.com/7104155/148572060-8448d153-5eba-4118-a916-3620f28742b0.PNG)

The id is auto generated by here you have to manually add it for to generate the btc address


  
 
  
 


