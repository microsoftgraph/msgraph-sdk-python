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
    from .....models.content_type import ContentType
    from .....models.o_data_errors.o_data_error import ODataError
    from .associate_with_hub_sites.associate_with_hub_sites_request_builder import AssociateWithHubSitesRequestBuilder
    from .base.base_request_builder_ import BaseRequestBuilder_
    from .base_types.base_types_request_builder import BaseTypesRequestBuilder
    from .columns.columns_request_builder import ColumnsRequestBuilder
    from .column_links.column_links_request_builder import ColumnLinksRequestBuilder
    from .column_positions.column_positions_request_builder import ColumnPositionsRequestBuilder
    from .copy_to_default_content_location.copy_to_default_content_location_request_builder import CopyToDefaultContentLocationRequestBuilder
    from .is_published.is_published_request_builder import IsPublishedRequestBuilder
    from .publish.publish_request_builder import PublishRequestBuilder
    from .unpublish.unpublish_request_builder import UnpublishRequestBuilder

class ContentTypeItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the contentTypes property of the microsoft.graph.site entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ContentTypeItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}/contentTypes/{contentType%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Remove a content type from a list or a site.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/contenttype-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ContentTypeItemRequestBuilderGetQueryParameters]] = None) -> Optional[ContentType]:
        """
        Retrieve the metadata for a content type in a site or a list.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ContentType]
        Find more info here: https://learn.microsoft.com/graph/api/contenttype-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.content_type import ContentType

        return await self.request_adapter.send_async(request_info, ContentType, error_mapping)
    
    async def patch(self,body: ContentType, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ContentType]:
        """
        Update a content type.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ContentType]
        Find more info here: https://learn.microsoft.com/graph/api/contenttype-update?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.content_type import ContentType

        return await self.request_adapter.send_async(request_info, ContentType, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Remove a content type from a list or a site.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ContentTypeItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve the metadata for a content type in a site or a list.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ContentType, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update a content type.
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
    
    def with_url(self,raw_url: str) -> ContentTypeItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ContentTypeItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ContentTypeItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def associate_with_hub_sites(self) -> AssociateWithHubSitesRequestBuilder:
        """
        Provides operations to call the associateWithHubSites method.
        """
        from .associate_with_hub_sites.associate_with_hub_sites_request_builder import AssociateWithHubSitesRequestBuilder

        return AssociateWithHubSitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def base(self) -> BaseRequestBuilder_:
        """
        Provides operations to manage the base property of the microsoft.graph.contentType entity.
        """
        from .base.base_request_builder_ import BaseRequestBuilder_

        return BaseRequestBuilder_(self.request_adapter, self.path_parameters)
    
    @property
    def base_types(self) -> BaseTypesRequestBuilder:
        """
        Provides operations to manage the baseTypes property of the microsoft.graph.contentType entity.
        """
        from .base_types.base_types_request_builder import BaseTypesRequestBuilder

        return BaseTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def column_links(self) -> ColumnLinksRequestBuilder:
        """
        Provides operations to manage the columnLinks property of the microsoft.graph.contentType entity.
        """
        from .column_links.column_links_request_builder import ColumnLinksRequestBuilder

        return ColumnLinksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def column_positions(self) -> ColumnPositionsRequestBuilder:
        """
        Provides operations to manage the columnPositions property of the microsoft.graph.contentType entity.
        """
        from .column_positions.column_positions_request_builder import ColumnPositionsRequestBuilder

        return ColumnPositionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def columns(self) -> ColumnsRequestBuilder:
        """
        Provides operations to manage the columns property of the microsoft.graph.contentType entity.
        """
        from .columns.columns_request_builder import ColumnsRequestBuilder

        return ColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def copy_to_default_content_location(self) -> CopyToDefaultContentLocationRequestBuilder:
        """
        Provides operations to call the copyToDefaultContentLocation method.
        """
        from .copy_to_default_content_location.copy_to_default_content_location_request_builder import CopyToDefaultContentLocationRequestBuilder

        return CopyToDefaultContentLocationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def is_published(self) -> IsPublishedRequestBuilder:
        """
        Provides operations to call the isPublished method.
        """
        from .is_published.is_published_request_builder import IsPublishedRequestBuilder

        return IsPublishedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def publish(self) -> PublishRequestBuilder:
        """
        Provides operations to call the publish method.
        """
        from .publish.publish_request_builder import PublishRequestBuilder

        return PublishRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unpublish(self) -> UnpublishRequestBuilder:
        """
        Provides operations to call the unpublish method.
        """
        from .unpublish.unpublish_request_builder import UnpublishRequestBuilder

        return UnpublishRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ContentTypeItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ContentTypeItemRequestBuilderGetQueryParameters():
        """
        Retrieve the metadata for a content type in a site or a list.
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
    class ContentTypeItemRequestBuilderGetRequestConfiguration(RequestConfiguration[ContentTypeItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ContentTypeItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

