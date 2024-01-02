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
    from ...models.authentication_methods_root import AuthenticationMethodsRoot
    from ...models.o_data_errors.o_data_error import ODataError
    from .users_registered_by_feature.users_registered_by_feature_request_builder import UsersRegisteredByFeatureRequestBuilder
    from .users_registered_by_feature_with_included_user_types_with_included_user_roles.users_registered_by_feature_with_included_user_types_with_included_user_roles_request_builder import UsersRegisteredByFeatureWithIncludedUserTypesWithIncludedUserRolesRequestBuilder
    from .users_registered_by_method.users_registered_by_method_request_builder import UsersRegisteredByMethodRequestBuilder
    from .users_registered_by_method_with_included_user_types_with_included_user_roles.users_registered_by_method_with_included_user_types_with_included_user_roles_request_builder import UsersRegisteredByMethodWithIncludedUserTypesWithIncludedUserRolesRequestBuilder
    from .user_registration_details.user_registration_details_request_builder import UserRegistrationDetailsRequestBuilder

class AuthenticationMethodsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the authenticationMethods property of the microsoft.graph.reportRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AuthenticationMethodsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/reports/authenticationMethods{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[AuthenticationMethodsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property authenticationMethods for reports
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AuthenticationMethodsRequestBuilderGetRequestConfiguration] = None) -> Optional[AuthenticationMethodsRoot]:
        """
        Container for navigation properties for Microsoft Entra authentication methods resources.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AuthenticationMethodsRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.authentication_methods_root import AuthenticationMethodsRoot

        return await self.request_adapter.send_async(request_info, AuthenticationMethodsRoot, error_mapping)
    
    async def patch(self,body: Optional[AuthenticationMethodsRoot] = None, request_configuration: Optional[AuthenticationMethodsRequestBuilderPatchRequestConfiguration] = None) -> Optional[AuthenticationMethodsRoot]:
        """
        Update the navigation property authenticationMethods in reports
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AuthenticationMethodsRoot]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.authentication_methods_root import AuthenticationMethodsRoot

        return await self.request_adapter.send_async(request_info, AuthenticationMethodsRoot, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AuthenticationMethodsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property authenticationMethods for reports
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
    
    def to_get_request_information(self,request_configuration: Optional[AuthenticationMethodsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Container for navigation properties for Microsoft Entra authentication methods resources.
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
    
    def to_patch_request_information(self,body: Optional[AuthenticationMethodsRoot] = None, request_configuration: Optional[AuthenticationMethodsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property authenticationMethods in reports
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
    
    def users_registered_by_feature_with_included_user_types_with_included_user_roles(self,included_user_roles: Optional[str] = None, included_user_types: Optional[str] = None) -> UsersRegisteredByFeatureWithIncludedUserTypesWithIncludedUserRolesRequestBuilder:
        """
        Provides operations to call the usersRegisteredByFeature method.
        param included_user_roles: Usage: includedUserRoles='{includedUserRoles}'
        param included_user_types: Usage: includedUserTypes='{includedUserTypes}'
        Returns: UsersRegisteredByFeatureWithIncludedUserTypesWithIncludedUserRolesRequestBuilder
        """
        if not included_user_roles:
            raise TypeError("included_user_roles cannot be null.")
        if not included_user_types:
            raise TypeError("included_user_types cannot be null.")
        from .users_registered_by_feature_with_included_user_types_with_included_user_roles.users_registered_by_feature_with_included_user_types_with_included_user_roles_request_builder import UsersRegisteredByFeatureWithIncludedUserTypesWithIncludedUserRolesRequestBuilder

        return UsersRegisteredByFeatureWithIncludedUserTypesWithIncludedUserRolesRequestBuilder(self.request_adapter, self.path_parameters, included_user_roles, included_user_types)
    
    def users_registered_by_method_with_included_user_types_with_included_user_roles(self,included_user_roles: Optional[str] = None, included_user_types: Optional[str] = None) -> UsersRegisteredByMethodWithIncludedUserTypesWithIncludedUserRolesRequestBuilder:
        """
        Provides operations to call the usersRegisteredByMethod method.
        param included_user_roles: Usage: includedUserRoles='{includedUserRoles}'
        param included_user_types: Usage: includedUserTypes='{includedUserTypes}'
        Returns: UsersRegisteredByMethodWithIncludedUserTypesWithIncludedUserRolesRequestBuilder
        """
        if not included_user_roles:
            raise TypeError("included_user_roles cannot be null.")
        if not included_user_types:
            raise TypeError("included_user_types cannot be null.")
        from .users_registered_by_method_with_included_user_types_with_included_user_roles.users_registered_by_method_with_included_user_types_with_included_user_roles_request_builder import UsersRegisteredByMethodWithIncludedUserTypesWithIncludedUserRolesRequestBuilder

        return UsersRegisteredByMethodWithIncludedUserTypesWithIncludedUserRolesRequestBuilder(self.request_adapter, self.path_parameters, included_user_roles, included_user_types)
    
    def with_url(self,raw_url: Optional[str] = None) -> AuthenticationMethodsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AuthenticationMethodsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AuthenticationMethodsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def user_registration_details(self) -> UserRegistrationDetailsRequestBuilder:
        """
        Provides operations to manage the userRegistrationDetails property of the microsoft.graph.authenticationMethodsRoot entity.
        """
        from .user_registration_details.user_registration_details_request_builder import UserRegistrationDetailsRequestBuilder

        return UserRegistrationDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users_registered_by_feature(self) -> UsersRegisteredByFeatureRequestBuilder:
        """
        Provides operations to call the usersRegisteredByFeature method.
        """
        from .users_registered_by_feature.users_registered_by_feature_request_builder import UsersRegisteredByFeatureRequestBuilder

        return UsersRegisteredByFeatureRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users_registered_by_method(self) -> UsersRegisteredByMethodRequestBuilder:
        """
        Provides operations to call the usersRegisteredByMethod method.
        """
        from .users_registered_by_method.users_registered_by_method_request_builder import UsersRegisteredByMethodRequestBuilder

        return UsersRegisteredByMethodRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AuthenticationMethodsRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class AuthenticationMethodsRequestBuilderGetQueryParameters():
        """
        Container for navigation properties for Microsoft Entra authentication methods resources.
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
    class AuthenticationMethodsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AuthenticationMethodsRequestBuilder.AuthenticationMethodsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AuthenticationMethodsRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

