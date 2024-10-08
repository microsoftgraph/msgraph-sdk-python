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
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.security.labels_root import LabelsRoot
    from .authorities.authorities_request_builder import AuthoritiesRequestBuilder
    from .categories.categories_request_builder import CategoriesRequestBuilder
    from .citations.citations_request_builder import CitationsRequestBuilder
    from .departments.departments_request_builder import DepartmentsRequestBuilder
    from .file_plan_references.file_plan_references_request_builder import FilePlanReferencesRequestBuilder
    from .retention_labels.retention_labels_request_builder import RetentionLabelsRequestBuilder

class LabelsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the labels property of the microsoft.graph.security entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new LabelsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/labels{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property labels for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[LabelsRequestBuilderGetQueryParameters]] = None) -> Optional[LabelsRoot]:
        """
        Get labels from security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LabelsRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.security.labels_root import LabelsRoot

        return await self.request_adapter.send_async(request_info, LabelsRoot, error_mapping)
    
    async def patch(self,body: LabelsRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[LabelsRoot]:
        """
        Update the navigation property labels in security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[LabelsRoot]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.security.labels_root import LabelsRoot

        return await self.request_adapter.send_async(request_info, LabelsRoot, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property labels for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[LabelsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get labels from security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: LabelsRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property labels in security
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
    
    def with_url(self,raw_url: str) -> LabelsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LabelsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LabelsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def authorities(self) -> AuthoritiesRequestBuilder:
        """
        Provides operations to manage the authorities property of the microsoft.graph.security.labelsRoot entity.
        """
        from .authorities.authorities_request_builder import AuthoritiesRequestBuilder

        return AuthoritiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def categories(self) -> CategoriesRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.security.labelsRoot entity.
        """
        from .categories.categories_request_builder import CategoriesRequestBuilder

        return CategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def citations(self) -> CitationsRequestBuilder:
        """
        Provides operations to manage the citations property of the microsoft.graph.security.labelsRoot entity.
        """
        from .citations.citations_request_builder import CitationsRequestBuilder

        return CitationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def departments(self) -> DepartmentsRequestBuilder:
        """
        Provides operations to manage the departments property of the microsoft.graph.security.labelsRoot entity.
        """
        from .departments.departments_request_builder import DepartmentsRequestBuilder

        return DepartmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def file_plan_references(self) -> FilePlanReferencesRequestBuilder:
        """
        Provides operations to manage the filePlanReferences property of the microsoft.graph.security.labelsRoot entity.
        """
        from .file_plan_references.file_plan_references_request_builder import FilePlanReferencesRequestBuilder

        return FilePlanReferencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retention_labels(self) -> RetentionLabelsRequestBuilder:
        """
        Provides operations to manage the retentionLabels property of the microsoft.graph.security.labelsRoot entity.
        """
        from .retention_labels.retention_labels_request_builder import RetentionLabelsRequestBuilder

        return RetentionLabelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class LabelsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class LabelsRequestBuilderGetQueryParameters():
        """
        Get labels from security
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
    class LabelsRequestBuilderGetRequestConfiguration(RequestConfiguration[LabelsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class LabelsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

