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
    from .....models.o_data_errors.o_data_error import ODataError
    from .....models.scoped_role_membership import ScopedRoleMembership
    from .....models.scoped_role_membership_collection_response import ScopedRoleMembershipCollectionResponse
    from .count.count_request_builder import CountRequestBuilder
    from .item.scoped_role_membership_item_request_builder import ScopedRoleMembershipItemRequestBuilder

class ScopedRoleMembersRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the scopedRoleMembers property of the microsoft.graph.administrativeUnit entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ScopedRoleMembersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/directory/administrativeUnits/{administrativeUnit%2Did}/scopedRoleMembers{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}", path_parameters)
    
    def by_scoped_role_membership_id(self,scoped_role_membership_id: str) -> ScopedRoleMembershipItemRequestBuilder:
        """
        Provides operations to manage the scopedRoleMembers property of the microsoft.graph.administrativeUnit entity.
        param scoped_role_membership_id: The unique identifier of scopedRoleMembership
        Returns: ScopedRoleMembershipItemRequestBuilder
        """
        if not scoped_role_membership_id:
            raise TypeError("scoped_role_membership_id cannot be null.")
        from .item.scoped_role_membership_item_request_builder import ScopedRoleMembershipItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["scopedRoleMembership%2Did"] = scoped_role_membership_id
        return ScopedRoleMembershipItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ScopedRoleMembersRequestBuilderGetRequestConfiguration] = None) -> Optional[ScopedRoleMembershipCollectionResponse]:
        """
        List Microsoft Entra role assignments with administrative unit scope.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ScopedRoleMembershipCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/administrativeunit-list-scopedrolemembers?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.scoped_role_membership_collection_response import ScopedRoleMembershipCollectionResponse

        return await self.request_adapter.send_async(request_info, ScopedRoleMembershipCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[ScopedRoleMembership] = None, request_configuration: Optional[ScopedRoleMembersRequestBuilderPostRequestConfiguration] = None) -> Optional[ScopedRoleMembership]:
        """
        Assign a Microsoft Entra role with administrative unit scope. For a list of roles that can be assigned with administrative unit scope, see Assign Microsoft Entra roles with administrative unit scope.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ScopedRoleMembership]
        Find more info here: https://learn.microsoft.com/graph/api/administrativeunit-post-scopedrolemembers?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.scoped_role_membership import ScopedRoleMembership

        return await self.request_adapter.send_async(request_info, ScopedRoleMembership, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[ScopedRoleMembersRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        List Microsoft Entra role assignments with administrative unit scope.
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
    
    def to_post_request_information(self,body: Optional[ScopedRoleMembership] = None, request_configuration: Optional[ScopedRoleMembersRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Assign a Microsoft Entra role with administrative unit scope. For a list of roles that can be assigned with administrative unit scope, see Assign Microsoft Entra roles with administrative unit scope.
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
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ScopedRoleMembersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ScopedRoleMembersRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ScopedRoleMembersRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ScopedRoleMembersRequestBuilderGetQueryParameters():
        """
        List Microsoft Entra role assignments with administrative unit scope.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ScopedRoleMembersRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[ScopedRoleMembersRequestBuilder.ScopedRoleMembersRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class ScopedRoleMembersRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

