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

o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
ediscovery_case = lazy_import('msgraph.generated.models.security.ediscovery_case')
close_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.close.close_request_builder')
custodians_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.custodians.custodians_request_builder')
ediscovery_custodian_item_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.custodians.item.ediscovery_custodian_item_request_builder')
noncustodial_data_sources_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.noncustodial_data_sources.noncustodial_data_sources_request_builder')
ediscovery_noncustodial_data_source_item_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.noncustodial_data_sources.item.ediscovery_noncustodial_data_source_item_request_builder')
operations_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.operations.operations_request_builder')
case_operation_item_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.operations.item.case_operation_item_request_builder')
reopen_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.reopen.reopen_request_builder')
review_sets_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.review_sets.review_sets_request_builder')
ediscovery_review_set_item_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.review_sets.item.ediscovery_review_set_item_request_builder')
searches_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.searches.searches_request_builder')
ediscovery_search_item_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.searches.item.ediscovery_search_item_request_builder')
settings_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.settings.settings_request_builder')
tags_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.tags.tags_request_builder')
ediscovery_review_tag_item_request_builder = lazy_import('msgraph.generated.security.cases.ediscovery_cases.item.tags.item.ediscovery_review_tag_item_request_builder')

class EdiscoveryCaseItemRequestBuilder():
    """
    Provides operations to manage the ediscoveryCases property of the microsoft.graph.security.casesRoot entity.
    """
    def close(self) -> close_request_builder.CloseRequestBuilder:
        """
        Provides operations to call the close method.
        """
        return close_request_builder.CloseRequestBuilder(self.request_adapter, self.path_parameters)
    
    def custodians(self) -> custodians_request_builder.CustodiansRequestBuilder:
        """
        Provides operations to manage the custodians property of the microsoft.graph.security.ediscoveryCase entity.
        """
        return custodians_request_builder.CustodiansRequestBuilder(self.request_adapter, self.path_parameters)
    
    def noncustodial_data_sources(self) -> noncustodial_data_sources_request_builder.NoncustodialDataSourcesRequestBuilder:
        """
        Provides operations to manage the noncustodialDataSources property of the microsoft.graph.security.ediscoveryCase entity.
        """
        return noncustodial_data_sources_request_builder.NoncustodialDataSourcesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.security.ediscoveryCase entity.
        """
        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def reopen(self) -> reopen_request_builder.ReopenRequestBuilder:
        """
        Provides operations to call the reopen method.
        """
        return reopen_request_builder.ReopenRequestBuilder(self.request_adapter, self.path_parameters)
    
    def review_sets(self) -> review_sets_request_builder.ReviewSetsRequestBuilder:
        """
        Provides operations to manage the reviewSets property of the microsoft.graph.security.ediscoveryCase entity.
        """
        return review_sets_request_builder.ReviewSetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def searches(self) -> searches_request_builder.SearchesRequestBuilder:
        """
        Provides operations to manage the searches property of the microsoft.graph.security.ediscoveryCase entity.
        """
        return searches_request_builder.SearchesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def settings(self) -> settings_request_builder.SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.security.ediscoveryCase entity.
        """
        return settings_request_builder.SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def tags(self) -> tags_request_builder.TagsRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.security.ediscoveryCase entity.
        """
        return tags_request_builder.TagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EdiscoveryCaseItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[EdiscoveryCaseItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property ediscoveryCases for security
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
    
    def create_get_request_information(self,request_configuration: Optional[EdiscoveryCaseItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get ediscoveryCases from security
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
    
    def create_patch_request_information(self,body: Optional[ediscovery_case.EdiscoveryCase] = None, request_configuration: Optional[EdiscoveryCaseItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property ediscoveryCases in security
        Args:
            body: 
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
    
    def custodians_by_id(self,id: str) -> ediscovery_custodian_item_request_builder.EdiscoveryCustodianItemRequestBuilder:
        """
        Provides operations to manage the custodians property of the microsoft.graph.security.ediscoveryCase entity.
        Args:
            id: Unique identifier of the item
        Returns: ediscovery_custodian_item_request_builder.EdiscoveryCustodianItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ediscoveryCustodian%2Did"] = id
        return ediscovery_custodian_item_request_builder.EdiscoveryCustodianItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[EdiscoveryCaseItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property ediscoveryCases for security
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
    
    async def get(self,request_configuration: Optional[EdiscoveryCaseItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[ediscovery_case.EdiscoveryCase]:
        """
        Get ediscoveryCases from security
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[ediscovery_case.EdiscoveryCase]
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
        return await self.request_adapter.send_async(request_info, ediscovery_case.EdiscoveryCase, response_handler, error_mapping)
    
    def noncustodial_data_sources_by_id(self,id: str) -> ediscovery_noncustodial_data_source_item_request_builder.EdiscoveryNoncustodialDataSourceItemRequestBuilder:
        """
        Provides operations to manage the noncustodialDataSources property of the microsoft.graph.security.ediscoveryCase entity.
        Args:
            id: Unique identifier of the item
        Returns: ediscovery_noncustodial_data_source_item_request_builder.EdiscoveryNoncustodialDataSourceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ediscoveryNoncustodialDataSource%2Did"] = id
        return ediscovery_noncustodial_data_source_item_request_builder.EdiscoveryNoncustodialDataSourceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def operations_by_id(self,id: str) -> case_operation_item_request_builder.CaseOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.security.ediscoveryCase entity.
        Args:
            id: Unique identifier of the item
        Returns: case_operation_item_request_builder.CaseOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["caseOperation%2Did"] = id
        return case_operation_item_request_builder.CaseOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[ediscovery_case.EdiscoveryCase] = None, request_configuration: Optional[EdiscoveryCaseItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[ediscovery_case.EdiscoveryCase]:
        """
        Update the navigation property ediscoveryCases in security
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[ediscovery_case.EdiscoveryCase]
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
        return await self.request_adapter.send_async(request_info, ediscovery_case.EdiscoveryCase, response_handler, error_mapping)
    
    def review_sets_by_id(self,id: str) -> ediscovery_review_set_item_request_builder.EdiscoveryReviewSetItemRequestBuilder:
        """
        Provides operations to manage the reviewSets property of the microsoft.graph.security.ediscoveryCase entity.
        Args:
            id: Unique identifier of the item
        Returns: ediscovery_review_set_item_request_builder.EdiscoveryReviewSetItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ediscoveryReviewSet%2Did"] = id
        return ediscovery_review_set_item_request_builder.EdiscoveryReviewSetItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def searches_by_id(self,id: str) -> ediscovery_search_item_request_builder.EdiscoverySearchItemRequestBuilder:
        """
        Provides operations to manage the searches property of the microsoft.graph.security.ediscoveryCase entity.
        Args:
            id: Unique identifier of the item
        Returns: ediscovery_search_item_request_builder.EdiscoverySearchItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ediscoverySearch%2Did"] = id
        return ediscovery_search_item_request_builder.EdiscoverySearchItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def tags_by_id(self,id: str) -> ediscovery_review_tag_item_request_builder.EdiscoveryReviewTagItemRequestBuilder:
        """
        Provides operations to manage the tags property of the microsoft.graph.security.ediscoveryCase entity.
        Args:
            id: Unique identifier of the item
        Returns: ediscovery_review_tag_item_request_builder.EdiscoveryReviewTagItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ediscoveryReviewTag%2Did"] = id
        return ediscovery_review_tag_item_request_builder.EdiscoveryReviewTagItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class EdiscoveryCaseItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class EdiscoveryCaseItemRequestBuilderGetQueryParameters():
        """
        Get ediscoveryCases from security
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
    class EdiscoveryCaseItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EdiscoveryCaseItemRequestBuilder.EdiscoveryCaseItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class EdiscoveryCaseItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

