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
    from ......models.workbook import Workbook
    from .application.application_request_builder import ApplicationRequestBuilder
    from .close_session.close_session_request_builder import CloseSessionRequestBuilder
    from .comments.comments_request_builder import CommentsRequestBuilder
    from .create_session.create_session_request_builder import CreateSessionRequestBuilder
    from .functions.functions_request_builder import FunctionsRequestBuilder
    from .names.names_request_builder import NamesRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .refresh_session.refresh_session_request_builder import RefreshSessionRequestBuilder
    from .session_info_resource_with_key.session_info_resource_with_key_request_builder import SessionInfoResourceWithKeyRequestBuilder
    from .tables.tables_request_builder import TablesRequestBuilder
    from .table_row_operation_result_with_key.table_row_operation_result_with_key_request_builder import TableRowOperationResultWithKeyRequestBuilder
    from .worksheets.worksheets_request_builder import WorksheetsRequestBuilder

class WorkbookRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the workbook property of the microsoft.graph.driveItem entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WorkbookRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property workbook for drives
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WorkbookRequestBuilderGetQueryParameters]] = None) -> Optional[Workbook]:
        """
        For files that are Excel spreadsheets, access to the workbook API to work with the spreadsheet's contents. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Workbook]
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
        from ......models.workbook import Workbook

        return await self.request_adapter.send_async(request_info, Workbook, error_mapping)
    
    async def patch(self,body: Workbook, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Workbook]:
        """
        Update the navigation property workbook in drives
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Workbook]
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
        from ......models.workbook import Workbook

        return await self.request_adapter.send_async(request_info, Workbook, error_mapping)
    
    def session_info_resource_with_key(self,key: str) -> SessionInfoResourceWithKeyRequestBuilder:
        """
        Provides operations to call the sessionInfoResource method.
        param key: Usage: key='{key}'
        Returns: SessionInfoResourceWithKeyRequestBuilder
        """
        if key is None:
            raise TypeError("key cannot be null.")
        from .session_info_resource_with_key.session_info_resource_with_key_request_builder import SessionInfoResourceWithKeyRequestBuilder

        return SessionInfoResourceWithKeyRequestBuilder(self.request_adapter, self.path_parameters, key)
    
    def table_row_operation_result_with_key(self,key: str) -> TableRowOperationResultWithKeyRequestBuilder:
        """
        Provides operations to call the tableRowOperationResult method.
        param key: Usage: key='{key}'
        Returns: TableRowOperationResultWithKeyRequestBuilder
        """
        if key is None:
            raise TypeError("key cannot be null.")
        from .table_row_operation_result_with_key.table_row_operation_result_with_key_request_builder import TableRowOperationResultWithKeyRequestBuilder

        return TableRowOperationResultWithKeyRequestBuilder(self.request_adapter, self.path_parameters, key)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property workbook for drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WorkbookRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        For files that are Excel spreadsheets, access to the workbook API to work with the spreadsheet's contents. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Workbook, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property workbook in drives
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
    
    def with_url(self,raw_url: str) -> WorkbookRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WorkbookRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WorkbookRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def application(self) -> ApplicationRequestBuilder:
        """
        Provides operations to manage the application property of the microsoft.graph.workbook entity.
        """
        from .application.application_request_builder import ApplicationRequestBuilder

        return ApplicationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def close_session(self) -> CloseSessionRequestBuilder:
        """
        Provides operations to call the closeSession method.
        """
        from .close_session.close_session_request_builder import CloseSessionRequestBuilder

        return CloseSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def comments(self) -> CommentsRequestBuilder:
        """
        Provides operations to manage the comments property of the microsoft.graph.workbook entity.
        """
        from .comments.comments_request_builder import CommentsRequestBuilder

        return CommentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_session(self) -> CreateSessionRequestBuilder:
        """
        Provides operations to call the createSession method.
        """
        from .create_session.create_session_request_builder import CreateSessionRequestBuilder

        return CreateSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def functions(self) -> FunctionsRequestBuilder:
        """
        Provides operations to manage the functions property of the microsoft.graph.workbook entity.
        """
        from .functions.functions_request_builder import FunctionsRequestBuilder

        return FunctionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def names(self) -> NamesRequestBuilder:
        """
        Provides operations to manage the names property of the microsoft.graph.workbook entity.
        """
        from .names.names_request_builder import NamesRequestBuilder

        return NamesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.workbook entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def refresh_session(self) -> RefreshSessionRequestBuilder:
        """
        Provides operations to call the refreshSession method.
        """
        from .refresh_session.refresh_session_request_builder import RefreshSessionRequestBuilder

        return RefreshSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tables(self) -> TablesRequestBuilder:
        """
        Provides operations to manage the tables property of the microsoft.graph.workbook entity.
        """
        from .tables.tables_request_builder import TablesRequestBuilder

        return TablesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def worksheets(self) -> WorksheetsRequestBuilder:
        """
        Provides operations to manage the worksheets property of the microsoft.graph.workbook entity.
        """
        from .worksheets.worksheets_request_builder import WorksheetsRequestBuilder

        return WorksheetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WorkbookRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WorkbookRequestBuilderGetQueryParameters():
        """
        For files that are Excel spreadsheets, access to the workbook API to work with the spreadsheet's contents. Nullable.
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
    class WorkbookRequestBuilderGetRequestConfiguration(RequestConfiguration[WorkbookRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WorkbookRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

