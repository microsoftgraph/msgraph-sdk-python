from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .apple_push_notification_certificate import ApplePushNotificationCertificate
    from .audit_event import AuditEvent
    from .compliance_management_partner import ComplianceManagementPartner
    from .detected_app import DetectedApp
    from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
    from .device_category import DeviceCategory
    from .device_compliance_policy import DeviceCompliancePolicy
    from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
    from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
    from .device_configuration import DeviceConfiguration
    from .device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
    from .device_enrollment_configuration import DeviceEnrollmentConfiguration
    from .device_management_exchange_connector import DeviceManagementExchangeConnector
    from .device_management_partner import DeviceManagementPartner
    from .device_management_reports import DeviceManagementReports
    from .device_management_settings import DeviceManagementSettings
    from .device_management_subscription_state import DeviceManagementSubscriptionState
    from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
    from .device_protection_overview import DeviceProtectionOverview
    from .entity import Entity
    from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
    from .intune_brand import IntuneBrand
    from .ios_update_device_status import IosUpdateDeviceStatus
    from .managed_device import ManagedDevice
    from .managed_device_overview import ManagedDeviceOverview
    from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
    from .mobile_threat_defense_connector import MobileThreatDefenseConnector
    from .notification_message_template import NotificationMessageTemplate
    from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
    from .remote_assistance_partner import RemoteAssistancePartner
    from .resource_operation import ResourceOperation
    from .role_definition import RoleDefinition
    from .software_update_status_summary import SoftwareUpdateStatusSummary
    from .telecom_expense_management_partner import TelecomExpenseManagementPartner
    from .terms_and_conditions import TermsAndConditions
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
    from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
    from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
    from .user_experience_analytics_overview import UserExperienceAnalyticsOverview
    from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory
    from .user_experience_analytics_settings import UserExperienceAnalyticsSettings
    from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
    from .user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
    from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance
    from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
    from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
    from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
    from .windows_malware_information import WindowsMalwareInformation
    from .windows_malware_overview import WindowsMalwareOverview

from .entity import Entity

@dataclass
class DeviceManagement(Entity):
    """
    Singleton entity that acts as a container for all device management functionality.
    """
    # Apple push notification certificate.
    apple_push_notification_certificate: Optional[ApplePushNotificationCertificate] = None
    # The Audit Events
    audit_events: Optional[List[AuditEvent]] = None
    # The list of Compliance Management Partners configured by the tenant.
    compliance_management_partners: Optional[List[ComplianceManagementPartner]] = None
    # The Exchange on premises conditional access settings. On premises conditional access will require devices to be both enrolled and compliant for mail access
    conditional_access_settings: Optional[OnPremisesConditionalAccessSettings] = None
    # The list of detected apps associated with a device.
    detected_apps: Optional[List[DetectedApp]] = None
    # The list of device categories with the tenant.
    device_categories: Optional[List[DeviceCategory]] = None
    # The device compliance policies.
    device_compliance_policies: Optional[List[DeviceCompliancePolicy]] = None
    # The device compliance state summary for this account.
    device_compliance_policy_device_state_summary: Optional[DeviceCompliancePolicyDeviceStateSummary] = None
    # The summary states of compliance policy settings for this account.
    device_compliance_policy_setting_state_summaries: Optional[List[DeviceCompliancePolicySettingStateSummary]] = None
    # The device configuration device state summary for this account.
    device_configuration_device_state_summaries: Optional[DeviceConfigurationDeviceStateSummary] = None
    # The device configurations.
    device_configurations: Optional[List[DeviceConfiguration]] = None
    # The list of device enrollment configurations
    device_enrollment_configurations: Optional[List[DeviceEnrollmentConfiguration]] = None
    # The list of Device Management Partners configured by the tenant.
    device_management_partners: Optional[List[DeviceManagementPartner]] = None
    # Device protection overview.
    device_protection_overview: Optional[DeviceProtectionOverview] = None
    # The list of Exchange Connectors configured by the tenant.
    exchange_connectors: Optional[List[DeviceManagementExchangeConnector]] = None
    # Collection of imported Windows autopilot devices.
    imported_windows_autopilot_device_identities: Optional[List[ImportedWindowsAutopilotDeviceIdentity]] = None
    # Intune Account Id for given tenant
    intune_account_id: Optional[UUID] = None
    # intuneBrand contains data which is used in customizing the appearance of the Company Portal applications as well as the end user web portal.
    intune_brand: Optional[IntuneBrand] = None
    # The IOS software update installation statuses for this account.
    ios_update_statuses: Optional[List[IosUpdateDeviceStatus]] = None
    # Device overview
    managed_device_overview: Optional[ManagedDeviceOverview] = None
    # The list of managed devices.
    managed_devices: Optional[List[ManagedDevice]] = None
    # The collection property of MobileAppTroubleshootingEvent.
    mobile_app_troubleshooting_events: Optional[List[MobileAppTroubleshootingEvent]] = None
    # The list of Mobile threat Defense connectors configured by the tenant.
    mobile_threat_defense_connectors: Optional[List[MobileThreatDefenseConnector]] = None
    # The Notification Message Templates.
    notification_message_templates: Optional[List[NotificationMessageTemplate]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The remote assist partners.
    remote_assistance_partners: Optional[List[RemoteAssistancePartner]] = None
    # Reports singleton
    reports: Optional[DeviceManagementReports] = None
    # The Resource Operations.
    resource_operations: Optional[List[ResourceOperation]] = None
    # The Role Assignments.
    role_assignments: Optional[List[DeviceAndAppManagementRoleAssignment]] = None
    # The Role Definitions.
    role_definitions: Optional[List[RoleDefinition]] = None
    # Account level settings.
    settings: Optional[DeviceManagementSettings] = None
    # The software update status summary.
    software_update_status_summary: Optional[SoftwareUpdateStatusSummary] = None
    # Tenant mobile device management subscription state.
    subscription_state: Optional[DeviceManagementSubscriptionState] = None
    # The telecom expense management partners.
    telecom_expense_management_partners: Optional[List[TelecomExpenseManagementPartner]] = None
    # The terms and conditions associated with device management of the company.
    terms_and_conditions: Optional[List[TermsAndConditions]] = None
    # The list of troubleshooting events for the tenant.
    troubleshooting_events: Optional[List[DeviceManagementTroubleshootingEvent]] = None
    # User experience analytics appHealth Application Performance
    user_experience_analytics_app_health_application_performance: Optional[List[UserExperienceAnalyticsAppHealthApplicationPerformance]] = None
    # User experience analytics appHealth Application Performance by App Version details
    user_experience_analytics_app_health_application_performance_by_app_version_details: Optional[List[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails]] = None
    # User experience analytics appHealth Application Performance by App Version Device Id
    user_experience_analytics_app_health_application_performance_by_app_version_device_id: Optional[List[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId]] = None
    # User experience analytics appHealth Application Performance by OS Version
    user_experience_analytics_app_health_application_performance_by_o_s_version: Optional[List[UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion]] = None
    # User experience analytics appHealth Model Performance
    user_experience_analytics_app_health_device_model_performance: Optional[List[UserExperienceAnalyticsAppHealthDeviceModelPerformance]] = None
    # User experience analytics appHealth Device Performance
    user_experience_analytics_app_health_device_performance: Optional[List[UserExperienceAnalyticsAppHealthDevicePerformance]] = None
    # User experience analytics device performance details
    user_experience_analytics_app_health_device_performance_details: Optional[List[UserExperienceAnalyticsAppHealthDevicePerformanceDetails]] = None
    # User experience analytics appHealth OS version Performance
    user_experience_analytics_app_health_o_s_version_performance: Optional[List[UserExperienceAnalyticsAppHealthOSVersionPerformance]] = None
    # User experience analytics appHealth overview
    user_experience_analytics_app_health_overview: Optional[UserExperienceAnalyticsCategory] = None
    # User experience analytics baselines
    user_experience_analytics_baselines: Optional[List[UserExperienceAnalyticsBaseline]] = None
    # User experience analytics categories
    user_experience_analytics_categories: Optional[List[UserExperienceAnalyticsCategory]] = None
    # User experience analytics device performance
    user_experience_analytics_device_performance: Optional[List[UserExperienceAnalyticsDevicePerformance]] = None
    # User experience analytics device scores
    user_experience_analytics_device_scores: Optional[List[UserExperienceAnalyticsDeviceScores]] = None
    # User experience analytics device Startup History
    user_experience_analytics_device_startup_history: Optional[List[UserExperienceAnalyticsDeviceStartupHistory]] = None
    # User experience analytics device Startup Process Performance
    user_experience_analytics_device_startup_process_performance: Optional[List[UserExperienceAnalyticsDeviceStartupProcessPerformance]] = None
    # User experience analytics device Startup Processes
    user_experience_analytics_device_startup_processes: Optional[List[UserExperienceAnalyticsDeviceStartupProcess]] = None
    # User experience analytics metric history
    user_experience_analytics_metric_history: Optional[List[UserExperienceAnalyticsMetricHistory]] = None
    # User experience analytics model scores
    user_experience_analytics_model_scores: Optional[List[UserExperienceAnalyticsModelScores]] = None
    # User experience analytics overview
    user_experience_analytics_overview: Optional[UserExperienceAnalyticsOverview] = None
    # User experience analytics device Startup Score History
    user_experience_analytics_score_history: Optional[List[UserExperienceAnalyticsScoreHistory]] = None
    # User experience analytics device settings
    user_experience_analytics_settings: Optional[UserExperienceAnalyticsSettings] = None
    # User experience analytics work from anywhere hardware readiness metrics.
    user_experience_analytics_work_from_anywhere_hardware_readiness_metric: Optional[UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric] = None
    # User experience analytics work from anywhere metrics.
    user_experience_analytics_work_from_anywhere_metrics: Optional[List[UserExperienceAnalyticsWorkFromAnywhereMetric]] = None
    # The user experience analytics work from anywhere model performance
    user_experience_analytics_work_from_anywhere_model_performance: Optional[List[UserExperienceAnalyticsWorkFromAnywhereModelPerformance]] = None
    # The Windows autopilot device identities contained collection.
    windows_autopilot_device_identities: Optional[List[WindowsAutopilotDeviceIdentity]] = None
    # The windows information protection app learning summaries.
    windows_information_protection_app_learning_summaries: Optional[List[WindowsInformationProtectionAppLearningSummary]] = None
    # The windows information protection network learning summaries.
    windows_information_protection_network_learning_summaries: Optional[List[WindowsInformationProtectionNetworkLearningSummary]] = None
    # The list of affected malware in the tenant.
    windows_malware_information: Optional[List[WindowsMalwareInformation]] = None
    # Malware overview for windows devices.
    windows_malware_overview: Optional[WindowsMalwareOverview] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagement
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .apple_push_notification_certificate import ApplePushNotificationCertificate
        from .audit_event import AuditEvent
        from .compliance_management_partner import ComplianceManagementPartner
        from .detected_app import DetectedApp
        from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
        from .device_category import DeviceCategory
        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
        from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
        from .device_configuration import DeviceConfiguration
        from .device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
        from .device_enrollment_configuration import DeviceEnrollmentConfiguration
        from .device_management_exchange_connector import DeviceManagementExchangeConnector
        from .device_management_partner import DeviceManagementPartner
        from .device_management_reports import DeviceManagementReports
        from .device_management_settings import DeviceManagementSettings
        from .device_management_subscription_state import DeviceManagementSubscriptionState
        from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
        from .device_protection_overview import DeviceProtectionOverview
        from .entity import Entity
        from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
        from .intune_brand import IntuneBrand
        from .ios_update_device_status import IosUpdateDeviceStatus
        from .managed_device import ManagedDevice
        from .managed_device_overview import ManagedDeviceOverview
        from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
        from .mobile_threat_defense_connector import MobileThreatDefenseConnector
        from .notification_message_template import NotificationMessageTemplate
        from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
        from .remote_assistance_partner import RemoteAssistancePartner
        from .resource_operation import ResourceOperation
        from .role_definition import RoleDefinition
        from .software_update_status_summary import SoftwareUpdateStatusSummary
        from .telecom_expense_management_partner import TelecomExpenseManagementPartner
        from .terms_and_conditions import TermsAndConditions
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
        from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
        from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
        from .user_experience_analytics_overview import UserExperienceAnalyticsOverview
        from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory
        from .user_experience_analytics_settings import UserExperienceAnalyticsSettings
        from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
        from .user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
        from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance
        from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
        from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
        from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
        from .windows_malware_information import WindowsMalwareInformation
        from .windows_malware_overview import WindowsMalwareOverview

        from .apple_push_notification_certificate import ApplePushNotificationCertificate
        from .audit_event import AuditEvent
        from .compliance_management_partner import ComplianceManagementPartner
        from .detected_app import DetectedApp
        from .device_and_app_management_role_assignment import DeviceAndAppManagementRoleAssignment
        from .device_category import DeviceCategory
        from .device_compliance_policy import DeviceCompliancePolicy
        from .device_compliance_policy_device_state_summary import DeviceCompliancePolicyDeviceStateSummary
        from .device_compliance_policy_setting_state_summary import DeviceCompliancePolicySettingStateSummary
        from .device_configuration import DeviceConfiguration
        from .device_configuration_device_state_summary import DeviceConfigurationDeviceStateSummary
        from .device_enrollment_configuration import DeviceEnrollmentConfiguration
        from .device_management_exchange_connector import DeviceManagementExchangeConnector
        from .device_management_partner import DeviceManagementPartner
        from .device_management_reports import DeviceManagementReports
        from .device_management_settings import DeviceManagementSettings
        from .device_management_subscription_state import DeviceManagementSubscriptionState
        from .device_management_troubleshooting_event import DeviceManagementTroubleshootingEvent
        from .device_protection_overview import DeviceProtectionOverview
        from .entity import Entity
        from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
        from .intune_brand import IntuneBrand
        from .ios_update_device_status import IosUpdateDeviceStatus
        from .managed_device import ManagedDevice
        from .managed_device_overview import ManagedDeviceOverview
        from .mobile_app_troubleshooting_event import MobileAppTroubleshootingEvent
        from .mobile_threat_defense_connector import MobileThreatDefenseConnector
        from .notification_message_template import NotificationMessageTemplate
        from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
        from .remote_assistance_partner import RemoteAssistancePartner
        from .resource_operation import ResourceOperation
        from .role_definition import RoleDefinition
        from .software_update_status_summary import SoftwareUpdateStatusSummary
        from .telecom_expense_management_partner import TelecomExpenseManagementPartner
        from .terms_and_conditions import TermsAndConditions
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
        from .user_experience_analytics_metric_history import UserExperienceAnalyticsMetricHistory
        from .user_experience_analytics_model_scores import UserExperienceAnalyticsModelScores
        from .user_experience_analytics_overview import UserExperienceAnalyticsOverview
        from .user_experience_analytics_score_history import UserExperienceAnalyticsScoreHistory
        from .user_experience_analytics_settings import UserExperienceAnalyticsSettings
        from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric
        from .user_experience_analytics_work_from_anywhere_metric import UserExperienceAnalyticsWorkFromAnywhereMetric
        from .user_experience_analytics_work_from_anywhere_model_performance import UserExperienceAnalyticsWorkFromAnywhereModelPerformance
        from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
        from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
        from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
        from .windows_malware_information import WindowsMalwareInformation
        from .windows_malware_overview import WindowsMalwareOverview

        fields: Dict[str, Callable[[Any], None]] = {
            "apple_push_notification_certificate": lambda n : setattr(self, 'apple_push_notification_certificate', n.get_object_value(ApplePushNotificationCertificate)),
            "audit_events": lambda n : setattr(self, 'audit_events', n.get_collection_of_object_values(AuditEvent)),
            "compliance_management_partners": lambda n : setattr(self, 'compliance_management_partners', n.get_collection_of_object_values(ComplianceManagementPartner)),
            "conditional_access_settings": lambda n : setattr(self, 'conditional_access_settings', n.get_object_value(OnPremisesConditionalAccessSettings)),
            "detected_apps": lambda n : setattr(self, 'detected_apps', n.get_collection_of_object_values(DetectedApp)),
            "device_categories": lambda n : setattr(self, 'device_categories', n.get_collection_of_object_values(DeviceCategory)),
            "device_compliance_policies": lambda n : setattr(self, 'device_compliance_policies', n.get_collection_of_object_values(DeviceCompliancePolicy)),
            "device_compliance_policy_device_state_summary": lambda n : setattr(self, 'device_compliance_policy_device_state_summary', n.get_object_value(DeviceCompliancePolicyDeviceStateSummary)),
            "device_compliance_policy_setting_state_summaries": lambda n : setattr(self, 'device_compliance_policy_setting_state_summaries', n.get_collection_of_object_values(DeviceCompliancePolicySettingStateSummary)),
            "device_configuration_device_state_summaries": lambda n : setattr(self, 'device_configuration_device_state_summaries', n.get_object_value(DeviceConfigurationDeviceStateSummary)),
            "device_configurations": lambda n : setattr(self, 'device_configurations', n.get_collection_of_object_values(DeviceConfiguration)),
            "device_enrollment_configurations": lambda n : setattr(self, 'device_enrollment_configurations', n.get_collection_of_object_values(DeviceEnrollmentConfiguration)),
            "device_management_partners": lambda n : setattr(self, 'device_management_partners', n.get_collection_of_object_values(DeviceManagementPartner)),
            "device_protection_overview": lambda n : setattr(self, 'device_protection_overview', n.get_object_value(DeviceProtectionOverview)),
            "exchange_connectors": lambda n : setattr(self, 'exchange_connectors', n.get_collection_of_object_values(DeviceManagementExchangeConnector)),
            "imported_windows_autopilot_device_identities": lambda n : setattr(self, 'imported_windows_autopilot_device_identities', n.get_collection_of_object_values(ImportedWindowsAutopilotDeviceIdentity)),
            "intune_account_id": lambda n : setattr(self, 'intune_account_id', n.get_uuid_value()),
            "intune_brand": lambda n : setattr(self, 'intune_brand', n.get_object_value(IntuneBrand)),
            "ios_update_statuses": lambda n : setattr(self, 'ios_update_statuses', n.get_collection_of_object_values(IosUpdateDeviceStatus)),
            "managed_device_overview": lambda n : setattr(self, 'managed_device_overview', n.get_object_value(ManagedDeviceOverview)),
            "managed_devices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(ManagedDevice)),
            "mobile_app_troubleshooting_events": lambda n : setattr(self, 'mobile_app_troubleshooting_events', n.get_collection_of_object_values(MobileAppTroubleshootingEvent)),
            "mobile_threat_defense_connectors": lambda n : setattr(self, 'mobile_threat_defense_connectors', n.get_collection_of_object_values(MobileThreatDefenseConnector)),
            "notification_message_templates": lambda n : setattr(self, 'notification_message_templates', n.get_collection_of_object_values(NotificationMessageTemplate)),
            "remote_assistance_partners": lambda n : setattr(self, 'remote_assistance_partners', n.get_collection_of_object_values(RemoteAssistancePartner)),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(DeviceManagementReports)),
            "resource_operations": lambda n : setattr(self, 'resource_operations', n.get_collection_of_object_values(ResourceOperation)),
            "role_assignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(DeviceAndAppManagementRoleAssignment)),
            "role_definitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(RoleDefinition)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(DeviceManagementSettings)),
            "software_update_status_summary": lambda n : setattr(self, 'software_update_status_summary', n.get_object_value(SoftwareUpdateStatusSummary)),
            "subscription_state": lambda n : setattr(self, 'subscription_state', n.get_enum_value(DeviceManagementSubscriptionState)),
            "telecom_expense_management_partners": lambda n : setattr(self, 'telecom_expense_management_partners', n.get_collection_of_object_values(TelecomExpenseManagementPartner)),
            "terms_and_conditions": lambda n : setattr(self, 'terms_and_conditions', n.get_collection_of_object_values(TermsAndConditions)),
            "troubleshooting_events": lambda n : setattr(self, 'troubleshooting_events', n.get_collection_of_object_values(DeviceManagementTroubleshootingEvent)),
            "user_experience_analytics_app_health_application_performance": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthApplicationPerformance)),
            "user_experience_analytics_app_health_application_performance_by_app_version_details": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_app_version_details', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails)),
            "user_experience_analytics_app_health_application_performance_by_app_version_device_id": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_app_version_device_id', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId)),
            "user_experience_analytics_app_health_application_performance_by_o_s_version": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_o_s_version', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion)),
            "user_experience_analytics_app_health_device_model_performance": lambda n : setattr(self, 'user_experience_analytics_app_health_device_model_performance', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthDeviceModelPerformance)),
            "user_experience_analytics_app_health_device_performance": lambda n : setattr(self, 'user_experience_analytics_app_health_device_performance', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthDevicePerformance)),
            "user_experience_analytics_app_health_device_performance_details": lambda n : setattr(self, 'user_experience_analytics_app_health_device_performance_details', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthDevicePerformanceDetails)),
            "user_experience_analytics_app_health_o_s_version_performance": lambda n : setattr(self, 'user_experience_analytics_app_health_o_s_version_performance', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthOSVersionPerformance)),
            "user_experience_analytics_app_health_overview": lambda n : setattr(self, 'user_experience_analytics_app_health_overview', n.get_object_value(UserExperienceAnalyticsCategory)),
            "user_experience_analytics_baselines": lambda n : setattr(self, 'user_experience_analytics_baselines', n.get_collection_of_object_values(UserExperienceAnalyticsBaseline)),
            "user_experience_analytics_categories": lambda n : setattr(self, 'user_experience_analytics_categories', n.get_collection_of_object_values(UserExperienceAnalyticsCategory)),
            "user_experience_analytics_device_performance": lambda n : setattr(self, 'user_experience_analytics_device_performance', n.get_collection_of_object_values(UserExperienceAnalyticsDevicePerformance)),
            "user_experience_analytics_device_scores": lambda n : setattr(self, 'user_experience_analytics_device_scores', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceScores)),
            "user_experience_analytics_device_startup_history": lambda n : setattr(self, 'user_experience_analytics_device_startup_history', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceStartupHistory)),
            "user_experience_analytics_device_startup_process_performance": lambda n : setattr(self, 'user_experience_analytics_device_startup_process_performance', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceStartupProcessPerformance)),
            "user_experience_analytics_device_startup_processes": lambda n : setattr(self, 'user_experience_analytics_device_startup_processes', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceStartupProcess)),
            "user_experience_analytics_metric_history": lambda n : setattr(self, 'user_experience_analytics_metric_history', n.get_collection_of_object_values(UserExperienceAnalyticsMetricHistory)),
            "user_experience_analytics_model_scores": lambda n : setattr(self, 'user_experience_analytics_model_scores', n.get_collection_of_object_values(UserExperienceAnalyticsModelScores)),
            "user_experience_analytics_overview": lambda n : setattr(self, 'user_experience_analytics_overview', n.get_object_value(UserExperienceAnalyticsOverview)),
            "user_experience_analytics_score_history": lambda n : setattr(self, 'user_experience_analytics_score_history', n.get_collection_of_object_values(UserExperienceAnalyticsScoreHistory)),
            "user_experience_analytics_settings": lambda n : setattr(self, 'user_experience_analytics_settings', n.get_object_value(UserExperienceAnalyticsSettings)),
            "user_experience_analytics_work_from_anywhere_hardware_readiness_metric": lambda n : setattr(self, 'user_experience_analytics_work_from_anywhere_hardware_readiness_metric', n.get_object_value(UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric)),
            "user_experience_analytics_work_from_anywhere_metrics": lambda n : setattr(self, 'user_experience_analytics_work_from_anywhere_metrics', n.get_collection_of_object_values(UserExperienceAnalyticsWorkFromAnywhereMetric)),
            "user_experience_analytics_work_from_anywhere_model_performance": lambda n : setattr(self, 'user_experience_analytics_work_from_anywhere_model_performance', n.get_collection_of_object_values(UserExperienceAnalyticsWorkFromAnywhereModelPerformance)),
            "windows_autopilot_device_identities": lambda n : setattr(self, 'windows_autopilot_device_identities', n.get_collection_of_object_values(WindowsAutopilotDeviceIdentity)),
            "windows_information_protection_app_learning_summaries": lambda n : setattr(self, 'windows_information_protection_app_learning_summaries', n.get_collection_of_object_values(WindowsInformationProtectionAppLearningSummary)),
            "windows_information_protection_network_learning_summaries": lambda n : setattr(self, 'windows_information_protection_network_learning_summaries', n.get_collection_of_object_values(WindowsInformationProtectionNetworkLearningSummary)),
            "windows_malware_information": lambda n : setattr(self, 'windows_malware_information', n.get_collection_of_object_values(WindowsMalwareInformation)),
            "windows_malware_overview": lambda n : setattr(self, 'windows_malware_overview', n.get_object_value(WindowsMalwareOverview)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("apple_push_notification_certificate", self.apple_push_notification_certificate)
        writer.write_collection_of_object_values("audit_events", self.audit_events)
        writer.write_collection_of_object_values("compliance_management_partners", self.compliance_management_partners)
        writer.write_object_value("conditional_access_settings", self.conditional_access_settings)
        writer.write_collection_of_object_values("detected_apps", self.detected_apps)
        writer.write_collection_of_object_values("device_categories", self.device_categories)
        writer.write_collection_of_object_values("device_compliance_policies", self.device_compliance_policies)
        writer.write_object_value("device_compliance_policy_device_state_summary", self.device_compliance_policy_device_state_summary)
        writer.write_collection_of_object_values("device_compliance_policy_setting_state_summaries", self.device_compliance_policy_setting_state_summaries)
        writer.write_object_value("device_configuration_device_state_summaries", self.device_configuration_device_state_summaries)
        writer.write_collection_of_object_values("device_configurations", self.device_configurations)
        writer.write_collection_of_object_values("device_enrollment_configurations", self.device_enrollment_configurations)
        writer.write_collection_of_object_values("device_management_partners", self.device_management_partners)
        writer.write_object_value("device_protection_overview", self.device_protection_overview)
        writer.write_collection_of_object_values("exchange_connectors", self.exchange_connectors)
        writer.write_collection_of_object_values("imported_windows_autopilot_device_identities", self.imported_windows_autopilot_device_identities)
        writer.write_uuid_value("intune_account_id", self.intune_account_id)
        writer.write_object_value("intune_brand", self.intune_brand)
        writer.write_collection_of_object_values("ios_update_statuses", self.ios_update_statuses)
        writer.write_object_value("managed_device_overview", self.managed_device_overview)
        writer.write_collection_of_object_values("managed_devices", self.managed_devices)
        writer.write_collection_of_object_values("mobile_app_troubleshooting_events", self.mobile_app_troubleshooting_events)
        writer.write_collection_of_object_values("mobile_threat_defense_connectors", self.mobile_threat_defense_connectors)
        writer.write_collection_of_object_values("notification_message_templates", self.notification_message_templates)
        writer.write_collection_of_object_values("remote_assistance_partners", self.remote_assistance_partners)
        writer.write_object_value("reports", self.reports)
        writer.write_collection_of_object_values("resource_operations", self.resource_operations)
        writer.write_collection_of_object_values("role_assignments", self.role_assignments)
        writer.write_collection_of_object_values("role_definitions", self.role_definitions)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("software_update_status_summary", self.software_update_status_summary)
        writer.write_enum_value("subscription_state", self.subscription_state)
        writer.write_collection_of_object_values("telecom_expense_management_partners", self.telecom_expense_management_partners)
        writer.write_collection_of_object_values("terms_and_conditions", self.terms_and_conditions)
        writer.write_collection_of_object_values("troubleshooting_events", self.troubleshooting_events)
        writer.write_collection_of_object_values("user_experience_analytics_app_health_application_performance", self.user_experience_analytics_app_health_application_performance)
        writer.write_collection_of_object_values("user_experience_analytics_app_health_application_performance_by_app_version_details", self.user_experience_analytics_app_health_application_performance_by_app_version_details)
        writer.write_collection_of_object_values("user_experience_analytics_app_health_application_performance_by_app_version_device_id", self.user_experience_analytics_app_health_application_performance_by_app_version_device_id)
        writer.write_collection_of_object_values("user_experience_analytics_app_health_application_performance_by_o_s_version", self.user_experience_analytics_app_health_application_performance_by_o_s_version)
        writer.write_collection_of_object_values("user_experience_analytics_app_health_device_model_performance", self.user_experience_analytics_app_health_device_model_performance)
        writer.write_collection_of_object_values("user_experience_analytics_app_health_device_performance", self.user_experience_analytics_app_health_device_performance)
        writer.write_collection_of_object_values("user_experience_analytics_app_health_device_performance_details", self.user_experience_analytics_app_health_device_performance_details)
        writer.write_collection_of_object_values("user_experience_analytics_app_health_o_s_version_performance", self.user_experience_analytics_app_health_o_s_version_performance)
        writer.write_object_value("user_experience_analytics_app_health_overview", self.user_experience_analytics_app_health_overview)
        writer.write_collection_of_object_values("user_experience_analytics_baselines", self.user_experience_analytics_baselines)
        writer.write_collection_of_object_values("user_experience_analytics_categories", self.user_experience_analytics_categories)
        writer.write_collection_of_object_values("user_experience_analytics_device_performance", self.user_experience_analytics_device_performance)
        writer.write_collection_of_object_values("user_experience_analytics_device_scores", self.user_experience_analytics_device_scores)
        writer.write_collection_of_object_values("user_experience_analytics_device_startup_history", self.user_experience_analytics_device_startup_history)
        writer.write_collection_of_object_values("user_experience_analytics_device_startup_process_performance", self.user_experience_analytics_device_startup_process_performance)
        writer.write_collection_of_object_values("user_experience_analytics_device_startup_processes", self.user_experience_analytics_device_startup_processes)
        writer.write_collection_of_object_values("user_experience_analytics_metric_history", self.user_experience_analytics_metric_history)
        writer.write_collection_of_object_values("user_experience_analytics_model_scores", self.user_experience_analytics_model_scores)
        writer.write_object_value("user_experience_analytics_overview", self.user_experience_analytics_overview)
        writer.write_collection_of_object_values("user_experience_analytics_score_history", self.user_experience_analytics_score_history)
        writer.write_object_value("user_experience_analytics_settings", self.user_experience_analytics_settings)
        writer.write_object_value("user_experience_analytics_work_from_anywhere_hardware_readiness_metric", self.user_experience_analytics_work_from_anywhere_hardware_readiness_metric)
        writer.write_collection_of_object_values("user_experience_analytics_work_from_anywhere_metrics", self.user_experience_analytics_work_from_anywhere_metrics)
        writer.write_collection_of_object_values("user_experience_analytics_work_from_anywhere_model_performance", self.user_experience_analytics_work_from_anywhere_model_performance)
        writer.write_collection_of_object_values("windows_autopilot_device_identities", self.windows_autopilot_device_identities)
        writer.write_collection_of_object_values("windows_information_protection_app_learning_summaries", self.windows_information_protection_app_learning_summaries)
        writer.write_collection_of_object_values("windows_information_protection_network_learning_summaries", self.windows_information_protection_network_learning_summaries)
        writer.write_collection_of_object_values("windows_malware_information", self.windows_malware_information)
        writer.write_object_value("windows_malware_overview", self.windows_malware_overview)
    

