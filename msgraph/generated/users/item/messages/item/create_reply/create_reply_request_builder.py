from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.message import Message
    from ......models.o_data_errors.o_data_error import ODataError
    from .create_reply_post_request_body import CreateReplyPostRequestBody

class CreateReplyRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the createReply method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new CreateReplyRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/messages/{message%2Did}/createReply", path_parameters)
    
    async def post(self,body: Optional[CreateReplyPostRequestBody] = None, request_configuration: Optional[CreateReplyRequestBuilderPostRequestConfiguration] = None) -> Optional[Message]:
        """
        Create a draft to reply to the sender of a message in either JSON or MIME format. When using JSON format:- Specify either a comment or the body property of the message parameter. Specifying both will return an HTTP 400 Bad Request error.- If replyTo is specified in the original message, per Internet Message Format (RFC 2822), you should send the reply to the recipients in replyTo, and not the recipients in from.- You can update the draft later to add reply content to the body or change other message properties. When using MIME format:- Provide the applicable Internet message headers and the MIME content, all encoded in base64 format in the request body.- Add any attachments and S/MIME properties to the MIME content. Send the draft message in a subsequent operation. Alternatively, reply to a message in a single operation.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Message]
        Find more info here: https://learn.microsoft.com/graph/api/message-createreply?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.message import Message

        return await self.request_adapter.send_async(request_info, Message, error_mapping)
    
    def to_post_request_information(self,body: Optional[CreateReplyPostRequestBody] = None, request_configuration: Optional[CreateReplyRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create a draft to reply to the sender of a message in either JSON or MIME format. When using JSON format:- Specify either a comment or the body property of the message parameter. Specifying both will return an HTTP 400 Bad Request error.- If replyTo is specified in the original message, per Internet Message Format (RFC 2822), you should send the reply to the recipients in replyTo, and not the recipients in from.- You can update the draft later to add reply content to the body or change other message properties. When using MIME format:- Provide the applicable Internet message headers and the MIME content, all encoded in base64 format in the request body.- Add any attachments and S/MIME properties to the MIME content. Send the draft message in a subsequent operation. Alternatively, reply to a message in a single operation.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CreateReplyRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CreateReplyRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CreateReplyRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CreateReplyRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

