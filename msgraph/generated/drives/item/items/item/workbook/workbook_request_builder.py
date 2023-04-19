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
    from ......models import workbook
    from ......models.o_data_errors import o_data_error
    from .application import application_request_builder
    from .close_session import close_session_request_builder
    from .comments import comments_request_builder
    from .create_session import create_session_request_builder
    from .functions import functions_request_builder
    from .names import names_request_builder
    from .operations import operations_request_builder
    from .refresh_session import refresh_session_request_builder
    from .session_info_resource_with_key import session_info_resource_with_key_request_builder
    from .table_row_operation_result_with_key import table_row_operation_result_with_key_request_builder
    from .tables import tables_request_builder
    from .worksheets import worksheets_request_builder

class WorkbookRequestBuilder():
    """
    Provides operations to manage the workbook property of the microsoft.graph.driveItem entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new WorkbookRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[WorkbookRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property workbook for drives
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[WorkbookRequestBuilderGetRequestConfiguration] = None) -> Optional[workbook.Workbook]:
        """
        For files that are Excel spreadsheets, accesses the workbook API to work with the spreadsheet's contents. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook.Workbook]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import workbook

        return await self.request_adapter.send_async(request_info, workbook.Workbook, error_mapping)
    
    async def patch(self,body: Optional[workbook.Workbook] = None, request_configuration: Optional[WorkbookRequestBuilderPatchRequestConfiguration] = None) -> Optional[workbook.Workbook]:
        """
        Update the navigation property workbook in drives
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[workbook.Workbook]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import workbook

        return await self.request_adapter.send_async(request_info, workbook.Workbook, error_mapping)
    
    def session_info_resource_with_key(self,key: Optional[str] = None) -> session_info_resource_with_key_request_builder.SessionInfoResourceWithKeyRequestBuilder:
        """
        Provides operations to call the sessionInfoResource method.
        Args:
            key: Usage: key='{key}'
        Returns: session_info_resource_with_key_request_builder.SessionInfoResourceWithKeyRequestBuilder
        """
        if key is None:
            raise Exception("key cannot be undefined")
        from .session_info_resource_with_key import session_info_resource_with_key_request_builder

        return session_info_resource_with_key_request_builder.SessionInfoResourceWithKeyRequestBuilder(self.request_adapter, self.path_parameters, key)
    
    def table_row_operation_result_with_key(self,key: Optional[str] = None) -> table_row_operation_result_with_key_request_builder.TableRowOperationResultWithKeyRequestBuilder:
        """
        Provides operations to call the tableRowOperationResult method.
        Args:
            key: Usage: key='{key}'
        Returns: table_row_operation_result_with_key_request_builder.TableRowOperationResultWithKeyRequestBuilder
        """
        if key is None:
            raise Exception("key cannot be undefined")
        from .table_row_operation_result_with_key import table_row_operation_result_with_key_request_builder

        return table_row_operation_result_with_key_request_builder.TableRowOperationResultWithKeyRequestBuilder(self.request_adapter, self.path_parameters, key)
    
    def to_delete_request_information(self,request_configuration: Optional[WorkbookRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property workbook for drives
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
    
    def to_get_request_information(self,request_configuration: Optional[WorkbookRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        For files that are Excel spreadsheets, accesses the workbook API to work with the spreadsheet's contents. Nullable.
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
    
    def to_patch_request_information(self,body: Optional[workbook.Workbook] = None, request_configuration: Optional[WorkbookRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property workbook in drives
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
    def application(self) -> application_request_builder.ApplicationRequestBuilder:
        """
        Provides operations to manage the application property of the microsoft.graph.workbook entity.
        """
        from .application import application_request_builder

        return application_request_builder.ApplicationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def close_session(self) -> close_session_request_builder.CloseSessionRequestBuilder:
        """
        Provides operations to call the closeSession method.
        """
        from .close_session import close_session_request_builder

        return close_session_request_builder.CloseSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def comments(self) -> comments_request_builder.CommentsRequestBuilder:
        """
        Provides operations to manage the comments property of the microsoft.graph.workbook entity.
        """
        from .comments import comments_request_builder

        return comments_request_builder.CommentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_session(self) -> create_session_request_builder.CreateSessionRequestBuilder:
        """
        Provides operations to call the createSession method.
        """
        from .create_session import create_session_request_builder

        return create_session_request_builder.CreateSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def functions(self) -> functions_request_builder.FunctionsRequestBuilder:
        """
        Provides operations to manage the functions property of the microsoft.graph.workbook entity.
        """
        from .functions import functions_request_builder

        return functions_request_builder.FunctionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def names(self) -> names_request_builder.NamesRequestBuilder:
        """
        Provides operations to manage the names property of the microsoft.graph.workbook entity.
        """
        from .names import names_request_builder

        return names_request_builder.NamesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.workbook entity.
        """
        from .operations import operations_request_builder

        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def refresh_session(self) -> refresh_session_request_builder.RefreshSessionRequestBuilder:
        """
        Provides operations to call the refreshSession method.
        """
        from .refresh_session import refresh_session_request_builder

        return refresh_session_request_builder.RefreshSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tables(self) -> tables_request_builder.TablesRequestBuilder:
        """
        Provides operations to manage the tables property of the microsoft.graph.workbook entity.
        """
        from .tables import tables_request_builder

        return tables_request_builder.TablesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def worksheets(self) -> worksheets_request_builder.WorksheetsRequestBuilder:
        """
        Provides operations to manage the worksheets property of the microsoft.graph.workbook entity.
        """
        from .worksheets import worksheets_request_builder

        return worksheets_request_builder.WorksheetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WorkbookRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class WorkbookRequestBuilderGetQueryParameters():
        """
        For files that are Excel spreadsheets, accesses the workbook API to work with the spreadsheet's contents. Nullable.
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
    class WorkbookRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[WorkbookRequestBuilder.WorkbookRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class WorkbookRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

