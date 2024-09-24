from __future__ import annotations
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
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ........models.o_data_errors.o_data_error import ODataError
    from ........models.term_store.set import Set
    from .children.children_request_builder import ChildrenRequestBuilder
    from .parent_group.parent_group_request_builder import ParentGroupRequestBuilder
    from .relations.relations_request_builder import RelationsRequestBuilder
    from .terms.terms_request_builder import TermsRequestBuilder

class SetItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the sets property of the microsoft.graph.termStore.store entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new SetItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/termStore/sets/{set%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property sets for groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SetItemRequestBuilderGetQueryParameters]] = None) -> Optional[Set]:
        """
        Collection of all sets available in the term store. This relationship can only be used to load a specific term set.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Set]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.term_store.set import Set

        return await self.request_adapter.send_async(request_info, Set, error_mapping)
    
    async def patch(self,body: Set, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Set]:
        """
        Update the navigation property sets in groups
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Set]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ........models.term_store.set import Set

        return await self.request_adapter.send_async(request_info, Set, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property sets for groups
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SetItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Collection of all sets available in the term store. This relationship can only be used to load a specific term set.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Set, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property sets in groups
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
    
    def with_url(self,raw_url: str) -> SetItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SetItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SetItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def children(self) -> ChildrenRequestBuilder:
        """
        Provides operations to manage the children property of the microsoft.graph.termStore.set entity.
        """
        from .children.children_request_builder import ChildrenRequestBuilder

        return ChildrenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def parent_group(self) -> ParentGroupRequestBuilder:
        """
        Provides operations to manage the parentGroup property of the microsoft.graph.termStore.set entity.
        """
        from .parent_group.parent_group_request_builder import ParentGroupRequestBuilder

        return ParentGroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def relations(self) -> RelationsRequestBuilder:
        """
        Provides operations to manage the relations property of the microsoft.graph.termStore.set entity.
        """
        from .relations.relations_request_builder import RelationsRequestBuilder

        return RelationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def terms(self) -> TermsRequestBuilder:
        """
        Provides operations to manage the terms property of the microsoft.graph.termStore.set entity.
        """
        from .terms.terms_request_builder import TermsRequestBuilder

        return TermsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SetItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SetItemRequestBuilderGetQueryParameters():
        """
        Collection of all sets available in the term store. This relationship can only be used to load a specific term set.
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
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class SetItemRequestBuilderGetRequestConfiguration(RequestConfiguration[SetItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SetItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

