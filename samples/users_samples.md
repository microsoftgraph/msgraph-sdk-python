## Create the API Client

```py
import asyncio

from azure.identity import ClientSecretCredential
from kiota_abstractions.api_error import APIError
from msgraph import GraphServiceClient

# Set the event loop policy for Windows
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) 

# Create a credential object. Used to authenticate requests
credential = ClientSecretCredential(
    tenant_id='TENANT_ID',
    client_id='CLIENT_ID',
    client_secret='CLIENT_SECRET'
)
scopes = ['https://graph.microsoft.com/.default']

# Create an API client with the credentials and scopes.
client = GraphServiceClient(credential, scopes=scopes)
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
        user = await client.users.by_user_id('USER_ID').get()
        if user:
            print(user.user_principal_name, user.display_name, user.id)
    except APIError as e:
        print(f'Error: {e.error.message}')
asyncio.run(get_user())

# LIST ALL TRANSITIVE MEMBERSHIPS OF A USER (GET /users/{id}/transitiveMemberOf)

async def get_memberships():
    try:
        memberships = await client.users.by_user_id('USER_ID').transitive_member_of.get()
        if memberships and memberships.value:
            for membership in memberships.value:
                obj = await client.directory_objects.by_directory_object_id(membership.id).get()
                if obj and obj.odata_type == '#microsoft.graph.group':
                    group = await client.groups.by_group_id(obj.id).get()
                    if group:
                        print(group.id, group.group_types, group.display_name, group.mail)
    except Exception as e:
        print(e)
asyncio.run(get_memberships())