import ip2whois

# Configures IP2WHOIS API key
ip2whois_init = ip2whois.Api('YOUR_API_KEY')

# Lookup domain information
parameter = {'domain': 'example.com'}
results = ip2whois_init.lookup(parameter)
print(results)

# Convert normal text to punycode
parameter = {'domain': 'xn--tst-qla.de'}
result = ip2whois_init.getPunycode(parameter)
print(result)

# Convert punycode to normal text
parameter = {'domain': 'täst.de'}
result = ip2whois_init.getNormalText(parameter)
print(result)