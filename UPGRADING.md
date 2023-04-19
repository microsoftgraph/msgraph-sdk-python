# Microsoft Graph Python SDK Upgrade Guide

This guide highlights breaking changes, and new features introduced in the new Microsoft Graph Python SDK.

# Upgrading to msgraph-sdk from msgraph-core

- [Installation](#installation)
- [New Features](#new-features)
- [Breaking Changes](#breaking-changes)

# Installation

```py
# msgraph-core
pip install msgraph-core

# msgraph-sdk
pip install msgraph-sdk
```

# New Features

## Model classes

The `msgraph-sdk` provides auto-generated model classes that correspond to objects that are accepted and returned from the Microsoft Graph API. These models leverage Python's `typing` features and have fully typed properties, methods and return types.

This package (`msgraph-sdk`) will only contain models that match the [Microsoft Graph v1 API metadata](https://graph.microsoft.com/v1.0/$metadata). If you are interested in the Beta API, please see the [Microsoft Graph Beta Python SDK](https://github.com/microsoftgraph/msgraph-sdk-beta-python).

## Fluent Request Builder Pattern
`msgraph-sdk` provides a fluent interface that takes advantage of method chaining and IDE autocomplete when making requests to Microsoft Graph. This is a shift from `msgraph-core` where raw URLs would be passed instead:

```py
# msgraph-core
resp =client.get('/users/userId/messages')

# msgraph-sdk
req = client.users.by_user_id('userId').messages.get()
resp = asyncio.run(req)
```

Hopefully this makes it more intuitive to work with the SDK and reduces time checking reference docs. Your feedback would be appreciated on your preferred experience or whether we should support both scenarios.

# Breaking changes

The following breaking changes were introduced in `msgraph-sdk`:

- [Changes to Authentication mechanism](#changes-to-authentication)
- [Changes to the Microsoft Graph client construction and configuration experience](#changes-to-graph-client-instantiation-and-configuration).
- [Changes to Microsoft Graph request functionality](#changes-to-graph-request-functionality).
- [Dependency changes](#dependency-changes).

## Changes to authentication
`msgraph-sdk` introduces an `AuthenticationProvider` that handles the fetching, caching and refreshing of tokens ensuring all your requests are always authenticated.

The AuthenticationProvider makes use of the [azure-identity](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/identity/azure-identity) library hence its name - `AzureIdentityAuthenticationProvider`. The `AzureIdentityAuthenticationProvider` class is imported from the [kiota-authentication](https://github.com/microsoft/kiota-authentication-azure-python) package and expects an async credential. See [azure.identity.aio](https://aka.ms/azsdk/python/identity/aio/docs) documentation for more details on supported credential classes.

```py

# msgraph-core
from azure.identity import ClientSecretCredential
from msgraph.core import GraphClient

credential = ClientSecretCredential(tenant_id: str, client_id: str, client_secret: str)


# msgraph-sdk
from azure.identity.aio import ClientSecretCredential # async credentials only
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider

credential=ClientSecretCredential(tenant_id: str, client_id: str, client_secret: str)
auth_provider = AzureIdentityAuthenticationProvider(credential)
```

See more [code samples](README.md#create-an-authenticationprovider-object) on how to initialise the Authentication Provider.

## Changes to Microsoft Graph client instantiation and configuration

`msgraph-sdk` introduces a new format for creating and configuring clients based on our [Kiota](https://github.com/microsoft/kiota) client generator. It involves creating an instance of a `GraphRequestAdapter` that will take care of all generic processing of HTTP requests, and passing the instance to the `GraphServiceClient` which holds strongly typed models and request builders to simplify the process of creating requests and consuming responses.

```py

# msgraph-core
from msgraph.core import GraphClient

client = GraphClient(credential=credential)


# msgraph-sdk
from msgraph import GraphRequestAdapter
from msgraph import GraphServiceClient

adapter = GraphRequestAdapter(auth_provider)
client = GraphServiceClient(request_adapter)
```
With version 2's configuration, all your requests are authenticated without additional effort.

See [this example](docs/Examples.md#creating-a-request-adapter) on how to customise the GraphRequestAdapter configuration.

## Changes to graph request mechanism

All requests are asynchronous by default in the `msgraph-sdk` and return a coroutine. In order to execute a request, you need to run them in an async environment using one of the available popular python async libraries `asyncio`, `anyio`, `trio`.

To configure the request, you need to pass a `RequestConfiguration` object to the method call.

The request method also allows you to pass your custom response handler that handles the raw Response object. By default the Response body is deserialized to the expected model type.


```py

# msgraph-core
result = client.get('/users/userId/messages',params={'$select': 'subject','$top': '5', '$skip': '1'})
for message in result.json()['value']:
    print message['subject']

# msgraph-sdk
query_params = MessagesRequestBuilder.MessagesRequestBuilderGetQueryParameters(
    select=['subject',], skip=1, top=5
)
request_config = MessagesRequestBuilder.MessagesRequestBuilderGetRequestConfiguration(
    query_parameters=query_params,
)

messages = asyncio.run(client.users.by_user_id('userId').messages.get(request_configuration=request_config))
for msg in messages.value:
    print(msg.subject)
```

See [the examples](docs/Examples.md) on how to pass headers in your requests.

## Exception handling

Any `4xx` or `5xx` responses from the Graph API will result in an `APIError` being thrown.

```py
from kiota_abstractions.api_error import APIError
try:
    users = asyncio.run(client.users().get())

except APIError as e {
    return f"Exception occurred: {e.error.message}"
}
```
## Dependency changes

- Python `3.6` is the new minimum supported Python version.
- `requests` support is deprecated in favour of `httpx`.
- `asyncio`/any other supported async envronment e.g `AnyIO`, `Trio`.
