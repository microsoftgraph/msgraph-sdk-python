## Create the API Client

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
```

## 1. GET ALL USERS IN A TENANT (GET /users)

```py
async def get_users():
    users = await client.users.get()
    if users and users.value:
        for user in users.value:
            print(user.id, user.display_name, user.mail)
asyncio.run(get_users())
```

## 2. GET A SPECIFIC USER (GET /users/{id | userPrincipalName})

```py
async def get_user():
    user = await client.users.by_user_id('USER_ID').get()
    if user:
        print(user.user_principal_name, user.display_name, user.id)
asyncio.run(get_user())

# LIST ALL TRANSITIVE MEMBERSHIPS OF A USER (GET /users/{id}/transitiveMemberOf)

async def get_memberships():
    memberships = await client.users.by_user_id('USER_ID').transitive_member_of.get()
    if memberships and memberships.value:
        for membership in memberships.value:
            obj = await client.directory_objects.by_directory_object_id(membership.id).get()
            if obj and obj.odata_type == '#microsoft.graph.group':
                group = await client.groups.by_group_id(obj.id).get()
                if group:
                    print(group.id, group.group_types, group.display_name, group.mail)
asyncio.run(get_memberships())
```

## 3. SEARCH USER BY NAME (GET /users/$search?=)

```py
import asyncio

from azure.identity import AzureCliCredential
from msgraph import GraphServiceClient
from msgraph.generated.users.users_request_builder import UsersRequestBuilder


async def find_user(user_name: str, client: GraphServiceClient) -> None:
    # The query used here is the same when searching for users in Azure AD via web console
    query_params = UsersRequestBuilder.UsersRequestBuilderGetQueryParameters(
        search=[
            f'("displayName:{user_name}" OR "mail:{user_name}" OR "userPrincipalName:{user_name}" OR "givenName:{user_name}" OR "surName:{user_name}" OR "otherMails:{user_name}")'
        ],
    )
    request_configuration = (
        UsersRequestBuilder.UsersRequestBuilderGetRequestConfiguration(
            query_parameters=query_params,
        )
    )
    request_configuration.headers.add("ConsistencyLevel", "eventual")

    response = await client.users.get(request_configuration=request_configuration)
    if response.value:
        user = response.value[0]
        print(
            f"Found user for {user_name} in the Azure AD with user principal name {user.user_principal_name} and display name {user.display_name}"
        )
    else:
        print(f"{user_name} user in the Azure AD not found")


def main():
    # Use cli credentials to authenticate against Azure
    # Before running script do `az login`
    credential = AzureCliCredential()
    scopes = ["https://graph.microsoft.com/.default"]
    client = GraphServiceClient(credentials=credential, scopes=scopes)
    asyncio.run(find_user("john", client))


main()
```
