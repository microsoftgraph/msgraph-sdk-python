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

o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
term = lazy_import('msgraph.generated.models.term_store.term')
children_request_builder = lazy_import('msgraph.generated.sites.item.term_store.groups.item.sets.item.terms.item.children.children_request_builder')
term_item_request_builder = lazy_import('msgraph.generated.sites.item.term_store.groups.item.sets.item.terms.item.children.item.term_item_request_builder')
relations_request_builder = lazy_import('msgraph.generated.sites.item.term_store.groups.item.sets.item.terms.item.relations.relations_request_builder')
relation_item_request_builder = lazy_import('msgraph.generated.sites.item.term_store.groups.item.sets.item.terms.item.relations.item.relation_item_request_builder')
set_request_builder = lazy_import('msgraph.generated.sites.item.term_store.groups.item.sets.item.terms.item.set.set_request_builder')

class TermItemRequestBuilder():
    """
    Provides operations to manage the terms property of the microsoft.graph.termStore.set entity.
    """
    @property
    def children(self) -> children_request_builder.ChildrenRequestBuilder:
        """
        Provides operations to manage the children property of the microsoft.graph.termStore.term entity.
        """
        return children_request_builder.ChildrenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def relations(self) -> relations_request_builder.RelationsRequestBuilder:
        """
        Provides operations to manage the relations property of the microsoft.graph.termStore.term entity.
        """
        return relations_request_builder.RelationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def set(self) -> set_request_builder.SetRequestBuilder:
        """
        Provides operations to manage the set property of the microsoft.graph.termStore.term entity.
        """
        return set_request_builder.SetRequestBuilder(self.request_adapter, self.path_parameters)
    
    def children_by_id(self,id: str) -> TermItemRequestBuilder:
        """
        Provides operations to manage the children property of the microsoft.graph.termStore.term entity.
        Args:
            id: Unique identifier of the item
        Returns: TermItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["term%2Did1"] = id
        return TermItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TermItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/sites/{site%2Did}/termStore/groups/{group%2Did}/sets/{set%2Did}/terms/{term%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[TermItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property terms for sites
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
    
    def create_get_request_information(self,request_configuration: Optional[TermItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        All the terms under the set.
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
    
    def create_patch_request_information(self,body: Optional[term.Term] = None, request_configuration: Optional[TermItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property terms in sites
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
    
    async def delete(self,request_configuration: Optional[TermItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property terms for sites
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
    
    async def get(self,request_configuration: Optional[TermItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[term.Term]:
        """
        All the terms under the set.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[term.Term]
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
        return await self.request_adapter.send_async(request_info, term.Term, response_handler, error_mapping)
    
    async def patch(self,body: Optional[term.Term] = None, request_configuration: Optional[TermItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[term.Term]:
        """
        Update the navigation property terms in sites
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[term.Term]
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
        return await self.request_adapter.send_async(request_info, term.Term, response_handler, error_mapping)
    
    def relations_by_id(self,id: str) -> relation_item_request_builder.RelationItemRequestBuilder:
        """
        Provides operations to manage the relations property of the microsoft.graph.termStore.term entity.
        Args:
            id: Unique identifier of the item
        Returns: relation_item_request_builder.RelationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["relation%2Did"] = id
        return relation_item_request_builder.RelationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class TermItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class TermItemRequestBuilderGetQueryParameters():
        """
        All the terms under the set.
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
    class TermItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TermItemRequestBuilder.TermItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class TermItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

