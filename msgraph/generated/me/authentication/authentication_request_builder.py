from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models import authentication
    from ...models.o_data_errors import o_data_error
    from .email_methods import email_methods_request_builder
    from .fido2_methods import fido2_methods_request_builder
    from .methods import methods_request_builder
    from .microsoft_authenticator_methods import microsoft_authenticator_methods_request_builder
    from .operations import operations_request_builder
    from .password_methods import password_methods_request_builder
    from .phone_methods import phone_methods_request_builder
    from .software_oath_methods import software_oath_methods_request_builder
    from .temporary_access_pass_methods import temporary_access_pass_methods_request_builder
    from .windows_hello_for_business_methods import windows_hello_for_business_methods_request_builder

class AuthenticationRequestBuilder():
    """
    Provides operations to manage the authentication property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AuthenticationRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/authentication{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[AuthenticationRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property authentication for me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AuthenticationRequestBuilderGetRequestConfiguration] = None) -> Optional[authentication.Authentication]:
        """
        The authentication methods that are supported for the user.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[authentication.Authentication]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import authentication

        return await self.request_adapter.send_async(request_info, authentication.Authentication, error_mapping)
    
    async def patch(self,body: Optional[authentication.Authentication] = None, request_configuration: Optional[AuthenticationRequestBuilderPatchRequestConfiguration] = None) -> Optional[authentication.Authentication]:
        """
        Update the navigation property authentication in me
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[authentication.Authentication]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import authentication

        return await self.request_adapter.send_async(request_info, authentication.Authentication, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AuthenticationRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property authentication for me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[AuthenticationRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The authentication methods that are supported for the user.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[authentication.Authentication] = None, request_configuration: Optional[AuthenticationRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property authentication in me
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def email_methods(self) -> email_methods_request_builder.EmailMethodsRequestBuilder:
        """
        Provides operations to manage the emailMethods property of the microsoft.graph.authentication entity.
        """
        from .email_methods import email_methods_request_builder

        return email_methods_request_builder.EmailMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fido2_methods(self) -> fido2_methods_request_builder.Fido2MethodsRequestBuilder:
        """
        Provides operations to manage the fido2Methods property of the microsoft.graph.authentication entity.
        """
        from .fido2_methods import fido2_methods_request_builder

        return fido2_methods_request_builder.Fido2MethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def methods(self) -> methods_request_builder.MethodsRequestBuilder:
        """
        Provides operations to manage the methods property of the microsoft.graph.authentication entity.
        """
        from .methods import methods_request_builder

        return methods_request_builder.MethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_authenticator_methods(self) -> microsoft_authenticator_methods_request_builder.MicrosoftAuthenticatorMethodsRequestBuilder:
        """
        Provides operations to manage the microsoftAuthenticatorMethods property of the microsoft.graph.authentication entity.
        """
        from .microsoft_authenticator_methods import microsoft_authenticator_methods_request_builder

        return microsoft_authenticator_methods_request_builder.MicrosoftAuthenticatorMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.authentication entity.
        """
        from .operations import operations_request_builder

        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def password_methods(self) -> password_methods_request_builder.PasswordMethodsRequestBuilder:
        """
        Provides operations to manage the passwordMethods property of the microsoft.graph.authentication entity.
        """
        from .password_methods import password_methods_request_builder

        return password_methods_request_builder.PasswordMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def phone_methods(self) -> phone_methods_request_builder.PhoneMethodsRequestBuilder:
        """
        Provides operations to manage the phoneMethods property of the microsoft.graph.authentication entity.
        """
        from .phone_methods import phone_methods_request_builder

        return phone_methods_request_builder.PhoneMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def software_oath_methods(self) -> software_oath_methods_request_builder.SoftwareOathMethodsRequestBuilder:
        """
        Provides operations to manage the softwareOathMethods property of the microsoft.graph.authentication entity.
        """
        from .software_oath_methods import software_oath_methods_request_builder

        return software_oath_methods_request_builder.SoftwareOathMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def temporary_access_pass_methods(self) -> temporary_access_pass_methods_request_builder.TemporaryAccessPassMethodsRequestBuilder:
        """
        Provides operations to manage the temporaryAccessPassMethods property of the microsoft.graph.authentication entity.
        """
        from .temporary_access_pass_methods import temporary_access_pass_methods_request_builder

        return temporary_access_pass_methods_request_builder.TemporaryAccessPassMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_hello_for_business_methods(self) -> windows_hello_for_business_methods_request_builder.WindowsHelloForBusinessMethodsRequestBuilder:
        """
        Provides operations to manage the windowsHelloForBusinessMethods property of the microsoft.graph.authentication entity.
        """
        from .windows_hello_for_business_methods import windows_hello_for_business_methods_request_builder

        return windows_hello_for_business_methods_request_builder.WindowsHelloForBusinessMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AuthenticationRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AuthenticationRequestBuilderGetQueryParameters():
        """
        The authentication methods that are supported for the user.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
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

    
    @dataclass
    class AuthenticationRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[AuthenticationRequestBuilder.AuthenticationRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class AuthenticationRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

