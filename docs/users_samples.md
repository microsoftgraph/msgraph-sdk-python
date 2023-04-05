## Create the API Client

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
```

## 1. GET ALL USERS IN A TENANT (GET /users)

```py
async def get_users():
    try:
        users = await client.users.get()
        if users and users.value:
            for user in users.value:
                print(user.id, user.display_name, user.mail)
    except APIError as e:
        print(e.error.message)
asyncio.run(get_users())
```

## 2. GET A SPECIFIC USER (GET /users/{id | userPrincipalName})

```py
async def get_user():
    try:
        user = await client.users_by_id('USER_ID').get()
        if user:
            print(user.user_principal_name, user.display_name, user.id)
    except APIError as e:
        print(f'Error: {e.error.message}')
asyncio.run(get_user())

# LIST ALL TRANSITIVE MEMBERSHIPS OF A USER (GET /users/{id}/transitiveMemberOf)

async def get_memberships():
    try:
        memberships = await client.users_by_id('USER_ID').transitive_member_of.get()
        if memberships and memberships.value:
            for membership in memberships.value:
                obj = await client.directory_objects_by_id(membership.id).get()
                if obj and obj.odata_type == '#microsoft.graph.group':
                    group = await client.groups_by_id(obj.id).get()
                    if group:
                        print(group.id, group.group_types, group.display_name, group.mail)
    except Exception as e:
        print(e)
asyncio.run(get_memberships())