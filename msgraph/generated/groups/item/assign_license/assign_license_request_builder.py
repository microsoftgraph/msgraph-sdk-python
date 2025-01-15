from __future__ import annotations
from collections.abc import Callable
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
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.group import Group
    from ....models.o_data_errors.o_data_error import ODataError
    from .assign_license_post_request_body import AssignLicensePostRequestBody

class AssignLicenseRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the assignLicense method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AssignLicenseRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/assignLicense", path_parameters)
    
    async def post(self,body: AssignLicensePostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Group]:
        """
        Add or remove licenses on a group. Licenses assigned to the group will be assigned to all users in the group. Group-based licensing is an alternative to direct user licensing. To learn more about group-based licensing, see What is group-based licensing in Microsoft Entra ID. To get the subscriptions available in the directory, perform a GET subscribedSkus request.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Group]
        Find more info here: https://learn.microsoft.com/graph/api/group-assignlicense?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.group import Group

        return await self.request_adapter.send_async(request_info, Group, error_mapping)
    
    def to_post_request_information(self,body: AssignLicensePostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Add or remove licenses on a group. Licenses assigned to the group will be assigned to all users in the group. Group-based licensing is an alternative to direct user licensing. To learn more about group-based licensing, see What is group-based licensing in Microsoft Entra ID. To get the subscriptions available in the directory, perform a GET subscribedSkus request.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> AssignLicenseRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AssignLicenseRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AssignLicenseRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class AssignLicenseRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

