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

application_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.application.application_request_builder')
comments_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.comments.comments_request_builder')
workbook_comment_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.comments.item.workbook_comment_item_request_builder')
functions_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.functions.functions_request_builder')
close_session_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.microsoft_graph_close_session.close_session_request_builder')
create_session_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.microsoft_graph_create_session.create_session_request_builder')
refresh_session_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.microsoft_graph_refresh_session.refresh_session_request_builder')
session_info_resource_with_key_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.microsoft_graph_session_info_resource_with_key.session_info_resource_with_key_request_builder')
table_row_operation_result_with_key_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.microsoft_graph_table_row_operation_result_with_key.table_row_operation_result_with_key_request_builder')
names_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.names.names_request_builder')
workbook_named_item_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.names.item.workbook_named_item_item_request_builder')
operations_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.operations.operations_request_builder')
workbook_operation_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.operations.item.workbook_operation_item_request_builder')
tables_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.tables.tables_request_builder')
workbook_table_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.tables.item.workbook_table_item_request_builder')
worksheets_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.worksheets_request_builder')
workbook_worksheet_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.worksheets.item.workbook_worksheet_item_request_builder')
workbook = lazy_import('msgraph.generated.models.workbook')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class WorkbookRequestBuilder():
    """
    Provides operations to manage the workbook property of the microsoft.graph.driveItem entity.
    """
    @property
    def application(self) -> application_request_builder.ApplicationRequestBuilder:
        """
        Provides operations to manage the application property of the microsoft.graph.workbook entity.
        """
        return application_request_builder.ApplicationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def comments(self) -> comments_request_builder.CommentsRequestBuilder:
        """
        Provides operations to manage the comments property of the microsoft.graph.workbook entity.
        """
        return comments_request_builder.CommentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def functions(self) -> functions_request_builder.FunctionsRequestBuilder:
        """
        Provides operations to manage the functions property of the microsoft.graph.workbook entity.
        """
        return functions_request_builder.FunctionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_close_session(self) -> close_session_request_builder.CloseSessionRequestBuilder:
        """
        Provides operations to call the closeSession method.
        """
        return close_session_request_builder.CloseSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_create_session(self) -> create_session_request_builder.CreateSessionRequestBuilder:
        """
        Provides operations to call the createSession method.
        """
        return create_session_request_builder.CreateSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_refresh_session(self) -> refresh_session_request_builder.RefreshSessionRequestBuilder:
        """
        Provides operations to call the refreshSession method.
        """
        return refresh_session_request_builder.RefreshSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def names(self) -> names_request_builder.NamesRequestBuilder:
        """
        Provides operations to manage the names property of the microsoft.graph.workbook entity.
        """
        return names_request_builder.NamesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.workbook entity.
        """
        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tables(self) -> tables_request_builder.TablesRequestBuilder:
        """
        Provides operations to manage the tables property of the microsoft.graph.workbook entity.
        """
        return tables_request_builder.TablesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def worksheets(self) -> worksheets_request_builder.WorksheetsRequestBuilder:
        """
        Provides operations to manage the worksheets property of the microsoft.graph.workbook entity.
        """
        return worksheets_request_builder.WorksheetsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def comments_by_id(self,id: str) -> workbook_comment_item_request_builder.WorkbookCommentItemRequestBuilder:
        """
        Provides operations to manage the comments property of the microsoft.graph.workbook entity.
        Args:
            id: Unique identifier of the item
        Returns: workbook_comment_item_request_builder.WorkbookCommentItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workbookComment%2Did"] = id
        return workbook_comment_item_request_builder.WorkbookCommentItemRequestBuilder(self.request_adapter, url_tpl_params)
    
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
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, workbook.Workbook, error_mapping)
    
    def microsoft_graph_session_info_resource_with_key(self,key: Optional[str] = None) -> session_info_resource_with_key_request_builder.SessionInfoResourceWithKeyRequestBuilder:
        """
        Provides operations to call the sessionInfoResource method.
        Args:
            key: Usage: key='{key}'
        Returns: session_info_resource_with_key_request_builder.SessionInfoResourceWithKeyRequestBuilder
        """
        if key is None:
            raise Exception("key cannot be undefined")
        return session_info_resource_with_key_request_builder.SessionInfoResourceWithKeyRequestBuilder(self.request_adapter, self.path_parameters, key)
    
    def microsoft_graph_table_row_operation_result_with_key(self,key: Optional[str] = None) -> table_row_operation_result_with_key_request_builder.TableRowOperationResultWithKeyRequestBuilder:
        """
        Provides operations to call the tableRowOperationResult method.
        Args:
            key: Usage: key='{key}'
        Returns: table_row_operation_result_with_key_request_builder.TableRowOperationResultWithKeyRequestBuilder
        """
        if key is None:
            raise Exception("key cannot be undefined")
        return table_row_operation_result_with_key_request_builder.TableRowOperationResultWithKeyRequestBuilder(self.request_adapter, self.path_parameters, key)
    
    def names_by_id(self,id: str) -> workbook_named_item_item_request_builder.WorkbookNamedItemItemRequestBuilder:
        """
        Provides operations to manage the names property of the microsoft.graph.workbook entity.
        Args:
            id: Unique identifier of the item
        Returns: workbook_named_item_item_request_builder.WorkbookNamedItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workbookNamedItem%2Did"] = id
        return workbook_named_item_item_request_builder.WorkbookNamedItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def operations_by_id(self,id: str) -> workbook_operation_item_request_builder.WorkbookOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.workbook entity.
        Args:
            id: Unique identifier of the item
        Returns: workbook_operation_item_request_builder.WorkbookOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workbookOperation%2Did"] = id
        return workbook_operation_item_request_builder.WorkbookOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
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
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, workbook.Workbook, error_mapping)
    
    def tables_by_id(self,id: str) -> workbook_table_item_request_builder.WorkbookTableItemRequestBuilder:
        """
        Provides operations to manage the tables property of the microsoft.graph.workbook entity.
        Args:
            id: Unique identifier of the item
        Returns: workbook_table_item_request_builder.WorkbookTableItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workbookTable%2Did"] = id
        return workbook_table_item_request_builder.WorkbookTableItemRequestBuilder(self.request_adapter, url_tpl_params)
    
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
        request_info.headers["Accept"] = "application/json"
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def worksheets_by_id(self,id: str) -> workbook_worksheet_item_request_builder.WorkbookWorksheetItemRequestBuilder:
        """
        Provides operations to manage the worksheets property of the microsoft.graph.workbook entity.
        Args:
            id: Unique identifier of the item
        Returns: workbook_worksheet_item_request_builder.WorkbookWorksheetItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["workbookWorksheet%2Did"] = id
        return workbook_worksheet_item_request_builder.WorkbookWorksheetItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class WorkbookRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class WorkbookRequestBuilderGetQueryParameters():
        """
        For files that are Excel spreadsheets, accesses the workbook API to work with the spreadsheet's contents. Nullable.
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
    class WorkbookRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

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
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

