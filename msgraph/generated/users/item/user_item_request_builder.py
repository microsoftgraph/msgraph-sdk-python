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
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.user import User
    from .activities.activities_request_builder import ActivitiesRequestBuilder
    from .adhoc_calls.adhoc_calls_request_builder import AdhocCallsRequestBuilder
    from .agreement_acceptances.agreement_acceptances_request_builder import AgreementAcceptancesRequestBuilder
    from .app_role_assignments.app_role_assignments_request_builder import AppRoleAssignmentsRequestBuilder
    from .assign_license.assign_license_request_builder import AssignLicenseRequestBuilder
    from .authentication.authentication_request_builder import AuthenticationRequestBuilder
    from .calendar.calendar_request_builder import CalendarRequestBuilder
    from .calendars.calendars_request_builder import CalendarsRequestBuilder
    from .calendar_groups.calendar_groups_request_builder import CalendarGroupsRequestBuilder
    from .calendar_view.calendar_view_request_builder import CalendarViewRequestBuilder
    from .change_password.change_password_request_builder import ChangePasswordRequestBuilder
    from .chats.chats_request_builder import ChatsRequestBuilder
    from .check_member_groups.check_member_groups_request_builder import CheckMemberGroupsRequestBuilder
    from .check_member_objects.check_member_objects_request_builder import CheckMemberObjectsRequestBuilder
    from .cloud_clipboard.cloud_clipboard_request_builder import CloudClipboardRequestBuilder
    from .cloud_p_cs.cloud_p_cs_request_builder import CloudPCsRequestBuilder
    from .contacts.contacts_request_builder import ContactsRequestBuilder
    from .contact_folders.contact_folders_request_builder import ContactFoldersRequestBuilder
    from .created_objects.created_objects_request_builder import CreatedObjectsRequestBuilder
    from .data_security_and_governance.data_security_and_governance_request_builder import DataSecurityAndGovernanceRequestBuilder
    from .device_management_troubleshooting_events.device_management_troubleshooting_events_request_builder import DeviceManagementTroubleshootingEventsRequestBuilder
    from .direct_reports.direct_reports_request_builder import DirectReportsRequestBuilder
    from .drive.drive_request_builder import DriveRequestBuilder
    from .drives.drives_request_builder import DrivesRequestBuilder
    from .employee_experience.employee_experience_request_builder import EmployeeExperienceRequestBuilder
    from .events.events_request_builder import EventsRequestBuilder
    from .export_device_and_app_management_data.export_device_and_app_management_data_request_builder import ExportDeviceAndAppManagementDataRequestBuilder
    from .export_device_and_app_management_data_with_skip_with_top.export_device_and_app_management_data_with_skip_with_top_request_builder import ExportDeviceAndAppManagementDataWithSkipWithTopRequestBuilder
    from .export_personal_data.export_personal_data_request_builder import ExportPersonalDataRequestBuilder
    from .extensions.extensions_request_builder import ExtensionsRequestBuilder
    from .find_meeting_times.find_meeting_times_request_builder import FindMeetingTimesRequestBuilder
    from .followed_sites.followed_sites_request_builder import FollowedSitesRequestBuilder
    from .get_mail_tips.get_mail_tips_request_builder import GetMailTipsRequestBuilder
    from .get_managed_app_diagnostic_statuses.get_managed_app_diagnostic_statuses_request_builder import GetManagedAppDiagnosticStatusesRequestBuilder
    from .get_managed_app_policies.get_managed_app_policies_request_builder import GetManagedAppPoliciesRequestBuilder
    from .get_managed_devices_with_app_failures.get_managed_devices_with_app_failures_request_builder import GetManagedDevicesWithAppFailuresRequestBuilder
    from .get_member_groups.get_member_groups_request_builder import GetMemberGroupsRequestBuilder
    from .get_member_objects.get_member_objects_request_builder import GetMemberObjectsRequestBuilder
    from .inference_classification.inference_classification_request_builder import InferenceClassificationRequestBuilder
    from .insights.insights_request_builder import InsightsRequestBuilder
    from .joined_teams.joined_teams_request_builder import JoinedTeamsRequestBuilder
    from .license_details.license_details_request_builder import LicenseDetailsRequestBuilder
    from .mailbox_settings.mailbox_settings_request_builder import MailboxSettingsRequestBuilder
    from .mail_folders.mail_folders_request_builder import MailFoldersRequestBuilder
    from .managed_app_registrations.managed_app_registrations_request_builder import ManagedAppRegistrationsRequestBuilder
    from .managed_devices.managed_devices_request_builder import ManagedDevicesRequestBuilder
    from .manager.manager_request_builder import ManagerRequestBuilder
    from .member_of.member_of_request_builder import MemberOfRequestBuilder
    from .messages.messages_request_builder import MessagesRequestBuilder
    from .oauth2_permission_grants.oauth2_permission_grants_request_builder import Oauth2PermissionGrantsRequestBuilder
    from .onenote.onenote_request_builder import OnenoteRequestBuilder
    from .online_meetings.online_meetings_request_builder import OnlineMeetingsRequestBuilder
    from .on_premises_sync_behavior.on_premises_sync_behavior_request_builder import OnPremisesSyncBehaviorRequestBuilder
    from .outlook.outlook_request_builder import OutlookRequestBuilder
    from .owned_devices.owned_devices_request_builder import OwnedDevicesRequestBuilder
    from .owned_objects.owned_objects_request_builder import OwnedObjectsRequestBuilder
    from .people.people_request_builder import PeopleRequestBuilder
    from .permission_grants.permission_grants_request_builder import PermissionGrantsRequestBuilder
    from .photo.photo_request_builder import PhotoRequestBuilder
    from .photos.photos_request_builder import PhotosRequestBuilder
    from .planner.planner_request_builder import PlannerRequestBuilder
    from .presence.presence_request_builder import PresenceRequestBuilder
    from .registered_devices.registered_devices_request_builder import RegisteredDevicesRequestBuilder
    from .reminder_view_with_start_date_time_with_end_date_time.reminder_view_with_start_date_time_with_end_date_time_request_builder import ReminderViewWithStartDateTimeWithEndDateTimeRequestBuilder
    from .remove_all_devices_from_management.remove_all_devices_from_management_request_builder import RemoveAllDevicesFromManagementRequestBuilder
    from .reprocess_license_assignment.reprocess_license_assignment_request_builder import ReprocessLicenseAssignmentRequestBuilder
    from .restore.restore_request_builder import RestoreRequestBuilder
    from .retry_service_provisioning.retry_service_provisioning_request_builder import RetryServiceProvisioningRequestBuilder
    from .revoke_sign_in_sessions.revoke_sign_in_sessions_request_builder import RevokeSignInSessionsRequestBuilder
    from .scoped_role_member_of.scoped_role_member_of_request_builder import ScopedRoleMemberOfRequestBuilder
    from .send_mail.send_mail_request_builder import SendMailRequestBuilder
    from .service_provisioning_errors.service_provisioning_errors_request_builder import ServiceProvisioningErrorsRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder
    from .solutions.solutions_request_builder import SolutionsRequestBuilder
    from .sponsors.sponsors_request_builder import SponsorsRequestBuilder
    from .teamwork.teamwork_request_builder import TeamworkRequestBuilder
    from .todo.todo_request_builder import TodoRequestBuilder
    from .transitive_member_of.transitive_member_of_request_builder import TransitiveMemberOfRequestBuilder
    from .translate_exchange_ids.translate_exchange_ids_request_builder import TranslateExchangeIdsRequestBuilder
    from .wipe_managed_app_registrations_by_device_tag.wipe_managed_app_registrations_by_device_tag_request_builder import WipeManagedAppRegistrationsByDeviceTagRequestBuilder

class UserItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of user entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new UserItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete a user object.   When deleted, user resources, including their mailbox and license assignments, are moved to a temporary container and if the user is restored within 30 days, these objects are restored to them. The user is also restored to any groups they were a member of. After 30 days and if not restored, the user object is permanently deleted and their assigned resources freed. To manage the deleted user object, see deletedItems.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/user-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def export_device_and_app_management_data_with_skip_with_top(self,skip: int, top: int) -> ExportDeviceAndAppManagementDataWithSkipWithTopRequestBuilder:
        """
        Provides operations to call the exportDeviceAndAppManagementData method.
        param skip: Usage: skip={skip}
        param top: Usage: top={top}
        Returns: ExportDeviceAndAppManagementDataWithSkipWithTopRequestBuilder
        """
        if skip is None:
            raise TypeError("skip cannot be null.")
        if top is None:
            raise TypeError("top cannot be null.")
        from .export_device_and_app_management_data_with_skip_with_top.export_device_and_app_management_data_with_skip_with_top_request_builder import ExportDeviceAndAppManagementDataWithSkipWithTopRequestBuilder

        return ExportDeviceAndAppManagementDataWithSkipWithTopRequestBuilder(self.request_adapter, self.path_parameters, skip, top)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[UserItemRequestBuilderGetQueryParameters]] = None) -> Optional[User]:
        """
        Retrieve the properties and relationships of user object. This operation returns by default only a subset of the more commonly used properties for each user. These default properties are noted in the Properties section. To get properties that are not returned by default, do a GET operation for the user and specify the properties in a $select OData query option. Because the user resource supports extensions, you can also use the GET operation to get custom properties and extension data in a user instance. Customers through Microsoft Entra ID for customers can also use this API operation to retrieve their details.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[User]
        Find more info here: https://learn.microsoft.com/graph/api/user-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.user import User

        return await self.request_adapter.send_async(request_info, User, error_mapping)
    
    async def patch(self,body: User, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[User]:
        """
        Update the properties of a user object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[User]
        Find more info here: https://learn.microsoft.com/graph/api/user-update?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.user import User

        return await self.request_adapter.send_async(request_info, User, error_mapping)
    
    def reminder_view_with_start_date_time_with_end_date_time(self,end_date_time: str, start_date_time: str) -> ReminderViewWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the reminderView method.
        param end_date_time: Usage: EndDateTime='{EndDateTime}'
        param start_date_time: Usage: StartDateTime='{StartDateTime}'
        Returns: ReminderViewWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if end_date_time is None:
            raise TypeError("end_date_time cannot be null.")
        if start_date_time is None:
            raise TypeError("start_date_time cannot be null.")
        from .reminder_view_with_start_date_time_with_end_date_time.reminder_view_with_start_date_time_with_end_date_time_request_builder import ReminderViewWithStartDateTimeWithEndDateTimeRequestBuilder

        return ReminderViewWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete a user object.   When deleted, user resources, including their mailbox and license assignments, are moved to a temporary container and if the user is restored within 30 days, these objects are restored to them. The user is also restored to any groups they were a member of. After 30 days and if not restored, the user object is permanently deleted and their assigned resources freed. To manage the deleted user object, see deletedItems.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[UserItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of user object. This operation returns by default only a subset of the more commonly used properties for each user. These default properties are noted in the Properties section. To get properties that are not returned by default, do a GET operation for the user and specify the properties in a $select OData query option. Because the user resource supports extensions, you can also use the GET operation to get custom properties and extension data in a user instance. Customers through Microsoft Entra ID for customers can also use this API operation to retrieve their details.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: User, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of a user object.
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
    
    def with_url(self,raw_url: str) -> UserItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: UserItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return UserItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def activities(self) -> ActivitiesRequestBuilder:
        """
        Provides operations to manage the activities property of the microsoft.graph.user entity.
        """
        from .activities.activities_request_builder import ActivitiesRequestBuilder

        return ActivitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def adhoc_calls(self) -> AdhocCallsRequestBuilder:
        """
        Provides operations to manage the adhocCalls property of the microsoft.graph.user entity.
        """
        from .adhoc_calls.adhoc_calls_request_builder import AdhocCallsRequestBuilder

        return AdhocCallsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def agreement_acceptances(self) -> AgreementAcceptancesRequestBuilder:
        """
        Provides operations to manage the agreementAcceptances property of the microsoft.graph.user entity.
        """
        from .agreement_acceptances.agreement_acceptances_request_builder import AgreementAcceptancesRequestBuilder

        return AgreementAcceptancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_role_assignments(self) -> AppRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the appRoleAssignments property of the microsoft.graph.user entity.
        """
        from .app_role_assignments.app_role_assignments_request_builder import AppRoleAssignmentsRequestBuilder

        return AppRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assign_license(self) -> AssignLicenseRequestBuilder:
        """
        Provides operations to call the assignLicense method.
        """
        from .assign_license.assign_license_request_builder import AssignLicenseRequestBuilder

        return AssignLicenseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication(self) -> AuthenticationRequestBuilder:
        """
        Provides operations to manage the authentication property of the microsoft.graph.user entity.
        """
        from .authentication.authentication_request_builder import AuthenticationRequestBuilder

        return AuthenticationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar(self) -> CalendarRequestBuilder:
        """
        Provides operations to manage the calendar property of the microsoft.graph.user entity.
        """
        from .calendar.calendar_request_builder import CalendarRequestBuilder

        return CalendarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar_groups(self) -> CalendarGroupsRequestBuilder:
        """
        Provides operations to manage the calendarGroups property of the microsoft.graph.user entity.
        """
        from .calendar_groups.calendar_groups_request_builder import CalendarGroupsRequestBuilder

        return CalendarGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar_view(self) -> CalendarViewRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.user entity.
        """
        from .calendar_view.calendar_view_request_builder import CalendarViewRequestBuilder

        return CalendarViewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendars(self) -> CalendarsRequestBuilder:
        """
        Provides operations to manage the calendars property of the microsoft.graph.user entity.
        """
        from .calendars.calendars_request_builder import CalendarsRequestBuilder

        return CalendarsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def change_password(self) -> ChangePasswordRequestBuilder:
        """
        Provides operations to call the changePassword method.
        """
        from .change_password.change_password_request_builder import ChangePasswordRequestBuilder

        return ChangePasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chats(self) -> ChatsRequestBuilder:
        """
        Provides operations to manage the chats property of the microsoft.graph.user entity.
        """
        from .chats.chats_request_builder import ChatsRequestBuilder

        return ChatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_member_groups(self) -> CheckMemberGroupsRequestBuilder:
        """
        Provides operations to call the checkMemberGroups method.
        """
        from .check_member_groups.check_member_groups_request_builder import CheckMemberGroupsRequestBuilder

        return CheckMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_member_objects(self) -> CheckMemberObjectsRequestBuilder:
        """
        Provides operations to call the checkMemberObjects method.
        """
        from .check_member_objects.check_member_objects_request_builder import CheckMemberObjectsRequestBuilder

        return CheckMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cloud_clipboard(self) -> CloudClipboardRequestBuilder:
        """
        Provides operations to manage the cloudClipboard property of the microsoft.graph.user entity.
        """
        from .cloud_clipboard.cloud_clipboard_request_builder import CloudClipboardRequestBuilder

        return CloudClipboardRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cloud_p_cs(self) -> CloudPCsRequestBuilder:
        """
        Provides operations to manage the cloudPCs property of the microsoft.graph.user entity.
        """
        from .cloud_p_cs.cloud_p_cs_request_builder import CloudPCsRequestBuilder

        return CloudPCsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contact_folders(self) -> ContactFoldersRequestBuilder:
        """
        Provides operations to manage the contactFolders property of the microsoft.graph.user entity.
        """
        from .contact_folders.contact_folders_request_builder import ContactFoldersRequestBuilder

        return ContactFoldersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contacts(self) -> ContactsRequestBuilder:
        """
        Provides operations to manage the contacts property of the microsoft.graph.user entity.
        """
        from .contacts.contacts_request_builder import ContactsRequestBuilder

        return ContactsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def created_objects(self) -> CreatedObjectsRequestBuilder:
        """
        Provides operations to manage the createdObjects property of the microsoft.graph.user entity.
        """
        from .created_objects.created_objects_request_builder import CreatedObjectsRequestBuilder

        return CreatedObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def data_security_and_governance(self) -> DataSecurityAndGovernanceRequestBuilder:
        """
        Provides operations to manage the dataSecurityAndGovernance property of the microsoft.graph.user entity.
        """
        from .data_security_and_governance.data_security_and_governance_request_builder import DataSecurityAndGovernanceRequestBuilder

        return DataSecurityAndGovernanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_management_troubleshooting_events(self) -> DeviceManagementTroubleshootingEventsRequestBuilder:
        """
        Provides operations to manage the deviceManagementTroubleshootingEvents property of the microsoft.graph.user entity.
        """
        from .device_management_troubleshooting_events.device_management_troubleshooting_events_request_builder import DeviceManagementTroubleshootingEventsRequestBuilder

        return DeviceManagementTroubleshootingEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def direct_reports(self) -> DirectReportsRequestBuilder:
        """
        Provides operations to manage the directReports property of the microsoft.graph.user entity.
        """
        from .direct_reports.direct_reports_request_builder import DirectReportsRequestBuilder

        return DirectReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive(self) -> DriveRequestBuilder:
        """
        Provides operations to manage the drive property of the microsoft.graph.user entity.
        """
        from .drive.drive_request_builder import DriveRequestBuilder

        return DriveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drives(self) -> DrivesRequestBuilder:
        """
        Provides operations to manage the drives property of the microsoft.graph.user entity.
        """
        from .drives.drives_request_builder import DrivesRequestBuilder

        return DrivesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def employee_experience(self) -> EmployeeExperienceRequestBuilder:
        """
        Provides operations to manage the employeeExperience property of the microsoft.graph.user entity.
        """
        from .employee_experience.employee_experience_request_builder import EmployeeExperienceRequestBuilder

        return EmployeeExperienceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def events(self) -> EventsRequestBuilder:
        """
        Provides operations to manage the events property of the microsoft.graph.user entity.
        """
        from .events.events_request_builder import EventsRequestBuilder

        return EventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def export_device_and_app_management_data(self) -> ExportDeviceAndAppManagementDataRequestBuilder:
        """
        Provides operations to call the exportDeviceAndAppManagementData method.
        """
        from .export_device_and_app_management_data.export_device_and_app_management_data_request_builder import ExportDeviceAndAppManagementDataRequestBuilder

        return ExportDeviceAndAppManagementDataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def export_personal_data(self) -> ExportPersonalDataRequestBuilder:
        """
        Provides operations to call the exportPersonalData method.
        """
        from .export_personal_data.export_personal_data_request_builder import ExportPersonalDataRequestBuilder

        return ExportPersonalDataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.user entity.
        """
        from .extensions.extensions_request_builder import ExtensionsRequestBuilder

        return ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def find_meeting_times(self) -> FindMeetingTimesRequestBuilder:
        """
        Provides operations to call the findMeetingTimes method.
        """
        from .find_meeting_times.find_meeting_times_request_builder import FindMeetingTimesRequestBuilder

        return FindMeetingTimesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def followed_sites(self) -> FollowedSitesRequestBuilder:
        """
        Provides operations to manage the followedSites property of the microsoft.graph.user entity.
        """
        from .followed_sites.followed_sites_request_builder import FollowedSitesRequestBuilder

        return FollowedSitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_mail_tips(self) -> GetMailTipsRequestBuilder:
        """
        Provides operations to call the getMailTips method.
        """
        from .get_mail_tips.get_mail_tips_request_builder import GetMailTipsRequestBuilder

        return GetMailTipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_managed_app_diagnostic_statuses(self) -> GetManagedAppDiagnosticStatusesRequestBuilder:
        """
        Provides operations to call the getManagedAppDiagnosticStatuses method.
        """
        from .get_managed_app_diagnostic_statuses.get_managed_app_diagnostic_statuses_request_builder import GetManagedAppDiagnosticStatusesRequestBuilder

        return GetManagedAppDiagnosticStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_managed_app_policies(self) -> GetManagedAppPoliciesRequestBuilder:
        """
        Provides operations to call the getManagedAppPolicies method.
        """
        from .get_managed_app_policies.get_managed_app_policies_request_builder import GetManagedAppPoliciesRequestBuilder

        return GetManagedAppPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_managed_devices_with_app_failures(self) -> GetManagedDevicesWithAppFailuresRequestBuilder:
        """
        Provides operations to call the getManagedDevicesWithAppFailures method.
        """
        from .get_managed_devices_with_app_failures.get_managed_devices_with_app_failures_request_builder import GetManagedDevicesWithAppFailuresRequestBuilder

        return GetManagedDevicesWithAppFailuresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_groups(self) -> GetMemberGroupsRequestBuilder:
        """
        Provides operations to call the getMemberGroups method.
        """
        from .get_member_groups.get_member_groups_request_builder import GetMemberGroupsRequestBuilder

        return GetMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_objects(self) -> GetMemberObjectsRequestBuilder:
        """
        Provides operations to call the getMemberObjects method.
        """
        from .get_member_objects.get_member_objects_request_builder import GetMemberObjectsRequestBuilder

        return GetMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def inference_classification(self) -> InferenceClassificationRequestBuilder:
        """
        Provides operations to manage the inferenceClassification property of the microsoft.graph.user entity.
        """
        from .inference_classification.inference_classification_request_builder import InferenceClassificationRequestBuilder

        return InferenceClassificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def insights(self) -> InsightsRequestBuilder:
        """
        Provides operations to manage the insights property of the microsoft.graph.user entity.
        """
        from .insights.insights_request_builder import InsightsRequestBuilder

        return InsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def joined_teams(self) -> JoinedTeamsRequestBuilder:
        """
        Provides operations to manage the joinedTeams property of the microsoft.graph.user entity.
        """
        from .joined_teams.joined_teams_request_builder import JoinedTeamsRequestBuilder

        return JoinedTeamsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def license_details(self) -> LicenseDetailsRequestBuilder:
        """
        Provides operations to manage the licenseDetails property of the microsoft.graph.user entity.
        """
        from .license_details.license_details_request_builder import LicenseDetailsRequestBuilder

        return LicenseDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mail_folders(self) -> MailFoldersRequestBuilder:
        """
        Provides operations to manage the mailFolders property of the microsoft.graph.user entity.
        """
        from .mail_folders.mail_folders_request_builder import MailFoldersRequestBuilder

        return MailFoldersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mailbox_settings(self) -> MailboxSettingsRequestBuilder:
        """
        The mailboxSettings property
        """
        from .mailbox_settings.mailbox_settings_request_builder import MailboxSettingsRequestBuilder

        return MailboxSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_app_registrations(self) -> ManagedAppRegistrationsRequestBuilder:
        """
        Provides operations to manage the managedAppRegistrations property of the microsoft.graph.user entity.
        """
        from .managed_app_registrations.managed_app_registrations_request_builder import ManagedAppRegistrationsRequestBuilder

        return ManagedAppRegistrationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_devices(self) -> ManagedDevicesRequestBuilder:
        """
        Provides operations to manage the managedDevices property of the microsoft.graph.user entity.
        """
        from .managed_devices.managed_devices_request_builder import ManagedDevicesRequestBuilder

        return ManagedDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def manager(self) -> ManagerRequestBuilder:
        """
        Provides operations to manage the manager property of the microsoft.graph.user entity.
        """
        from .manager.manager_request_builder import ManagerRequestBuilder

        return ManagerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_of(self) -> MemberOfRequestBuilder:
        """
        Provides operations to manage the memberOf property of the microsoft.graph.user entity.
        """
        from .member_of.member_of_request_builder import MemberOfRequestBuilder

        return MemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def messages(self) -> MessagesRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.user entity.
        """
        from .messages.messages_request_builder import MessagesRequestBuilder

        return MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oauth2_permission_grants(self) -> Oauth2PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the oauth2PermissionGrants property of the microsoft.graph.user entity.
        """
        from .oauth2_permission_grants.oauth2_permission_grants_request_builder import Oauth2PermissionGrantsRequestBuilder

        return Oauth2PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def on_premises_sync_behavior(self) -> OnPremisesSyncBehaviorRequestBuilder:
        """
        Provides operations to manage the onPremisesSyncBehavior property of the microsoft.graph.user entity.
        """
        from .on_premises_sync_behavior.on_premises_sync_behavior_request_builder import OnPremisesSyncBehaviorRequestBuilder

        return OnPremisesSyncBehaviorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def onenote(self) -> OnenoteRequestBuilder:
        """
        Provides operations to manage the onenote property of the microsoft.graph.user entity.
        """
        from .onenote.onenote_request_builder import OnenoteRequestBuilder

        return OnenoteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def online_meetings(self) -> OnlineMeetingsRequestBuilder:
        """
        Provides operations to manage the onlineMeetings property of the microsoft.graph.user entity.
        """
        from .online_meetings.online_meetings_request_builder import OnlineMeetingsRequestBuilder

        return OnlineMeetingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def outlook(self) -> OutlookRequestBuilder:
        """
        Provides operations to manage the outlook property of the microsoft.graph.user entity.
        """
        from .outlook.outlook_request_builder import OutlookRequestBuilder

        return OutlookRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owned_devices(self) -> OwnedDevicesRequestBuilder:
        """
        Provides operations to manage the ownedDevices property of the microsoft.graph.user entity.
        """
        from .owned_devices.owned_devices_request_builder import OwnedDevicesRequestBuilder

        return OwnedDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owned_objects(self) -> OwnedObjectsRequestBuilder:
        """
        Provides operations to manage the ownedObjects property of the microsoft.graph.user entity.
        """
        from .owned_objects.owned_objects_request_builder import OwnedObjectsRequestBuilder

        return OwnedObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def people(self) -> PeopleRequestBuilder:
        """
        Provides operations to manage the people property of the microsoft.graph.user entity.
        """
        from .people.people_request_builder import PeopleRequestBuilder

        return PeopleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permission_grants(self) -> PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the permissionGrants property of the microsoft.graph.user entity.
        """
        from .permission_grants.permission_grants_request_builder import PermissionGrantsRequestBuilder

        return PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def photo(self) -> PhotoRequestBuilder:
        """
        Provides operations to manage the photo property of the microsoft.graph.user entity.
        """
        from .photo.photo_request_builder import PhotoRequestBuilder

        return PhotoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def photos(self) -> PhotosRequestBuilder:
        """
        Provides operations to manage the photos property of the microsoft.graph.user entity.
        """
        from .photos.photos_request_builder import PhotosRequestBuilder

        return PhotosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def planner(self) -> PlannerRequestBuilder:
        """
        Provides operations to manage the planner property of the microsoft.graph.user entity.
        """
        from .planner.planner_request_builder import PlannerRequestBuilder

        return PlannerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def presence(self) -> PresenceRequestBuilder:
        """
        Provides operations to manage the presence property of the microsoft.graph.user entity.
        """
        from .presence.presence_request_builder import PresenceRequestBuilder

        return PresenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def registered_devices(self) -> RegisteredDevicesRequestBuilder:
        """
        Provides operations to manage the registeredDevices property of the microsoft.graph.user entity.
        """
        from .registered_devices.registered_devices_request_builder import RegisteredDevicesRequestBuilder

        return RegisteredDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_all_devices_from_management(self) -> RemoveAllDevicesFromManagementRequestBuilder:
        """
        Provides operations to call the removeAllDevicesFromManagement method.
        """
        from .remove_all_devices_from_management.remove_all_devices_from_management_request_builder import RemoveAllDevicesFromManagementRequestBuilder

        return RemoveAllDevicesFromManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reprocess_license_assignment(self) -> ReprocessLicenseAssignmentRequestBuilder:
        """
        Provides operations to call the reprocessLicenseAssignment method.
        """
        from .reprocess_license_assignment.reprocess_license_assignment_request_builder import ReprocessLicenseAssignmentRequestBuilder

        return ReprocessLicenseAssignmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore.restore_request_builder import RestoreRequestBuilder

        return RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retry_service_provisioning(self) -> RetryServiceProvisioningRequestBuilder:
        """
        Provides operations to call the retryServiceProvisioning method.
        """
        from .retry_service_provisioning.retry_service_provisioning_request_builder import RetryServiceProvisioningRequestBuilder

        return RetryServiceProvisioningRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def revoke_sign_in_sessions(self) -> RevokeSignInSessionsRequestBuilder:
        """
        Provides operations to call the revokeSignInSessions method.
        """
        from .revoke_sign_in_sessions.revoke_sign_in_sessions_request_builder import RevokeSignInSessionsRequestBuilder

        return RevokeSignInSessionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def scoped_role_member_of(self) -> ScopedRoleMemberOfRequestBuilder:
        """
        Provides operations to manage the scopedRoleMemberOf property of the microsoft.graph.user entity.
        """
        from .scoped_role_member_of.scoped_role_member_of_request_builder import ScopedRoleMemberOfRequestBuilder

        return ScopedRoleMemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_mail(self) -> SendMailRequestBuilder:
        """
        Provides operations to call the sendMail method.
        """
        from .send_mail.send_mail_request_builder import SendMailRequestBuilder

        return SendMailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_provisioning_errors(self) -> ServiceProvisioningErrorsRequestBuilder:
        """
        The serviceProvisioningErrors property
        """
        from .service_provisioning_errors.service_provisioning_errors_request_builder import ServiceProvisioningErrorsRequestBuilder

        return ServiceProvisioningErrorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.user entity.
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def solutions(self) -> SolutionsRequestBuilder:
        """
        Provides operations to manage the solutions property of the microsoft.graph.user entity.
        """
        from .solutions.solutions_request_builder import SolutionsRequestBuilder

        return SolutionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sponsors(self) -> SponsorsRequestBuilder:
        """
        Provides operations to manage the sponsors property of the microsoft.graph.user entity.
        """
        from .sponsors.sponsors_request_builder import SponsorsRequestBuilder

        return SponsorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teamwork(self) -> TeamworkRequestBuilder:
        """
        Provides operations to manage the teamwork property of the microsoft.graph.user entity.
        """
        from .teamwork.teamwork_request_builder import TeamworkRequestBuilder

        return TeamworkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def todo(self) -> TodoRequestBuilder:
        """
        Provides operations to manage the todo property of the microsoft.graph.user entity.
        """
        from .todo.todo_request_builder import TodoRequestBuilder

        return TodoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transitive_member_of(self) -> TransitiveMemberOfRequestBuilder:
        """
        Provides operations to manage the transitiveMemberOf property of the microsoft.graph.user entity.
        """
        from .transitive_member_of.transitive_member_of_request_builder import TransitiveMemberOfRequestBuilder

        return TransitiveMemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def translate_exchange_ids(self) -> TranslateExchangeIdsRequestBuilder:
        """
        Provides operations to call the translateExchangeIds method.
        """
        from .translate_exchange_ids.translate_exchange_ids_request_builder import TranslateExchangeIdsRequestBuilder

        return TranslateExchangeIdsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def wipe_managed_app_registrations_by_device_tag(self) -> WipeManagedAppRegistrationsByDeviceTagRequestBuilder:
        """
        Provides operations to call the wipeManagedAppRegistrationsByDeviceTag method.
        """
        from .wipe_managed_app_registrations_by_device_tag.wipe_managed_app_registrations_by_device_tag_request_builder import WipeManagedAppRegistrationsByDeviceTagRequestBuilder

        return WipeManagedAppRegistrationsByDeviceTagRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class UserItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class UserItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of user object. This operation returns by default only a subset of the more commonly used properties for each user. These default properties are noted in the Properties section. To get properties that are not returned by default, do a GET operation for the user and specify the properties in a $select OData query option. Because the user resource supports extensions, you can also use the GET operation to get custom properties and extension data in a user instance. Customers through Microsoft Entra ID for customers can also use this API operation to retrieve their details.
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
    class UserItemRequestBuilderGetRequestConfiguration(RequestConfiguration[UserItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class UserItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

