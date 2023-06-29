from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.group import Group
    from ....models.o_data_errors.o_data_error import ODataError
    from .assign_license_post_request_body import AssignLicensePostRequestBody

class AssignLicenseRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the assignLicense method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AssignLicenseRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/assignLicense", path_parameters)
    
    async def post(self,body: Optional[AssignLicensePostRequestBody] = None, request_configuration: Optional[AssignLicenseRequestBuilderPostRequestConfiguration] = None) -> Optional[Group]:
        """
        Add or remove licenses on the group. Licenses assigned to the group will be assigned to all users in the group. To learn more about group-based licensing, see What is group-based licensing in Azure Active Directory. To get the subscriptions available in the directory, perform a GET subscribedSkus request.
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Group]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.group import Group

        return await self.request_adapter.send_async(request_info, Group, error_mapping)
    
    def to_post_request_information(self,body: Optional[AssignLicensePostRequestBody] = None, request_configuration: Optional[AssignLicenseRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Add or remove licenses on the group. Licenses assigned to the group will be assigned to all users in the group. To learn more about group-based licensing, see What is group-based licensing in Azure Active Directory. To get the subscriptions available in the directory, perform a GET subscribedSkus request.
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AssignLicenseRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

