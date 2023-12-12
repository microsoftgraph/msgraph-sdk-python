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
    from ......models.phone_authentication_method import PhoneAuthenticationMethod
    from .disable_sms_sign_in.disable_sms_sign_in_request_builder import DisableSmsSignInRequestBuilder
    from .enable_sms_sign_in.enable_sms_sign_in_request_builder import EnableSmsSignInRequestBuilder

class PhoneAuthenticationMethodItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the phoneMethods property of the microsoft.graph.authentication entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PhoneAuthenticationMethodItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/authentication/phoneMethods/{phoneAuthenticationMethod%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[PhoneAuthenticationMethodItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete a user's phone authentication method. This removes the phone number from the user and they'll no longer be able to use the number for authentication, whether via SMS or voice calls. A user can't have an alternateMobile number without a mobile number. If you want to remove a mobile number from a user that also has an alternateMobile number, first update the mobile number to the new number, then delete the alternateMobile number. If the phone number is the user's default Azure multi-factor authentication (MFA) authentication method, it can't be deleted. Have the user change their default authentication method, and then delete the number.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/phoneauthenticationmethod-delete?view=graph-rest-1.0
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
    
    async def get(self,request_configuration: Optional[PhoneAuthenticationMethodItemRequestBuilderGetRequestConfiguration] = None) -> Optional[PhoneAuthenticationMethod]:
        """
        Retrieve a single phoneAuthenticationMethod object for a user. This method is available only for standard Microsoft Entra ID and B2B users, but not B2C users.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PhoneAuthenticationMethod]
        Find more info here: https://learn.microsoft.com/graph/api/phoneauthenticationmethod-get?view=graph-rest-1.0
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
        from ......models.phone_authentication_method import PhoneAuthenticationMethod

        return await self.request_adapter.send_async(request_info, PhoneAuthenticationMethod, error_mapping)
    
    async def patch(self,body: Optional[PhoneAuthenticationMethod] = None, request_configuration: Optional[PhoneAuthenticationMethodItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[PhoneAuthenticationMethod]:
        """
        Update a user's phone number associated with a phone authentication method object. You can't change a phone's type. To change a phone's type, add a new number of the desired type and then delete the object with the original type. If a user is enabled by policy to use SMS to sign in and the mobile number is changed, the system will attempt to register the number for use in that system.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PhoneAuthenticationMethod]
        Find more info here: https://learn.microsoft.com/graph/api/phoneauthenticationmethod-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.phone_authentication_method import PhoneAuthenticationMethod

        return await self.request_adapter.send_async(request_info, PhoneAuthenticationMethod, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[PhoneAuthenticationMethodItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete a user's phone authentication method. This removes the phone number from the user and they'll no longer be able to use the number for authentication, whether via SMS or voice calls. A user can't have an alternateMobile number without a mobile number. If you want to remove a mobile number from a user that also has an alternateMobile number, first update the mobile number to the new number, then delete the alternateMobile number. If the phone number is the user's default Azure multi-factor authentication (MFA) authentication method, it can't be deleted. Have the user change their default authentication method, and then delete the number.
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
    
    def to_get_request_information(self,request_configuration: Optional[PhoneAuthenticationMethodItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve a single phoneAuthenticationMethod object for a user. This method is available only for standard Microsoft Entra ID and B2B users, but not B2C users.
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
    
    def to_patch_request_information(self,body: Optional[PhoneAuthenticationMethod] = None, request_configuration: Optional[PhoneAuthenticationMethodItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update a user's phone number associated with a phone authentication method object. You can't change a phone's type. To change a phone's type, add a new number of the desired type and then delete the object with the original type. If a user is enabled by policy to use SMS to sign in and the mobile number is changed, the system will attempt to register the number for use in that system.
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
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> PhoneAuthenticationMethodItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PhoneAuthenticationMethodItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PhoneAuthenticationMethodItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def disable_sms_sign_in(self) -> DisableSmsSignInRequestBuilder:
        """
        Provides operations to call the disableSmsSignIn method.
        """
        from .disable_sms_sign_in.disable_sms_sign_in_request_builder import DisableSmsSignInRequestBuilder

        return DisableSmsSignInRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enable_sms_sign_in(self) -> EnableSmsSignInRequestBuilder:
        """
        Provides operations to call the enableSmsSignIn method.
        """
        from .enable_sms_sign_in.enable_sms_sign_in_request_builder import EnableSmsSignInRequestBuilder

        return EnableSmsSignInRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PhoneAuthenticationMethodItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class PhoneAuthenticationMethodItemRequestBuilderGetQueryParameters():
        """
        Retrieve a single phoneAuthenticationMethod object for a user. This method is available only for standard Microsoft Entra ID and B2B users, but not B2C users.
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
    class PhoneAuthenticationMethodItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[PhoneAuthenticationMethodItemRequestBuilder.PhoneAuthenticationMethodItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PhoneAuthenticationMethodItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

