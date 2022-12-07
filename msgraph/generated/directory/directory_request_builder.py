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

administrative_units_request_builder = lazy_import('msgraph.generated.directory.administrative_units.administrative_units_request_builder')
administrative_unit_item_request_builder = lazy_import('msgraph.generated.directory.administrative_units.item.administrative_unit_item_request_builder')
deleted_items_request_builder = lazy_import('msgraph.generated.directory.deleted_items.deleted_items_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.directory.deleted_items.item.directory_object_item_request_builder')
federation_configurations_request_builder = lazy_import('msgraph.generated.directory.federation_configurations.federation_configurations_request_builder')
identity_provider_base_item_request_builder = lazy_import('msgraph.generated.directory.federation_configurations.item.identity_provider_base_item_request_builder')
directory = lazy_import('msgraph.generated.models.directory')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DirectoryRequestBuilder():
    """
    Provides operations to manage the directory singleton.
    """
    def administrative_units(self) -> administrative_units_request_builder.AdministrativeUnitsRequestBuilder:
        """
        Provides operations to manage the administrativeUnits property of the microsoft.graph.directory entity.
        """
        return administrative_units_request_builder.AdministrativeUnitsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def deleted_items(self) -> deleted_items_request_builder.DeletedItemsRequestBuilder:
        """
        Provides operations to manage the deletedItems property of the microsoft.graph.directory entity.
        """
        return deleted_items_request_builder.DeletedItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def federation_configurations(self) -> federation_configurations_request_builder.FederationConfigurationsRequestBuilder:
        """
        Provides operations to manage the federationConfigurations property of the microsoft.graph.directory entity.
        """
        return federation_configurations_request_builder.FederationConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def administrative_units_by_id(self,id: str) -> administrative_unit_item_request_builder.AdministrativeUnitItemRequestBuilder:
        """
        Provides operations to manage the administrativeUnits property of the microsoft.graph.directory entity.
        Args:
            id: Unique identifier of the item
        Returns: administrative_unit_item_request_builder.AdministrativeUnitItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["administrativeUnit%2Did"] = id
        return administrative_unit_item_request_builder.AdministrativeUnitItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DirectoryRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/directory{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[DirectoryRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get directory
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
    
    def create_patch_request_information(self,body: Optional[directory.Directory] = None, request_configuration: Optional[DirectoryRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update directory
        Args:
            body: 
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
    
    def deleted_items_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the deletedItems property of the microsoft.graph.directory entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def federation_configurations_by_id(self,id: str) -> identity_provider_base_item_request_builder.IdentityProviderBaseItemRequestBuilder:
        """
        Provides operations to manage the federationConfigurations property of the microsoft.graph.directory entity.
        Args:
            id: Unique identifier of the item
        Returns: identity_provider_base_item_request_builder.IdentityProviderBaseItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["identityProviderBase%2Did"] = id
        return identity_provider_base_item_request_builder.IdentityProviderBaseItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DirectoryRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[directory.Directory]:
        """
        Get directory
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[directory.Directory]
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
        return await self.request_adapter.send_async(request_info, directory.Directory, response_handler, error_mapping)
    
    async def patch(self,body: Optional[directory.Directory] = None, request_configuration: Optional[DirectoryRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[directory.Directory]:
        """
        Update directory
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[directory.Directory]
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
        return await self.request_adapter.send_async(request_info, directory.Directory, response_handler, error_mapping)
    
    @dataclass
    class DirectoryRequestBuilderGetQueryParameters():
        """
        Get directory
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
    class DirectoryRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DirectoryRequestBuilder.DirectoryRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DirectoryRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

