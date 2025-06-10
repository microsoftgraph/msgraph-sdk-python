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
    from ....models.authentication import Authentication
    from ....models.o_data_errors.o_data_error import ODataError
    from .email_methods.email_methods_request_builder import EmailMethodsRequestBuilder
    from .fido2_methods.fido2_methods_request_builder import Fido2MethodsRequestBuilder
    from .methods.methods_request_builder import MethodsRequestBuilder
    from .microsoft_authenticator_methods.microsoft_authenticator_methods_request_builder import MicrosoftAuthenticatorMethodsRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .password_methods.password_methods_request_builder import PasswordMethodsRequestBuilder
    from .phone_methods.phone_methods_request_builder import PhoneMethodsRequestBuilder
    from .platform_credential_methods.platform_credential_methods_request_builder import PlatformCredentialMethodsRequestBuilder
    from .software_oath_methods.software_oath_methods_request_builder import SoftwareOathMethodsRequestBuilder
    from .temporary_access_pass_methods.temporary_access_pass_methods_request_builder import TemporaryAccessPassMethodsRequestBuilder
    from .windows_hello_for_business_methods.windows_hello_for_business_methods_request_builder import WindowsHelloForBusinessMethodsRequestBuilder

class AuthenticationRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the authentication property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AuthenticationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/authentication{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property authentication for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AuthenticationRequestBuilderGetQueryParameters]] = None) -> Optional[Authentication]:
        """
        The authentication methods that are supported for the user.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Authentication]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.authentication import Authentication

        return await self.request_adapter.send_async(request_info, Authentication, error_mapping)
    
    async def patch(self,body: Authentication, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Authentication]:
        """
        Update the navigation property authentication in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Authentication]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.authentication import Authentication

        return await self.request_adapter.send_async(request_info, Authentication, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property authentication for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AuthenticationRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The authentication methods that are supported for the user.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Authentication, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property authentication in users
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
    
    def with_url(self,raw_url: str) -> AuthenticationRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AuthenticationRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AuthenticationRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def email_methods(self) -> EmailMethodsRequestBuilder:
        """
        Provides operations to manage the emailMethods property of the microsoft.graph.authentication entity.
        """
        from .email_methods.email_methods_request_builder import EmailMethodsRequestBuilder

        return EmailMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fido2_methods(self) -> Fido2MethodsRequestBuilder:
        """
        Provides operations to manage the fido2Methods property of the microsoft.graph.authentication entity.
        """
        from .fido2_methods.fido2_methods_request_builder import Fido2MethodsRequestBuilder

        return Fido2MethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def methods(self) -> MethodsRequestBuilder:
        """
        Provides operations to manage the methods property of the microsoft.graph.authentication entity.
        """
        from .methods.methods_request_builder import MethodsRequestBuilder

        return MethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_authenticator_methods(self) -> MicrosoftAuthenticatorMethodsRequestBuilder:
        """
        Provides operations to manage the microsoftAuthenticatorMethods property of the microsoft.graph.authentication entity.
        """
        from .microsoft_authenticator_methods.microsoft_authenticator_methods_request_builder import MicrosoftAuthenticatorMethodsRequestBuilder

        return MicrosoftAuthenticatorMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.authentication entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def password_methods(self) -> PasswordMethodsRequestBuilder:
        """
        Provides operations to manage the passwordMethods property of the microsoft.graph.authentication entity.
        """
        from .password_methods.password_methods_request_builder import PasswordMethodsRequestBuilder

        return PasswordMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def phone_methods(self) -> PhoneMethodsRequestBuilder:
        """
        Provides operations to manage the phoneMethods property of the microsoft.graph.authentication entity.
        """
        from .phone_methods.phone_methods_request_builder import PhoneMethodsRequestBuilder

        return PhoneMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def platform_credential_methods(self) -> PlatformCredentialMethodsRequestBuilder:
        """
        Provides operations to manage the platformCredentialMethods property of the microsoft.graph.authentication entity.
        """
        from .platform_credential_methods.platform_credential_methods_request_builder import PlatformCredentialMethodsRequestBuilder

        return PlatformCredentialMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def software_oath_methods(self) -> SoftwareOathMethodsRequestBuilder:
        """
        Provides operations to manage the softwareOathMethods property of the microsoft.graph.authentication entity.
        """
        from .software_oath_methods.software_oath_methods_request_builder import SoftwareOathMethodsRequestBuilder

        return SoftwareOathMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def temporary_access_pass_methods(self) -> TemporaryAccessPassMethodsRequestBuilder:
        """
        Provides operations to manage the temporaryAccessPassMethods property of the microsoft.graph.authentication entity.
        """
        from .temporary_access_pass_methods.temporary_access_pass_methods_request_builder import TemporaryAccessPassMethodsRequestBuilder

        return TemporaryAccessPassMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_hello_for_business_methods(self) -> WindowsHelloForBusinessMethodsRequestBuilder:
        """
        Provides operations to manage the windowsHelloForBusinessMethods property of the microsoft.graph.authentication entity.
        """
        from .windows_hello_for_business_methods.windows_hello_for_business_methods_request_builder import WindowsHelloForBusinessMethodsRequestBuilder

        return WindowsHelloForBusinessMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class AuthenticationRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AuthenticationRequestBuilderGetQueryParameters():
        """
        The authentication methods that are supported for the user.
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
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class AuthenticationRequestBuilderGetRequestConfiguration(RequestConfiguration[AuthenticationRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AuthenticationRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

