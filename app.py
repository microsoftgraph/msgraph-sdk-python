import asyncio
import time
from azure.identity.aio import EnvironmentCredential
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph.graph_request_adapter import GraphRequestAdapter
from msgraph.graph_service_client import GraphServiceClient

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

credential = EnvironmentCredential()
auth_provider = AzureIdentityAuthenticationProvider(credential)
request_adapter = GraphRequestAdapter(auth_provider)
client = GraphServiceClient(request_adapter)
# users = asyncio.run(client.users().get())
# for user in users.value:
#     print(user.id, user.user_principal_name)


try:
    print(time.time())
    user = asyncio.run(client.users_by_id('MeganB@M365x64588001.OnMicrosoft.com').get())
    print(time.time())
    print(user.user_principal_name, user.display_name, user.id)
    
except Exception as e:
    print(f'Error: {vars(e)} and {vars(e.error)}')
    

# msgs = asyncio.run(client.users_by_id('MeganB@M365x64588001.OnMicrosoft.com').messages().get())
# print(msgs.value)

