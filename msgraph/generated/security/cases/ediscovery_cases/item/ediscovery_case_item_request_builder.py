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
    from .....models.o_data_errors.o_data_error import ODataError
    from .....models.security.ediscovery_case import EdiscoveryCase
    from .case_members.case_members_request_builder import CaseMembersRequestBuilder
    from .custodians.custodians_request_builder import CustodiansRequestBuilder
    from .microsoft_graph_security_close.microsoft_graph_security_close_request_builder import MicrosoftGraphSecurityCloseRequestBuilder
    from .microsoft_graph_security_reopen.microsoft_graph_security_reopen_request_builder import MicrosoftGraphSecurityReopenRequestBuilder
    from .noncustodial_data_sources.noncustodial_data_sources_request_builder import NoncustodialDataSourcesRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .review_sets.review_sets_request_builder import ReviewSetsRequestBuilder
    from .searches.searches_request_builder import SearchesRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder
    from .tags.tags_request_builder import TagsRequestBuilder

class EdiscoveryCaseItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the ediscoveryCases property of the microsoft.graph.security.casesRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EdiscoveryCaseItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete an ediscoveryCase object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/security-casesroot-delete-ediscoverycases?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[EdiscoveryCaseItemRequestBuilderGetQueryParameters]] = None) -> Optional[EdiscoveryCase]:
        """
        Read the properties and relationships of an ediscoveryCase object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EdiscoveryCase]
        Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycase-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.security.ediscovery_case import EdiscoveryCase

        return await self.request_adapter.send_async(request_info, EdiscoveryCase, error_mapping)
    
    async def patch(self,body: EdiscoveryCase, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EdiscoveryCase]:
        """
        Update the properties of an ediscoveryCase object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EdiscoveryCase]
        Find more info here: https://learn.microsoft.com/graph/api/security-ediscoverycase-update?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.security.ediscovery_case import EdiscoveryCase

        return await self.request_adapter.send_async(request_info, EdiscoveryCase, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete an ediscoveryCase object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[EdiscoveryCaseItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read the properties and relationships of an ediscoveryCase object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: EdiscoveryCase, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of an ediscoveryCase object.
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
    
    def with_url(self,raw_url: str) -> EdiscoveryCaseItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: EdiscoveryCaseItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return EdiscoveryCaseItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def case_members(self) -> CaseMembersRequestBuilder:
        """
        Provides operations to manage the caseMembers property of the microsoft.graph.security.ediscoveryCase entity.
        """
        from .case_members.case_members_request_builder import CaseMembersRequestBuilder

        return CaseMembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custodians(self) -> CustodiansRequestBuilder:
        """
        Provides operations to manage the custodians property of the microsoft.graph.security.ediscoveryCase entity.
        """
        from .custodians.custodians_request_builder import CustodiansRequestBuilder

        return CustodiansRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_close(self) -> MicrosoftGraphSecurityCloseRequestBuilder:
        """
        Provides operations to call the close method.
        """
        from .microsoft_graph_security_close.microsoft_graph_security_close_request_builder import MicrosoftGraphSecurityCloseRequestBuilder

        return MicrosoftGraphSecurityCloseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_security_reopen(self) -> MicrosoftGraphSecurityReopenRequestBuilder:
        """
        Provides operations to call the reopen method.
        """
        from .microsoft_graph_security_reopen.microsoft_graph_security_reopen_request_builder import MicrosoftGraphSecurityReopenRequestBuilder

        return MicrosoftGraphSecurityReopenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def noncustodial_data_sources(self) -> NoncustodialDataSourcesRequestBuilder:
        """
        Provides operations to manage the noncustodialDataSources property of the microsoft.graph.security.ediscoveryCase entity.
        """
        from .noncustodial_data_sources.noncustodial_data_sources_request_builder import NoncustodialDataSourcesRequestBuilder

        return NoncustodialDataSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.security.ediscoveryCase entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def review_sets(self) -> ReviewSetsRequestBuilder:
        """
        Provides operations to manage the reviewSets property of the microsoft.graph.security.ediscoveryCase entity.
        """
        from .review_sets.review_sets_request_builder import ReviewSetsRequestBuilder

        return ReviewSetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def searches(self) -> SearchesRequestBuilder:
        """
        Provides operations to manage the searches property of the microsoft.graph.security.ediscoveryCase entity.
        """
        from .searches.searches_request_builder import SearchesRequestBuilder

        return SearchesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.security.ediscoveryCase entity.
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tags(self) -> TagsRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.security.ediscoveryCase entity.
        """
        from .tags.tags_request_builder import TagsRequestBuilder

        return TagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EdiscoveryCaseItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EdiscoveryCaseItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of an ediscoveryCase object.
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
    class EdiscoveryCaseItemRequestBuilderGetRequestConfiguration(RequestConfiguration[EdiscoveryCaseItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class EdiscoveryCaseItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

