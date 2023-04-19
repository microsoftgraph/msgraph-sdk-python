from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import resource_specific_permission_grant, resource_specific_permission_grant_collection_response
    from ....models.o_data_errors import o_data_error
    from .count import count_request_builder
    from .delta import delta_request_builder
    from .get_available_extension_properties import get_available_extension_properties_request_builder
    from .get_by_ids import get_by_ids_request_builder
    from .item import resource_specific_permission_grant_item_request_builder
    from .validate_properties import validate_properties_request_builder

class PermissionGrantsRequestBuilder():
    """
    Provides operations to manage the permissionGrants property of the microsoft.graph.group entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PermissionGrantsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/permissionGrants{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def by_resource_specific_permission_grant_id(self,resource_specific_permission_grant_id: str) -> resource_specific_permission_grant_item_request_builder.ResourceSpecificPermissionGrantItemRequestBuilder:
        """
        Provides operations to manage the permissionGrants property of the microsoft.graph.group entity.
        Args:
            resource_specific_permission_grant_id: Unique identifier of the item
        Returns: resource_specific_permission_grant_item_request_builder.ResourceSpecificPermissionGrantItemRequestBuilder
        """
        if resource_specific_permission_grant_id is None:
            raise Exception("resource_specific_permission_grant_id cannot be undefined")
        from .item import resource_specific_permission_grant_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["resourceSpecificPermissionGrant%2Did"] = resource_specific_permission_grant_id
        return resource_specific_permission_grant_item_request_builder.ResourceSpecificPermissionGrantItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[PermissionGrantsRequestBuilderGetRequestConfiguration] = None) -> Optional[resource_specific_permission_grant_collection_response.ResourceSpecificPermissionGrantCollectionResponse]:
        """
        List all resource-specific permission grants on the group. This list specifies the Azure AD apps that have access to the **group**, along with the corresponding kind of resource-specific access that each app has.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[resource_specific_permission_grant_collection_response.ResourceSpecificPermissionGrantCollectionResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import resource_specific_permission_grant_collection_response

        return await self.request_adapter.send_async(request_info, resource_specific_permission_grant_collection_response.ResourceSpecificPermissionGrantCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[resource_specific_permission_grant.ResourceSpecificPermissionGrant] = None, request_configuration: Optional[PermissionGrantsRequestBuilderPostRequestConfiguration] = None) -> Optional[resource_specific_permission_grant.ResourceSpecificPermissionGrant]:
        """
        Create new navigation property to permissionGrants for groups
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[resource_specific_permission_grant.ResourceSpecificPermissionGrant]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import resource_specific_permission_grant

        return await self.request_adapter.send_async(request_info, resource_specific_permission_grant.ResourceSpecificPermissionGrant, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[PermissionGrantsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        List all resource-specific permission grants on the group. This list specifies the Azure AD apps that have access to the **group**, along with the corresponding kind of resource-specific access that each app has.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_post_request_information(self,body: Optional[resource_specific_permission_grant.ResourceSpecificPermissionGrant] = None, request_configuration: Optional[PermissionGrantsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create new navigation property to permissionGrants for groups
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
        request_info.http_method = Method.POST
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def count(self) -> count_request_builder.CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count import count_request_builder

        return count_request_builder.CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delta(self) -> delta_request_builder.DeltaRequestBuilder:
        """
        Provides operations to call the delta method.
        """
        from .delta import delta_request_builder

        return delta_request_builder.DeltaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_available_extension_properties(self) -> get_available_extension_properties_request_builder.GetAvailableExtensionPropertiesRequestBuilder:
        """
        Provides operations to call the getAvailableExtensionProperties method.
        """
        from .get_available_extension_properties import get_available_extension_properties_request_builder

        return get_available_extension_properties_request_builder.GetAvailableExtensionPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_by_ids(self) -> get_by_ids_request_builder.GetByIdsRequestBuilder:
        """
        Provides operations to call the getByIds method.
        """
        from .get_by_ids import get_by_ids_request_builder

        return get_by_ids_request_builder.GetByIdsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate_properties(self) -> validate_properties_request_builder.ValidatePropertiesRequestBuilder:
        """
        Provides operations to call the validateProperties method.
        """
        from .validate_properties import validate_properties_request_builder

        return validate_properties_request_builder.ValidatePropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PermissionGrantsRequestBuilderGetQueryParameters():
        """
        List all resource-specific permission grants on the group. This list specifies the Azure AD apps that have access to the **group**, along with the corresponding kind of resource-specific access that each app has.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
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

    
    @dataclass
    class PermissionGrantsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[PermissionGrantsRequestBuilder.PermissionGrantsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class PermissionGrantsRequestBuilderPostRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

