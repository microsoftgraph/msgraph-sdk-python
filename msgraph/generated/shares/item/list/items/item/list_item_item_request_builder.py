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
    from ......models import list_item
    from ......models.o_data_errors import o_data_error
    from .analytics import analytics_request_builder
    from .document_set_versions import document_set_versions_request_builder
    from .document_set_versions.item import document_set_version_item_request_builder
    from .drive_item import drive_item_request_builder
    from .fields import fields_request_builder
    from .get_activities_by_interval import get_activities_by_interval_request_builder
    from .get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval import get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder
    from .versions import versions_request_builder
    from .versions.item import list_item_version_item_request_builder

class ListItemItemRequestBuilder():
    """
    Provides operations to manage the items property of the microsoft.graph.list entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ListItemItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/shares/{sharedDriveItem%2Did}/list/items/{listItem%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ListItemItemRequestBuilderDeleteRequestConfiguration] = None) -> bytes:
        """
        Delete navigation property items for shares
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
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
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    def document_set_versions_by_id(self,id: str) -> document_set_version_item_request_builder.DocumentSetVersionItemRequestBuilder:
        """
        Provides operations to manage the documentSetVersions property of the microsoft.graph.listItem entity.
        Args:
            id: Unique identifier of the item
        Returns: document_set_version_item_request_builder.DocumentSetVersionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .document_set_versions.item import document_set_version_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["documentSetVersion%2Did"] = id
        return document_set_version_item_request_builder.DocumentSetVersionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ListItemItemRequestBuilderGetRequestConfiguration] = None) -> Optional[list_item.ListItem]:
        """
        All items contained in the list.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list_item.ListItem]
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
        from ......models import list_item

        return await self.request_adapter.send_async(request_info, list_item.ListItem, error_mapping)
    
    def get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval(self,end_date_time: Optional[str] = None, interval: Optional[str] = None, start_date_time: Optional[str] = None) -> get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder.GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder:
        """
        Provides operations to call the getActivitiesByInterval method.
        Args:
            endDateTime: Usage: endDateTime='{endDateTime}'
            interval: Usage: interval='{interval}'
            startDateTime: Usage: startDateTime='{startDateTime}'
        Returns: get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder.GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder
        """
        if end_date_time is None:
            raise Exception("end_date_time cannot be undefined")
        if interval is None:
            raise Exception("interval cannot be undefined")
        if start_date_time is None:
            raise Exception("start_date_time cannot be undefined")
        from .get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval import get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder

        return get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder.GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, interval, start_date_time)
    
    async def patch(self,body: Optional[list_item.ListItem] = None, request_configuration: Optional[ListItemItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[list_item.ListItem]:
        """
        Update the navigation property items in shares
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list_item.ListItem]
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
        from ......models import list_item

        return await self.request_adapter.send_async(request_info, list_item.ListItem, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ListItemItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property items for shares
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
    
    def to_get_request_information(self,request_configuration: Optional[ListItemItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        All items contained in the list.
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
    
    def to_patch_request_information(self,body: Optional[list_item.ListItem] = None, request_configuration: Optional[ListItemItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property items in shares
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
    
    def versions_by_id(self,id: str) -> list_item_version_item_request_builder.ListItemVersionItemRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.listItem entity.
        Args:
            id: Unique identifier of the item
        Returns: list_item_version_item_request_builder.ListItemVersionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .versions.item import list_item_version_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["listItemVersion%2Did"] = id
        return list_item_version_item_request_builder.ListItemVersionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def analytics(self) -> analytics_request_builder.AnalyticsRequestBuilder:
        """
        Provides operations to manage the analytics property of the microsoft.graph.listItem entity.
        """
        from .analytics import analytics_request_builder

        return analytics_request_builder.AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def document_set_versions(self) -> document_set_versions_request_builder.DocumentSetVersionsRequestBuilder:
        """
        Provides operations to manage the documentSetVersions property of the microsoft.graph.listItem entity.
        """
        from .document_set_versions import document_set_versions_request_builder

        return document_set_versions_request_builder.DocumentSetVersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive_item(self) -> drive_item_request_builder.DriveItemRequestBuilder:
        """
        Provides operations to manage the driveItem property of the microsoft.graph.listItem entity.
        """
        from .drive_item import drive_item_request_builder

        return drive_item_request_builder.DriveItemRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fields(self) -> fields_request_builder.FieldsRequestBuilder:
        """
        Provides operations to manage the fields property of the microsoft.graph.listItem entity.
        """
        from .fields import fields_request_builder

        return fields_request_builder.FieldsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_activities_by_interval(self) -> get_activities_by_interval_request_builder.GetActivitiesByIntervalRequestBuilder:
        """
        Provides operations to call the getActivitiesByInterval method.
        """
        from .get_activities_by_interval import get_activities_by_interval_request_builder

        return get_activities_by_interval_request_builder.GetActivitiesByIntervalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def versions(self) -> versions_request_builder.VersionsRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.listItem entity.
        """
        from .versions import versions_request_builder

        return versions_request_builder.VersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ListItemItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ListItemItemRequestBuilderGetQueryParameters():
        """
        All items contained in the list.
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
    class ListItemItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ListItemItemRequestBuilder.ListItemItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ListItemItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

