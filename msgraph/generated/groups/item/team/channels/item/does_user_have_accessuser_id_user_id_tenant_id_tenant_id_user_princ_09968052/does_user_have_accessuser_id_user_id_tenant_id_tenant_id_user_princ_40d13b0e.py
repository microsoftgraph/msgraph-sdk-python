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
    from .......models.o_data_errors.o_data_error import ODataError
    from .does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_princ_db370633 import DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrinc_db370633

class DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrinc_40d13b0e(BaseRequestBuilder):
    """
    Provides operations to call the doesUserHaveAccess method. Original name: DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrincipalNameUserPrincipalNameRequestBuilder
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrinc_40d13b0e and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/team/channels/{channel%2Did}/doesUserHaveAccess(userId='@userId',tenantId='@tenantId',userPrincipalName='@userPrincipalName'){?tenantId*,userId*,userPrincipalName*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrincipalNameUserPrincipalNameRequestBuilderGetQueryParameters]] = None) -> Optional[DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrinc_db370633]:
        """
        Determine whether a user has access to a channel.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrinc_db370633]
        Find more info here: https://learn.microsoft.com/graph/api/channel-doesuserhaveaccess?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .does_user_have_accessuser_id_user_id_tenant_id_tenant_id_user_princ_db370633 import DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrinc_db370633

        return await self.request_adapter.send_async(request_info, DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrinc_db370633, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrincipalNameUserPrincipalNameRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Determine whether a user has access to a channel.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrinc_40d13b0e:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrinc_40d13b0e
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrinc_40d13b0e(self.request_adapter, raw_url)
    
    @dataclass
    class DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrincipalNameUserPrincipalNameRequestBuilderGetQueryParameters():
        """
        Determine whether a user has access to a channel.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "tenant_id":
                return "tenantId"
            if original_name == "user_id":
                return "userId"
            if original_name == "user_principal_name":
                return "userPrincipalName"
            return original_name
        
        # Usage: tenantId='@tenantId'
        tenant_id: Optional[str] = None

        # Usage: userId='@userId'
        user_id: Optional[str] = None

        # Usage: userPrincipalName='@userPrincipalName'
        user_principal_name: Optional[str] = None

    
    @dataclass
    class DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrincipalNameUserPrincipalNameRequestBuilderGetRequestConfiguration(RequestConfiguration[DoesUserHaveAccessuserIdUserIdTenantIdTenantIdUserPrincipalNameUserPrincipalNameRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

