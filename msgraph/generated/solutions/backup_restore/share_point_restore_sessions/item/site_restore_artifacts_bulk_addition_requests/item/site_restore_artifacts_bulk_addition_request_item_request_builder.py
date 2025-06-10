from __future__ import annotations
from collections.abc import Callable
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
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .......models.o_data_errors.o_data_error import ODataError
    from .......models.site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest

class SiteRestoreArtifactsBulkAdditionRequestItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the siteRestoreArtifactsBulkAdditionRequests property of the microsoft.graph.sharePointRestoreSession entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SiteRestoreArtifactsBulkAdditionRequestItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/sharePointRestoreSessions/{sharePointRestoreSession%2Did}/siteRestoreArtifactsBulkAdditionRequests/{siteRestoreArtifactsBulkAdditionRequest%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete a siteRestoreArtifactsBulkAdditionRequest object associated with a sharepointRestoreSession.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/siterestoreartifactsbulkadditionrequest-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SiteRestoreArtifactsBulkAdditionRequestItemRequestBuilderGetQueryParameters]] = None) -> Optional[SiteRestoreArtifactsBulkAdditionRequest]:
        """
        Get a siteRestoreArtifactsBulkAdditionRequest object by its id, associated with a sharePointRestoreSession.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SiteRestoreArtifactsBulkAdditionRequest]
        Find more info here: https://learn.microsoft.com/graph/api/siterestoreartifactsbulkadditionrequest-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest

        return await self.request_adapter.send_async(request_info, SiteRestoreArtifactsBulkAdditionRequest, error_mapping)
    
    async def patch(self,body: SiteRestoreArtifactsBulkAdditionRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SiteRestoreArtifactsBulkAdditionRequest]:
        """
        Update the navigation property siteRestoreArtifactsBulkAdditionRequests in solutions
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SiteRestoreArtifactsBulkAdditionRequest]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest

        return await self.request_adapter.send_async(request_info, SiteRestoreArtifactsBulkAdditionRequest, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete a siteRestoreArtifactsBulkAdditionRequest object associated with a sharepointRestoreSession.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SiteRestoreArtifactsBulkAdditionRequestItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get a siteRestoreArtifactsBulkAdditionRequest object by its id, associated with a sharePointRestoreSession.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: SiteRestoreArtifactsBulkAdditionRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property siteRestoreArtifactsBulkAdditionRequests in solutions
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
    
    def with_url(self,raw_url: str) -> SiteRestoreArtifactsBulkAdditionRequestItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SiteRestoreArtifactsBulkAdditionRequestItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SiteRestoreArtifactsBulkAdditionRequestItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SiteRestoreArtifactsBulkAdditionRequestItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SiteRestoreArtifactsBulkAdditionRequestItemRequestBuilderGetQueryParameters():
        """
        Get a siteRestoreArtifactsBulkAdditionRequest object by its id, associated with a sharePointRestoreSession.
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
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class SiteRestoreArtifactsBulkAdditionRequestItemRequestBuilderGetRequestConfiguration(RequestConfiguration[SiteRestoreArtifactsBulkAdditionRequestItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SiteRestoreArtifactsBulkAdditionRequestItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

