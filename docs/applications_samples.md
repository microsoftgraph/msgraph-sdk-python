# Create the API Client

```py
import asyncio

from azure.identity import ClientSecretCredential
from msgraph import GraphServiceClient

# Create a credential object. Used to authenticate requests
credential = ClientSecretCredential(
    tenant_id='TENANT_ID',
    client_id='CLIENT_ID',
    client_secret='CLIENT_SECRET',
)
scopes = ['https://graph.microsoft.com/.default']

# Create an API client with the credentials and scopes
client = GraphServiceClient(credentials=credential, scopes=scopes)
```

## 1. LIST ALL APPLICATIONS IN THE TENANT (GET /applications)

```py
async def get_applications():
    apps = await client.applications.get()
    if apps and apps.value:
        for app in apps.value:
            print(app.id)
asyncio.run(get_applications())
```