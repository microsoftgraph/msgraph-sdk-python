from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ..........models.o_data_errors.o_data_error import ODataError
    from ..........models.profile_photo import ProfilePhoto
    from .value.content_request_builder import ContentRequestBuilder

class PhotoRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the photo property of the microsoft.graph.contact entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PhotoRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/contactFolders/{contactFolder%2Did}/childFolders/{contactFolder%2Did1}/contacts/{contact%2Did}/photo{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PhotoRequestBuilderGetQueryParameters]] = None) -> Optional[ProfilePhoto]:
        """
        Optional contact picture. You can get or set a photo for a contact.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ProfilePhoto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models.profile_photo import ProfilePhoto

        return await self.request_adapter.send_async(request_info, ProfilePhoto, error_mapping)
    
    async def patch(self,body: ProfilePhoto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ProfilePhoto]:
        """
        Update the navigation property photo in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ProfilePhoto]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..........models.profile_photo import ProfilePhoto

        return await self.request_adapter.send_async(request_info, ProfilePhoto, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PhotoRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Optional contact picture. You can get or set a photo for a contact.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ProfilePhoto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property photo in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> PhotoRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PhotoRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PhotoRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def content(self) -> ContentRequestBuilder:
        """
        Provides operations to manage the media for the user entity.
        """
        from .value.content_request_builder import ContentRequestBuilder

        return ContentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PhotoRequestBuilderGetQueryParameters():
        """
        Optional contact picture. You can get or set a photo for a contact.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class PhotoRequestBuilderGetRequestConfiguration(RequestConfiguration[PhotoRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PhotoRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

