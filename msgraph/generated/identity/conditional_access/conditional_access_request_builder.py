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

authentication_context_class_references_request_builder = lazy_import('msgraph.generated.identity.conditional_access.authentication_context_class_references.authentication_context_class_references_request_builder')
authentication_context_class_reference_item_request_builder = lazy_import('msgraph.generated.identity.conditional_access.authentication_context_class_references.item.authentication_context_class_reference_item_request_builder')
named_locations_request_builder = lazy_import('msgraph.generated.identity.conditional_access.named_locations.named_locations_request_builder')
named_location_item_request_builder = lazy_import('msgraph.generated.identity.conditional_access.named_locations.item.named_location_item_request_builder')
policies_request_builder = lazy_import('msgraph.generated.identity.conditional_access.policies.policies_request_builder')
conditional_access_policy_item_request_builder = lazy_import('msgraph.generated.identity.conditional_access.policies.item.conditional_access_policy_item_request_builder')
templates_request_builder = lazy_import('msgraph.generated.identity.conditional_access.templates.templates_request_builder')
conditional_access_template_item_request_builder = lazy_import('msgraph.generated.identity.conditional_access.templates.item.conditional_access_template_item_request_builder')
conditional_access_root = lazy_import('msgraph.generated.models.conditional_access_root')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class ConditionalAccessRequestBuilder():
    """
    Provides operations to manage the conditionalAccess property of the microsoft.graph.identityContainer entity.
    """
    def authentication_context_class_references(self) -> authentication_context_class_references_request_builder.AuthenticationContextClassReferencesRequestBuilder:
        """
        Provides operations to manage the authenticationContextClassReferences property of the microsoft.graph.conditionalAccessRoot entity.
        """
        return authentication_context_class_references_request_builder.AuthenticationContextClassReferencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def named_locations(self) -> named_locations_request_builder.NamedLocationsRequestBuilder:
        """
        Provides operations to manage the namedLocations property of the microsoft.graph.conditionalAccessRoot entity.
        """
        return named_locations_request_builder.NamedLocationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def policies(self) -> policies_request_builder.PoliciesRequestBuilder:
        """
        Provides operations to manage the policies property of the microsoft.graph.conditionalAccessRoot entity.
        """
        return policies_request_builder.PoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def templates(self) -> templates_request_builder.TemplatesRequestBuilder:
        """
        Provides operations to manage the templates property of the microsoft.graph.conditionalAccessRoot entity.
        """
        return templates_request_builder.TemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def authentication_context_class_references_by_id(self,id: str) -> authentication_context_class_reference_item_request_builder.AuthenticationContextClassReferenceItemRequestBuilder:
        """
        Provides operations to manage the authenticationContextClassReferences property of the microsoft.graph.conditionalAccessRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: authentication_context_class_reference_item_request_builder.AuthenticationContextClassReferenceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["authenticationContextClassReference%2Did"] = id
        return authentication_context_class_reference_item_request_builder.AuthenticationContextClassReferenceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ConditionalAccessRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identity/conditionalAccess{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[ConditionalAccessRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property conditionalAccess for identity
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
    
    def create_get_request_information(self,request_configuration: Optional[ConditionalAccessRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        the entry point for the Conditional Access (CA) object model.
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
    
    def create_patch_request_information(self,body: Optional[conditional_access_root.ConditionalAccessRoot] = None, request_configuration: Optional[ConditionalAccessRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property conditionalAccess in identity
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
    
    async def delete(self,request_configuration: Optional[ConditionalAccessRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property conditionalAccess for identity
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
    
    async def get(self,request_configuration: Optional[ConditionalAccessRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[conditional_access_root.ConditionalAccessRoot]:
        """
        the entry point for the Conditional Access (CA) object model.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[conditional_access_root.ConditionalAccessRoot]
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
        return await self.request_adapter.send_async(request_info, conditional_access_root.ConditionalAccessRoot, response_handler, error_mapping)
    
    def named_locations_by_id(self,id: str) -> named_location_item_request_builder.NamedLocationItemRequestBuilder:
        """
        Provides operations to manage the namedLocations property of the microsoft.graph.conditionalAccessRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: named_location_item_request_builder.NamedLocationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["namedLocation%2Did"] = id
        return named_location_item_request_builder.NamedLocationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[conditional_access_root.ConditionalAccessRoot] = None, request_configuration: Optional[ConditionalAccessRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[conditional_access_root.ConditionalAccessRoot]:
        """
        Update the navigation property conditionalAccess in identity
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[conditional_access_root.ConditionalAccessRoot]
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
        return await self.request_adapter.send_async(request_info, conditional_access_root.ConditionalAccessRoot, response_handler, error_mapping)
    
    def policies_by_id(self,id: str) -> conditional_access_policy_item_request_builder.ConditionalAccessPolicyItemRequestBuilder:
        """
        Provides operations to manage the policies property of the microsoft.graph.conditionalAccessRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: conditional_access_policy_item_request_builder.ConditionalAccessPolicyItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["conditionalAccessPolicy%2Did"] = id
        return conditional_access_policy_item_request_builder.ConditionalAccessPolicyItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def templates_by_id(self,id: str) -> conditional_access_template_item_request_builder.ConditionalAccessTemplateItemRequestBuilder:
        """
        Provides operations to manage the templates property of the microsoft.graph.conditionalAccessRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: conditional_access_template_item_request_builder.ConditionalAccessTemplateItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["conditionalAccessTemplate%2Did"] = id
        return conditional_access_template_item_request_builder.ConditionalAccessTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class ConditionalAccessRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ConditionalAccessRequestBuilderGetQueryParameters():
        """
        the entry point for the Conditional Access (CA) object model.
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
    class ConditionalAccessRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ConditionalAccessRequestBuilder.ConditionalAccessRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ConditionalAccessRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

