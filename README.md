# IP2WHOIS Python SDK

This Python module enables user to easily implement the checking of WHOIS information for a particular domain into their solution using the API from [https://www.ip2whois.com](https://www.ip2whois.com/). It is a WHOIS lookup api that helps users to obtain domain information, WHOIS record, by using a domain name. The WHOIS API returns a comprehensive WHOIS data such as creation date, updated date, expiration date, domain age, the contact information of the registrant, mailing address, phone number, email address, nameservers the domain is using and much more. IP2WHOIS supports the query for [1113 TLDs and 634 ccTLDs](https://www.ip2whois.com/tld-cctld-supported).

This module requires API key to function. You may sign up for a free API key at https://www.ip2whois.com/register.

# Installation

To install this module type the following:

```bash
pip install IP2WHOIS
```

# Usage Example

### Lookup Domain Information

#### Object Properties

| Property Name | Property Type | Description  |
| ------------- | ------------- | ------------ |
| domain        | string        | Domain name. |

```python
import ip2whois

# Configures IP2WHOIS API key
ip2whois_init = ip2whois.Api('YOUR_API_KEY')

# Lookup domain information
parameter = {'domain': 'example.com'}
results = ip2whois_init.lookup(parameter)
print(results)
```

### Convert Normal Text to Punycode

#### Object Properties

| Property Name | Property Type | Description  |
| ------------- | ------------- | ------------ |
| domain        | string        | Domain name. |

```python
import ip2whois

# Configures IP2WHOIS API key
ip2whois_init = ip2whois.Api('YOUR_API_KEY')


# Convert normal text to punycode
parameter = {'domain': 'xn--tst-qla.de'}
result = ip2whois_init.getPunycode(parameter)
print(result)
```

### Convert Punycode to Normal Text

#### Object Properties

| Property Name | Property Type | Description  |
| ------------- | ------------- | ------------ |
| domain        | string        | Domain name. |

```python
import ip2whois

# Configures IP2WHOIS API key
ip2whois_init = ip2whois.Api('YOUR_API_KEY')


# Convert punycode to normal text
parameter = {'domain': 'täst.de'}
result = ip2whois_init.getNormalText(parameter)
print(result)
```

# LICENCE

See the LICENSE file.