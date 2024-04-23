
# DELEGATED ACCESS SAMPLES (REQUIRES SIGNED IN USER)

## 1. DEVICE CODE FLOW
```py
import asyncio

from azure.identity import DeviceCodeCredential
from msgraph import GraphServiceClient

# Create a credential object. Used to authenticate requests
credential = DeviceCodeCredential(
    client_id='CLIENT_ID',
    tenant_id='TENANT_ID',
    )

scopes = ["User.Read"]

# Create an API client with the credentials and scopes.
client = GraphServiceClient(credentials=credential, scopes=scopes)

# GET A USER USING THE USER ID (GET /users/{id})
async def get_user():
    user = await client.users_by_id('USER_ID').get()
    if user:
        print(user.user_principal_name, user.display_name, user.id)
asyncio.run(get_user())
```

## 2. INTERACTIVE BROWSER FLOW

```py
import asyncio
from azure.identity import InteractiveBrowserCredential
from msgraph import GraphServiceClient

# Create a credential object. Used to authenticate requests 
credentials = InteractiveBrowserCredential(
    client_id=os.getenv('client_id'),
    tenant_id=os.getenv('tenant_id'),
)

scopes = ["User.Read"]

# Create an API client with the credentials and scopes.
client = GraphServiceClient(credentials=credential, scopes=scopes)

# GET A USER USING THE USER ID (GET /users/{id})
async def get_user():
    user = await client.users_by_id('USER_ID').get()
    if user:
        print(user.user_principal_name, user.display_name, user.id)
asyncio.run(get_user())
```

# APPLICATION ACCESS SAMPLES (APPLICATIONS ONLY)

## 3. CLIENT SECRET CREDENTIALS FLOW

```py
import asyncio

from azure.identity import ClientSecretCredential
from msgraph import GraphServiceClient

# Create a credential object. Used to authenticate requests
credential = ClientSecretCredential(
    tenant_id='TENANT_ID',
    client_id='CLIENT_ID',
    client_secret='CLIENT_SECRET'
)
scopes = ['https://graph.microsoft.com/.default']

# Create an API client with the credentials and scopes.
client = GraphServiceClient(credentials=credential, scopes=scopes)

# GET A USER USING THE USER ID (GET /users/{id})
async def get_user():
    user = await client.users.by_user_id('USER_ID').get()
    if user:
        print(user.user_principal_name, user.display_name, user.id)
asyncio.run(get_user())
```

## 4. ENVIRONMENT CREDENTIAL FLOW (ASYNC)

```py
import asyncio

from azure.identity.aio import EnvironmentCredential
from msgraph import GraphServiceClient

# Create a credential object. Used to authenticate requests
credential = EnvironmentCredential()
scopes = ['https://graph.microsoft.com/.default']

# Create an API client with the credentials and scopes.
client = GraphServiceClient(credentials=credential, scopes=scopes)

# GET A USER USING THE USER ID (GET /users/{id})
async def get_user():
    user = await client.users.by_user_id('USER_ID').get()
    if user:
        print(user.user_principal_name, user.display_name, user.id)
asyncio.run(get_user())
