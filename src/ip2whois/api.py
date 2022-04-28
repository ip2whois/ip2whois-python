import json
import sys

# Compability support for Python 2.7
if sys.version < '3':
    import urllib, httplib
    def urlencode(x):
        return urllib.urlencode(x)
    def httprequest(x, usessl):
        try:
            if (usessl is True):
                conn = httplib.HTTPSConnection("api.ip2whois.com")
            else:
                conn = httplib.HTTPConnection("api.ip2whois.com")
            conn.request("GET", "/v2?" + x)
            res = conn.getresponse()
            return json.loads(res.read())
        except:
            return None
else:
    import urllib.parse, http.client
    def urlencode(x):
        return urllib.parse.urlencode(x)
    def httprequest(x, usessl):
        try:
            if (usessl is True):
                conn = http.client.HTTPSConnection("api.ip2whois.com")
            else:
                conn = http.client.HTTPConnection("api.ip2whois.com")
            conn.request("GET", "/v2?" + x)
            res = conn.getresponse()
            return json.loads(res.read())
        except:
            return None

class Api:
    def __init__(self, apikey, usessl=True):
        self.apikey = apikey
        self.usessl = usessl
    
    def lookup(self, domain = ''):

         try:
             parameters = urlencode((("key", self.apikey), ("format", 'json'), ("domain", domain if domain else '')))
             response = httprequest(parameters, self.usessl)
             return response
         except:
             return None
    
    def getPunycode(self, domain = ''):
        domain = domain if domain else ''
        if sys.version < '3':
            converted_result = domain.encode('idna').decode('ascii')
            return converted_result.encode('utf-8')
        else:
            return domain.encode('idna').decode('ascii')
    
    def getNormalText(self, domain = ''):
         if sys.version < '3':
            converted_result = unicode(domain if domain else '').encode('ascii').decode('idna')
            return converted_result.encode('utf-8')
         else:
            return domain.encode('ascii').decode('idna')