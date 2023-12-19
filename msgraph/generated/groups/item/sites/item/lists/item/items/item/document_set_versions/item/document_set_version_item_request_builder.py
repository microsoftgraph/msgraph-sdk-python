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
    from ...........models.document_set_version import DocumentSetVersion
    from ...........models.o_data_errors.o_data_error import ODataError
    from .fields.fields_request_builder import FieldsRequestBuilder
    from .restore.restore_request_builder import RestoreRequestBuilder

class DocumentSetVersionItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the documentSetVersions property of the microsoft.graph.listItem entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DocumentSetVersionItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/lists/{list%2Did}/items/{listItem%2Did}/documentSetVersions/{documentSetVersion%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[DocumentSetVersionItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete a version of a document set in a list.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/documentsetversion-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[DocumentSetVersionItemRequestBuilderGetRequestConfiguration] = None) -> Optional[DocumentSetVersion]:
        """
        Read the properties and relationships of a documentSetVersion object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DocumentSetVersion]
        Find more info here: https://learn.microsoft.com/graph/api/documentsetversion-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...........models.document_set_version import DocumentSetVersion

        return await self.request_adapter.send_async(request_info, DocumentSetVersion, error_mapping)
    
    async def patch(self,body: Optional[DocumentSetVersion] = None, request_configuration: Optional[DocumentSetVersionItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[DocumentSetVersion]:
        """
        Update the navigation property documentSetVersions in groups
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DocumentSetVersion]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...........models.document_set_version import DocumentSetVersion

        return await self.request_adapter.send_async(request_info, DocumentSetVersion, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[DocumentSetVersionItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete a version of a document set in a list.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[DocumentSetVersionItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of a documentSetVersion object.
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
    
    def to_patch_request_information(self,body: Optional[DocumentSetVersion] = None, request_configuration: Optional[DocumentSetVersionItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property documentSetVersions in groups
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
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> DocumentSetVersionItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DocumentSetVersionItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return DocumentSetVersionItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def fields(self) -> FieldsRequestBuilder:
        """
        Provides operations to manage the fields property of the microsoft.graph.listItemVersion entity.
        """
        from .fields.fields_request_builder import FieldsRequestBuilder

        return FieldsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore.restore_request_builder import RestoreRequestBuilder

        return RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DocumentSetVersionItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class DocumentSetVersionItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a documentSetVersion object.
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
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DocumentSetVersionItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[DocumentSetVersionItemRequestBuilder.DocumentSetVersionItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DocumentSetVersionItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

