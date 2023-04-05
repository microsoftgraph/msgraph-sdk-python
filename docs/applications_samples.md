```py
import asyncio

from azure.identity import EnvironmentCredential
from kiota_abstractions.api_error import APIError
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph import GraphRequestAdapter
from msgraph import GraphServiceClient

# Set the event loop policy for Windows
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Create authentication provider object. Used to authenticate request
credential=EnvironmentCredential()
auth_provider = AzureIdentityAuthenticationProvider(credential)

# Initialize a request adapter. Handles the HTTP concerns.
request_adapter = GraphRequestAdapter(auth_provider)

# Get a service client.
client = GraphServiceClient(request_adapter)

# GET ALL APPLICATIONS IN THE TENANT (GET /applications)
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