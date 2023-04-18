from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......models.o_data_errors import o_data_error
    from .......models.security import ediscovery_search
    from .additional_sources import additional_sources_request_builder
    from .add_to_review_set_operation import add_to_review_set_operation_request_builder
    from .custodian_sources import custodian_sources_request_builder
    from .last_estimate_statistics_operation import last_estimate_statistics_operation_request_builder
    from .noncustodial_sources import noncustodial_sources_request_builder
    from .security_estimate_statistics import security_estimate_statistics_request_builder
    from .security_purge_data import security_purge_data_request_builder

class EdiscoverySearchItemRequestBuilder():
    """
    Provides operations to manage the searches property of the microsoft.graph.security.ediscoveryCase entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EdiscoverySearchItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/searches/{ediscoverySearch%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[EdiscoverySearchItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property searches for security
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[EdiscoverySearchItemRequestBuilderGetRequestConfiguration] = None) -> Optional[ediscovery_search.EdiscoverySearch]:
        """
        Returns a list of eDiscoverySearch objects associated with this case.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ediscovery_search.EdiscoverySearch]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.security import ediscovery_search

        return await self.request_adapter.send_async(request_info, ediscovery_search.EdiscoverySearch, error_mapping)
    
    async def patch(self,body: Optional[ediscovery_search.EdiscoverySearch] = None, request_configuration: Optional[EdiscoverySearchItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[ediscovery_search.EdiscoverySearch]:
        """
        Update the navigation property searches in security
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ediscovery_search.EdiscoverySearch]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.security import ediscovery_search

        return await self.request_adapter.send_async(request_info, ediscovery_search.EdiscoverySearch, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[EdiscoverySearchItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property searches for security
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
    
    def to_get_request_information(self,request_configuration: Optional[EdiscoverySearchItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Returns a list of eDiscoverySearch objects associated with this case.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[ediscovery_search.EdiscoverySearch] = None, request_configuration: Optional[EdiscoverySearchItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property searches in security
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def additional_sources(self) -> additional_sources_request_builder.AdditionalSourcesRequestBuilder:
        """
        Provides operations to manage the additionalSources property of the microsoft.graph.security.ediscoverySearch entity.
        """
        from .additional_sources import additional_sources_request_builder

        return additional_sources_request_builder.AdditionalSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def add_to_review_set_operation(self) -> add_to_review_set_operation_request_builder.AddToReviewSetOperationRequestBuilder:
        """
        Provides operations to manage the addToReviewSetOperation property of the microsoft.graph.security.ediscoverySearch entity.
        """
        from .add_to_review_set_operation import add_to_review_set_operation_request_builder

        return add_to_review_set_operation_request_builder.AddToReviewSetOperationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custodian_sources(self) -> custodian_sources_request_builder.CustodianSourcesRequestBuilder:
        """
        Provides operations to manage the custodianSources property of the microsoft.graph.security.ediscoverySearch entity.
        """
        from .custodian_sources import custodian_sources_request_builder

        return custodian_sources_request_builder.CustodianSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_estimate_statistics_operation(self) -> last_estimate_statistics_operation_request_builder.LastEstimateStatisticsOperationRequestBuilder:
        """
        Provides operations to manage the lastEstimateStatisticsOperation property of the microsoft.graph.security.ediscoverySearch entity.
        """
        from .last_estimate_statistics_operation import last_estimate_statistics_operation_request_builder

        return last_estimate_statistics_operation_request_builder.LastEstimateStatisticsOperationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def noncustodial_sources(self) -> noncustodial_sources_request_builder.NoncustodialSourcesRequestBuilder:
        """
        Provides operations to manage the noncustodialSources property of the microsoft.graph.security.ediscoverySearch entity.
        """
        from .noncustodial_sources import noncustodial_sources_request_builder

        return noncustodial_sources_request_builder.NoncustodialSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security_estimate_statistics(self) -> security_estimate_statistics_request_builder.SecurityEstimateStatisticsRequestBuilder:
        """
        Provides operations to call the estimateStatistics method.
        """
        from .security_estimate_statistics import security_estimate_statistics_request_builder

        return security_estimate_statistics_request_builder.SecurityEstimateStatisticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security_purge_data(self) -> security_purge_data_request_builder.SecurityPurgeDataRequestBuilder:
        """
        Provides operations to call the purgeData method.
        """
        from .security_purge_data import security_purge_data_request_builder

        return security_purge_data_request_builder.SecurityPurgeDataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EdiscoverySearchItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class EdiscoverySearchItemRequestBuilderGetQueryParameters():
        """
        Returns a list of eDiscoverySearch objects associated with this case.
        """
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class EdiscoverySearchItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EdiscoverySearchItemRequestBuilder.EdiscoverySearchItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class EdiscoverySearchItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

