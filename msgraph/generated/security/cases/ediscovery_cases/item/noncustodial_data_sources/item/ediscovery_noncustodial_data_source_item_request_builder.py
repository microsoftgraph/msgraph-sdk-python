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
    from .......models.security import ediscovery_noncustodial_data_source
    from .data_source import data_source_request_builder
    from .last_index_operation import last_index_operation_request_builder
    from .security_apply_hold import security_apply_hold_request_builder
    from .security_release import security_release_request_builder
    from .security_remove_hold import security_remove_hold_request_builder
    from .security_update_index import security_update_index_request_builder

class EdiscoveryNoncustodialDataSourceItemRequestBuilder():
    """
    Provides operations to manage the noncustodialDataSources property of the microsoft.graph.security.ediscoveryCase entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new EdiscoveryNoncustodialDataSourceItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/security/cases/ediscoveryCases/{ediscoveryCase%2Did}/noncustodialDataSources/{ediscoveryNoncustodialDataSource%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[EdiscoveryNoncustodialDataSourceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property noncustodialDataSources for security
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
    
    async def get(self,request_configuration: Optional[EdiscoveryNoncustodialDataSourceItemRequestBuilderGetRequestConfiguration] = None) -> Optional[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource]:
        """
        Returns a list of case ediscoveryNoncustodialDataSource objects for this case.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource]
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
        from .......models.security import ediscovery_noncustodial_data_source

        return await self.request_adapter.send_async(request_info, ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource, error_mapping)
    
    async def patch(self,body: Optional[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource] = None, request_configuration: Optional[EdiscoveryNoncustodialDataSourceItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource]:
        """
        Update the navigation property noncustodialDataSources in security
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource]
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
        from .......models.security import ediscovery_noncustodial_data_source

        return await self.request_adapter.send_async(request_info, ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[EdiscoveryNoncustodialDataSourceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property noncustodialDataSources for security
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
    
    def to_get_request_information(self,request_configuration: Optional[EdiscoveryNoncustodialDataSourceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Returns a list of case ediscoveryNoncustodialDataSource objects for this case.
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
    
    def to_patch_request_information(self,body: Optional[ediscovery_noncustodial_data_source.EdiscoveryNoncustodialDataSource] = None, request_configuration: Optional[EdiscoveryNoncustodialDataSourceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property noncustodialDataSources in security
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
    def data_source(self) -> data_source_request_builder.DataSourceRequestBuilder:
        """
        Provides operations to manage the dataSource property of the microsoft.graph.security.ediscoveryNoncustodialDataSource entity.
        """
        from .data_source import data_source_request_builder

        return data_source_request_builder.DataSourceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_index_operation(self) -> last_index_operation_request_builder.LastIndexOperationRequestBuilder:
        """
        Provides operations to manage the lastIndexOperation property of the microsoft.graph.security.ediscoveryNoncustodialDataSource entity.
        """
        from .last_index_operation import last_index_operation_request_builder

        return last_index_operation_request_builder.LastIndexOperationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security_apply_hold(self) -> security_apply_hold_request_builder.SecurityApplyHoldRequestBuilder:
        """
        Provides operations to call the applyHold method.
        """
        from .security_apply_hold import security_apply_hold_request_builder

        return security_apply_hold_request_builder.SecurityApplyHoldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security_release(self) -> security_release_request_builder.SecurityReleaseRequestBuilder:
        """
        Provides operations to call the release method.
        """
        from .security_release import security_release_request_builder

        return security_release_request_builder.SecurityReleaseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security_remove_hold(self) -> security_remove_hold_request_builder.SecurityRemoveHoldRequestBuilder:
        """
        Provides operations to call the removeHold method.
        """
        from .security_remove_hold import security_remove_hold_request_builder

        return security_remove_hold_request_builder.SecurityRemoveHoldRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def security_update_index(self) -> security_update_index_request_builder.SecurityUpdateIndexRequestBuilder:
        """
        Provides operations to call the updateIndex method.
        """
        from .security_update_index import security_update_index_request_builder

        return security_update_index_request_builder.SecurityUpdateIndexRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class EdiscoveryNoncustodialDataSourceItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class EdiscoveryNoncustodialDataSourceItemRequestBuilderGetQueryParameters():
        """
        Returns a list of case ediscoveryNoncustodialDataSource objects for this case.
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
    class EdiscoveryNoncustodialDataSourceItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[EdiscoveryNoncustodialDataSourceItemRequestBuilder.EdiscoveryNoncustodialDataSourceItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class EdiscoveryNoncustodialDataSourceItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

