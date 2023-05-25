# Create the API Client

```py
import asyncio

from azure.identity import EnvironmentCredential
from kiota_abstractions.api_error import APIError
from msgraph import GraphServiceClient

# Set the event loop policy for Windows
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Create a credential object. Used to authenticate requests
credential=EnvironmentCredential()
scopes = ['https://graph.microsoft.com/.default']

# Create an API client with the credentials and scopes
client = GraphServiceClient(credentials, scopes=scopes)
```

## 1. LIST ALL APPLICATIONS IN THE TENANT (GET /applications)

```py
async def get_applications():
    try:
        apps = await client.applications.get()
        if apps and apps.value:
            for app in apps.value:
                print(app.id)
    except APIError as e:
        print(e.error.message)
asyncio.run(get_applications())
```