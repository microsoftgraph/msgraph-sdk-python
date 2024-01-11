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
    from ......models.o_data_errors.o_data_error import ODataError
    from .add_group_post_request_body import AddGroupPostRequestBody
    from .add_group_post_response import AddGroupPostResponse

class AddGroupRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the addGroup method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AddGroupRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/groupLifecyclePolicies/{groupLifecyclePolicy%2Did}/addGroup", path_parameters)
    
    async def post(self,body: Optional[AddGroupPostRequestBody] = None, request_configuration: Optional[AddGroupRequestBuilderPostRequestConfiguration] = None) -> Optional[AddGroupPostResponse]:
        """
        Adds specific groups to a lifecycle policy. This action limits the group lifecycle policy to a set of groups only if the managedGroupTypes property of groupLifecyclePolicy is set to Selected.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AddGroupPostResponse]
        Find more info here: https://learn.microsoft.com/graph/api/grouplifecyclepolicy-addgroup?view=graph-rest-1.0
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
        from .add_group_post_response import AddGroupPostResponse

        return await self.request_adapter.send_async(request_info, AddGroupPostResponse, error_mapping)
    
    def to_post_request_information(self,body: Optional[AddGroupPostRequestBody] = None, request_configuration: Optional[AddGroupRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Adds specific groups to a lifecycle policy. This action limits the group lifecycle policy to a set of groups only if the managedGroupTypes property of groupLifecyclePolicy is set to Selected.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> AddGroupRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AddGroupRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AddGroupRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AddGroupRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

