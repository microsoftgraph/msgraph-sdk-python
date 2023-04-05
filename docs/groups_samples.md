```py
import asyncio

## Create the API Client

```py
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

## 1. LIST ALL GROUPS IN THE TENANT (GET /groups)
```py
async def get_groups():
    try:
        groups = await client.groups.get()
        if groups and groups.value:
            for group in groups.value:
                print(group.id, group.display_name)
    except APIError as e:
        print(e.error.message)
asyncio.run(get_groups())
```

## 2. GET A SPECIFIC GROUP (GET /groups/{id})

```py
async def get_group():
    try:
        group = await client.groups_by_id('GROUP_ID').get()
        if group:
            print(group.id, group.display_name, group.description, group.group_types,
                group.security_enabled)
    except APIError as e:
        print(e.error.message)
asyncio.run(get_group())
```

## 3. LIST ALL MEMBERS IN A GROUP (GET /groups/{id}/members)

```py
async def get_group_members():
    try:
        members = await client.groups_by_id('GROUP_ID').members.get()
        if members and members.value:
            for member in members.value:
                user = await client.users_by_id(member.id).get()
                if user:
                    print(user.display_name, user.mail)
    except APIError as e:
        print(e.error.message)
asyncio.run(get_group_members())
```

## 4. LIST A GROUP TEAM SHAREPOINT SITES (GET /groups/{id}/sites)

```py
async def get_group_sites():
    try:
        sites = await client.groups_by_id('GROUP_ID').sites.get()
        if sites and sites.value:
            for site in sites.value:
                print(site.id, site.web_url)
    except APIError as e:
        print(e.error.message)
asyncio.run(get_group_sites())
```

## 5. LIST A GROUP'S TRANSITIVE MEMBERS (GET /groups/{id}/transitiveMembers)

```py
async def get_group_transitive_members():
    try:
        members = await client.groups_by_id('GROUP_ID').transitive_members.get()
        if members and members.value:
            for member in members.value:
                object = await client.directory_objects_by_id(member.id).get()
                if object and object.odata_type == '#microsoft.graph.user':
                    user = await client.users_by_id(object.id).get()
                    if user:
                        print(user.id, user.display_name, user.mail)
    except Exception as e:
        print(e)
asyncio.run(get_group_transitive_members())
```

## 6. LIST ALL GROUP DRIVES (GET /groups/{id}/drives)

```py
async def get_group_drives():
    try:
        drives = await client.groups_by_id('1a735b59-61f2-4053-95b6-648637628618').drives.get()
        if drives and drives.value:
            for drive in drives.value:
                print(drive.id, drive.name)
    except Exception as e:
        print(e)
asyncio.run(get_group_drives())
```

## 7. GET A GROUP DRIVE (GET /groups/{id}/drives/{id})

```py
async def get_group_drive():
    try:
        drive = await client.groups_by_id(
            'GROUP_ID'
            ).drives_by_id(
                'DRIVE_ID'
                ).get()
        if drive:
            print(drive.id, drive.drive_type, drive.name, drive.web_url, drive.items)
    except APIError as e:
        print(e.error.message)
asyncio.run(get_group_drive())
```