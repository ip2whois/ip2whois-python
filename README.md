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
```python
import ip2whois

# Configures IP2WHOIS API key
ip2whois_init = ip2whois.Api('YOUR_API_KEY')

# Lookup domain information
results = ip2whois_init.lookup('example.com')
print(results)
```

### Convert Normal Text to Punycode
```python
import ip2whois

# Configures IP2WHOIS API key
ip2whois_init = ip2whois.Api('YOUR_API_KEY')

# Convert normal text to punycode
result = ip2whois_init.getPunycode('täst.de')
print(result)
```

### Convert Punycode to Normal Text
```python
import ip2whois

# Configures IP2WHOIS API key
ip2whois_init = ip2whois.Api('YOUR_API_KEY')

# Convert punycode to normal text
result = ip2whois_init.getNormalText('xn--tst-qla.de')
print(result)
```


Response Parameter
============
### Lookup function
| Parameter | Type | Description |
|---|---|---|
|domain|string|Domain name.|
|domain_id|string|Domain name ID.|
|status|string|Domain name status.|
|create_date|string|Domain name creation date.|
|update_date|string|Domain name updated date.|
|expire_date|string|Domain name expiration date.|
|domain_age|integer|Domain name age in day(s).|
|whois_server|string|WHOIS server name.|
|registrar.iana_id|string|Registrar IANA ID.|
|registrar.name|string|Registrar name.|
|registrar.url|string|Registrar URL.|
|registrant.name|string|Registrant name.|
|registrant.organization|string|Registrant organization.|
|registrant.street_address|string|Registrant street address.|
|registrant.city|string|Registrant city.|
|registrant.region|string|Registrant region.|
|registrant.zip_code|string|Registrant ZIP Code.|
|registrant.country|string|Registrant country.|
|registrant.phone|string|Registrant phone number.|
|registrant.fax|string|Registrant fax number.|
|registrant.email|string|Registrant email address.|
|admin.name|string|Admin name.|
|admin.organization|string|Admin organization.|
|admin.street_address|string|Admin street address.|
|admin.city|string|Admin city.|
|admin.region|string|Admin region.|
|admin.zip_code|string|Admin ZIP Code.|
|admin.country|string|Admin country.|
|admin.phone|string|Admin phone number.|
|admin.fax|string|Admin fax number.|
|admin.email|string|Admin email address.|
|tech.name|string|Tech name.|
|tech.organization|string|Tech organization.|
|tech.street_address|string|Tech street address.|
|tech.city|string|Tech city.|
|tech.region|string|Tech region.|
|tech.zip_code|string|Tech ZIP Code.|
|tech.country|string|Tech country.|
|tech.phone|string|Tech phone number.|
|tech.fax|string|Tech fax number.|
|tech.email|string|Tech email address.|
|billing.name|string|Billing name.|
|billing.organization|string|Billing organization.|
|billing.street_address|string|Billing street address.|
|billing.city|string|Billing city.|
|billing.region|string|Billing region.|
|billing.zip_code|string|Billing ZIP Code.|
|billing.country|string|Billing country.|
|billing.phone|string|Billing phone number.|
|billing.fax|string|Billing fax number.|
|billing.email|string|Billing email address.|
|name_servers|array|Name servers|

```
{
    "domain": "greendot.com",
    "domain_id": "600750_DOMAIN_COM-VRSN",
    "status": "registered",
    "create_date": "1997-11-03T00:00:00Z",
    "update_date": "2019-10-29T01:25:57Z",
    "expire_date": "2021-11-02T05:00:00Z",
    "domain_age": 9027,
    "whois_server": "whois.corporatedomains.com",
    "registrar": {
        "iana_id": "299",
        "name": "CSC CORPORATE DOMAINS, INC.",
        "url": "www.cscprotectsbrands.com"
    },
    "registrant": {
        "name": "Admin Role",
        "organization": "Green Dot Corporation",
        "street_address": "",
        "city": "Pasadena",
        "region": "CA",
        "zip_code": "91107",
        "country": "US",
        "phone": "+1.8664120548",
        "fax": "+1.8664120548",
        "email": "adminrole@greendotcorp.com"
    },
    "admin": {
        "name": "Admin Role",
        "organization": "Green Dot Corporation",
        "street_address": "",
        "city": "Pasadena",
        "region": "CA",
        "zip_code": "91107",
        "country": "US",
        "phone": "+1.8664120548",
        "fax": "+1.8664120548",
        "email": "adminrole@greendotcorp.com"
    },
    "tech": {
        "name": "Admin Role",
        "organization": "Green Dot Corporation",
        "street_address": "",
        "city": "Pasadena",
        "region": "CA",
        "zip_code": "91107",
        "country": "US",
        "phone": "+1.8664120548",
        "fax": "+1.8664120548",
        "email": "adminrole@greendotcorp.com"
    },
    "billing": {
        "name": "",
        "organization": "",
        "street_address": "",
        "city": "",
        "region": "",
        "zip_code": "",
        "country": "",
        "phone": "",
        "fax": "",
        "email": ""
    },
    "nameservers": "ns1.greendotdns.com, ns2.greendotdns.com"
}
```


# LICENCE
See the LICENSE file.
