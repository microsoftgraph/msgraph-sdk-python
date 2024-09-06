# Microsoft Graph SDK for Python

[![PyPI version](https://badge.fury.io/py/msgraph-sdk.svg)](https://badge.fury.io/py/msgraph-sdk)
[![Downloads](https://pepy.tech/badge/msgraph-sdk)](https://pepy.tech/project/msgraph-sdk)
[![Supported Versions](https://img.shields.io/pypi/pyversions/msgraph-sdk.svg)](https://pypi.org/project/msgraph-sdk)
[![Contributors](https://img.shields.io/github/contributors/microsoftgraph/msgraph-sdk-python.svg)](https://github.com/microsoftgraph/msgraph-sdk-python/graphs/contributors)

Get started with the Microsoft Graph SDK for Python by integrating the [Microsoft Graph API](https://docs.microsoft.com/graph/overview) into your Python application.

> **Note:**
>
> * This SDK allows you to build applications using the [v1.0](https://docs.microsoft.com/graph/use-the-api#version) of Microsoft Graph. If you want to try the latest Microsoft Graph APIs, try the [beta](https://github.com/microsoftgraph/msgraph-beta-sdk-python) SDK.  

## 1. Installation

```py
pip install msgraph-sdk
```

> **Note:**
>
> * The Microsoft Graph SDK for Python is a fairly large package. It may take a few minutes for the initial installation to complete.
> * Enable long paths in your environment if you receive a `Could not install packages due to an OSError`. For details, see [Enable Long Paths in Windows 10, Version 1607, and Later](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=powershell#enable-long-paths-in-windows-10-version-1607-and-later).

## 2. Getting started with Microsoft Graph

### 2.1 Register your application

Register your application by following the steps at [Register your app with the Microsoft Identity Platform](https://docs.microsoft.com/graph/auth-register-app-v2).

### 2.2 Select and create an authentication provider

To start writing code and making requests to the Microsoft Graph service, you need to set up an authentication provider. This object will authenticate your requests to Microsoft Graph. For authentication, the Microsoft Graph Python SDK supports both sync and async credential classes from Azure Identity. Which library to choose depends on the type of application you are building.

> **Note**: For authentication we support both `sync` and `async` credential classes from `azure.identity`. Please see the azure identity [docs](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity?view=azure-python) for more information.

The easiest way to filter this decision is by looking at the permissions set you'd use. Microsoft Graph supports 2 different types of permissions: delegated and application permissions:

* Application permissions are used when you don’t need a user to login to your app, but the app will perform tasks on its own and run in the background.
* Delegated permissions, also called scopes, are used when your app requires a user to login and interact with data related to this user in a session.

The following table lists common libraries by permissions set.
| MSAL library | Permissions set | Common use case |
|---|---|---|
| [ClientSecretCredential](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.aio.clientsecretcredential?view=azure-python&preserve-view=true) | Application permissions | Daemon apps or applications running in the background without a signed-in user. |
| [DeviceCodeCredential](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.devicecodecredential?view=azure-python) | Delegated permissions | Enviroments where authentication is triggered in one machine and completed in another e.g in a cloud server. |
| [InteractiveBrowserCredentials](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.interactivebrowsercredential?view=azure-python) | Delegated permissions | Environments where a browser is available and the user wants to key in their username/password. |
| [AuthorizationCodeCredentials](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.authorizationcodecredential?view=azure-python) | Delegated permissions | Usually for custom customer applications where the frontend calls the backend and waits for the authorization code at a particular url. |

You can also use [EnvironmentCredential](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.environmentcredential?view=azure-python), [DefaultAzureCredential](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.defaultazurecredential?view=azure-python), [OnBehalfOfCredential](https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.onbehalfofcredential?view=azure-python), or any other [Azure Identity library](https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python#credential-classes).

Once you've picked an authentication library, we can initiate the authentication provider in your app. The following example uses ClientSecretCredential with application permissions.

```python
import asyncio

from azure.identity.aio import ClientSecretCredential

credential = ClientSecretCredential("tenantID",
                                    "clientID",
                                    "clientSecret")
scopes = ['https://graph.microsoft.com/.default']
```

The following example uses DeviceCodeCredentials with delegated permissions.

```python
import asyncio

from azure.identity import DeviceCodeCredential

credential = DeviceCodeCredential("client_id",
                                  "tenant_id")
scopes = ['https://graph.microsoft.com/.default']
```

### 2.3 Initialize a GraphServiceClient object

You must create **GraphServiceClient** object to make requests against the service. To create a new instance of this class, you need to provide credentials and scopes, which can authenticate requests to Microsoft Graph.

```py
# Example using async credentials and application access.
from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient

credentials = ClientSecretCredential(
    'TENANT_ID',
    'CLIENT_ID',
    'CLIENT_SECRET',
)
scopes = ['https://graph.microsoft.com/.default']
client = GraphServiceClient(credentials=credentials, scopes=scopes)
```

The above example uses default scopes for [app-only access](https://learn.microsoft.com/en-us/graph/permissions-overview?tabs=http#application-permissions).  If using [delegated access](https://learn.microsoft.com/en-us/graph/permissions-overview#delegated-permissions) you can provide custom scopes:

```py
# Example using sync credentials and delegated access.
from azure.identity import DeviceCodeCredential
from msgraph import GraphServiceClient

credentials = DeviceCodeCredential(
    'CLIENT_ID',
    'TENANT_ID',
)
scopes = ['https://graph.microsoft.com/.default']
client = GraphServiceClient(credentials=credentials, scopes=scopes)
```

> **Note**: Refer to the [following documentation page](https://learn.microsoft.com/graph/sdks/customize-client?tabs=python#configuring-the-http-proxy-for-the-client) if you need to configure an HTTP proxy.

## 3. Make requests against the service

After you have a **GraphServiceClient** that is authenticated, you can begin making calls against the service. The requests against the service look like our [REST API](https://docs.microsoft.com/graph/api/overview?view=graph-rest-1.0).

> **Note**: This SDK offers an asynchronous API by default. Async is a concurrency model that is far more efficient than multi-threading, and can provide significant performance benefits and enable the use of long-lived network connections such as WebSockets. We support popular python async environments such as `asyncio`, `anyio` or `trio`.

The following is a complete example that shows how to fetch a user from Microsoft Graph.

```py
import asyncio
from azure.identity.aio import ClientSecretCredential
from msgraph import GraphServiceClient

credential = ClientSecretCredential(
    'tenant_id',
    'client_id',
    'client_secret'
)
scopes = ['https://graph.microsoft.com/.default']
client = GraphServiceClient(credentials=credential, scopes=scopes)

# GET /users/{id | userPrincipalName}
async def get_user():
    user = await client.users.by_user_id('userPrincipalName').get()
    if user:
        print(user.display_name)
asyncio.run(get_user())
```

Note that to calling `me` requires a signed-in user and therefore delegated permissions. See [Authenticating Users](https://learn.microsoft.com/en-us/python/api/overview/azure/identity-readme?view=azure-python#authenticate-users) for more:

```py
import asyncio
from azure.identity import InteractiveBrowserCredential
from msgraph import GraphServiceClient

credential = InteractiveBrowserCredential(
    client_id=os.getenv('client_id'),
    tenant_id=os.getenv('tenant_id'),
)
scopes = ["User.Read"]
client = GraphServiceClient(credentials=credential, scopes=scopes,)

# GET /me
async def me():
    me = await client.me.get()
    if me:
        print(me.display_name)
asyncio.run(me())
```

### 3.1 Error Handling

Failed requests raise `APIError` exceptions. You can handle these exceptions using `try` `catch` statements.

```py
from kiota_abstractions.api_error import APIError
async def get_user():
    try:
        user = await client.users.by_user_id('userID').get()
        print(user.user_principal_name, user.display_name, user.id)
    except APIError as e:
        print(f'Error: {e.error.message}')
asyncio.run(get_user())
```

### 3.2 Pagination

By default a maximum of 100 rows are returned but in the response if odata_next_link is present, it can be used to fetch the next batch of max 100 rows. Here's an example to fetch the initial rows of members in a group, then iterate over the pages of rows using the odata_next_link

```py
        # get group members
        members = await client.groups.by_group_id(id).members.get()
        if members:
            print(f"########## Members:")
            for i in range(len(members.value)):
                print(f"display_name: {members.value[i].display_name}, mail: {members.value[i].mail}, id: {members.value[i].id}")

        # iterate over result batches > 100 rows
        while members is not None and members.odata_next_link is not None:
            members = await client.groups.by_group_id(id).members.with_url(members.odata_next_link).get()
            if members:
                print(f"########## Members:")
                for i in range(len(members.value)):
                    print(f"display_name: {members.value[i].display_name}, mail: {members.value[i].mail}, id: {members.value[i].id}")
```

## Documentation and resources

* [Overview](https://docs.microsoft.com/graph/overview)

* [Microsoft Graph website](https://aka.ms/graph)

* [Samples](docs)

## Upgrading

For detailed information on breaking changes, bug fixes and new functionality introduced during major upgrades, check out our [Upgrade Guide](UPGRADING.md)

## Issues

View or log issues on the [Issues](https://github.com/microsoftgraph/msgraph-sdk-python/issues) tab in the repo.

## Contribute

Please read our [Contributing](CONTRIBUTING.md) guidelines carefully for advice on how to contribute to this repo.

## Copyright and license

Copyright (c) Microsoft Corporation. All Rights Reserved. Licensed under the MIT [license](LICENSE).

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Third Party Notices

[Third-party notices](THIRD%20PARTY%20NOTICES)
