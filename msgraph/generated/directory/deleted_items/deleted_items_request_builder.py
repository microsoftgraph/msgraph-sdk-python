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
    from ...models.directory_object_collection_response import DirectoryObjectCollectionResponse
    from ...models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .get_available_extension_properties.get_available_extension_properties_request_builder import GetAvailableExtensionPropertiesRequestBuilder
    from .get_by_ids.get_by_ids_request_builder import GetByIdsRequestBuilder
    from .graph_administrative_unit.graph_administrative_unit_request_builder import GraphAdministrativeUnitRequestBuilder
    from .graph_application.graph_application_request_builder import GraphApplicationRequestBuilder
    from .graph_device.graph_device_request_builder import GraphDeviceRequestBuilder
    from .graph_group.graph_group_request_builder import GraphGroupRequestBuilder
    from .graph_service_principal.graph_service_principal_request_builder import GraphServicePrincipalRequestBuilder
    from .graph_user.graph_user_request_builder import GraphUserRequestBuilder
    from .item.directory_object_item_request_builder import DirectoryObjectItemRequestBuilder
    from .validate_properties.validate_properties_request_builder import ValidatePropertiesRequestBuilder

class DeletedItemsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the deletedItems property of the microsoft.graph.directory entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DeletedItemsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/directory/deletedItems{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_directory_object_id(self,directory_object_id: str) -> DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the deletedItems property of the microsoft.graph.directory entity.
        param directory_object_id: The unique identifier of directoryObject
        Returns: DirectoryObjectItemRequestBuilder
        """
        if directory_object_id is None:
            raise TypeError("directory_object_id cannot be null.")
        from .item.directory_object_item_request_builder import DirectoryObjectItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = directory_object_id
        return DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DeletedItemsRequestBuilderGetQueryParameters]] = None) -> Optional[DirectoryObjectCollectionResponse]:
        """
        Retrieve the properties of a recently deleted application, group, servicePrincipal, administrative unit, or user object from deleted items. Retrieve the properties of a recently deleted directory object from deleted items. The following types are supported:- administrativeUnit- application- certificateBasedAuthPki- certificateAuthorityDetail- group- servicePrincipal- user
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DirectoryObjectCollectionResponse]
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
        from ...models.directory_object_collection_response import DirectoryObjectCollectionResponse

        return await self.request_adapter.send_async(request_info, DirectoryObjectCollectionResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DeletedItemsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve the properties of a recently deleted application, group, servicePrincipal, administrative unit, or user object from deleted items. Retrieve the properties of a recently deleted directory object from deleted items. The following types are supported:- administrativeUnit- application- certificateBasedAuthPki- certificateAuthorityDetail- group- servicePrincipal- user
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> DeletedItemsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DeletedItemsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DeletedItemsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_available_extension_properties(self) -> GetAvailableExtensionPropertiesRequestBuilder:
        """
        Provides operations to call the getAvailableExtensionProperties method.
        """
        from .get_available_extension_properties.get_available_extension_properties_request_builder import GetAvailableExtensionPropertiesRequestBuilder

        return GetAvailableExtensionPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_by_ids(self) -> GetByIdsRequestBuilder:
        """
        Provides operations to call the getByIds method.
        """
        from .get_by_ids.get_by_ids_request_builder import GetByIdsRequestBuilder

        return GetByIdsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_administrative_unit(self) -> GraphAdministrativeUnitRequestBuilder:
        """
        Casts the previous resource to administrativeUnit.
        """
        from .graph_administrative_unit.graph_administrative_unit_request_builder import GraphAdministrativeUnitRequestBuilder

        return GraphAdministrativeUnitRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_application(self) -> GraphApplicationRequestBuilder:
        """
        Casts the previous resource to application.
        """
        from .graph_application.graph_application_request_builder import GraphApplicationRequestBuilder

        return GraphApplicationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_device(self) -> GraphDeviceRequestBuilder:
        """
        Casts the previous resource to device.
        """
        from .graph_device.graph_device_request_builder import GraphDeviceRequestBuilder

        return GraphDeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_group(self) -> GraphGroupRequestBuilder:
        """
        Casts the previous resource to group.
        """
        from .graph_group.graph_group_request_builder import GraphGroupRequestBuilder

        return GraphGroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_service_principal(self) -> GraphServicePrincipalRequestBuilder:
        """
        Casts the previous resource to servicePrincipal.
        """
        from .graph_service_principal.graph_service_principal_request_builder import GraphServicePrincipalRequestBuilder

        return GraphServicePrincipalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_user(self) -> GraphUserRequestBuilder:
        """
        Casts the previous resource to user.
        """
        from .graph_user.graph_user_request_builder import GraphUserRequestBuilder

        return GraphUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate_properties(self) -> ValidatePropertiesRequestBuilder:
        """
        Provides operations to call the validateProperties method.
        """
        from .validate_properties.validate_properties_request_builder import ValidatePropertiesRequestBuilder

        return ValidatePropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DeletedItemsRequestBuilderGetQueryParameters():
        """
        Retrieve the properties of a recently deleted application, group, servicePrincipal, administrative unit, or user object from deleted items. Retrieve the properties of a recently deleted directory object from deleted items. The following types are supported:- administrativeUnit- application- certificateBasedAuthPki- certificateAuthorityDetail- group- servicePrincipal- user
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
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
        expand: Optional[list[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[list[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class DeletedItemsRequestBuilderGetRequestConfiguration(RequestConfiguration[DeletedItemsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

