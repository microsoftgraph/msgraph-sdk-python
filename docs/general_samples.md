# Usage Examples

## 1. Creating a Graph client
This creates a default Graph client that uses `https://graph.microsoft.com` as the default base URL and default configured HTTPX client to make the requests.

```py
from azure.identity import AuthorizationCodeCredential
from msgraph import GraphServiceClient

credentials = AuthorizationCodeCredential(
    tenant_id: str,
    client_id: str,
    authorization_code: str,
    redirect_uri: str
)
scopes = ['User.Read', 'Mail.ReadWrite']
client = GraphServiceClient(credentials=credentials, scopes=scopes)
```

## 2. Creating a Graph client using a custom `httpx.AsyncClient` instance

```py
from msgraph import GraphRequestAdapter
from msgraph_core import GraphClientFactory

http_client = GraphClientFactory.create_with_default_middleware(client=httpx.AsyncClient())
request_adapter = GraphRequestAdapter(auth_provider, http_client)
client = GraphServiceClient(request_adapter=request_adapter)
```

## 3. Get an item from the Microsoft Graph API

This sample fetches the current signed-in user. Note that to use `/me` endpoint you need
a delegated permission. Alternatively, using application permissions, you can request `/users/[userPrincipalName]`. See [Microsoft Graph Permissions](https://docs.microsoft.com/en-us/graph/auth/auth-concepts#microsoft-graph-permissions) for more.


```py
async def get_me():
    me = await client.me.get()
    if me:
        print(me.user_principal_name, me.display_name, me.id)
asyncio.run(get_me())
```

## 4. Get a collection of items
This snippet retrieves the messages in a user's mailbox. Ensure you have the [correct permissions](https://docs.microsoft.com/en-us/graph/api/user-list-messages?view=graph-rest-1.0&tabs=http#permissions) set.
The Graph API response is deserialized into a collection of `Message` - a model class provided by the SDK.

```py
async def get_user_messages():
    messages = await (client.users.by_user_id('USER_ID').messages.get())
    if messages and messages.value:
        for msg in messages.value:
            print(msg.subject, msg.id, msg.from_)
asyncio.run(get_user_messages())
```

## 5. Passing custom request headers
Each execution method i.e. `get()`, `post()`, `put()`, `patch()`, `delete()` accepts a `RequestConfiguration` object where the request headers can be set:

```py
from msgraph.generated.users.item.messages.messages_request_builder import MessagesRequestBuilder

async def get_user_messages():
    request_config = MessagesRequestBuilder.MessagesRequestBuilderGetRequestConfiguration(
    )
    request_config.headers.add("prefer", "outlook.body-content-type=text")

    messages = await (client.users.by_user_id('USER_ID')
                    .messages
                    .get(request_configuration=request_config))
    if messages and messages.value:
        for msg in messages.value:
            print(msg.subject, msg.id, msg.from_)
asyncio.run(get_user_messages())
```

## 6. Passing query parameters

```py
from msgraph.generated.users.item.messages.messages_request_builder import MessagesRequestBuilder

async def get_5_user_messages():
    query_params = MessagesRequestBuilder.MessagesRequestBuilderGetQueryParameters(
        select=['subject', 'from'], skip = 2, top=5
    )
    request_config = MessagesRequestBuilder.MessagesRequestBuilderGetRequestConfiguration(
        query_parameters=query_params
    )

    messages = await (client.users.by_user_id('USER_ID')
                    .messages
                    .get(request_configuration=request_config))
    if messages and messages.value:
        for msg in messages.value:
            print(msg.subject)
asyncio.run(get_5_user_messages())
```

## 7. Get the raw http response
The SDK provides a default response handler which returns the native HTTPX response.

To get the raw response:
```py
from kiota_abstractions.native_response_handler import NativeResponseHandler
from kiota_http.middleware.options import ResponseHandlerOption
from msgraph.generated.users.item.messages.messages_request_builder import MessagesRequestBuilder

async def get_user_messages():
    request_config = MessagesRequestBuilder.MessagesRequestBuilderGetRequestConfiguration(
        options=[ResponseHandlerOption(NativeResponseHandler())], )
    messages = await client.users.by_user_id('USER_ID').messages.get(request_configuration=request_config)
    print(messages.json())
asyncio.run(get_user())
```

## 8. Send Mail with User's delegation

This sample sends an email. The request body is constructed using the provided models.
Ensure you have the [right permissions](https://docs.microsoft.com/en-us/graph/api/user-sendmail?view=graph-rest-1.0&tabs=http#permissions).

Setup includes:
1. App Registration > Authentication > `Platform: Mobile and desktop applications` with `redirect_uri` specified as `http://localhost` and **public client flow** enabled.
2. App Registration > API permissions > `Mail.Send` permissions, potentially requiring admin consent.


```py
import asyncio
from msgraph import GraphServiceClient

from msgraph.generated.users.item.send_mail.send_mail_post_request_body import SendMailPostRequestBody
from msgraph.generated.models.body_type import BodyType
from msgraph.generated.models.message import Message
from msgraph.generated.models.email_address import EmailAddress
from msgraph.generated.models.importance import Importance
from msgraph.generated.models.item_body import ItemBody
from msgraph.generated.models.recipient import Recipient
from msgraph.generated.users.item.messages.messages_request_builder import MessagesRequestBuilder

from azure.identity import InteractiveBrowserCredential

credential = InteractiveBrowserCredential(
    client_id,
    authority,
    tenant_id,
    redirect_uri
)
scopes = ['Mail.Send']
# alternatively, use "Mail.Send.Shared" for a shared mailbox.

client = GraphServiceClient(credentials=credential, scopes=scopes)

async def send_mail():
    
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
asyncio.run(send_mail())
```
## 8.1 Send Mail with Shared Mailbox and "Public Client" setup
To use a shared mailbox (From) to which user (Sender) has access, the "From" recipient has to be additionally. Resulting in the following code.

Note that you require **Mail.Send.Shared** permissions to send from shared mailboxes.

```py
import asyncio
from msgraph import GraphServiceClient

from msgraph.generated.models.body_type import BodyType
from msgraph.generated.models.message import Message
from msgraph.generated.models.email_address import EmailAddress
from msgraph.generated.models.item_body import ItemBody
from msgraph.generated.models.recipient import Recipient
from msgraph.generated.users.item.send_mail.send_mail_post_request_body import SendMailPostRequestBody

from azure.identity import InteractiveBrowserCredential

# Create a credential object. Used to authenticate requests
credential = InteractiveBrowserCredential(
    client_id,
    authority, # e.g. https://login.microsoftonline.com/ for public Azure cloud
    tenant_id,
    redirect_uri # as configured in your App Registration > Authentication > Platform: Mobile and desktop applications
)
scopes = ["Mail.Send.Shared"]

# Create an API client with the credentials and scopes.
client = GraphServiceClient(credentials=credential, scopes=scopes)


async def send_mail():
    sender = EmailAddress()
    sender.address = 'john.doe@outlook.com'
    sender.name = 'John Doe' # skip to use default

    sender_recipient = Recipient()
    sender_recipient.email_address = sender

    from_mailbox = EmailAddress()
    from_mailbox.address = 'your-shared-mailbox@outlook.com'
    # skip from_mailbox.name = ... to use the default display name of the shared mailbox

    from_recipient = Recipient()
    from_recipient.email_address = from_mailbox

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
    message.sender = sender_recipient
    message.from_ = from_recipient
    message.to_recipients = recipients
    message.body = email_body

    request_body = SendMailPostRequestBody()
    request_body.message = message
    response = await client.me.send_mail.post(request_body)
asyncio.run(send_mail())
```