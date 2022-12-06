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

analytics_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.analytics.analytics_request_builder')
columns_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.columns.columns_request_builder')
column_definition_item_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.columns.item.column_definition_item_request_builder')
content_types_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.content_types.content_types_request_builder')
content_type_item_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.content_types.item.content_type_item_request_builder')
drive_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.drive.drive_request_builder')
drives_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.drives.drives_request_builder')
drive_item_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.drives.item.drive_item_request_builder')
external_columns_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.external_columns.external_columns_request_builder')
column_definition_item_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.external_columns.item.column_definition_item_request_builder')
get_activities_by_interval_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.get_activities_by_interval.get_activities_by_interval_request_builder')
get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval.get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder')
get_applicable_content_types_for_list_with_list_id_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.get_applicable_content_types_for_list_with_list_id.get_applicable_content_types_for_list_with_list_id_request_builder')
get_by_path_with_path_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.get_by_path_with_path.get_by_path_with_path_request_builder')
items_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.items.items_request_builder')
base_item_item_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.items.item.base_item_item_request_builder')
lists_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.lists.lists_request_builder')
list_item_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.lists.item.list_item_request_builder')
onenote_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.onenote.onenote_request_builder')
operations_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.operations.operations_request_builder')
rich_long_running_operation_item_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.operations.item.rich_long_running_operation_item_request_builder')
permissions_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.permissions.permissions_request_builder')
permission_item_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.permissions.item.permission_item_request_builder')
sites_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.sites.sites_request_builder')
site_item_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.sites.item.site_item_request_builder')
term_store_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.term_store.term_store_request_builder')
term_stores_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.term_stores.term_stores_request_builder')
store_item_request_builder = lazy_import('msgraph.generated.groups.item.sites.item.term_stores.item.store_item_request_builder')
site = lazy_import('msgraph.generated.models.site')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class SiteItemRequestBuilder():
    """
    Provides operations to manage the sites property of the microsoft.graph.group entity.
    """
    def analytics(self) -> analytics_request_builder.AnalyticsRequestBuilder:
        """
        Provides operations to manage the analytics property of the microsoft.graph.site entity.
        """
        return analytics_request_builder.AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def columns(self) -> columns_request_builder.ColumnsRequestBuilder:
        """
        Provides operations to manage the columns property of the microsoft.graph.site entity.
        """
        return columns_request_builder.ColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def content_types(self) -> content_types_request_builder.ContentTypesRequestBuilder:
        """
        Provides operations to manage the contentTypes property of the microsoft.graph.site entity.
        """
        return content_types_request_builder.ContentTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def drive(self) -> drive_request_builder.DriveRequestBuilder:
        """
        Provides operations to manage the drive property of the microsoft.graph.site entity.
        """
        return drive_request_builder.DriveRequestBuilder(self.request_adapter, self.path_parameters)
    
    def drives(self) -> drives_request_builder.DrivesRequestBuilder:
        """
        Provides operations to manage the drives property of the microsoft.graph.site entity.
        """
        return drives_request_builder.DrivesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def external_columns(self) -> external_columns_request_builder.ExternalColumnsRequestBuilder:
        """
        Provides operations to manage the externalColumns property of the microsoft.graph.site entity.
        """
        return external_columns_request_builder.ExternalColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def items(self) -> items_request_builder.ItemsRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.site entity.
        """
        return items_request_builder.ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def lists(self) -> lists_request_builder.ListsRequestBuilder:
        """
        Provides operations to manage the lists property of the microsoft.graph.site entity.
        """
        return lists_request_builder.ListsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def onenote(self) -> onenote_request_builder.OnenoteRequestBuilder:
        """
        Provides operations to manage the onenote property of the microsoft.graph.site entity.
        """
        return onenote_request_builder.OnenoteRequestBuilder(self.request_adapter, self.path_parameters)
    
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.site entity.
        """
        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def permissions(self) -> permissions_request_builder.PermissionsRequestBuilder:
        """
        Provides operations to manage the permissions property of the microsoft.graph.site entity.
        """
        return permissions_request_builder.PermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def sites(self) -> sites_request_builder.SitesRequestBuilder:
        """
        Provides operations to manage the sites property of the microsoft.graph.site entity.
        """
        return sites_request_builder.SitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def term_store(self) -> term_store_request_builder.TermStoreRequestBuilder:
        """
        Provides operations to manage the termStore property of the microsoft.graph.site entity.
        """
        return term_store_request_builder.TermStoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    def term_stores(self) -> term_stores_request_builder.TermStoresRequestBuilder:
        """
        Provides operations to manage the termStores property of the microsoft.graph.site entity.
        """
        return term_stores_request_builder.TermStoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    def columns_by_id(self,id: str) -> column_definition_item_request_builder.ColumnDefinitionItemRequestBuilder:
        """
        Provides operations to manage the columns property of the microsoft.graph.site entity.
        Args:
            id: Unique identifier of the item
        Returns: column_definition_item_request_builder.ColumnDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["columnDefinition%2Did"] = id
        return column_definition_item_request_builder.ColumnDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SiteItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def content_types_by_id(self,id: str) -> content_type_item_request_builder.ContentTypeItemRequestBuilder:
        """
        Provides operations to manage the contentTypes property of the microsoft.graph.site entity.
        Args:
            id: Unique identifier of the item
        Returns: content_type_item_request_builder.ContentTypeItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["contentType%2Did"] = id
        return content_type_item_request_builder.ContentTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def create_get_request_information(self,request_configuration: Optional[SiteItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The list of SharePoint sites in this group. Access the default site with /sites/root.
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
    
    def create_patch_request_information(self,body: Optional[site.Site] = None, request_configuration: Optional[SiteItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property sites in groups
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
    
    def drives_by_id(self,id: str) -> drive_item_request_builder.DriveItemRequestBuilder:
        """
        Provides operations to manage the drives property of the microsoft.graph.site entity.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_request_builder.DriveItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["drive%2Did"] = id
        return drive_item_request_builder.DriveItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def external_columns_by_id(self,id: str) -> column_definition_item_request_builder.ColumnDefinitionItemRequestBuilder:
        """
        Provides operations to manage the externalColumns property of the microsoft.graph.site entity.
        Args:
            id: Unique identifier of the item
        Returns: column_definition_item_request_builder.ColumnDefinitionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["columnDefinition%2Did"] = id
        return column_definition_item_request_builder.ColumnDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[SiteItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[site.Site]:
        """
        The list of SharePoint sites in this group. Access the default site with /sites/root.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[site.Site]
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
        return await self.request_adapter.send_async(request_info, site.Site, response_handler, error_mapping)
    
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
    
    def get_applicable_content_types_for_list_with_list_id(self,list_id: Optional[str] = None) -> get_applicable_content_types_for_list_with_list_id_request_builder.GetApplicableContentTypesForListWithListIdRequestBuilder:
        """
        Provides operations to call the getApplicableContentTypesForList method.
        Args:
            listId: Usage: listId='{listId}'
        Returns: get_applicable_content_types_for_list_with_list_id_request_builder.GetApplicableContentTypesForListWithListIdRequestBuilder
        """
        if list_id is None:
            raise Exception("list_id cannot be undefined")
        return get_applicable_content_types_for_list_with_list_id_request_builder.GetApplicableContentTypesForListWithListIdRequestBuilder(self.request_adapter, self.path_parameters, listId)
    
    def get_by_path_with_path(self,path: Optional[str] = None) -> get_by_path_with_path_request_builder.GetByPathWithPathRequestBuilder:
        """
        Provides operations to call the getByPath method.
        Args:
            path: Usage: path='{path}'
        Returns: get_by_path_with_path_request_builder.GetByPathWithPathRequestBuilder
        """
        if path is None:
            raise Exception("path cannot be undefined")
        return get_by_path_with_path_request_builder.GetByPathWithPathRequestBuilder(self.request_adapter, self.path_parameters, path)
    
    def items_by_id(self,id: str) -> base_item_item_request_builder.BaseItemItemRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.site entity.
        Args:
            id: Unique identifier of the item
        Returns: base_item_item_request_builder.BaseItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["baseItem%2Did"] = id
        return base_item_item_request_builder.BaseItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def lists_by_id(self,id: str) -> list_item_request_builder.ListItemRequestBuilder:
        """
        Provides operations to manage the lists property of the microsoft.graph.site entity.
        Args:
            id: Unique identifier of the item
        Returns: list_item_request_builder.ListItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["list%2Did"] = id
        return list_item_request_builder.ListItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def operations_by_id(self,id: str) -> rich_long_running_operation_item_request_builder.RichLongRunningOperationItemRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.site entity.
        Args:
            id: Unique identifier of the item
        Returns: rich_long_running_operation_item_request_builder.RichLongRunningOperationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["richLongRunningOperation%2Did"] = id
        return rich_long_running_operation_item_request_builder.RichLongRunningOperationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[site.Site] = None, request_configuration: Optional[SiteItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[site.Site]:
        """
        Update the navigation property sites in groups
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[site.Site]
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
        return await self.request_adapter.send_async(request_info, site.Site, response_handler, error_mapping)
    
    def permissions_by_id(self,id: str) -> permission_item_request_builder.PermissionItemRequestBuilder:
        """
        Provides operations to manage the permissions property of the microsoft.graph.site entity.
        Args:
            id: Unique identifier of the item
        Returns: permission_item_request_builder.PermissionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["permission%2Did"] = id
        return permission_item_request_builder.PermissionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def sites_by_id(self,id: str) -> SiteItemRequestBuilder:
        """
        Provides operations to manage the sites property of the microsoft.graph.site entity.
        Args:
            id: Unique identifier of the item
        Returns: SiteItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["site%2Did1"] = id
        return SiteItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def term_stores_by_id(self,id: str) -> store_item_request_builder.StoreItemRequestBuilder:
        """
        Provides operations to manage the termStores property of the microsoft.graph.site entity.
        Args:
            id: Unique identifier of the item
        Returns: store_item_request_builder.StoreItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["store%2Did"] = id
        return store_item_request_builder.StoreItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class SiteItemRequestBuilderGetQueryParameters():
        """
        The list of SharePoint sites in this group. Access the default site with /sites/root.
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
    class SiteItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SiteItemRequestBuilder.SiteItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SiteItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

