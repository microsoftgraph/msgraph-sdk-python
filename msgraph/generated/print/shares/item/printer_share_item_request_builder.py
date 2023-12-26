from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.printer_share import PrinterShare
    from .allowed_groups.allowed_groups_request_builder import AllowedGroupsRequestBuilder
    from .allowed_users.allowed_users_request_builder import AllowedUsersRequestBuilder
    from .jobs.jobs_request_builder import JobsRequestBuilder
    from .printer.printer_request_builder import PrinterRequestBuilder

class PrinterShareItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the shares property of the microsoft.graph.print entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new PrinterShareItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/print/shares/{printerShare%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[PrinterShareItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete a printer share (unshare the associated printer). This action can't be undone. If the printer is shared again in the future, any Windows users who had previously installed the printer needs to discover and reinstall it.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/printershare-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[PrinterShareItemRequestBuilderGetRequestConfiguration] = None) -> Optional[PrinterShare]:
        """
        Retrieve the properties and relationships of a printer share.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PrinterShare]
        Find more info here: https://learn.microsoft.com/graph/api/printershare-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.printer_share import PrinterShare

        return await self.request_adapter.send_async(request_info, PrinterShare, error_mapping)
    
    async def patch(self,body: Optional[PrinterShare] = None, request_configuration: Optional[PrinterShareItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[PrinterShare]:
        """
        Update the properties of a printer share. This method can be used to swap printers. For example, if a physical printer device breaks, an administrator can register a new printer device and update this printerShare to point to the new printer without requiring users to take any action.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PrinterShare]
        Find more info here: https://learn.microsoft.com/graph/api/printershare-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.printer_share import PrinterShare

        return await self.request_adapter.send_async(request_info, PrinterShare, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[PrinterShareItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete a printer share (unshare the associated printer). This action can't be undone. If the printer is shared again in the future, any Windows users who had previously installed the printer needs to discover and reinstall it.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[PrinterShareItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a printer share.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[PrinterShare] = None, request_configuration: Optional[PrinterShareItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a printer share. This method can be used to swap printers. For example, if a physical printer device breaks, an administrator can register a new printer device and update this printerShare to point to the new printer without requiring users to take any action.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> PrinterShareItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PrinterShareItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return PrinterShareItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def allowed_groups(self) -> AllowedGroupsRequestBuilder:
        """
        Provides operations to manage the allowedGroups property of the microsoft.graph.printerShare entity.
        """
        from .allowed_groups.allowed_groups_request_builder import AllowedGroupsRequestBuilder

        return AllowedGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def allowed_users(self) -> AllowedUsersRequestBuilder:
        """
        Provides operations to manage the allowedUsers property of the microsoft.graph.printerShare entity.
        """
        from .allowed_users.allowed_users_request_builder import AllowedUsersRequestBuilder

        return AllowedUsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def jobs(self) -> JobsRequestBuilder:
        """
        Provides operations to manage the jobs property of the microsoft.graph.printerBase entity.
        """
        from .jobs.jobs_request_builder import JobsRequestBuilder

        return JobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def printer(self) -> PrinterRequestBuilder:
        """
        Provides operations to manage the printer property of the microsoft.graph.printerShare entity.
        """
        from .printer.printer_request_builder import PrinterRequestBuilder

        return PrinterRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PrinterShareItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class PrinterShareItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a printer share.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PrinterShareItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[PrinterShareItemRequestBuilder.PrinterShareItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class PrinterShareItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

