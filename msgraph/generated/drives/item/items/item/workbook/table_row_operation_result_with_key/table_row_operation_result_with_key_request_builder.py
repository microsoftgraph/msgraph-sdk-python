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
    from .......models.workbook_table_row import WorkbookTableRow

class TableRowOperationResultWithKeyRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the tableRowOperationResult method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]], key: Optional[str] = None) -> None:
        """
        Instantiates a new TableRowOperationResultWithKeyRequestBuilder and sets the default values.
        param key: Usage: key='{key}'
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['key'] = key
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}/workbook/tableRowOperationResult(key='{key}')", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WorkbookTableRow]:
        """
        This function is the last in a series of steps to create a workbookTableRow resource asynchronously. A best practice to create multiple table rows is to batch them in one create tableRow operation and carry out the operation asynchronously. An asynchronous request to create table rows involves the following steps:1. Issue an async Create tableRow request and get the query URL returned in the Location response header.2. Use the query URL returned from step 1 to issue the Get workbookOperation request and get the operation ID for step 3.     Alternatively, for convenience, after you get a succeeded operationStatus result, you can get the query URL from the resourceLocation property of the workbookOperation returned in the response, and apply the query URL to step 3. 3. Use the query URL returned from step 2 as the GET request URL for this function tableRowOperationResult. A successful function call returns the new table rows in a workbookTableRow resource. This function does not do anything if called independently.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WorkbookTableRow]
        Find more info here: https://learn.microsoft.com/graph/api/workbook-tablerowoperationresult?view=graph-rest-1.0
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
        from .......models.workbook_table_row import WorkbookTableRow

        return await self.request_adapter.send_async(request_info, WorkbookTableRow, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        This function is the last in a series of steps to create a workbookTableRow resource asynchronously. A best practice to create multiple table rows is to batch them in one create tableRow operation and carry out the operation asynchronously. An asynchronous request to create table rows involves the following steps:1. Issue an async Create tableRow request and get the query URL returned in the Location response header.2. Use the query URL returned from step 1 to issue the Get workbookOperation request and get the operation ID for step 3.     Alternatively, for convenience, after you get a succeeded operationStatus result, you can get the query URL from the resourceLocation property of the workbookOperation returned in the response, and apply the query URL to step 3. 3. Use the query URL returned from step 2 as the GET request URL for this function tableRowOperationResult. A successful function call returns the new table rows in a workbookTableRow resource. This function does not do anything if called independently.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> TableRowOperationResultWithKeyRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TableRowOperationResultWithKeyRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TableRowOperationResultWithKeyRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class TableRowOperationResultWithKeyRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

