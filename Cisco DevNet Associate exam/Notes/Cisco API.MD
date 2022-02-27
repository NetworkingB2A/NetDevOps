### What is an SDK?
SDK is a software development kit that allows a user to grab pre-written APIs and communicate and an endpoint. Alternatively in the case of Python, you could create your own class that can call an API and program it the exact way you want it. or you can use an SDK and cut down on coding time and maintenance.  
A good SDK has these qualities
- Is easy to use
- Is well documented
- Has vault-added functionality
- Integrates will with other SDKs
- Has minimal impact on hardware resources
SDKs provide the following advantages
- Quicker integration
- Faster and more efficient development
- Brand control
- Increased security
- Metrics

### Cisco Meraki
Cisco Meraki cloud platform provides several APIs
- Captive Portal API
- Scanning API
- MV Sense Camera API
- Dashboard API
Cisco Meraki dashboard only allows 5 API calls per second per organization, in the first second there is a burst of additional 5 API calls that can be made.  
If you notice your API calls are giving back too much info your may want to take a pagination approach and limit your calls. some options for pagination in Meraki include:
- perPage: The number of entries to be returned.
- startingAfter: A value used to indicate that the returned data will start immediately after this value
- endingBefore: A value used to indicate that the returned data will end immediately before this value.  
If you have large configuration changes that need to happen you can use action batches in order to send multiple configurations request in a single transaction. this will avoid hitting the API limits.  


