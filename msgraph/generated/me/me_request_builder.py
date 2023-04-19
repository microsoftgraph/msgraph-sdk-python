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
    from ..models import user
    from ..models.o_data_errors import o_data_error
    from .activities import activities_request_builder
    from .agreement_acceptances import agreement_acceptances_request_builder
    from .app_role_assignments import app_role_assignments_request_builder
    from .assign_license import assign_license_request_builder
    from .authentication import authentication_request_builder
    from .calendar import calendar_request_builder
    from .calendar_groups import calendar_groups_request_builder
    from .calendars import calendars_request_builder
    from .calendar_view import calendar_view_request_builder
    from .change_password import change_password_request_builder
    from .chats import chats_request_builder
    from .check_member_groups import check_member_groups_request_builder
    from .check_member_objects import check_member_objects_request_builder
    from .contact_folders import contact_folders_request_builder
    from .contacts import contacts_request_builder
    from .created_objects import created_objects_request_builder
    from .device_management_troubleshooting_events import device_management_troubleshooting_events_request_builder
    from .direct_reports import direct_reports_request_builder
    from .drive import drive_request_builder
    from .drives import drives_request_builder
    from .events import events_request_builder
    from .export_device_and_app_management_data import export_device_and_app_management_data_request_builder
    from .export_device_and_app_management_data_with_skip_with_top import export_device_and_app_management_data_with_skip_with_top_request_builder
    from .export_personal_data import export_personal_data_request_builder
    from .extensions import extensions_request_builder
    from .find_meeting_times import find_meeting_times_request_builder
    from .followed_sites import followed_sites_request_builder
    from .get_mail_tips import get_mail_tips_request_builder
    from .get_managed_app_diagnostic_statuses import get_managed_app_diagnostic_statuses_request_builder
    from .get_managed_app_policies import get_managed_app_policies_request_builder
    from .get_managed_devices_with_app_failures import get_managed_devices_with_app_failures_request_builder
    from .get_member_groups import get_member_groups_request_builder
    from .get_member_objects import get_member_objects_request_builder
    from .inference_classification import inference_classification_request_builder
    from .insights import insights_request_builder
    from .joined_teams import joined_teams_request_builder
    from .license_details import license_details_request_builder
    from .mailbox_settings import mailbox_settings_request_builder
    from .mail_folders import mail_folders_request_builder
    from .managed_app_registrations import managed_app_registrations_request_builder
    from .managed_devices import managed_devices_request_builder
    from .manager import manager_request_builder
    from .member_of import member_of_request_builder
    from .messages import messages_request_builder
    from .oauth2_permission_grants import oauth2_permission_grants_request_builder
    from .onenote import onenote_request_builder
    from .online_meetings import online_meetings_request_builder
    from .outlook import outlook_request_builder
    from .owned_devices import owned_devices_request_builder
    from .owned_objects import owned_objects_request_builder
    from .people import people_request_builder
    from .photo import photo_request_builder
    from .photos import photos_request_builder
    from .planner import planner_request_builder
    from .presence import presence_request_builder
    from .registered_devices import registered_devices_request_builder
    from .reminder_view_with_start_date_time_with_end_date_time import reminder_view_with_start_date_time_with_end_date_time_request_builder
    from .remove_all_devices_from_management import remove_all_devices_from_management_request_builder
    from .reprocess_license_assignment import reprocess_license_assignment_request_builder
    from .restore import restore_request_builder
    from .revoke_sign_in_sessions import revoke_sign_in_sessions_request_builder
    from .scoped_role_member_of import scoped_role_member_of_request_builder
    from .send_mail import send_mail_request_builder
    from .settings import settings_request_builder
    from .teamwork import teamwork_request_builder
    from .todo import todo_request_builder
    from .transitive_member_of import transitive_member_of_request_builder
    from .translate_exchange_ids import translate_exchange_ids_request_builder
    from .wipe_managed_app_registrations_by_device_tag import wipe_managed_app_registrations_by_device_tag_request_builder

class MeRequestBuilder():
    """
    Provides operations to manage the user singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MeRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/me{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def export_device_and_app_management_data_with_skip_with_top(self,skip: Optional[int] = None, top: Optional[int] = None) -> export_device_and_app_management_data_with_skip_with_top_request_builder.ExportDeviceAndAppManagementDataWithSkipWithTopRequestBuilder:
        """
        Provides operations to call the exportDeviceAndAppManagementData method.
        Args:
            skip: Usage: skip={skip}
            top: Usage: top={top}
        Returns: export_device_and_app_management_data_with_skip_with_top_request_builder.ExportDeviceAndAppManagementDataWithSkipWithTopRequestBuilder
        """
        if skip is None:
            raise Exception("skip cannot be undefined")
        if top is None:
            raise Exception("top cannot be undefined")
        from .export_device_and_app_management_data_with_skip_with_top import export_device_and_app_management_data_with_skip_with_top_request_builder

        return export_device_and_app_management_data_with_skip_with_top_request_builder.ExportDeviceAndAppManagementDataWithSkipWithTopRequestBuilder(self.request_adapter, self.path_parameters, skip, top)
    
    async def get(self,request_configuration: Optional[MeRequestBuilderGetRequestConfiguration] = None) -> Optional[user.User]:
        """
        Retrieve the properties and relationships of user object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[user.User]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import user

        return await self.request_adapter.send_async(request_info, user.User, error_mapping)
    
    async def patch(self,body: Optional[user.User] = None, request_configuration: Optional[MeRequestBuilderPatchRequestConfiguration] = None) -> Optional[user.User]:
        """
        Update the properties of a user object. Not all properties can be updated by Member or Guest users with their default permissions without Administrator roles. Compare member and guest default permissions to see properties they can manage.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[user.User]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models import user

        return await self.request_adapter.send_async(request_info, user.User, error_mapping)
    
    def reminder_view_with_start_date_time_with_end_date_time(self,end_date_time: Optional[str] = None, start_date_time: Optional[str] = None) -> reminder_view_with_start_date_time_with_end_date_time_request_builder.ReminderViewWithStartDateTimeWithEndDateTimeRequestBuilder:
        """
        Provides operations to call the reminderView method.
        Args:
            EndDateTime: Usage: EndDateTime='{EndDateTime}'
            StartDateTime: Usage: StartDateTime='{StartDateTime}'
        Returns: reminder_view_with_start_date_time_with_end_date_time_request_builder.ReminderViewWithStartDateTimeWithEndDateTimeRequestBuilder
        """
        if end_date_time is None:
            raise Exception("end_date_time cannot be undefined")
        if start_date_time is None:
            raise Exception("start_date_time cannot be undefined")
        from .reminder_view_with_start_date_time_with_end_date_time import reminder_view_with_start_date_time_with_end_date_time_request_builder

        return reminder_view_with_start_date_time_with_end_date_time_request_builder.ReminderViewWithStartDateTimeWithEndDateTimeRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, start_date_time)
    
    def to_get_request_information(self,request_configuration: Optional[MeRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of user object.
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
    
    def to_patch_request_information(self,body: Optional[user.User] = None, request_configuration: Optional[MeRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a user object. Not all properties can be updated by Member or Guest users with their default permissions without Administrator roles. Compare member and guest default permissions to see properties they can manage.
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
    def activities(self) -> activities_request_builder.ActivitiesRequestBuilder:
        """
        Provides operations to manage the activities property of the microsoft.graph.user entity.
        """
        from .activities import activities_request_builder

        return activities_request_builder.ActivitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def agreement_acceptances(self) -> agreement_acceptances_request_builder.AgreementAcceptancesRequestBuilder:
        """
        Provides operations to manage the agreementAcceptances property of the microsoft.graph.user entity.
        """
        from .agreement_acceptances import agreement_acceptances_request_builder

        return agreement_acceptances_request_builder.AgreementAcceptancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_role_assignments(self) -> app_role_assignments_request_builder.AppRoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the appRoleAssignments property of the microsoft.graph.user entity.
        """
        from .app_role_assignments import app_role_assignments_request_builder

        return app_role_assignments_request_builder.AppRoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def assign_license(self) -> assign_license_request_builder.AssignLicenseRequestBuilder:
        """
        Provides operations to call the assignLicense method.
        """
        from .assign_license import assign_license_request_builder

        return assign_license_request_builder.AssignLicenseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication(self) -> authentication_request_builder.AuthenticationRequestBuilder:
        """
        Provides operations to manage the authentication property of the microsoft.graph.user entity.
        """
        from .authentication import authentication_request_builder

        return authentication_request_builder.AuthenticationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar(self) -> calendar_request_builder.CalendarRequestBuilder:
        """
        Provides operations to manage the calendar property of the microsoft.graph.user entity.
        """
        from .calendar import calendar_request_builder

        return calendar_request_builder.CalendarRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar_groups(self) -> calendar_groups_request_builder.CalendarGroupsRequestBuilder:
        """
        Provides operations to manage the calendarGroups property of the microsoft.graph.user entity.
        """
        from .calendar_groups import calendar_groups_request_builder

        return calendar_groups_request_builder.CalendarGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendars(self) -> calendars_request_builder.CalendarsRequestBuilder:
        """
        Provides operations to manage the calendars property of the microsoft.graph.user entity.
        """
        from .calendars import calendars_request_builder

        return calendars_request_builder.CalendarsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar_view(self) -> calendar_view_request_builder.CalendarViewRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.user entity.
        """
        from .calendar_view import calendar_view_request_builder

        return calendar_view_request_builder.CalendarViewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def change_password(self) -> change_password_request_builder.ChangePasswordRequestBuilder:
        """
        Provides operations to call the changePassword method.
        """
        from .change_password import change_password_request_builder

        return change_password_request_builder.ChangePasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def chats(self) -> chats_request_builder.ChatsRequestBuilder:
        """
        Provides operations to manage the chats property of the microsoft.graph.user entity.
        """
        from .chats import chats_request_builder

        return chats_request_builder.ChatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_member_groups(self) -> check_member_groups_request_builder.CheckMemberGroupsRequestBuilder:
        """
        Provides operations to call the checkMemberGroups method.
        """
        from .check_member_groups import check_member_groups_request_builder

        return check_member_groups_request_builder.CheckMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def check_member_objects(self) -> check_member_objects_request_builder.CheckMemberObjectsRequestBuilder:
        """
        Provides operations to call the checkMemberObjects method.
        """
        from .check_member_objects import check_member_objects_request_builder

        return check_member_objects_request_builder.CheckMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contact_folders(self) -> contact_folders_request_builder.ContactFoldersRequestBuilder:
        """
        Provides operations to manage the contactFolders property of the microsoft.graph.user entity.
        """
        from .contact_folders import contact_folders_request_builder

        return contact_folders_request_builder.ContactFoldersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contacts(self) -> contacts_request_builder.ContactsRequestBuilder:
        """
        Provides operations to manage the contacts property of the microsoft.graph.user entity.
        """
        from .contacts import contacts_request_builder

        return contacts_request_builder.ContactsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def created_objects(self) -> created_objects_request_builder.CreatedObjectsRequestBuilder:
        """
        Provides operations to manage the createdObjects property of the microsoft.graph.user entity.
        """
        from .created_objects import created_objects_request_builder

        return created_objects_request_builder.CreatedObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_management_troubleshooting_events(self) -> device_management_troubleshooting_events_request_builder.DeviceManagementTroubleshootingEventsRequestBuilder:
        """
        Provides operations to manage the deviceManagementTroubleshootingEvents property of the microsoft.graph.user entity.
        """
        from .device_management_troubleshooting_events import device_management_troubleshooting_events_request_builder

        return device_management_troubleshooting_events_request_builder.DeviceManagementTroubleshootingEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def direct_reports(self) -> direct_reports_request_builder.DirectReportsRequestBuilder:
        """
        Provides operations to manage the directReports property of the microsoft.graph.user entity.
        """
        from .direct_reports import direct_reports_request_builder

        return direct_reports_request_builder.DirectReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive(self) -> drive_request_builder.DriveRequestBuilder:
        """
        Provides operations to manage the drive property of the microsoft.graph.user entity.
        """
        from .drive import drive_request_builder

        return drive_request_builder.DriveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drives(self) -> drives_request_builder.DrivesRequestBuilder:
        """
        Provides operations to manage the drives property of the microsoft.graph.user entity.
        """
        from .drives import drives_request_builder

        return drives_request_builder.DrivesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def events(self) -> events_request_builder.EventsRequestBuilder:
        """
        Provides operations to manage the events property of the microsoft.graph.user entity.
        """
        from .events import events_request_builder

        return events_request_builder.EventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def export_device_and_app_management_data(self) -> export_device_and_app_management_data_request_builder.ExportDeviceAndAppManagementDataRequestBuilder:
        """
        Provides operations to call the exportDeviceAndAppManagementData method.
        """
        from .export_device_and_app_management_data import export_device_and_app_management_data_request_builder

        return export_device_and_app_management_data_request_builder.ExportDeviceAndAppManagementDataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def export_personal_data(self) -> export_personal_data_request_builder.ExportPersonalDataRequestBuilder:
        """
        Provides operations to call the exportPersonalData method.
        """
        from .export_personal_data import export_personal_data_request_builder

        return export_personal_data_request_builder.ExportPersonalDataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def extensions(self) -> extensions_request_builder.ExtensionsRequestBuilder:
        """
        Provides operations to manage the extensions property of the microsoft.graph.user entity.
        """
        from .extensions import extensions_request_builder

        return extensions_request_builder.ExtensionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def find_meeting_times(self) -> find_meeting_times_request_builder.FindMeetingTimesRequestBuilder:
        """
        Provides operations to call the findMeetingTimes method.
        """
        from .find_meeting_times import find_meeting_times_request_builder

        return find_meeting_times_request_builder.FindMeetingTimesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def followed_sites(self) -> followed_sites_request_builder.FollowedSitesRequestBuilder:
        """
        Provides operations to manage the followedSites property of the microsoft.graph.user entity.
        """
        from .followed_sites import followed_sites_request_builder

        return followed_sites_request_builder.FollowedSitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_mail_tips(self) -> get_mail_tips_request_builder.GetMailTipsRequestBuilder:
        """
        Provides operations to call the getMailTips method.
        """
        from .get_mail_tips import get_mail_tips_request_builder

        return get_mail_tips_request_builder.GetMailTipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_managed_app_diagnostic_statuses(self) -> get_managed_app_diagnostic_statuses_request_builder.GetManagedAppDiagnosticStatusesRequestBuilder:
        """
        Provides operations to call the getManagedAppDiagnosticStatuses method.
        """
        from .get_managed_app_diagnostic_statuses import get_managed_app_diagnostic_statuses_request_builder

        return get_managed_app_diagnostic_statuses_request_builder.GetManagedAppDiagnosticStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_managed_app_policies(self) -> get_managed_app_policies_request_builder.GetManagedAppPoliciesRequestBuilder:
        """
        Provides operations to call the getManagedAppPolicies method.
        """
        from .get_managed_app_policies import get_managed_app_policies_request_builder

        return get_managed_app_policies_request_builder.GetManagedAppPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_managed_devices_with_app_failures(self) -> get_managed_devices_with_app_failures_request_builder.GetManagedDevicesWithAppFailuresRequestBuilder:
        """
        Provides operations to call the getManagedDevicesWithAppFailures method.
        """
        from .get_managed_devices_with_app_failures import get_managed_devices_with_app_failures_request_builder

        return get_managed_devices_with_app_failures_request_builder.GetManagedDevicesWithAppFailuresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_groups(self) -> get_member_groups_request_builder.GetMemberGroupsRequestBuilder:
        """
        Provides operations to call the getMemberGroups method.
        """
        from .get_member_groups import get_member_groups_request_builder

        return get_member_groups_request_builder.GetMemberGroupsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_member_objects(self) -> get_member_objects_request_builder.GetMemberObjectsRequestBuilder:
        """
        Provides operations to call the getMemberObjects method.
        """
        from .get_member_objects import get_member_objects_request_builder

        return get_member_objects_request_builder.GetMemberObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def inference_classification(self) -> inference_classification_request_builder.InferenceClassificationRequestBuilder:
        """
        Provides operations to manage the inferenceClassification property of the microsoft.graph.user entity.
        """
        from .inference_classification import inference_classification_request_builder

        return inference_classification_request_builder.InferenceClassificationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def insights(self) -> insights_request_builder.InsightsRequestBuilder:
        """
        Provides operations to manage the insights property of the microsoft.graph.user entity.
        """
        from .insights import insights_request_builder

        return insights_request_builder.InsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def joined_teams(self) -> joined_teams_request_builder.JoinedTeamsRequestBuilder:
        """
        Provides operations to manage the joinedTeams property of the microsoft.graph.user entity.
        """
        from .joined_teams import joined_teams_request_builder

        return joined_teams_request_builder.JoinedTeamsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def license_details(self) -> license_details_request_builder.LicenseDetailsRequestBuilder:
        """
        Provides operations to manage the licenseDetails property of the microsoft.graph.user entity.
        """
        from .license_details import license_details_request_builder

        return license_details_request_builder.LicenseDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mailbox_settings(self) -> mailbox_settings_request_builder.MailboxSettingsRequestBuilder:
        """
        The mailboxSettings property
        """
        from .mailbox_settings import mailbox_settings_request_builder

        return mailbox_settings_request_builder.MailboxSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mail_folders(self) -> mail_folders_request_builder.MailFoldersRequestBuilder:
        """
        Provides operations to manage the mailFolders property of the microsoft.graph.user entity.
        """
        from .mail_folders import mail_folders_request_builder

        return mail_folders_request_builder.MailFoldersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_app_registrations(self) -> managed_app_registrations_request_builder.ManagedAppRegistrationsRequestBuilder:
        """
        Provides operations to manage the managedAppRegistrations property of the microsoft.graph.user entity.
        """
        from .managed_app_registrations import managed_app_registrations_request_builder

        return managed_app_registrations_request_builder.ManagedAppRegistrationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_devices(self) -> managed_devices_request_builder.ManagedDevicesRequestBuilder:
        """
        Provides operations to manage the managedDevices property of the microsoft.graph.user entity.
        """
        from .managed_devices import managed_devices_request_builder

        return managed_devices_request_builder.ManagedDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def manager(self) -> manager_request_builder.ManagerRequestBuilder:
        """
        Provides operations to manage the manager property of the microsoft.graph.user entity.
        """
        from .manager import manager_request_builder

        return manager_request_builder.ManagerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def member_of(self) -> member_of_request_builder.MemberOfRequestBuilder:
        """
        Provides operations to manage the memberOf property of the microsoft.graph.user entity.
        """
        from .member_of import member_of_request_builder

        return member_of_request_builder.MemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def messages(self) -> messages_request_builder.MessagesRequestBuilder:
        """
        Provides operations to manage the messages property of the microsoft.graph.user entity.
        """
        from .messages import messages_request_builder

        return messages_request_builder.MessagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def oauth2_permission_grants(self) -> oauth2_permission_grants_request_builder.Oauth2PermissionGrantsRequestBuilder:
        """
        Provides operations to manage the oauth2PermissionGrants property of the microsoft.graph.user entity.
        """
        from .oauth2_permission_grants import oauth2_permission_grants_request_builder

        return oauth2_permission_grants_request_builder.Oauth2PermissionGrantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def onenote(self) -> onenote_request_builder.OnenoteRequestBuilder:
        """
        Provides operations to manage the onenote property of the microsoft.graph.user entity.
        """
        from .onenote import onenote_request_builder

        return onenote_request_builder.OnenoteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def online_meetings(self) -> online_meetings_request_builder.OnlineMeetingsRequestBuilder:
        """
        Provides operations to manage the onlineMeetings property of the microsoft.graph.user entity.
        """
        from .online_meetings import online_meetings_request_builder

        return online_meetings_request_builder.OnlineMeetingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def outlook(self) -> outlook_request_builder.OutlookRequestBuilder:
        """
        Provides operations to manage the outlook property of the microsoft.graph.user entity.
        """
        from .outlook import outlook_request_builder

        return outlook_request_builder.OutlookRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owned_devices(self) -> owned_devices_request_builder.OwnedDevicesRequestBuilder:
        """
        Provides operations to manage the ownedDevices property of the microsoft.graph.user entity.
        """
        from .owned_devices import owned_devices_request_builder

        return owned_devices_request_builder.OwnedDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def owned_objects(self) -> owned_objects_request_builder.OwnedObjectsRequestBuilder:
        """
        Provides operations to manage the ownedObjects property of the microsoft.graph.user entity.
        """
        from .owned_objects import owned_objects_request_builder

        return owned_objects_request_builder.OwnedObjectsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def people(self) -> people_request_builder.PeopleRequestBuilder:
        """
        Provides operations to manage the people property of the microsoft.graph.user entity.
        """
        from .people import people_request_builder

        return people_request_builder.PeopleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def photo(self) -> photo_request_builder.PhotoRequestBuilder:
        """
        Provides operations to manage the photo property of the microsoft.graph.user entity.
        """
        from .photo import photo_request_builder

        return photo_request_builder.PhotoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def photos(self) -> photos_request_builder.PhotosRequestBuilder:
        """
        Provides operations to manage the photos property of the microsoft.graph.user entity.
        """
        from .photos import photos_request_builder

        return photos_request_builder.PhotosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def planner(self) -> planner_request_builder.PlannerRequestBuilder:
        """
        Provides operations to manage the planner property of the microsoft.graph.user entity.
        """
        from .planner import planner_request_builder

        return planner_request_builder.PlannerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def presence(self) -> presence_request_builder.PresenceRequestBuilder:
        """
        Provides operations to manage the presence property of the microsoft.graph.user entity.
        """
        from .presence import presence_request_builder

        return presence_request_builder.PresenceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def registered_devices(self) -> registered_devices_request_builder.RegisteredDevicesRequestBuilder:
        """
        Provides operations to manage the registeredDevices property of the microsoft.graph.user entity.
        """
        from .registered_devices import registered_devices_request_builder

        return registered_devices_request_builder.RegisteredDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove_all_devices_from_management(self) -> remove_all_devices_from_management_request_builder.RemoveAllDevicesFromManagementRequestBuilder:
        """
        Provides operations to call the removeAllDevicesFromManagement method.
        """
        from .remove_all_devices_from_management import remove_all_devices_from_management_request_builder

        return remove_all_devices_from_management_request_builder.RemoveAllDevicesFromManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reprocess_license_assignment(self) -> reprocess_license_assignment_request_builder.ReprocessLicenseAssignmentRequestBuilder:
        """
        Provides operations to call the reprocessLicenseAssignment method.
        """
        from .reprocess_license_assignment import reprocess_license_assignment_request_builder

        return reprocess_license_assignment_request_builder.ReprocessLicenseAssignmentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> restore_request_builder.RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore import restore_request_builder

        return restore_request_builder.RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def revoke_sign_in_sessions(self) -> revoke_sign_in_sessions_request_builder.RevokeSignInSessionsRequestBuilder:
        """
        Provides operations to call the revokeSignInSessions method.
        """
        from .revoke_sign_in_sessions import revoke_sign_in_sessions_request_builder

        return revoke_sign_in_sessions_request_builder.RevokeSignInSessionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def scoped_role_member_of(self) -> scoped_role_member_of_request_builder.ScopedRoleMemberOfRequestBuilder:
        """
        Provides operations to manage the scopedRoleMemberOf property of the microsoft.graph.user entity.
        """
        from .scoped_role_member_of import scoped_role_member_of_request_builder

        return scoped_role_member_of_request_builder.ScopedRoleMemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_mail(self) -> send_mail_request_builder.SendMailRequestBuilder:
        """
        Provides operations to call the sendMail method.
        """
        from .send_mail import send_mail_request_builder

        return send_mail_request_builder.SendMailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> settings_request_builder.SettingsRequestBuilder:
        """
        Provides operations to manage the settings property of the microsoft.graph.user entity.
        """
        from .settings import settings_request_builder

        return settings_request_builder.SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def teamwork(self) -> teamwork_request_builder.TeamworkRequestBuilder:
        """
        Provides operations to manage the teamwork property of the microsoft.graph.user entity.
        """
        from .teamwork import teamwork_request_builder

        return teamwork_request_builder.TeamworkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def todo(self) -> todo_request_builder.TodoRequestBuilder:
        """
        Provides operations to manage the todo property of the microsoft.graph.user entity.
        """
        from .todo import todo_request_builder

        return todo_request_builder.TodoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def transitive_member_of(self) -> transitive_member_of_request_builder.TransitiveMemberOfRequestBuilder:
        """
        Provides operations to manage the transitiveMemberOf property of the microsoft.graph.user entity.
        """
        from .transitive_member_of import transitive_member_of_request_builder

        return transitive_member_of_request_builder.TransitiveMemberOfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def translate_exchange_ids(self) -> translate_exchange_ids_request_builder.TranslateExchangeIdsRequestBuilder:
        """
        Provides operations to call the translateExchangeIds method.
        """
        from .translate_exchange_ids import translate_exchange_ids_request_builder

        return translate_exchange_ids_request_builder.TranslateExchangeIdsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def wipe_managed_app_registrations_by_device_tag(self) -> wipe_managed_app_registrations_by_device_tag_request_builder.WipeManagedAppRegistrationsByDeviceTagRequestBuilder:
        """
        Provides operations to call the wipeManagedAppRegistrationsByDeviceTag method.
        """
        from .wipe_managed_app_registrations_by_device_tag import wipe_managed_app_registrations_by_device_tag_request_builder

        return wipe_managed_app_registrations_by_device_tag_request_builder.WipeManagedAppRegistrationsByDeviceTagRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MeRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of user object.
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
    class MeRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[MeRequestBuilder.MeRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class MeRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

