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
The crytocurrency RESTful API, endpoints (URLs):

>1: Generate <b>valid</b> BTC / Ethereum address
>2. List addresses (BTC/ETH)
>3. Retrieve address (BTC/ETH)



Endpoint |HTTP Method | API Method | Result
-- | -- |-- |--
BITCOIN |  |  |
`btc-address-list` | GET | READ | Get all bitcoin addresses
`btc-detail/:id` | GET | READ | Get bitcoin address details
`btc-create`| POST | CREATE | Generate new bitcoin address
ETHEREUM |  |  |
`eth-address-list` | GET | READ | Get all eth addresses
`eth-detail/:id` | GET | READ | Get eth address details
`eth-create`| POST | CREATE | Generate new eth address


  
 
  
 


