import ip2whois

# Configures IP2WHOIS API key
ip2whois_init = ip2whois.Api('YOUR_API_KEY')

# Lookup domain information
results = ip2whois_init.lookup('example.com')
print(results)

# Convert normal text to punycode
result = ip2whois_init.getPunycode('xn--tst-qla.de')
print(result)

# Convert punycode to normal text
result = ip2whois_init.getNormalText('täst.de')
print(result)