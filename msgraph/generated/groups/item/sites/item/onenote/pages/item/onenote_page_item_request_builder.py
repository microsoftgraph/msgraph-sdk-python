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

content_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.onenote.pages.item.content.content_request_builder')
copy_to_section_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.onenote.pages.item.copy_to_section.copy_to_section_request_builder')
onenote_patch_content_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.onenote.pages.item.onenote_patch_content.onenote_patch_content_request_builder')
parent_notebook_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.onenote.pages.item.parent_notebook.parent_notebook_request_builder')
parent_section_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.onenote.pages.item.parent_section.parent_section_request_builder')
preview_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.onenote.pages.item.preview.preview_request_builder')
onenote_page = lazy_import('msgraph.generated.models.onenote_page')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class OnenotePageItemRequestBuilder():
    """
    Provides operations to manage the pages property of the microsoft.graph.onenote entity.
    """
    @property
    def content(self) -> content_request_builder.ContentRequestBuilder:
        """
        Provides operations to manage the media for the group entity.
        """
        return content_request_builder.ContentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def copy_to_section(self) -> copy_to_section_request_builder.CopyToSectionRequestBuilder:
        """
        Provides operations to call the copyToSection method.
        """
        return copy_to_section_request_builder.CopyToSectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def onenote_patch_content(self) -> onenote_patch_content_request_builder.OnenotePatchContentRequestBuilder:
        """
        Provides operations to call the onenotePatchContent method.
        """
        return onenote_patch_content_request_builder.OnenotePatchContentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def parent_notebook(self) -> parent_notebook_request_builder.ParentNotebookRequestBuilder:
        """
        Provides operations to manage the parentNotebook property of the microsoft.graph.onenotePage entity.
        """
        return parent_notebook_request_builder.ParentNotebookRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def parent_section(self) -> parent_section_request_builder.ParentSectionRequestBuilder:
        """
        Provides operations to manage the parentSection property of the microsoft.graph.onenotePage entity.
        """
        return parent_section_request_builder.ParentSectionRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new OnenotePageItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/onenote/pages/{onenotePage%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[OnenotePageItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property pages for groups
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
    
    def create_get_request_information(self,request_configuration: Optional[OnenotePageItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
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
    
    def create_patch_request_information(self,body: Optional[onenote_page.OnenotePage] = None, request_configuration: Optional[OnenotePageItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property pages in groups
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
    
    async def delete(self,request_configuration: Optional[OnenotePageItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property pages for groups
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
    
    async def get(self,request_configuration: Optional[OnenotePageItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[onenote_page.OnenotePage]:
        """
        The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[onenote_page.OnenotePage]
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
        return await self.request_adapter.send_async(request_info, onenote_page.OnenotePage, response_handler, error_mapping)
    
    async def patch(self,body: Optional[onenote_page.OnenotePage] = None, request_configuration: Optional[OnenotePageItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[onenote_page.OnenotePage]:
        """
        Update the navigation property pages in groups
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[onenote_page.OnenotePage]
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
        return await self.request_adapter.send_async(request_info, onenote_page.OnenotePage, response_handler, error_mapping)
    
    def preview(self,) -> preview_request_builder.PreviewRequestBuilder:
        """
        Provides operations to call the preview method.
        Returns: preview_request_builder.PreviewRequestBuilder
        """
        return preview_request_builder.PreviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OnenotePageItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class OnenotePageItemRequestBuilderGetQueryParameters():
        """
        The pages in all OneNote notebooks that are owned by the user or group.  Read-only. Nullable.
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
    class OnenotePageItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[OnenotePageItemRequestBuilder.OnenotePageItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class OnenotePageItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

