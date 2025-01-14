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
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AuthenticationMethodsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/reports/authenticationMethods{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property authenticationMethods for reports
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AuthenticationMethodsRequestBuilderGetQueryParameters]] = None) -> Optional[AuthenticationMethodsRoot]:
        """
        Container for navigation properties for Microsoft Entra authentication methods resources.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AuthenticationMethodsRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.authentication_methods_root import AuthenticationMethodsRoot

        return await self.request_adapter.send_async(request_info, AuthenticationMethodsRoot, error_mapping)
    
    async def patch(self,body: AuthenticationMethodsRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[AuthenticationMethodsRoot]:
        """
        Update the navigation property authenticationMethods in reports
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AuthenticationMethodsRoot]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.authentication_methods_root import AuthenticationMethodsRoot

        return await self.request_adapter.send_async(request_info, AuthenticationMethodsRoot, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property authenticationMethods for reports
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AuthenticationMethodsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Container for navigation properties for Microsoft Entra authentication methods resources.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: AuthenticationMethodsRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property authenticationMethods in reports
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
    
    def users_registered_by_feature_with_included_user_types_with_included_user_roles(self,included_user_roles: str, included_user_types: str) -> UsersRegisteredByFeatureWithIncludedUserTypesWithIncludedUserRolesRequestBuilder:
        """
        Provides operations to call the usersRegisteredByFeature method.
        param included_user_roles: Usage: includedUserRoles='{includedUserRoles}'
        param included_user_types: Usage: includedUserTypes='{includedUserTypes}'
        Returns: UsersRegisteredByFeatureWithIncludedUserTypesWithIncludedUserRolesRequestBuilder
        """
        if included_user_roles is None:
            raise TypeError("included_user_roles cannot be null.")
        if included_user_types is None:
            raise TypeError("included_user_types cannot be null.")
        from .users_registered_by_feature_with_included_user_types_with_included_user_roles.users_registered_by_feature_with_included_user_types_with_included_user_roles_request_builder import UsersRegisteredByFeatureWithIncludedUserTypesWithIncludedUserRolesRequestBuilder

        return UsersRegisteredByFeatureWithIncludedUserTypesWithIncludedUserRolesRequestBuilder(self.request_adapter, self.path_parameters, included_user_roles, included_user_types)
    
    def users_registered_by_method_with_included_user_types_with_included_user_roles(self,included_user_roles: str, included_user_types: str) -> UsersRegisteredByMethodWithIncludedUserTypesWithIncludedUserRolesRequestBuilder:
        """
        Provides operations to call the usersRegisteredByMethod method.
        param included_user_roles: Usage: includedUserRoles='{includedUserRoles}'
        param included_user_types: Usage: includedUserTypes='{includedUserTypes}'
        Returns: UsersRegisteredByMethodWithIncludedUserTypesWithIncludedUserRolesRequestBuilder
        """
        if included_user_roles is None:
            raise TypeError("included_user_roles cannot be null.")
        if included_user_types is None:
            raise TypeError("included_user_types cannot be null.")
        from .users_registered_by_method_with_included_user_types_with_included_user_roles.users_registered_by_method_with_included_user_types_with_included_user_roles_request_builder import UsersRegisteredByMethodWithIncludedUserTypesWithIncludedUserRolesRequestBuilder

        return UsersRegisteredByMethodWithIncludedUserTypesWithIncludedUserRolesRequestBuilder(self.request_adapter, self.path_parameters, included_user_roles, included_user_types)
    
    def with_url(self,raw_url: str) -> AuthenticationMethodsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AuthenticationMethodsRequestBuilder
        """
        if raw_url is None:
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
    
    @dataclass
    class AuthenticationMethodsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AuthenticationMethodsRequestBuilderGetQueryParameters():
        """
        Container for navigation properties for Microsoft Entra authentication methods resources.
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
    class AuthenticationMethodsRequestBuilderGetRequestConfiguration(RequestConfiguration[AuthenticationMethodsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AuthenticationMethodsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

