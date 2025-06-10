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
    from ......models.o_data_errors.o_data_error import ODataError
    from ......models.security.file_plan_descriptor import FilePlanDescriptor
    from .authority_template.authority_template_request_builder import AuthorityTemplateRequestBuilder
    from .category_template.category_template_request_builder import CategoryTemplateRequestBuilder
    from .citation_template.citation_template_request_builder import CitationTemplateRequestBuilder
    from .department_template.department_template_request_builder import DepartmentTemplateRequestBuilder
    from .file_plan_reference_template.file_plan_reference_template_request_builder import FilePlanReferenceTemplateRequestBuilder

class DescriptorsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the descriptors property of the microsoft.graph.security.retentionLabel entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DescriptorsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/labels/retentionLabels/{retentionLabel%2Did}/descriptors{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property descriptors for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DescriptorsRequestBuilderGetQueryParameters]] = None) -> Optional[FilePlanDescriptor]:
        """
        Represents out-of-the-box values that provide more options to improve the manageability and organization of the content you need to label.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FilePlanDescriptor]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.security.file_plan_descriptor import FilePlanDescriptor

        return await self.request_adapter.send_async(request_info, FilePlanDescriptor, error_mapping)
    
    async def patch(self,body: FilePlanDescriptor, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FilePlanDescriptor]:
        """
        Update the navigation property descriptors in security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FilePlanDescriptor]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.security.file_plan_descriptor import FilePlanDescriptor

        return await self.request_adapter.send_async(request_info, FilePlanDescriptor, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property descriptors for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DescriptorsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Represents out-of-the-box values that provide more options to improve the manageability and organization of the content you need to label.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: FilePlanDescriptor, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property descriptors in security
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
    
    def with_url(self,raw_url: str) -> DescriptorsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DescriptorsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DescriptorsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def authority_template(self) -> AuthorityTemplateRequestBuilder:
        """
        Provides operations to manage the authorityTemplate property of the microsoft.graph.security.filePlanDescriptor entity.
        """
        from .authority_template.authority_template_request_builder import AuthorityTemplateRequestBuilder

        return AuthorityTemplateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def category_template(self) -> CategoryTemplateRequestBuilder:
        """
        Provides operations to manage the categoryTemplate property of the microsoft.graph.security.filePlanDescriptor entity.
        """
        from .category_template.category_template_request_builder import CategoryTemplateRequestBuilder

        return CategoryTemplateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def citation_template(self) -> CitationTemplateRequestBuilder:
        """
        Provides operations to manage the citationTemplate property of the microsoft.graph.security.filePlanDescriptor entity.
        """
        from .citation_template.citation_template_request_builder import CitationTemplateRequestBuilder

        return CitationTemplateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def department_template(self) -> DepartmentTemplateRequestBuilder:
        """
        Provides operations to manage the departmentTemplate property of the microsoft.graph.security.filePlanDescriptor entity.
        """
        from .department_template.department_template_request_builder import DepartmentTemplateRequestBuilder

        return DepartmentTemplateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def file_plan_reference_template(self) -> FilePlanReferenceTemplateRequestBuilder:
        """
        Provides operations to manage the filePlanReferenceTemplate property of the microsoft.graph.security.filePlanDescriptor entity.
        """
        from .file_plan_reference_template.file_plan_reference_template_request_builder import FilePlanReferenceTemplateRequestBuilder

        return FilePlanReferenceTemplateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DescriptorsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DescriptorsRequestBuilderGetQueryParameters():
        """
        Represents out-of-the-box values that provide more options to improve the manageability and organization of the content you need to label.
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
    class DescriptorsRequestBuilderGetRequestConfiguration(RequestConfiguration[DescriptorsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DescriptorsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

