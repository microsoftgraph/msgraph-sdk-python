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

analytics_request_builder = lazy_import('msgraph.generated.drives.item.items.item.analytics.analytics_request_builder')
children_request_builder = lazy_import('msgraph.generated.drives.item.items.item.children.children_request_builder')
drive_item_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.children.item.drive_item_item_request_builder')
content_request_builder = lazy_import('msgraph.generated.drives.item.items.item.content.content_request_builder')
list_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.list_item.list_item_request_builder')
microsoft_graph_checkin_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_checkin.microsoft_graph_checkin_request_builder')
microsoft_graph_checkout_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_checkout.microsoft_graph_checkout_request_builder')
microsoft_graph_copy_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_copy.microsoft_graph_copy_request_builder')
microsoft_graph_create_link_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_create_link.microsoft_graph_create_link_request_builder')
microsoft_graph_create_upload_session_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_create_upload_session.microsoft_graph_create_upload_session_request_builder')
microsoft_graph_delta_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_delta.microsoft_graph_delta_request_builder')
microsoft_graph_delta_with_token_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_delta_with_token.microsoft_graph_delta_with_token_request_builder')
microsoft_graph_follow_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_follow.microsoft_graph_follow_request_builder')
microsoft_graph_get_activities_by_interval_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_get_activities_by_interval.microsoft_graph_get_activities_by_interval_request_builder')
microsoft_graph_get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval.microsoft_graph_get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder')
microsoft_graph_invite_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_invite.microsoft_graph_invite_request_builder')
microsoft_graph_preview_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_preview.microsoft_graph_preview_request_builder')
microsoft_graph_restore_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_restore.microsoft_graph_restore_request_builder')
microsoft_graph_search_with_q_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_search_with_q.microsoft_graph_search_with_q_request_builder')
microsoft_graph_unfollow_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_unfollow.microsoft_graph_unfollow_request_builder')
microsoft_graph_validate_permission_request_builder = lazy_import('msgraph.generated.drives.item.items.item.microsoft_graph_validate_permission.microsoft_graph_validate_permission_request_builder')
permissions_request_builder = lazy_import('msgraph.generated.drives.item.items.item.permissions.permissions_request_builder')
permission_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.permissions.item.permission_item_request_builder')
subscriptions_request_builder = lazy_import('msgraph.generated.drives.item.items.item.subscriptions.subscriptions_request_builder')
subscription_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.subscriptions.item.subscription_item_request_builder')
thumbnails_request_builder = lazy_import('msgraph.generated.drives.item.items.item.thumbnails.thumbnails_request_builder')
thumbnail_set_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.thumbnails.item.thumbnail_set_item_request_builder')
versions_request_builder = lazy_import('msgraph.generated.drives.item.items.item.versions.versions_request_builder')
drive_item_version_item_request_builder = lazy_import('msgraph.generated.drives.item.items.item.versions.item.drive_item_version_item_request_builder')
workbook_request_builder = lazy_import('msgraph.generated.drives.item.items.item.workbook.workbook_request_builder')
drive_item = lazy_import('msgraph.generated.models.drive_item')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DriveItemItemRequestBuilder():
    """
    Provides operations to manage the items property of the microsoft.graph.drive entity.
    """
    @property
    def analytics(self) -> analytics_request_builder.AnalyticsRequestBuilder:
        """
        Provides operations to manage the analytics property of the microsoft.graph.driveItem entity.
        """
        return analytics_request_builder.AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def children(self) -> children_request_builder.ChildrenRequestBuilder:
        """
        Provides operations to manage the children property of the microsoft.graph.driveItem entity.
        """
        return children_request_builder.ChildrenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def content(self) -> content_request_builder.ContentRequestBuilder:
        """
        Provides operations to manage the media for the drive entity.
        """
        return content_request_builder.ContentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def list_item(self) -> list_item_request_builder.ListItemRequestBuilder:
        """
        Provides operations to manage the listItem property of the microsoft.graph.driveItem entity.
        """
        return list_item_request_builder.ListItemRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_checkin(self) -> microsoft_graph_checkin_request_builder.MicrosoftGraphCheckinRequestBuilder:
        """
        Provides operations to call the checkin method.
        """
        return microsoft_graph_checkin_request_builder.MicrosoftGraphCheckinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_checkout(self) -> microsoft_graph_checkout_request_builder.MicrosoftGraphCheckoutRequestBuilder:
        """
        Provides operations to call the checkout method.
        """
        return microsoft_graph_checkout_request_builder.MicrosoftGraphCheckoutRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_copy(self) -> microsoft_graph_copy_request_builder.MicrosoftGraphCopyRequestBuilder:
        """
        Provides operations to call the copy method.
        """
        return microsoft_graph_copy_request_builder.MicrosoftGraphCopyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_create_link(self) -> microsoft_graph_create_link_request_builder.MicrosoftGraphCreateLinkRequestBuilder:
        """
        Provides operations to call the createLink method.
        """
        return microsoft_graph_create_link_request_builder.MicrosoftGraphCreateLinkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_create_upload_session(self) -> microsoft_graph_create_upload_session_request_builder.MicrosoftGraphCreateUploadSessionRequestBuilder:
        """
        Provides operations to call the createUploadSession method.
        """
        return microsoft_graph_create_upload_session_request_builder.MicrosoftGraphCreateUploadSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_delta(self) -> microsoft_graph_delta_request_builder.MicrosoftGraphDeltaRequestBuilder:
        """
        Provides operations to call the delta method.
        """
        return microsoft_graph_delta_request_builder.MicrosoftGraphDeltaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_follow(self) -> microsoft_graph_follow_request_builder.MicrosoftGraphFollowRequestBuilder:
        """
        Provides operations to call the follow method.
        """
        return microsoft_graph_follow_request_builder.MicrosoftGraphFollowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_get_activities_by_interval(self) -> microsoft_graph_get_activities_by_interval_request_builder.MicrosoftGraphGetActivitiesByIntervalRequestBuilder:
        """
        Provides operations to call the getActivitiesByInterval method.
        """
        return microsoft_graph_get_activities_by_interval_request_builder.MicrosoftGraphGetActivitiesByIntervalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_invite(self) -> microsoft_graph_invite_request_builder.MicrosoftGraphInviteRequestBuilder:
        """
        Provides operations to call the invite method.
        """
        return microsoft_graph_invite_request_builder.MicrosoftGraphInviteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_preview(self) -> microsoft_graph_preview_request_builder.MicrosoftGraphPreviewRequestBuilder:
        """
        Provides operations to call the preview method.
        """
        return microsoft_graph_preview_request_builder.MicrosoftGraphPreviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_restore(self) -> microsoft_graph_restore_request_builder.MicrosoftGraphRestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        return microsoft_graph_restore_request_builder.MicrosoftGraphRestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_unfollow(self) -> microsoft_graph_unfollow_request_builder.MicrosoftGraphUnfollowRequestBuilder:
        """
        Provides operations to call the unfollow method.
        """
        return microsoft_graph_unfollow_request_builder.MicrosoftGraphUnfollowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def microsoft_graph_validate_permission(self) -> microsoft_graph_validate_permission_request_builder.MicrosoftGraphValidatePermissionRequestBuilder:
        """
        Provides operations to call the validatePermission method.
        """
        return microsoft_graph_validate_permission_request_builder.MicrosoftGraphValidatePermissionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permissions(self) -> permissions_request_builder.PermissionsRequestBuilder:
        """
        Provides operations to manage the permissions property of the microsoft.graph.driveItem entity.
        """
        return permissions_request_builder.PermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscriptions(self) -> subscriptions_request_builder.SubscriptionsRequestBuilder:
        """
        Provides operations to manage the subscriptions property of the microsoft.graph.driveItem entity.
        """
        return subscriptions_request_builder.SubscriptionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def thumbnails(self) -> thumbnails_request_builder.ThumbnailsRequestBuilder:
        """
        Provides operations to manage the thumbnails property of the microsoft.graph.driveItem entity.
        """
        return thumbnails_request_builder.ThumbnailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def versions(self) -> versions_request_builder.VersionsRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.driveItem entity.
        """
        return versions_request_builder.VersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def workbook(self) -> workbook_request_builder.WorkbookRequestBuilder:
        """
        Provides operations to manage the workbook property of the microsoft.graph.driveItem entity.
        """
        return workbook_request_builder.WorkbookRequestBuilder(self.request_adapter, self.path_parameters)
    
    def children_by_id(self,id: str) -> DriveItemItemRequestBuilder:
        """
        Provides operations to manage the children property of the microsoft.graph.driveItem entity.
        Args:
            id: Unique identifier of the item
        Returns: DriveItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["driveItem%2Did1"] = id
        return DriveItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DriveItemItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[DriveItemItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property items for drives
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
    
    async def get(self,request_configuration: Optional[DriveItemItemRequestBuilderGetRequestConfiguration] = None) -> Optional[drive_item.DriveItem]:
        """
        All items contained in the drive. Read-only. Nullable.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[drive_item.DriveItem]
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
        return await self.request_adapter.send_async(request_info, drive_item.DriveItem, error_mapping)
    
    def microsoft_graph_delta_with_token(self,token: Optional[str] = None) -> microsoft_graph_delta_with_token_request_builder.MicrosoftGraphDeltaWithTokenRequestBuilder:
        """
        Provides operations to call the delta method.
        Args:
            token: Usage: token='{token}'
        Returns: microsoft_graph_delta_with_token_request_builder.MicrosoftGraphDeltaWithTokenRequestBuilder
        """
        if token is None:
            raise Exception("token cannot be undefined")
        return microsoft_graph_delta_with_token_request_builder.MicrosoftGraphDeltaWithTokenRequestBuilder(self.request_adapter, self.path_parameters, token)
    
    def microsoft_graph_get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval(self,end_date_time: Optional[str] = None, interval: Optional[str] = None, start_date_time: Optional[str] = None) -> microsoft_graph_get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder.MicrosoftGraphGetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder:
        """
        Provides operations to call the getActivitiesByInterval method.
        Args:
            endDateTime: Usage: endDateTime='{endDateTime}'
            interval: Usage: interval='{interval}'
            startDateTime: Usage: startDateTime='{startDateTime}'
        Returns: microsoft_graph_get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder.MicrosoftGraphGetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder
        """
        if end_date_time is None:
            raise Exception("end_date_time cannot be undefined")
        if interval is None:
            raise Exception("interval cannot be undefined")
        if start_date_time is None:
            raise Exception("start_date_time cannot be undefined")
        return microsoft_graph_get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder.MicrosoftGraphGetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder(self.request_adapter, self.path_parameters, endDateTime, interval, startDateTime)
    
    def microsoft_graph_search_with_q(self,q: Optional[str] = None) -> microsoft_graph_search_with_q_request_builder.MicrosoftGraphSearchWithQRequestBuilder:
        """
        Provides operations to call the search method.
        Args:
            q: Usage: q='{q}'
        Returns: microsoft_graph_search_with_q_request_builder.MicrosoftGraphSearchWithQRequestBuilder
        """
        if q is None:
            raise Exception("q cannot be undefined")
        return microsoft_graph_search_with_q_request_builder.MicrosoftGraphSearchWithQRequestBuilder(self.request_adapter, self.path_parameters, q)
    
    async def patch(self,body: Optional[drive_item.DriveItem] = None, request_configuration: Optional[DriveItemItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[drive_item.DriveItem]:
        """
        Update the navigation property items in drives
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[drive_item.DriveItem]
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
        return await self.request_adapter.send_async(request_info, drive_item.DriveItem, error_mapping)
    
    def permissions_by_id(self,id: str) -> permission_item_request_builder.PermissionItemRequestBuilder:
        """
        Provides operations to manage the permissions property of the microsoft.graph.driveItem entity.
        Args:
            id: Unique identifier of the item
        Returns: permission_item_request_builder.PermissionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["permission%2Did"] = id
        return permission_item_request_builder.PermissionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def subscriptions_by_id(self,id: str) -> subscription_item_request_builder.SubscriptionItemRequestBuilder:
        """
        Provides operations to manage the subscriptions property of the microsoft.graph.driveItem entity.
        Args:
            id: Unique identifier of the item
        Returns: subscription_item_request_builder.SubscriptionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["subscription%2Did"] = id
        return subscription_item_request_builder.SubscriptionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def thumbnails_by_id(self,id: str) -> thumbnail_set_item_request_builder.ThumbnailSetItemRequestBuilder:
        """
        Provides operations to manage the thumbnails property of the microsoft.graph.driveItem entity.
        Args:
            id: Unique identifier of the item
        Returns: thumbnail_set_item_request_builder.ThumbnailSetItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["thumbnailSet%2Did"] = id
        return thumbnail_set_item_request_builder.ThumbnailSetItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def to_delete_request_information(self,request_configuration: Optional[DriveItemItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property items for drives
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
    
    def to_get_request_information(self,request_configuration: Optional[DriveItemItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        All items contained in the drive. Read-only. Nullable.
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
    
    def to_patch_request_information(self,body: Optional[drive_item.DriveItem] = None, request_configuration: Optional[DriveItemItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property items in drives
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
    
    def versions_by_id(self,id: str) -> drive_item_version_item_request_builder.DriveItemVersionItemRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.driveItem entity.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_version_item_request_builder.DriveItemVersionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["driveItemVersion%2Did"] = id
        return drive_item_version_item_request_builder.DriveItemVersionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class DriveItemItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DriveItemItemRequestBuilderGetQueryParameters():
        """
        All items contained in the drive. Read-only. Nullable.
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
    class DriveItemItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DriveItemItemRequestBuilder.DriveItemItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DriveItemItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

