# -*- coding: utf-8 -*-

import pytest
import json

import ip2whois

def test_lookup(global_data):
    ip2whois_init = ip2whois.Api(global_data["apikey"])
    results = ip2whois_init.lookup('example.c')
    # assert results['error_message'] == 'API key not found.'
    if (global_data["apikey"] == 'YOUR_API_KEY'):
        assert results['error']['error_message'] == 'API key not found.'
    else:
        assert results['error']['error_message'] == 'Invalid domain.'

# def test_api_key_exist(global_data, capsys):
    # if (global_data["apikey"] == 'YOUR_API_KEY'):
        # with capsys.disabled():
            # print ("You could enter a IP2WHOIS API Key in tests/conftest.py for real web service calling test.")
            # print ("You could sign up for a free API key at https://www.ip2whois.com/register if you do not have one.")
        # assert global_data["apikey"] == "YOUR_API_KEY"
    # else:
        # assert global_data["apikey"] != "YOUR_API_KEY"

def test_function_exist(global_data):
    ip2whois_init = ip2whois.Api(global_data["apikey"])
    errors = []
    functions_list = ['lookup', 'getPunycode', 'getNormalText']
    for x in range(len(functions_list)): 
        # assert hasattr(mbv, functions_list[x]) == True, "Function did not exist."
        if (hasattr(ip2whois_init, functions_list[x]) is False):
            errors.append("Function " + functions_list[x] + " did not exist.")
    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))

def test_get_puny_code(global_data):
    ip2whois_init = ip2whois.Api(global_data["apikey"])
    result = ip2whois_init.getPunycode('täst.de')
    assert result == "xn--tst-qla.de"

def test_get_normal_text(global_data):
    ip2whois_init = ip2whois.Api(global_data["apikey"])
    result = ip2whois_init.getNormalText('xn--tst-qla.de')
    assert result == "täst.de"

def test_get_domain_name(global_data):
    ip2whois_init = ip2whois.Api(global_data["apikey"])
    result = ip2whois_init.getDomainName('https://www.example.com/exe')
    assert result == "example.com"

def test_get_domain_extension(global_data):
    ip2whois_init = ip2whois.Api(global_data["apikey"])
    result = ip2whois_init.getDomainExtension('https://www.example.com/exe')
    assert result == ".com"