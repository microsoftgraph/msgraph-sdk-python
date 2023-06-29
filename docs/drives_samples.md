# Create the API Client

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

## 1. LIST ALL DRIVES (GET /drives)

```py
async def get_drives():
    drives = await client.drives.get()
    if drives and drives.value:
        for drive in drives.value:
            print(drive.id, drive.drive_type, drive.name, drive.description, drive.web_url)
asyncio.run(get_drives())
```

## 2. GET DRIVE BY ID (GET /drives/{id})

```py
async def get_drive():
    drive = await client.drives.by_drive_id('DRIVE_ID').get()
    if drive:
        print(drive.id, drive.drive_type, drive.name, drive.description, drive.web_url)
asyncio.run(get_drive())
```

## 3. LIST ALL THE ITEMS IN A DRIVE (GET /drives/{id}/items)

```py
async def get_drive_items():
    items = await client.drives.by_drive_id('DRIVE_ID').items.get()
    if items and items.value:
        for item in items.value:
            print(item.id, item.name, item.size, item.folder, item.file)
asyncio.run(get_drive_items())
```

##  4. GET AN ITEM IN THE DRIVE (GET /drives/{id}/items/{id})

```py
async def get_drive_item():
    item = await client.drives.by_drive_id('DRIVE_ID').items.by_drive_item_id('ITEM_ID').get()
    if item:
        print(item.id, item.name, item.size, item.folder, item.file)
asyncio.run(get_drive_item())
```

## 5. GET THE ROOT FOLDER OF THE DRIVE (GET /drives/{id}/root)

```py
async def get_drive_root():
    root = await client.drives.by_drive_id('DRIVE_ID').root.get()
    if root:
        print(root.id, root.name, root.folder.child_count, root.root, root.size)
asyncio.run(get_drive_root())
```

## 6. GET ITEMS IN THE ROOT FOLDER OF THE DRIVE (GET drives/{id}/items/root/children)

```py
async def get_drive():
    items = await client.drives.by_drive_id('DRIVE_ID').items.by_drive_item_id('root').children.get()
    if items and items.value:
        for item in items.value:
            print(item.id, item.name, item.size, item.folder, item.file)
asyncio.run(get_drive())
```