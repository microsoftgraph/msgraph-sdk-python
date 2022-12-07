from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

email_methods_request_builder = lazy_import('msgraph.generated.me.authentication.email_methods.email_methods_request_builder')
email_authentication_method_item_request_builder = lazy_import('msgraph.generated.me.authentication.email_methods.item.email_authentication_method_item_request_builder')
fido2_methods_request_builder = lazy_import('msgraph.generated.me.authentication.fido2_methods.fido2_methods_request_builder')
fido2_authentication_method_item_request_builder = lazy_import('msgraph.generated.me.authentication.fido2_methods.item.fido2_authentication_method_item_request_builder')
methods_request_builder = lazy_import('msgraph.generated.me.authentication.methods.methods_request_builder')
authentication_method_item_request_builder = lazy_import('msgraph.generated.me.authentication.methods.item.authentication_method_item_request_builder')
microsoft_authenticator_methods_request_builder = lazy_import('msgraph.generated.me.authentication.microsoft_authenticator_methods.microsoft_authenticator_methods_request_builder')
microsoft_authenticator_authentication_method_item_request_builder = lazy_import('msgraph.generated.me.authentication.microsoft_authenticator_methods.item.microsoft_authenticator_authentication_method_item_request_builder')
operations_request_builder = lazy_import('msgraph.generated.me.authentication.operations.operations_request_builder')
long_running_operation_item_request_builder = lazy_import('msgraph.generated.me.authentication.operations.item.long_running_operation_item_request_builder')
password_methods_request_builder = lazy_import('msgraph.generated.me.authentication.password_methods.password_methods_request_builder')
password_authentication_method_item_request_builder = lazy_import('msgraph.generated.me.authentication.password_methods.item.password_authentication_method_item_request_builder')
phone_methods_request_builder = lazy_import('msgraph.generated.me.authentication.phone_methods.phone_methods_request_builder')
phone_authentication_method_item_request_builder = lazy_import('msgraph.generated.me.authentication.phone_methods.item.phone_authentication_method_item_request_builder')
software_oath_methods_request_builder = lazy_import('msgraph.generated.me.authentication.software_oath_methods.software_oath_methods_request_builder')
software_oath_authentication_method_item_request_builder = lazy_import('msgraph.generated.me.authentication.software_oath_methods.item.software_oath_authentication_method_item_request_builder')
temporary_access_pass_methods_request_builder = lazy_import('msgraph.generated.me.authentication.temporary_access_pass_methods.temporary_access_pass_methods_request_builder')
temporary_access_pass_authentication_method_item_request_builder = lazy_import('msgraph.generated.me.authentication.temporary_access_pass_methods.item.temporary_access_pass_authentication_method_item_request_builder')
windows_hello_for_business_methods_request_builder = lazy_import('msgraph.generated.me.authentication.windows_hello_for_business_methods.windows_hello_for_business_methods_request_builder')
windows_hello_for_business_authentication_method_item_request_builder = lazy_import('msgraph.generated.me.authentication.windows_hello_for_business_methods.item.windows_hello_for_business_authentication_method_item_request_builder')
authentication = lazy_import('msgraph.generated.models.authentication')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class AuthenticationRequestBuilder():
    """
    Provides operations to manage the authentication property of the microsoft.graph.user entity.
    """
    def email_methods(self) -> email_methods_request_builder.EmailMethodsRequestBuilder:
        """
        Provides operations to manage the emailMethods property of the microsoft.graph.authentication entity.
        """
        return email_methods_request_builder.EmailMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def fido2_methods(self) -> fido2_methods_request_builder.Fido2MethodsRequestBuilder:
        """
        Provides operations to manage the fido2Methods property of the microsoft.graph.authentication entity.
        """
        return fido2_methods_request_builder.Fido2MethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def methods(self) -> methods_request_builder.MethodsRequestBuilder:
        """
        Provides operations to manage the methods property of the microsoft.graph.authentication entity.
        """
        return methods_request_builder.MethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def microsoft_authenticator_methods(self) -> microsoft_authenticator_methods_request_builder.MicrosoftAuthenticatorMethodsRequestBuilder:
        """
        Provides operations to manage the microsoftAuthenticatorMethods property of the microsoft.graph.authentication entity.
        """
        return microsoft_authenticator_methods_request_builder.MicrosoftAuthenticatorMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.authentication entity.
        """
        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def password_methods(self) -> password_methods_request_builder.PasswordMethodsRequestBuilder:
        """
        Provides operations to manage the passwordMethods property of the microsoft.graph.authentication entity.
        """
        return password_methods_request_builder.PasswordMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def phone_methods(self) -> phone_methods_request_builder.PhoneMethodsRequestBuilder:
        """
        Provides operations to manage the phoneMethods property of the microsoft.graph.authentication entity.
        """
        return phone_methods_request_builder.PhoneMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def software_oath_methods(self) -> software_oath_methods_request_builder.SoftwareOathMethodsRequestBuilder:
        """
        Provides operations to manage the softwareOathMethods property of the microsoft.graph.authentication entity.
        """
        return software_oath_methods_request_builder.SoftwareOathMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def temporary_access_pass_methods(self) -> temporary_access_pass_methods_request_builder.TemporaryAccessPassMethodsRequestBuilder:
        """
        Provides operations to manage the temporaryAccessPassMethods property of the microsoft.graph.authentication entity.
        """
        return temporary_access_pass_methods_request_builder.TemporaryAccessPassMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def windows_hello_for_business_methods(self) -> windows_hello_for_business_methods_request_builder.WindowsHelloForBusinessMethodsRequestBuilder:
        """
        Provides operations to manage the windowsHelloForBusinessMethods property of the microsoft.graph.authentication entity.
        """
        return windows_hello_for_business_methods_request_builder.WindowsHelloForBusinessMethodsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AuthenticationRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/authentication{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[AuthenticationRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
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
    
    def create_get_request_information(self,request_configuration: Optional[AuthenticationRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[authentication.Authentication] = None, request_configuration: Optional[AuthenticationRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property authentication in me
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[AuthenticationRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property authentication for me
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    def email_methods_by_id(self,id: str) -> email_authentication_method_item_request_builder.EmailAuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the emailMethods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: email_authentication_method_item_request_builder.EmailAuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["emailAuthenticationMethod%2Did"] = id
        return email_authentication_method_item_request_builder.EmailAuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def fido2_methods_by_id(self,id: str) -> fido2_authentication_method_item_request_builder.Fido2AuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the fido2Methods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: fido2_authentication_method_item_request_builder.Fido2AuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["fido2AuthenticationMethod%2Did"] = id
        return fido2_authentication_method_item_request_builder.Fido2AuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[AuthenticationRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[authentication.Authentication]:
        """
        The authentication methods that are supported for the user.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[authentication.Authentication]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, authentication.Authentication, response_handler, error_mapping)
    
    def methods_by_id(self,id: str) -> authentication_method_item_request_builder.AuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the methods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: authentication_method_item_request_builder.AuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["authenticationMethod%2Did"] = id
        return authentication_method_item_request_builder.AuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def microsoft_authenticator_methods_by_id(self,id: str) -> microsoft_authenticator_authentication_method_item_request_builder.MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the microsoftAuthenticatorMethods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: microsoft_authenticator_authentication_method_item_request_builder.MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["microsoftAuthenticatorAuthenticationMethod%2Did"] = id
        return microsoft_authenticator_authentication_method_item_request_builder.MicrosoftAuthenticatorAuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def operations_by_id(self,id: str) -> long_running_operation_item_request_builder.LongRunningOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: long_running_operation_item_request_builder.LongRunningOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["longRunningOperation%2Did"] = id
        return long_running_operation_item_request_builder.LongRunningOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def password_methods_by_id(self,id: str) -> password_authentication_method_item_request_builder.PasswordAuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the passwordMethods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: password_authentication_method_item_request_builder.PasswordAuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["passwordAuthenticationMethod%2Did"] = id
        return password_authentication_method_item_request_builder.PasswordAuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[authentication.Authentication] = None, request_configuration: Optional[AuthenticationRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[authentication.Authentication]:
        """
        Update the navigation property authentication in me
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[authentication.Authentication]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, authentication.Authentication, response_handler, error_mapping)
    
    def phone_methods_by_id(self,id: str) -> phone_authentication_method_item_request_builder.PhoneAuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the phoneMethods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: phone_authentication_method_item_request_builder.PhoneAuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["phoneAuthenticationMethod%2Did"] = id
        return phone_authentication_method_item_request_builder.PhoneAuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def software_oath_methods_by_id(self,id: str) -> software_oath_authentication_method_item_request_builder.SoftwareOathAuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the softwareOathMethods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: software_oath_authentication_method_item_request_builder.SoftwareOathAuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["softwareOathAuthenticationMethod%2Did"] = id
        return software_oath_authentication_method_item_request_builder.SoftwareOathAuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def temporary_access_pass_methods_by_id(self,id: str) -> temporary_access_pass_authentication_method_item_request_builder.TemporaryAccessPassAuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the temporaryAccessPassMethods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: temporary_access_pass_authentication_method_item_request_builder.TemporaryAccessPassAuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["temporaryAccessPassAuthenticationMethod%2Did"] = id
        return temporary_access_pass_authentication_method_item_request_builder.TemporaryAccessPassAuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def windows_hello_for_business_methods_by_id(self,id: str) -> windows_hello_for_business_authentication_method_item_request_builder.WindowsHelloForBusinessAuthenticationMethodItemRequestBuilder:
        """
        Provides operations to manage the windowsHelloForBusinessMethods property of the microsoft.graph.authentication entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_hello_for_business_authentication_method_item_request_builder.WindowsHelloForBusinessAuthenticationMethodItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsHelloForBusinessAuthenticationMethod%2Did"] = id
        return windows_hello_for_business_authentication_method_item_request_builder.WindowsHelloForBusinessAuthenticationMethodItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class AuthenticationRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class AuthenticationRequestBuilderGetQueryParameters():
        """
        The authentication methods that are supported for the user.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class AuthenticationRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

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
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

