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
    from .....models.drive_item import DriveItem
    from .....models.o_data_errors.o_data_error import ODataError
    from .analytics.analytics_request_builder import AnalyticsRequestBuilder
    from .assign_sensitivity_label.assign_sensitivity_label_request_builder import AssignSensitivityLabelRequestBuilder
    from .checkin.checkin_request_builder import CheckinRequestBuilder
    from .checkout.checkout_request_builder import CheckoutRequestBuilder
    from .children.children_request_builder import ChildrenRequestBuilder
    from .content.content_request_builder import ContentRequestBuilder
    from .copy.copy_request_builder import CopyRequestBuilder
    from .created_by_user.created_by_user_request_builder import CreatedByUserRequestBuilder
    from .create_link.create_link_request_builder import CreateLinkRequestBuilder
    from .create_upload_session.create_upload_session_request_builder import CreateUploadSessionRequestBuilder
    from .delta.delta_request_builder import DeltaRequestBuilder
    from .delta_with_token.delta_with_token_request_builder import DeltaWithTokenRequestBuilder
    from .discard_checkout.discard_checkout_request_builder import DiscardCheckoutRequestBuilder
    from .extract_sensitivity_labels.extract_sensitivity_labels_request_builder import ExtractSensitivityLabelsRequestBuilder
    from .follow.follow_request_builder import FollowRequestBuilder
    from .get_activities_by_interval.get_activities_by_interval_request_builder import GetActivitiesByIntervalRequestBuilder
    from .get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval.get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder import GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder
    from .invite.invite_request_builder import InviteRequestBuilder
    from .last_modified_by_user.last_modified_by_user_request_builder import LastModifiedByUserRequestBuilder
    from .list_item.list_item_request_builder import ListItemRequestBuilder
    from .permanent_delete.permanent_delete_request_builder import PermanentDeleteRequestBuilder
    from .permissions.permissions_request_builder import PermissionsRequestBuilder
    from .preview.preview_request_builder import PreviewRequestBuilder
    from .restore.restore_request_builder import RestoreRequestBuilder
    from .retention_label.retention_label_request_builder import RetentionLabelRequestBuilder
    from .search_with_q.search_with_q_request_builder import SearchWithQRequestBuilder
    from .subscriptions.subscriptions_request_builder import SubscriptionsRequestBuilder
    from .thumbnails.thumbnails_request_builder import ThumbnailsRequestBuilder
    from .unfollow.unfollow_request_builder import UnfollowRequestBuilder
    from .validate_permission.validate_permission_request_builder import ValidatePermissionRequestBuilder
    from .versions.versions_request_builder import VersionsRequestBuilder
    from .workbook.workbook_request_builder import WorkbookRequestBuilder

class DriveItemItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the items property of the microsoft.graph.drive entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DriveItemItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/drives/{drive%2Did}/items/{driveItem%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property items for drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def delta_with_token(self,token: str) -> DeltaWithTokenRequestBuilder:
        """
        Provides operations to call the delta method.
        param token: Usage: token='{token}'
        Returns: DeltaWithTokenRequestBuilder
        """
        if token is None:
            raise TypeError("token cannot be null.")
        from .delta_with_token.delta_with_token_request_builder import DeltaWithTokenRequestBuilder

        return DeltaWithTokenRequestBuilder(self.request_adapter, self.path_parameters, token)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DriveItemItemRequestBuilderGetQueryParameters]] = None) -> Optional[DriveItem]:
        """
        All items contained in the drive. Read-only. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DriveItem]
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
        from .....models.drive_item import DriveItem

        return await self.request_adapter.send_async(request_info, DriveItem, error_mapping)
    
    def get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval(self,end_date_time: str, interval: str, start_date_time: str) -> GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder:
        """
        Provides operations to call the getActivitiesByInterval method.
        param end_date_time: Usage: endDateTime='{endDateTime}'
        param interval: Usage: interval='{interval}'
        param start_date_time: Usage: startDateTime='{startDateTime}'
        Returns: GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder
        """
        if end_date_time is None:
            raise TypeError("end_date_time cannot be null.")
        if interval is None:
            raise TypeError("interval cannot be null.")
        if start_date_time is None:
            raise TypeError("start_date_time cannot be null.")
        from .get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval.get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder import GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder

        return GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, interval, start_date_time)
    
    async def patch(self,body: DriveItem, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DriveItem]:
        """
        Update the navigation property items in drives
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DriveItem]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.drive_item import DriveItem

        return await self.request_adapter.send_async(request_info, DriveItem, error_mapping)
    
    def search_with_q(self,q: str) -> SearchWithQRequestBuilder:
        """
        Provides operations to call the search method.
        param q: Usage: q='{q}'
        Returns: SearchWithQRequestBuilder
        """
        if q is None:
            raise TypeError("q cannot be null.")
        from .search_with_q.search_with_q_request_builder import SearchWithQRequestBuilder

        return SearchWithQRequestBuilder(self.request_adapter, self.path_parameters, q)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property items for drives
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DriveItemItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        All items contained in the drive. Read-only. Nullable.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: DriveItem, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property items in drives
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> DriveItemItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DriveItemItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DriveItemItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def analytics(self) -> AnalyticsRequestBuilder:
        """
        Provides operations to manage the analytics property of the microsoft.graph.driveItem entity.
        """
        from .analytics.analytics_request_builder import AnalyticsRequestBuilder

        return AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assign_sensitivity_label(self) -> AssignSensitivityLabelRequestBuilder:
        """
        Provides operations to call the assignSensitivityLabel method.
        """
        from .assign_sensitivity_label.assign_sensitivity_label_request_builder import AssignSensitivityLabelRequestBuilder

        return AssignSensitivityLabelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def checkin(self) -> CheckinRequestBuilder:
        """
        Provides operations to call the checkin method.
        """
        from .checkin.checkin_request_builder import CheckinRequestBuilder

        return CheckinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def checkout(self) -> CheckoutRequestBuilder:
        """
        Provides operations to call the checkout method.
        """
        from .checkout.checkout_request_builder import CheckoutRequestBuilder

        return CheckoutRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def children(self) -> ChildrenRequestBuilder:
        """
        Provides operations to manage the children property of the microsoft.graph.driveItem entity.
        """
        from .children.children_request_builder import ChildrenRequestBuilder

        return ChildrenRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def content(self) -> ContentRequestBuilder:
        """
        Provides operations to manage the media for the drive entity.
        """
        from .content.content_request_builder import ContentRequestBuilder

        return ContentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def copy(self) -> CopyRequestBuilder:
        """
        Provides operations to call the copy method.
        """
        from .copy.copy_request_builder import CopyRequestBuilder

        return CopyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_link(self) -> CreateLinkRequestBuilder:
        """
        Provides operations to call the createLink method.
        """
        from .create_link.create_link_request_builder import CreateLinkRequestBuilder

        return CreateLinkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def create_upload_session(self) -> CreateUploadSessionRequestBuilder:
        """
        Provides operations to call the createUploadSession method.
        """
        from .create_upload_session.create_upload_session_request_builder import CreateUploadSessionRequestBuilder

        return CreateUploadSessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def created_by_user(self) -> CreatedByUserRequestBuilder:
        """
        Provides operations to manage the createdByUser property of the microsoft.graph.baseItem entity.
        """
        from .created_by_user.created_by_user_request_builder import CreatedByUserRequestBuilder

        return CreatedByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delta(self) -> DeltaRequestBuilder:
        """
        Provides operations to call the delta method.
        """
        from .delta.delta_request_builder import DeltaRequestBuilder

        return DeltaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def discard_checkout(self) -> DiscardCheckoutRequestBuilder:
        """
        Provides operations to call the discardCheckout method.
        """
        from .discard_checkout.discard_checkout_request_builder import DiscardCheckoutRequestBuilder

        return DiscardCheckoutRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extract_sensitivity_labels(self) -> ExtractSensitivityLabelsRequestBuilder:
        """
        Provides operations to call the extractSensitivityLabels method.
        """
        from .extract_sensitivity_labels.extract_sensitivity_labels_request_builder import ExtractSensitivityLabelsRequestBuilder

        return ExtractSensitivityLabelsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def follow(self) -> FollowRequestBuilder:
        """
        Provides operations to call the follow method.
        """
        from .follow.follow_request_builder import FollowRequestBuilder

        return FollowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_activities_by_interval(self) -> GetActivitiesByIntervalRequestBuilder:
        """
        Provides operations to call the getActivitiesByInterval method.
        """
        from .get_activities_by_interval.get_activities_by_interval_request_builder import GetActivitiesByIntervalRequestBuilder

        return GetActivitiesByIntervalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def invite(self) -> InviteRequestBuilder:
        """
        Provides operations to call the invite method.
        """
        from .invite.invite_request_builder import InviteRequestBuilder

        return InviteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_modified_by_user(self) -> LastModifiedByUserRequestBuilder:
        """
        Provides operations to manage the lastModifiedByUser property of the microsoft.graph.baseItem entity.
        """
        from .last_modified_by_user.last_modified_by_user_request_builder import LastModifiedByUserRequestBuilder

        return LastModifiedByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def list_item(self) -> ListItemRequestBuilder:
        """
        Provides operations to manage the listItem property of the microsoft.graph.driveItem entity.
        """
        from .list_item.list_item_request_builder import ListItemRequestBuilder

        return ListItemRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permanent_delete(self) -> PermanentDeleteRequestBuilder:
        """
        Provides operations to call the permanentDelete method.
        """
        from .permanent_delete.permanent_delete_request_builder import PermanentDeleteRequestBuilder

        return PermanentDeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permissions(self) -> PermissionsRequestBuilder:
        """
        Provides operations to manage the permissions property of the microsoft.graph.driveItem entity.
        """
        from .permissions.permissions_request_builder import PermissionsRequestBuilder

        return PermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def preview(self) -> PreviewRequestBuilder:
        """
        Provides operations to call the preview method.
        """
        from .preview.preview_request_builder import PreviewRequestBuilder

        return PreviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore.restore_request_builder import RestoreRequestBuilder

        return RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retention_label(self) -> RetentionLabelRequestBuilder:
        """
        Provides operations to manage the retentionLabel property of the microsoft.graph.driveItem entity.
        """
        from .retention_label.retention_label_request_builder import RetentionLabelRequestBuilder

        return RetentionLabelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscriptions(self) -> SubscriptionsRequestBuilder:
        """
        Provides operations to manage the subscriptions property of the microsoft.graph.driveItem entity.
        """
        from .subscriptions.subscriptions_request_builder import SubscriptionsRequestBuilder

        return SubscriptionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def thumbnails(self) -> ThumbnailsRequestBuilder:
        """
        Provides operations to manage the thumbnails property of the microsoft.graph.driveItem entity.
        """
        from .thumbnails.thumbnails_request_builder import ThumbnailsRequestBuilder

        return ThumbnailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unfollow(self) -> UnfollowRequestBuilder:
        """
        Provides operations to call the unfollow method.
        """
        from .unfollow.unfollow_request_builder import UnfollowRequestBuilder

        return UnfollowRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def validate_permission(self) -> ValidatePermissionRequestBuilder:
        """
        Provides operations to call the validatePermission method.
        """
        from .validate_permission.validate_permission_request_builder import ValidatePermissionRequestBuilder

        return ValidatePermissionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def versions(self) -> VersionsRequestBuilder:
        """
        Provides operations to manage the versions property of the microsoft.graph.driveItem entity.
        """
        from .versions.versions_request_builder import VersionsRequestBuilder

        return VersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def workbook(self) -> WorkbookRequestBuilder:
        """
        Provides operations to manage the workbook property of the microsoft.graph.driveItem entity.
        """
        from .workbook.workbook_request_builder import WorkbookRequestBuilder

        return WorkbookRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DriveItemItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DriveItemItemRequestBuilderGetQueryParameters():
        """
        All items contained in the drive. Read-only. Nullable.
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
    class DriveItemItemRequestBuilderGetRequestConfiguration(RequestConfiguration[DriveItemItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DriveItemItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

