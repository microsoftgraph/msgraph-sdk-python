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
    from ..........models.attachment import Attachment
    from ..........models.attachment_collection_response import AttachmentCollectionResponse
    from ..........models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .create_upload_session.create_upload_session_request_builder import CreateUploadSessionRequestBuilder
    from .item.attachment_item_request_builder import AttachmentItemRequestBuilder

class AttachmentsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the attachments property of the microsoft.graph.message entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AttachmentsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/mailFolders/{mailFolder%2Did}/childFolders/{mailFolder%2Did1}/messages/{message%2Did}/attachments{?%24filter,%24count,%24orderby,%24select,%24expand}", path_parameters)
    
    def by_attachment_id(self,attachment_id: str) -> AttachmentItemRequestBuilder:
        """
        Provides operations to manage the attachments property of the microsoft.graph.message entity.
        param attachment_id: The unique identifier of attachment
        Returns: AttachmentItemRequestBuilder
        """
        if not attachment_id:
            raise TypeError("attachment_id cannot be null.")
        from .item.attachment_item_request_builder import AttachmentItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["attachment%2Did"] = attachment_id
        return AttachmentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[AttachmentsRequestBuilderGetRequestConfiguration] = None) -> Optional[AttachmentCollectionResponse]:
        """
        Retrieve a list of attachment objects.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AttachmentCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/eventmessage-list-attachments?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models.attachment_collection_response import AttachmentCollectionResponse

        return await self.request_adapter.send_async(request_info, AttachmentCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[Attachment] = None, request_configuration: Optional[AttachmentsRequestBuilderPostRequestConfiguration] = None) -> Optional[Attachment]:
        """
        Use this API to add an attachment to a message. An attachment can be one of the following types: All these types of attachment resources are derived from the attachmentresource. You can add an attachment to an existing message by posting to its attachments collection, or you canadd an attachment to a message that is being created and sent on the fly. This operation limits the size of the attachment you can add to under 3 MB.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Attachment]
        Find more info here: https://learn.microsoft.com/graph/api/message-post-attachments?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models.attachment import Attachment

        return await self.request_adapter.send_async(request_info, Attachment, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[AttachmentsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve a list of attachment objects.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[Attachment] = None, request_configuration: Optional[AttachmentsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Use this API to add an attachment to a message. An attachment can be one of the following types: All these types of attachment resources are derived from the attachmentresource. You can add an attachment to an existing message by posting to its attachments collection, or you canadd an attachment to a message that is being created and sent on the fly. This operation limits the size of the attachment you can add to under 3 MB.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> AttachmentsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AttachmentsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AttachmentsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_upload_session(self) -> CreateUploadSessionRequestBuilder:
        """
        Provides operations to call the createUploadSession method.
        """
        from .create_upload_session.create_upload_session_request_builder import CreateUploadSessionRequestBuilder

        return CreateUploadSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AttachmentsRequestBuilderGetQueryParameters():
        """
        Retrieve a list of attachment objects.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AttachmentsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AttachmentsRequestBuilder.AttachmentsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AttachmentsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

