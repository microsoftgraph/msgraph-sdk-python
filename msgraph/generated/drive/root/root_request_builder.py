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

analytics_request_builder = lazy_import('msgraph.generated.drive.root.analytics.analytics_request_builder')
checkin_request_builder = lazy_import('msgraph.generated.drive.root.checkin.checkin_request_builder')
checkout_request_builder = lazy_import('msgraph.generated.drive.root.checkout.checkout_request_builder')
children_request_builder = lazy_import('msgraph.generated.drive.root.children.children_request_builder')
drive_item_item_request_builder = lazy_import('msgraph.generated.drive.root.children.item.drive_item_item_request_builder')
content_request_builder = lazy_import('msgraph.generated.drive.root.content.content_request_builder')
copy_request_builder = lazy_import('msgraph.generated.drive.root.copy.copy_request_builder')
create_link_request_builder = lazy_import('msgraph.generated.drive.root.create_link.create_link_request_builder')
create_upload_session_request_builder = lazy_import('msgraph.generated.drive.root.create_upload_session.create_upload_session_request_builder')
delta_request_builder = lazy_import('msgraph.generated.drive.root.delta.delta_request_builder')
delta_with_token_request_builder = lazy_import('msgraph.generated.drive.root.delta_with_token.delta_with_token_request_builder')
follow_request_builder = lazy_import('msgraph.generated.drive.root.follow.follow_request_builder')
get_activities_by_interval_request_builder = lazy_import('msgraph.generated.drive.root.get_activities_by_interval.get_activities_by_interval_request_builder')
get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder = lazy_import('msgraph.generated.drive.root.get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval.get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder')
invite_request_builder = lazy_import('msgraph.generated.drive.root.invite.invite_request_builder')
list_item_request_builder = lazy_import('msgraph.generated.drive.root.list_item.list_item_request_builder')
permissions_request_builder = lazy_import('msgraph.generated.drive.root.permissions.permissions_request_builder')
permission_item_request_builder = lazy_import('msgraph.generated.drive.root.permissions.item.permission_item_request_builder')
preview_request_builder = lazy_import('msgraph.generated.drive.root.preview.preview_request_builder')
restore_request_builder = lazy_import('msgraph.generated.drive.root.restore.restore_request_builder')
search_with_q_request_builder = lazy_import('msgraph.generated.drive.root.search_with_q.search_with_q_request_builder')
subscriptions_request_builder = lazy_import('msgraph.generated.drive.root.subscriptions.subscriptions_request_builder')
subscription_item_request_builder = lazy_import('msgraph.generated.drive.root.subscriptions.item.subscription_item_request_builder')
thumbnails_request_builder = lazy_import('msgraph.generated.drive.root.thumbnails.thumbnails_request_builder')
thumbnail_set_item_request_builder = lazy_import('msgraph.generated.drive.root.thumbnails.item.thumbnail_set_item_request_builder')
unfollow_request_builder = lazy_import('msgraph.generated.drive.root.unfollow.unfollow_request_builder')
validate_permission_request_builder = lazy_import('msgraph.generated.drive.root.validate_permission.validate_permission_request_builder')
versions_request_builder = lazy_import('msgraph.generated.drive.root.versions.versions_request_builder')
drive_item_version_item_request_builder = lazy_import('msgraph.generated.drive.root.versions.item.drive_item_version_item_request_builder')
drive_item = lazy_import('msgraph.generated.models.drive_item')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class RootRequestBuilder():
    """
    Provides operations to manage the root property of the microsoft.graph.drive entity.
    """
    def analytics(self) -> analytics_request_builder.AnalyticsRequestBuilder:
        """
        Provides operations to manage the analytics property of the microsoft.graph.driveItem entity.
        """
        return analytics_request_builder.AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def checkin(self) -> checkin_request_builder.CheckinRequestBuilder:
        """
        Provides operations to call the checkin method.
        """
        return checkin_request_builder.CheckinRequestBuilder(self.request_adapter, self.path_parameters)
    
    def checkout(self) -> checkout_request_builder.CheckoutRequestBuilder:
        """
        Provides operations to call the checkout method.
        """
        return checkout_request_builder.CheckoutRequestBuilder(self.request_adapter, self.path_parameters)
    
    def children(self) -> children_request_builder.ChildrenRequestBuilder:
        """
        Provides operations to manage the children property of the microsoft.graph.driveItem entity.
        """
        return children_request_builder.ChildrenRequestBuilder(self.request_adapter, self.path_parameters)
    
    def content(self) -> content_request_builder.ContentRequestBuilder:
        """
        Provides operations to manage the media for the drive entity.
        """
        return content_request_builder.ContentRequestBuilder(self.request_adapter, self.path_parameters)
    
    def copy(self) -> copy_request_builder.CopyRequestBuilder:
        """
        Provides operations to call the copy method.
        """
        return copy_request_builder.CopyRequestBuilder(self.request_adapter, self.path_parameters)
    
    def create_link(self) -> create_link_request_builder.CreateLinkRequestBuilder:
        """
        Provides operations to call the createLink method.
        """
        return create_link_request_builder.CreateLinkRequestBuilder(self.request_adapter, self.path_parameters)
    
    def create_upload_session(self) -> create_upload_session_request_builder.CreateUploadSessionRequestBuilder:
        """
        Provides operations to call the createUploadSession method.
        """
        return create_upload_session_request_builder.CreateUploadSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    def follow(self) -> follow_request_builder.FollowRequestBuilder:
        """
        Provides operations to call the follow method.
        """
        return follow_request_builder.FollowRequestBuilder(self.request_adapter, self.path_parameters)
    
    def invite(self) -> invite_request_builder.InviteRequestBuilder:
        """
        Provides operations to call the invite method.
        """
        return invite_request_builder.InviteRequestBuilder(self.request_adapter, self.path_parameters)
    
    def list_item(self) -> list_item_request_builder.ListItemRequestBuilder:
        """
        Provides operations to manage the listItem property of the microsoft.graph.driveItem entity.
        """
        return list_item_request_builder.ListItemRequestBuilder(self.request_adapter, self.path_parameters)
    
    def permissions(self) -> permissions_request_builder.PermissionsRequestBuilder:
        """
        Provides operations to manage the permissions property of the microsoft.graph.driveItem entity.
        """
        return permissions_request_builder.PermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def preview(self) -> preview_request_builder.PreviewRequestBuilder:
        """
        Provides operations to call the preview method.
        """
        return preview_request_builder.PreviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    def restore(self) -> restore_request_builder.RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        return restore_request_builder.RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    def subscriptions(self) -> subscriptions_request_builder.SubscriptionsRequestBuilder:
        """
        Provides operations to manage the subscriptions property of the microsoft.graph.driveItem entity.
        """
        return subscriptions_request_builder.SubscriptionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def thumbnails(self) -> thumbnails_request_builder.ThumbnailsRequestBuilder:
        """
        Provides operations to manage the thumbnails property of the microsoft.graph.driveItem entity.
        """
        return thumbnails_request_builder.ThumbnailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def unfollow(self) -> unfollow_request_builder.UnfollowRequestBuilder:
        """
        Provides operations to call the unfollow method.
        """
        return unfollow_request_builder.UnfollowRequestBuilder(self.request_adapter, self.path_parameters)
    
    def validate_permission(self) -> validate_permission_request_builder.ValidatePermissionRequestBuilder:
        """
        Provides operations to call the validatePermission method.
        """
        return validate_permission_request_builder.ValidatePermissionRequestBuilder(self.request_adapter, self.path_parameters)
    
    def versions(self) -> versions_request_builder.VersionsRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.driveItem entity.
        """
        return versions_request_builder.VersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def children_by_id(self,id: str) -> drive_item_item_request_builder.DriveItemItemRequestBuilder:
        """
        Provides operations to manage the children property of the microsoft.graph.driveItem entity.
        Args:
            id: Unique identifier of the item
        Returns: drive_item_item_request_builder.DriveItemItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["driveItem%2Did"] = id
        return drive_item_item_request_builder.DriveItemItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new RootRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/drive/root{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[RootRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property root for drive
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
    
    def create_get_request_information(self,request_configuration: Optional[RootRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the metadata for a driveItem in a drive by file system path or ID.`item-id` is the ID of a driveItem. It may also be the unique ID of a SharePoint list item.
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
    
    def create_patch_request_information(self,body: Optional[drive_item.DriveItem] = None, request_configuration: Optional[RootRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property root in drive
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
    
    async def delete(self,request_configuration: Optional[RootRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property root for drive
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
    
    def delta(self,) -> delta_request_builder.DeltaRequestBuilder:
        """
        Provides operations to call the delta method.
        Returns: delta_request_builder.DeltaRequestBuilder
        """
        return delta_request_builder.DeltaRequestBuilder(self.request_adapter, self.path_parameters)
    
    def delta_with_token(self,token: Optional[str] = None) -> delta_with_token_request_builder.DeltaWithTokenRequestBuilder:
        """
        Provides operations to call the delta method.
        Args:
            token: Usage: token='{token}'
        Returns: delta_with_token_request_builder.DeltaWithTokenRequestBuilder
        """
        if token is None:
            raise Exception("token cannot be undefined")
        return delta_with_token_request_builder.DeltaWithTokenRequestBuilder(self.request_adapter, self.path_parameters, token)
    
    async def get(self,request_configuration: Optional[RootRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[drive_item.DriveItem]:
        """
        Retrieve the metadata for a driveItem in a drive by file system path or ID.`item-id` is the ID of a driveItem. It may also be the unique ID of a SharePoint list item.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[drive_item.DriveItem]
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
        return await self.request_adapter.send_async(request_info, drive_item.DriveItem, response_handler, error_mapping)
    
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
    
    async def patch(self,body: Optional[drive_item.DriveItem] = None, request_configuration: Optional[RootRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[drive_item.DriveItem]:
        """
        Update the navigation property root in drive
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[drive_item.DriveItem]
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
        return await self.request_adapter.send_async(request_info, drive_item.DriveItem, response_handler, error_mapping)
    
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
    
    def search_with_q(self,q: Optional[str] = None) -> search_with_q_request_builder.SearchWithQRequestBuilder:
        """
        Provides operations to call the search method.
        Args:
            q: Usage: q='{q}'
        Returns: search_with_q_request_builder.SearchWithQRequestBuilder
        """
        if q is None:
            raise Exception("q cannot be undefined")
        return search_with_q_request_builder.SearchWithQRequestBuilder(self.request_adapter, self.path_parameters, q)
    
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
    class RootRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class RootRequestBuilderGetQueryParameters():
        """
        Retrieve the metadata for a driveItem in a drive by file system path or ID.`item-id` is the ID of a driveItem. It may also be the unique ID of a SharePoint list item.
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
    class RootRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[RootRequestBuilder.RootRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class RootRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

