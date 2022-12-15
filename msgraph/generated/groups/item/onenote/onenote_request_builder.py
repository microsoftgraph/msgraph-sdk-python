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

notebooks_request_builder = lazy_import('msgraph.generated.groups.item.onenote.notebooks.notebooks_request_builder')
notebook_item_request_builder = lazy_import('msgraph.generated.groups.item.onenote.notebooks.item.notebook_item_request_builder')
operations_request_builder = lazy_import('msgraph.generated.groups.item.onenote.operations.operations_request_builder')
onenote_operation_item_request_builder = lazy_import('msgraph.generated.groups.item.onenote.operations.item.onenote_operation_item_request_builder')
pages_request_builder = lazy_import('msgraph.generated.groups.item.onenote.pages.pages_request_builder')
onenote_page_item_request_builder = lazy_import('msgraph.generated.groups.item.onenote.pages.item.onenote_page_item_request_builder')
resources_request_builder = lazy_import('msgraph.generated.groups.item.onenote.resources.resources_request_builder')
onenote_resource_item_request_builder = lazy_import('msgraph.generated.groups.item.onenote.resources.item.onenote_resource_item_request_builder')
section_groups_request_builder = lazy_import('msgraph.generated.groups.item.onenote.section_groups.section_groups_request_builder')
section_group_item_request_builder = lazy_import('msgraph.generated.groups.item.onenote.section_groups.item.section_group_item_request_builder')
sections_request_builder = lazy_import('msgraph.generated.groups.item.onenote.sections.sections_request_builder')
onenote_section_item_request_builder = lazy_import('msgraph.generated.groups.item.onenote.sections.item.onenote_section_item_request_builder')
onenote = lazy_import('msgraph.generated.models.onenote')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class OnenoteRequestBuilder():
    """
    Provides operations to manage the onenote property of the microsoft.graph.group entity.
    """
    @property
    def notebooks(self) -> notebooks_request_builder.NotebooksRequestBuilder:
        """
        Provides operations to manage the notebooks property of the microsoft.graph.onenote entity.
        """
        return notebooks_request_builder.NotebooksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.onenote entity.
        """
        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pages(self) -> pages_request_builder.PagesRequestBuilder:
        """
        Provides operations to manage the pages property of the microsoft.graph.onenote entity.
        """
        return pages_request_builder.PagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resources(self) -> resources_request_builder.ResourcesRequestBuilder:
        """
        Provides operations to manage the resources property of the microsoft.graph.onenote entity.
        """
        return resources_request_builder.ResourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def section_groups(self) -> section_groups_request_builder.SectionGroupsRequestBuilder:
        """
        Provides operations to manage the sectionGroups property of the microsoft.graph.onenote entity.
        """
        return section_groups_request_builder.SectionGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sections(self) -> sections_request_builder.SectionsRequestBuilder:
        """
        Provides operations to manage the sections property of the microsoft.graph.onenote entity.
        """
        return sections_request_builder.SectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new OnenoteRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/onenote{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[OnenoteRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property onenote for groups
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
    
    def create_get_request_information(self,request_configuration: Optional[OnenoteRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get onenote from groups
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
    
    def create_patch_request_information(self,body: Optional[onenote.Onenote] = None, request_configuration: Optional[OnenoteRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property onenote in groups
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
    
    async def delete(self,request_configuration: Optional[OnenoteRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property onenote for groups
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
    
    async def get(self,request_configuration: Optional[OnenoteRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[onenote.Onenote]:
        """
        Get onenote from groups
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[onenote.Onenote]
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
        return await self.request_adapter.send_async(request_info, onenote.Onenote, response_handler, error_mapping)
    
    def notebooks_by_id(self,id: str) -> notebook_item_request_builder.NotebookItemRequestBuilder:
        """
        Provides operations to manage the notebooks property of the microsoft.graph.onenote entity.
        Args:
            id: Unique identifier of the item
        Returns: notebook_item_request_builder.NotebookItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["notebook%2Did"] = id
        return notebook_item_request_builder.NotebookItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def operations_by_id(self,id: str) -> onenote_operation_item_request_builder.OnenoteOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.onenote entity.
        Args:
            id: Unique identifier of the item
        Returns: onenote_operation_item_request_builder.OnenoteOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["onenoteOperation%2Did"] = id
        return onenote_operation_item_request_builder.OnenoteOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def pages_by_id(self,id: str) -> onenote_page_item_request_builder.OnenotePageItemRequestBuilder:
        """
        Provides operations to manage the pages property of the microsoft.graph.onenote entity.
        Args:
            id: Unique identifier of the item
        Returns: onenote_page_item_request_builder.OnenotePageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["onenotePage%2Did"] = id
        return onenote_page_item_request_builder.OnenotePageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[onenote.Onenote] = None, request_configuration: Optional[OnenoteRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[onenote.Onenote]:
        """
        Update the navigation property onenote in groups
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[onenote.Onenote]
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
        return await self.request_adapter.send_async(request_info, onenote.Onenote, response_handler, error_mapping)
    
    def resources_by_id(self,id: str) -> onenote_resource_item_request_builder.OnenoteResourceItemRequestBuilder:
        """
        Provides operations to manage the resources property of the microsoft.graph.onenote entity.
        Args:
            id: Unique identifier of the item
        Returns: onenote_resource_item_request_builder.OnenoteResourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["onenoteResource%2Did"] = id
        return onenote_resource_item_request_builder.OnenoteResourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def section_groups_by_id(self,id: str) -> section_group_item_request_builder.SectionGroupItemRequestBuilder:
        """
        Provides operations to manage the sectionGroups property of the microsoft.graph.onenote entity.
        Args:
            id: Unique identifier of the item
        Returns: section_group_item_request_builder.SectionGroupItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["sectionGroup%2Did"] = id
        return section_group_item_request_builder.SectionGroupItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def sections_by_id(self,id: str) -> onenote_section_item_request_builder.OnenoteSectionItemRequestBuilder:
        """
        Provides operations to manage the sections property of the microsoft.graph.onenote entity.
        Args:
            id: Unique identifier of the item
        Returns: onenote_section_item_request_builder.OnenoteSectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["onenoteSection%2Did"] = id
        return onenote_section_item_request_builder.OnenoteSectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class OnenoteRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class OnenoteRequestBuilderGetQueryParameters():
        """
        Get onenote from groups
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
    class OnenoteRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[OnenoteRequestBuilder.OnenoteRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class OnenoteRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

