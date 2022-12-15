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

content_type = lazy_import('msgraph.generated.models.content_type')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
associate_with_hub_sites_request_builder = lazy_import('msgraph.generated.sites.item.content_types.item.associate_with_hub_sites.associate_with_hub_sites_request_builder')
base_request_builder = lazy_import('msgraph.generated.sites.item.content_types.item.base.base_request_builder')
base_types_request_builder = lazy_import('msgraph.generated.sites.item.content_types.item.base_types.base_types_request_builder')
content_type_item_request_builder = lazy_import('msgraph.generated.sites.item.content_types.item.base_types.item.content_type_item_request_builder')
column_links_request_builder = lazy_import('msgraph.generated.sites.item.content_types.item.column_links.column_links_request_builder')
column_link_item_request_builder = lazy_import('msgraph.generated.sites.item.content_types.item.column_links.item.column_link_item_request_builder')
column_positions_request_builder = lazy_import('msgraph.generated.sites.item.content_types.item.column_positions.column_positions_request_builder')
column_definition_item_request_builder = lazy_import('msgraph.generated.sites.item.content_types.item.column_positions.item.column_definition_item_request_builder')
columns_request_builder = lazy_import('msgraph.generated.sites.item.content_types.item.columns.columns_request_builder')
column_definition_item_request_builder = lazy_import('msgraph.generated.sites.item.content_types.item.columns.item.column_definition_item_request_builder')
copy_to_default_content_location_request_builder = lazy_import('msgraph.generated.sites.item.content_types.item.copy_to_default_content_location.copy_to_default_content_location_request_builder')
is_published_request_builder = lazy_import('msgraph.generated.sites.item.content_types.item.is_published.is_published_request_builder')
publish_request_builder = lazy_import('msgraph.generated.sites.item.content_types.item.publish.publish_request_builder')
unpublish_request_builder = lazy_import('msgraph.generated.sites.item.content_types.item.unpublish.unpublish_request_builder')

class ContentTypeItemRequestBuilder():
    """
    Provides operations to manage the contentTypes property of the microsoft.graph.site entity.
    """
    @property
    def associate_with_hub_sites(self) -> associate_with_hub_sites_request_builder.AssociateWithHubSitesRequestBuilder:
        """
        Provides operations to call the associateWithHubSites method.
        """
        return associate_with_hub_sites_request_builder.AssociateWithHubSitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def base(self) -> base_request_builder.BaseRequestBuilder:
        """
        Provides operations to manage the base property of the microsoft.graph.contentType entity.
        """
        return base_request_builder.BaseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def base_types(self) -> base_types_request_builder.BaseTypesRequestBuilder:
        """
        Provides operations to manage the baseTypes property of the microsoft.graph.contentType entity.
        """
        return base_types_request_builder.BaseTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def column_links(self) -> column_links_request_builder.ColumnLinksRequestBuilder:
        """
        Provides operations to manage the columnLinks property of the microsoft.graph.contentType entity.
        """
        return column_links_request_builder.ColumnLinksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def column_positions(self) -> column_positions_request_builder.ColumnPositionsRequestBuilder:
        """
        Provides operations to manage the columnPositions property of the microsoft.graph.contentType entity.
        """
        return column_positions_request_builder.ColumnPositionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def columns(self) -> columns_request_builder.ColumnsRequestBuilder:
        """
        Provides operations to manage the columns property of the microsoft.graph.contentType entity.
        """
        return columns_request_builder.ColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def copy_to_default_content_location(self) -> copy_to_default_content_location_request_builder.CopyToDefaultContentLocationRequestBuilder:
        """
        Provides operations to call the copyToDefaultContentLocation method.
        """
        return copy_to_default_content_location_request_builder.CopyToDefaultContentLocationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def publish(self) -> publish_request_builder.PublishRequestBuilder:
        """
        Provides operations to call the publish method.
        """
        return publish_request_builder.PublishRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unpublish(self) -> unpublish_request_builder.UnpublishRequestBuilder:
        """
        Provides operations to call the unpublish method.
        """
        return unpublish_request_builder.UnpublishRequestBuilder(self.request_adapter, self.path_parameters)
    
    def base_types_by_id(self,id: str) -> ContentTypeItemRequestBuilder:
        """
        Provides operations to manage the baseTypes property of the microsoft.graph.contentType entity.
        Args:
            id: Unique identifier of the item
        Returns: ContentTypeItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["contentType%2Did1"] = id
        return ContentTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def column_links_by_id(self,id: str) -> column_link_item_request_builder.ColumnLinkItemRequestBuilder:
        """
        Provides operations to manage the columnLinks property of the microsoft.graph.contentType entity.
        Args:
            id: Unique identifier of the item
        Returns: column_link_item_request_builder.ColumnLinkItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["columnLink%2Did"] = id
        return column_link_item_request_builder.ColumnLinkItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def column_positions_by_id(self,id: str) -> column_definition_item_request_builder.ColumnDefinitionItemRequestBuilder:
        """
        Provides operations to manage the columnPositions property of the microsoft.graph.contentType entity.
        Args:
            id: Unique identifier of the item
        Returns: column_definition_item_request_builder.ColumnDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["columnDefinition%2Did"] = id
        return column_definition_item_request_builder.ColumnDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def columns_by_id(self,id: str) -> column_definition_item_request_builder.ColumnDefinitionItemRequestBuilder:
        """
        Provides operations to manage the columns property of the microsoft.graph.contentType entity.
        Args:
            id: Unique identifier of the item
        Returns: column_definition_item_request_builder.ColumnDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["columnDefinition%2Did"] = id
        return column_definition_item_request_builder.ColumnDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ContentTypeItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/sites/{site%2Did}/contentTypes/{contentType%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[ContentTypeItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property contentTypes for sites
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
    
    def create_get_request_information(self,request_configuration: Optional[ContentTypeItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The collection of content types defined for this site.
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
    
    def create_patch_request_information(self,body: Optional[content_type.ContentType] = None, request_configuration: Optional[ContentTypeItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property contentTypes in sites
        Args:
            body: The request body
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
    
    async def delete(self,request_configuration: Optional[ContentTypeItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property contentTypes for sites
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
    
    async def get(self,request_configuration: Optional[ContentTypeItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[content_type.ContentType]:
        """
        The collection of content types defined for this site.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[content_type.ContentType]
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
        return await self.request_adapter.send_async(request_info, content_type.ContentType, response_handler, error_mapping)
    
    def is_published(self,) -> is_published_request_builder.IsPublishedRequestBuilder:
        """
        Provides operations to call the isPublished method.
        Returns: is_published_request_builder.IsPublishedRequestBuilder
        """
        return is_published_request_builder.IsPublishedRequestBuilder(self.request_adapter, self.path_parameters)
    
    async def patch(self,body: Optional[content_type.ContentType] = None, request_configuration: Optional[ContentTypeItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[content_type.ContentType]:
        """
        Update the navigation property contentTypes in sites
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[content_type.ContentType]
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
        return await self.request_adapter.send_async(request_info, content_type.ContentType, response_handler, error_mapping)
    
    @dataclass
    class ContentTypeItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ContentTypeItemRequestBuilderGetQueryParameters():
        """
        The collection of content types defined for this site.
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
    class ContentTypeItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ContentTypeItemRequestBuilder.ContentTypeItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ContentTypeItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

