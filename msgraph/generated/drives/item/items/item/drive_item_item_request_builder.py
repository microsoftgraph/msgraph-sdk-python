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
    from .....models import drive_item
    from .....models.o_data_errors import o_data_error
    from .analytics import analytics_request_builder
    from .checkin import checkin_request_builder
    from .checkout import checkout_request_builder
    from .children import children_request_builder
    from .content import content_request_builder
    from .copy import copy_request_builder
    from .created_by_user import created_by_user_request_builder
    from .create_link import create_link_request_builder
    from .create_upload_session import create_upload_session_request_builder
    from .delta import delta_request_builder
    from .delta_with_token import delta_with_token_request_builder
    from .follow import follow_request_builder
    from .get_activities_by_interval import get_activities_by_interval_request_builder
    from .get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval import get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder
    from .invite import invite_request_builder
    from .last_modified_by_user import last_modified_by_user_request_builder
    from .list_item import list_item_request_builder
    from .permissions import permissions_request_builder
    from .preview import preview_request_builder
    from .restore import restore_request_builder
    from .search_with_q import search_with_q_request_builder
    from .subscriptions import subscriptions_request_builder
    from .thumbnails import thumbnails_request_builder
    from .unfollow import unfollow_request_builder
    from .validate_permission import validate_permission_request_builder
    from .versions import versions_request_builder
    from .workbook import workbook_request_builder

class DriveItemItemRequestBuilder():
    """
    Provides operations to manage the items property of the microsoft.graph.drive entity.
    """
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
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def delta_with_token(self,token: Optional[str] = None) -> delta_with_token_request_builder.DeltaWithTokenRequestBuilder:
        """
        Provides operations to call the delta method.
        Args:
            token: Usage: token='{token}'
        Returns: delta_with_token_request_builder.DeltaWithTokenRequestBuilder
        """
        if token is None:
            raise Exception("token cannot be undefined")
        from .delta_with_token import delta_with_token_request_builder

        return delta_with_token_request_builder.DeltaWithTokenRequestBuilder(self.request_adapter, self.path_parameters, token)
    
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
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import drive_item

        return await self.request_adapter.send_async(request_info, drive_item.DriveItem, error_mapping)
    
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
        from .....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models import drive_item

        return await self.request_adapter.send_async(request_info, drive_item.DriveItem, error_mapping)
    
    def search_with_q(self,q: Optional[str] = None) -> search_with_q_request_builder.SearchWithQRequestBuilder:
        """
        Provides operations to call the search method.
        Args:
            q: Usage: q='{q}'
        Returns: search_with_q_request_builder.SearchWithQRequestBuilder
        """
        if q is None:
            raise Exception("q cannot be undefined")
        from .search_with_q import search_with_q_request_builder

        return search_with_q_request_builder.SearchWithQRequestBuilder(self.request_adapter, self.path_parameters, q)
    
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
        request_info.headers["Accept"] = ["application/json"]
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def analytics(self) -> analytics_request_builder.AnalyticsRequestBuilder:
        """
        Provides operations to manage the analytics property of the microsoft.graph.driveItem entity.
        """
        from .analytics import analytics_request_builder

        return analytics_request_builder.AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def checkin(self) -> checkin_request_builder.CheckinRequestBuilder:
        """
        Provides operations to call the checkin method.
        """
        from .checkin import checkin_request_builder

        return checkin_request_builder.CheckinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def checkout(self) -> checkout_request_builder.CheckoutRequestBuilder:
        """
        Provides operations to call the checkout method.
        """
        from .checkout import checkout_request_builder

        return checkout_request_builder.CheckoutRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def children(self) -> children_request_builder.ChildrenRequestBuilder:
        """
        Provides operations to manage the children property of the microsoft.graph.driveItem entity.
        """
        from .children import children_request_builder

        return children_request_builder.ChildrenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def content(self) -> content_request_builder.ContentRequestBuilder:
        """
        Provides operations to manage the media for the drive entity.
        """
        from .content import content_request_builder

        return content_request_builder.ContentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def copy(self) -> copy_request_builder.CopyRequestBuilder:
        """
        Provides operations to call the copy method.
        """
        from .copy import copy_request_builder

        return copy_request_builder.CopyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def created_by_user(self) -> created_by_user_request_builder.CreatedByUserRequestBuilder:
        """
        Provides operations to manage the createdByUser property of the microsoft.graph.baseItem entity.
        """
        from .created_by_user import created_by_user_request_builder

        return created_by_user_request_builder.CreatedByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_link(self) -> create_link_request_builder.CreateLinkRequestBuilder:
        """
        Provides operations to call the createLink method.
        """
        from .create_link import create_link_request_builder

        return create_link_request_builder.CreateLinkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_upload_session(self) -> create_upload_session_request_builder.CreateUploadSessionRequestBuilder:
        """
        Provides operations to call the createUploadSession method.
        """
        from .create_upload_session import create_upload_session_request_builder

        return create_upload_session_request_builder.CreateUploadSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delta(self) -> delta_request_builder.DeltaRequestBuilder:
        """
        Provides operations to call the delta method.
        """
        from .delta import delta_request_builder

        return delta_request_builder.DeltaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def follow(self) -> follow_request_builder.FollowRequestBuilder:
        """
        Provides operations to call the follow method.
        """
        from .follow import follow_request_builder

        return follow_request_builder.FollowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_activities_by_interval(self) -> get_activities_by_interval_request_builder.GetActivitiesByIntervalRequestBuilder:
        """
        Provides operations to call the getActivitiesByInterval method.
        """
        from .get_activities_by_interval import get_activities_by_interval_request_builder

        return get_activities_by_interval_request_builder.GetActivitiesByIntervalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def invite(self) -> invite_request_builder.InviteRequestBuilder:
        """
        Provides operations to call the invite method.
        """
        from .invite import invite_request_builder

        return invite_request_builder.InviteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_modified_by_user(self) -> last_modified_by_user_request_builder.LastModifiedByUserRequestBuilder:
        """
        Provides operations to manage the lastModifiedByUser property of the microsoft.graph.baseItem entity.
        """
        from .last_modified_by_user import last_modified_by_user_request_builder

        return last_modified_by_user_request_builder.LastModifiedByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def list_item(self) -> list_item_request_builder.ListItemRequestBuilder:
        """
        Provides operations to manage the listItem property of the microsoft.graph.driveItem entity.
        """
        from .list_item import list_item_request_builder

        return list_item_request_builder.ListItemRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permissions(self) -> permissions_request_builder.PermissionsRequestBuilder:
        """
        Provides operations to manage the permissions property of the microsoft.graph.driveItem entity.
        """
        from .permissions import permissions_request_builder

        return permissions_request_builder.PermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def preview(self) -> preview_request_builder.PreviewRequestBuilder:
        """
        Provides operations to call the preview method.
        """
        from .preview import preview_request_builder

        return preview_request_builder.PreviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> restore_request_builder.RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore import restore_request_builder

        return restore_request_builder.RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscriptions(self) -> subscriptions_request_builder.SubscriptionsRequestBuilder:
        """
        Provides operations to manage the subscriptions property of the microsoft.graph.driveItem entity.
        """
        from .subscriptions import subscriptions_request_builder

        return subscriptions_request_builder.SubscriptionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def thumbnails(self) -> thumbnails_request_builder.ThumbnailsRequestBuilder:
        """
        Provides operations to manage the thumbnails property of the microsoft.graph.driveItem entity.
        """
        from .thumbnails import thumbnails_request_builder

        return thumbnails_request_builder.ThumbnailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unfollow(self) -> unfollow_request_builder.UnfollowRequestBuilder:
        """
        Provides operations to call the unfollow method.
        """
        from .unfollow import unfollow_request_builder

        return unfollow_request_builder.UnfollowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate_permission(self) -> validate_permission_request_builder.ValidatePermissionRequestBuilder:
        """
        Provides operations to call the validatePermission method.
        """
        from .validate_permission import validate_permission_request_builder

        return validate_permission_request_builder.ValidatePermissionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def versions(self) -> versions_request_builder.VersionsRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.driveItem entity.
        """
        from .versions import versions_request_builder

        return versions_request_builder.VersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def workbook(self) -> workbook_request_builder.WorkbookRequestBuilder:
        """
        Provides operations to manage the workbook property of the microsoft.graph.driveItem entity.
        """
        from .workbook import workbook_request_builder

        return workbook_request_builder.WorkbookRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DriveItemItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DriveItemItemRequestBuilderGetQueryParameters():
        """
        All items contained in the drive. Read-only. Nullable.
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
    class DriveItemItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

