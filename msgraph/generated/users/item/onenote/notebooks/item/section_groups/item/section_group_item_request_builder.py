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
    from ........models.section_group import SectionGroup
    from .parent_notebook.parent_notebook_request_builder import ParentNotebookRequestBuilder
    from .parent_section_group.parent_section_group_request_builder import ParentSectionGroupRequestBuilder
    from .sections.sections_request_builder import SectionsRequestBuilder
    from .section_groups.section_groups_request_builder import SectionGroupsRequestBuilder

class SectionGroupItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the sectionGroups property of the microsoft.graph.notebook entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new SectionGroupItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/onenote/notebooks/{notebook%2Did}/sectionGroups/{sectionGroup%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property sectionGroups for users
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SectionGroupItemRequestBuilderGetQueryParameters]] = None) -> Optional[SectionGroup]:
        """
        The section groups in the notebook. Read-only. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SectionGroup]
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
        from ........models.section_group import SectionGroup

        return await self.request_adapter.send_async(request_info, SectionGroup, error_mapping)
    
    async def patch(self,body: SectionGroup, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SectionGroup]:
        """
        Update the navigation property sectionGroups in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SectionGroup]
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
        from ........models.section_group import SectionGroup

        return await self.request_adapter.send_async(request_info, SectionGroup, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property sectionGroups for users
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SectionGroupItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The section groups in the notebook. Read-only. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: SectionGroup, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property sectionGroups in users
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
    
    def with_url(self,raw_url: str) -> SectionGroupItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SectionGroupItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SectionGroupItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def parent_notebook(self) -> ParentNotebookRequestBuilder:
        """
        Provides operations to manage the parentNotebook property of the microsoft.graph.sectionGroup entity.
        """
        from .parent_notebook.parent_notebook_request_builder import ParentNotebookRequestBuilder

        return ParentNotebookRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def parent_section_group(self) -> ParentSectionGroupRequestBuilder:
        """
        Provides operations to manage the parentSectionGroup property of the microsoft.graph.sectionGroup entity.
        """
        from .parent_section_group.parent_section_group_request_builder import ParentSectionGroupRequestBuilder

        return ParentSectionGroupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def section_groups(self) -> SectionGroupsRequestBuilder:
        """
        Provides operations to manage the sectionGroups property of the microsoft.graph.sectionGroup entity.
        """
        from .section_groups.section_groups_request_builder import SectionGroupsRequestBuilder

        return SectionGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sections(self) -> SectionsRequestBuilder:
        """
        Provides operations to manage the sections property of the microsoft.graph.sectionGroup entity.
        """
        from .sections.sections_request_builder import SectionsRequestBuilder

        return SectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SectionGroupItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SectionGroupItemRequestBuilderGetQueryParameters():
        """
        The section groups in the notebook. Read-only. Nullable.
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
    class SectionGroupItemRequestBuilderGetRequestConfiguration(RequestConfiguration[SectionGroupItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SectionGroupItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

