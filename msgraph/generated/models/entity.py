from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .aad_user_conversation_member import AadUserConversationMember
    from .access_package import AccessPackage
    from .access_package_assignment import AccessPackageAssignment
    from .access_package_assignment_policy import AccessPackageAssignmentPolicy
    from .access_package_assignment_request import AccessPackageAssignmentRequest
    from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
    from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
    from .access_package_catalog import AccessPackageCatalog
    from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
    from .access_package_question import AccessPackageQuestion
    from .access_package_resource import AccessPackageResource
    from .access_package_resource_environment import AccessPackageResourceEnvironment
    from .access_package_resource_request import AccessPackageResourceRequest
    from .access_package_resource_role import AccessPackageResourceRole
    from .access_package_resource_role_scope import AccessPackageResourceRoleScope
    from .access_package_resource_scope import AccessPackageResourceScope
    from .access_package_subject import AccessPackageSubject
    from .access_package_text_input_question import AccessPackageTextInputQuestion
    from .access_review_history_definition import AccessReviewHistoryDefinition
    from .access_review_history_instance import AccessReviewHistoryInstance
    from .access_review_instance import AccessReviewInstance
    from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
    from .access_review_reviewer import AccessReviewReviewer
    from .access_review_schedule_definition import AccessReviewScheduleDefinition
    from .access_review_set import AccessReviewSet
    from .access_review_stage import AccessReviewStage
    from .activities_container import ActivitiesContainer
    from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
    from .activity_history_item import ActivityHistoryItem
    from .add_large_gallery_view_operation import AddLargeGalleryViewOperation
    from .adhoc_call import AdhocCall
    from .administrative_unit import AdministrativeUnit
    from .admin_consent_request_policy import AdminConsentRequestPolicy
    from .admin_microsoft365_apps import AdminMicrosoft365Apps
    from .admin_report_settings import AdminReportSettings
    from .agreement import Agreement
    from .agreement_acceptance import AgreementAcceptance
    from .agreement_file import AgreementFile
    from .agreement_file_localization import AgreementFileLocalization
    from .agreement_file_properties import AgreementFileProperties
    from .agreement_file_version import AgreementFileVersion
    from .ai_interaction import AiInteraction
    from .ai_interaction_history import AiInteractionHistory
    from .ai_online_meeting import AiOnlineMeeting
    from .ai_user import AiUser
    from .akamai_web_application_firewall_provider import AkamaiWebApplicationFirewallProvider
    from .alert import Alert
    from .allowed_value import AllowedValue
    from .android_compliance_policy import AndroidCompliancePolicy
    from .android_custom_configuration import AndroidCustomConfiguration
    from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
    from .android_lob_app import AndroidLobApp
    from .android_managed_app_protection import AndroidManagedAppProtection
    from .android_managed_app_registration import AndroidManagedAppRegistration
    from .android_store_app import AndroidStoreApp
    from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy
    from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
    from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
    from .anonymous_guest_conversation_member import AnonymousGuestConversationMember
    from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
    from .apple_managed_identity_provider import AppleManagedIdentityProvider
    from .apple_push_notification_certificate import ApplePushNotificationCertificate
    from .application import Application
    from .application_template import ApplicationTemplate
    from .approval import Approval
    from .approval_stage import ApprovalStage
    from .app_catalogs import AppCatalogs
    from .app_consent_approval_route import AppConsentApprovalRoute
    from .app_consent_request import AppConsentRequest
    from .app_log_collection_request import AppLogCollectionRequest
    from .app_management_policy import AppManagementPolicy
    from .app_role_assignment import AppRoleAssignment
    from .app_scope import AppScope
    from .arkose_fraud_protection_provider import ArkoseFraudProtectionProvider
    from .associated_team_info import AssociatedTeamInfo
    from .attachment import Attachment
    from .attachment_base import AttachmentBase
    from .attachment_session import AttachmentSession
    from .attack_simulation_operation import AttackSimulationOperation
    from .attack_simulation_root import AttackSimulationRoot
    from .attendance_record import AttendanceRecord
    from .attribute_mapping_function_schema import AttributeMappingFunctionSchema
    from .attribute_set import AttributeSet
    from .audio_routing_group import AudioRoutingGroup
    from .audit_event import AuditEvent
    from .audit_log_root import AuditLogRoot
    from .authentication import Authentication
    from .authentication_combination_configuration import AuthenticationCombinationConfiguration
    from .authentication_context_class_reference import AuthenticationContextClassReference
    from .authentication_events_flow import AuthenticationEventsFlow
    from .authentication_event_listener import AuthenticationEventListener
    from .authentication_flows_policy import AuthenticationFlowsPolicy
    from .authentication_method import AuthenticationMethod
    from .authentication_methods_policy import AuthenticationMethodsPolicy
    from .authentication_methods_root import AuthenticationMethodsRoot
    from .authentication_method_configuration import AuthenticationMethodConfiguration
    from .authentication_method_mode_detail import AuthenticationMethodModeDetail
    from .authentication_method_target import AuthenticationMethodTarget
    from .authentication_strength_policy import AuthenticationStrengthPolicy
    from .authentication_strength_root import AuthenticationStrengthRoot
    from .authored_note import AuthoredNote
    from .authorization_policy import AuthorizationPolicy
    from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember
    from .b2x_identity_user_flow import B2xIdentityUserFlow
    from .backup_restore_root import BackupRestoreRoot
    from .base_item import BaseItem
    from .base_item_version import BaseItemVersion
    from .base_map_feature import BaseMapFeature
    from .base_site_page import BaseSitePage
    from .bitlocker import Bitlocker
    from .bitlocker_recovery_key import BitlockerRecoveryKey
    from .booking_appointment import BookingAppointment
    from .booking_business import BookingBusiness
    from .booking_currency import BookingCurrency
    from .booking_customer import BookingCustomer
    from .booking_customer_base import BookingCustomerBase
    from .booking_custom_question import BookingCustomQuestion
    from .booking_service import BookingService
    from .booking_staff_member import BookingStaffMember
    from .booking_staff_member_base import BookingStaffMemberBase
    from .browser_shared_cookie import BrowserSharedCookie
    from .browser_site import BrowserSite
    from .browser_site_list import BrowserSiteList
    from .building import Building
    from .building_map import BuildingMap
    from .built_in_identity_provider import BuiltInIdentityProvider
    from .bulk_upload import BulkUpload
    from .calendar import Calendar
    from .calendar_group import CalendarGroup
    from .calendar_permission import CalendarPermission
    from .calendar_sharing_message import CalendarSharingMessage
    from .call import Call
    from .call_ai_insight import CallAiInsight
    from .call_event import CallEvent
    from .call_recording import CallRecording
    from .call_records.call_record import CallRecord
    from .call_records.organizer import Organizer
    from .call_records.participant import Participant
    from .call_records.participant_base import ParticipantBase
    from .call_records.segment import Segment
    from .call_records.session import Session
    from .call_transcript import CallTranscript
    from .cancel_media_processing_operation import CancelMediaProcessingOperation
    from .canvas_layout import CanvasLayout
    from .certificate_authority_detail import CertificateAuthorityDetail
    from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration
    from .certificate_based_auth_pki import CertificateBasedAuthPki
    from .change_tracked_entity import ChangeTrackedEntity
    from .channel import Channel
    from .chat import Chat
    from .chat_message import ChatMessage
    from .chat_message_hosted_content import ChatMessageHostedContent
    from .chat_message_info import ChatMessageInfo
    from .checklist_item import ChecklistItem
    from .claims_mapping_policy import ClaimsMappingPolicy
    from .cloud_clipboard_item import CloudClipboardItem
    from .cloud_clipboard_root import CloudClipboardRoot
    from .cloud_flare_web_application_firewall_provider import CloudFlareWebApplicationFirewallProvider
    from .cloud_pc_audit_event import CloudPcAuditEvent
    from .cloud_pc_device_image import CloudPcDeviceImage
    from .cloud_pc_gallery_image import CloudPcGalleryImage
    from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
    from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
    from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment
    from .cloud_pc_report import CloudPcReport
    from .cloud_pc_user_setting import CloudPcUserSetting
    from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment
    from .cloud_p_c import CloudPC
    from .column_definition import ColumnDefinition
    from .column_link import ColumnLink
    from .comms_operation import CommsOperation
    from .community import Community
    from .company_subscription import CompanySubscription
    from .compliance_management_partner import ComplianceManagementPartner
    from .conditional_access_policy import ConditionalAccessPolicy
    from .conditional_access_root import ConditionalAccessRoot
    from .conditional_access_template import ConditionalAccessTemplate
    from .connected_organization import ConnectedOrganization
    from .contact import Contact
    from .contact_folder import ContactFolder
    from .content_activity import ContentActivity
    from .content_sharing_session import ContentSharingSession
    from .content_type import ContentType
    from .contract import Contract
    from .conversation import Conversation
    from .conversation_member import ConversationMember
    from .conversation_thread import ConversationThread
    from .copilot_admin import CopilotAdmin
    from .copilot_admin_limited_mode import CopilotAdminLimitedMode
    from .copilot_admin_setting import CopilotAdminSetting
    from .copilot_report_root import CopilotReportRoot
    from .country_named_location import CountryNamedLocation
    from .cross_tenant_access_policy import CrossTenantAccessPolicy
    from .cross_tenant_access_policy_configuration_default import CrossTenantAccessPolicyConfigurationDefault
    from .custom_authentication_extension import CustomAuthenticationExtension
    from .custom_callout_extension import CustomCalloutExtension
    from .custom_extension_stage_setting import CustomExtensionStageSetting
    from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
    from .data_policy_operation import DataPolicyOperation
    from .data_security_and_governance import DataSecurityAndGovernance
    from .day_note import DayNote
    from .default_managed_app_protection import DefaultManagedAppProtection
    from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment
    from .delegated_admin_customer import DelegatedAdminCustomer
    from .delegated_admin_relationship import DelegatedAdminRelationship
    from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation
    from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest
    from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail
    from .delegated_permission_classification import DelegatedPermissionClassification
    from .deleted_chat import DeletedChat
    from .deleted_item_container import DeletedItemContainer
    from .deleted_team import DeletedTeam
    from .delta_participants import DeltaParticipants
    from .desk import Desk
    from .detected_app import DetectedApp
    from .device import Device
    from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
    from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition
    from .device_app_management import DeviceAppManagement
    from .device_category import DeviceCategory
    from .device_compliance_action_item import DeviceComplianceActionItem
    from .device_compliance_device_overview import DeviceComplianceDeviceOverview
    from .device_compliance_device_status import DeviceComplianceDeviceStatus
    from .device_compliance_policy import DeviceCompliancePolicy
    from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
    from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
    from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
    from .device_compliance_policy_state import DeviceCompliancePolicyState
    from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
    from .device_compliance_setting_state import DeviceComplianceSettingState
    from .device_compliance_user_overview import DeviceComplianceUserOverview
    from .device_compliance_user_status import DeviceComplianceUserStatus
    from .device_configuration import DeviceConfiguration
    from .device_configuration_assignment import DeviceConfigurationAssignment
    from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
    from .device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
    from .device_configuration_device_status import DeviceConfigurationDeviceStatus
    from .device_configuration_state import DeviceConfigurationState
    from .device_configuration_user_overview import DeviceConfigurationUserOverview
    from .device_configuration_user_status import DeviceConfigurationUserStatus
    from .device_enrollment_configuration import DeviceEnrollmentConfiguration
    from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration
    from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration
    from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration
    from .device_install_state import DeviceInstallState
    from .device_local_credential_info import DeviceLocalCredentialInfo
    from .device_log_collection_response import DeviceLogCollectionResponse
    from .device_management import DeviceManagement
    from .device_management_cached_report_configuration import DeviceManagementCachedReportConfiguration
    from .device_management_exchange_connector import DeviceManagementExchangeConnector
    from .device_management_export_job import DeviceManagementExportJob
    from .device_management_partner import DeviceManagementPartner
    from .device_management_reports import DeviceManagementReports
    from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
    from .device_registration_policy import DeviceRegistrationPolicy
    from .directory import Directory
    from .directory_audit import DirectoryAudit
    from .directory_definition import DirectoryDefinition
    from .directory_object import DirectoryObject
    from .directory_object_partner_reference import DirectoryObjectPartnerReference
    from .directory_role import DirectoryRole
    from .directory_role_template import DirectoryRoleTemplate
    from .document_set_version import DocumentSetVersion
    from .domain import Domain
    from .domain_dns_cname_record import DomainDnsCnameRecord
    from .domain_dns_mx_record import DomainDnsMxRecord
    from .domain_dns_record import DomainDnsRecord
    from .domain_dns_srv_record import DomainDnsSrvRecord
    from .domain_dns_txt_record import DomainDnsTxtRecord
    from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
    from .drive import Drive
    from .drive_item import DriveItem
    from .drive_item_version import DriveItemVersion
    from .drive_protection_rule import DriveProtectionRule
    from .drive_protection_unit import DriveProtectionUnit
    from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob
    from .drive_restore_artifact import DriveRestoreArtifact
    from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest
    from .edge import Edge
    from .edition_upgrade_configuration import EditionUpgradeConfiguration
    from .education_assignment import EducationAssignment
    from .education_assignment_defaults import EducationAssignmentDefaults
    from .education_assignment_resource import EducationAssignmentResource
    from .education_assignment_settings import EducationAssignmentSettings
    from .education_category import EducationCategory
    from .education_class import EducationClass
    from .education_feedback_outcome import EducationFeedbackOutcome
    from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome
    from .education_grading_category import EducationGradingCategory
    from .education_grading_scheme import EducationGradingScheme
    from .education_module import EducationModule
    from .education_module_resource import EducationModuleResource
    from .education_organization import EducationOrganization
    from .education_outcome import EducationOutcome
    from .education_points_outcome import EducationPointsOutcome
    from .education_rubric import EducationRubric
    from .education_rubric_outcome import EducationRubricOutcome
    from .education_school import EducationSchool
    from .education_submission import EducationSubmission
    from .education_submission_resource import EducationSubmissionResource
    from .education_user import EducationUser
    from .email_authentication_method import EmailAuthenticationMethod
    from .email_authentication_method_configuration import EmailAuthenticationMethodConfiguration
    from .email_file_assessment_request import EmailFileAssessmentRequest
    from .emergency_call_event import EmergencyCallEvent
    from .employee_experience_user import EmployeeExperienceUser
    from .endpoint import Endpoint
    from .end_user_notification import EndUserNotification
    from .end_user_notification_detail import EndUserNotificationDetail
    from .engagement_async_operation import EngagementAsyncOperation
    from .engagement_conversation import EngagementConversation
    from .engagement_conversation_discussion_message import EngagementConversationDiscussionMessage
    from .engagement_conversation_message import EngagementConversationMessage
    from .engagement_conversation_message_reaction import EngagementConversationMessageReaction
    from .engagement_conversation_question_message import EngagementConversationQuestionMessage
    from .engagement_conversation_system_message import EngagementConversationSystemMessage
    from .engagement_role import EngagementRole
    from .engagement_role_member import EngagementRoleMember
    from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
    from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
    from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate
    from .entitlement_management import EntitlementManagement
    from .entitlement_management_settings import EntitlementManagementSettings
    from .event import Event
    from .event_message import EventMessage
    from .event_message_request import EventMessageRequest
    from .event_message_response import EventMessageResponse
    from .exchange_protection_policy import ExchangeProtectionPolicy
    from .exchange_restore_session import ExchangeRestoreSession
    from .extension import Extension
    from .extension_property import ExtensionProperty
    from .external_connectors.connection_operation import ConnectionOperation
    from .external_connectors.external_activity import ExternalActivity
    from .external_connectors.external_activity_result import ExternalActivityResult
    from .external_connectors.external_connection import ExternalConnection
    from .external_connectors.external_group import ExternalGroup
    from .external_connectors.external_item import ExternalItem
    from .external_connectors.identity import Identity
    from .external_connectors.schema import Schema
    from .external_domain_name import ExternalDomainName
    from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow
    from .e_book_install_summary import EBookInstallSummary
    from .feature_rollout_policy import FeatureRolloutPolicy
    from .federated_identity_credential import FederatedIdentityCredential
    from .fido2_authentication_method import Fido2AuthenticationMethod
    from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration
    from .fido2_combination_configuration import Fido2CombinationConfiguration
    from .field_value_set import FieldValueSet
    from .file_assessment_request import FileAssessmentRequest
    from .file_attachment import FileAttachment
    from .file_storage import FileStorage
    from .file_storage_container import FileStorageContainer
    from .file_storage_container_type import FileStorageContainerType
    from .file_storage_container_type_registration import FileStorageContainerTypeRegistration
    from .filter_operator_schema import FilterOperatorSchema
    from .fixture_map import FixtureMap
    from .floor import Floor
    from .footprint_map import FootprintMap
    from .fraud_protection_provider import FraudProtectionProvider
    from .governance_insight import GovernanceInsight
    from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
    from .group import Group
    from .group_lifecycle_policy import GroupLifecyclePolicy
    from .group_setting import GroupSetting
    from .group_setting_template import GroupSettingTemplate
    from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
    from .horizontal_section import HorizontalSection
    from .horizontal_section_column import HorizontalSectionColumn
    from .human_security_fraud_protection_provider import HumanSecurityFraudProtectionProvider
    from .identity_api_connector import IdentityApiConnector
    from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
    from .identity_container import IdentityContainer
    from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute
    from .identity_governance.custom_task_extension import CustomTaskExtension
    from .identity_governance.insights import Insights
    from .identity_governance.lifecycle_management_settings import LifecycleManagementSettings
    from .identity_governance.lifecycle_workflows_container import LifecycleWorkflowsContainer
    from .identity_governance.run import Run
    from .identity_governance.task import Task
    from .identity_governance.task_definition import TaskDefinition
    from .identity_governance.task_processing_result import TaskProcessingResult
    from .identity_governance.task_report import TaskReport
    from .identity_governance.user_processing_result import UserProcessingResult
    from .identity_governance.workflow_template import WorkflowTemplate
    from .identity_provider import IdentityProvider
    from .identity_provider_base import IdentityProviderBase
    from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
    from .identity_user_flow import IdentityUserFlow
    from .identity_user_flow_attribute import IdentityUserFlowAttribute
    from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
    from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
    from .imported_windows_autopilot_device_identity_upload import ImportedWindowsAutopilotDeviceIdentityUpload
    from .inference_classification import InferenceClassification
    from .inference_classification_override import InferenceClassificationOverride
    from .insights_settings import InsightsSettings
    from .internal_domain_federation import InternalDomainFederation
    from .internet_explorer_mode import InternetExplorerMode
    from .invitation import Invitation
    from .invite_participants_operation import InviteParticipantsOperation
    from .iosi_pad_o_s_web_clip import IosiPadOSWebClip
    from .ios_certificate_profile import IosCertificateProfile
    from .ios_compliance_policy import IosCompliancePolicy
    from .ios_custom_configuration import IosCustomConfiguration
    from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
    from .ios_general_device_configuration import IosGeneralDeviceConfiguration
    from .ios_lob_app import IosLobApp
    from .ios_lob_app_provisioning_configuration_assignment import IosLobAppProvisioningConfigurationAssignment
    from .ios_managed_app_protection import IosManagedAppProtection
    from .ios_managed_app_registration import IosManagedAppRegistration
    from .ios_mobile_app_configuration import IosMobileAppConfiguration
    from .ios_store_app import IosStoreApp
    from .ios_update_configuration import IosUpdateConfiguration
    from .ios_update_device_status import IosUpdateDeviceStatus
    from .ios_vpp_app import IosVppApp
    from .ios_vpp_e_book import IosVppEBook
    from .ios_vpp_e_book_assignment import IosVppEBookAssignment
    from .ip_named_location import IpNamedLocation
    from .item_activity import ItemActivity
    from .item_activity_stat import ItemActivityStat
    from .item_analytics import ItemAnalytics
    from .item_attachment import ItemAttachment
    from .item_insights import ItemInsights
    from .item_retention_label import ItemRetentionLabel
    from .label_content_right import LabelContentRight
    from .landing_page import LandingPage
    from .landing_page_detail import LandingPageDetail
    from .learning_assignment import LearningAssignment
    from .learning_content import LearningContent
    from .learning_course_activity import LearningCourseActivity
    from .learning_provider import LearningProvider
    from .learning_self_initiated_course import LearningSelfInitiatedCourse
    from .level_map import LevelMap
    from .license_details import LicenseDetails
    from .linked_resource import LinkedResource
    from .list_ import List_
    from .list_item import ListItem
    from .list_item_version import ListItemVersion
    from .localized_notification_message import LocalizedNotificationMessage
    from .login_page import LoginPage
    from .long_running_operation import LongRunningOperation
    from .m365_apps_installation_options import M365AppsInstallationOptions
    from .mac_o_s_compliance_policy import MacOSCompliancePolicy
    from .mac_o_s_custom_configuration import MacOSCustomConfiguration
    from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
    from .mac_o_s_dmg_app import MacOSDmgApp
    from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
    from .mac_o_s_lob_app import MacOSLobApp
    from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp
    from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp
    from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp
    from .mailbox_protection_rule import MailboxProtectionRule
    from .mailbox_protection_unit import MailboxProtectionUnit
    from .mailbox_protection_units_bulk_addition_job import MailboxProtectionUnitsBulkAdditionJob
    from .mailbox_restore_artifact import MailboxRestoreArtifact
    from .mailbox_restore_artifacts_bulk_addition_request import MailboxRestoreArtifactsBulkAdditionRequest
    from .mail_assessment_request import MailAssessmentRequest
    from .mail_folder import MailFolder
    from .mail_search_folder import MailSearchFolder
    from .malware_state_for_windows_device import MalwareStateForWindowsDevice
    from .managed_android_lob_app import ManagedAndroidLobApp
    from .managed_android_store_app import ManagedAndroidStoreApp
    from .managed_app import ManagedApp
    from .managed_app_configuration import ManagedAppConfiguration
    from .managed_app_operation import ManagedAppOperation
    from .managed_app_policy import ManagedAppPolicy
    from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
    from .managed_app_protection import ManagedAppProtection
    from .managed_app_registration import ManagedAppRegistration
    from .managed_app_status import ManagedAppStatus
    from .managed_app_status_raw import ManagedAppStatusRaw
    from .managed_device import ManagedDevice
    from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
    from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
    from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
    from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary
    from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
    from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary
    from .managed_device_overview import ManagedDeviceOverview
    from .managed_e_book import ManagedEBook
    from .managed_e_book_assignment import ManagedEBookAssignment
    from .managed_i_o_s_lob_app import ManagedIOSLobApp
    from .managed_i_o_s_store_app import ManagedIOSStoreApp
    from .managed_mobile_app import ManagedMobileApp
    from .managed_mobile_lob_app import ManagedMobileLobApp
    from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
    from .meeting_attendance_report import MeetingAttendanceReport
    from .membership_outlier_insight import MembershipOutlierInsight
    from .message import Message
    from .message_rule import MessageRule
    from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember
    from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
    from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration
    from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
    from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp
    from .mobile_app import MobileApp
    from .mobile_app_assignment import MobileAppAssignment
    from .mobile_app_category import MobileAppCategory
    from .mobile_app_content import MobileAppContent
    from .mobile_app_content_file import MobileAppContentFile
    from .mobile_app_relationship import MobileAppRelationship
    from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
    from .mobile_contained_app import MobileContainedApp
    from .mobile_lob_app import MobileLobApp
    from .mobile_threat_defense_connector import MobileThreatDefenseConnector
    from .multi_tenant_organization import MultiTenantOrganization
    from .multi_tenant_organization_identity_sync_policy_template import MultiTenantOrganizationIdentitySyncPolicyTemplate
    from .multi_tenant_organization_join_request_record import MultiTenantOrganizationJoinRequestRecord
    from .multi_tenant_organization_member import MultiTenantOrganizationMember
    from .multi_tenant_organization_partner_configuration_template import MultiTenantOrganizationPartnerConfigurationTemplate
    from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
    from .mute_participant_operation import MuteParticipantOperation
    from .named_location import NamedLocation
    from .notebook import Notebook
    from .notification_message_template import NotificationMessageTemplate
    from .offer_shift_request import OfferShiftRequest
    from .office_graph_insights import OfficeGraphInsights
    from .onenote import Onenote
    from .onenote_entity_base_model import OnenoteEntityBaseModel
    from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
    from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
    from .onenote_operation import OnenoteOperation
    from .onenote_page import OnenotePage
    from .onenote_resource import OnenoteResource
    from .onenote_section import OnenoteSection
    from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
    from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
    from .online_meeting import OnlineMeeting
    from .online_meeting_base import OnlineMeetingBase
    from .online_meeting_engagement_conversation import OnlineMeetingEngagementConversation
    from .on_attribute_collection_listener import OnAttributeCollectionListener
    from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
    from .on_attribute_collection_start_listener import OnAttributeCollectionStartListener
    from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
    from .on_attribute_collection_submit_listener import OnAttributeCollectionSubmitListener
    from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener
    from .on_email_otp_send_listener import OnEmailOtpSendListener
    from .on_fraud_protection_load_start_listener import OnFraudProtectionLoadStartListener
    from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener
    from .on_otp_send_custom_extension import OnOtpSendCustomExtension
    from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
    from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
    from .on_premises_sync_behavior import OnPremisesSyncBehavior
    from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension
    from .on_token_issuance_start_listener import OnTokenIssuanceStartListener
    from .on_user_create_start_listener import OnUserCreateStartListener
    from .open_shift import OpenShift
    from .open_shift_change_request import OpenShiftChangeRequest
    from .open_type_extension import OpenTypeExtension
    from .operation import Operation
    from .organization import Organization
    from .organizational_branding import OrganizationalBranding
    from .organizational_branding_localization import OrganizationalBrandingLocalization
    from .organizational_branding_properties import OrganizationalBrandingProperties
    from .org_contact import OrgContact
    from .outlook_category import OutlookCategory
    from .outlook_item import OutlookItem
    from .outlook_user import OutlookUser
    from .o_auth2_permission_grant import OAuth2PermissionGrant
    from .participant import Participant
    from .participant_joining_notification import ParticipantJoiningNotification
    from .participant_left_notification import ParticipantLeftNotification
    from .partners.billing.azure_usage import AzureUsage
    from .partners.billing.billed_reconciliation import BilledReconciliation
    from .partners.billing.billed_usage import BilledUsage
    from .partners.billing.billing import Billing
    from .partners.billing.billing_reconciliation import BillingReconciliation
    from .partners.billing.export_success_operation import ExportSuccessOperation
    from .partners.billing.failed_operation import FailedOperation
    from .partners.billing.manifest import Manifest
    from .partners.billing.operation import Operation
    from .partners.billing.running_operation import RunningOperation
    from .partners.billing.unbilled_reconciliation import UnbilledReconciliation
    from .partners.billing.unbilled_usage import UnbilledUsage
    from .partners.partners import Partners
    from .password_authentication_method import PasswordAuthenticationMethod
    from .payload import Payload
    from .people_admin_settings import PeopleAdminSettings
    from .permission import Permission
    from .permission_grant_condition_set import PermissionGrantConditionSet
    from .permission_grant_policy import PermissionGrantPolicy
    from .person import Person
    from .phone_authentication_method import PhoneAuthenticationMethod
    from .phone_user_conversation_member import PhoneUserConversationMember
    from .pinned_chat_message_info import PinnedChatMessageInfo
    from .place import Place
    from .planner import Planner
    from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
    from .planner_bucket import PlannerBucket
    from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
    from .planner_group import PlannerGroup
    from .planner_plan import PlannerPlan
    from .planner_plan_details import PlannerPlanDetails
    from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
    from .planner_task import PlannerTask
    from .planner_task_details import PlannerTaskDetails
    from .planner_user import PlannerUser
    from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
    from .play_prompt_operation import PlayPromptOperation
    from .policy_base import PolicyBase
    from .policy_root import PolicyRoot
    from .policy_template import PolicyTemplate
    from .post import Post
    from .presence import Presence
    from .printer import Printer
    from .printer_base import PrinterBase
    from .printer_create_operation import PrinterCreateOperation
    from .printer_share import PrinterShare
    from .print_connector import PrintConnector
    from .print_document import PrintDocument
    from .print_job import PrintJob
    from .print_operation import PrintOperation
    from .print_service import PrintService
    from .print_service_endpoint import PrintServiceEndpoint
    from .print_task import PrintTask
    from .print_task_definition import PrintTaskDefinition
    from .print_task_trigger import PrintTaskTrigger
    from .print_usage import PrintUsage
    from .print_usage_by_printer import PrintUsageByPrinter
    from .print_usage_by_user import PrintUsageByUser
    from .privileged_access_group import PrivilegedAccessGroup
    from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
    from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
    from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
    from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
    from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
    from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
    from .privileged_access_root import PrivilegedAccessRoot
    from .privileged_access_schedule import PrivilegedAccessSchedule
    from .privileged_access_schedule_instance import PrivilegedAccessScheduleInstance
    from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest
    from .profile_card_property import ProfileCardProperty
    from .profile_photo import ProfilePhoto
    from .pronouns_settings import PronounsSettings
    from .protection_policy_base import ProtectionPolicyBase
    from .protection_rule_base import ProtectionRuleBase
    from .protection_units_bulk_job_base import ProtectionUnitsBulkJobBase
    from .protection_unit_base import ProtectionUnitBase
    from .provisioning_object_summary import ProvisioningObjectSummary
    from .public_key_infrastructure_root import PublicKeyInfrastructureRoot
    from .rbac_application import RbacApplication
    from .reading_assignment_submission import ReadingAssignmentSubmission
    from .reading_coach_passage import ReadingCoachPassage
    from .record_operation import RecordOperation
    from .recycle_bin import RecycleBin
    from .recycle_bin_item import RecycleBinItem
    from .reference_attachment import ReferenceAttachment
    from .reflect_check_in_response import ReflectCheckInResponse
    from .relying_party_detailed_summary import RelyingPartyDetailedSummary
    from .remote_assistance_partner import RemoteAssistancePartner
    from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
    from .reports_root import ReportsRoot
    from .request import Request
    from .reseller_delegated_admin_relationship import ResellerDelegatedAdminRelationship
    from .resource_operation import ResourceOperation
    from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
    from .restore_artifacts_bulk_request_base import RestoreArtifactsBulkRequestBase
    from .restore_artifact_base import RestoreArtifactBase
    from .restore_point import RestorePoint
    from .restore_session_base import RestoreSessionBase
    from .rich_long_running_operation import RichLongRunningOperation
    from .risky_service_principal import RiskyServicePrincipal
    from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem
    from .risky_user import RiskyUser
    from .risky_user_history_item import RiskyUserHistoryItem
    from .risk_detection import RiskDetection
    from .role_assignment import RoleAssignment
    from .role_definition import RoleDefinition
    from .room import Room
    from .room_list import RoomList
    from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
    from .saml_or_ws_fed_provider import SamlOrWsFedProvider
    from .schedule import Schedule
    from .schedule_change_request import ScheduleChangeRequest
    from .scheduling_group import SchedulingGroup
    from .schema_extension import SchemaExtension
    from .scoped_role_membership import ScopedRoleMembership
    from .search.acronym import Acronym
    from .search.bookmark import Bookmark
    from .search.qna import Qna
    from .search.search_answer import SearchAnswer
    from .search_entity import SearchEntity
    from .section import Section
    from .section_group import SectionGroup
    from .section_map import SectionMap
    from .secure_score import SecureScore
    from .secure_score_control_profile import SecureScoreControlProfile
    from .security.alert import Alert
    from .security.article import Article
    from .security.article_indicator import ArticleIndicator
    from .security.artifact import Artifact
    from .security.authority_template import AuthorityTemplate
    from .security.case import Case
    from .security.cases_root import CasesRoot
    from .security.case_operation import CaseOperation
    from .security.category_template import CategoryTemplate
    from .security.citation_template import CitationTemplate
    from .security.data_set import DataSet
    from .security.data_source import DataSource
    from .security.data_source_container import DataSourceContainer
    from .security.department_template import DepartmentTemplate
    from .security.disposition_review_stage import DispositionReviewStage
    from .security.ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
    from .security.ediscovery_case import EdiscoveryCase
    from .security.ediscovery_case_member import EdiscoveryCaseMember
    from .security.ediscovery_case_settings import EdiscoveryCaseSettings
    from .security.ediscovery_custodian import EdiscoveryCustodian
    from .security.ediscovery_estimate_operation import EdiscoveryEstimateOperation
    from .security.ediscovery_export_operation import EdiscoveryExportOperation
    from .security.ediscovery_hold_operation import EdiscoveryHoldOperation
    from .security.ediscovery_hold_policy_sync_operation import EdiscoveryHoldPolicySyncOperation
    from .security.ediscovery_index_operation import EdiscoveryIndexOperation
    from .security.ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
    from .security.ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
    from .security.ediscovery_review_set import EdiscoveryReviewSet
    from .security.ediscovery_review_set_query import EdiscoveryReviewSetQuery
    from .security.ediscovery_review_tag import EdiscoveryReviewTag
    from .security.ediscovery_search import EdiscoverySearch
    from .security.ediscovery_search_export_operation import EdiscoverySearchExportOperation
    from .security.ediscovery_tag_operation import EdiscoveryTagOperation
    from .security.file_plan_descriptor import FilePlanDescriptor
    from .security.file_plan_descriptor_template import FilePlanDescriptorTemplate
    from .security.file_plan_reference_template import FilePlanReferenceTemplate
    from .security.health_issue import HealthIssue
    from .security.host import Host
    from .security.hostname import Hostname
    from .security.host_component import HostComponent
    from .security.host_cookie import HostCookie
    from .security.host_pair import HostPair
    from .security.host_port import HostPort
    from .security.host_reputation import HostReputation
    from .security.host_ssl_certificate import HostSslCertificate
    from .security.host_tracker import HostTracker
    from .security.identity_accounts import IdentityAccounts
    from .security.identity_container import IdentityContainer
    from .security.incident import Incident
    from .security.indicator import Indicator
    from .security.intelligence_profile import IntelligenceProfile
    from .security.intelligence_profile_indicator import IntelligenceProfileIndicator
    from .security.ip_address import IpAddress
    from .security.labels_root import LabelsRoot
    from .security.network_adapter import NetworkAdapter
    from .security.passive_dns_record import PassiveDnsRecord
    from .security.retention_event import RetentionEvent
    from .security.retention_event_type import RetentionEventType
    from .security.retention_label import RetentionLabel
    from .security.search import Search
    from .security.security import Security
    from .security.sensor import Sensor
    from .security.sensor_candidate import SensorCandidate
    from .security.sensor_candidate_activation_configuration import SensorCandidateActivationConfiguration
    from .security.site_source import SiteSource
    from .security.ssl_certificate import SslCertificate
    from .security.subcategory_template import SubcategoryTemplate
    from .security.subdomain import Subdomain
    from .security.tag import Tag
    from .security.threat_intelligence import ThreatIntelligence
    from .security.triggers_root import TriggersRoot
    from .security.trigger_types_root import TriggerTypesRoot
    from .security.unclassified_artifact import UnclassifiedArtifact
    from .security.unified_group_source import UnifiedGroupSource
    from .security.user import User
    from .security.user_source import UserSource
    from .security.vulnerability import Vulnerability
    from .security.vulnerability_component import VulnerabilityComponent
    from .security.whois_base_record import WhoisBaseRecord
    from .security.whois_history_record import WhoisHistoryRecord
    from .security.whois_record import WhoisRecord
    from .security_reports_root import SecurityReportsRoot
    from .send_dtmf_tones_operation import SendDtmfTonesOperation
    from .sensitivity_label import SensitivityLabel
    from .service_announcement import ServiceAnnouncement
    from .service_announcement_attachment import ServiceAnnouncementAttachment
    from .service_announcement_base import ServiceAnnouncementBase
    from .service_app import ServiceApp
    from .service_health import ServiceHealth
    from .service_health_issue import ServiceHealthIssue
    from .service_principal import ServicePrincipal
    from .service_principal_risk_detection import ServicePrincipalRiskDetection
    from .service_storage_quota_breakdown import ServiceStorageQuotaBreakdown
    from .service_update_message import ServiceUpdateMessage
    from .setting_state_device_summary import SettingStateDeviceSummary
    from .shared_drive_item import SharedDriveItem
    from .shared_insight import SharedInsight
    from .shared_p_c_configuration import SharedPCConfiguration
    from .shared_with_channel_team_info import SharedWithChannelTeamInfo
    from .sharepoint import Sharepoint
    from .sharepoint_settings import SharepointSettings
    from .share_point_migration_event import SharePointMigrationEvent
    from .share_point_migration_finish_manifest_file_upload_event import SharePointMigrationFinishManifestFileUploadEvent
    from .share_point_migration_job import SharePointMigrationJob
    from .share_point_migration_job_cancelled_event import SharePointMigrationJobCancelledEvent
    from .share_point_migration_job_deleted_event import SharePointMigrationJobDeletedEvent
    from .share_point_migration_job_error_event import SharePointMigrationJobErrorEvent
    from .share_point_migration_job_postponed_event import SharePointMigrationJobPostponedEvent
    from .share_point_migration_job_progress_event import SharePointMigrationJobProgressEvent
    from .share_point_migration_job_queued_event import SharePointMigrationJobQueuedEvent
    from .share_point_migration_job_start_event import SharePointMigrationJobStartEvent
    from .share_point_protection_policy import SharePointProtectionPolicy
    from .share_point_restore_session import SharePointRestoreSession
    from .shift import Shift
    from .shift_preferences import ShiftPreferences
    from .sign_in import SignIn
    from .simulation import Simulation
    from .simulation_automation import SimulationAutomation
    from .simulation_automation_run import SimulationAutomationRun
    from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
    from .site import Site
    from .site_page import SitePage
    from .site_protection_rule import SiteProtectionRule
    from .site_protection_unit import SiteProtectionUnit
    from .site_protection_units_bulk_addition_job import SiteProtectionUnitsBulkAdditionJob
    from .site_restore_artifact import SiteRestoreArtifact
    from .site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest
    from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember
    from .skype_user_conversation_member import SkypeUserConversationMember
    from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration
    from .sms_authentication_method_target import SmsAuthenticationMethodTarget
    from .social_identity_provider import SocialIdentityProvider
    from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
    from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration
    from .software_update_status_summary import SoftwareUpdateStatusSummary
    from .speaker_assignment_submission import SpeakerAssignmentSubmission
    from .standard_web_part import StandardWebPart
    from .start_hold_music_operation import StartHoldMusicOperation
    from .stop_hold_music_operation import StopHoldMusicOperation
    from .storage_quota_breakdown import StorageQuotaBreakdown
    from .storage_settings import StorageSettings
    from .sts_policy import StsPolicy
    from .subject_rights_request import SubjectRightsRequest
    from .subscribed_sku import SubscribedSku
    from .subscribe_to_tone_operation import SubscribeToToneOperation
    from .subscription import Subscription
    from .swap_shifts_change_request import SwapShiftsChangeRequest
    from .synchronization import Synchronization
    from .synchronization_job import SynchronizationJob
    from .synchronization_schema import SynchronizationSchema
    from .synchronization_template import SynchronizationTemplate
    from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
    from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
    from .targeted_managed_app_protection import TargetedManagedAppProtection
    from .target_device_group import TargetDeviceGroup
    from .task_file_attachment import TaskFileAttachment
    from .team import Team
    from .teams_administration.teams_admin_root import TeamsAdminRoot
    from .teams_administration.teams_user_configuration import TeamsUserConfiguration
    from .teams_app import TeamsApp
    from .teams_app_definition import TeamsAppDefinition
    from .teams_app_installation import TeamsAppInstallation
    from .teams_app_settings import TeamsAppSettings
    from .teams_async_operation import TeamsAsyncOperation
    from .teams_tab import TeamsTab
    from .teams_template import TeamsTemplate
    from .teamwork import Teamwork
    from .teamwork_bot import TeamworkBot
    from .teamwork_hosted_content import TeamworkHostedContent
    from .teamwork_tag import TeamworkTag
    from .teamwork_tag_member import TeamworkTagMember
    from .team_info import TeamInfo
    from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
    from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration
    from .tenant_app_management_policy import TenantAppManagementPolicy
    from .tenant_data_security_and_governance import TenantDataSecurityAndGovernance
    from .tenant_protection_scope_container import TenantProtectionScopeContainer
    from .terms_and_conditions import TermsAndConditions
    from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
    from .terms_and_conditions_assignment import TermsAndConditionsAssignment
    from .terms_of_use_container import TermsOfUseContainer
    from .term_store.group import Group
    from .term_store.relation import Relation
    from .term_store.set import Set
    from .term_store.store import Store
    from .term_store.term import Term
    from .text_web_part import TextWebPart
    from .threat_assessment_request import ThreatAssessmentRequest
    from .threat_assessment_result import ThreatAssessmentResult
    from .thumbnail_set import ThumbnailSet
    from .time_card import TimeCard
    from .time_off import TimeOff
    from .time_off_reason import TimeOffReason
    from .time_off_request import TimeOffRequest
    from .todo import Todo
    from .todo_task import TodoTask
    from .todo_task_list import TodoTaskList
    from .token_issuance_policy import TokenIssuancePolicy
    from .token_lifetime_policy import TokenLifetimePolicy
    from .training import Training
    from .training_language_detail import TrainingLanguageDetail
    from .trending import Trending
    from .unified_rbac_resource_action import UnifiedRbacResourceAction
    from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
    from .unified_role_assignment import UnifiedRoleAssignment
    from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
    from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
    from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
    from .unified_role_definition import UnifiedRoleDefinition
    from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
    from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
    from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest
    from .unified_role_management_policy import UnifiedRoleManagementPolicy
    from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule
    from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment
    from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule
    from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule
    from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule
    from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule
    from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule
    from .unified_role_schedule_base import UnifiedRoleScheduleBase
    from .unified_role_schedule_instance_base import UnifiedRoleScheduleInstanceBase
    from .unified_storage_quota import UnifiedStorageQuota
    from .unit_map import UnitMap
    from .unmute_participant_operation import UnmuteParticipantOperation
    from .update_recording_status_operation import UpdateRecordingStatusOperation
    from .url_assessment_request import UrlAssessmentRequest
    from .usage_rights_included import UsageRightsIncluded
    from .used_insight import UsedInsight
    from .user import User
    from .user_activity import UserActivity
    from .user_consent_request import UserConsentRequest
    from .user_data_security_and_governance import UserDataSecurityAndGovernance
    from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformance
    from .user_experience_analytics_app_health_app_performance_by_app_version_details import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
    from .user_experience_analytics_app_health_app_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId
    from .user_experience_analytics_app_health_app_performance_by_o_s_version import UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion
    from .user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformance
    from .user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformance
    from .user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetails
    from .user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformance
    from .user_experience_analytics_baseline import UserExperienceAnalyticsBaseline
    from .user_experience_analytics_category import UserExperienceAnalyticsCategory
    from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance
    from .user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScores
    from .user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistory
    from .user_experience_analytics_device_startup_process import UserExperienceAnalyticsDeviceStartupProcess
    from .user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformance
    from .user_experience_analytics_metric import UserExperienceAnalyticsMetric
    from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
    from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
    from .user_experience_analytics_overview import UserExperienceAnalyticsOverview
    from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory
    from .user_experience_analytics_work_from_anywhere_device import UserExperienceAnalyticsWorkFromAnywhereDevice
    from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
    from .user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
    from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance
    from .user_flow_language_configuration import UserFlowLanguageConfiguration
    from .user_flow_language_page import UserFlowLanguagePage
    from .user_insights_settings import UserInsightsSettings
    from .user_install_state_summary import UserInstallStateSummary
    from .user_protection_scope_container import UserProtectionScopeContainer
    from .user_registration_details import UserRegistrationDetails
    from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation
    from .user_settings import UserSettings
    from .user_sign_in_insight import UserSignInInsight
    from .user_solution_root import UserSolutionRoot
    from .user_storage import UserStorage
    from .user_teamwork import UserTeamwork
    from .vertical_section import VerticalSection
    from .virtual_endpoint import VirtualEndpoint
    from .virtual_event import VirtualEvent
    from .virtual_events_root import VirtualEventsRoot
    from .virtual_event_presenter import VirtualEventPresenter
    from .virtual_event_registration import VirtualEventRegistration
    from .virtual_event_registration_configuration import VirtualEventRegistrationConfiguration
    from .virtual_event_registration_custom_question import VirtualEventRegistrationCustomQuestion
    from .virtual_event_registration_predefined_question import VirtualEventRegistrationPredefinedQuestion
    from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase
    from .virtual_event_session import VirtualEventSession
    from .virtual_event_townhall import VirtualEventTownhall
    from .virtual_event_webinar import VirtualEventWebinar
    from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration
    from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration
    from .vpp_token import VppToken
    from .web_app import WebApp
    from .web_application_firewall_provider import WebApplicationFirewallProvider
    from .web_application_firewall_verification_model import WebApplicationFirewallVerificationModel
    from .web_part import WebPart
    from .what_if_analysis_result import WhatIfAnalysisResult
    from .win32_lob_app import Win32LobApp
    from .windows10_compliance_policy import Windows10CompliancePolicy
    from .windows10_custom_configuration import Windows10CustomConfiguration
    from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
    from .windows10_enrollment_completion_page_configuration import Windows10EnrollmentCompletionPageConfiguration
    from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
    from .windows10_general_configuration import Windows10GeneralConfiguration
    from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy
    from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
    from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
    from .windows81_compliance_policy import Windows81CompliancePolicy
    from .windows81_general_configuration import Windows81GeneralConfiguration
    from .windows_app_x import WindowsAppX
    from .windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
    from .windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment
    from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
    from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
    from .windows_device_malware_state import WindowsDeviceMalwareState
    from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod
    from .windows_information_protection import WindowsInformationProtection
    from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
    from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile
    from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
    from .windows_information_protection_policy import WindowsInformationProtectionPolicy
    from .windows_malware_information import WindowsMalwareInformation
    from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp
    from .windows_mobile_m_s_i import WindowsMobileMSI
    from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy
    from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
    from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
    from .windows_protection_state import WindowsProtectionState
    from .windows_setting import WindowsSetting
    from .windows_setting_instance import WindowsSettingInstance
    from .windows_universal_app_x import WindowsUniversalAppX
    from .windows_universal_app_x_contained_app import WindowsUniversalAppXContainedApp
    from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration
    from .windows_web_app import WindowsWebApp
    from .workbook import Workbook
    from .workbook_application import WorkbookApplication
    from .workbook_chart import WorkbookChart
    from .workbook_chart_area_format import WorkbookChartAreaFormat
    from .workbook_chart_axes import WorkbookChartAxes
    from .workbook_chart_axis import WorkbookChartAxis
    from .workbook_chart_axis_format import WorkbookChartAxisFormat
    from .workbook_chart_axis_title import WorkbookChartAxisTitle
    from .workbook_chart_axis_title_format import WorkbookChartAxisTitleFormat
    from .workbook_chart_data_labels import WorkbookChartDataLabels
    from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat
    from .workbook_chart_fill import WorkbookChartFill
    from .workbook_chart_font import WorkbookChartFont
    from .workbook_chart_gridlines import WorkbookChartGridlines
    from .workbook_chart_gridlines_format import WorkbookChartGridlinesFormat
    from .workbook_chart_legend import WorkbookChartLegend
    from .workbook_chart_legend_format import WorkbookChartLegendFormat
    from .workbook_chart_line_format import WorkbookChartLineFormat
    from .workbook_chart_point import WorkbookChartPoint
    from .workbook_chart_point_format import WorkbookChartPointFormat
    from .workbook_chart_series import WorkbookChartSeries
    from .workbook_chart_series_format import WorkbookChartSeriesFormat
    from .workbook_chart_title import WorkbookChartTitle
    from .workbook_chart_title_format import WorkbookChartTitleFormat
    from .workbook_comment import WorkbookComment
    from .workbook_comment_reply import WorkbookCommentReply
    from .workbook_filter import WorkbookFilter
    from .workbook_format_protection import WorkbookFormatProtection
    from .workbook_functions import WorkbookFunctions
    from .workbook_function_result import WorkbookFunctionResult
    from .workbook_named_item import WorkbookNamedItem
    from .workbook_operation import WorkbookOperation
    from .workbook_pivot_table import WorkbookPivotTable
    from .workbook_range import WorkbookRange
    from .workbook_range_border import WorkbookRangeBorder
    from .workbook_range_fill import WorkbookRangeFill
    from .workbook_range_font import WorkbookRangeFont
    from .workbook_range_format import WorkbookRangeFormat
    from .workbook_range_sort import WorkbookRangeSort
    from .workbook_range_view import WorkbookRangeView
    from .workbook_table import WorkbookTable
    from .workbook_table_column import WorkbookTableColumn
    from .workbook_table_row import WorkbookTableRow
    from .workbook_table_sort import WorkbookTableSort
    from .workbook_worksheet import WorkbookWorksheet
    from .workbook_worksheet_protection import WorkbookWorksheetProtection
    from .workforce_integration import WorkforceIntegration
    from .working_time_schedule import WorkingTimeSchedule
    from .workspace import Workspace
    from .work_hours_and_locations_setting import WorkHoursAndLocationsSetting
    from .work_plan_occurrence import WorkPlanOccurrence
    from .work_plan_recurrence import WorkPlanRecurrence
    from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration
    from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration

@dataclass
class Entity(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The unique identifier for an entity. Read-only.
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Entity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Entity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aadUserConversationMember".casefold():
            from .aad_user_conversation_member import AadUserConversationMember

            return AadUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackage".casefold():
            from .access_package import AccessPackage

            return AccessPackage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignment".casefold():
            from .access_package_assignment import AccessPackageAssignment

            return AccessPackageAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignmentPolicy".casefold():
            from .access_package_assignment_policy import AccessPackageAssignmentPolicy

            return AccessPackageAssignmentPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignmentRequest".casefold():
            from .access_package_assignment_request import AccessPackageAssignmentRequest

            return AccessPackageAssignmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignmentRequestWorkflowExtension".casefold():
            from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension

            return AccessPackageAssignmentRequestWorkflowExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageAssignmentWorkflowExtension".casefold():
            from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension

            return AccessPackageAssignmentWorkflowExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageCatalog".casefold():
            from .access_package_catalog import AccessPackageCatalog

            return AccessPackageCatalog()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageMultipleChoiceQuestion".casefold():
            from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion

            return AccessPackageMultipleChoiceQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageQuestion".casefold():
            from .access_package_question import AccessPackageQuestion

            return AccessPackageQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageResource".casefold():
            from .access_package_resource import AccessPackageResource

            return AccessPackageResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageResourceEnvironment".casefold():
            from .access_package_resource_environment import AccessPackageResourceEnvironment

            return AccessPackageResourceEnvironment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageResourceRequest".casefold():
            from .access_package_resource_request import AccessPackageResourceRequest

            return AccessPackageResourceRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageResourceRole".casefold():
            from .access_package_resource_role import AccessPackageResourceRole

            return AccessPackageResourceRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageResourceRoleScope".casefold():
            from .access_package_resource_role_scope import AccessPackageResourceRoleScope

            return AccessPackageResourceRoleScope()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageResourceScope".casefold():
            from .access_package_resource_scope import AccessPackageResourceScope

            return AccessPackageResourceScope()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageSubject".casefold():
            from .access_package_subject import AccessPackageSubject

            return AccessPackageSubject()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessPackageTextInputQuestion".casefold():
            from .access_package_text_input_question import AccessPackageTextInputQuestion

            return AccessPackageTextInputQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewHistoryDefinition".casefold():
            from .access_review_history_definition import AccessReviewHistoryDefinition

            return AccessReviewHistoryDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewHistoryInstance".casefold():
            from .access_review_history_instance import AccessReviewHistoryInstance

            return AccessReviewHistoryInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewInstance".casefold():
            from .access_review_instance import AccessReviewInstance

            return AccessReviewInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewInstanceDecisionItem".casefold():
            from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem

            return AccessReviewInstanceDecisionItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewReviewer".casefold():
            from .access_review_reviewer import AccessReviewReviewer

            return AccessReviewReviewer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewScheduleDefinition".casefold():
            from .access_review_schedule_definition import AccessReviewScheduleDefinition

            return AccessReviewScheduleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewSet".casefold():
            from .access_review_set import AccessReviewSet

            return AccessReviewSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewStage".casefold():
            from .access_review_stage import AccessReviewStage

            return AccessReviewStage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activitiesContainer".casefold():
            from .activities_container import ActivitiesContainer

            return ActivitiesContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activityBasedTimeoutPolicy".casefold():
            from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy

            return ActivityBasedTimeoutPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.activityHistoryItem".casefold():
            from .activity_history_item import ActivityHistoryItem

            return ActivityHistoryItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.addLargeGalleryViewOperation".casefold():
            from .add_large_gallery_view_operation import AddLargeGalleryViewOperation

            return AddLargeGalleryViewOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.adhocCall".casefold():
            from .adhoc_call import AdhocCall

            return AdhocCall()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.adminConsentRequestPolicy".casefold():
            from .admin_consent_request_policy import AdminConsentRequestPolicy

            return AdminConsentRequestPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.administrativeUnit".casefold():
            from .administrative_unit import AdministrativeUnit

            return AdministrativeUnit()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.adminMicrosoft365Apps".casefold():
            from .admin_microsoft365_apps import AdminMicrosoft365Apps

            return AdminMicrosoft365Apps()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.adminReportSettings".casefold():
            from .admin_report_settings import AdminReportSettings

            return AdminReportSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreement".casefold():
            from .agreement import Agreement

            return Agreement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementAcceptance".casefold():
            from .agreement_acceptance import AgreementAcceptance

            return AgreementAcceptance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementFile".casefold():
            from .agreement_file import AgreementFile

            return AgreementFile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementFileLocalization".casefold():
            from .agreement_file_localization import AgreementFileLocalization

            return AgreementFileLocalization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementFileProperties".casefold():
            from .agreement_file_properties import AgreementFileProperties

            return AgreementFileProperties()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.agreementFileVersion".casefold():
            from .agreement_file_version import AgreementFileVersion

            return AgreementFileVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aiInteraction".casefold():
            from .ai_interaction import AiInteraction

            return AiInteraction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aiInteractionHistory".casefold():
            from .ai_interaction_history import AiInteractionHistory

            return AiInteractionHistory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aiOnlineMeeting".casefold():
            from .ai_online_meeting import AiOnlineMeeting

            return AiOnlineMeeting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.aiUser".casefold():
            from .ai_user import AiUser

            return AiUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.akamaiWebApplicationFirewallProvider".casefold():
            from .akamai_web_application_firewall_provider import AkamaiWebApplicationFirewallProvider

            return AkamaiWebApplicationFirewallProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.alert".casefold():
            from .alert import Alert
            from .security.alert import Alert

            return Alert()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.allowedValue".casefold():
            from .allowed_value import AllowedValue

            return AllowedValue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidCompliancePolicy".casefold():
            from .android_compliance_policy import AndroidCompliancePolicy

            return AndroidCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidCustomConfiguration".casefold():
            from .android_custom_configuration import AndroidCustomConfiguration

            return AndroidCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidGeneralDeviceConfiguration".casefold():
            from .android_general_device_configuration import AndroidGeneralDeviceConfiguration

            return AndroidGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidLobApp".casefold():
            from .android_lob_app import AndroidLobApp

            return AndroidLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedAppProtection".casefold():
            from .android_managed_app_protection import AndroidManagedAppProtection

            return AndroidManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidManagedAppRegistration".casefold():
            from .android_managed_app_registration import AndroidManagedAppRegistration

            return AndroidManagedAppRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidStoreApp".casefold():
            from .android_store_app import AndroidStoreApp

            return AndroidStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileCompliancePolicy".casefold():
            from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy

            return AndroidWorkProfileCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileCustomConfiguration".casefold():
            from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration

            return AndroidWorkProfileCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration".casefold():
            from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration

            return AndroidWorkProfileGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.anonymousGuestConversationMember".casefold():
            from .anonymous_guest_conversation_member import AnonymousGuestConversationMember

            return AnonymousGuestConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appCatalogs".casefold():
            from .app_catalogs import AppCatalogs

            return AppCatalogs()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appConsentApprovalRoute".casefold():
            from .app_consent_approval_route import AppConsentApprovalRoute

            return AppConsentApprovalRoute()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appConsentRequest".casefold():
            from .app_consent_request import AppConsentRequest

            return AppConsentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleDeviceFeaturesConfigurationBase".casefold():
            from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase

            return AppleDeviceFeaturesConfigurationBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appleManagedIdentityProvider".casefold():
            from .apple_managed_identity_provider import AppleManagedIdentityProvider

            return AppleManagedIdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.applePushNotificationCertificate".casefold():
            from .apple_push_notification_certificate import ApplePushNotificationCertificate

            return ApplePushNotificationCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.application".casefold():
            from .application import Application

            return Application()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.applicationTemplate".casefold():
            from .application_template import ApplicationTemplate

            return ApplicationTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appLogCollectionRequest".casefold():
            from .app_log_collection_request import AppLogCollectionRequest

            return AppLogCollectionRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appManagementPolicy".casefold():
            from .app_management_policy import AppManagementPolicy

            return AppManagementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appRoleAssignment".casefold():
            from .app_role_assignment import AppRoleAssignment

            return AppRoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.approval".casefold():
            from .approval import Approval

            return Approval()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.approvalStage".casefold():
            from .approval_stage import ApprovalStage

            return ApprovalStage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.appScope".casefold():
            from .app_scope import AppScope

            return AppScope()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.arkoseFraudProtectionProvider".casefold():
            from .arkose_fraud_protection_provider import ArkoseFraudProtectionProvider

            return ArkoseFraudProtectionProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.associatedTeamInfo".casefold():
            from .associated_team_info import AssociatedTeamInfo

            return AssociatedTeamInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attachment".casefold():
            from .attachment import Attachment

            return Attachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attachmentBase".casefold():
            from .attachment_base import AttachmentBase

            return AttachmentBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attachmentSession".casefold():
            from .attachment_session import AttachmentSession

            return AttachmentSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attackSimulationOperation".casefold():
            from .attack_simulation_operation import AttackSimulationOperation

            return AttackSimulationOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attackSimulationRoot".casefold():
            from .attack_simulation_root import AttackSimulationRoot

            return AttackSimulationRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attendanceRecord".casefold():
            from .attendance_record import AttendanceRecord

            return AttendanceRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attributeMappingFunctionSchema".casefold():
            from .attribute_mapping_function_schema import AttributeMappingFunctionSchema

            return AttributeMappingFunctionSchema()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attributeSet".casefold():
            from .attribute_set import AttributeSet

            return AttributeSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.audioRoutingGroup".casefold():
            from .audio_routing_group import AudioRoutingGroup

            return AudioRoutingGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.auditEvent".casefold():
            from .audit_event import AuditEvent

            return AuditEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.auditLogRoot".casefold():
            from .audit_log_root import AuditLogRoot

            return AuditLogRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authentication".casefold():
            from .authentication import Authentication

            return Authentication()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationCombinationConfiguration".casefold():
            from .authentication_combination_configuration import AuthenticationCombinationConfiguration

            return AuthenticationCombinationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationContextClassReference".casefold():
            from .authentication_context_class_reference import AuthenticationContextClassReference

            return AuthenticationContextClassReference()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationEventListener".casefold():
            from .authentication_event_listener import AuthenticationEventListener

            return AuthenticationEventListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationEventsFlow".casefold():
            from .authentication_events_flow import AuthenticationEventsFlow

            return AuthenticationEventsFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationFlowsPolicy".casefold():
            from .authentication_flows_policy import AuthenticationFlowsPolicy

            return AuthenticationFlowsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethod".casefold():
            from .authentication_method import AuthenticationMethod

            return AuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethodConfiguration".casefold():
            from .authentication_method_configuration import AuthenticationMethodConfiguration

            return AuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethodModeDetail".casefold():
            from .authentication_method_mode_detail import AuthenticationMethodModeDetail

            return AuthenticationMethodModeDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethodsPolicy".casefold():
            from .authentication_methods_policy import AuthenticationMethodsPolicy

            return AuthenticationMethodsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethodsRoot".casefold():
            from .authentication_methods_root import AuthenticationMethodsRoot

            return AuthenticationMethodsRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationMethodTarget".casefold():
            from .authentication_method_target import AuthenticationMethodTarget

            return AuthenticationMethodTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationStrengthPolicy".casefold():
            from .authentication_strength_policy import AuthenticationStrengthPolicy

            return AuthenticationStrengthPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authenticationStrengthRoot".casefold():
            from .authentication_strength_root import AuthenticationStrengthRoot

            return AuthenticationStrengthRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authoredNote".casefold():
            from .authored_note import AuthoredNote

            return AuthoredNote()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.authorizationPolicy".casefold():
            from .authorization_policy import AuthorizationPolicy

            return AuthorizationPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureCommunicationServicesUserConversationMember".casefold():
            from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember

            return AzureCommunicationServicesUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.b2xIdentityUserFlow".casefold():
            from .b2x_identity_user_flow import B2xIdentityUserFlow

            return B2xIdentityUserFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.backupRestoreRoot".casefold():
            from .backup_restore_root import BackupRestoreRoot

            return BackupRestoreRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.baseItem".casefold():
            from .base_item import BaseItem

            return BaseItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.baseItemVersion".casefold():
            from .base_item_version import BaseItemVersion

            return BaseItemVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.baseMapFeature".casefold():
            from .base_map_feature import BaseMapFeature

            return BaseMapFeature()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.baseSitePage".casefold():
            from .base_site_page import BaseSitePage

            return BaseSitePage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bitlocker".casefold():
            from .bitlocker import Bitlocker

            return Bitlocker()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bitlockerRecoveryKey".casefold():
            from .bitlocker_recovery_key import BitlockerRecoveryKey

            return BitlockerRecoveryKey()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingAppointment".casefold():
            from .booking_appointment import BookingAppointment

            return BookingAppointment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingBusiness".casefold():
            from .booking_business import BookingBusiness

            return BookingBusiness()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingCurrency".casefold():
            from .booking_currency import BookingCurrency

            return BookingCurrency()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingCustomer".casefold():
            from .booking_customer import BookingCustomer

            return BookingCustomer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingCustomerBase".casefold():
            from .booking_customer_base import BookingCustomerBase

            return BookingCustomerBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingCustomQuestion".casefold():
            from .booking_custom_question import BookingCustomQuestion

            return BookingCustomQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingService".casefold():
            from .booking_service import BookingService

            return BookingService()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingStaffMember".casefold():
            from .booking_staff_member import BookingStaffMember

            return BookingStaffMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bookingStaffMemberBase".casefold():
            from .booking_staff_member_base import BookingStaffMemberBase

            return BookingStaffMemberBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.browserSharedCookie".casefold():
            from .browser_shared_cookie import BrowserSharedCookie

            return BrowserSharedCookie()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.browserSite".casefold():
            from .browser_site import BrowserSite

            return BrowserSite()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.browserSiteList".casefold():
            from .browser_site_list import BrowserSiteList

            return BrowserSiteList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.building".casefold():
            from .building import Building

            return Building()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.buildingMap".casefold():
            from .building_map import BuildingMap

            return BuildingMap()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.builtInIdentityProvider".casefold():
            from .built_in_identity_provider import BuiltInIdentityProvider

            return BuiltInIdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.bulkUpload".casefold():
            from .bulk_upload import BulkUpload

            return BulkUpload()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.calendar".casefold():
            from .calendar import Calendar

            return Calendar()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.calendarGroup".casefold():
            from .calendar_group import CalendarGroup

            return CalendarGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.calendarPermission".casefold():
            from .calendar_permission import CalendarPermission

            return CalendarPermission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.calendarSharingMessage".casefold():
            from .calendar_sharing_message import CalendarSharingMessage

            return CalendarSharingMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.call".casefold():
            from .call import Call

            return Call()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callAiInsight".casefold():
            from .call_ai_insight import CallAiInsight

            return CallAiInsight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callEvent".casefold():
            from .call_event import CallEvent

            return CallEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecording".casefold():
            from .call_recording import CallRecording

            return CallRecording()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.callRecord".casefold():
            from .call_records.call_record import CallRecord

            return CallRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.organizer".casefold():
            from .call_records.organizer import Organizer

            return Organizer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.participant".casefold():
            from .call_records.participant import Participant
            from .participant import Participant

            return Participant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.participantBase".casefold():
            from .call_records.participant_base import ParticipantBase

            return ParticipantBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.segment".casefold():
            from .call_records.segment import Segment

            return Segment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.session".casefold():
            from .call_records.session import Session

            return Session()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callTranscript".casefold():
            from .call_transcript import CallTranscript

            return CallTranscript()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cancelMediaProcessingOperation".casefold():
            from .cancel_media_processing_operation import CancelMediaProcessingOperation

            return CancelMediaProcessingOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.canvasLayout".casefold():
            from .canvas_layout import CanvasLayout

            return CanvasLayout()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.certificateAuthorityDetail".casefold():
            from .certificate_authority_detail import CertificateAuthorityDetail

            return CertificateAuthorityDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.certificateBasedAuthConfiguration".casefold():
            from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration

            return CertificateBasedAuthConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.certificateBasedAuthPki".casefold():
            from .certificate_based_auth_pki import CertificateBasedAuthPki

            return CertificateBasedAuthPki()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.changeTrackedEntity".casefold():
            from .change_tracked_entity import ChangeTrackedEntity

            return ChangeTrackedEntity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.channel".casefold():
            from .channel import Channel

            return Channel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chat".casefold():
            from .chat import Chat

            return Chat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatMessage".casefold():
            from .chat_message import ChatMessage

            return ChatMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatMessageHostedContent".casefold():
            from .chat_message_hosted_content import ChatMessageHostedContent

            return ChatMessageHostedContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.chatMessageInfo".casefold():
            from .chat_message_info import ChatMessageInfo

            return ChatMessageInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.checklistItem".casefold():
            from .checklist_item import ChecklistItem

            return ChecklistItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.claimsMappingPolicy".casefold():
            from .claims_mapping_policy import ClaimsMappingPolicy

            return ClaimsMappingPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudClipboardItem".casefold():
            from .cloud_clipboard_item import CloudClipboardItem

            return CloudClipboardItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudClipboardRoot".casefold():
            from .cloud_clipboard_root import CloudClipboardRoot

            return CloudClipboardRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudFlareWebApplicationFirewallProvider".casefold():
            from .cloud_flare_web_application_firewall_provider import CloudFlareWebApplicationFirewallProvider

            return CloudFlareWebApplicationFirewallProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPC".casefold():
            from .cloud_p_c import CloudPC

            return CloudPC()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcAuditEvent".casefold():
            from .cloud_pc_audit_event import CloudPcAuditEvent

            return CloudPcAuditEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcDeviceImage".casefold():
            from .cloud_pc_device_image import CloudPcDeviceImage

            return CloudPcDeviceImage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcGalleryImage".casefold():
            from .cloud_pc_gallery_image import CloudPcGalleryImage

            return CloudPcGalleryImage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcOnPremisesConnection".casefold():
            from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection

            return CloudPcOnPremisesConnection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcProvisioningPolicy".casefold():
            from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy

            return CloudPcProvisioningPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcProvisioningPolicyAssignment".casefold():
            from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment

            return CloudPcProvisioningPolicyAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcReport".casefold():
            from .cloud_pc_report import CloudPcReport

            return CloudPcReport()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcUserSetting".casefold():
            from .cloud_pc_user_setting import CloudPcUserSetting

            return CloudPcUserSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.cloudPcUserSettingAssignment".casefold():
            from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment

            return CloudPcUserSettingAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.columnDefinition".casefold():
            from .column_definition import ColumnDefinition

            return ColumnDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.columnLink".casefold():
            from .column_link import ColumnLink

            return ColumnLink()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.commsOperation".casefold():
            from .comms_operation import CommsOperation

            return CommsOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.community".casefold():
            from .community import Community

            return Community()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.companySubscription".casefold():
            from .company_subscription import CompanySubscription

            return CompanySubscription()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.complianceManagementPartner".casefold():
            from .compliance_management_partner import ComplianceManagementPartner

            return ComplianceManagementPartner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conditionalAccessPolicy".casefold():
            from .conditional_access_policy import ConditionalAccessPolicy

            return ConditionalAccessPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conditionalAccessRoot".casefold():
            from .conditional_access_root import ConditionalAccessRoot

            return ConditionalAccessRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conditionalAccessTemplate".casefold():
            from .conditional_access_template import ConditionalAccessTemplate

            return ConditionalAccessTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.connectedOrganization".casefold():
            from .connected_organization import ConnectedOrganization

            return ConnectedOrganization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contact".casefold():
            from .contact import Contact

            return Contact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contactFolder".casefold():
            from .contact_folder import ContactFolder

            return ContactFolder()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contentActivity".casefold():
            from .content_activity import ContentActivity

            return ContentActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contentSharingSession".casefold():
            from .content_sharing_session import ContentSharingSession

            return ContentSharingSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contentType".casefold():
            from .content_type import ContentType

            return ContentType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.contract".casefold():
            from .contract import Contract

            return Contract()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conversation".casefold():
            from .conversation import Conversation

            return Conversation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conversationMember".casefold():
            from .conversation_member import ConversationMember

            return ConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.conversationThread".casefold():
            from .conversation_thread import ConversationThread

            return ConversationThread()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotAdmin".casefold():
            from .copilot_admin import CopilotAdmin

            return CopilotAdmin()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotAdminLimitedMode".casefold():
            from .copilot_admin_limited_mode import CopilotAdminLimitedMode

            return CopilotAdminLimitedMode()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotAdminSetting".casefold():
            from .copilot_admin_setting import CopilotAdminSetting

            return CopilotAdminSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.copilotReportRoot".casefold():
            from .copilot_report_root import CopilotReportRoot

            return CopilotReportRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.countryNamedLocation".casefold():
            from .country_named_location import CountryNamedLocation

            return CountryNamedLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantAccessPolicy".casefold():
            from .cross_tenant_access_policy import CrossTenantAccessPolicy

            return CrossTenantAccessPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.crossTenantAccessPolicyConfigurationDefault".casefold():
            from .cross_tenant_access_policy_configuration_default import CrossTenantAccessPolicyConfigurationDefault

            return CrossTenantAccessPolicyConfigurationDefault()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customAuthenticationExtension".casefold():
            from .custom_authentication_extension import CustomAuthenticationExtension

            return CustomAuthenticationExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customCalloutExtension".casefold():
            from .custom_callout_extension import CustomCalloutExtension

            return CustomCalloutExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customExtensionStageSetting".casefold():
            from .custom_extension_stage_setting import CustomExtensionStageSetting

            return CustomExtensionStageSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customSecurityAttributeDefinition".casefold():
            from .custom_security_attribute_definition import CustomSecurityAttributeDefinition

            return CustomSecurityAttributeDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dataPolicyOperation".casefold():
            from .data_policy_operation import DataPolicyOperation

            return DataPolicyOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dataSecurityAndGovernance".casefold():
            from .data_security_and_governance import DataSecurityAndGovernance

            return DataSecurityAndGovernance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.dayNote".casefold():
            from .day_note import DayNote

            return DayNote()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.defaultManagedAppProtection".casefold():
            from .default_managed_app_protection import DefaultManagedAppProtection

            return DefaultManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminAccessAssignment".casefold():
            from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment

            return DelegatedAdminAccessAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminCustomer".casefold():
            from .delegated_admin_customer import DelegatedAdminCustomer

            return DelegatedAdminCustomer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminRelationship".casefold():
            from .delegated_admin_relationship import DelegatedAdminRelationship

            return DelegatedAdminRelationship()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminRelationshipOperation".casefold():
            from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation

            return DelegatedAdminRelationshipOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminRelationshipRequest".casefold():
            from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest

            return DelegatedAdminRelationshipRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedAdminServiceManagementDetail".casefold():
            from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail

            return DelegatedAdminServiceManagementDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.delegatedPermissionClassification".casefold():
            from .delegated_permission_classification import DelegatedPermissionClassification

            return DelegatedPermissionClassification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deletedChat".casefold():
            from .deleted_chat import DeletedChat

            return DeletedChat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deletedItemContainer".casefold():
            from .deleted_item_container import DeletedItemContainer

            return DeletedItemContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deletedTeam".casefold():
            from .deleted_team import DeletedTeam

            return DeletedTeam()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deltaParticipants".casefold():
            from .delta_participants import DeltaParticipants

            return DeltaParticipants()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.desk".casefold():
            from .desk import Desk

            return Desk()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.detectedApp".casefold():
            from .detected_app import DetectedApp

            return DetectedApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.device".casefold():
            from .device import Device

            return Device()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceAndAppManagementRoleAssignment".casefold():
            from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment

            return DeviceAndAppManagementRoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceAndAppManagementRoleDefinition".casefold():
            from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition

            return DeviceAndAppManagementRoleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceAppManagement".casefold():
            from .device_app_management import DeviceAppManagement

            return DeviceAppManagement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCategory".casefold():
            from .device_category import DeviceCategory

            return DeviceCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceActionItem".casefold():
            from .device_compliance_action_item import DeviceComplianceActionItem

            return DeviceComplianceActionItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceDeviceOverview".casefold():
            from .device_compliance_device_overview import DeviceComplianceDeviceOverview

            return DeviceComplianceDeviceOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceDeviceStatus".casefold():
            from .device_compliance_device_status import DeviceComplianceDeviceStatus

            return DeviceComplianceDeviceStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicy".casefold():
            from .device_compliance_policy import DeviceCompliancePolicy

            return DeviceCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicyAssignment".casefold():
            from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment

            return DeviceCompliancePolicyAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicyDeviceStateSummary".casefold():
            from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary

            return DeviceCompliancePolicyDeviceStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicySettingStateSummary".casefold():
            from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary

            return DeviceCompliancePolicySettingStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceCompliancePolicyState".casefold():
            from .device_compliance_policy_state import DeviceCompliancePolicyState

            return DeviceCompliancePolicyState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceScheduledActionForRule".casefold():
            from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule

            return DeviceComplianceScheduledActionForRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceSettingState".casefold():
            from .device_compliance_setting_state import DeviceComplianceSettingState

            return DeviceComplianceSettingState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceUserOverview".casefold():
            from .device_compliance_user_overview import DeviceComplianceUserOverview

            return DeviceComplianceUserOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceComplianceUserStatus".casefold():
            from .device_compliance_user_status import DeviceComplianceUserStatus

            return DeviceComplianceUserStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfiguration".casefold():
            from .device_configuration import DeviceConfiguration

            return DeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationAssignment".casefold():
            from .device_configuration_assignment import DeviceConfigurationAssignment

            return DeviceConfigurationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationDeviceOverview".casefold():
            from .device_configuration_device_overview import DeviceConfigurationDeviceOverview

            return DeviceConfigurationDeviceOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationDeviceStateSummary".casefold():
            from .device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary

            return DeviceConfigurationDeviceStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationDeviceStatus".casefold():
            from .device_configuration_device_status import DeviceConfigurationDeviceStatus

            return DeviceConfigurationDeviceStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationState".casefold():
            from .device_configuration_state import DeviceConfigurationState

            return DeviceConfigurationState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationUserOverview".casefold():
            from .device_configuration_user_overview import DeviceConfigurationUserOverview

            return DeviceConfigurationUserOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceConfigurationUserStatus".casefold():
            from .device_configuration_user_status import DeviceConfigurationUserStatus

            return DeviceConfigurationUserStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentConfiguration".casefold():
            from .device_enrollment_configuration import DeviceEnrollmentConfiguration

            return DeviceEnrollmentConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentLimitConfiguration".casefold():
            from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration

            return DeviceEnrollmentLimitConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentPlatformRestrictionsConfiguration".casefold():
            from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration

            return DeviceEnrollmentPlatformRestrictionsConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceEnrollmentWindowsHelloForBusinessConfiguration".casefold():
            from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration

            return DeviceEnrollmentWindowsHelloForBusinessConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceInstallState".casefold():
            from .device_install_state import DeviceInstallState

            return DeviceInstallState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceLocalCredentialInfo".casefold():
            from .device_local_credential_info import DeviceLocalCredentialInfo

            return DeviceLocalCredentialInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceLogCollectionResponse".casefold():
            from .device_log_collection_response import DeviceLogCollectionResponse

            return DeviceLogCollectionResponse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagement".casefold():
            from .device_management import DeviceManagement

            return DeviceManagement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementCachedReportConfiguration".casefold():
            from .device_management_cached_report_configuration import DeviceManagementCachedReportConfiguration

            return DeviceManagementCachedReportConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementExchangeConnector".casefold():
            from .device_management_exchange_connector import DeviceManagementExchangeConnector

            return DeviceManagementExchangeConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementExportJob".casefold():
            from .device_management_export_job import DeviceManagementExportJob

            return DeviceManagementExportJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementPartner".casefold():
            from .device_management_partner import DeviceManagementPartner

            return DeviceManagementPartner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementReports".casefold():
            from .device_management_reports import DeviceManagementReports

            return DeviceManagementReports()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceManagementTroubleshootingEvent".casefold():
            from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent

            return DeviceManagementTroubleshootingEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.deviceRegistrationPolicy".casefold():
            from .device_registration_policy import DeviceRegistrationPolicy

            return DeviceRegistrationPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directory".casefold():
            from .directory import Directory

            return Directory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryAudit".casefold():
            from .directory_audit import DirectoryAudit

            return DirectoryAudit()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryDefinition".casefold():
            from .directory_definition import DirectoryDefinition

            return DirectoryDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryObject".casefold():
            from .directory_object import DirectoryObject

            return DirectoryObject()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryObjectPartnerReference".casefold():
            from .directory_object_partner_reference import DirectoryObjectPartnerReference

            return DirectoryObjectPartnerReference()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryRole".casefold():
            from .directory_role import DirectoryRole

            return DirectoryRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.directoryRoleTemplate".casefold():
            from .directory_role_template import DirectoryRoleTemplate

            return DirectoryRoleTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.documentSetVersion".casefold():
            from .document_set_version import DocumentSetVersion

            return DocumentSetVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domain".casefold():
            from .domain import Domain

            return Domain()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsCnameRecord".casefold():
            from .domain_dns_cname_record import DomainDnsCnameRecord

            return DomainDnsCnameRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsMxRecord".casefold():
            from .domain_dns_mx_record import DomainDnsMxRecord

            return DomainDnsMxRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsRecord".casefold():
            from .domain_dns_record import DomainDnsRecord

            return DomainDnsRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsSrvRecord".casefold():
            from .domain_dns_srv_record import DomainDnsSrvRecord

            return DomainDnsSrvRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsTxtRecord".casefold():
            from .domain_dns_txt_record import DomainDnsTxtRecord

            return DomainDnsTxtRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.domainDnsUnavailableRecord".casefold():
            from .domain_dns_unavailable_record import DomainDnsUnavailableRecord

            return DomainDnsUnavailableRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.drive".casefold():
            from .drive import Drive

            return Drive()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveItem".casefold():
            from .drive_item import DriveItem

            return DriveItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveItemVersion".casefold():
            from .drive_item_version import DriveItemVersion

            return DriveItemVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveProtectionRule".casefold():
            from .drive_protection_rule import DriveProtectionRule

            return DriveProtectionRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveProtectionUnit".casefold():
            from .drive_protection_unit import DriveProtectionUnit

            return DriveProtectionUnit()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveProtectionUnitsBulkAdditionJob".casefold():
            from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob

            return DriveProtectionUnitsBulkAdditionJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveRestoreArtifact".casefold():
            from .drive_restore_artifact import DriveRestoreArtifact

            return DriveRestoreArtifact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.driveRestoreArtifactsBulkAdditionRequest".casefold():
            from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest

            return DriveRestoreArtifactsBulkAdditionRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eBookInstallSummary".casefold():
            from .e_book_install_summary import EBookInstallSummary

            return EBookInstallSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.edge".casefold():
            from .edge import Edge

            return Edge()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.editionUpgradeConfiguration".casefold():
            from .edition_upgrade_configuration import EditionUpgradeConfiguration

            return EditionUpgradeConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationAssignment".casefold():
            from .education_assignment import EducationAssignment

            return EducationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationAssignmentDefaults".casefold():
            from .education_assignment_defaults import EducationAssignmentDefaults

            return EducationAssignmentDefaults()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationAssignmentResource".casefold():
            from .education_assignment_resource import EducationAssignmentResource

            return EducationAssignmentResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationAssignmentSettings".casefold():
            from .education_assignment_settings import EducationAssignmentSettings

            return EducationAssignmentSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationCategory".casefold():
            from .education_category import EducationCategory

            return EducationCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationClass".casefold():
            from .education_class import EducationClass

            return EducationClass()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationFeedbackOutcome".casefold():
            from .education_feedback_outcome import EducationFeedbackOutcome

            return EducationFeedbackOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationFeedbackResourceOutcome".casefold():
            from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome

            return EducationFeedbackResourceOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationGradingCategory".casefold():
            from .education_grading_category import EducationGradingCategory

            return EducationGradingCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationGradingScheme".casefold():
            from .education_grading_scheme import EducationGradingScheme

            return EducationGradingScheme()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationModule".casefold():
            from .education_module import EducationModule

            return EducationModule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationModuleResource".casefold():
            from .education_module_resource import EducationModuleResource

            return EducationModuleResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationOrganization".casefold():
            from .education_organization import EducationOrganization

            return EducationOrganization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationOutcome".casefold():
            from .education_outcome import EducationOutcome

            return EducationOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationPointsOutcome".casefold():
            from .education_points_outcome import EducationPointsOutcome

            return EducationPointsOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationRubric".casefold():
            from .education_rubric import EducationRubric

            return EducationRubric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationRubricOutcome".casefold():
            from .education_rubric_outcome import EducationRubricOutcome

            return EducationRubricOutcome()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationSchool".casefold():
            from .education_school import EducationSchool

            return EducationSchool()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationSubmission".casefold():
            from .education_submission import EducationSubmission

            return EducationSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationSubmissionResource".casefold():
            from .education_submission_resource import EducationSubmissionResource

            return EducationSubmissionResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.educationUser".casefold():
            from .education_user import EducationUser

            return EducationUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailAuthenticationMethod".casefold():
            from .email_authentication_method import EmailAuthenticationMethod

            return EmailAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailAuthenticationMethodConfiguration".casefold():
            from .email_authentication_method_configuration import EmailAuthenticationMethodConfiguration

            return EmailAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailFileAssessmentRequest".casefold():
            from .email_file_assessment_request import EmailFileAssessmentRequest

            return EmailFileAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emergencyCallEvent".casefold():
            from .emergency_call_event import EmergencyCallEvent

            return EmergencyCallEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.employeeExperienceUser".casefold():
            from .employee_experience_user import EmployeeExperienceUser

            return EmployeeExperienceUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.endpoint".casefold():
            from .endpoint import Endpoint

            return Endpoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.endUserNotification".casefold():
            from .end_user_notification import EndUserNotification

            return EndUserNotification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.endUserNotificationDetail".casefold():
            from .end_user_notification_detail import EndUserNotificationDetail

            return EndUserNotificationDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.engagementAsyncOperation".casefold():
            from .engagement_async_operation import EngagementAsyncOperation

            return EngagementAsyncOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.engagementConversation".casefold():
            from .engagement_conversation import EngagementConversation

            return EngagementConversation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.engagementConversationDiscussionMessage".casefold():
            from .engagement_conversation_discussion_message import EngagementConversationDiscussionMessage

            return EngagementConversationDiscussionMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.engagementConversationMessage".casefold():
            from .engagement_conversation_message import EngagementConversationMessage

            return EngagementConversationMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.engagementConversationMessageReaction".casefold():
            from .engagement_conversation_message_reaction import EngagementConversationMessageReaction

            return EngagementConversationMessageReaction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.engagementConversationQuestionMessage".casefold():
            from .engagement_conversation_question_message import EngagementConversationQuestionMessage

            return EngagementConversationQuestionMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.engagementConversationSystemMessage".casefold():
            from .engagement_conversation_system_message import EngagementConversationSystemMessage

            return EngagementConversationSystemMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.engagementRole".casefold():
            from .engagement_role import EngagementRole

            return EngagementRole()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.engagementRoleMember".casefold():
            from .engagement_role_member import EngagementRoleMember

            return EngagementRoleMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enrollmentConfigurationAssignment".casefold():
            from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment

            return EnrollmentConfigurationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enrollmentTroubleshootingEvent".casefold():
            from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent

            return EnrollmentTroubleshootingEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.enterpriseCodeSigningCertificate".casefold():
            from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate

            return EnterpriseCodeSigningCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.entitlementManagement".casefold():
            from .entitlement_management import EntitlementManagement

            return EntitlementManagement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.entitlementManagementSettings".casefold():
            from .entitlement_management_settings import EntitlementManagementSettings

            return EntitlementManagementSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.event".casefold():
            from .event import Event

            return Event()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessage".casefold():
            from .event_message import EventMessage

            return EventMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessageRequest".casefold():
            from .event_message_request import EventMessageRequest

            return EventMessageRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.eventMessageResponse".casefold():
            from .event_message_response import EventMessageResponse

            return EventMessageResponse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exchangeProtectionPolicy".casefold():
            from .exchange_protection_policy import ExchangeProtectionPolicy

            return ExchangeProtectionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.exchangeRestoreSession".casefold():
            from .exchange_restore_session import ExchangeRestoreSession

            return ExchangeRestoreSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.extension".casefold():
            from .extension import Extension

            return Extension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.extensionProperty".casefold():
            from .extension_property import ExtensionProperty

            return ExtensionProperty()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.connectionOperation".casefold():
            from .external_connectors.connection_operation import ConnectionOperation

            return ConnectionOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalActivity".casefold():
            from .external_connectors.external_activity import ExternalActivity

            return ExternalActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalActivityResult".casefold():
            from .external_connectors.external_activity_result import ExternalActivityResult

            return ExternalActivityResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalConnection".casefold():
            from .external_connectors.external_connection import ExternalConnection

            return ExternalConnection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalGroup".casefold():
            from .external_connectors.external_group import ExternalGroup

            return ExternalGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.externalItem".casefold():
            from .external_connectors.external_item import ExternalItem

            return ExternalItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.identity".casefold():
            from .external_connectors.identity import Identity

            return Identity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalConnectors.schema".casefold():
            from .external_connectors.schema import Schema

            return Schema()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalDomainName".casefold():
            from .external_domain_name import ExternalDomainName

            return ExternalDomainName()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalUsersSelfServiceSignUpEventsFlow".casefold():
            from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow

            return ExternalUsersSelfServiceSignUpEventsFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.featureRolloutPolicy".casefold():
            from .feature_rollout_policy import FeatureRolloutPolicy

            return FeatureRolloutPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.federatedIdentityCredential".casefold():
            from .federated_identity_credential import FederatedIdentityCredential

            return FederatedIdentityCredential()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fido2AuthenticationMethod".casefold():
            from .fido2_authentication_method import Fido2AuthenticationMethod

            return Fido2AuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fido2AuthenticationMethodConfiguration".casefold():
            from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration

            return Fido2AuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fido2CombinationConfiguration".casefold():
            from .fido2_combination_configuration import Fido2CombinationConfiguration

            return Fido2CombinationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fieldValueSet".casefold():
            from .field_value_set import FieldValueSet

            return FieldValueSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileAssessmentRequest".casefold():
            from .file_assessment_request import FileAssessmentRequest

            return FileAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileAttachment".casefold():
            from .file_attachment import FileAttachment

            return FileAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileStorage".casefold():
            from .file_storage import FileStorage

            return FileStorage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileStorageContainer".casefold():
            from .file_storage_container import FileStorageContainer

            return FileStorageContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileStorageContainerType".casefold():
            from .file_storage_container_type import FileStorageContainerType

            return FileStorageContainerType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fileStorageContainerTypeRegistration".casefold():
            from .file_storage_container_type_registration import FileStorageContainerTypeRegistration

            return FileStorageContainerTypeRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.filterOperatorSchema".casefold():
            from .filter_operator_schema import FilterOperatorSchema

            return FilterOperatorSchema()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fixtureMap".casefold():
            from .fixture_map import FixtureMap

            return FixtureMap()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.floor".casefold():
            from .floor import Floor

            return Floor()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.footprintMap".casefold():
            from .footprint_map import FootprintMap

            return FootprintMap()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.fraudProtectionProvider".casefold():
            from .fraud_protection_provider import FraudProtectionProvider

            return FraudProtectionProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.governanceInsight".casefold():
            from .governance_insight import GovernanceInsight

            return GovernanceInsight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.granularMailboxRestoreArtifact".casefold():
            from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact

            return GranularMailboxRestoreArtifact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.group".casefold():
            from .group import Group
            from .term_store.group import Group

            return Group()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupLifecyclePolicy".casefold():
            from .group_lifecycle_policy import GroupLifecyclePolicy

            return GroupLifecyclePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupSetting".casefold():
            from .group_setting import GroupSetting

            return GroupSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupSettingTemplate".casefold():
            from .group_setting_template import GroupSettingTemplate

            return GroupSettingTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.homeRealmDiscoveryPolicy".casefold():
            from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy

            return HomeRealmDiscoveryPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.horizontalSection".casefold():
            from .horizontal_section import HorizontalSection

            return HorizontalSection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.horizontalSectionColumn".casefold():
            from .horizontal_section_column import HorizontalSectionColumn

            return HorizontalSectionColumn()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.humanSecurityFraudProtectionProvider".casefold():
            from .human_security_fraud_protection_provider import HumanSecurityFraudProtectionProvider

            return HumanSecurityFraudProtectionProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityApiConnector".casefold():
            from .identity_api_connector import IdentityApiConnector

            return IdentityApiConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityBuiltInUserFlowAttribute".casefold():
            from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute

            return IdentityBuiltInUserFlowAttribute()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityContainer".casefold():
            from .identity_container import IdentityContainer
            from .security.identity_container import IdentityContainer

            return IdentityContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityCustomUserFlowAttribute".casefold():
            from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute

            return IdentityCustomUserFlowAttribute()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.customTaskExtension".casefold():
            from .identity_governance.custom_task_extension import CustomTaskExtension

            return CustomTaskExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.insights".casefold():
            from .identity_governance.insights import Insights

            return Insights()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.lifecycleManagementSettings".casefold():
            from .identity_governance.lifecycle_management_settings import LifecycleManagementSettings

            return LifecycleManagementSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.lifecycleWorkflowsContainer".casefold():
            from .identity_governance.lifecycle_workflows_container import LifecycleWorkflowsContainer

            return LifecycleWorkflowsContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.run".casefold():
            from .identity_governance.run import Run

            return Run()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.task".casefold():
            from .identity_governance.task import Task

            return Task()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.taskDefinition".casefold():
            from .identity_governance.task_definition import TaskDefinition

            return TaskDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.taskProcessingResult".casefold():
            from .identity_governance.task_processing_result import TaskProcessingResult

            return TaskProcessingResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.taskReport".casefold():
            from .identity_governance.task_report import TaskReport

            return TaskReport()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.userProcessingResult".casefold():
            from .identity_governance.user_processing_result import UserProcessingResult

            return UserProcessingResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityGovernance.workflowTemplate".casefold():
            from .identity_governance.workflow_template import WorkflowTemplate

            return WorkflowTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityProvider".casefold():
            from .identity_provider import IdentityProvider

            return IdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityProviderBase".casefold():
            from .identity_provider_base import IdentityProviderBase

            return IdentityProviderBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identitySecurityDefaultsEnforcementPolicy".casefold():
            from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy

            return IdentitySecurityDefaultsEnforcementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityUserFlow".casefold():
            from .identity_user_flow import IdentityUserFlow

            return IdentityUserFlow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityUserFlowAttribute".casefold():
            from .identity_user_flow_attribute import IdentityUserFlowAttribute

            return IdentityUserFlowAttribute()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.identityUserFlowAttributeAssignment".casefold():
            from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment

            return IdentityUserFlowAttributeAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.importedWindowsAutopilotDeviceIdentity".casefold():
            from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity

            return ImportedWindowsAutopilotDeviceIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.importedWindowsAutopilotDeviceIdentityUpload".casefold():
            from .imported_windows_autopilot_device_identity_upload import ImportedWindowsAutopilotDeviceIdentityUpload

            return ImportedWindowsAutopilotDeviceIdentityUpload()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inferenceClassification".casefold():
            from .inference_classification import InferenceClassification

            return InferenceClassification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inferenceClassificationOverride".casefold():
            from .inference_classification_override import InferenceClassificationOverride

            return InferenceClassificationOverride()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.insightsSettings".casefold():
            from .insights_settings import InsightsSettings

            return InsightsSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.internalDomainFederation".casefold():
            from .internal_domain_federation import InternalDomainFederation

            return InternalDomainFederation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.internetExplorerMode".casefold():
            from .internet_explorer_mode import InternetExplorerMode

            return InternetExplorerMode()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.invitation".casefold():
            from .invitation import Invitation

            return Invitation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.inviteParticipantsOperation".casefold():
            from .invite_participants_operation import InviteParticipantsOperation

            return InviteParticipantsOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCertificateProfile".casefold():
            from .ios_certificate_profile import IosCertificateProfile

            return IosCertificateProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCompliancePolicy".casefold():
            from .ios_compliance_policy import IosCompliancePolicy

            return IosCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosCustomConfiguration".casefold():
            from .ios_custom_configuration import IosCustomConfiguration

            return IosCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosDeviceFeaturesConfiguration".casefold():
            from .ios_device_features_configuration import IosDeviceFeaturesConfiguration

            return IosDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosGeneralDeviceConfiguration".casefold():
            from .ios_general_device_configuration import IosGeneralDeviceConfiguration

            return IosGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosiPadOSWebClip".casefold():
            from .iosi_pad_o_s_web_clip import IosiPadOSWebClip

            return IosiPadOSWebClip()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosLobApp".casefold():
            from .ios_lob_app import IosLobApp

            return IosLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosLobAppProvisioningConfigurationAssignment".casefold():
            from .ios_lob_app_provisioning_configuration_assignment import IosLobAppProvisioningConfigurationAssignment

            return IosLobAppProvisioningConfigurationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosManagedAppProtection".casefold():
            from .ios_managed_app_protection import IosManagedAppProtection

            return IosManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosManagedAppRegistration".casefold():
            from .ios_managed_app_registration import IosManagedAppRegistration

            return IosManagedAppRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosMobileAppConfiguration".casefold():
            from .ios_mobile_app_configuration import IosMobileAppConfiguration

            return IosMobileAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosStoreApp".casefold():
            from .ios_store_app import IosStoreApp

            return IosStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosUpdateConfiguration".casefold():
            from .ios_update_configuration import IosUpdateConfiguration

            return IosUpdateConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosUpdateDeviceStatus".casefold():
            from .ios_update_device_status import IosUpdateDeviceStatus

            return IosUpdateDeviceStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppApp".casefold():
            from .ios_vpp_app import IosVppApp

            return IosVppApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppEBook".casefold():
            from .ios_vpp_e_book import IosVppEBook

            return IosVppEBook()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.iosVppEBookAssignment".casefold():
            from .ios_vpp_e_book_assignment import IosVppEBookAssignment

            return IosVppEBookAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.ipNamedLocation".casefold():
            from .ip_named_location import IpNamedLocation

            return IpNamedLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemActivity".casefold():
            from .item_activity import ItemActivity

            return ItemActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemActivityStat".casefold():
            from .item_activity_stat import ItemActivityStat

            return ItemActivityStat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemAnalytics".casefold():
            from .item_analytics import ItemAnalytics

            return ItemAnalytics()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemAttachment".casefold():
            from .item_attachment import ItemAttachment

            return ItemAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemInsights".casefold():
            from .item_insights import ItemInsights

            return ItemInsights()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.itemRetentionLabel".casefold():
            from .item_retention_label import ItemRetentionLabel

            return ItemRetentionLabel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.labelContentRight".casefold():
            from .label_content_right import LabelContentRight

            return LabelContentRight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.landingPage".casefold():
            from .landing_page import LandingPage

            return LandingPage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.landingPageDetail".casefold():
            from .landing_page_detail import LandingPageDetail

            return LandingPageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.learningAssignment".casefold():
            from .learning_assignment import LearningAssignment

            return LearningAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.learningContent".casefold():
            from .learning_content import LearningContent

            return LearningContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.learningCourseActivity".casefold():
            from .learning_course_activity import LearningCourseActivity

            return LearningCourseActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.learningProvider".casefold():
            from .learning_provider import LearningProvider

            return LearningProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.learningSelfInitiatedCourse".casefold():
            from .learning_self_initiated_course import LearningSelfInitiatedCourse

            return LearningSelfInitiatedCourse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.levelMap".casefold():
            from .level_map import LevelMap

            return LevelMap()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.licenseDetails".casefold():
            from .license_details import LicenseDetails

            return LicenseDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.linkedResource".casefold():
            from .linked_resource import LinkedResource

            return LinkedResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.list".casefold():
            from .list_ import List_

            return List_()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.listItem".casefold():
            from .list_item import ListItem

            return ListItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.listItemVersion".casefold():
            from .list_item_version import ListItemVersion

            return ListItemVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.localizedNotificationMessage".casefold():
            from .localized_notification_message import LocalizedNotificationMessage

            return LocalizedNotificationMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.loginPage".casefold():
            from .login_page import LoginPage

            return LoginPage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.longRunningOperation".casefold():
            from .long_running_operation import LongRunningOperation

            return LongRunningOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.m365AppsInstallationOptions".casefold():
            from .m365_apps_installation_options import M365AppsInstallationOptions

            return M365AppsInstallationOptions()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCompliancePolicy".casefold():
            from .mac_o_s_compliance_policy import MacOSCompliancePolicy

            return MacOSCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSCustomConfiguration".casefold():
            from .mac_o_s_custom_configuration import MacOSCustomConfiguration

            return MacOSCustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSDeviceFeaturesConfiguration".casefold():
            from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration

            return MacOSDeviceFeaturesConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSDmgApp".casefold():
            from .mac_o_s_dmg_app import MacOSDmgApp

            return MacOSDmgApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSGeneralDeviceConfiguration".casefold():
            from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration

            return MacOSGeneralDeviceConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSLobApp".casefold():
            from .mac_o_s_lob_app import MacOSLobApp

            return MacOSLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSMicrosoftDefenderApp".casefold():
            from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp

            return MacOSMicrosoftDefenderApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSMicrosoftEdgeApp".casefold():
            from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp

            return MacOSMicrosoftEdgeApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.macOSOfficeSuiteApp".casefold():
            from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp

            return MacOSOfficeSuiteApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailAssessmentRequest".casefold():
            from .mail_assessment_request import MailAssessmentRequest

            return MailAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailboxProtectionRule".casefold():
            from .mailbox_protection_rule import MailboxProtectionRule

            return MailboxProtectionRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailboxProtectionUnit".casefold():
            from .mailbox_protection_unit import MailboxProtectionUnit

            return MailboxProtectionUnit()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailboxProtectionUnitsBulkAdditionJob".casefold():
            from .mailbox_protection_units_bulk_addition_job import MailboxProtectionUnitsBulkAdditionJob

            return MailboxProtectionUnitsBulkAdditionJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailboxRestoreArtifact".casefold():
            from .mailbox_restore_artifact import MailboxRestoreArtifact

            return MailboxRestoreArtifact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailboxRestoreArtifactsBulkAdditionRequest".casefold():
            from .mailbox_restore_artifacts_bulk_addition_request import MailboxRestoreArtifactsBulkAdditionRequest

            return MailboxRestoreArtifactsBulkAdditionRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailFolder".casefold():
            from .mail_folder import MailFolder

            return MailFolder()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailSearchFolder".casefold():
            from .mail_search_folder import MailSearchFolder

            return MailSearchFolder()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.malwareStateForWindowsDevice".casefold():
            from .malware_state_for_windows_device import MalwareStateForWindowsDevice

            return MalwareStateForWindowsDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAndroidLobApp".casefold():
            from .managed_android_lob_app import ManagedAndroidLobApp

            return ManagedAndroidLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAndroidStoreApp".casefold():
            from .managed_android_store_app import ManagedAndroidStoreApp

            return ManagedAndroidStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedApp".casefold():
            from .managed_app import ManagedApp

            return ManagedApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppConfiguration".casefold():
            from .managed_app_configuration import ManagedAppConfiguration

            return ManagedAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppOperation".casefold():
            from .managed_app_operation import ManagedAppOperation

            return ManagedAppOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppPolicy".casefold():
            from .managed_app_policy import ManagedAppPolicy

            return ManagedAppPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppPolicyDeploymentSummary".casefold():
            from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary

            return ManagedAppPolicyDeploymentSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppProtection".casefold():
            from .managed_app_protection import ManagedAppProtection

            return ManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppRegistration".casefold():
            from .managed_app_registration import ManagedAppRegistration

            return ManagedAppRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppStatus".casefold():
            from .managed_app_status import ManagedAppStatus

            return ManagedAppStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedAppStatusRaw".casefold():
            from .managed_app_status_raw import ManagedAppStatusRaw

            return ManagedAppStatusRaw()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDevice".casefold():
            from .managed_device import ManagedDevice

            return ManagedDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfiguration".casefold():
            from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration

            return ManagedDeviceMobileAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationAssignment".casefold():
            from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment

            return ManagedDeviceMobileAppConfigurationAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationDeviceStatus".casefold():
            from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus

            return ManagedDeviceMobileAppConfigurationDeviceStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationDeviceSummary".casefold():
            from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary

            return ManagedDeviceMobileAppConfigurationDeviceSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationUserStatus".casefold():
            from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus

            return ManagedDeviceMobileAppConfigurationUserStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceMobileAppConfigurationUserSummary".casefold():
            from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary

            return ManagedDeviceMobileAppConfigurationUserSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedDeviceOverview".casefold():
            from .managed_device_overview import ManagedDeviceOverview

            return ManagedDeviceOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedEBook".casefold():
            from .managed_e_book import ManagedEBook

            return ManagedEBook()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedEBookAssignment".casefold():
            from .managed_e_book_assignment import ManagedEBookAssignment

            return ManagedEBookAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedIOSLobApp".casefold():
            from .managed_i_o_s_lob_app import ManagedIOSLobApp

            return ManagedIOSLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedIOSStoreApp".casefold():
            from .managed_i_o_s_store_app import ManagedIOSStoreApp

            return ManagedIOSStoreApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedMobileApp".casefold():
            from .managed_mobile_app import ManagedMobileApp

            return ManagedMobileApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.managedMobileLobApp".casefold():
            from .managed_mobile_lob_app import ManagedMobileLobApp

            return ManagedMobileLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mdmWindowsInformationProtectionPolicy".casefold():
            from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy

            return MdmWindowsInformationProtectionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.meetingAttendanceReport".casefold():
            from .meeting_attendance_report import MeetingAttendanceReport

            return MeetingAttendanceReport()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.membershipOutlierInsight".casefold():
            from .membership_outlier_insight import MembershipOutlierInsight

            return MembershipOutlierInsight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.message".casefold():
            from .message import Message

            return Message()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.messageRule".casefold():
            from .message_rule import MessageRule

            return MessageRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAccountUserConversationMember".casefold():
            from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember

            return MicrosoftAccountUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethod".casefold():
            from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod

            return MicrosoftAuthenticatorAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodConfiguration".casefold():
            from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration

            return MicrosoftAuthenticatorAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftAuthenticatorAuthenticationMethodTarget".casefold():
            from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget

            return MicrosoftAuthenticatorAuthenticationMethodTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftStoreForBusinessApp".casefold():
            from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp

            return MicrosoftStoreForBusinessApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileApp".casefold():
            from .mobile_app import MobileApp

            return MobileApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppAssignment".casefold():
            from .mobile_app_assignment import MobileAppAssignment

            return MobileAppAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppCategory".casefold():
            from .mobile_app_category import MobileAppCategory

            return MobileAppCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppContent".casefold():
            from .mobile_app_content import MobileAppContent

            return MobileAppContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppContentFile".casefold():
            from .mobile_app_content_file import MobileAppContentFile

            return MobileAppContentFile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppRelationship".casefold():
            from .mobile_app_relationship import MobileAppRelationship

            return MobileAppRelationship()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileAppTroubleshootingEvent".casefold():
            from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent

            return MobileAppTroubleshootingEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileContainedApp".casefold():
            from .mobile_contained_app import MobileContainedApp

            return MobileContainedApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileLobApp".casefold():
            from .mobile_lob_app import MobileLobApp

            return MobileLobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mobileThreatDefenseConnector".casefold():
            from .mobile_threat_defense_connector import MobileThreatDefenseConnector

            return MobileThreatDefenseConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiTenantOrganization".casefold():
            from .multi_tenant_organization import MultiTenantOrganization

            return MultiTenantOrganization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiTenantOrganizationIdentitySyncPolicyTemplate".casefold():
            from .multi_tenant_organization_identity_sync_policy_template import MultiTenantOrganizationIdentitySyncPolicyTemplate

            return MultiTenantOrganizationIdentitySyncPolicyTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiTenantOrganizationJoinRequestRecord".casefold():
            from .multi_tenant_organization_join_request_record import MultiTenantOrganizationJoinRequestRecord

            return MultiTenantOrganizationJoinRequestRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiTenantOrganizationMember".casefold():
            from .multi_tenant_organization_member import MultiTenantOrganizationMember

            return MultiTenantOrganizationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiTenantOrganizationPartnerConfigurationTemplate".casefold():
            from .multi_tenant_organization_partner_configuration_template import MultiTenantOrganizationPartnerConfigurationTemplate

            return MultiTenantOrganizationPartnerConfigurationTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.multiValueLegacyExtendedProperty".casefold():
            from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty

            return MultiValueLegacyExtendedProperty()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.muteParticipantOperation".casefold():
            from .mute_participant_operation import MuteParticipantOperation

            return MuteParticipantOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.namedLocation".casefold():
            from .named_location import NamedLocation

            return NamedLocation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.notebook".casefold():
            from .notebook import Notebook

            return Notebook()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.notificationMessageTemplate".casefold():
            from .notification_message_template import NotificationMessageTemplate

            return NotificationMessageTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.oAuth2PermissionGrant".casefold():
            from .o_auth2_permission_grant import OAuth2PermissionGrant

            return OAuth2PermissionGrant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.offerShiftRequest".casefold():
            from .offer_shift_request import OfferShiftRequest

            return OfferShiftRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.officeGraphInsights".casefold():
            from .office_graph_insights import OfficeGraphInsights

            return OfficeGraphInsights()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAttributeCollectionListener".casefold():
            from .on_attribute_collection_listener import OnAttributeCollectionListener

            return OnAttributeCollectionListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAttributeCollectionStartCustomExtension".casefold():
            from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension

            return OnAttributeCollectionStartCustomExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAttributeCollectionStartListener".casefold():
            from .on_attribute_collection_start_listener import OnAttributeCollectionStartListener

            return OnAttributeCollectionStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAttributeCollectionSubmitCustomExtension".casefold():
            from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension

            return OnAttributeCollectionSubmitCustomExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAttributeCollectionSubmitListener".casefold():
            from .on_attribute_collection_submit_listener import OnAttributeCollectionSubmitListener

            return OnAttributeCollectionSubmitListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onAuthenticationMethodLoadStartListener".casefold():
            from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener

            return OnAuthenticationMethodLoadStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.oneDriveForBusinessProtectionPolicy".casefold():
            from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy

            return OneDriveForBusinessProtectionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.oneDriveForBusinessRestoreSession".casefold():
            from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession

            return OneDriveForBusinessRestoreSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onEmailOtpSendListener".casefold():
            from .on_email_otp_send_listener import OnEmailOtpSendListener

            return OnEmailOtpSendListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenote".casefold():
            from .onenote import Onenote

            return Onenote()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteEntityBaseModel".casefold():
            from .onenote_entity_base_model import OnenoteEntityBaseModel

            return OnenoteEntityBaseModel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteEntityHierarchyModel".casefold():
            from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel

            return OnenoteEntityHierarchyModel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteEntitySchemaObjectModel".casefold():
            from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel

            return OnenoteEntitySchemaObjectModel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteOperation".casefold():
            from .onenote_operation import OnenoteOperation

            return OnenoteOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenotePage".casefold():
            from .onenote_page import OnenotePage

            return OnenotePage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteResource".casefold():
            from .onenote_resource import OnenoteResource

            return OnenoteResource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteSection".casefold():
            from .onenote_section import OnenoteSection

            return OnenoteSection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onFraudProtectionLoadStartListener".casefold():
            from .on_fraud_protection_load_start_listener import OnFraudProtectionLoadStartListener

            return OnFraudProtectionLoadStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onInteractiveAuthFlowStartListener".casefold():
            from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener

            return OnInteractiveAuthFlowStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onlineMeeting".casefold():
            from .online_meeting import OnlineMeeting

            return OnlineMeeting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onlineMeetingBase".casefold():
            from .online_meeting_base import OnlineMeetingBase

            return OnlineMeetingBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onlineMeetingEngagementConversation".casefold():
            from .online_meeting_engagement_conversation import OnlineMeetingEngagementConversation

            return OnlineMeetingEngagementConversation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onOtpSendCustomExtension".casefold():
            from .on_otp_send_custom_extension import OnOtpSendCustomExtension

            return OnOtpSendCustomExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onPremisesConditionalAccessSettings".casefold():
            from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings

            return OnPremisesConditionalAccessSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onPremisesDirectorySynchronization".casefold():
            from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization

            return OnPremisesDirectorySynchronization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onPremisesSyncBehavior".casefold():
            from .on_premises_sync_behavior import OnPremisesSyncBehavior

            return OnPremisesSyncBehavior()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onTokenIssuanceStartCustomExtension".casefold():
            from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension

            return OnTokenIssuanceStartCustomExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onTokenIssuanceStartListener".casefold():
            from .on_token_issuance_start_listener import OnTokenIssuanceStartListener

            return OnTokenIssuanceStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onUserCreateStartListener".casefold():
            from .on_user_create_start_listener import OnUserCreateStartListener

            return OnUserCreateStartListener()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openShift".casefold():
            from .open_shift import OpenShift

            return OpenShift()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openShiftChangeRequest".casefold():
            from .open_shift_change_request import OpenShiftChangeRequest

            return OpenShiftChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.openTypeExtension".casefold():
            from .open_type_extension import OpenTypeExtension

            return OpenTypeExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.operation".casefold():
            from .operation import Operation
            from .partners.billing.operation import Operation

            return Operation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organization".casefold():
            from .organization import Organization

            return Organization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organizationalBranding".casefold():
            from .organizational_branding import OrganizationalBranding

            return OrganizationalBranding()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organizationalBrandingLocalization".casefold():
            from .organizational_branding_localization import OrganizationalBrandingLocalization

            return OrganizationalBrandingLocalization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.organizationalBrandingProperties".casefold():
            from .organizational_branding_properties import OrganizationalBrandingProperties

            return OrganizationalBrandingProperties()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.orgContact".casefold():
            from .org_contact import OrgContact

            return OrgContact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.outlookCategory".casefold():
            from .outlook_category import OutlookCategory

            return OutlookCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.outlookItem".casefold():
            from .outlook_item import OutlookItem

            return OutlookItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.outlookUser".casefold():
            from .outlook_user import OutlookUser

            return OutlookUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.participant".casefold():
            from .call_records.participant import Participant
            from .participant import Participant

            return Participant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.participantJoiningNotification".casefold():
            from .participant_joining_notification import ParticipantJoiningNotification

            return ParticipantJoiningNotification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.participantLeftNotification".casefold():
            from .participant_left_notification import ParticipantLeftNotification

            return ParticipantLeftNotification()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners".casefold():
            from .partners.partners import Partners

            return Partners()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.azureUsage".casefold():
            from .partners.billing.azure_usage import AzureUsage

            return AzureUsage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.billedReconciliation".casefold():
            from .partners.billing.billed_reconciliation import BilledReconciliation

            return BilledReconciliation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.billedUsage".casefold():
            from .partners.billing.billed_usage import BilledUsage

            return BilledUsage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.billing".casefold():
            from .partners.billing.billing import Billing

            return Billing()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.billingReconciliation".casefold():
            from .partners.billing.billing_reconciliation import BillingReconciliation

            return BillingReconciliation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.exportSuccessOperation".casefold():
            from .partners.billing.export_success_operation import ExportSuccessOperation

            return ExportSuccessOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.failedOperation".casefold():
            from .partners.billing.failed_operation import FailedOperation

            return FailedOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.manifest".casefold():
            from .partners.billing.manifest import Manifest

            return Manifest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.operation".casefold():
            from .operation import Operation
            from .partners.billing.operation import Operation

            return Operation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.runningOperation".casefold():
            from .partners.billing.running_operation import RunningOperation

            return RunningOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.unbilledReconciliation".casefold():
            from .partners.billing.unbilled_reconciliation import UnbilledReconciliation

            return UnbilledReconciliation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.partners.billing.unbilledUsage".casefold():
            from .partners.billing.unbilled_usage import UnbilledUsage

            return UnbilledUsage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.passwordAuthenticationMethod".casefold():
            from .password_authentication_method import PasswordAuthenticationMethod

            return PasswordAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.payload".casefold():
            from .payload import Payload

            return Payload()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.peopleAdminSettings".casefold():
            from .people_admin_settings import PeopleAdminSettings

            return PeopleAdminSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permission".casefold():
            from .permission import Permission

            return Permission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionGrantConditionSet".casefold():
            from .permission_grant_condition_set import PermissionGrantConditionSet

            return PermissionGrantConditionSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.permissionGrantPolicy".casefold():
            from .permission_grant_policy import PermissionGrantPolicy

            return PermissionGrantPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.person".casefold():
            from .person import Person

            return Person()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.phoneAuthenticationMethod".casefold():
            from .phone_authentication_method import PhoneAuthenticationMethod

            return PhoneAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.phoneUserConversationMember".casefold():
            from .phone_user_conversation_member import PhoneUserConversationMember

            return PhoneUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.pinnedChatMessageInfo".casefold():
            from .pinned_chat_message_info import PinnedChatMessageInfo

            return PinnedChatMessageInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.place".casefold():
            from .place import Place

            return Place()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.planner".casefold():
            from .planner import Planner

            return Planner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerAssignedToTaskBoardTaskFormat".casefold():
            from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat

            return PlannerAssignedToTaskBoardTaskFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerBucket".casefold():
            from .planner_bucket import PlannerBucket

            return PlannerBucket()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerBucketTaskBoardTaskFormat".casefold():
            from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat

            return PlannerBucketTaskBoardTaskFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerGroup".casefold():
            from .planner_group import PlannerGroup

            return PlannerGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerPlan".casefold():
            from .planner_plan import PlannerPlan

            return PlannerPlan()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerPlanDetails".casefold():
            from .planner_plan_details import PlannerPlanDetails

            return PlannerPlanDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerProgressTaskBoardTaskFormat".casefold():
            from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat

            return PlannerProgressTaskBoardTaskFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerTask".casefold():
            from .planner_task import PlannerTask

            return PlannerTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerTaskDetails".casefold():
            from .planner_task_details import PlannerTaskDetails

            return PlannerTaskDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.plannerUser".casefold():
            from .planner_user import PlannerUser

            return PlannerUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.platformCredentialAuthenticationMethod".casefold():
            from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod

            return PlatformCredentialAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.playPromptOperation".casefold():
            from .play_prompt_operation import PlayPromptOperation

            return PlayPromptOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.policyBase".casefold():
            from .policy_base import PolicyBase

            return PolicyBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.policyRoot".casefold():
            from .policy_root import PolicyRoot

            return PolicyRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.policyTemplate".casefold():
            from .policy_template import PolicyTemplate

            return PolicyTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.post".casefold():
            from .post import Post

            return Post()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.presence".casefold():
            from .presence import Presence

            return Presence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printConnector".casefold():
            from .print_connector import PrintConnector

            return PrintConnector()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printDocument".casefold():
            from .print_document import PrintDocument

            return PrintDocument()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printer".casefold():
            from .printer import Printer

            return Printer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printerBase".casefold():
            from .printer_base import PrinterBase

            return PrinterBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printerCreateOperation".casefold():
            from .printer_create_operation import PrinterCreateOperation

            return PrinterCreateOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printerShare".casefold():
            from .printer_share import PrinterShare

            return PrinterShare()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printJob".casefold():
            from .print_job import PrintJob

            return PrintJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printOperation".casefold():
            from .print_operation import PrintOperation

            return PrintOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printService".casefold():
            from .print_service import PrintService

            return PrintService()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printServiceEndpoint".casefold():
            from .print_service_endpoint import PrintServiceEndpoint

            return PrintServiceEndpoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printTask".casefold():
            from .print_task import PrintTask

            return PrintTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printTaskDefinition".casefold():
            from .print_task_definition import PrintTaskDefinition

            return PrintTaskDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printTaskTrigger".casefold():
            from .print_task_trigger import PrintTaskTrigger

            return PrintTaskTrigger()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printUsage".casefold():
            from .print_usage import PrintUsage

            return PrintUsage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printUsageByPrinter".casefold():
            from .print_usage_by_printer import PrintUsageByPrinter

            return PrintUsageByPrinter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.printUsageByUser".casefold():
            from .print_usage_by_user import PrintUsageByUser

            return PrintUsageByUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroup".casefold():
            from .privileged_access_group import PrivilegedAccessGroup

            return PrivilegedAccessGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupAssignmentSchedule".casefold():
            from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule

            return PrivilegedAccessGroupAssignmentSchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupAssignmentScheduleInstance".casefold():
            from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance

            return PrivilegedAccessGroupAssignmentScheduleInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupAssignmentScheduleRequest".casefold():
            from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest

            return PrivilegedAccessGroupAssignmentScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupEligibilitySchedule".casefold():
            from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule

            return PrivilegedAccessGroupEligibilitySchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupEligibilityScheduleInstance".casefold():
            from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance

            return PrivilegedAccessGroupEligibilityScheduleInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessGroupEligibilityScheduleRequest".casefold():
            from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest

            return PrivilegedAccessGroupEligibilityScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessRoot".casefold():
            from .privileged_access_root import PrivilegedAccessRoot

            return PrivilegedAccessRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessSchedule".casefold():
            from .privileged_access_schedule import PrivilegedAccessSchedule

            return PrivilegedAccessSchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessScheduleInstance".casefold():
            from .privileged_access_schedule_instance import PrivilegedAccessScheduleInstance

            return PrivilegedAccessScheduleInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.privilegedAccessScheduleRequest".casefold():
            from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest

            return PrivilegedAccessScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.profileCardProperty".casefold():
            from .profile_card_property import ProfileCardProperty

            return ProfileCardProperty()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.profilePhoto".casefold():
            from .profile_photo import ProfilePhoto

            return ProfilePhoto()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.pronounsSettings".casefold():
            from .pronouns_settings import PronounsSettings

            return PronounsSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.protectionPolicyBase".casefold():
            from .protection_policy_base import ProtectionPolicyBase

            return ProtectionPolicyBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.protectionRuleBase".casefold():
            from .protection_rule_base import ProtectionRuleBase

            return ProtectionRuleBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.protectionUnitBase".casefold():
            from .protection_unit_base import ProtectionUnitBase

            return ProtectionUnitBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.protectionUnitsBulkJobBase".casefold():
            from .protection_units_bulk_job_base import ProtectionUnitsBulkJobBase

            return ProtectionUnitsBulkJobBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.provisioningObjectSummary".casefold():
            from .provisioning_object_summary import ProvisioningObjectSummary

            return ProvisioningObjectSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.publicKeyInfrastructureRoot".casefold():
            from .public_key_infrastructure_root import PublicKeyInfrastructureRoot

            return PublicKeyInfrastructureRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.rbacApplication".casefold():
            from .rbac_application import RbacApplication

            return RbacApplication()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.readingAssignmentSubmission".casefold():
            from .reading_assignment_submission import ReadingAssignmentSubmission

            return ReadingAssignmentSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.readingCoachPassage".casefold():
            from .reading_coach_passage import ReadingCoachPassage

            return ReadingCoachPassage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recordOperation".casefold():
            from .record_operation import RecordOperation

            return RecordOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recycleBin".casefold():
            from .recycle_bin import RecycleBin

            return RecycleBin()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.recycleBinItem".casefold():
            from .recycle_bin_item import RecycleBinItem

            return RecycleBinItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.referenceAttachment".casefold():
            from .reference_attachment import ReferenceAttachment

            return ReferenceAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.reflectCheckInResponse".casefold():
            from .reflect_check_in_response import ReflectCheckInResponse

            return ReflectCheckInResponse()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.relyingPartyDetailedSummary".casefold():
            from .relying_party_detailed_summary import RelyingPartyDetailedSummary

            return RelyingPartyDetailedSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.remoteAssistancePartner".casefold():
            from .remote_assistance_partner import RemoteAssistancePartner

            return RemoteAssistancePartner()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.remoteDesktopSecurityConfiguration".casefold():
            from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration

            return RemoteDesktopSecurityConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.reportsRoot".casefold():
            from .reports_root import ReportsRoot

            return ReportsRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.request".casefold():
            from .request import Request

            return Request()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.resellerDelegatedAdminRelationship".casefold():
            from .reseller_delegated_admin_relationship import ResellerDelegatedAdminRelationship

            return ResellerDelegatedAdminRelationship()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.resourceOperation".casefold():
            from .resource_operation import ResourceOperation

            return ResourceOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.resourceSpecificPermissionGrant".casefold():
            from .resource_specific_permission_grant import ResourceSpecificPermissionGrant

            return ResourceSpecificPermissionGrant()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.restoreArtifactBase".casefold():
            from .restore_artifact_base import RestoreArtifactBase

            return RestoreArtifactBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.restoreArtifactsBulkRequestBase".casefold():
            from .restore_artifacts_bulk_request_base import RestoreArtifactsBulkRequestBase

            return RestoreArtifactsBulkRequestBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.restorePoint".casefold():
            from .restore_point import RestorePoint

            return RestorePoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.restoreSessionBase".casefold():
            from .restore_session_base import RestoreSessionBase

            return RestoreSessionBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.richLongRunningOperation".casefold():
            from .rich_long_running_operation import RichLongRunningOperation

            return RichLongRunningOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskDetection".casefold():
            from .risk_detection import RiskDetection

            return RiskDetection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyServicePrincipal".casefold():
            from .risky_service_principal import RiskyServicePrincipal

            return RiskyServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyServicePrincipalHistoryItem".casefold():
            from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem

            return RiskyServicePrincipalHistoryItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyUser".casefold():
            from .risky_user import RiskyUser

            return RiskyUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.riskyUserHistoryItem".casefold():
            from .risky_user_history_item import RiskyUserHistoryItem

            return RiskyUserHistoryItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roleAssignment".casefold():
            from .role_assignment import RoleAssignment

            return RoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roleDefinition".casefold():
            from .role_definition import RoleDefinition

            return RoleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.room".casefold():
            from .room import Room

            return Room()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.roomList".casefold():
            from .room_list import RoomList

            return RoomList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.samlOrWsFedExternalDomainFederation".casefold():
            from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation

            return SamlOrWsFedExternalDomainFederation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.samlOrWsFedProvider".casefold():
            from .saml_or_ws_fed_provider import SamlOrWsFedProvider

            return SamlOrWsFedProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.schedule".casefold():
            from .schedule import Schedule

            return Schedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.scheduleChangeRequest".casefold():
            from .schedule_change_request import ScheduleChangeRequest

            return ScheduleChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.schedulingGroup".casefold():
            from .scheduling_group import SchedulingGroup

            return SchedulingGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.schemaExtension".casefold():
            from .schema_extension import SchemaExtension

            return SchemaExtension()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.scopedRoleMembership".casefold():
            from .scoped_role_membership import ScopedRoleMembership

            return ScopedRoleMembership()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.search.acronym".casefold():
            from .search.acronym import Acronym

            return Acronym()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.search.bookmark".casefold():
            from .search.bookmark import Bookmark

            return Bookmark()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.search.qna".casefold():
            from .search.qna import Qna

            return Qna()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.search.searchAnswer".casefold():
            from .search.search_answer import SearchAnswer

            return SearchAnswer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.searchEntity".casefold():
            from .search_entity import SearchEntity

            return SearchEntity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.section".casefold():
            from .section import Section

            return Section()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sectionGroup".casefold():
            from .section_group import SectionGroup

            return SectionGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sectionMap".casefold():
            from .section_map import SectionMap

            return SectionMap()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secureScore".casefold():
            from .secure_score import SecureScore

            return SecureScore()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.secureScoreControlProfile".casefold():
            from .secure_score_control_profile import SecureScoreControlProfile

            return SecureScoreControlProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security".casefold():
            from .security.security import Security

            return Security()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.alert".casefold():
            from .alert import Alert
            from .security.alert import Alert

            return Alert()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.article".casefold():
            from .security.article import Article

            return Article()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.articleIndicator".casefold():
            from .security.article_indicator import ArticleIndicator

            return ArticleIndicator()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.artifact".casefold():
            from .security.artifact import Artifact

            return Artifact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.authorityTemplate".casefold():
            from .security.authority_template import AuthorityTemplate

            return AuthorityTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.case".casefold():
            from .security.case import Case

            return Case()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.caseOperation".casefold():
            from .security.case_operation import CaseOperation

            return CaseOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.casesRoot".casefold():
            from .security.cases_root import CasesRoot

            return CasesRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.categoryTemplate".casefold():
            from .security.category_template import CategoryTemplate

            return CategoryTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.citationTemplate".casefold():
            from .security.citation_template import CitationTemplate

            return CitationTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataSet".casefold():
            from .security.data_set import DataSet

            return DataSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataSource".casefold():
            from .security.data_source import DataSource

            return DataSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dataSourceContainer".casefold():
            from .security.data_source_container import DataSourceContainer

            return DataSourceContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.departmentTemplate".casefold():
            from .security.department_template import DepartmentTemplate

            return DepartmentTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.dispositionReviewStage".casefold():
            from .security.disposition_review_stage import DispositionReviewStage

            return DispositionReviewStage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryAddToReviewSetOperation".casefold():
            from .security.ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation

            return EdiscoveryAddToReviewSetOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryCase".casefold():
            from .security.ediscovery_case import EdiscoveryCase

            return EdiscoveryCase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryCaseMember".casefold():
            from .security.ediscovery_case_member import EdiscoveryCaseMember

            return EdiscoveryCaseMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryCaseSettings".casefold():
            from .security.ediscovery_case_settings import EdiscoveryCaseSettings

            return EdiscoveryCaseSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryCustodian".casefold():
            from .security.ediscovery_custodian import EdiscoveryCustodian

            return EdiscoveryCustodian()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryEstimateOperation".casefold():
            from .security.ediscovery_estimate_operation import EdiscoveryEstimateOperation

            return EdiscoveryEstimateOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryExportOperation".casefold():
            from .security.ediscovery_export_operation import EdiscoveryExportOperation

            return EdiscoveryExportOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryHoldOperation".casefold():
            from .security.ediscovery_hold_operation import EdiscoveryHoldOperation

            return EdiscoveryHoldOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryHoldPolicySyncOperation".casefold():
            from .security.ediscovery_hold_policy_sync_operation import EdiscoveryHoldPolicySyncOperation

            return EdiscoveryHoldPolicySyncOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryIndexOperation".casefold():
            from .security.ediscovery_index_operation import EdiscoveryIndexOperation

            return EdiscoveryIndexOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryNoncustodialDataSource".casefold():
            from .security.ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource

            return EdiscoveryNoncustodialDataSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryPurgeDataOperation".casefold():
            from .security.ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation

            return EdiscoveryPurgeDataOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryReviewSet".casefold():
            from .security.ediscovery_review_set import EdiscoveryReviewSet

            return EdiscoveryReviewSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryReviewSetQuery".casefold():
            from .security.ediscovery_review_set_query import EdiscoveryReviewSetQuery

            return EdiscoveryReviewSetQuery()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryReviewTag".casefold():
            from .security.ediscovery_review_tag import EdiscoveryReviewTag

            return EdiscoveryReviewTag()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoverySearch".casefold():
            from .security.ediscovery_search import EdiscoverySearch

            return EdiscoverySearch()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoverySearchExportOperation".casefold():
            from .security.ediscovery_search_export_operation import EdiscoverySearchExportOperation

            return EdiscoverySearchExportOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ediscoveryTagOperation".casefold():
            from .security.ediscovery_tag_operation import EdiscoveryTagOperation

            return EdiscoveryTagOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.filePlanDescriptor".casefold():
            from .security.file_plan_descriptor import FilePlanDescriptor

            return FilePlanDescriptor()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.filePlanDescriptorTemplate".casefold():
            from .security.file_plan_descriptor_template import FilePlanDescriptorTemplate

            return FilePlanDescriptorTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.filePlanReferenceTemplate".casefold():
            from .security.file_plan_reference_template import FilePlanReferenceTemplate

            return FilePlanReferenceTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.healthIssue".casefold():
            from .security.health_issue import HealthIssue

            return HealthIssue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.host".casefold():
            from .security.host import Host

            return Host()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostComponent".casefold():
            from .security.host_component import HostComponent

            return HostComponent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostCookie".casefold():
            from .security.host_cookie import HostCookie

            return HostCookie()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostname".casefold():
            from .security.hostname import Hostname

            return Hostname()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostPair".casefold():
            from .security.host_pair import HostPair

            return HostPair()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostPort".casefold():
            from .security.host_port import HostPort

            return HostPort()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostReputation".casefold():
            from .security.host_reputation import HostReputation

            return HostReputation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostSslCertificate".casefold():
            from .security.host_ssl_certificate import HostSslCertificate

            return HostSslCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.hostTracker".casefold():
            from .security.host_tracker import HostTracker

            return HostTracker()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.identityAccounts".casefold():
            from .security.identity_accounts import IdentityAccounts

            return IdentityAccounts()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.identityContainer".casefold():
            from .identity_container import IdentityContainer
            from .security.identity_container import IdentityContainer

            return IdentityContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.incident".casefold():
            from .security.incident import Incident

            return Incident()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.indicator".casefold():
            from .security.indicator import Indicator

            return Indicator()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.intelligenceProfile".casefold():
            from .security.intelligence_profile import IntelligenceProfile

            return IntelligenceProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.intelligenceProfileIndicator".casefold():
            from .security.intelligence_profile_indicator import IntelligenceProfileIndicator

            return IntelligenceProfileIndicator()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.ipAddress".casefold():
            from .security.ip_address import IpAddress

            return IpAddress()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.labelsRoot".casefold():
            from .security.labels_root import LabelsRoot

            return LabelsRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.networkAdapter".casefold():
            from .security.network_adapter import NetworkAdapter

            return NetworkAdapter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.passiveDnsRecord".casefold():
            from .security.passive_dns_record import PassiveDnsRecord

            return PassiveDnsRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.retentionEvent".casefold():
            from .security.retention_event import RetentionEvent

            return RetentionEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.retentionEventType".casefold():
            from .security.retention_event_type import RetentionEventType

            return RetentionEventType()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.retentionLabel".casefold():
            from .security.retention_label import RetentionLabel

            return RetentionLabel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.search".casefold():
            from .security.search import Search

            return Search()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sensor".casefold():
            from .security.sensor import Sensor

            return Sensor()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sensorCandidate".casefold():
            from .security.sensor_candidate import SensorCandidate

            return SensorCandidate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sensorCandidateActivationConfiguration".casefold():
            from .security.sensor_candidate_activation_configuration import SensorCandidateActivationConfiguration

            return SensorCandidateActivationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.siteSource".casefold():
            from .security.site_source import SiteSource

            return SiteSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.sslCertificate".casefold():
            from .security.ssl_certificate import SslCertificate

            return SslCertificate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.subcategoryTemplate".casefold():
            from .security.subcategory_template import SubcategoryTemplate

            return SubcategoryTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.subdomain".casefold():
            from .security.subdomain import Subdomain

            return Subdomain()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.tag".casefold():
            from .security.tag import Tag

            return Tag()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.threatIntelligence".casefold():
            from .security.threat_intelligence import ThreatIntelligence

            return ThreatIntelligence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.triggersRoot".casefold():
            from .security.triggers_root import TriggersRoot

            return TriggersRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.triggerTypesRoot".casefold():
            from .security.trigger_types_root import TriggerTypesRoot

            return TriggerTypesRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.unclassifiedArtifact".casefold():
            from .security.unclassified_artifact import UnclassifiedArtifact

            return UnclassifiedArtifact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.unifiedGroupSource".casefold():
            from .security.unified_group_source import UnifiedGroupSource

            return UnifiedGroupSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.user".casefold():
            from .security.user import User
            from .user import User

            return User()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.userSource".casefold():
            from .security.user_source import UserSource

            return UserSource()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vulnerability".casefold():
            from .security.vulnerability import Vulnerability

            return Vulnerability()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.vulnerabilityComponent".casefold():
            from .security.vulnerability_component import VulnerabilityComponent

            return VulnerabilityComponent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.whoisBaseRecord".casefold():
            from .security.whois_base_record import WhoisBaseRecord

            return WhoisBaseRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.whoisHistoryRecord".casefold():
            from .security.whois_history_record import WhoisHistoryRecord

            return WhoisHistoryRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.security.whoisRecord".casefold():
            from .security.whois_record import WhoisRecord

            return WhoisRecord()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.securityReportsRoot".casefold():
            from .security_reports_root import SecurityReportsRoot

            return SecurityReportsRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sendDtmfTonesOperation".casefold():
            from .send_dtmf_tones_operation import SendDtmfTonesOperation

            return SendDtmfTonesOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sensitivityLabel".casefold():
            from .sensitivity_label import SensitivityLabel

            return SensitivityLabel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceAnnouncement".casefold():
            from .service_announcement import ServiceAnnouncement

            return ServiceAnnouncement()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceAnnouncementAttachment".casefold():
            from .service_announcement_attachment import ServiceAnnouncementAttachment

            return ServiceAnnouncementAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceAnnouncementBase".casefold():
            from .service_announcement_base import ServiceAnnouncementBase

            return ServiceAnnouncementBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceApp".casefold():
            from .service_app import ServiceApp

            return ServiceApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceHealth".casefold():
            from .service_health import ServiceHealth

            return ServiceHealth()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceHealthIssue".casefold():
            from .service_health_issue import ServiceHealthIssue

            return ServiceHealthIssue()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.servicePrincipal".casefold():
            from .service_principal import ServicePrincipal

            return ServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.servicePrincipalRiskDetection".casefold():
            from .service_principal_risk_detection import ServicePrincipalRiskDetection

            return ServicePrincipalRiskDetection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceStorageQuotaBreakdown".casefold():
            from .service_storage_quota_breakdown import ServiceStorageQuotaBreakdown

            return ServiceStorageQuotaBreakdown()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.serviceUpdateMessage".casefold():
            from .service_update_message import ServiceUpdateMessage

            return ServiceUpdateMessage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.settingStateDeviceSummary".casefold():
            from .setting_state_device_summary import SettingStateDeviceSummary

            return SettingStateDeviceSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedDriveItem".casefold():
            from .shared_drive_item import SharedDriveItem

            return SharedDriveItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedInsight".casefold():
            from .shared_insight import SharedInsight

            return SharedInsight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedPCConfiguration".casefold():
            from .shared_p_c_configuration import SharedPCConfiguration

            return SharedPCConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharedWithChannelTeamInfo".casefold():
            from .shared_with_channel_team_info import SharedWithChannelTeamInfo

            return SharedWithChannelTeamInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharepoint".casefold():
            from .sharepoint import Sharepoint

            return Sharepoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationEvent".casefold():
            from .share_point_migration_event import SharePointMigrationEvent

            return SharePointMigrationEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationFinishManifestFileUploadEvent".casefold():
            from .share_point_migration_finish_manifest_file_upload_event import SharePointMigrationFinishManifestFileUploadEvent

            return SharePointMigrationFinishManifestFileUploadEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationJob".casefold():
            from .share_point_migration_job import SharePointMigrationJob

            return SharePointMigrationJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationJobCancelledEvent".casefold():
            from .share_point_migration_job_cancelled_event import SharePointMigrationJobCancelledEvent

            return SharePointMigrationJobCancelledEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationJobDeletedEvent".casefold():
            from .share_point_migration_job_deleted_event import SharePointMigrationJobDeletedEvent

            return SharePointMigrationJobDeletedEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationJobErrorEvent".casefold():
            from .share_point_migration_job_error_event import SharePointMigrationJobErrorEvent

            return SharePointMigrationJobErrorEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationJobPostponedEvent".casefold():
            from .share_point_migration_job_postponed_event import SharePointMigrationJobPostponedEvent

            return SharePointMigrationJobPostponedEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationJobProgressEvent".casefold():
            from .share_point_migration_job_progress_event import SharePointMigrationJobProgressEvent

            return SharePointMigrationJobProgressEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationJobQueuedEvent".casefold():
            from .share_point_migration_job_queued_event import SharePointMigrationJobQueuedEvent

            return SharePointMigrationJobQueuedEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointMigrationJobStartEvent".casefold():
            from .share_point_migration_job_start_event import SharePointMigrationJobStartEvent

            return SharePointMigrationJobStartEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointProtectionPolicy".casefold():
            from .share_point_protection_policy import SharePointProtectionPolicy

            return SharePointProtectionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointRestoreSession".casefold():
            from .share_point_restore_session import SharePointRestoreSession

            return SharePointRestoreSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharepointSettings".casefold():
            from .sharepoint_settings import SharepointSettings

            return SharepointSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.shift".casefold():
            from .shift import Shift

            return Shift()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.shiftPreferences".casefold():
            from .shift_preferences import ShiftPreferences

            return ShiftPreferences()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.signIn".casefold():
            from .sign_in import SignIn

            return SignIn()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.simulation".casefold():
            from .simulation import Simulation

            return Simulation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.simulationAutomation".casefold():
            from .simulation_automation import SimulationAutomation

            return SimulationAutomation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.simulationAutomationRun".casefold():
            from .simulation_automation_run import SimulationAutomationRun

            return SimulationAutomationRun()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.singleValueLegacyExtendedProperty".casefold():
            from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

            return SingleValueLegacyExtendedProperty()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.site".casefold():
            from .site import Site

            return Site()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sitePage".casefold():
            from .site_page import SitePage

            return SitePage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.siteProtectionRule".casefold():
            from .site_protection_rule import SiteProtectionRule

            return SiteProtectionRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.siteProtectionUnit".casefold():
            from .site_protection_unit import SiteProtectionUnit

            return SiteProtectionUnit()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.siteProtectionUnitsBulkAdditionJob".casefold():
            from .site_protection_units_bulk_addition_job import SiteProtectionUnitsBulkAdditionJob

            return SiteProtectionUnitsBulkAdditionJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.siteRestoreArtifact".casefold():
            from .site_restore_artifact import SiteRestoreArtifact

            return SiteRestoreArtifact()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.siteRestoreArtifactsBulkAdditionRequest".casefold():
            from .site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest

            return SiteRestoreArtifactsBulkAdditionRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.skypeForBusinessUserConversationMember".casefold():
            from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember

            return SkypeForBusinessUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.skypeUserConversationMember".casefold():
            from .skype_user_conversation_member import SkypeUserConversationMember

            return SkypeUserConversationMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.smsAuthenticationMethodConfiguration".casefold():
            from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration

            return SmsAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.smsAuthenticationMethodTarget".casefold():
            from .sms_authentication_method_target import SmsAuthenticationMethodTarget

            return SmsAuthenticationMethodTarget()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.socialIdentityProvider".casefold():
            from .social_identity_provider import SocialIdentityProvider

            return SocialIdentityProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.softwareOathAuthenticationMethod".casefold():
            from .software_oath_authentication_method import SoftwareOathAuthenticationMethod

            return SoftwareOathAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.softwareOathAuthenticationMethodConfiguration".casefold():
            from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration

            return SoftwareOathAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.softwareUpdateStatusSummary".casefold():
            from .software_update_status_summary import SoftwareUpdateStatusSummary

            return SoftwareUpdateStatusSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.speakerAssignmentSubmission".casefold():
            from .speaker_assignment_submission import SpeakerAssignmentSubmission

            return SpeakerAssignmentSubmission()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.standardWebPart".casefold():
            from .standard_web_part import StandardWebPart

            return StandardWebPart()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.startHoldMusicOperation".casefold():
            from .start_hold_music_operation import StartHoldMusicOperation

            return StartHoldMusicOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.stopHoldMusicOperation".casefold():
            from .stop_hold_music_operation import StopHoldMusicOperation

            return StopHoldMusicOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.storageQuotaBreakdown".casefold():
            from .storage_quota_breakdown import StorageQuotaBreakdown

            return StorageQuotaBreakdown()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.storageSettings".casefold():
            from .storage_settings import StorageSettings

            return StorageSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.stsPolicy".casefold():
            from .sts_policy import StsPolicy

            return StsPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.subjectRightsRequest".casefold():
            from .subject_rights_request import SubjectRightsRequest

            return SubjectRightsRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.subscribedSku".casefold():
            from .subscribed_sku import SubscribedSku

            return SubscribedSku()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.subscribeToToneOperation".casefold():
            from .subscribe_to_tone_operation import SubscribeToToneOperation

            return SubscribeToToneOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.subscription".casefold():
            from .subscription import Subscription

            return Subscription()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.swapShiftsChangeRequest".casefold():
            from .swap_shifts_change_request import SwapShiftsChangeRequest

            return SwapShiftsChangeRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.synchronization".casefold():
            from .synchronization import Synchronization

            return Synchronization()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.synchronizationJob".casefold():
            from .synchronization_job import SynchronizationJob

            return SynchronizationJob()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.synchronizationSchema".casefold():
            from .synchronization_schema import SynchronizationSchema

            return SynchronizationSchema()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.synchronizationTemplate".casefold():
            from .synchronization_template import SynchronizationTemplate

            return SynchronizationTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetDeviceGroup".casefold():
            from .target_device_group import TargetDeviceGroup

            return TargetDeviceGroup()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppConfiguration".casefold():
            from .targeted_managed_app_configuration import TargetedManagedAppConfiguration

            return TargetedManagedAppConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppPolicyAssignment".casefold():
            from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment

            return TargetedManagedAppPolicyAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetedManagedAppProtection".casefold():
            from .targeted_managed_app_protection import TargetedManagedAppProtection

            return TargetedManagedAppProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.taskFileAttachment".casefold():
            from .task_file_attachment import TaskFileAttachment

            return TaskFileAttachment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.team".casefold():
            from .team import Team

            return Team()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamInfo".casefold():
            from .team_info import TeamInfo

            return TeamInfo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAdministration.teamsAdminRoot".casefold():
            from .teams_administration.teams_admin_root import TeamsAdminRoot

            return TeamsAdminRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAdministration.teamsUserConfiguration".casefold():
            from .teams_administration.teams_user_configuration import TeamsUserConfiguration

            return TeamsUserConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsApp".casefold():
            from .teams_app import TeamsApp

            return TeamsApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppDefinition".casefold():
            from .teams_app_definition import TeamsAppDefinition

            return TeamsAppDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppInstallation".casefold():
            from .teams_app_installation import TeamsAppInstallation

            return TeamsAppInstallation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAppSettings".casefold():
            from .teams_app_settings import TeamsAppSettings

            return TeamsAppSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsAsyncOperation".casefold():
            from .teams_async_operation import TeamsAsyncOperation

            return TeamsAsyncOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsTab".casefold():
            from .teams_tab import TeamsTab

            return TeamsTab()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamsTemplate".casefold():
            from .teams_template import TeamsTemplate

            return TeamsTemplate()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamwork".casefold():
            from .teamwork import Teamwork

            return Teamwork()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkBot".casefold():
            from .teamwork_bot import TeamworkBot

            return TeamworkBot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkHostedContent".casefold():
            from .teamwork_hosted_content import TeamworkHostedContent

            return TeamworkHostedContent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkTag".casefold():
            from .teamwork_tag import TeamworkTag

            return TeamworkTag()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkTagMember".casefold():
            from .teamwork_tag_member import TeamworkTagMember

            return TeamworkTagMember()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.temporaryAccessPassAuthenticationMethod".casefold():
            from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod

            return TemporaryAccessPassAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.temporaryAccessPassAuthenticationMethodConfiguration".casefold():
            from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration

            return TemporaryAccessPassAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tenantAppManagementPolicy".casefold():
            from .tenant_app_management_policy import TenantAppManagementPolicy

            return TenantAppManagementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tenantDataSecurityAndGovernance".casefold():
            from .tenant_data_security_and_governance import TenantDataSecurityAndGovernance

            return TenantDataSecurityAndGovernance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tenantProtectionScopeContainer".casefold():
            from .tenant_protection_scope_container import TenantProtectionScopeContainer

            return TenantProtectionScopeContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termsAndConditions".casefold():
            from .terms_and_conditions import TermsAndConditions

            return TermsAndConditions()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termsAndConditionsAcceptanceStatus".casefold():
            from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus

            return TermsAndConditionsAcceptanceStatus()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termsAndConditionsAssignment".casefold():
            from .terms_and_conditions_assignment import TermsAndConditionsAssignment

            return TermsAndConditionsAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termsOfUseContainer".casefold():
            from .terms_of_use_container import TermsOfUseContainer

            return TermsOfUseContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termStore.group".casefold():
            from .group import Group
            from .term_store.group import Group

            return Group()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termStore.relation".casefold():
            from .term_store.relation import Relation

            return Relation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termStore.set".casefold():
            from .term_store.set import Set

            return Set()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termStore.store".casefold():
            from .term_store.store import Store

            return Store()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.termStore.term".casefold():
            from .term_store.term import Term

            return Term()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.textWebPart".casefold():
            from .text_web_part import TextWebPart

            return TextWebPart()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.threatAssessmentRequest".casefold():
            from .threat_assessment_request import ThreatAssessmentRequest

            return ThreatAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.threatAssessmentResult".casefold():
            from .threat_assessment_result import ThreatAssessmentResult

            return ThreatAssessmentResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.thumbnailSet".casefold():
            from .thumbnail_set import ThumbnailSet

            return ThumbnailSet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeCard".casefold():
            from .time_card import TimeCard

            return TimeCard()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOff".casefold():
            from .time_off import TimeOff

            return TimeOff()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOffReason".casefold():
            from .time_off_reason import TimeOffReason

            return TimeOffReason()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.timeOffRequest".casefold():
            from .time_off_request import TimeOffRequest

            return TimeOffRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.todo".casefold():
            from .todo import Todo

            return Todo()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.todoTask".casefold():
            from .todo_task import TodoTask

            return TodoTask()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.todoTaskList".casefold():
            from .todo_task_list import TodoTaskList

            return TodoTaskList()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tokenIssuancePolicy".casefold():
            from .token_issuance_policy import TokenIssuancePolicy

            return TokenIssuancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.tokenLifetimePolicy".casefold():
            from .token_lifetime_policy import TokenLifetimePolicy

            return TokenLifetimePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.training".casefold():
            from .training import Training

            return Training()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.trainingLanguageDetail".casefold():
            from .training_language_detail import TrainingLanguageDetail

            return TrainingLanguageDetail()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.trending".casefold():
            from .trending import Trending

            return Trending()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRbacResourceAction".casefold():
            from .unified_rbac_resource_action import UnifiedRbacResourceAction

            return UnifiedRbacResourceAction()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRbacResourceNamespace".casefold():
            from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace

            return UnifiedRbacResourceNamespace()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignment".casefold():
            from .unified_role_assignment import UnifiedRoleAssignment

            return UnifiedRoleAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignmentSchedule".casefold():
            from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule

            return UnifiedRoleAssignmentSchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignmentScheduleInstance".casefold():
            from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance

            return UnifiedRoleAssignmentScheduleInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleAssignmentScheduleRequest".casefold():
            from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest

            return UnifiedRoleAssignmentScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleDefinition".casefold():
            from .unified_role_definition import UnifiedRoleDefinition

            return UnifiedRoleDefinition()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleEligibilitySchedule".casefold():
            from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule

            return UnifiedRoleEligibilitySchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleEligibilityScheduleInstance".casefold():
            from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance

            return UnifiedRoleEligibilityScheduleInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleEligibilityScheduleRequest".casefold():
            from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest

            return UnifiedRoleEligibilityScheduleRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicy".casefold():
            from .unified_role_management_policy import UnifiedRoleManagementPolicy

            return UnifiedRoleManagementPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyApprovalRule".casefold():
            from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule

            return UnifiedRoleManagementPolicyApprovalRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyAssignment".casefold():
            from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment

            return UnifiedRoleManagementPolicyAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyAuthenticationContextRule".casefold():
            from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule

            return UnifiedRoleManagementPolicyAuthenticationContextRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyEnablementRule".casefold():
            from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule

            return UnifiedRoleManagementPolicyEnablementRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyExpirationRule".casefold():
            from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule

            return UnifiedRoleManagementPolicyExpirationRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyNotificationRule".casefold():
            from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule

            return UnifiedRoleManagementPolicyNotificationRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleManagementPolicyRule".casefold():
            from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule

            return UnifiedRoleManagementPolicyRule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleScheduleBase".casefold():
            from .unified_role_schedule_base import UnifiedRoleScheduleBase

            return UnifiedRoleScheduleBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedRoleScheduleInstanceBase".casefold():
            from .unified_role_schedule_instance_base import UnifiedRoleScheduleInstanceBase

            return UnifiedRoleScheduleInstanceBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unifiedStorageQuota".casefold():
            from .unified_storage_quota import UnifiedStorageQuota

            return UnifiedStorageQuota()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unitMap".casefold():
            from .unit_map import UnitMap

            return UnitMap()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.unmuteParticipantOperation".casefold():
            from .unmute_participant_operation import UnmuteParticipantOperation

            return UnmuteParticipantOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.updateRecordingStatusOperation".casefold():
            from .update_recording_status_operation import UpdateRecordingStatusOperation

            return UpdateRecordingStatusOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.urlAssessmentRequest".casefold():
            from .url_assessment_request import UrlAssessmentRequest

            return UrlAssessmentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.usageRightsIncluded".casefold():
            from .usage_rights_included import UsageRightsIncluded

            return UsageRightsIncluded()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.usedInsight".casefold():
            from .used_insight import UsedInsight

            return UsedInsight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.user".casefold():
            from .security.user import User
            from .user import User

            return User()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userActivity".casefold():
            from .user_activity import UserActivity

            return UserActivity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userConsentRequest".casefold():
            from .user_consent_request import UserConsentRequest

            return UserConsentRequest()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userDataSecurityAndGovernance".casefold():
            from .user_data_security_and_governance import UserDataSecurityAndGovernance

            return UserDataSecurityAndGovernance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthApplicationPerformance".casefold():
            from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformance

            return UserExperienceAnalyticsAppHealthApplicationPerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails".casefold():
            from .user_experience_analytics_app_health_app_performance_by_app_version_details import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails

            return UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId".casefold():
            from .user_experience_analytics_app_health_app_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId

            return UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthAppPerformanceByOSVersion".casefold():
            from .user_experience_analytics_app_health_app_performance_by_o_s_version import UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion

            return UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthDeviceModelPerformance".casefold():
            from .user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformance

            return UserExperienceAnalyticsAppHealthDeviceModelPerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthDevicePerformance".casefold():
            from .user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformance

            return UserExperienceAnalyticsAppHealthDevicePerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthDevicePerformanceDetails".casefold():
            from .user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetails

            return UserExperienceAnalyticsAppHealthDevicePerformanceDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsAppHealthOSVersionPerformance".casefold():
            from .user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformance

            return UserExperienceAnalyticsAppHealthOSVersionPerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsBaseline".casefold():
            from .user_experience_analytics_baseline import UserExperienceAnalyticsBaseline

            return UserExperienceAnalyticsBaseline()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsCategory".casefold():
            from .user_experience_analytics_category import UserExperienceAnalyticsCategory

            return UserExperienceAnalyticsCategory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsDevicePerformance".casefold():
            from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance

            return UserExperienceAnalyticsDevicePerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsDeviceScores".casefold():
            from .user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScores

            return UserExperienceAnalyticsDeviceScores()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsDeviceStartupHistory".casefold():
            from .user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistory

            return UserExperienceAnalyticsDeviceStartupHistory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsDeviceStartupProcess".casefold():
            from .user_experience_analytics_device_startup_process import UserExperienceAnalyticsDeviceStartupProcess

            return UserExperienceAnalyticsDeviceStartupProcess()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsDeviceStartupProcessPerformance".casefold():
            from .user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformance

            return UserExperienceAnalyticsDeviceStartupProcessPerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsMetric".casefold():
            from .user_experience_analytics_metric import UserExperienceAnalyticsMetric

            return UserExperienceAnalyticsMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsMetricHistory".casefold():
            from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory

            return UserExperienceAnalyticsMetricHistory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsModelScores".casefold():
            from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores

            return UserExperienceAnalyticsModelScores()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsOverview".casefold():
            from .user_experience_analytics_overview import UserExperienceAnalyticsOverview

            return UserExperienceAnalyticsOverview()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsScoreHistory".casefold():
            from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory

            return UserExperienceAnalyticsScoreHistory()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereDevice".casefold():
            from .user_experience_analytics_work_from_anywhere_device import UserExperienceAnalyticsWorkFromAnywhereDevice

            return UserExperienceAnalyticsWorkFromAnywhereDevice()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric".casefold():
            from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric

            return UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereMetric".casefold():
            from .user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric

            return UserExperienceAnalyticsWorkFromAnywhereMetric()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userExperienceAnalyticsWorkFromAnywhereModelPerformance".casefold():
            from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance

            return UserExperienceAnalyticsWorkFromAnywhereModelPerformance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userFlowLanguageConfiguration".casefold():
            from .user_flow_language_configuration import UserFlowLanguageConfiguration

            return UserFlowLanguageConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userFlowLanguagePage".casefold():
            from .user_flow_language_page import UserFlowLanguagePage

            return UserFlowLanguagePage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userInsightsSettings".casefold():
            from .user_insights_settings import UserInsightsSettings

            return UserInsightsSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userInstallStateSummary".casefold():
            from .user_install_state_summary import UserInstallStateSummary

            return UserInstallStateSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userProtectionScopeContainer".casefold():
            from .user_protection_scope_container import UserProtectionScopeContainer

            return UserProtectionScopeContainer()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userRegistrationDetails".casefold():
            from .user_registration_details import UserRegistrationDetails

            return UserRegistrationDetails()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userScopeTeamsAppInstallation".casefold():
            from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation

            return UserScopeTeamsAppInstallation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userSettings".casefold():
            from .user_settings import UserSettings

            return UserSettings()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userSignInInsight".casefold():
            from .user_sign_in_insight import UserSignInInsight

            return UserSignInInsight()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userSolutionRoot".casefold():
            from .user_solution_root import UserSolutionRoot

            return UserSolutionRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userStorage".casefold():
            from .user_storage import UserStorage

            return UserStorage()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userTeamwork".casefold():
            from .user_teamwork import UserTeamwork

            return UserTeamwork()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.verticalSection".casefold():
            from .vertical_section import VerticalSection

            return VerticalSection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEndpoint".casefold():
            from .virtual_endpoint import VirtualEndpoint

            return VirtualEndpoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEvent".casefold():
            from .virtual_event import VirtualEvent

            return VirtualEvent()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventPresenter".casefold():
            from .virtual_event_presenter import VirtualEventPresenter

            return VirtualEventPresenter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventRegistration".casefold():
            from .virtual_event_registration import VirtualEventRegistration

            return VirtualEventRegistration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventRegistrationConfiguration".casefold():
            from .virtual_event_registration_configuration import VirtualEventRegistrationConfiguration

            return VirtualEventRegistrationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventRegistrationCustomQuestion".casefold():
            from .virtual_event_registration_custom_question import VirtualEventRegistrationCustomQuestion

            return VirtualEventRegistrationCustomQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventRegistrationPredefinedQuestion".casefold():
            from .virtual_event_registration_predefined_question import VirtualEventRegistrationPredefinedQuestion

            return VirtualEventRegistrationPredefinedQuestion()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventRegistrationQuestionBase".casefold():
            from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase

            return VirtualEventRegistrationQuestionBase()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventSession".casefold():
            from .virtual_event_session import VirtualEventSession

            return VirtualEventSession()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventsRoot".casefold():
            from .virtual_events_root import VirtualEventsRoot

            return VirtualEventsRoot()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventTownhall".casefold():
            from .virtual_event_townhall import VirtualEventTownhall

            return VirtualEventTownhall()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventWebinar".casefold():
            from .virtual_event_webinar import VirtualEventWebinar

            return VirtualEventWebinar()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.virtualEventWebinarRegistrationConfiguration".casefold():
            from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration

            return VirtualEventWebinarRegistrationConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.voiceAuthenticationMethodConfiguration".casefold():
            from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration

            return VoiceAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.vppToken".casefold():
            from .vpp_token import VppToken

            return VppToken()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.webApp".casefold():
            from .web_app import WebApp

            return WebApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.webApplicationFirewallProvider".casefold():
            from .web_application_firewall_provider import WebApplicationFirewallProvider

            return WebApplicationFirewallProvider()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.webApplicationFirewallVerificationModel".casefold():
            from .web_application_firewall_verification_model import WebApplicationFirewallVerificationModel

            return WebApplicationFirewallVerificationModel()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.webPart".casefold():
            from .web_part import WebPart

            return WebPart()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.whatIfAnalysisResult".casefold():
            from .what_if_analysis_result import WhatIfAnalysisResult

            return WhatIfAnalysisResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.win32LobApp".casefold():
            from .win32_lob_app import Win32LobApp

            return Win32LobApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CompliancePolicy".casefold():
            from .windows10_compliance_policy import Windows10CompliancePolicy

            return Windows10CompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10CustomConfiguration".casefold():
            from .windows10_custom_configuration import Windows10CustomConfiguration

            return Windows10CustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EndpointProtectionConfiguration".casefold():
            from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration

            return Windows10EndpointProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EnrollmentCompletionPageConfiguration".casefold():
            from .windows10_enrollment_completion_page_configuration import Windows10EnrollmentCompletionPageConfiguration

            return Windows10EnrollmentCompletionPageConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration".casefold():
            from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration

            return Windows10EnterpriseModernAppManagementConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10GeneralConfiguration".casefold():
            from .windows10_general_configuration import Windows10GeneralConfiguration

            return Windows10GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10MobileCompliancePolicy".casefold():
            from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy

            return Windows10MobileCompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10SecureAssessmentConfiguration".casefold():
            from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration

            return Windows10SecureAssessmentConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows10TeamGeneralConfiguration".casefold():
            from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration

            return Windows10TeamGeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81CompliancePolicy".casefold():
            from .windows81_compliance_policy import Windows81CompliancePolicy

            return Windows81CompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windows81GeneralConfiguration".casefold():
            from .windows81_general_configuration import Windows81GeneralConfiguration

            return Windows81GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAppX".casefold():
            from .windows_app_x import WindowsAppX

            return WindowsAppX()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAutopilotDeploymentProfile".casefold():
            from .windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile

            return WindowsAutopilotDeploymentProfile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAutopilotDeploymentProfileAssignment".casefold():
            from .windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment

            return WindowsAutopilotDeploymentProfileAssignment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsAutopilotDeviceIdentity".casefold():
            from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity

            return WindowsAutopilotDeviceIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration".casefold():
            from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration

            return WindowsDefenderAdvancedThreatProtectionConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsDeviceMalwareState".casefold():
            from .windows_device_malware_state import WindowsDeviceMalwareState

            return WindowsDeviceMalwareState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsHelloForBusinessAuthenticationMethod".casefold():
            from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod

            return WindowsHelloForBusinessAuthenticationMethod()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtection".casefold():
            from .windows_information_protection import WindowsInformationProtection

            return WindowsInformationProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionAppLearningSummary".casefold():
            from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary

            return WindowsInformationProtectionAppLearningSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionAppLockerFile".casefold():
            from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile

            return WindowsInformationProtectionAppLockerFile()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionNetworkLearningSummary".casefold():
            from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary

            return WindowsInformationProtectionNetworkLearningSummary()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsInformationProtectionPolicy".casefold():
            from .windows_information_protection_policy import WindowsInformationProtectionPolicy

            return WindowsInformationProtectionPolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsMalwareInformation".casefold():
            from .windows_malware_information import WindowsMalwareInformation

            return WindowsMalwareInformation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsMicrosoftEdgeApp".casefold():
            from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp

            return WindowsMicrosoftEdgeApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsMobileMSI".casefold():
            from .windows_mobile_m_s_i import WindowsMobileMSI

            return WindowsMobileMSI()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81CompliancePolicy".casefold():
            from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy

            return WindowsPhone81CompliancePolicy()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81CustomConfiguration".casefold():
            from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration

            return WindowsPhone81CustomConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsPhone81GeneralConfiguration".casefold():
            from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration

            return WindowsPhone81GeneralConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsProtectionState".casefold():
            from .windows_protection_state import WindowsProtectionState

            return WindowsProtectionState()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsSetting".casefold():
            from .windows_setting import WindowsSetting

            return WindowsSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsSettingInstance".casefold():
            from .windows_setting_instance import WindowsSettingInstance

            return WindowsSettingInstance()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUniversalAppX".casefold():
            from .windows_universal_app_x import WindowsUniversalAppX

            return WindowsUniversalAppX()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUniversalAppXContainedApp".casefold():
            from .windows_universal_app_x_contained_app import WindowsUniversalAppXContainedApp

            return WindowsUniversalAppXContainedApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsUpdateForBusinessConfiguration".casefold():
            from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration

            return WindowsUpdateForBusinessConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.windowsWebApp".casefold():
            from .windows_web_app import WindowsWebApp

            return WindowsWebApp()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbook".casefold():
            from .workbook import Workbook

            return Workbook()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookApplication".casefold():
            from .workbook_application import WorkbookApplication

            return WorkbookApplication()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChart".casefold():
            from .workbook_chart import WorkbookChart

            return WorkbookChart()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAreaFormat".casefold():
            from .workbook_chart_area_format import WorkbookChartAreaFormat

            return WorkbookChartAreaFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAxes".casefold():
            from .workbook_chart_axes import WorkbookChartAxes

            return WorkbookChartAxes()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAxis".casefold():
            from .workbook_chart_axis import WorkbookChartAxis

            return WorkbookChartAxis()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAxisFormat".casefold():
            from .workbook_chart_axis_format import WorkbookChartAxisFormat

            return WorkbookChartAxisFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAxisTitle".casefold():
            from .workbook_chart_axis_title import WorkbookChartAxisTitle

            return WorkbookChartAxisTitle()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartAxisTitleFormat".casefold():
            from .workbook_chart_axis_title_format import WorkbookChartAxisTitleFormat

            return WorkbookChartAxisTitleFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartDataLabelFormat".casefold():
            from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat

            return WorkbookChartDataLabelFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartDataLabels".casefold():
            from .workbook_chart_data_labels import WorkbookChartDataLabels

            return WorkbookChartDataLabels()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartFill".casefold():
            from .workbook_chart_fill import WorkbookChartFill

            return WorkbookChartFill()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartFont".casefold():
            from .workbook_chart_font import WorkbookChartFont

            return WorkbookChartFont()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartGridlines".casefold():
            from .workbook_chart_gridlines import WorkbookChartGridlines

            return WorkbookChartGridlines()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartGridlinesFormat".casefold():
            from .workbook_chart_gridlines_format import WorkbookChartGridlinesFormat

            return WorkbookChartGridlinesFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartLegend".casefold():
            from .workbook_chart_legend import WorkbookChartLegend

            return WorkbookChartLegend()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartLegendFormat".casefold():
            from .workbook_chart_legend_format import WorkbookChartLegendFormat

            return WorkbookChartLegendFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartLineFormat".casefold():
            from .workbook_chart_line_format import WorkbookChartLineFormat

            return WorkbookChartLineFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartPoint".casefold():
            from .workbook_chart_point import WorkbookChartPoint

            return WorkbookChartPoint()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartPointFormat".casefold():
            from .workbook_chart_point_format import WorkbookChartPointFormat

            return WorkbookChartPointFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartSeries".casefold():
            from .workbook_chart_series import WorkbookChartSeries

            return WorkbookChartSeries()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartSeriesFormat".casefold():
            from .workbook_chart_series_format import WorkbookChartSeriesFormat

            return WorkbookChartSeriesFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartTitle".casefold():
            from .workbook_chart_title import WorkbookChartTitle

            return WorkbookChartTitle()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookChartTitleFormat".casefold():
            from .workbook_chart_title_format import WorkbookChartTitleFormat

            return WorkbookChartTitleFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookComment".casefold():
            from .workbook_comment import WorkbookComment

            return WorkbookComment()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookCommentReply".casefold():
            from .workbook_comment_reply import WorkbookCommentReply

            return WorkbookCommentReply()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookFilter".casefold():
            from .workbook_filter import WorkbookFilter

            return WorkbookFilter()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookFormatProtection".casefold():
            from .workbook_format_protection import WorkbookFormatProtection

            return WorkbookFormatProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookFunctionResult".casefold():
            from .workbook_function_result import WorkbookFunctionResult

            return WorkbookFunctionResult()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookFunctions".casefold():
            from .workbook_functions import WorkbookFunctions

            return WorkbookFunctions()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookNamedItem".casefold():
            from .workbook_named_item import WorkbookNamedItem

            return WorkbookNamedItem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookOperation".casefold():
            from .workbook_operation import WorkbookOperation

            return WorkbookOperation()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookPivotTable".casefold():
            from .workbook_pivot_table import WorkbookPivotTable

            return WorkbookPivotTable()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRange".casefold():
            from .workbook_range import WorkbookRange

            return WorkbookRange()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeBorder".casefold():
            from .workbook_range_border import WorkbookRangeBorder

            return WorkbookRangeBorder()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeFill".casefold():
            from .workbook_range_fill import WorkbookRangeFill

            return WorkbookRangeFill()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeFont".casefold():
            from .workbook_range_font import WorkbookRangeFont

            return WorkbookRangeFont()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeFormat".casefold():
            from .workbook_range_format import WorkbookRangeFormat

            return WorkbookRangeFormat()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeSort".casefold():
            from .workbook_range_sort import WorkbookRangeSort

            return WorkbookRangeSort()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookRangeView".casefold():
            from .workbook_range_view import WorkbookRangeView

            return WorkbookRangeView()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookTable".casefold():
            from .workbook_table import WorkbookTable

            return WorkbookTable()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookTableColumn".casefold():
            from .workbook_table_column import WorkbookTableColumn

            return WorkbookTableColumn()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookTableRow".casefold():
            from .workbook_table_row import WorkbookTableRow

            return WorkbookTableRow()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookTableSort".casefold():
            from .workbook_table_sort import WorkbookTableSort

            return WorkbookTableSort()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookWorksheet".casefold():
            from .workbook_worksheet import WorkbookWorksheet

            return WorkbookWorksheet()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workbookWorksheetProtection".casefold():
            from .workbook_worksheet_protection import WorkbookWorksheetProtection

            return WorkbookWorksheetProtection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workforceIntegration".casefold():
            from .workforce_integration import WorkforceIntegration

            return WorkforceIntegration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workHoursAndLocationsSetting".casefold():
            from .work_hours_and_locations_setting import WorkHoursAndLocationsSetting

            return WorkHoursAndLocationsSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workingTimeSchedule".casefold():
            from .working_time_schedule import WorkingTimeSchedule

            return WorkingTimeSchedule()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workPlanOccurrence".casefold():
            from .work_plan_occurrence import WorkPlanOccurrence

            return WorkPlanOccurrence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workPlanRecurrence".casefold():
            from .work_plan_recurrence import WorkPlanRecurrence

            return WorkPlanRecurrence()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.workspace".casefold():
            from .workspace import Workspace

            return Workspace()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.x509CertificateAuthenticationMethodConfiguration".casefold():
            from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration

            return X509CertificateAuthenticationMethodConfiguration()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.x509CertificateCombinationConfiguration".casefold():
            from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration

            return X509CertificateCombinationConfiguration()
        return Entity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .aad_user_conversation_member import AadUserConversationMember
        from .access_package import AccessPackage
        from .access_package_assignment import AccessPackageAssignment
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_request import AccessPackageAssignmentRequest
        from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
        from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
        from .access_package_question import AccessPackageQuestion
        from .access_package_resource import AccessPackageResource
        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_request import AccessPackageResourceRequest
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_role_scope import AccessPackageResourceRoleScope
        from .access_package_resource_scope import AccessPackageResourceScope
        from .access_package_subject import AccessPackageSubject
        from .access_package_text_input_question import AccessPackageTextInputQuestion
        from .access_review_history_definition import AccessReviewHistoryDefinition
        from .access_review_history_instance import AccessReviewHistoryInstance
        from .access_review_instance import AccessReviewInstance
        from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
        from .access_review_reviewer import AccessReviewReviewer
        from .access_review_schedule_definition import AccessReviewScheduleDefinition
        from .access_review_set import AccessReviewSet
        from .access_review_stage import AccessReviewStage
        from .activities_container import ActivitiesContainer
        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .activity_history_item import ActivityHistoryItem
        from .add_large_gallery_view_operation import AddLargeGalleryViewOperation
        from .adhoc_call import AdhocCall
        from .administrative_unit import AdministrativeUnit
        from .admin_consent_request_policy import AdminConsentRequestPolicy
        from .admin_microsoft365_apps import AdminMicrosoft365Apps
        from .admin_report_settings import AdminReportSettings
        from .agreement import Agreement
        from .agreement_acceptance import AgreementAcceptance
        from .agreement_file import AgreementFile
        from .agreement_file_localization import AgreementFileLocalization
        from .agreement_file_properties import AgreementFileProperties
        from .agreement_file_version import AgreementFileVersion
        from .ai_interaction import AiInteraction
        from .ai_interaction_history import AiInteractionHistory
        from .ai_online_meeting import AiOnlineMeeting
        from .ai_user import AiUser
        from .akamai_web_application_firewall_provider import AkamaiWebApplicationFirewallProvider
        from .alert import Alert
        from .allowed_value import AllowedValue
        from .android_compliance_policy import AndroidCompliancePolicy
        from .android_custom_configuration import AndroidCustomConfiguration
        from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
        from .android_lob_app import AndroidLobApp
        from .android_managed_app_protection import AndroidManagedAppProtection
        from .android_managed_app_registration import AndroidManagedAppRegistration
        from .android_store_app import AndroidStoreApp
        from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy
        from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
        from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
        from .anonymous_guest_conversation_member import AnonymousGuestConversationMember
        from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
        from .apple_managed_identity_provider import AppleManagedIdentityProvider
        from .apple_push_notification_certificate import ApplePushNotificationCertificate
        from .application import Application
        from .application_template import ApplicationTemplate
        from .approval import Approval
        from .approval_stage import ApprovalStage
        from .app_catalogs import AppCatalogs
        from .app_consent_approval_route import AppConsentApprovalRoute
        from .app_consent_request import AppConsentRequest
        from .app_log_collection_request import AppLogCollectionRequest
        from .app_management_policy import AppManagementPolicy
        from .app_role_assignment import AppRoleAssignment
        from .app_scope import AppScope
        from .arkose_fraud_protection_provider import ArkoseFraudProtectionProvider
        from .associated_team_info import AssociatedTeamInfo
        from .attachment import Attachment
        from .attachment_base import AttachmentBase
        from .attachment_session import AttachmentSession
        from .attack_simulation_operation import AttackSimulationOperation
        from .attack_simulation_root import AttackSimulationRoot
        from .attendance_record import AttendanceRecord
        from .attribute_mapping_function_schema import AttributeMappingFunctionSchema
        from .attribute_set import AttributeSet
        from .audio_routing_group import AudioRoutingGroup
        from .audit_event import AuditEvent
        from .audit_log_root import AuditLogRoot
        from .authentication import Authentication
        from .authentication_combination_configuration import AuthenticationCombinationConfiguration
        from .authentication_context_class_reference import AuthenticationContextClassReference
        from .authentication_events_flow import AuthenticationEventsFlow
        from .authentication_event_listener import AuthenticationEventListener
        from .authentication_flows_policy import AuthenticationFlowsPolicy
        from .authentication_method import AuthenticationMethod
        from .authentication_methods_policy import AuthenticationMethodsPolicy
        from .authentication_methods_root import AuthenticationMethodsRoot
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_mode_detail import AuthenticationMethodModeDetail
        from .authentication_method_target import AuthenticationMethodTarget
        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .authentication_strength_root import AuthenticationStrengthRoot
        from .authored_note import AuthoredNote
        from .authorization_policy import AuthorizationPolicy
        from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember
        from .b2x_identity_user_flow import B2xIdentityUserFlow
        from .backup_restore_root import BackupRestoreRoot
        from .base_item import BaseItem
        from .base_item_version import BaseItemVersion
        from .base_map_feature import BaseMapFeature
        from .base_site_page import BaseSitePage
        from .bitlocker import Bitlocker
        from .bitlocker_recovery_key import BitlockerRecoveryKey
        from .booking_appointment import BookingAppointment
        from .booking_business import BookingBusiness
        from .booking_currency import BookingCurrency
        from .booking_customer import BookingCustomer
        from .booking_customer_base import BookingCustomerBase
        from .booking_custom_question import BookingCustomQuestion
        from .booking_service import BookingService
        from .booking_staff_member import BookingStaffMember
        from .booking_staff_member_base import BookingStaffMemberBase
        from .browser_shared_cookie import BrowserSharedCookie
        from .browser_site import BrowserSite
        from .browser_site_list import BrowserSiteList
        from .building import Building
        from .building_map import BuildingMap
        from .built_in_identity_provider import BuiltInIdentityProvider
        from .bulk_upload import BulkUpload
        from .calendar import Calendar
        from .calendar_group import CalendarGroup
        from .calendar_permission import CalendarPermission
        from .calendar_sharing_message import CalendarSharingMessage
        from .call import Call
        from .call_ai_insight import CallAiInsight
        from .call_event import CallEvent
        from .call_recording import CallRecording
        from .call_records.call_record import CallRecord
        from .call_records.organizer import Organizer
        from .call_records.participant import Participant
        from .call_records.participant_base import ParticipantBase
        from .call_records.segment import Segment
        from .call_records.session import Session
        from .call_transcript import CallTranscript
        from .cancel_media_processing_operation import CancelMediaProcessingOperation
        from .canvas_layout import CanvasLayout
        from .certificate_authority_detail import CertificateAuthorityDetail
        from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration
        from .certificate_based_auth_pki import CertificateBasedAuthPki
        from .change_tracked_entity import ChangeTrackedEntity
        from .channel import Channel
        from .chat import Chat
        from .chat_message import ChatMessage
        from .chat_message_hosted_content import ChatMessageHostedContent
        from .chat_message_info import ChatMessageInfo
        from .checklist_item import ChecklistItem
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .cloud_clipboard_item import CloudClipboardItem
        from .cloud_clipboard_root import CloudClipboardRoot
        from .cloud_flare_web_application_firewall_provider import CloudFlareWebApplicationFirewallProvider
        from .cloud_pc_audit_event import CloudPcAuditEvent
        from .cloud_pc_device_image import CloudPcDeviceImage
        from .cloud_pc_gallery_image import CloudPcGalleryImage
        from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
        from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
        from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment
        from .cloud_pc_report import CloudPcReport
        from .cloud_pc_user_setting import CloudPcUserSetting
        from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment
        from .cloud_p_c import CloudPC
        from .column_definition import ColumnDefinition
        from .column_link import ColumnLink
        from .comms_operation import CommsOperation
        from .community import Community
        from .company_subscription import CompanySubscription
        from .compliance_management_partner import ComplianceManagementPartner
        from .conditional_access_policy import ConditionalAccessPolicy
        from .conditional_access_root import ConditionalAccessRoot
        from .conditional_access_template import ConditionalAccessTemplate
        from .connected_organization import ConnectedOrganization
        from .contact import Contact
        from .contact_folder import ContactFolder
        from .content_activity import ContentActivity
        from .content_sharing_session import ContentSharingSession
        from .content_type import ContentType
        from .contract import Contract
        from .conversation import Conversation
        from .conversation_member import ConversationMember
        from .conversation_thread import ConversationThread
        from .copilot_admin import CopilotAdmin
        from .copilot_admin_limited_mode import CopilotAdminLimitedMode
        from .copilot_admin_setting import CopilotAdminSetting
        from .copilot_report_root import CopilotReportRoot
        from .country_named_location import CountryNamedLocation
        from .cross_tenant_access_policy import CrossTenantAccessPolicy
        from .cross_tenant_access_policy_configuration_default import CrossTenantAccessPolicyConfigurationDefault
        from .custom_authentication_extension import CustomAuthenticationExtension
        from .custom_callout_extension import CustomCalloutExtension
        from .custom_extension_stage_setting import CustomExtensionStageSetting
        from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
        from .data_policy_operation import DataPolicyOperation
        from .data_security_and_governance import DataSecurityAndGovernance
        from .day_note import DayNote
        from .default_managed_app_protection import DefaultManagedAppProtection
        from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment
        from .delegated_admin_customer import DelegatedAdminCustomer
        from .delegated_admin_relationship import DelegatedAdminRelationship
        from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation
        from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest
        from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail
        from .delegated_permission_classification import DelegatedPermissionClassification
        from .deleted_chat import DeletedChat
        from .deleted_item_container import DeletedItemContainer
        from .deleted_team import DeletedTeam
        from .delta_participants import DeltaParticipants
        from .desk import Desk
        from .detected_app import DetectedApp
        from .device import Device
        from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
        from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition
        from .device_app_management import DeviceAppManagement
        from .device_category import DeviceCategory
        from .device_compliance_action_item import DeviceComplianceActionItem
        from .device_compliance_device_overview import DeviceComplianceDeviceOverview
        from .device_compliance_device_status import DeviceComplianceDeviceStatus
        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
        from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
        from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
        from .device_compliance_policy_state import DeviceCompliancePolicyState
        from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
        from .device_compliance_setting_state import DeviceComplianceSettingState
        from .device_compliance_user_overview import DeviceComplianceUserOverview
        from .device_compliance_user_status import DeviceComplianceUserStatus
        from .device_configuration import DeviceConfiguration
        from .device_configuration_assignment import DeviceConfigurationAssignment
        from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
        from .device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
        from .device_configuration_device_status import DeviceConfigurationDeviceStatus
        from .device_configuration_state import DeviceConfigurationState
        from .device_configuration_user_overview import DeviceConfigurationUserOverview
        from .device_configuration_user_status import DeviceConfigurationUserStatus
        from .device_enrollment_configuration import DeviceEnrollmentConfiguration
        from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration
        from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration
        from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration
        from .device_install_state import DeviceInstallState
        from .device_local_credential_info import DeviceLocalCredentialInfo
        from .device_log_collection_response import DeviceLogCollectionResponse
        from .device_management import DeviceManagement
        from .device_management_cached_report_configuration import DeviceManagementCachedReportConfiguration
        from .device_management_exchange_connector import DeviceManagementExchangeConnector
        from .device_management_export_job import DeviceManagementExportJob
        from .device_management_partner import DeviceManagementPartner
        from .device_management_reports import DeviceManagementReports
        from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
        from .device_registration_policy import DeviceRegistrationPolicy
        from .directory import Directory
        from .directory_audit import DirectoryAudit
        from .directory_definition import DirectoryDefinition
        from .directory_object import DirectoryObject
        from .directory_object_partner_reference import DirectoryObjectPartnerReference
        from .directory_role import DirectoryRole
        from .directory_role_template import DirectoryRoleTemplate
        from .document_set_version import DocumentSetVersion
        from .domain import Domain
        from .domain_dns_cname_record import DomainDnsCnameRecord
        from .domain_dns_mx_record import DomainDnsMxRecord
        from .domain_dns_record import DomainDnsRecord
        from .domain_dns_srv_record import DomainDnsSrvRecord
        from .domain_dns_txt_record import DomainDnsTxtRecord
        from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
        from .drive import Drive
        from .drive_item import DriveItem
        from .drive_item_version import DriveItemVersion
        from .drive_protection_rule import DriveProtectionRule
        from .drive_protection_unit import DriveProtectionUnit
        from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob
        from .drive_restore_artifact import DriveRestoreArtifact
        from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest
        from .edge import Edge
        from .edition_upgrade_configuration import EditionUpgradeConfiguration
        from .education_assignment import EducationAssignment
        from .education_assignment_defaults import EducationAssignmentDefaults
        from .education_assignment_resource import EducationAssignmentResource
        from .education_assignment_settings import EducationAssignmentSettings
        from .education_category import EducationCategory
        from .education_class import EducationClass
        from .education_feedback_outcome import EducationFeedbackOutcome
        from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome
        from .education_grading_category import EducationGradingCategory
        from .education_grading_scheme import EducationGradingScheme
        from .education_module import EducationModule
        from .education_module_resource import EducationModuleResource
        from .education_organization import EducationOrganization
        from .education_outcome import EducationOutcome
        from .education_points_outcome import EducationPointsOutcome
        from .education_rubric import EducationRubric
        from .education_rubric_outcome import EducationRubricOutcome
        from .education_school import EducationSchool
        from .education_submission import EducationSubmission
        from .education_submission_resource import EducationSubmissionResource
        from .education_user import EducationUser
        from .email_authentication_method import EmailAuthenticationMethod
        from .email_authentication_method_configuration import EmailAuthenticationMethodConfiguration
        from .email_file_assessment_request import EmailFileAssessmentRequest
        from .emergency_call_event import EmergencyCallEvent
        from .employee_experience_user import EmployeeExperienceUser
        from .endpoint import Endpoint
        from .end_user_notification import EndUserNotification
        from .end_user_notification_detail import EndUserNotificationDetail
        from .engagement_async_operation import EngagementAsyncOperation
        from .engagement_conversation import EngagementConversation
        from .engagement_conversation_discussion_message import EngagementConversationDiscussionMessage
        from .engagement_conversation_message import EngagementConversationMessage
        from .engagement_conversation_message_reaction import EngagementConversationMessageReaction
        from .engagement_conversation_question_message import EngagementConversationQuestionMessage
        from .engagement_conversation_system_message import EngagementConversationSystemMessage
        from .engagement_role import EngagementRole
        from .engagement_role_member import EngagementRoleMember
        from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
        from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
        from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate
        from .entitlement_management import EntitlementManagement
        from .entitlement_management_settings import EntitlementManagementSettings
        from .event import Event
        from .event_message import EventMessage
        from .event_message_request import EventMessageRequest
        from .event_message_response import EventMessageResponse
        from .exchange_protection_policy import ExchangeProtectionPolicy
        from .exchange_restore_session import ExchangeRestoreSession
        from .extension import Extension
        from .extension_property import ExtensionProperty
        from .external_connectors.connection_operation import ConnectionOperation
        from .external_connectors.external_activity import ExternalActivity
        from .external_connectors.external_activity_result import ExternalActivityResult
        from .external_connectors.external_connection import ExternalConnection
        from .external_connectors.external_group import ExternalGroup
        from .external_connectors.external_item import ExternalItem
        from .external_connectors.identity import Identity
        from .external_connectors.schema import Schema
        from .external_domain_name import ExternalDomainName
        from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow
        from .e_book_install_summary import EBookInstallSummary
        from .feature_rollout_policy import FeatureRolloutPolicy
        from .federated_identity_credential import FederatedIdentityCredential
        from .fido2_authentication_method import Fido2AuthenticationMethod
        from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration
        from .fido2_combination_configuration import Fido2CombinationConfiguration
        from .field_value_set import FieldValueSet
        from .file_assessment_request import FileAssessmentRequest
        from .file_attachment import FileAttachment
        from .file_storage import FileStorage
        from .file_storage_container import FileStorageContainer
        from .file_storage_container_type import FileStorageContainerType
        from .file_storage_container_type_registration import FileStorageContainerTypeRegistration
        from .filter_operator_schema import FilterOperatorSchema
        from .fixture_map import FixtureMap
        from .floor import Floor
        from .footprint_map import FootprintMap
        from .fraud_protection_provider import FraudProtectionProvider
        from .governance_insight import GovernanceInsight
        from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
        from .group import Group
        from .group_lifecycle_policy import GroupLifecyclePolicy
        from .group_setting import GroupSetting
        from .group_setting_template import GroupSettingTemplate
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .horizontal_section import HorizontalSection
        from .horizontal_section_column import HorizontalSectionColumn
        from .human_security_fraud_protection_provider import HumanSecurityFraudProtectionProvider
        from .identity_api_connector import IdentityApiConnector
        from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
        from .identity_container import IdentityContainer
        from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute
        from .identity_governance.custom_task_extension import CustomTaskExtension
        from .identity_governance.insights import Insights
        from .identity_governance.lifecycle_management_settings import LifecycleManagementSettings
        from .identity_governance.lifecycle_workflows_container import LifecycleWorkflowsContainer
        from .identity_governance.run import Run
        from .identity_governance.task import Task
        from .identity_governance.task_definition import TaskDefinition
        from .identity_governance.task_processing_result import TaskProcessingResult
        from .identity_governance.task_report import TaskReport
        from .identity_governance.user_processing_result import UserProcessingResult
        from .identity_governance.workflow_template import WorkflowTemplate
        from .identity_provider import IdentityProvider
        from .identity_provider_base import IdentityProviderBase
        from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
        from .identity_user_flow import IdentityUserFlow
        from .identity_user_flow_attribute import IdentityUserFlowAttribute
        from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
        from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
        from .imported_windows_autopilot_device_identity_upload import ImportedWindowsAutopilotDeviceIdentityUpload
        from .inference_classification import InferenceClassification
        from .inference_classification_override import InferenceClassificationOverride
        from .insights_settings import InsightsSettings
        from .internal_domain_federation import InternalDomainFederation
        from .internet_explorer_mode import InternetExplorerMode
        from .invitation import Invitation
        from .invite_participants_operation import InviteParticipantsOperation
        from .iosi_pad_o_s_web_clip import IosiPadOSWebClip
        from .ios_certificate_profile import IosCertificateProfile
        from .ios_compliance_policy import IosCompliancePolicy
        from .ios_custom_configuration import IosCustomConfiguration
        from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
        from .ios_general_device_configuration import IosGeneralDeviceConfiguration
        from .ios_lob_app import IosLobApp
        from .ios_lob_app_provisioning_configuration_assignment import IosLobAppProvisioningConfigurationAssignment
        from .ios_managed_app_protection import IosManagedAppProtection
        from .ios_managed_app_registration import IosManagedAppRegistration
        from .ios_mobile_app_configuration import IosMobileAppConfiguration
        from .ios_store_app import IosStoreApp
        from .ios_update_configuration import IosUpdateConfiguration
        from .ios_update_device_status import IosUpdateDeviceStatus
        from .ios_vpp_app import IosVppApp
        from .ios_vpp_e_book import IosVppEBook
        from .ios_vpp_e_book_assignment import IosVppEBookAssignment
        from .ip_named_location import IpNamedLocation
        from .item_activity import ItemActivity
        from .item_activity_stat import ItemActivityStat
        from .item_analytics import ItemAnalytics
        from .item_attachment import ItemAttachment
        from .item_insights import ItemInsights
        from .item_retention_label import ItemRetentionLabel
        from .label_content_right import LabelContentRight
        from .landing_page import LandingPage
        from .landing_page_detail import LandingPageDetail
        from .learning_assignment import LearningAssignment
        from .learning_content import LearningContent
        from .learning_course_activity import LearningCourseActivity
        from .learning_provider import LearningProvider
        from .learning_self_initiated_course import LearningSelfInitiatedCourse
        from .level_map import LevelMap
        from .license_details import LicenseDetails
        from .linked_resource import LinkedResource
        from .list_ import List_
        from .list_item import ListItem
        from .list_item_version import ListItemVersion
        from .localized_notification_message import LocalizedNotificationMessage
        from .login_page import LoginPage
        from .long_running_operation import LongRunningOperation
        from .m365_apps_installation_options import M365AppsInstallationOptions
        from .mac_o_s_compliance_policy import MacOSCompliancePolicy
        from .mac_o_s_custom_configuration import MacOSCustomConfiguration
        from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
        from .mac_o_s_dmg_app import MacOSDmgApp
        from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
        from .mac_o_s_lob_app import MacOSLobApp
        from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp
        from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp
        from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp
        from .mailbox_protection_rule import MailboxProtectionRule
        from .mailbox_protection_unit import MailboxProtectionUnit
        from .mailbox_protection_units_bulk_addition_job import MailboxProtectionUnitsBulkAdditionJob
        from .mailbox_restore_artifact import MailboxRestoreArtifact
        from .mailbox_restore_artifacts_bulk_addition_request import MailboxRestoreArtifactsBulkAdditionRequest
        from .mail_assessment_request import MailAssessmentRequest
        from .mail_folder import MailFolder
        from .mail_search_folder import MailSearchFolder
        from .malware_state_for_windows_device import MalwareStateForWindowsDevice
        from .managed_android_lob_app import ManagedAndroidLobApp
        from .managed_android_store_app import ManagedAndroidStoreApp
        from .managed_app import ManagedApp
        from .managed_app_configuration import ManagedAppConfiguration
        from .managed_app_operation import ManagedAppOperation
        from .managed_app_policy import ManagedAppPolicy
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_app_protection import ManagedAppProtection
        from .managed_app_registration import ManagedAppRegistration
        from .managed_app_status import ManagedAppStatus
        from .managed_app_status_raw import ManagedAppStatusRaw
        from .managed_device import ManagedDevice
        from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
        from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
        from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
        from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary
        from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
        from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary
        from .managed_device_overview import ManagedDeviceOverview
        from .managed_e_book import ManagedEBook
        from .managed_e_book_assignment import ManagedEBookAssignment
        from .managed_i_o_s_lob_app import ManagedIOSLobApp
        from .managed_i_o_s_store_app import ManagedIOSStoreApp
        from .managed_mobile_app import ManagedMobileApp
        from .managed_mobile_lob_app import ManagedMobileLobApp
        from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
        from .meeting_attendance_report import MeetingAttendanceReport
        from .membership_outlier_insight import MembershipOutlierInsight
        from .message import Message
        from .message_rule import MessageRule
        from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember
        from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
        from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration
        from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
        from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp
        from .mobile_app import MobileApp
        from .mobile_app_assignment import MobileAppAssignment
        from .mobile_app_category import MobileAppCategory
        from .mobile_app_content import MobileAppContent
        from .mobile_app_content_file import MobileAppContentFile
        from .mobile_app_relationship import MobileAppRelationship
        from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
        from .mobile_contained_app import MobileContainedApp
        from .mobile_lob_app import MobileLobApp
        from .mobile_threat_defense_connector import MobileThreatDefenseConnector
        from .multi_tenant_organization import MultiTenantOrganization
        from .multi_tenant_organization_identity_sync_policy_template import MultiTenantOrganizationIdentitySyncPolicyTemplate
        from .multi_tenant_organization_join_request_record import MultiTenantOrganizationJoinRequestRecord
        from .multi_tenant_organization_member import MultiTenantOrganizationMember
        from .multi_tenant_organization_partner_configuration_template import MultiTenantOrganizationPartnerConfigurationTemplate
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .mute_participant_operation import MuteParticipantOperation
        from .named_location import NamedLocation
        from .notebook import Notebook
        from .notification_message_template import NotificationMessageTemplate
        from .offer_shift_request import OfferShiftRequest
        from .office_graph_insights import OfficeGraphInsights
        from .onenote import Onenote
        from .onenote_entity_base_model import OnenoteEntityBaseModel
        from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
        from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
        from .onenote_operation import OnenoteOperation
        from .onenote_page import OnenotePage
        from .onenote_resource import OnenoteResource
        from .onenote_section import OnenoteSection
        from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
        from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
        from .online_meeting import OnlineMeeting
        from .online_meeting_base import OnlineMeetingBase
        from .online_meeting_engagement_conversation import OnlineMeetingEngagementConversation
        from .on_attribute_collection_listener import OnAttributeCollectionListener
        from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
        from .on_attribute_collection_start_listener import OnAttributeCollectionStartListener
        from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
        from .on_attribute_collection_submit_listener import OnAttributeCollectionSubmitListener
        from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener
        from .on_email_otp_send_listener import OnEmailOtpSendListener
        from .on_fraud_protection_load_start_listener import OnFraudProtectionLoadStartListener
        from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener
        from .on_otp_send_custom_extension import OnOtpSendCustomExtension
        from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
        from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
        from .on_premises_sync_behavior import OnPremisesSyncBehavior
        from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension
        from .on_token_issuance_start_listener import OnTokenIssuanceStartListener
        from .on_user_create_start_listener import OnUserCreateStartListener
        from .open_shift import OpenShift
        from .open_shift_change_request import OpenShiftChangeRequest
        from .open_type_extension import OpenTypeExtension
        from .operation import Operation
        from .organization import Organization
        from .organizational_branding import OrganizationalBranding
        from .organizational_branding_localization import OrganizationalBrandingLocalization
        from .organizational_branding_properties import OrganizationalBrandingProperties
        from .org_contact import OrgContact
        from .outlook_category import OutlookCategory
        from .outlook_item import OutlookItem
        from .outlook_user import OutlookUser
        from .o_auth2_permission_grant import OAuth2PermissionGrant
        from .participant import Participant
        from .participant_joining_notification import ParticipantJoiningNotification
        from .participant_left_notification import ParticipantLeftNotification
        from .partners.billing.azure_usage import AzureUsage
        from .partners.billing.billed_reconciliation import BilledReconciliation
        from .partners.billing.billed_usage import BilledUsage
        from .partners.billing.billing import Billing
        from .partners.billing.billing_reconciliation import BillingReconciliation
        from .partners.billing.export_success_operation import ExportSuccessOperation
        from .partners.billing.failed_operation import FailedOperation
        from .partners.billing.manifest import Manifest
        from .partners.billing.operation import Operation
        from .partners.billing.running_operation import RunningOperation
        from .partners.billing.unbilled_reconciliation import UnbilledReconciliation
        from .partners.billing.unbilled_usage import UnbilledUsage
        from .partners.partners import Partners
        from .password_authentication_method import PasswordAuthenticationMethod
        from .payload import Payload
        from .people_admin_settings import PeopleAdminSettings
        from .permission import Permission
        from .permission_grant_condition_set import PermissionGrantConditionSet
        from .permission_grant_policy import PermissionGrantPolicy
        from .person import Person
        from .phone_authentication_method import PhoneAuthenticationMethod
        from .phone_user_conversation_member import PhoneUserConversationMember
        from .pinned_chat_message_info import PinnedChatMessageInfo
        from .place import Place
        from .planner import Planner
        from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
        from .planner_bucket import PlannerBucket
        from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
        from .planner_group import PlannerGroup
        from .planner_plan import PlannerPlan
        from .planner_plan_details import PlannerPlanDetails
        from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
        from .planner_task import PlannerTask
        from .planner_task_details import PlannerTaskDetails
        from .planner_user import PlannerUser
        from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
        from .play_prompt_operation import PlayPromptOperation
        from .policy_base import PolicyBase
        from .policy_root import PolicyRoot
        from .policy_template import PolicyTemplate
        from .post import Post
        from .presence import Presence
        from .printer import Printer
        from .printer_base import PrinterBase
        from .printer_create_operation import PrinterCreateOperation
        from .printer_share import PrinterShare
        from .print_connector import PrintConnector
        from .print_document import PrintDocument
        from .print_job import PrintJob
        from .print_operation import PrintOperation
        from .print_service import PrintService
        from .print_service_endpoint import PrintServiceEndpoint
        from .print_task import PrintTask
        from .print_task_definition import PrintTaskDefinition
        from .print_task_trigger import PrintTaskTrigger
        from .print_usage import PrintUsage
        from .print_usage_by_printer import PrintUsageByPrinter
        from .print_usage_by_user import PrintUsageByUser
        from .privileged_access_group import PrivilegedAccessGroup
        from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
        from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
        from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
        from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
        from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
        from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
        from .privileged_access_root import PrivilegedAccessRoot
        from .privileged_access_schedule import PrivilegedAccessSchedule
        from .privileged_access_schedule_instance import PrivilegedAccessScheduleInstance
        from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest
        from .profile_card_property import ProfileCardProperty
        from .profile_photo import ProfilePhoto
        from .pronouns_settings import PronounsSettings
        from .protection_policy_base import ProtectionPolicyBase
        from .protection_rule_base import ProtectionRuleBase
        from .protection_units_bulk_job_base import ProtectionUnitsBulkJobBase
        from .protection_unit_base import ProtectionUnitBase
        from .provisioning_object_summary import ProvisioningObjectSummary
        from .public_key_infrastructure_root import PublicKeyInfrastructureRoot
        from .rbac_application import RbacApplication
        from .reading_assignment_submission import ReadingAssignmentSubmission
        from .reading_coach_passage import ReadingCoachPassage
        from .record_operation import RecordOperation
        from .recycle_bin import RecycleBin
        from .recycle_bin_item import RecycleBinItem
        from .reference_attachment import ReferenceAttachment
        from .reflect_check_in_response import ReflectCheckInResponse
        from .relying_party_detailed_summary import RelyingPartyDetailedSummary
        from .remote_assistance_partner import RemoteAssistancePartner
        from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
        from .reports_root import ReportsRoot
        from .request import Request
        from .reseller_delegated_admin_relationship import ResellerDelegatedAdminRelationship
        from .resource_operation import ResourceOperation
        from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
        from .restore_artifacts_bulk_request_base import RestoreArtifactsBulkRequestBase
        from .restore_artifact_base import RestoreArtifactBase
        from .restore_point import RestorePoint
        from .restore_session_base import RestoreSessionBase
        from .rich_long_running_operation import RichLongRunningOperation
        from .risky_service_principal import RiskyServicePrincipal
        from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem
        from .risky_user import RiskyUser
        from .risky_user_history_item import RiskyUserHistoryItem
        from .risk_detection import RiskDetection
        from .role_assignment import RoleAssignment
        from .role_definition import RoleDefinition
        from .room import Room
        from .room_list import RoomList
        from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
        from .saml_or_ws_fed_provider import SamlOrWsFedProvider
        from .schedule import Schedule
        from .schedule_change_request import ScheduleChangeRequest
        from .scheduling_group import SchedulingGroup
        from .schema_extension import SchemaExtension
        from .scoped_role_membership import ScopedRoleMembership
        from .search.acronym import Acronym
        from .search.bookmark import Bookmark
        from .search.qna import Qna
        from .search.search_answer import SearchAnswer
        from .search_entity import SearchEntity
        from .section import Section
        from .section_group import SectionGroup
        from .section_map import SectionMap
        from .secure_score import SecureScore
        from .secure_score_control_profile import SecureScoreControlProfile
        from .security.alert import Alert
        from .security.article import Article
        from .security.article_indicator import ArticleIndicator
        from .security.artifact import Artifact
        from .security.authority_template import AuthorityTemplate
        from .security.case import Case
        from .security.cases_root import CasesRoot
        from .security.case_operation import CaseOperation
        from .security.category_template import CategoryTemplate
        from .security.citation_template import CitationTemplate
        from .security.data_set import DataSet
        from .security.data_source import DataSource
        from .security.data_source_container import DataSourceContainer
        from .security.department_template import DepartmentTemplate
        from .security.disposition_review_stage import DispositionReviewStage
        from .security.ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
        from .security.ediscovery_case import EdiscoveryCase
        from .security.ediscovery_case_member import EdiscoveryCaseMember
        from .security.ediscovery_case_settings import EdiscoveryCaseSettings
        from .security.ediscovery_custodian import EdiscoveryCustodian
        from .security.ediscovery_estimate_operation import EdiscoveryEstimateOperation
        from .security.ediscovery_export_operation import EdiscoveryExportOperation
        from .security.ediscovery_hold_operation import EdiscoveryHoldOperation
        from .security.ediscovery_hold_policy_sync_operation import EdiscoveryHoldPolicySyncOperation
        from .security.ediscovery_index_operation import EdiscoveryIndexOperation
        from .security.ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
        from .security.ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
        from .security.ediscovery_review_set import EdiscoveryReviewSet
        from .security.ediscovery_review_set_query import EdiscoveryReviewSetQuery
        from .security.ediscovery_review_tag import EdiscoveryReviewTag
        from .security.ediscovery_search import EdiscoverySearch
        from .security.ediscovery_search_export_operation import EdiscoverySearchExportOperation
        from .security.ediscovery_tag_operation import EdiscoveryTagOperation
        from .security.file_plan_descriptor import FilePlanDescriptor
        from .security.file_plan_descriptor_template import FilePlanDescriptorTemplate
        from .security.file_plan_reference_template import FilePlanReferenceTemplate
        from .security.health_issue import HealthIssue
        from .security.host import Host
        from .security.hostname import Hostname
        from .security.host_component import HostComponent
        from .security.host_cookie import HostCookie
        from .security.host_pair import HostPair
        from .security.host_port import HostPort
        from .security.host_reputation import HostReputation
        from .security.host_ssl_certificate import HostSslCertificate
        from .security.host_tracker import HostTracker
        from .security.identity_accounts import IdentityAccounts
        from .security.identity_container import IdentityContainer
        from .security.incident import Incident
        from .security.indicator import Indicator
        from .security.intelligence_profile import IntelligenceProfile
        from .security.intelligence_profile_indicator import IntelligenceProfileIndicator
        from .security.ip_address import IpAddress
        from .security.labels_root import LabelsRoot
        from .security.network_adapter import NetworkAdapter
        from .security.passive_dns_record import PassiveDnsRecord
        from .security.retention_event import RetentionEvent
        from .security.retention_event_type import RetentionEventType
        from .security.retention_label import RetentionLabel
        from .security.search import Search
        from .security.security import Security
        from .security.sensor import Sensor
        from .security.sensor_candidate import SensorCandidate
        from .security.sensor_candidate_activation_configuration import SensorCandidateActivationConfiguration
        from .security.site_source import SiteSource
        from .security.ssl_certificate import SslCertificate
        from .security.subcategory_template import SubcategoryTemplate
        from .security.subdomain import Subdomain
        from .security.tag import Tag
        from .security.threat_intelligence import ThreatIntelligence
        from .security.triggers_root import TriggersRoot
        from .security.trigger_types_root import TriggerTypesRoot
        from .security.unclassified_artifact import UnclassifiedArtifact
        from .security.unified_group_source import UnifiedGroupSource
        from .security.user import User
        from .security.user_source import UserSource
        from .security.vulnerability import Vulnerability
        from .security.vulnerability_component import VulnerabilityComponent
        from .security.whois_base_record import WhoisBaseRecord
        from .security.whois_history_record import WhoisHistoryRecord
        from .security.whois_record import WhoisRecord
        from .security_reports_root import SecurityReportsRoot
        from .send_dtmf_tones_operation import SendDtmfTonesOperation
        from .sensitivity_label import SensitivityLabel
        from .service_announcement import ServiceAnnouncement
        from .service_announcement_attachment import ServiceAnnouncementAttachment
        from .service_announcement_base import ServiceAnnouncementBase
        from .service_app import ServiceApp
        from .service_health import ServiceHealth
        from .service_health_issue import ServiceHealthIssue
        from .service_principal import ServicePrincipal
        from .service_principal_risk_detection import ServicePrincipalRiskDetection
        from .service_storage_quota_breakdown import ServiceStorageQuotaBreakdown
        from .service_update_message import ServiceUpdateMessage
        from .setting_state_device_summary import SettingStateDeviceSummary
        from .shared_drive_item import SharedDriveItem
        from .shared_insight import SharedInsight
        from .shared_p_c_configuration import SharedPCConfiguration
        from .shared_with_channel_team_info import SharedWithChannelTeamInfo
        from .sharepoint import Sharepoint
        from .sharepoint_settings import SharepointSettings
        from .share_point_migration_event import SharePointMigrationEvent
        from .share_point_migration_finish_manifest_file_upload_event import SharePointMigrationFinishManifestFileUploadEvent
        from .share_point_migration_job import SharePointMigrationJob
        from .share_point_migration_job_cancelled_event import SharePointMigrationJobCancelledEvent
        from .share_point_migration_job_deleted_event import SharePointMigrationJobDeletedEvent
        from .share_point_migration_job_error_event import SharePointMigrationJobErrorEvent
        from .share_point_migration_job_postponed_event import SharePointMigrationJobPostponedEvent
        from .share_point_migration_job_progress_event import SharePointMigrationJobProgressEvent
        from .share_point_migration_job_queued_event import SharePointMigrationJobQueuedEvent
        from .share_point_migration_job_start_event import SharePointMigrationJobStartEvent
        from .share_point_protection_policy import SharePointProtectionPolicy
        from .share_point_restore_session import SharePointRestoreSession
        from .shift import Shift
        from .shift_preferences import ShiftPreferences
        from .sign_in import SignIn
        from .simulation import Simulation
        from .simulation_automation import SimulationAutomation
        from .simulation_automation_run import SimulationAutomationRun
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
        from .site import Site
        from .site_page import SitePage
        from .site_protection_rule import SiteProtectionRule
        from .site_protection_unit import SiteProtectionUnit
        from .site_protection_units_bulk_addition_job import SiteProtectionUnitsBulkAdditionJob
        from .site_restore_artifact import SiteRestoreArtifact
        from .site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest
        from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember
        from .skype_user_conversation_member import SkypeUserConversationMember
        from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration
        from .sms_authentication_method_target import SmsAuthenticationMethodTarget
        from .social_identity_provider import SocialIdentityProvider
        from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
        from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration
        from .software_update_status_summary import SoftwareUpdateStatusSummary
        from .speaker_assignment_submission import SpeakerAssignmentSubmission
        from .standard_web_part import StandardWebPart
        from .start_hold_music_operation import StartHoldMusicOperation
        from .stop_hold_music_operation import StopHoldMusicOperation
        from .storage_quota_breakdown import StorageQuotaBreakdown
        from .storage_settings import StorageSettings
        from .sts_policy import StsPolicy
        from .subject_rights_request import SubjectRightsRequest
        from .subscribed_sku import SubscribedSku
        from .subscribe_to_tone_operation import SubscribeToToneOperation
        from .subscription import Subscription
        from .swap_shifts_change_request import SwapShiftsChangeRequest
        from .synchronization import Synchronization
        from .synchronization_job import SynchronizationJob
        from .synchronization_schema import SynchronizationSchema
        from .synchronization_template import SynchronizationTemplate
        from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
        from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
        from .targeted_managed_app_protection import TargetedManagedAppProtection
        from .target_device_group import TargetDeviceGroup
        from .task_file_attachment import TaskFileAttachment
        from .team import Team
        from .teams_administration.teams_admin_root import TeamsAdminRoot
        from .teams_administration.teams_user_configuration import TeamsUserConfiguration
        from .teams_app import TeamsApp
        from .teams_app_definition import TeamsAppDefinition
        from .teams_app_installation import TeamsAppInstallation
        from .teams_app_settings import TeamsAppSettings
        from .teams_async_operation import TeamsAsyncOperation
        from .teams_tab import TeamsTab
        from .teams_template import TeamsTemplate
        from .teamwork import Teamwork
        from .teamwork_bot import TeamworkBot
        from .teamwork_hosted_content import TeamworkHostedContent
        from .teamwork_tag import TeamworkTag
        from .teamwork_tag_member import TeamworkTagMember
        from .team_info import TeamInfo
        from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
        from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration
        from .tenant_app_management_policy import TenantAppManagementPolicy
        from .tenant_data_security_and_governance import TenantDataSecurityAndGovernance
        from .tenant_protection_scope_container import TenantProtectionScopeContainer
        from .terms_and_conditions import TermsAndConditions
        from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
        from .terms_and_conditions_assignment import TermsAndConditionsAssignment
        from .terms_of_use_container import TermsOfUseContainer
        from .term_store.group import Group
        from .term_store.relation import Relation
        from .term_store.set import Set
        from .term_store.store import Store
        from .term_store.term import Term
        from .text_web_part import TextWebPart
        from .threat_assessment_request import ThreatAssessmentRequest
        from .threat_assessment_result import ThreatAssessmentResult
        from .thumbnail_set import ThumbnailSet
        from .time_card import TimeCard
        from .time_off import TimeOff
        from .time_off_reason import TimeOffReason
        from .time_off_request import TimeOffRequest
        from .todo import Todo
        from .todo_task import TodoTask
        from .todo_task_list import TodoTaskList
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .training import Training
        from .training_language_detail import TrainingLanguageDetail
        from .trending import Trending
        from .unified_rbac_resource_action import UnifiedRbacResourceAction
        from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
        from .unified_role_assignment import UnifiedRoleAssignment
        from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
        from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
        from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
        from .unified_role_definition import UnifiedRoleDefinition
        from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
        from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
        from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest
        from .unified_role_management_policy import UnifiedRoleManagementPolicy
        from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule
        from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment
        from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule
        from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule
        from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule
        from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule
        from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule
        from .unified_role_schedule_base import UnifiedRoleScheduleBase
        from .unified_role_schedule_instance_base import UnifiedRoleScheduleInstanceBase
        from .unified_storage_quota import UnifiedStorageQuota
        from .unit_map import UnitMap
        from .unmute_participant_operation import UnmuteParticipantOperation
        from .update_recording_status_operation import UpdateRecordingStatusOperation
        from .url_assessment_request import UrlAssessmentRequest
        from .usage_rights_included import UsageRightsIncluded
        from .used_insight import UsedInsight
        from .user import User
        from .user_activity import UserActivity
        from .user_consent_request import UserConsentRequest
        from .user_data_security_and_governance import UserDataSecurityAndGovernance
        from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformance
        from .user_experience_analytics_app_health_app_performance_by_app_version_details import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
        from .user_experience_analytics_app_health_app_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId
        from .user_experience_analytics_app_health_app_performance_by_o_s_version import UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion
        from .user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformance
        from .user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformance
        from .user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetails
        from .user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformance
        from .user_experience_analytics_baseline import UserExperienceAnalyticsBaseline
        from .user_experience_analytics_category import UserExperienceAnalyticsCategory
        from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance
        from .user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScores
        from .user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistory
        from .user_experience_analytics_device_startup_process import UserExperienceAnalyticsDeviceStartupProcess
        from .user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformance
        from .user_experience_analytics_metric import UserExperienceAnalyticsMetric
        from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
        from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
        from .user_experience_analytics_overview import UserExperienceAnalyticsOverview
        from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory
        from .user_experience_analytics_work_from_anywhere_device import UserExperienceAnalyticsWorkFromAnywhereDevice
        from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
        from .user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
        from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance
        from .user_flow_language_configuration import UserFlowLanguageConfiguration
        from .user_flow_language_page import UserFlowLanguagePage
        from .user_insights_settings import UserInsightsSettings
        from .user_install_state_summary import UserInstallStateSummary
        from .user_protection_scope_container import UserProtectionScopeContainer
        from .user_registration_details import UserRegistrationDetails
        from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation
        from .user_settings import UserSettings
        from .user_sign_in_insight import UserSignInInsight
        from .user_solution_root import UserSolutionRoot
        from .user_storage import UserStorage
        from .user_teamwork import UserTeamwork
        from .vertical_section import VerticalSection
        from .virtual_endpoint import VirtualEndpoint
        from .virtual_event import VirtualEvent
        from .virtual_events_root import VirtualEventsRoot
        from .virtual_event_presenter import VirtualEventPresenter
        from .virtual_event_registration import VirtualEventRegistration
        from .virtual_event_registration_configuration import VirtualEventRegistrationConfiguration
        from .virtual_event_registration_custom_question import VirtualEventRegistrationCustomQuestion
        from .virtual_event_registration_predefined_question import VirtualEventRegistrationPredefinedQuestion
        from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase
        from .virtual_event_session import VirtualEventSession
        from .virtual_event_townhall import VirtualEventTownhall
        from .virtual_event_webinar import VirtualEventWebinar
        from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration
        from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration
        from .vpp_token import VppToken
        from .web_app import WebApp
        from .web_application_firewall_provider import WebApplicationFirewallProvider
        from .web_application_firewall_verification_model import WebApplicationFirewallVerificationModel
        from .web_part import WebPart
        from .what_if_analysis_result import WhatIfAnalysisResult
        from .win32_lob_app import Win32LobApp
        from .windows10_compliance_policy import Windows10CompliancePolicy
        from .windows10_custom_configuration import Windows10CustomConfiguration
        from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
        from .windows10_enrollment_completion_page_configuration import Windows10EnrollmentCompletionPageConfiguration
        from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
        from .windows10_general_configuration import Windows10GeneralConfiguration
        from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy
        from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
        from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
        from .windows81_compliance_policy import Windows81CompliancePolicy
        from .windows81_general_configuration import Windows81GeneralConfiguration
        from .windows_app_x import WindowsAppX
        from .windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
        from .windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment
        from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
        from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
        from .windows_device_malware_state import WindowsDeviceMalwareState
        from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod
        from .windows_information_protection import WindowsInformationProtection
        from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
        from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile
        from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
        from .windows_information_protection_policy import WindowsInformationProtectionPolicy
        from .windows_malware_information import WindowsMalwareInformation
        from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp
        from .windows_mobile_m_s_i import WindowsMobileMSI
        from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy
        from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
        from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
        from .windows_protection_state import WindowsProtectionState
        from .windows_setting import WindowsSetting
        from .windows_setting_instance import WindowsSettingInstance
        from .windows_universal_app_x import WindowsUniversalAppX
        from .windows_universal_app_x_contained_app import WindowsUniversalAppXContainedApp
        from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration
        from .windows_web_app import WindowsWebApp
        from .workbook import Workbook
        from .workbook_application import WorkbookApplication
        from .workbook_chart import WorkbookChart
        from .workbook_chart_area_format import WorkbookChartAreaFormat
        from .workbook_chart_axes import WorkbookChartAxes
        from .workbook_chart_axis import WorkbookChartAxis
        from .workbook_chart_axis_format import WorkbookChartAxisFormat
        from .workbook_chart_axis_title import WorkbookChartAxisTitle
        from .workbook_chart_axis_title_format import WorkbookChartAxisTitleFormat
        from .workbook_chart_data_labels import WorkbookChartDataLabels
        from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat
        from .workbook_chart_fill import WorkbookChartFill
        from .workbook_chart_font import WorkbookChartFont
        from .workbook_chart_gridlines import WorkbookChartGridlines
        from .workbook_chart_gridlines_format import WorkbookChartGridlinesFormat
        from .workbook_chart_legend import WorkbookChartLegend
        from .workbook_chart_legend_format import WorkbookChartLegendFormat
        from .workbook_chart_line_format import WorkbookChartLineFormat
        from .workbook_chart_point import WorkbookChartPoint
        from .workbook_chart_point_format import WorkbookChartPointFormat
        from .workbook_chart_series import WorkbookChartSeries
        from .workbook_chart_series_format import WorkbookChartSeriesFormat
        from .workbook_chart_title import WorkbookChartTitle
        from .workbook_chart_title_format import WorkbookChartTitleFormat
        from .workbook_comment import WorkbookComment
        from .workbook_comment_reply import WorkbookCommentReply
        from .workbook_filter import WorkbookFilter
        from .workbook_format_protection import WorkbookFormatProtection
        from .workbook_functions import WorkbookFunctions
        from .workbook_function_result import WorkbookFunctionResult
        from .workbook_named_item import WorkbookNamedItem
        from .workbook_operation import WorkbookOperation
        from .workbook_pivot_table import WorkbookPivotTable
        from .workbook_range import WorkbookRange
        from .workbook_range_border import WorkbookRangeBorder
        from .workbook_range_fill import WorkbookRangeFill
        from .workbook_range_font import WorkbookRangeFont
        from .workbook_range_format import WorkbookRangeFormat
        from .workbook_range_sort import WorkbookRangeSort
        from .workbook_range_view import WorkbookRangeView
        from .workbook_table import WorkbookTable
        from .workbook_table_column import WorkbookTableColumn
        from .workbook_table_row import WorkbookTableRow
        from .workbook_table_sort import WorkbookTableSort
        from .workbook_worksheet import WorkbookWorksheet
        from .workbook_worksheet_protection import WorkbookWorksheetProtection
        from .workforce_integration import WorkforceIntegration
        from .working_time_schedule import WorkingTimeSchedule
        from .workspace import Workspace
        from .work_hours_and_locations_setting import WorkHoursAndLocationsSetting
        from .work_plan_occurrence import WorkPlanOccurrence
        from .work_plan_recurrence import WorkPlanRecurrence
        from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration
        from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration

        from .aad_user_conversation_member import AadUserConversationMember
        from .access_package import AccessPackage
        from .access_package_assignment import AccessPackageAssignment
        from .access_package_assignment_policy import AccessPackageAssignmentPolicy
        from .access_package_assignment_request import AccessPackageAssignmentRequest
        from .access_package_assignment_request_workflow_extension import AccessPackageAssignmentRequestWorkflowExtension
        from .access_package_assignment_workflow_extension import AccessPackageAssignmentWorkflowExtension
        from .access_package_catalog import AccessPackageCatalog
        from .access_package_multiple_choice_question import AccessPackageMultipleChoiceQuestion
        from .access_package_question import AccessPackageQuestion
        from .access_package_resource import AccessPackageResource
        from .access_package_resource_environment import AccessPackageResourceEnvironment
        from .access_package_resource_request import AccessPackageResourceRequest
        from .access_package_resource_role import AccessPackageResourceRole
        from .access_package_resource_role_scope import AccessPackageResourceRoleScope
        from .access_package_resource_scope import AccessPackageResourceScope
        from .access_package_subject import AccessPackageSubject
        from .access_package_text_input_question import AccessPackageTextInputQuestion
        from .access_review_history_definition import AccessReviewHistoryDefinition
        from .access_review_history_instance import AccessReviewHistoryInstance
        from .access_review_instance import AccessReviewInstance
        from .access_review_instance_decision_item import AccessReviewInstanceDecisionItem
        from .access_review_reviewer import AccessReviewReviewer
        from .access_review_schedule_definition import AccessReviewScheduleDefinition
        from .access_review_set import AccessReviewSet
        from .access_review_stage import AccessReviewStage
        from .activities_container import ActivitiesContainer
        from .activity_based_timeout_policy import ActivityBasedTimeoutPolicy
        from .activity_history_item import ActivityHistoryItem
        from .add_large_gallery_view_operation import AddLargeGalleryViewOperation
        from .adhoc_call import AdhocCall
        from .administrative_unit import AdministrativeUnit
        from .admin_consent_request_policy import AdminConsentRequestPolicy
        from .admin_microsoft365_apps import AdminMicrosoft365Apps
        from .admin_report_settings import AdminReportSettings
        from .agreement import Agreement
        from .agreement_acceptance import AgreementAcceptance
        from .agreement_file import AgreementFile
        from .agreement_file_localization import AgreementFileLocalization
        from .agreement_file_properties import AgreementFileProperties
        from .agreement_file_version import AgreementFileVersion
        from .ai_interaction import AiInteraction
        from .ai_interaction_history import AiInteractionHistory
        from .ai_online_meeting import AiOnlineMeeting
        from .ai_user import AiUser
        from .akamai_web_application_firewall_provider import AkamaiWebApplicationFirewallProvider
        from .alert import Alert
        from .allowed_value import AllowedValue
        from .android_compliance_policy import AndroidCompliancePolicy
        from .android_custom_configuration import AndroidCustomConfiguration
        from .android_general_device_configuration import AndroidGeneralDeviceConfiguration
        from .android_lob_app import AndroidLobApp
        from .android_managed_app_protection import AndroidManagedAppProtection
        from .android_managed_app_registration import AndroidManagedAppRegistration
        from .android_store_app import AndroidStoreApp
        from .android_work_profile_compliance_policy import AndroidWorkProfileCompliancePolicy
        from .android_work_profile_custom_configuration import AndroidWorkProfileCustomConfiguration
        from .android_work_profile_general_device_configuration import AndroidWorkProfileGeneralDeviceConfiguration
        from .anonymous_guest_conversation_member import AnonymousGuestConversationMember
        from .apple_device_features_configuration_base import AppleDeviceFeaturesConfigurationBase
        from .apple_managed_identity_provider import AppleManagedIdentityProvider
        from .apple_push_notification_certificate import ApplePushNotificationCertificate
        from .application import Application
        from .application_template import ApplicationTemplate
        from .approval import Approval
        from .approval_stage import ApprovalStage
        from .app_catalogs import AppCatalogs
        from .app_consent_approval_route import AppConsentApprovalRoute
        from .app_consent_request import AppConsentRequest
        from .app_log_collection_request import AppLogCollectionRequest
        from .app_management_policy import AppManagementPolicy
        from .app_role_assignment import AppRoleAssignment
        from .app_scope import AppScope
        from .arkose_fraud_protection_provider import ArkoseFraudProtectionProvider
        from .associated_team_info import AssociatedTeamInfo
        from .attachment import Attachment
        from .attachment_base import AttachmentBase
        from .attachment_session import AttachmentSession
        from .attack_simulation_operation import AttackSimulationOperation
        from .attack_simulation_root import AttackSimulationRoot
        from .attendance_record import AttendanceRecord
        from .attribute_mapping_function_schema import AttributeMappingFunctionSchema
        from .attribute_set import AttributeSet
        from .audio_routing_group import AudioRoutingGroup
        from .audit_event import AuditEvent
        from .audit_log_root import AuditLogRoot
        from .authentication import Authentication
        from .authentication_combination_configuration import AuthenticationCombinationConfiguration
        from .authentication_context_class_reference import AuthenticationContextClassReference
        from .authentication_events_flow import AuthenticationEventsFlow
        from .authentication_event_listener import AuthenticationEventListener
        from .authentication_flows_policy import AuthenticationFlowsPolicy
        from .authentication_method import AuthenticationMethod
        from .authentication_methods_policy import AuthenticationMethodsPolicy
        from .authentication_methods_root import AuthenticationMethodsRoot
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_mode_detail import AuthenticationMethodModeDetail
        from .authentication_method_target import AuthenticationMethodTarget
        from .authentication_strength_policy import AuthenticationStrengthPolicy
        from .authentication_strength_root import AuthenticationStrengthRoot
        from .authored_note import AuthoredNote
        from .authorization_policy import AuthorizationPolicy
        from .azure_communication_services_user_conversation_member import AzureCommunicationServicesUserConversationMember
        from .b2x_identity_user_flow import B2xIdentityUserFlow
        from .backup_restore_root import BackupRestoreRoot
        from .base_item import BaseItem
        from .base_item_version import BaseItemVersion
        from .base_map_feature import BaseMapFeature
        from .base_site_page import BaseSitePage
        from .bitlocker import Bitlocker
        from .bitlocker_recovery_key import BitlockerRecoveryKey
        from .booking_appointment import BookingAppointment
        from .booking_business import BookingBusiness
        from .booking_currency import BookingCurrency
        from .booking_customer import BookingCustomer
        from .booking_customer_base import BookingCustomerBase
        from .booking_custom_question import BookingCustomQuestion
        from .booking_service import BookingService
        from .booking_staff_member import BookingStaffMember
        from .booking_staff_member_base import BookingStaffMemberBase
        from .browser_shared_cookie import BrowserSharedCookie
        from .browser_site import BrowserSite
        from .browser_site_list import BrowserSiteList
        from .building import Building
        from .building_map import BuildingMap
        from .built_in_identity_provider import BuiltInIdentityProvider
        from .bulk_upload import BulkUpload
        from .calendar import Calendar
        from .calendar_group import CalendarGroup
        from .calendar_permission import CalendarPermission
        from .calendar_sharing_message import CalendarSharingMessage
        from .call import Call
        from .call_ai_insight import CallAiInsight
        from .call_event import CallEvent
        from .call_recording import CallRecording
        from .call_records.call_record import CallRecord
        from .call_records.organizer import Organizer
        from .call_records.participant import Participant
        from .call_records.participant_base import ParticipantBase
        from .call_records.segment import Segment
        from .call_records.session import Session
        from .call_transcript import CallTranscript
        from .cancel_media_processing_operation import CancelMediaProcessingOperation
        from .canvas_layout import CanvasLayout
        from .certificate_authority_detail import CertificateAuthorityDetail
        from .certificate_based_auth_configuration import CertificateBasedAuthConfiguration
        from .certificate_based_auth_pki import CertificateBasedAuthPki
        from .change_tracked_entity import ChangeTrackedEntity
        from .channel import Channel
        from .chat import Chat
        from .chat_message import ChatMessage
        from .chat_message_hosted_content import ChatMessageHostedContent
        from .chat_message_info import ChatMessageInfo
        from .checklist_item import ChecklistItem
        from .claims_mapping_policy import ClaimsMappingPolicy
        from .cloud_clipboard_item import CloudClipboardItem
        from .cloud_clipboard_root import CloudClipboardRoot
        from .cloud_flare_web_application_firewall_provider import CloudFlareWebApplicationFirewallProvider
        from .cloud_pc_audit_event import CloudPcAuditEvent
        from .cloud_pc_device_image import CloudPcDeviceImage
        from .cloud_pc_gallery_image import CloudPcGalleryImage
        from .cloud_pc_on_premises_connection import CloudPcOnPremisesConnection
        from .cloud_pc_provisioning_policy import CloudPcProvisioningPolicy
        from .cloud_pc_provisioning_policy_assignment import CloudPcProvisioningPolicyAssignment
        from .cloud_pc_report import CloudPcReport
        from .cloud_pc_user_setting import CloudPcUserSetting
        from .cloud_pc_user_setting_assignment import CloudPcUserSettingAssignment
        from .cloud_p_c import CloudPC
        from .column_definition import ColumnDefinition
        from .column_link import ColumnLink
        from .comms_operation import CommsOperation
        from .community import Community
        from .company_subscription import CompanySubscription
        from .compliance_management_partner import ComplianceManagementPartner
        from .conditional_access_policy import ConditionalAccessPolicy
        from .conditional_access_root import ConditionalAccessRoot
        from .conditional_access_template import ConditionalAccessTemplate
        from .connected_organization import ConnectedOrganization
        from .contact import Contact
        from .contact_folder import ContactFolder
        from .content_activity import ContentActivity
        from .content_sharing_session import ContentSharingSession
        from .content_type import ContentType
        from .contract import Contract
        from .conversation import Conversation
        from .conversation_member import ConversationMember
        from .conversation_thread import ConversationThread
        from .copilot_admin import CopilotAdmin
        from .copilot_admin_limited_mode import CopilotAdminLimitedMode
        from .copilot_admin_setting import CopilotAdminSetting
        from .copilot_report_root import CopilotReportRoot
        from .country_named_location import CountryNamedLocation
        from .cross_tenant_access_policy import CrossTenantAccessPolicy
        from .cross_tenant_access_policy_configuration_default import CrossTenantAccessPolicyConfigurationDefault
        from .custom_authentication_extension import CustomAuthenticationExtension
        from .custom_callout_extension import CustomCalloutExtension
        from .custom_extension_stage_setting import CustomExtensionStageSetting
        from .custom_security_attribute_definition import CustomSecurityAttributeDefinition
        from .data_policy_operation import DataPolicyOperation
        from .data_security_and_governance import DataSecurityAndGovernance
        from .day_note import DayNote
        from .default_managed_app_protection import DefaultManagedAppProtection
        from .delegated_admin_access_assignment import DelegatedAdminAccessAssignment
        from .delegated_admin_customer import DelegatedAdminCustomer
        from .delegated_admin_relationship import DelegatedAdminRelationship
        from .delegated_admin_relationship_operation import DelegatedAdminRelationshipOperation
        from .delegated_admin_relationship_request import DelegatedAdminRelationshipRequest
        from .delegated_admin_service_management_detail import DelegatedAdminServiceManagementDetail
        from .delegated_permission_classification import DelegatedPermissionClassification
        from .deleted_chat import DeletedChat
        from .deleted_item_container import DeletedItemContainer
        from .deleted_team import DeletedTeam
        from .delta_participants import DeltaParticipants
        from .desk import Desk
        from .detected_app import DetectedApp
        from .device import Device
        from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
        from .device_and_app_management_role_definition import DeviceAndAppManagementRoleDefinition
        from .device_app_management import DeviceAppManagement
        from .device_category import DeviceCategory
        from .device_compliance_action_item import DeviceComplianceActionItem
        from .device_compliance_device_overview import DeviceComplianceDeviceOverview
        from .device_compliance_device_status import DeviceComplianceDeviceStatus
        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_compliance_policy_assignment import DeviceCompliancePolicyAssignment
        from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
        from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
        from .device_compliance_policy_state import DeviceCompliancePolicyState
        from .device_compliance_scheduled_action_for_rule import DeviceComplianceScheduledActionForRule
        from .device_compliance_setting_state import DeviceComplianceSettingState
        from .device_compliance_user_overview import DeviceComplianceUserOverview
        from .device_compliance_user_status import DeviceComplianceUserStatus
        from .device_configuration import DeviceConfiguration
        from .device_configuration_assignment import DeviceConfigurationAssignment
        from .device_configuration_device_overview import DeviceConfigurationDeviceOverview
        from .device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
        from .device_configuration_device_status import DeviceConfigurationDeviceStatus
        from .device_configuration_state import DeviceConfigurationState
        from .device_configuration_user_overview import DeviceConfigurationUserOverview
        from .device_configuration_user_status import DeviceConfigurationUserStatus
        from .device_enrollment_configuration import DeviceEnrollmentConfiguration
        from .device_enrollment_limit_configuration import DeviceEnrollmentLimitConfiguration
        from .device_enrollment_platform_restrictions_configuration import DeviceEnrollmentPlatformRestrictionsConfiguration
        from .device_enrollment_windows_hello_for_business_configuration import DeviceEnrollmentWindowsHelloForBusinessConfiguration
        from .device_install_state import DeviceInstallState
        from .device_local_credential_info import DeviceLocalCredentialInfo
        from .device_log_collection_response import DeviceLogCollectionResponse
        from .device_management import DeviceManagement
        from .device_management_cached_report_configuration import DeviceManagementCachedReportConfiguration
        from .device_management_exchange_connector import DeviceManagementExchangeConnector
        from .device_management_export_job import DeviceManagementExportJob
        from .device_management_partner import DeviceManagementPartner
        from .device_management_reports import DeviceManagementReports
        from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
        from .device_registration_policy import DeviceRegistrationPolicy
        from .directory import Directory
        from .directory_audit import DirectoryAudit
        from .directory_definition import DirectoryDefinition
        from .directory_object import DirectoryObject
        from .directory_object_partner_reference import DirectoryObjectPartnerReference
        from .directory_role import DirectoryRole
        from .directory_role_template import DirectoryRoleTemplate
        from .document_set_version import DocumentSetVersion
        from .domain import Domain
        from .domain_dns_cname_record import DomainDnsCnameRecord
        from .domain_dns_mx_record import DomainDnsMxRecord
        from .domain_dns_record import DomainDnsRecord
        from .domain_dns_srv_record import DomainDnsSrvRecord
        from .domain_dns_txt_record import DomainDnsTxtRecord
        from .domain_dns_unavailable_record import DomainDnsUnavailableRecord
        from .drive import Drive
        from .drive_item import DriveItem
        from .drive_item_version import DriveItemVersion
        from .drive_protection_rule import DriveProtectionRule
        from .drive_protection_unit import DriveProtectionUnit
        from .drive_protection_units_bulk_addition_job import DriveProtectionUnitsBulkAdditionJob
        from .drive_restore_artifact import DriveRestoreArtifact
        from .drive_restore_artifacts_bulk_addition_request import DriveRestoreArtifactsBulkAdditionRequest
        from .edge import Edge
        from .edition_upgrade_configuration import EditionUpgradeConfiguration
        from .education_assignment import EducationAssignment
        from .education_assignment_defaults import EducationAssignmentDefaults
        from .education_assignment_resource import EducationAssignmentResource
        from .education_assignment_settings import EducationAssignmentSettings
        from .education_category import EducationCategory
        from .education_class import EducationClass
        from .education_feedback_outcome import EducationFeedbackOutcome
        from .education_feedback_resource_outcome import EducationFeedbackResourceOutcome
        from .education_grading_category import EducationGradingCategory
        from .education_grading_scheme import EducationGradingScheme
        from .education_module import EducationModule
        from .education_module_resource import EducationModuleResource
        from .education_organization import EducationOrganization
        from .education_outcome import EducationOutcome
        from .education_points_outcome import EducationPointsOutcome
        from .education_rubric import EducationRubric
        from .education_rubric_outcome import EducationRubricOutcome
        from .education_school import EducationSchool
        from .education_submission import EducationSubmission
        from .education_submission_resource import EducationSubmissionResource
        from .education_user import EducationUser
        from .email_authentication_method import EmailAuthenticationMethod
        from .email_authentication_method_configuration import EmailAuthenticationMethodConfiguration
        from .email_file_assessment_request import EmailFileAssessmentRequest
        from .emergency_call_event import EmergencyCallEvent
        from .employee_experience_user import EmployeeExperienceUser
        from .endpoint import Endpoint
        from .end_user_notification import EndUserNotification
        from .end_user_notification_detail import EndUserNotificationDetail
        from .engagement_async_operation import EngagementAsyncOperation
        from .engagement_conversation import EngagementConversation
        from .engagement_conversation_discussion_message import EngagementConversationDiscussionMessage
        from .engagement_conversation_message import EngagementConversationMessage
        from .engagement_conversation_message_reaction import EngagementConversationMessageReaction
        from .engagement_conversation_question_message import EngagementConversationQuestionMessage
        from .engagement_conversation_system_message import EngagementConversationSystemMessage
        from .engagement_role import EngagementRole
        from .engagement_role_member import EngagementRoleMember
        from .enrollment_configuration_assignment import EnrollmentConfigurationAssignment
        from .enrollment_troubleshooting_event import EnrollmentTroubleshootingEvent
        from .enterprise_code_signing_certificate import EnterpriseCodeSigningCertificate
        from .entitlement_management import EntitlementManagement
        from .entitlement_management_settings import EntitlementManagementSettings
        from .event import Event
        from .event_message import EventMessage
        from .event_message_request import EventMessageRequest
        from .event_message_response import EventMessageResponse
        from .exchange_protection_policy import ExchangeProtectionPolicy
        from .exchange_restore_session import ExchangeRestoreSession
        from .extension import Extension
        from .extension_property import ExtensionProperty
        from .external_connectors.connection_operation import ConnectionOperation
        from .external_connectors.external_activity import ExternalActivity
        from .external_connectors.external_activity_result import ExternalActivityResult
        from .external_connectors.external_connection import ExternalConnection
        from .external_connectors.external_group import ExternalGroup
        from .external_connectors.external_item import ExternalItem
        from .external_connectors.identity import Identity
        from .external_connectors.schema import Schema
        from .external_domain_name import ExternalDomainName
        from .external_users_self_service_sign_up_events_flow import ExternalUsersSelfServiceSignUpEventsFlow
        from .e_book_install_summary import EBookInstallSummary
        from .feature_rollout_policy import FeatureRolloutPolicy
        from .federated_identity_credential import FederatedIdentityCredential
        from .fido2_authentication_method import Fido2AuthenticationMethod
        from .fido2_authentication_method_configuration import Fido2AuthenticationMethodConfiguration
        from .fido2_combination_configuration import Fido2CombinationConfiguration
        from .field_value_set import FieldValueSet
        from .file_assessment_request import FileAssessmentRequest
        from .file_attachment import FileAttachment
        from .file_storage import FileStorage
        from .file_storage_container import FileStorageContainer
        from .file_storage_container_type import FileStorageContainerType
        from .file_storage_container_type_registration import FileStorageContainerTypeRegistration
        from .filter_operator_schema import FilterOperatorSchema
        from .fixture_map import FixtureMap
        from .floor import Floor
        from .footprint_map import FootprintMap
        from .fraud_protection_provider import FraudProtectionProvider
        from .governance_insight import GovernanceInsight
        from .granular_mailbox_restore_artifact import GranularMailboxRestoreArtifact
        from .group import Group
        from .group_lifecycle_policy import GroupLifecyclePolicy
        from .group_setting import GroupSetting
        from .group_setting_template import GroupSettingTemplate
        from .home_realm_discovery_policy import HomeRealmDiscoveryPolicy
        from .horizontal_section import HorizontalSection
        from .horizontal_section_column import HorizontalSectionColumn
        from .human_security_fraud_protection_provider import HumanSecurityFraudProtectionProvider
        from .identity_api_connector import IdentityApiConnector
        from .identity_built_in_user_flow_attribute import IdentityBuiltInUserFlowAttribute
        from .identity_container import IdentityContainer
        from .identity_custom_user_flow_attribute import IdentityCustomUserFlowAttribute
        from .identity_governance.custom_task_extension import CustomTaskExtension
        from .identity_governance.insights import Insights
        from .identity_governance.lifecycle_management_settings import LifecycleManagementSettings
        from .identity_governance.lifecycle_workflows_container import LifecycleWorkflowsContainer
        from .identity_governance.run import Run
        from .identity_governance.task import Task
        from .identity_governance.task_definition import TaskDefinition
        from .identity_governance.task_processing_result import TaskProcessingResult
        from .identity_governance.task_report import TaskReport
        from .identity_governance.user_processing_result import UserProcessingResult
        from .identity_governance.workflow_template import WorkflowTemplate
        from .identity_provider import IdentityProvider
        from .identity_provider_base import IdentityProviderBase
        from .identity_security_defaults_enforcement_policy import IdentitySecurityDefaultsEnforcementPolicy
        from .identity_user_flow import IdentityUserFlow
        from .identity_user_flow_attribute import IdentityUserFlowAttribute
        from .identity_user_flow_attribute_assignment import IdentityUserFlowAttributeAssignment
        from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
        from .imported_windows_autopilot_device_identity_upload import ImportedWindowsAutopilotDeviceIdentityUpload
        from .inference_classification import InferenceClassification
        from .inference_classification_override import InferenceClassificationOverride
        from .insights_settings import InsightsSettings
        from .internal_domain_federation import InternalDomainFederation
        from .internet_explorer_mode import InternetExplorerMode
        from .invitation import Invitation
        from .invite_participants_operation import InviteParticipantsOperation
        from .iosi_pad_o_s_web_clip import IosiPadOSWebClip
        from .ios_certificate_profile import IosCertificateProfile
        from .ios_compliance_policy import IosCompliancePolicy
        from .ios_custom_configuration import IosCustomConfiguration
        from .ios_device_features_configuration import IosDeviceFeaturesConfiguration
        from .ios_general_device_configuration import IosGeneralDeviceConfiguration
        from .ios_lob_app import IosLobApp
        from .ios_lob_app_provisioning_configuration_assignment import IosLobAppProvisioningConfigurationAssignment
        from .ios_managed_app_protection import IosManagedAppProtection
        from .ios_managed_app_registration import IosManagedAppRegistration
        from .ios_mobile_app_configuration import IosMobileAppConfiguration
        from .ios_store_app import IosStoreApp
        from .ios_update_configuration import IosUpdateConfiguration
        from .ios_update_device_status import IosUpdateDeviceStatus
        from .ios_vpp_app import IosVppApp
        from .ios_vpp_e_book import IosVppEBook
        from .ios_vpp_e_book_assignment import IosVppEBookAssignment
        from .ip_named_location import IpNamedLocation
        from .item_activity import ItemActivity
        from .item_activity_stat import ItemActivityStat
        from .item_analytics import ItemAnalytics
        from .item_attachment import ItemAttachment
        from .item_insights import ItemInsights
        from .item_retention_label import ItemRetentionLabel
        from .label_content_right import LabelContentRight
        from .landing_page import LandingPage
        from .landing_page_detail import LandingPageDetail
        from .learning_assignment import LearningAssignment
        from .learning_content import LearningContent
        from .learning_course_activity import LearningCourseActivity
        from .learning_provider import LearningProvider
        from .learning_self_initiated_course import LearningSelfInitiatedCourse
        from .level_map import LevelMap
        from .license_details import LicenseDetails
        from .linked_resource import LinkedResource
        from .list_ import List_
        from .list_item import ListItem
        from .list_item_version import ListItemVersion
        from .localized_notification_message import LocalizedNotificationMessage
        from .login_page import LoginPage
        from .long_running_operation import LongRunningOperation
        from .m365_apps_installation_options import M365AppsInstallationOptions
        from .mac_o_s_compliance_policy import MacOSCompliancePolicy
        from .mac_o_s_custom_configuration import MacOSCustomConfiguration
        from .mac_o_s_device_features_configuration import MacOSDeviceFeaturesConfiguration
        from .mac_o_s_dmg_app import MacOSDmgApp
        from .mac_o_s_general_device_configuration import MacOSGeneralDeviceConfiguration
        from .mac_o_s_lob_app import MacOSLobApp
        from .mac_o_s_microsoft_defender_app import MacOSMicrosoftDefenderApp
        from .mac_o_s_microsoft_edge_app import MacOSMicrosoftEdgeApp
        from .mac_o_s_office_suite_app import MacOSOfficeSuiteApp
        from .mailbox_protection_rule import MailboxProtectionRule
        from .mailbox_protection_unit import MailboxProtectionUnit
        from .mailbox_protection_units_bulk_addition_job import MailboxProtectionUnitsBulkAdditionJob
        from .mailbox_restore_artifact import MailboxRestoreArtifact
        from .mailbox_restore_artifacts_bulk_addition_request import MailboxRestoreArtifactsBulkAdditionRequest
        from .mail_assessment_request import MailAssessmentRequest
        from .mail_folder import MailFolder
        from .mail_search_folder import MailSearchFolder
        from .malware_state_for_windows_device import MalwareStateForWindowsDevice
        from .managed_android_lob_app import ManagedAndroidLobApp
        from .managed_android_store_app import ManagedAndroidStoreApp
        from .managed_app import ManagedApp
        from .managed_app_configuration import ManagedAppConfiguration
        from .managed_app_operation import ManagedAppOperation
        from .managed_app_policy import ManagedAppPolicy
        from .managed_app_policy_deployment_summary import ManagedAppPolicyDeploymentSummary
        from .managed_app_protection import ManagedAppProtection
        from .managed_app_registration import ManagedAppRegistration
        from .managed_app_status import ManagedAppStatus
        from .managed_app_status_raw import ManagedAppStatusRaw
        from .managed_device import ManagedDevice
        from .managed_device_mobile_app_configuration import ManagedDeviceMobileAppConfiguration
        from .managed_device_mobile_app_configuration_assignment import ManagedDeviceMobileAppConfigurationAssignment
        from .managed_device_mobile_app_configuration_device_status import ManagedDeviceMobileAppConfigurationDeviceStatus
        from .managed_device_mobile_app_configuration_device_summary import ManagedDeviceMobileAppConfigurationDeviceSummary
        from .managed_device_mobile_app_configuration_user_status import ManagedDeviceMobileAppConfigurationUserStatus
        from .managed_device_mobile_app_configuration_user_summary import ManagedDeviceMobileAppConfigurationUserSummary
        from .managed_device_overview import ManagedDeviceOverview
        from .managed_e_book import ManagedEBook
        from .managed_e_book_assignment import ManagedEBookAssignment
        from .managed_i_o_s_lob_app import ManagedIOSLobApp
        from .managed_i_o_s_store_app import ManagedIOSStoreApp
        from .managed_mobile_app import ManagedMobileApp
        from .managed_mobile_lob_app import ManagedMobileLobApp
        from .mdm_windows_information_protection_policy import MdmWindowsInformationProtectionPolicy
        from .meeting_attendance_report import MeetingAttendanceReport
        from .membership_outlier_insight import MembershipOutlierInsight
        from .message import Message
        from .message_rule import MessageRule
        from .microsoft_account_user_conversation_member import MicrosoftAccountUserConversationMember
        from .microsoft_authenticator_authentication_method import MicrosoftAuthenticatorAuthenticationMethod
        from .microsoft_authenticator_authentication_method_configuration import MicrosoftAuthenticatorAuthenticationMethodConfiguration
        from .microsoft_authenticator_authentication_method_target import MicrosoftAuthenticatorAuthenticationMethodTarget
        from .microsoft_store_for_business_app import MicrosoftStoreForBusinessApp
        from .mobile_app import MobileApp
        from .mobile_app_assignment import MobileAppAssignment
        from .mobile_app_category import MobileAppCategory
        from .mobile_app_content import MobileAppContent
        from .mobile_app_content_file import MobileAppContentFile
        from .mobile_app_relationship import MobileAppRelationship
        from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
        from .mobile_contained_app import MobileContainedApp
        from .mobile_lob_app import MobileLobApp
        from .mobile_threat_defense_connector import MobileThreatDefenseConnector
        from .multi_tenant_organization import MultiTenantOrganization
        from .multi_tenant_organization_identity_sync_policy_template import MultiTenantOrganizationIdentitySyncPolicyTemplate
        from .multi_tenant_organization_join_request_record import MultiTenantOrganizationJoinRequestRecord
        from .multi_tenant_organization_member import MultiTenantOrganizationMember
        from .multi_tenant_organization_partner_configuration_template import MultiTenantOrganizationPartnerConfigurationTemplate
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .mute_participant_operation import MuteParticipantOperation
        from .named_location import NamedLocation
        from .notebook import Notebook
        from .notification_message_template import NotificationMessageTemplate
        from .offer_shift_request import OfferShiftRequest
        from .office_graph_insights import OfficeGraphInsights
        from .onenote import Onenote
        from .onenote_entity_base_model import OnenoteEntityBaseModel
        from .onenote_entity_hierarchy_model import OnenoteEntityHierarchyModel
        from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
        from .onenote_operation import OnenoteOperation
        from .onenote_page import OnenotePage
        from .onenote_resource import OnenoteResource
        from .onenote_section import OnenoteSection
        from .one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
        from .one_drive_for_business_restore_session import OneDriveForBusinessRestoreSession
        from .online_meeting import OnlineMeeting
        from .online_meeting_base import OnlineMeetingBase
        from .online_meeting_engagement_conversation import OnlineMeetingEngagementConversation
        from .on_attribute_collection_listener import OnAttributeCollectionListener
        from .on_attribute_collection_start_custom_extension import OnAttributeCollectionStartCustomExtension
        from .on_attribute_collection_start_listener import OnAttributeCollectionStartListener
        from .on_attribute_collection_submit_custom_extension import OnAttributeCollectionSubmitCustomExtension
        from .on_attribute_collection_submit_listener import OnAttributeCollectionSubmitListener
        from .on_authentication_method_load_start_listener import OnAuthenticationMethodLoadStartListener
        from .on_email_otp_send_listener import OnEmailOtpSendListener
        from .on_fraud_protection_load_start_listener import OnFraudProtectionLoadStartListener
        from .on_interactive_auth_flow_start_listener import OnInteractiveAuthFlowStartListener
        from .on_otp_send_custom_extension import OnOtpSendCustomExtension
        from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
        from .on_premises_directory_synchronization import OnPremisesDirectorySynchronization
        from .on_premises_sync_behavior import OnPremisesSyncBehavior
        from .on_token_issuance_start_custom_extension import OnTokenIssuanceStartCustomExtension
        from .on_token_issuance_start_listener import OnTokenIssuanceStartListener
        from .on_user_create_start_listener import OnUserCreateStartListener
        from .open_shift import OpenShift
        from .open_shift_change_request import OpenShiftChangeRequest
        from .open_type_extension import OpenTypeExtension
        from .operation import Operation
        from .organization import Organization
        from .organizational_branding import OrganizationalBranding
        from .organizational_branding_localization import OrganizationalBrandingLocalization
        from .organizational_branding_properties import OrganizationalBrandingProperties
        from .org_contact import OrgContact
        from .outlook_category import OutlookCategory
        from .outlook_item import OutlookItem
        from .outlook_user import OutlookUser
        from .o_auth2_permission_grant import OAuth2PermissionGrant
        from .participant import Participant
        from .participant_joining_notification import ParticipantJoiningNotification
        from .participant_left_notification import ParticipantLeftNotification
        from .partners.billing.azure_usage import AzureUsage
        from .partners.billing.billed_reconciliation import BilledReconciliation
        from .partners.billing.billed_usage import BilledUsage
        from .partners.billing.billing import Billing
        from .partners.billing.billing_reconciliation import BillingReconciliation
        from .partners.billing.export_success_operation import ExportSuccessOperation
        from .partners.billing.failed_operation import FailedOperation
        from .partners.billing.manifest import Manifest
        from .partners.billing.operation import Operation
        from .partners.billing.running_operation import RunningOperation
        from .partners.billing.unbilled_reconciliation import UnbilledReconciliation
        from .partners.billing.unbilled_usage import UnbilledUsage
        from .partners.partners import Partners
        from .password_authentication_method import PasswordAuthenticationMethod
        from .payload import Payload
        from .people_admin_settings import PeopleAdminSettings
        from .permission import Permission
        from .permission_grant_condition_set import PermissionGrantConditionSet
        from .permission_grant_policy import PermissionGrantPolicy
        from .person import Person
        from .phone_authentication_method import PhoneAuthenticationMethod
        from .phone_user_conversation_member import PhoneUserConversationMember
        from .pinned_chat_message_info import PinnedChatMessageInfo
        from .place import Place
        from .planner import Planner
        from .planner_assigned_to_task_board_task_format import PlannerAssignedToTaskBoardTaskFormat
        from .planner_bucket import PlannerBucket
        from .planner_bucket_task_board_task_format import PlannerBucketTaskBoardTaskFormat
        from .planner_group import PlannerGroup
        from .planner_plan import PlannerPlan
        from .planner_plan_details import PlannerPlanDetails
        from .planner_progress_task_board_task_format import PlannerProgressTaskBoardTaskFormat
        from .planner_task import PlannerTask
        from .planner_task_details import PlannerTaskDetails
        from .planner_user import PlannerUser
        from .platform_credential_authentication_method import PlatformCredentialAuthenticationMethod
        from .play_prompt_operation import PlayPromptOperation
        from .policy_base import PolicyBase
        from .policy_root import PolicyRoot
        from .policy_template import PolicyTemplate
        from .post import Post
        from .presence import Presence
        from .printer import Printer
        from .printer_base import PrinterBase
        from .printer_create_operation import PrinterCreateOperation
        from .printer_share import PrinterShare
        from .print_connector import PrintConnector
        from .print_document import PrintDocument
        from .print_job import PrintJob
        from .print_operation import PrintOperation
        from .print_service import PrintService
        from .print_service_endpoint import PrintServiceEndpoint
        from .print_task import PrintTask
        from .print_task_definition import PrintTaskDefinition
        from .print_task_trigger import PrintTaskTrigger
        from .print_usage import PrintUsage
        from .print_usage_by_printer import PrintUsageByPrinter
        from .print_usage_by_user import PrintUsageByUser
        from .privileged_access_group import PrivilegedAccessGroup
        from .privileged_access_group_assignment_schedule import PrivilegedAccessGroupAssignmentSchedule
        from .privileged_access_group_assignment_schedule_instance import PrivilegedAccessGroupAssignmentScheduleInstance
        from .privileged_access_group_assignment_schedule_request import PrivilegedAccessGroupAssignmentScheduleRequest
        from .privileged_access_group_eligibility_schedule import PrivilegedAccessGroupEligibilitySchedule
        from .privileged_access_group_eligibility_schedule_instance import PrivilegedAccessGroupEligibilityScheduleInstance
        from .privileged_access_group_eligibility_schedule_request import PrivilegedAccessGroupEligibilityScheduleRequest
        from .privileged_access_root import PrivilegedAccessRoot
        from .privileged_access_schedule import PrivilegedAccessSchedule
        from .privileged_access_schedule_instance import PrivilegedAccessScheduleInstance
        from .privileged_access_schedule_request import PrivilegedAccessScheduleRequest
        from .profile_card_property import ProfileCardProperty
        from .profile_photo import ProfilePhoto
        from .pronouns_settings import PronounsSettings
        from .protection_policy_base import ProtectionPolicyBase
        from .protection_rule_base import ProtectionRuleBase
        from .protection_units_bulk_job_base import ProtectionUnitsBulkJobBase
        from .protection_unit_base import ProtectionUnitBase
        from .provisioning_object_summary import ProvisioningObjectSummary
        from .public_key_infrastructure_root import PublicKeyInfrastructureRoot
        from .rbac_application import RbacApplication
        from .reading_assignment_submission import ReadingAssignmentSubmission
        from .reading_coach_passage import ReadingCoachPassage
        from .record_operation import RecordOperation
        from .recycle_bin import RecycleBin
        from .recycle_bin_item import RecycleBinItem
        from .reference_attachment import ReferenceAttachment
        from .reflect_check_in_response import ReflectCheckInResponse
        from .relying_party_detailed_summary import RelyingPartyDetailedSummary
        from .remote_assistance_partner import RemoteAssistancePartner
        from .remote_desktop_security_configuration import RemoteDesktopSecurityConfiguration
        from .reports_root import ReportsRoot
        from .request import Request
        from .reseller_delegated_admin_relationship import ResellerDelegatedAdminRelationship
        from .resource_operation import ResourceOperation
        from .resource_specific_permission_grant import ResourceSpecificPermissionGrant
        from .restore_artifacts_bulk_request_base import RestoreArtifactsBulkRequestBase
        from .restore_artifact_base import RestoreArtifactBase
        from .restore_point import RestorePoint
        from .restore_session_base import RestoreSessionBase
        from .rich_long_running_operation import RichLongRunningOperation
        from .risky_service_principal import RiskyServicePrincipal
        from .risky_service_principal_history_item import RiskyServicePrincipalHistoryItem
        from .risky_user import RiskyUser
        from .risky_user_history_item import RiskyUserHistoryItem
        from .risk_detection import RiskDetection
        from .role_assignment import RoleAssignment
        from .role_definition import RoleDefinition
        from .room import Room
        from .room_list import RoomList
        from .saml_or_ws_fed_external_domain_federation import SamlOrWsFedExternalDomainFederation
        from .saml_or_ws_fed_provider import SamlOrWsFedProvider
        from .schedule import Schedule
        from .schedule_change_request import ScheduleChangeRequest
        from .scheduling_group import SchedulingGroup
        from .schema_extension import SchemaExtension
        from .scoped_role_membership import ScopedRoleMembership
        from .search.acronym import Acronym
        from .search.bookmark import Bookmark
        from .search.qna import Qna
        from .search.search_answer import SearchAnswer
        from .search_entity import SearchEntity
        from .section import Section
        from .section_group import SectionGroup
        from .section_map import SectionMap
        from .secure_score import SecureScore
        from .secure_score_control_profile import SecureScoreControlProfile
        from .security.alert import Alert
        from .security.article import Article
        from .security.article_indicator import ArticleIndicator
        from .security.artifact import Artifact
        from .security.authority_template import AuthorityTemplate
        from .security.case import Case
        from .security.cases_root import CasesRoot
        from .security.case_operation import CaseOperation
        from .security.category_template import CategoryTemplate
        from .security.citation_template import CitationTemplate
        from .security.data_set import DataSet
        from .security.data_source import DataSource
        from .security.data_source_container import DataSourceContainer
        from .security.department_template import DepartmentTemplate
        from .security.disposition_review_stage import DispositionReviewStage
        from .security.ediscovery_add_to_review_set_operation import EdiscoveryAddToReviewSetOperation
        from .security.ediscovery_case import EdiscoveryCase
        from .security.ediscovery_case_member import EdiscoveryCaseMember
        from .security.ediscovery_case_settings import EdiscoveryCaseSettings
        from .security.ediscovery_custodian import EdiscoveryCustodian
        from .security.ediscovery_estimate_operation import EdiscoveryEstimateOperation
        from .security.ediscovery_export_operation import EdiscoveryExportOperation
        from .security.ediscovery_hold_operation import EdiscoveryHoldOperation
        from .security.ediscovery_hold_policy_sync_operation import EdiscoveryHoldPolicySyncOperation
        from .security.ediscovery_index_operation import EdiscoveryIndexOperation
        from .security.ediscovery_noncustodial_data_source import EdiscoveryNoncustodialDataSource
        from .security.ediscovery_purge_data_operation import EdiscoveryPurgeDataOperation
        from .security.ediscovery_review_set import EdiscoveryReviewSet
        from .security.ediscovery_review_set_query import EdiscoveryReviewSetQuery
        from .security.ediscovery_review_tag import EdiscoveryReviewTag
        from .security.ediscovery_search import EdiscoverySearch
        from .security.ediscovery_search_export_operation import EdiscoverySearchExportOperation
        from .security.ediscovery_tag_operation import EdiscoveryTagOperation
        from .security.file_plan_descriptor import FilePlanDescriptor
        from .security.file_plan_descriptor_template import FilePlanDescriptorTemplate
        from .security.file_plan_reference_template import FilePlanReferenceTemplate
        from .security.health_issue import HealthIssue
        from .security.host import Host
        from .security.hostname import Hostname
        from .security.host_component import HostComponent
        from .security.host_cookie import HostCookie
        from .security.host_pair import HostPair
        from .security.host_port import HostPort
        from .security.host_reputation import HostReputation
        from .security.host_ssl_certificate import HostSslCertificate
        from .security.host_tracker import HostTracker
        from .security.identity_accounts import IdentityAccounts
        from .security.identity_container import IdentityContainer
        from .security.incident import Incident
        from .security.indicator import Indicator
        from .security.intelligence_profile import IntelligenceProfile
        from .security.intelligence_profile_indicator import IntelligenceProfileIndicator
        from .security.ip_address import IpAddress
        from .security.labels_root import LabelsRoot
        from .security.network_adapter import NetworkAdapter
        from .security.passive_dns_record import PassiveDnsRecord
        from .security.retention_event import RetentionEvent
        from .security.retention_event_type import RetentionEventType
        from .security.retention_label import RetentionLabel
        from .security.search import Search
        from .security.security import Security
        from .security.sensor import Sensor
        from .security.sensor_candidate import SensorCandidate
        from .security.sensor_candidate_activation_configuration import SensorCandidateActivationConfiguration
        from .security.site_source import SiteSource
        from .security.ssl_certificate import SslCertificate
        from .security.subcategory_template import SubcategoryTemplate
        from .security.subdomain import Subdomain
        from .security.tag import Tag
        from .security.threat_intelligence import ThreatIntelligence
        from .security.triggers_root import TriggersRoot
        from .security.trigger_types_root import TriggerTypesRoot
        from .security.unclassified_artifact import UnclassifiedArtifact
        from .security.unified_group_source import UnifiedGroupSource
        from .security.user import User
        from .security.user_source import UserSource
        from .security.vulnerability import Vulnerability
        from .security.vulnerability_component import VulnerabilityComponent
        from .security.whois_base_record import WhoisBaseRecord
        from .security.whois_history_record import WhoisHistoryRecord
        from .security.whois_record import WhoisRecord
        from .security_reports_root import SecurityReportsRoot
        from .send_dtmf_tones_operation import SendDtmfTonesOperation
        from .sensitivity_label import SensitivityLabel
        from .service_announcement import ServiceAnnouncement
        from .service_announcement_attachment import ServiceAnnouncementAttachment
        from .service_announcement_base import ServiceAnnouncementBase
        from .service_app import ServiceApp
        from .service_health import ServiceHealth
        from .service_health_issue import ServiceHealthIssue
        from .service_principal import ServicePrincipal
        from .service_principal_risk_detection import ServicePrincipalRiskDetection
        from .service_storage_quota_breakdown import ServiceStorageQuotaBreakdown
        from .service_update_message import ServiceUpdateMessage
        from .setting_state_device_summary import SettingStateDeviceSummary
        from .shared_drive_item import SharedDriveItem
        from .shared_insight import SharedInsight
        from .shared_p_c_configuration import SharedPCConfiguration
        from .shared_with_channel_team_info import SharedWithChannelTeamInfo
        from .sharepoint import Sharepoint
        from .sharepoint_settings import SharepointSettings
        from .share_point_migration_event import SharePointMigrationEvent
        from .share_point_migration_finish_manifest_file_upload_event import SharePointMigrationFinishManifestFileUploadEvent
        from .share_point_migration_job import SharePointMigrationJob
        from .share_point_migration_job_cancelled_event import SharePointMigrationJobCancelledEvent
        from .share_point_migration_job_deleted_event import SharePointMigrationJobDeletedEvent
        from .share_point_migration_job_error_event import SharePointMigrationJobErrorEvent
        from .share_point_migration_job_postponed_event import SharePointMigrationJobPostponedEvent
        from .share_point_migration_job_progress_event import SharePointMigrationJobProgressEvent
        from .share_point_migration_job_queued_event import SharePointMigrationJobQueuedEvent
        from .share_point_migration_job_start_event import SharePointMigrationJobStartEvent
        from .share_point_protection_policy import SharePointProtectionPolicy
        from .share_point_restore_session import SharePointRestoreSession
        from .shift import Shift
        from .shift_preferences import ShiftPreferences
        from .sign_in import SignIn
        from .simulation import Simulation
        from .simulation_automation import SimulationAutomation
        from .simulation_automation_run import SimulationAutomationRun
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
        from .site import Site
        from .site_page import SitePage
        from .site_protection_rule import SiteProtectionRule
        from .site_protection_unit import SiteProtectionUnit
        from .site_protection_units_bulk_addition_job import SiteProtectionUnitsBulkAdditionJob
        from .site_restore_artifact import SiteRestoreArtifact
        from .site_restore_artifacts_bulk_addition_request import SiteRestoreArtifactsBulkAdditionRequest
        from .skype_for_business_user_conversation_member import SkypeForBusinessUserConversationMember
        from .skype_user_conversation_member import SkypeUserConversationMember
        from .sms_authentication_method_configuration import SmsAuthenticationMethodConfiguration
        from .sms_authentication_method_target import SmsAuthenticationMethodTarget
        from .social_identity_provider import SocialIdentityProvider
        from .software_oath_authentication_method import SoftwareOathAuthenticationMethod
        from .software_oath_authentication_method_configuration import SoftwareOathAuthenticationMethodConfiguration
        from .software_update_status_summary import SoftwareUpdateStatusSummary
        from .speaker_assignment_submission import SpeakerAssignmentSubmission
        from .standard_web_part import StandardWebPart
        from .start_hold_music_operation import StartHoldMusicOperation
        from .stop_hold_music_operation import StopHoldMusicOperation
        from .storage_quota_breakdown import StorageQuotaBreakdown
        from .storage_settings import StorageSettings
        from .sts_policy import StsPolicy
        from .subject_rights_request import SubjectRightsRequest
        from .subscribed_sku import SubscribedSku
        from .subscribe_to_tone_operation import SubscribeToToneOperation
        from .subscription import Subscription
        from .swap_shifts_change_request import SwapShiftsChangeRequest
        from .synchronization import Synchronization
        from .synchronization_job import SynchronizationJob
        from .synchronization_schema import SynchronizationSchema
        from .synchronization_template import SynchronizationTemplate
        from .targeted_managed_app_configuration import TargetedManagedAppConfiguration
        from .targeted_managed_app_policy_assignment import TargetedManagedAppPolicyAssignment
        from .targeted_managed_app_protection import TargetedManagedAppProtection
        from .target_device_group import TargetDeviceGroup
        from .task_file_attachment import TaskFileAttachment
        from .team import Team
        from .teams_administration.teams_admin_root import TeamsAdminRoot
        from .teams_administration.teams_user_configuration import TeamsUserConfiguration
        from .teams_app import TeamsApp
        from .teams_app_definition import TeamsAppDefinition
        from .teams_app_installation import TeamsAppInstallation
        from .teams_app_settings import TeamsAppSettings
        from .teams_async_operation import TeamsAsyncOperation
        from .teams_tab import TeamsTab
        from .teams_template import TeamsTemplate
        from .teamwork import Teamwork
        from .teamwork_bot import TeamworkBot
        from .teamwork_hosted_content import TeamworkHostedContent
        from .teamwork_tag import TeamworkTag
        from .teamwork_tag_member import TeamworkTagMember
        from .team_info import TeamInfo
        from .temporary_access_pass_authentication_method import TemporaryAccessPassAuthenticationMethod
        from .temporary_access_pass_authentication_method_configuration import TemporaryAccessPassAuthenticationMethodConfiguration
        from .tenant_app_management_policy import TenantAppManagementPolicy
        from .tenant_data_security_and_governance import TenantDataSecurityAndGovernance
        from .tenant_protection_scope_container import TenantProtectionScopeContainer
        from .terms_and_conditions import TermsAndConditions
        from .terms_and_conditions_acceptance_status import TermsAndConditionsAcceptanceStatus
        from .terms_and_conditions_assignment import TermsAndConditionsAssignment
        from .terms_of_use_container import TermsOfUseContainer
        from .term_store.group import Group
        from .term_store.relation import Relation
        from .term_store.set import Set
        from .term_store.store import Store
        from .term_store.term import Term
        from .text_web_part import TextWebPart
        from .threat_assessment_request import ThreatAssessmentRequest
        from .threat_assessment_result import ThreatAssessmentResult
        from .thumbnail_set import ThumbnailSet
        from .time_card import TimeCard
        from .time_off import TimeOff
        from .time_off_reason import TimeOffReason
        from .time_off_request import TimeOffRequest
        from .todo import Todo
        from .todo_task import TodoTask
        from .todo_task_list import TodoTaskList
        from .token_issuance_policy import TokenIssuancePolicy
        from .token_lifetime_policy import TokenLifetimePolicy
        from .training import Training
        from .training_language_detail import TrainingLanguageDetail
        from .trending import Trending
        from .unified_rbac_resource_action import UnifiedRbacResourceAction
        from .unified_rbac_resource_namespace import UnifiedRbacResourceNamespace
        from .unified_role_assignment import UnifiedRoleAssignment
        from .unified_role_assignment_schedule import UnifiedRoleAssignmentSchedule
        from .unified_role_assignment_schedule_instance import UnifiedRoleAssignmentScheduleInstance
        from .unified_role_assignment_schedule_request import UnifiedRoleAssignmentScheduleRequest
        from .unified_role_definition import UnifiedRoleDefinition
        from .unified_role_eligibility_schedule import UnifiedRoleEligibilitySchedule
        from .unified_role_eligibility_schedule_instance import UnifiedRoleEligibilityScheduleInstance
        from .unified_role_eligibility_schedule_request import UnifiedRoleEligibilityScheduleRequest
        from .unified_role_management_policy import UnifiedRoleManagementPolicy
        from .unified_role_management_policy_approval_rule import UnifiedRoleManagementPolicyApprovalRule
        from .unified_role_management_policy_assignment import UnifiedRoleManagementPolicyAssignment
        from .unified_role_management_policy_authentication_context_rule import UnifiedRoleManagementPolicyAuthenticationContextRule
        from .unified_role_management_policy_enablement_rule import UnifiedRoleManagementPolicyEnablementRule
        from .unified_role_management_policy_expiration_rule import UnifiedRoleManagementPolicyExpirationRule
        from .unified_role_management_policy_notification_rule import UnifiedRoleManagementPolicyNotificationRule
        from .unified_role_management_policy_rule import UnifiedRoleManagementPolicyRule
        from .unified_role_schedule_base import UnifiedRoleScheduleBase
        from .unified_role_schedule_instance_base import UnifiedRoleScheduleInstanceBase
        from .unified_storage_quota import UnifiedStorageQuota
        from .unit_map import UnitMap
        from .unmute_participant_operation import UnmuteParticipantOperation
        from .update_recording_status_operation import UpdateRecordingStatusOperation
        from .url_assessment_request import UrlAssessmentRequest
        from .usage_rights_included import UsageRightsIncluded
        from .used_insight import UsedInsight
        from .user import User
        from .user_activity import UserActivity
        from .user_consent_request import UserConsentRequest
        from .user_data_security_and_governance import UserDataSecurityAndGovernance
        from .user_experience_analytics_app_health_application_performance import UserExperienceAnalyticsAppHealthApplicationPerformance
        from .user_experience_analytics_app_health_app_performance_by_app_version_details import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails
        from .user_experience_analytics_app_health_app_performance_by_app_version_device_id import UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId
        from .user_experience_analytics_app_health_app_performance_by_o_s_version import UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion
        from .user_experience_analytics_app_health_device_model_performance import UserExperienceAnalyticsAppHealthDeviceModelPerformance
        from .user_experience_analytics_app_health_device_performance import UserExperienceAnalyticsAppHealthDevicePerformance
        from .user_experience_analytics_app_health_device_performance_details import UserExperienceAnalyticsAppHealthDevicePerformanceDetails
        from .user_experience_analytics_app_health_o_s_version_performance import UserExperienceAnalyticsAppHealthOSVersionPerformance
        from .user_experience_analytics_baseline import UserExperienceAnalyticsBaseline
        from .user_experience_analytics_category import UserExperienceAnalyticsCategory
        from .user_experience_analytics_device_performance import UserExperienceAnalyticsDevicePerformance
        from .user_experience_analytics_device_scores import UserExperienceAnalyticsDeviceScores
        from .user_experience_analytics_device_startup_history import UserExperienceAnalyticsDeviceStartupHistory
        from .user_experience_analytics_device_startup_process import UserExperienceAnalyticsDeviceStartupProcess
        from .user_experience_analytics_device_startup_process_performance import UserExperienceAnalyticsDeviceStartupProcessPerformance
        from .user_experience_analytics_metric import UserExperienceAnalyticsMetric
        from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
        from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
        from .user_experience_analytics_overview import UserExperienceAnalyticsOverview
        from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory
        from .user_experience_analytics_work_from_anywhere_device import UserExperienceAnalyticsWorkFromAnywhereDevice
        from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
        from .user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
        from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance
        from .user_flow_language_configuration import UserFlowLanguageConfiguration
        from .user_flow_language_page import UserFlowLanguagePage
        from .user_insights_settings import UserInsightsSettings
        from .user_install_state_summary import UserInstallStateSummary
        from .user_protection_scope_container import UserProtectionScopeContainer
        from .user_registration_details import UserRegistrationDetails
        from .user_scope_teams_app_installation import UserScopeTeamsAppInstallation
        from .user_settings import UserSettings
        from .user_sign_in_insight import UserSignInInsight
        from .user_solution_root import UserSolutionRoot
        from .user_storage import UserStorage
        from .user_teamwork import UserTeamwork
        from .vertical_section import VerticalSection
        from .virtual_endpoint import VirtualEndpoint
        from .virtual_event import VirtualEvent
        from .virtual_events_root import VirtualEventsRoot
        from .virtual_event_presenter import VirtualEventPresenter
        from .virtual_event_registration import VirtualEventRegistration
        from .virtual_event_registration_configuration import VirtualEventRegistrationConfiguration
        from .virtual_event_registration_custom_question import VirtualEventRegistrationCustomQuestion
        from .virtual_event_registration_predefined_question import VirtualEventRegistrationPredefinedQuestion
        from .virtual_event_registration_question_base import VirtualEventRegistrationQuestionBase
        from .virtual_event_session import VirtualEventSession
        from .virtual_event_townhall import VirtualEventTownhall
        from .virtual_event_webinar import VirtualEventWebinar
        from .virtual_event_webinar_registration_configuration import VirtualEventWebinarRegistrationConfiguration
        from .voice_authentication_method_configuration import VoiceAuthenticationMethodConfiguration
        from .vpp_token import VppToken
        from .web_app import WebApp
        from .web_application_firewall_provider import WebApplicationFirewallProvider
        from .web_application_firewall_verification_model import WebApplicationFirewallVerificationModel
        from .web_part import WebPart
        from .what_if_analysis_result import WhatIfAnalysisResult
        from .win32_lob_app import Win32LobApp
        from .windows10_compliance_policy import Windows10CompliancePolicy
        from .windows10_custom_configuration import Windows10CustomConfiguration
        from .windows10_endpoint_protection_configuration import Windows10EndpointProtectionConfiguration
        from .windows10_enrollment_completion_page_configuration import Windows10EnrollmentCompletionPageConfiguration
        from .windows10_enterprise_modern_app_management_configuration import Windows10EnterpriseModernAppManagementConfiguration
        from .windows10_general_configuration import Windows10GeneralConfiguration
        from .windows10_mobile_compliance_policy import Windows10MobileCompliancePolicy
        from .windows10_secure_assessment_configuration import Windows10SecureAssessmentConfiguration
        from .windows10_team_general_configuration import Windows10TeamGeneralConfiguration
        from .windows81_compliance_policy import Windows81CompliancePolicy
        from .windows81_general_configuration import Windows81GeneralConfiguration
        from .windows_app_x import WindowsAppX
        from .windows_autopilot_deployment_profile import WindowsAutopilotDeploymentProfile
        from .windows_autopilot_deployment_profile_assignment import WindowsAutopilotDeploymentProfileAssignment
        from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
        from .windows_defender_advanced_threat_protection_configuration import WindowsDefenderAdvancedThreatProtectionConfiguration
        from .windows_device_malware_state import WindowsDeviceMalwareState
        from .windows_hello_for_business_authentication_method import WindowsHelloForBusinessAuthenticationMethod
        from .windows_information_protection import WindowsInformationProtection
        from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
        from .windows_information_protection_app_locker_file import WindowsInformationProtectionAppLockerFile
        from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
        from .windows_information_protection_policy import WindowsInformationProtectionPolicy
        from .windows_malware_information import WindowsMalwareInformation
        from .windows_microsoft_edge_app import WindowsMicrosoftEdgeApp
        from .windows_mobile_m_s_i import WindowsMobileMSI
        from .windows_phone81_compliance_policy import WindowsPhone81CompliancePolicy
        from .windows_phone81_custom_configuration import WindowsPhone81CustomConfiguration
        from .windows_phone81_general_configuration import WindowsPhone81GeneralConfiguration
        from .windows_protection_state import WindowsProtectionState
        from .windows_setting import WindowsSetting
        from .windows_setting_instance import WindowsSettingInstance
        from .windows_universal_app_x import WindowsUniversalAppX
        from .windows_universal_app_x_contained_app import WindowsUniversalAppXContainedApp
        from .windows_update_for_business_configuration import WindowsUpdateForBusinessConfiguration
        from .windows_web_app import WindowsWebApp
        from .workbook import Workbook
        from .workbook_application import WorkbookApplication
        from .workbook_chart import WorkbookChart
        from .workbook_chart_area_format import WorkbookChartAreaFormat
        from .workbook_chart_axes import WorkbookChartAxes
        from .workbook_chart_axis import WorkbookChartAxis
        from .workbook_chart_axis_format import WorkbookChartAxisFormat
        from .workbook_chart_axis_title import WorkbookChartAxisTitle
        from .workbook_chart_axis_title_format import WorkbookChartAxisTitleFormat
        from .workbook_chart_data_labels import WorkbookChartDataLabels
        from .workbook_chart_data_label_format import WorkbookChartDataLabelFormat
        from .workbook_chart_fill import WorkbookChartFill
        from .workbook_chart_font import WorkbookChartFont
        from .workbook_chart_gridlines import WorkbookChartGridlines
        from .workbook_chart_gridlines_format import WorkbookChartGridlinesFormat
        from .workbook_chart_legend import WorkbookChartLegend
        from .workbook_chart_legend_format import WorkbookChartLegendFormat
        from .workbook_chart_line_format import WorkbookChartLineFormat
        from .workbook_chart_point import WorkbookChartPoint
        from .workbook_chart_point_format import WorkbookChartPointFormat
        from .workbook_chart_series import WorkbookChartSeries
        from .workbook_chart_series_format import WorkbookChartSeriesFormat
        from .workbook_chart_title import WorkbookChartTitle
        from .workbook_chart_title_format import WorkbookChartTitleFormat
        from .workbook_comment import WorkbookComment
        from .workbook_comment_reply import WorkbookCommentReply
        from .workbook_filter import WorkbookFilter
        from .workbook_format_protection import WorkbookFormatProtection
        from .workbook_functions import WorkbookFunctions
        from .workbook_function_result import WorkbookFunctionResult
        from .workbook_named_item import WorkbookNamedItem
        from .workbook_operation import WorkbookOperation
        from .workbook_pivot_table import WorkbookPivotTable
        from .workbook_range import WorkbookRange
        from .workbook_range_border import WorkbookRangeBorder
        from .workbook_range_fill import WorkbookRangeFill
        from .workbook_range_font import WorkbookRangeFont
        from .workbook_range_format import WorkbookRangeFormat
        from .workbook_range_sort import WorkbookRangeSort
        from .workbook_range_view import WorkbookRangeView
        from .workbook_table import WorkbookTable
        from .workbook_table_column import WorkbookTableColumn
        from .workbook_table_row import WorkbookTableRow
        from .workbook_table_sort import WorkbookTableSort
        from .workbook_worksheet import WorkbookWorksheet
        from .workbook_worksheet_protection import WorkbookWorksheetProtection
        from .workforce_integration import WorkforceIntegration
        from .working_time_schedule import WorkingTimeSchedule
        from .workspace import Workspace
        from .work_hours_and_locations_setting import WorkHoursAndLocationsSetting
        from .work_plan_occurrence import WorkPlanOccurrence
        from .work_plan_recurrence import WorkPlanRecurrence
        from .x509_certificate_authentication_method_configuration import X509CertificateAuthenticationMethodConfiguration
        from .x509_certificate_combination_configuration import X509CertificateCombinationConfiguration

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

