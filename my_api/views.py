from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Btc, Eth
from .serializers import BtcSerializer, EthSerializer
from bitcoin import *
from eth_account import Account
import secrets


"""
ZEPLY Wallet API Overview

"""
@api_view(['GET'])
def apiOverview(request):
    my_api_urls = {
        'Bitcoin Addresses' : '/btc-address-list/',
        'BTC Address Details' : '/btc-detail/<str:pk>/',
        'Generate Address' : '/btc-create/',

        'Ethereum Addresses': '/eth-address-list/',
        'Ethereum Address Details': '/eth-detail/<str:pk>/',
        'Generate Address': '/eth-create/',

    }
    return Response(my_api_urls)

"""
This function below will show the entire wallet addresses repository in the database.
"""
@api_view(['GET'])
def btcList(request):
    btc_addresses= Btc.objects.all()
    serializer = BtcSerializer(btc_addresses, many = True)
    return Response(serializer.data)

"""
This function will show the detailed view of a specific BTC address with the help of pk.
"""
@api_view(['GET'])
def btcDetail(request, pk):
    btc_addresses = Btc.objects.get(id=pk)
    serializer = BtcSerializer(btc_addresses, many = False)
    return Response(serializer.data)



@api_view(['POST'])
def btcCreate(request):
    print(request.data)
    message="Your Bitcoin address has been generated."
# The code to generate btc address and private key using bitcoin library
    my_private_key = random_key()
    public_key = privtopub(my_private_key)
    address = pubtoaddr(public_key)

    new_record = Btc.objects.create(private_key=my_private_key, public_key=public_key, address=address)
    new_record.save()

    return Response(message)


@api_view(['GET'])
def ethList(request):
    eth_addresses= Eth.objects.all()
    serializer = EthSerializer(eth_addresses, many = True)
    return Response(serializer.data)

"""
This function will show the detailed view of a specific ETH address with the help of pk.
"""
@api_view(['GET'])
def ethDetail(request, pk):
    eth_addresses = Eth.objects.get(id=pk)
    serializer = EthSerializer(eth_addresses, many = False)
    return Response(serializer.data)



@api_view(['POST'])
def ethCreate(request):

    print(request.data)
    message="Your Ethereum address has been generated."
# The code to generate btc address and private key using Web3 library
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    new_record1 = Eth.objects.create(private_key=private_key, public_key=acct.address, address=acct.address)
    new_record1.save()

    return Response(message)