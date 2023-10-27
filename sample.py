
from azure.identity import AuthorizationCodeCredential
from msgraph import GraphServiceClient
from msgraph.generated.users.users_request_builder import UsersRequestBuilder
from msgraph.generated.models
from msgraph.generated.applications.item.remove_key.remove_key_post_request_body import RemoveKeyPostRequestBody

credentials = AuthorizationCodeCredential(
    'tenant_id',
    'client_id',
    'authorization_code',
    'redirect_uri'
)
scopes = []
graph_client = GraphServiceClient(credentials=credentials, scopes=scopes)

async def  aad_advanced_queries_get_users_accountenabled_python_V1():


    # THE PYTHON SDK IS IN PREVIEW. FOR NON-PRODUCTION USE ONLY



    query_params = UsersRequestBuilder.UsersRequestBuilderGetQueryParameters(
    filter = "accountEnabled eq false",
    )

    request_configuration = UsersRequestBuilder.UsersRequestBuilderGetRequestConfiguration(
    query_parameters = query_params,
    )
    
    graph_client.external.connections.by_external_connection_id('').schema.patch()

    result = await graph_client.users.get(request_configuration = request_configuration)
