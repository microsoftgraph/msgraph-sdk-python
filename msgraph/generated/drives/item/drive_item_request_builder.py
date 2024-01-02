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
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DriveItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[DriveItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete entity from drives
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
    
    async def get(self,request_configuration: Optional[DriveItemRequestBuilderGetRequestConfiguration] = None) -> Optional[Drive]:
        """
        Get entity from drives by key
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Drive]
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
        from ...models.drive import Drive

        return await self.request_adapter.send_async(request_info, Drive, error_mapping)
    
    async def patch(self,body: Optional[Drive] = None, request_configuration: Optional[DriveItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[Drive]:
        """
        Update entity in drives
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Drive]
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
        from ...models.drive import Drive

        return await self.request_adapter.send_async(request_info, Drive, error_mapping)
    
    def search_with_q(self,q: Optional[str] = None) -> SearchWithQRequestBuilder:
        """
        Provides operations to call the search method.
        param q: Usage: q='{q}'
        Returns: SearchWithQRequestBuilder
        """
        if not q:
            raise TypeError("q cannot be null.")
        from .search_with_q.search_with_q_request_builder import SearchWithQRequestBuilder

        return SearchWithQRequestBuilder(self.request_adapter, self.path_parameters, q)
    
    def to_delete_request_information(self,request_configuration: Optional[DriveItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete entity from drives
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
    
    def to_get_request_information(self,request_configuration: Optional[DriveItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get entity from drives by key
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
    
    def to_patch_request_information(self,body: Optional[Drive] = None, request_configuration: Optional[DriveItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update entity in drives
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
    
    def with_url(self,raw_url: Optional[str] = None) -> DriveItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DriveItemRequestBuilder
        """
        if not raw_url:
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
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DriveItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class DriveItemRequestBuilderGetQueryParameters():
        """
        Get entity from drives by key
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
    class DriveItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[DriveItemRequestBuilder.DriveItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DriveItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

