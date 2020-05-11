from django.shortcuts import render
from django.http import HttpResponse


# List all accounts(GET)
def get_accounts(request):
    return HttpResponse("Accounts list")


# Allow to create new account(POST)
def post_accounts(request):
    return HttpResponse("Account creation")
