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
    from .....models.protection_unit_base import ProtectionUnitBase
    from .cancel_offboard.cancel_offboard_request_builder import CancelOffboardRequestBuilder
    from .graph_drive_protection_unit.graph_drive_protection_unit_request_builder import GraphDriveProtectionUnitRequestBuilder
    from .graph_mailbox_protection_unit.graph_mailbox_protection_unit_request_builder import GraphMailboxProtectionUnitRequestBuilder
    from .graph_site_protection_unit.graph_site_protection_unit_request_builder import GraphSiteProtectionUnitRequestBuilder
    from .offboard.offboard_request_builder import OffboardRequestBuilder

class ProtectionUnitBaseItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the protectionUnits property of the microsoft.graph.backupRestoreRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ProtectionUnitBaseItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/protectionUnits/{protectionUnitBase%2Did}{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ProtectionUnitBaseItemRequestBuilderGetQueryParameters]] = None) -> Optional[ProtectionUnitBase]:
        """
        Read the properties and relationships of a protectionUnitBase object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ProtectionUnitBase]
        Find more info here: https://learn.microsoft.com/graph/api/protectionunitbase-get?view=graph-rest-1.0
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
        from .....models.protection_unit_base import ProtectionUnitBase

        return await self.request_adapter.send_async(request_info, ProtectionUnitBase, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ProtectionUnitBaseItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read the properties and relationships of a protectionUnitBase object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ProtectionUnitBaseItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ProtectionUnitBaseItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ProtectionUnitBaseItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def cancel_offboard(self) -> CancelOffboardRequestBuilder:
        """
        Provides operations to call the cancelOffboard method.
        """
        from .cancel_offboard.cancel_offboard_request_builder import CancelOffboardRequestBuilder

        return CancelOffboardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_drive_protection_unit(self) -> GraphDriveProtectionUnitRequestBuilder:
        """
        Casts the previous resource to driveProtectionUnit.
        """
        from .graph_drive_protection_unit.graph_drive_protection_unit_request_builder import GraphDriveProtectionUnitRequestBuilder

        return GraphDriveProtectionUnitRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_mailbox_protection_unit(self) -> GraphMailboxProtectionUnitRequestBuilder:
        """
        Casts the previous resource to mailboxProtectionUnit.
        """
        from .graph_mailbox_protection_unit.graph_mailbox_protection_unit_request_builder import GraphMailboxProtectionUnitRequestBuilder

        return GraphMailboxProtectionUnitRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_site_protection_unit(self) -> GraphSiteProtectionUnitRequestBuilder:
        """
        Casts the previous resource to siteProtectionUnit.
        """
        from .graph_site_protection_unit.graph_site_protection_unit_request_builder import GraphSiteProtectionUnitRequestBuilder

        return GraphSiteProtectionUnitRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def offboard(self) -> OffboardRequestBuilder:
        """
        Provides operations to call the offboard method.
        """
        from .offboard.offboard_request_builder import OffboardRequestBuilder

        return OffboardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ProtectionUnitBaseItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a protectionUnitBase object.
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
    class ProtectionUnitBaseItemRequestBuilderGetRequestConfiguration(RequestConfiguration[ProtectionUnitBaseItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

