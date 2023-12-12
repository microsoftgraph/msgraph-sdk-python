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
    from ......models.microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
    from ......models.o_data_errors.o_data_error import ODataError
    from .device.device_request_builder import DeviceRequestBuilder

class MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the microsoftAuthenticatorMethods property of the microsoft.graph.authentication entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/authentication/microsoftAuthenticatorMethods/{microsoftAuthenticatorAuthenticationMethod%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Deletes a microsoftAuthenticatorAuthenticationMethod object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/microsoftauthenticatorauthenticationmethod-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilderGetRequestConfiguration] = None) -> Optional[MicrosoftAuthenticatorAuthenticationMethod]:
        """
        Read the properties and relationships of a microsoftAuthenticatorAuthenticationMethod object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MicrosoftAuthenticatorAuthenticationMethod]
        Find more info here: https://learn.microsoft.com/graph/api/microsoftauthenticatorauthenticationmethod-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod

        return await self.request_adapter.send_async(request_info, MicrosoftAuthenticatorAuthenticationMethod, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Deletes a microsoftAuthenticatorAuthenticationMethod object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of a microsoftAuthenticatorAuthenticationMethod object.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def device(self) -> DeviceRequestBuilder:
        """
        Provides operations to manage the device property of the microsoft.graph.microsoftAuthenticatorAuthenticationMethod entity.
        """
        from .device.device_request_builder import DeviceRequestBuilder

        return DeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a microsoftAuthenticatorAuthenticationMethod object.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilder.MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilderGetQueryParameters] = None

    

