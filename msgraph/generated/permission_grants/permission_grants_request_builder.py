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
    from ..models.o_data_errors.o_data_error import ODataError
    from ..models.resource_specific_permission_grant import ResourceSpecificPermissionGrant
    from ..models.resource_specific_permission_grant_collection_response import ResourceSpecificPermissionGrantCollectionResponse
    from .delta.delta_request_builder import DeltaRequestBuilder
    from .get_available_extension_properties.get_available_extension_properties_request_builder import GetAvailableExtensionPropertiesRequestBuilder
    from .get_by_ids.get_by_ids_request_builder import GetByIdsRequestBuilder
    from .item.resource_specific_permission_grant_item_request_builder import ResourceSpecificPermissionGrantItemRequestBuilder
    from .validate_properties.validate_properties_request_builder import ValidatePropertiesRequestBuilder

class PermissionGrantsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of resourceSpecificPermissionGrant entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PermissionGrantsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/permissionGrants{?%24search,%24filter,%24orderby,%24select,%24expand}", path_parameters)
    
    def by_resource_specific_permission_grant_id(self,resource_specific_permission_grant_id: str) -> ResourceSpecificPermissionGrantItemRequestBuilder:
        """
        Provides operations to manage the collection of resourceSpecificPermissionGrant entities.
        param resource_specific_permission_grant_id: The unique identifier of resourceSpecificPermissionGrant
        Returns: ResourceSpecificPermissionGrantItemRequestBuilder
        """
        if not resource_specific_permission_grant_id:
            raise TypeError("resource_specific_permission_grant_id cannot be null.")
        from .item.resource_specific_permission_grant_item_request_builder import ResourceSpecificPermissionGrantItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["resourceSpecificPermissionGrant%2Did"] = resource_specific_permission_grant_id
        return ResourceSpecificPermissionGrantItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[PermissionGrantsRequestBuilderGetRequestConfiguration] = None) -> Optional[ResourceSpecificPermissionGrantCollectionResponse]:
        """
        Get entities from permissionGrants
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ResourceSpecificPermissionGrantCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.resource_specific_permission_grant_collection_response import ResourceSpecificPermissionGrantCollectionResponse

        return await self.request_adapter.send_async(request_info, ResourceSpecificPermissionGrantCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[ResourceSpecificPermissionGrant] = None, request_configuration: Optional[PermissionGrantsRequestBuilderPostRequestConfiguration] = None) -> Optional[ResourceSpecificPermissionGrant]:
        """
        Add new entity to permissionGrants
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ResourceSpecificPermissionGrant]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.resource_specific_permission_grant import ResourceSpecificPermissionGrant

        return await self.request_adapter.send_async(request_info, ResourceSpecificPermissionGrant, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[PermissionGrantsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get entities from permissionGrants
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
    
    def to_post_request_information(self,body: Optional[ResourceSpecificPermissionGrant] = None, request_configuration: Optional[PermissionGrantsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Add new entity to permissionGrants
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
    
    def with_url(self,raw_url: Optional[str] = None) -> PermissionGrantsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PermissionGrantsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PermissionGrantsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def delta(self) -> DeltaRequestBuilder:
        """
        Provides operations to call the delta method.
        """
        from .delta.delta_request_builder import DeltaRequestBuilder

        return DeltaRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    def validate_properties(self) -> ValidatePropertiesRequestBuilder:
        """
        Provides operations to call the validateProperties method.
        """
        from .validate_properties.validate_properties_request_builder import ValidatePropertiesRequestBuilder

        return ValidatePropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PermissionGrantsRequestBuilderGetQueryParameters():
        """
        Get entities from permissionGrants
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
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            return original_name
        
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PermissionGrantsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[PermissionGrantsRequestBuilder.PermissionGrantsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PermissionGrantsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

