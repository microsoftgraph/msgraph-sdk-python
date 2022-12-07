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

analytics_request_builder = lazy_import('msgraph.generated.me.drives.item.root.list_item.analytics.analytics_request_builder')
document_set_versions_request_builder = lazy_import('msgraph.generated.me.drives.item.root.list_item.document_set_versions.document_set_versions_request_builder')
document_set_version_item_request_builder = lazy_import('msgraph.generated.me.drives.item.root.list_item.document_set_versions.item.document_set_version_item_request_builder')
drive_item_request_builder = lazy_import('msgraph.generated.me.drives.item.root.list_item.drive_item.drive_item_request_builder')
fields_request_builder = lazy_import('msgraph.generated.me.drives.item.root.list_item.fields.fields_request_builder')
get_activities_by_interval_request_builder = lazy_import('msgraph.generated.me.drives.item.root.list_item.get_activities_by_interval.get_activities_by_interval_request_builder')
get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder = lazy_import('msgraph.generated.me.drives.item.root.list_item.get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval.get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder')
versions_request_builder = lazy_import('msgraph.generated.me.drives.item.root.list_item.versions.versions_request_builder')
list_item_version_item_request_builder = lazy_import('msgraph.generated.me.drives.item.root.list_item.versions.item.list_item_version_item_request_builder')
list_item = lazy_import('msgraph.generated.models.list_item')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class ListItemRequestBuilder():
    """
    Provides operations to manage the listItem property of the microsoft.graph.driveItem entity.
    """
    def analytics(self) -> analytics_request_builder.AnalyticsRequestBuilder:
        """
        Provides operations to manage the analytics property of the microsoft.graph.listItem entity.
        """
        return analytics_request_builder.AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def document_set_versions(self) -> document_set_versions_request_builder.DocumentSetVersionsRequestBuilder:
        """
        Provides operations to manage the documentSetVersions property of the microsoft.graph.listItem entity.
        """
        return document_set_versions_request_builder.DocumentSetVersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def drive_item(self) -> drive_item_request_builder.DriveItemRequestBuilder:
        """
        Provides operations to manage the driveItem property of the microsoft.graph.listItem entity.
        """
        return drive_item_request_builder.DriveItemRequestBuilder(self.request_adapter, self.path_parameters)
    
    def fields(self) -> fields_request_builder.FieldsRequestBuilder:
        """
        Provides operations to manage the fields property of the microsoft.graph.listItem entity.
        """
        return fields_request_builder.FieldsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def versions(self) -> versions_request_builder.VersionsRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.listItem entity.
        """
        return versions_request_builder.VersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ListItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me/drives/{drive%2Did}/root/listItem{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[ListItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property listItem for me
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
    
    def create_get_request_information(self,request_configuration: Optional[ListItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        For drives in SharePoint, the associated document library list item. Read-only. Nullable.
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
    
    def create_patch_request_information(self,body: Optional[list_item.ListItem] = None, request_configuration: Optional[ListItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property listItem in me
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
    
    async def delete(self,request_configuration: Optional[ListItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property listItem for me
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
    
    def document_set_versions_by_id(self,id: str) -> document_set_version_item_request_builder.DocumentSetVersionItemRequestBuilder:
        """
        Provides operations to manage the documentSetVersions property of the microsoft.graph.listItem entity.
        Args:
            id: Unique identifier of the item
        Returns: document_set_version_item_request_builder.DocumentSetVersionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["documentSetVersion%2Did"] = id
        return document_set_version_item_request_builder.DocumentSetVersionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ListItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[list_item.ListItem]:
        """
        For drives in SharePoint, the associated document library list item. Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[list_item.ListItem]
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
        return await self.request_adapter.send_async(request_info, list_item.ListItem, response_handler, error_mapping)
    
    def get_activities_by_interval(self,) -> get_activities_by_interval_request_builder.GetActivitiesByIntervalRequestBuilder:
        """
        Provides operations to call the getActivitiesByInterval method.
        Returns: get_activities_by_interval_request_builder.GetActivitiesByIntervalRequestBuilder
        """
        return get_activities_by_interval_request_builder.GetActivitiesByIntervalRequestBuilder(self.request_adapter, self.path_parameters)
    
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
        return get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder.GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder(self.request_adapter, self.path_parameters, endDateTime, interval, startDateTime)
    
    async def patch(self,body: Optional[list_item.ListItem] = None, request_configuration: Optional[ListItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[list_item.ListItem]:
        """
        Update the navigation property listItem in me
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[list_item.ListItem]
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
        return await self.request_adapter.send_async(request_info, list_item.ListItem, response_handler, error_mapping)
    
    def versions_by_id(self,id: str) -> list_item_version_item_request_builder.ListItemVersionItemRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.listItem entity.
        Args:
            id: Unique identifier of the item
        Returns: list_item_version_item_request_builder.ListItemVersionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["listItemVersion%2Did"] = id
        return list_item_version_item_request_builder.ListItemVersionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class ListItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ListItemRequestBuilderGetQueryParameters():
        """
        For drives in SharePoint, the associated document library list item. Read-only. Nullable.
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
    class ListItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ListItemRequestBuilder.ListItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ListItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

