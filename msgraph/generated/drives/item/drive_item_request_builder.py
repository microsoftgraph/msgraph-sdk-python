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
    from ...models.drive import Drive
    from ...models.o_data_errors.o_data_error import ODataError
    from .bundles.bundles_request_builder import BundlesRequestBuilder
    from .created_by_user.created_by_user_request_builder import CreatedByUserRequestBuilder
    from .following.following_request_builder import FollowingRequestBuilder
    from .items.items_request_builder import ItemsRequestBuilder
    from .last_modified_by_user.last_modified_by_user_request_builder import LastModifiedByUserRequestBuilder
    from .list_.list_request_builder import ListRequestBuilder
    from .recent.recent_request_builder import RecentRequestBuilder
    from .root.root_request_builder import RootRequestBuilder
    from .search_with_q.search_with_q_request_builder import SearchWithQRequestBuilder
    from .shared_with_me.shared_with_me_request_builder import SharedWithMeRequestBuilder
    from .special.special_request_builder import SpecialRequestBuilder

class DriveItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of drive entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DriveItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete entity from drives
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DriveItemRequestBuilderGetQueryParameters]] = None) -> Optional[Drive]:
        """
        Get entity from drives by key
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Drive]
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
        from ...models.drive import Drive

        return await self.request_adapter.send_async(request_info, Drive, error_mapping)
    
    async def patch(self,body: Drive, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Drive]:
        """
        Update entity in drives
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Drive]
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
        from ...models.drive import Drive

        return await self.request_adapter.send_async(request_info, Drive, error_mapping)
    
    def search_with_q(self,q: str) -> SearchWithQRequestBuilder:
        """
        Provides operations to call the search method.
        param q: Usage: q='{q}'
        Returns: SearchWithQRequestBuilder
        """
        if q is None:
            raise TypeError("q cannot be null.")
        from .search_with_q.search_with_q_request_builder import SearchWithQRequestBuilder

        return SearchWithQRequestBuilder(self.request_adapter, self.path_parameters, q)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete entity from drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DriveItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get entity from drives by key
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Drive, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update entity in drives
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
    
    def with_url(self,raw_url: str) -> DriveItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DriveItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DriveItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bundles(self) -> BundlesRequestBuilder:
        """
        Provides operations to manage the bundles property of the microsoft.graph.drive entity.
        """
        from .bundles.bundles_request_builder import BundlesRequestBuilder

        return BundlesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def created_by_user(self) -> CreatedByUserRequestBuilder:
        """
        Provides operations to manage the createdByUser property of the microsoft.graph.baseItem entity.
        """
        from .created_by_user.created_by_user_request_builder import CreatedByUserRequestBuilder

        return CreatedByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def following(self) -> FollowingRequestBuilder:
        """
        Provides operations to manage the following property of the microsoft.graph.drive entity.
        """
        from .following.following_request_builder import FollowingRequestBuilder

        return FollowingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def items(self) -> ItemsRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.drive entity.
        """
        from .items.items_request_builder import ItemsRequestBuilder

        return ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_modified_by_user(self) -> LastModifiedByUserRequestBuilder:
        """
        Provides operations to manage the lastModifiedByUser property of the microsoft.graph.baseItem entity.
        """
        from .last_modified_by_user.last_modified_by_user_request_builder import LastModifiedByUserRequestBuilder

        return LastModifiedByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def list_(self) -> ListRequestBuilder:
        """
        Provides operations to manage the list property of the microsoft.graph.drive entity.
        """
        from .list_.list_request_builder import ListRequestBuilder

        return ListRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recent(self) -> RecentRequestBuilder:
        """
        Provides operations to call the recent method.
        """
        from .recent.recent_request_builder import RecentRequestBuilder

        return RecentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def root(self) -> RootRequestBuilder:
        """
        Provides operations to manage the root property of the microsoft.graph.drive entity.
        """
        from .root.root_request_builder import RootRequestBuilder

        return RootRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def shared_with_me(self) -> SharedWithMeRequestBuilder:
        """
        Provides operations to call the sharedWithMe method.
        """
        from .shared_with_me.shared_with_me_request_builder import SharedWithMeRequestBuilder

        return SharedWithMeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def special(self) -> SpecialRequestBuilder:
        """
        Provides operations to manage the special property of the microsoft.graph.drive entity.
        """
        from .special.special_request_builder import SpecialRequestBuilder

        return SpecialRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DriveItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DriveItemRequestBuilderGetQueryParameters():
        """
        Get entity from drives by key
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
    class DriveItemRequestBuilderGetRequestConfiguration(RequestConfiguration[DriveItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DriveItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

