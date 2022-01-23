# Application Programming Interfaces (API)

- Northbound APIs
  - Often a network controller to its management software.
  - Best practices suggest that the traffic should be encrypted using TLS between software and the controller.
- Southbound APIs
  - This would be pushing the configuration to the device from the controller. 

As network engineers we have been using this model of north and southbound aps for years and years. Think of wireless access points and the wireless controller.

## Synchronous vs Asynchronous APIs
Synchronous APIs means that your application is waiting for a response from the API in order to continue the process. You send a command, wait for a response, then send the next command. This works very much like TCP. Synchronous also means slower response times. You man need this type of API communication if you need data from another API before your program can continue. good example would be creating tokens.  
Asynchronous is just the opposite. You send a command, then you send another and another. You never need to wait to find out if the first command was successful. 

# Representational State Transfer (REST) APIs
- REST APIs are often referred to as RESTful API
- RESTful APIs use HTTP methods to gather and manipulate data.



| CRUD Function | Action |
|-|-|
| CREATE | Inserts data inside a database or an application |
| READ | Retrieves data from a database or an application |
| UPDATE | Modifies replaces data in a database or an application |
| Delete | Removes data from a database or an application | 

## RESTful API Fundamentals
### API Types
- Service API
  - An application can call on another application to solve a particular problem.
  - These different applications can work with out interaction from the other app, but this will extend the service for the two apps.
- Information API
  - An application can call on another application to provide information.
- Hardware API
  - An application can call the hardwares API to access the hardware level.

### API Access Types
- Private
  - For internal use only. Used inside a company only.
- Partner
  - APIs that are shared to specific business partners.
- Public
  - API that can be accessed by all.

## RESTful API Authentication

- Basic
  - One of the simplest and most common authentication methods used in APIs.
  - *IMPORTANT NOTE* Basic Auth is sent not encrypted in your program or to the southbound device. You often will use SSL or TLS to encrypt your HTTP call to prevent man in the middle attacks.
  -  Another issue is that the encoded string is sent back and forth in your APIs calls.
- API Keys
  - An API key is a predetermined string that is passed from the client to the server. It is intended to be a pre-shared secret and should not be well known or easy to guess.
  - API keys can be passed to the server in three different ways:
    - String
    - Request header
    - Cookie
  - The string is passed with every call you make.
  - If you are making multiple calls you would want to look into using a cookie or request header.
- Custom Tokens
  - Tokens are a way of authenticating using the REST API. You authenticate once and you receive your token, you use the token to authenticate. 

# HTTP
## HTTP Basics
In order for a HTTP request to be successful, the client need to include four items
- URL (uniform resource locator) 
  - The URL is the location where the service resides on the internet/intranet
  - A URL typically has four components
    - Protocol
      - HTTP
    - Server/Host address
      - first part of the URL the DNS name or ip address
    - Resource
      - Location on the server where the data is stored
    - Parameters
      - a filter or to clarify request
- Method
  - Different kinds of request methods includes  

| Method | Details | CRUD |
|-|-|-| 
| GET | Retrieve data from the server | Read |
| HEAD | Request for header information from a get request |
| POST | Post data or add new data server | Create |
| PUT | Request to ask server to store or update data | Update |
| PATCH | Request server to partially store or update data | Update |
| DELETE | Request server to delete information | Delete |
| TRACE | Request to ask server to return a diagnostic trace |
| OPTIONS | Ask the server for a list of request methods |
| CONNECT | Ask a proxy to make a request to another server |
 
- List of headers
  - The headers contain the meta data about tn HTTP request. 
    - The host name, connection type, The type of data you want to receive, the language, ect
- Body


### HTTP functions calls
| HTTP Function | Action |
|-|-|
| GET | Request data from a destination |
| POST | Submits data to a specific destination |
| PUT | Replaces data at a specific destination |
| Patch | Appends data to a specific destination |
| Delete | Removes data from a specific destination |

### Response codes
The types of response codes you will see
- 1xx (informational) - The request has been successfully received. The server is continuing the process
- 2xx (success) - The request was successful and is completed.
- 3xx (redirection) - Further action must be taken to complete this request.
- 4xx (client error) - The request cannot be understood or is unauthorized.
- 5xx (server error) - The server failed to fulfill a request.

Common response codes
| Status Code | Meaning |
|-|-|
| 100 | Continue |
| 200 | Okay | 
| 301 | Move permanently |
| 302 | Found and redirect |
| 304 | Not modified | 
| 400 | Bad request |
| 401 | Authentication required |
| 403 | Forbidden | 
| 404 | Not found | 
| 405 | Method not allowed |
| 408 | Request timed out | 
| 414 | request URI too large |
| 500 | Internal server error |
| 501 | Method not implemented |
| 502 | Bad gateway | 
| 503 | Service unavailable |
| 504 | Gateway timeout | 

### Webhooks
Webhooks are user-defined HTTP callbacks. Also called reverse APIs. When you want an event to happen based on a trigger that occurs.  
ngrok is a free tool that you can use to test out your webhooks.


## Simple Object Access Protocol (SOAP)
- SOAP is used to access web services.
- SOAP can use SMTP or HTTP as a transport protocol. SOAP is used to to exchange data between applications that were build on different programming languages.
- Using HTTP means that you wont need to open extra firewall ports.
- SOAP is based on XML.
- SOAP messages typically consist of four main components
  - Envelope
    - The envelope encloses the XML data and identifies it as a SOAP message.
  - Header
  - Body
  - Fault (optional)
    - SOAP Fault Options
      - faultCode : Not optional - Specifies the fault code of an error. Below are the fault codes.
        - VersionMismatch
        - MustUnderstand
        - DataEncodingUnknown
        - Sender
        - Receiver
      - faultString : Not optional - Describes an error
      - faultActor : Optional - Specifies who caused a fault
      - detail : Optional - Applies specific error messages

## Remote-Procedure Calls (RPCs)
RPC is used to execute code or a program on a remote node in a network.



