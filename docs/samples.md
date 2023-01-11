# Usage Examples

## Creating a Graph client
This creates a default Graph client that uses `https://graph.microsoft.com` as the default base URL and default configured HTTPX client to make the requests.

```py
from azure.identity import AuthorizationCodeCredential
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph import GraphRequestAdapter
from msgraph import GraphServiceClient

AuthorizationCodeCredential(
    tenant_id: str,
    client_id: str,
    authorization_code: str,
    redirect_uri: str
)
scopes = ['User.Read', 'Mail.ReadWrite']
auth_provider = AzureIdentityAuthenticationProvider(credential, scopes=scopes)
request_adapter = GraphRequestAdapter(auth_provider)
client = GraphServiceClient(request_adapter)
```

Using a custom `httpx.AsyncClient` instance:

```py
from msgraph import GraphRequestAdapter
from msgraph_core import GraphClientFactory

http_client = GraphClientFactory.create_with_default_middleware(client=httpx.AsyncClient())
request_adapter = GraphRequestAdapter(auth_provider, http_client)
```

## Get an item from the Graph

This sample fetches the current signed-in user. Note that to use `/me` endpoint you need
a delegated permission. Alternatively, using application permissions, you can request `/users/[userPrincipalName]`. See [Microsoft Graph Permissions](https://docs.microsoft.com/en-us/graph/auth/auth-concepts#microsoft-graph-permissions) for more.


```py
async def get_user():
    try:
        user = await client.me.get()
        return user
    except Exception as e:
        print(e.error.message)

asyncio.run(get_user())
```

## Get a collection of items
This snippet retrieves the messages in a user's mailbox. Ensure you have the [correct permissions](https://docs.microsoft.com/en-us/graph/api/user-list-messages?view=graph-rest-1.0&tabs=http#permissions) set.
The Graph API response is deserialized into a collection of `Message` - a model class provided by the SDK.

```py
async def get_user_messages():
    try:
        messages = await (client.users_by_id('USER_ID').messages.get())
        for msg in messages.value:
            print(msg.subject, msg.id, msg.from_escaped)
    except Exception as e:
        print(e.error.message)

asyncio.run(get_user_messages())
```

## Passing custom request headers
Each execution method i.e. `get()`, `post()`, `put()`, `patch()`, `delete()` accepts a `RequestConfiguration` object where the request headers can be set:

```py
from msgraph.generated.users.item.messages.messages_request_builder import MessagesRequestBuilder

async def get_user_messages():
    try:
        request_config = MessagesRequestBuilder.MessagesRequestBuilderGetRequestConfiguration(
            headers={"prefer": "outlook.body-content-type=text"}
        )

        messages = await (client.users_by_id('USER_ID')
                        .messages
                        .get(request_configuration=request_config))
        for msg in messages.value:
            print(msg.subject, msg.id, msg.from_escaped)
    except Exception as e:
        print(e.error.message)

asyncio.run(get_user_messages())
```

## Passing query parameters

```py
from msgraph.generated.users.item.messages.messages_request_builder import MessagesRequestBuilder

async def get_5_user_messages():
    try:
        query_params = MessagesRequestBuilder.MessagesRequestBuilderGetQueryParameters(
            select=['subject', 'from'], skip = 2, top=5
        )
        request_config = MessagesRequestBuilder.MessagesRequestBuilderGetRequestConfiguration(
            query_parameters=query_params
        )

        messages = await (client.users_by_id('USER_ID')
                        .messages
                        .get(request_configuration=request_config))
        for msg in messages.value:
            print(msg.subject)
    except Exception as e:
        print(e.error.message)

asyncio.run(get_5_user_messages())
```

## Paging through a collection of items
Some queries against Microsoft Graph return multiple pages of data either due to server-side paging or due to the use of the `$top` query parameter to specifically limit the page size in a request. When a result set spans multiple pages, Microsoft Graph returns an `@odata.nextLink` property in the response that contains a URL to the next page of results.

For now, you can page through the collection using the `@odata.nextLink` value. We intend to introduce a Page Iterator component in the future releases:

```py
from msgraph.generated.users.item.messages.messages_request_builder import MessagesRequestBuilder

async def get_user_messages():
    query_params = MessagesRequestBuilder.MessagesRequestBuilderGetQueryParameters(
        select=['subject',], top=3
    )
    request_config = MessagesRequestBuilder.MessagesRequestBuilderGetRequestConfiguration(
        query_parameters=query_params
    )

    messages = await (client.users_by_id('USER_ID')
                      .messages
                      .get(request_configuration=request_config))
    for msg in messages.value:
        print(msg.subject)
    while messages.odata_next_link:
        request_info = client.users_by_id(USER_ID)
                        .messages
                        .create_get_request_information(request_configuration=request_config)
        request_info.uri = messages.odata_next_link
        messages = request_adapter.send_async(request_info, MessageCollectionResponse)
        for msg in messages.value:
        print(msg.subject)

asyncio.run(get_user_messages())
```


## Get the raw response
The SDK provides a default response handler which returns the native HTTPX response.

To get the raw response:
```py
from kiota_abstractions.native_response_handler import NativeResponseHandler

async def get_user():
    try:
        user = await client.users_by_id('USER_ID').get(None, NativeResponseHandler())
        print(user.value)
    except Exception as e:
        print(e.error.message)
asyncio.run(get_user())
```

## Send an email

This sample sends an email. The request body is constructed using the provided models.
Ensure you have the [right permissions](https://docs.microsoft.com/en-us/graph/api/user-sendmail?view=graph-rest-1.0&tabs=http#permissions).

```py
from kiota_abstractions.api_error import APIError
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph import GraphRequestAdapter
from msgraph import GraphServiceClient

from msgraph.generated.me.send_mail.send_mail_post_request_body import SendMailPostRequestBody
from msgraph.generated.models.body_type import BodyType
from msgraph.generated.models.message import Message
from msgraph.generated.models.email_address import EmailAddress
from msgraph.generated.models.importance import Importance
from msgraph.generated.models.item_body import ItemBody
from msgraph.generated.models.recipient import Recipient
from msgraph.generated.users.item.messages.messages_request_builder import MessagesRequestBuilder



credential = ClientSecretCredential(
    'tenant_id',
    'client_id',
    'client_secret'
)
scopes = ['Mail.Send']
auth_provider = AzureIdentityAuthenticationProvider(credential, scopes=scopes)
request_adapter = GraphRequestAdapter(auth_provider)
client = GraphServiceClient(request_adapter)

async def send_mail():
    try:
        sender = EmailAddress()
        sender.address = 'john.doe@outlook.com'
        sender.name = 'John Doe'
        
        from_recipient = Recipient()
        from_recipient.email_address = sender
        recipients = []

        recipient_email = EmailAddress()
        recipient_email.address = 'jane.doe@outlook.com'
        recipient_email.name = 'Jane Doe'
        
        to_recipient = Recipient()
        to_recipient.email_address = recipient_email
        recipients.append(to_recipient) 

        email_body = ItemBody()
        email_body.content = 'Dummy content'
        email_body.content_type = BodyType.Text
        
        message = Message()
        message.subject = 'Test Email'
        message.from_escaped = from_recipient
        message.to_recipients = recipients
        message.body = email_body
        
        request_body = SendMailPostRequestBody()
        request_body.message = message
        response = await client.me.send_mail.post(request_body)

    except Exception as e:
        print(e.error.message)
asyncio.run(send_mail())

```