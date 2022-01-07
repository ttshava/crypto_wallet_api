# Simple Django REST API Cryptocurrency wallet

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





Endpoint |HTTP Method | API Method | Result
-- | -- |-- |--| --
BITCOIN |  |  |
`btc-address-list` | GET | READ | [http://127.0.0.1:8000/wallet/btc-address-list/] | Get all bitcoin addresses
`btc-detail/:id` | GET | READ |[http://127.0.0.1:8000/wallet/btc-detail/] |Get bitcoin address details
`btc-create`| POST | CREATE |[http://127.0.0.1:8000/wallet/btc-create/]| Generate new bitcoin address
ETHEREUM |  |  |
`eth-address-list` | GET | READ | [http://127.0.0.1:8000/wallet/eth-address-list/]| Get all eth addresses
`eth-detail/:id` | GET | READ |[http://127.0.0.1:8000/wallet/eth-detail/]| Get eth address details
`eth-create`| POST | CREATE |[http://127.0.0.1:8000/wallet/eth-create/] |Generate new eth address


  
 
  
 


