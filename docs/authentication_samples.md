
## 1. DEVICE CODE FLOW
```py
import asyncio

from azure.identity import DeviceCodeCredential
from kiota_abstractions.api_error import APIError
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph import GraphRequestAdapter, GraphServiceClient

# Set the event loop policy for Windows
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Create authentication provider object. Used to authenticate requests
credential = DeviceCodeCredential(
    client_id='CLIENT_ID',
    tenant_id='TENANT_ID',
    )

scopes = ["User.Read"]
auth_provider = AzureIdentityAuthenticationProvider(credential, scopes=scopes)

# Initialize a request adapter with the auth provider.
request_adapter = GraphRequestAdapter(auth_provider)

# Create an API client with the request adapter.
client = GraphServiceClient(request_adapter)

# GET A USER USING THE USER ID
# Request: GET /users/{id}
async def get_user():
    try:
        user = await client.users_by_id('USER_ID').get()
        if user:
            print(user.user_principal_name, user.display_name, user.id)
    except APIError as e:
        print(f'Error: {e.error.message}')

asyncio.run(get_user())
```

2. ## INTERACTIVE BROSWER FLOW

```py
import asyncio
from azure.identity import InteractiveBrowserCredential
from kiota_abstractions.api_error import APIError
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph import GraphRequestAdapter, GraphServiceClient

# Set the event loop policy for Windows
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Create authentication provider object. Used to authenticate requests
credential = InteractiveBrowserCredential()
scopes = ["User.Read"]
auth_provider = AzureIdentityAuthenticationProvider(credential, scopes=scopes)

# Initialize a request adapter with the auth provider.
request_adapter = GraphRequestAdapter(auth_provider)

# Create an API client with the request adapter.
client = GraphServiceClient(request_adapter)

# GET A USER USING THE USER ID
# Request: GET /users/{id}

async def get_user():
    try:
        user = await client.users_by_id('USER_ID').get()
        if user:
            print(user.user_principal_name, user.display_name, user.id)
    except APIError as e:
        print(f'Error: {e.error.message}')
asyncio.run(get_user())
```

## 3. CLIENT SECRET CREDENTIALS FLOW

```py
import asyncio

from azure.identity import ClientSecretCredential
from kiota_abstractions.api_error import APIError
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph import GraphRequestAdapter, GraphServiceClient

# Set the event loop policy for Windows
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) 

# Create authentication provider object. Used to authenticate request
credential = ClientSecretCredential(
    tenant_id='TENANT_ID',
    client_id='CLIENT_ID',
    client_secret='CLIENT_SECRET'
)
scopes = ['https://graph.microsoft.com/.default']
auth_provider = AzureIdentityAuthenticationProvider(credential, scopes=scopes)

# Initialize a request adapter with the auth provider.
request_adapter = GraphRequestAdapter(auth_provider)

# Create an API client with the request adapter.
client = GraphServiceClient(request_adapter)

# GET A USER USING THE USER ID
# Request: GET /users/{id}
async def get_user():
    try:
        user = await client.users_by_id('USER_ID').get()
        if user:
            print(user.user_principal_name, user.display_name, user.id)
    except APIError as e:
        print(f'Error: {e.error.message}')
asyncio.run(get_user())
```

## 4. ENVIRONMENT CREDENTIAL FLOW (ASYNC)

```py
import asyncio

from azure.identity.aio import EnvironmentCredential
from kiota_abstractions.api_error import APIError
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph import GraphRequestAdapter, GraphServiceClient

# Set the event loop policy for Windows
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Create authentication provider object. Used to authenticate request
credential = EnvironmentCredential()
scopes = ['https://graph.microsoft.com/.default']
auth_provider = AzureIdentityAuthenticationProvider(credential, scopes=scopes)

# Initialize a request adapter with the auth provider.
request_adapter = GraphRequestAdapter(auth_provider)

# Create an API client with the request adapter.
client = GraphServiceClient(request_adapter)

# GET A USER USING THE USER ID
# Request: GET /users/{id}
async def get_user():
    try:
        user = await client.users_by_id('USER_ID').get()
        if user:
            print(user.user_principal_name, user.display_name, user.id)
    except APIError as e:
        print(f'Error: {e.error.message}')

asyncio.run(get_user())
