from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
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
    from .virtual_endpoint import VirtualEndpoint
    from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
    from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
    from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
    from .windows_malware_information import WindowsMalwareInformation
    from .windows_malware_overview import WindowsMalwareOverview

from .entity import Entity

@dataclass
class DeviceManagement(Entity, Parsable):
    # Apple push notification certificate.
    apple_push_notification_certificate: Optional[ApplePushNotificationCertificate] = None
    # The Audit Events
    audit_events: Optional[list[AuditEvent]] = None
    # The list of Compliance Management Partners configured by the tenant.
    compliance_management_partners: Optional[list[ComplianceManagementPartner]] = None
    # The Exchange on premises conditional access settings. On premises conditional access will require devices to be both enrolled and compliant for mail access
    conditional_access_settings: Optional[OnPremisesConditionalAccessSettings] = None
    # The list of detected apps associated with a device.
    detected_apps: Optional[list[DetectedApp]] = None
    # The list of device categories with the tenant.
    device_categories: Optional[list[DeviceCategory]] = None
    # The device compliance policies.
    device_compliance_policies: Optional[list[DeviceCompliancePolicy]] = None
    # The device compliance state summary for this account.
    device_compliance_policy_device_state_summary: Optional[DeviceCompliancePolicyDeviceStateSummary] = None
    # The summary states of compliance policy settings for this account.
    device_compliance_policy_setting_state_summaries: Optional[list[DeviceCompliancePolicySettingStateSummary]] = None
    # The device configuration device state summary for this account.
    device_configuration_device_state_summaries: Optional[DeviceConfigurationDeviceStateSummary] = None
    # The device configurations.
    device_configurations: Optional[list[DeviceConfiguration]] = None
    # The list of device enrollment configurations
    device_enrollment_configurations: Optional[list[DeviceEnrollmentConfiguration]] = None
    # The list of Device Management Partners configured by the tenant.
    device_management_partners: Optional[list[DeviceManagementPartner]] = None
    # Device protection overview.
    device_protection_overview: Optional[DeviceProtectionOverview] = None
    # The list of Exchange Connectors configured by the tenant.
    exchange_connectors: Optional[list[DeviceManagementExchangeConnector]] = None
    # Collection of imported Windows autopilot devices.
    imported_windows_autopilot_device_identities: Optional[list[ImportedWindowsAutopilotDeviceIdentity]] = None
    # Intune Account Id for given tenant
    intune_account_id: Optional[UUID] = None
    # intuneBrand contains data which is used in customizing the appearance of the Company Portal applications as well as the end user web portal.
    intune_brand: Optional[IntuneBrand] = None
    # The IOS software update installation statuses for this account.
    ios_update_statuses: Optional[list[IosUpdateDeviceStatus]] = None
    # Device overview
    managed_device_overview: Optional[ManagedDeviceOverview] = None
    # The list of managed devices.
    managed_devices: Optional[list[ManagedDevice]] = None
    # The collection property of MobileAppTroubleshootingEvent.
    mobile_app_troubleshooting_events: Optional[list[MobileAppTroubleshootingEvent]] = None
    # The list of Mobile threat Defense connectors configured by the tenant.
    mobile_threat_defense_connectors: Optional[list[MobileThreatDefenseConnector]] = None
    # The Notification Message Templates.
    notification_message_templates: Optional[list[NotificationMessageTemplate]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The remote assist partners.
    remote_assistance_partners: Optional[list[RemoteAssistancePartner]] = None
    # The reports property
    reports: Optional[DeviceManagementReports] = None
    # The Resource Operations.
    resource_operations: Optional[list[ResourceOperation]] = None
    # The Role Assignments.
    role_assignments: Optional[list[DeviceAndAppManagementRoleAssignment]] = None
    # The Role Definitions.
    role_definitions: Optional[list[RoleDefinition]] = None
    # Account level settings.
    settings: Optional[DeviceManagementSettings] = None
    # The software update status summary.
    software_update_status_summary: Optional[SoftwareUpdateStatusSummary] = None
    # Tenant mobile device management subscription state.
    subscription_state: Optional[DeviceManagementSubscriptionState] = None
    # The terms and conditions associated with device management of the company.
    terms_and_conditions: Optional[list[TermsAndConditions]] = None
    # The list of troubleshooting events for the tenant.
    troubleshooting_events: Optional[list[DeviceManagementTroubleshootingEvent]] = None
    # User experience analytics appHealth Application Performance
    user_experience_analytics_app_health_application_performance: Optional[list[UserExperienceAnalyticsAppHealthApplicationPerformance]] = None
    # User experience analytics appHealth Application Performance by App Version details
    user_experience_analytics_app_health_application_performance_by_app_version_details: Optional[list[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails]] = None
    # User experience analytics appHealth Application Performance by App Version Device Id
    user_experience_analytics_app_health_application_performance_by_app_version_device_id: Optional[list[UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId]] = None
    # User experience analytics appHealth Application Performance by OS Version
    user_experience_analytics_app_health_application_performance_by_o_s_version: Optional[list[UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion]] = None
    # User experience analytics appHealth Model Performance
    user_experience_analytics_app_health_device_model_performance: Optional[list[UserExperienceAnalyticsAppHealthDeviceModelPerformance]] = None
    # User experience analytics appHealth Device Performance
    user_experience_analytics_app_health_device_performance: Optional[list[UserExperienceAnalyticsAppHealthDevicePerformance]] = None
    # User experience analytics device performance details
    user_experience_analytics_app_health_device_performance_details: Optional[list[UserExperienceAnalyticsAppHealthDevicePerformanceDetails]] = None
    # User experience analytics appHealth OS version Performance
    user_experience_analytics_app_health_o_s_version_performance: Optional[list[UserExperienceAnalyticsAppHealthOSVersionPerformance]] = None
    # User experience analytics appHealth overview
    user_experience_analytics_app_health_overview: Optional[UserExperienceAnalyticsCategory] = None
    # User experience analytics baselines
    user_experience_analytics_baselines: Optional[list[UserExperienceAnalyticsBaseline]] = None
    # User experience analytics categories
    user_experience_analytics_categories: Optional[list[UserExperienceAnalyticsCategory]] = None
    # User experience analytics device performance
    user_experience_analytics_device_performance: Optional[list[UserExperienceAnalyticsDevicePerformance]] = None
    # User experience analytics device scores
    user_experience_analytics_device_scores: Optional[list[UserExperienceAnalyticsDeviceScores]] = None
    # User experience analytics device Startup History
    user_experience_analytics_device_startup_history: Optional[list[UserExperienceAnalyticsDeviceStartupHistory]] = None
    # User experience analytics device Startup Process Performance
    user_experience_analytics_device_startup_process_performance: Optional[list[UserExperienceAnalyticsDeviceStartupProcessPerformance]] = None
    # User experience analytics device Startup Processes
    user_experience_analytics_device_startup_processes: Optional[list[UserExperienceAnalyticsDeviceStartupProcess]] = None
    # User experience analytics metric history
    user_experience_analytics_metric_history: Optional[list[UserExperienceAnalyticsMetricHistory]] = None
    # User experience analytics model scores
    user_experience_analytics_model_scores: Optional[list[UserExperienceAnalyticsModelScores]] = None
    # User experience analytics overview
    user_experience_analytics_overview: Optional[UserExperienceAnalyticsOverview] = None
    # User experience analytics device Startup Score History
    user_experience_analytics_score_history: Optional[list[UserExperienceAnalyticsScoreHistory]] = None
    # User experience analytics device settings
    user_experience_analytics_settings: Optional[UserExperienceAnalyticsSettings] = None
    # User experience analytics work from anywhere hardware readiness metrics.
    user_experience_analytics_work_from_anywhere_hardware_readiness_metric: Optional[UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric] = None
    # User experience analytics work from anywhere metrics.
    user_experience_analytics_work_from_anywhere_metrics: Optional[list[UserExperienceAnalyticsWorkFromAnywhereMetric]] = None
    # The user experience analytics work from anywhere model performance
    user_experience_analytics_work_from_anywhere_model_performance: Optional[list[UserExperienceAnalyticsWorkFromAnywhereModelPerformance]] = None
    # The virtualEndpoint property
    virtual_endpoint: Optional[VirtualEndpoint] = None
    # The Windows autopilot device identities contained collection.
    windows_autopilot_device_identities: Optional[list[WindowsAutopilotDeviceIdentity]] = None
    # The windows information protection app learning summaries.
    windows_information_protection_app_learning_summaries: Optional[list[WindowsInformationProtectionAppLearningSummary]] = None
    # The windows information protection network learning summaries.
    windows_information_protection_network_learning_summaries: Optional[list[WindowsInformationProtectionNetworkLearningSummary]] = None
    # The list of affected malware in the tenant.
    windows_malware_information: Optional[list[WindowsMalwareInformation]] = None
    # Malware overview for windows devices.
    windows_malware_overview: Optional[WindowsMalwareOverview] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeviceManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeviceManagement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
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
        from .virtual_endpoint import VirtualEndpoint
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
        from .virtual_endpoint import VirtualEndpoint
        from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
        from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
        from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary
        from .windows_malware_information import WindowsMalwareInformation
        from .windows_malware_overview import WindowsMalwareOverview

        fields: dict[str, Callable[[Any], None]] = {
            "applePushNotificationCertificate": lambda n : setattr(self, 'apple_push_notification_certificate', n.get_object_value(ApplePushNotificationCertificate)),
            "auditEvents": lambda n : setattr(self, 'audit_events', n.get_collection_of_object_values(AuditEvent)),
            "complianceManagementPartners": lambda n : setattr(self, 'compliance_management_partners', n.get_collection_of_object_values(ComplianceManagementPartner)),
            "conditionalAccessSettings": lambda n : setattr(self, 'conditional_access_settings', n.get_object_value(OnPremisesConditionalAccessSettings)),
            "detectedApps": lambda n : setattr(self, 'detected_apps', n.get_collection_of_object_values(DetectedApp)),
            "deviceCategories": lambda n : setattr(self, 'device_categories', n.get_collection_of_object_values(DeviceCategory)),
            "deviceCompliancePolicies": lambda n : setattr(self, 'device_compliance_policies', n.get_collection_of_object_values(DeviceCompliancePolicy)),
            "deviceCompliancePolicyDeviceStateSummary": lambda n : setattr(self, 'device_compliance_policy_device_state_summary', n.get_object_value(DeviceCompliancePolicyDeviceStateSummary)),
            "deviceCompliancePolicySettingStateSummaries": lambda n : setattr(self, 'device_compliance_policy_setting_state_summaries', n.get_collection_of_object_values(DeviceCompliancePolicySettingStateSummary)),
            "deviceConfigurationDeviceStateSummaries": lambda n : setattr(self, 'device_configuration_device_state_summaries', n.get_object_value(DeviceConfigurationDeviceStateSummary)),
            "deviceConfigurations": lambda n : setattr(self, 'device_configurations', n.get_collection_of_object_values(DeviceConfiguration)),
            "deviceEnrollmentConfigurations": lambda n : setattr(self, 'device_enrollment_configurations', n.get_collection_of_object_values(DeviceEnrollmentConfiguration)),
            "deviceManagementPartners": lambda n : setattr(self, 'device_management_partners', n.get_collection_of_object_values(DeviceManagementPartner)),
            "deviceProtectionOverview": lambda n : setattr(self, 'device_protection_overview', n.get_object_value(DeviceProtectionOverview)),
            "exchangeConnectors": lambda n : setattr(self, 'exchange_connectors', n.get_collection_of_object_values(DeviceManagementExchangeConnector)),
            "importedWindowsAutopilotDeviceIdentities": lambda n : setattr(self, 'imported_windows_autopilot_device_identities', n.get_collection_of_object_values(ImportedWindowsAutopilotDeviceIdentity)),
            "intuneAccountId": lambda n : setattr(self, 'intune_account_id', n.get_uuid_value()),
            "intuneBrand": lambda n : setattr(self, 'intune_brand', n.get_object_value(IntuneBrand)),
            "iosUpdateStatuses": lambda n : setattr(self, 'ios_update_statuses', n.get_collection_of_object_values(IosUpdateDeviceStatus)),
            "managedDeviceOverview": lambda n : setattr(self, 'managed_device_overview', n.get_object_value(ManagedDeviceOverview)),
            "managedDevices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(ManagedDevice)),
            "mobileAppTroubleshootingEvents": lambda n : setattr(self, 'mobile_app_troubleshooting_events', n.get_collection_of_object_values(MobileAppTroubleshootingEvent)),
            "mobileThreatDefenseConnectors": lambda n : setattr(self, 'mobile_threat_defense_connectors', n.get_collection_of_object_values(MobileThreatDefenseConnector)),
            "notificationMessageTemplates": lambda n : setattr(self, 'notification_message_templates', n.get_collection_of_object_values(NotificationMessageTemplate)),
            "remoteAssistancePartners": lambda n : setattr(self, 'remote_assistance_partners', n.get_collection_of_object_values(RemoteAssistancePartner)),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(DeviceManagementReports)),
            "resourceOperations": lambda n : setattr(self, 'resource_operations', n.get_collection_of_object_values(ResourceOperation)),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(DeviceAndAppManagementRoleAssignment)),
            "roleDefinitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(RoleDefinition)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(DeviceManagementSettings)),
            "softwareUpdateStatusSummary": lambda n : setattr(self, 'software_update_status_summary', n.get_object_value(SoftwareUpdateStatusSummary)),
            "subscriptionState": lambda n : setattr(self, 'subscription_state', n.get_enum_value(DeviceManagementSubscriptionState)),
            "termsAndConditions": lambda n : setattr(self, 'terms_and_conditions', n.get_collection_of_object_values(TermsAndConditions)),
            "troubleshootingEvents": lambda n : setattr(self, 'troubleshooting_events', n.get_collection_of_object_values(DeviceManagementTroubleshootingEvent)),
            "userExperienceAnalyticsAppHealthApplicationPerformance": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthApplicationPerformance)),
            "userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_app_version_details', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDetails)),
            "userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_app_version_device_id', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthAppPerformanceByAppVersionDeviceId)),
            "userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion": lambda n : setattr(self, 'user_experience_analytics_app_health_application_performance_by_o_s_version', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthAppPerformanceByOSVersion)),
            "userExperienceAnalyticsAppHealthDeviceModelPerformance": lambda n : setattr(self, 'user_experience_analytics_app_health_device_model_performance', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthDeviceModelPerformance)),
            "userExperienceAnalyticsAppHealthDevicePerformance": lambda n : setattr(self, 'user_experience_analytics_app_health_device_performance', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthDevicePerformance)),
            "userExperienceAnalyticsAppHealthDevicePerformanceDetails": lambda n : setattr(self, 'user_experience_analytics_app_health_device_performance_details', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthDevicePerformanceDetails)),
            "userExperienceAnalyticsAppHealthOSVersionPerformance": lambda n : setattr(self, 'user_experience_analytics_app_health_o_s_version_performance', n.get_collection_of_object_values(UserExperienceAnalyticsAppHealthOSVersionPerformance)),
            "userExperienceAnalyticsAppHealthOverview": lambda n : setattr(self, 'user_experience_analytics_app_health_overview', n.get_object_value(UserExperienceAnalyticsCategory)),
            "userExperienceAnalyticsBaselines": lambda n : setattr(self, 'user_experience_analytics_baselines', n.get_collection_of_object_values(UserExperienceAnalyticsBaseline)),
            "userExperienceAnalyticsCategories": lambda n : setattr(self, 'user_experience_analytics_categories', n.get_collection_of_object_values(UserExperienceAnalyticsCategory)),
            "userExperienceAnalyticsDevicePerformance": lambda n : setattr(self, 'user_experience_analytics_device_performance', n.get_collection_of_object_values(UserExperienceAnalyticsDevicePerformance)),
            "userExperienceAnalyticsDeviceScores": lambda n : setattr(self, 'user_experience_analytics_device_scores', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceScores)),
            "userExperienceAnalyticsDeviceStartupHistory": lambda n : setattr(self, 'user_experience_analytics_device_startup_history', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceStartupHistory)),
            "userExperienceAnalyticsDeviceStartupProcessPerformance": lambda n : setattr(self, 'user_experience_analytics_device_startup_process_performance', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceStartupProcessPerformance)),
            "userExperienceAnalyticsDeviceStartupProcesses": lambda n : setattr(self, 'user_experience_analytics_device_startup_processes', n.get_collection_of_object_values(UserExperienceAnalyticsDeviceStartupProcess)),
            "userExperienceAnalyticsMetricHistory": lambda n : setattr(self, 'user_experience_analytics_metric_history', n.get_collection_of_object_values(UserExperienceAnalyticsMetricHistory)),
            "userExperienceAnalyticsModelScores": lambda n : setattr(self, 'user_experience_analytics_model_scores', n.get_collection_of_object_values(UserExperienceAnalyticsModelScores)),
            "userExperienceAnalyticsOverview": lambda n : setattr(self, 'user_experience_analytics_overview', n.get_object_value(UserExperienceAnalyticsOverview)),
            "userExperienceAnalyticsScoreHistory": lambda n : setattr(self, 'user_experience_analytics_score_history', n.get_collection_of_object_values(UserExperienceAnalyticsScoreHistory)),
            "userExperienceAnalyticsSettings": lambda n : setattr(self, 'user_experience_analytics_settings', n.get_object_value(UserExperienceAnalyticsSettings)),
            "userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric": lambda n : setattr(self, 'user_experience_analytics_work_from_anywhere_hardware_readiness_metric', n.get_object_value(UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric)),
            "userExperienceAnalyticsWorkFromAnywhereMetrics": lambda n : setattr(self, 'user_experience_analytics_work_from_anywhere_metrics', n.get_collection_of_object_values(UserExperienceAnalyticsWorkFromAnywhereMetric)),
            "userExperienceAnalyticsWorkFromAnywhereModelPerformance": lambda n : setattr(self, 'user_experience_analytics_work_from_anywhere_model_performance', n.get_collection_of_object_values(UserExperienceAnalyticsWorkFromAnywhereModelPerformance)),
            "virtualEndpoint": lambda n : setattr(self, 'virtual_endpoint', n.get_object_value(VirtualEndpoint)),
            "windowsAutopilotDeviceIdentities": lambda n : setattr(self, 'windows_autopilot_device_identities', n.get_collection_of_object_values(WindowsAutopilotDeviceIdentity)),
            "windowsInformationProtectionAppLearningSummaries": lambda n : setattr(self, 'windows_information_protection_app_learning_summaries', n.get_collection_of_object_values(WindowsInformationProtectionAppLearningSummary)),
            "windowsInformationProtectionNetworkLearningSummaries": lambda n : setattr(self, 'windows_information_protection_network_learning_summaries', n.get_collection_of_object_values(WindowsInformationProtectionNetworkLearningSummary)),
            "windowsMalwareInformation": lambda n : setattr(self, 'windows_malware_information', n.get_collection_of_object_values(WindowsMalwareInformation)),
            "windowsMalwareOverview": lambda n : setattr(self, 'windows_malware_overview', n.get_object_value(WindowsMalwareOverview)),
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
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("applePushNotificationCertificate", self.apple_push_notification_certificate)
        writer.write_collection_of_object_values("auditEvents", self.audit_events)
        writer.write_collection_of_object_values("complianceManagementPartners", self.compliance_management_partners)
        writer.write_object_value("conditionalAccessSettings", self.conditional_access_settings)
        writer.write_collection_of_object_values("detectedApps", self.detected_apps)
        writer.write_collection_of_object_values("deviceCategories", self.device_categories)
        writer.write_collection_of_object_values("deviceCompliancePolicies", self.device_compliance_policies)
        writer.write_object_value("deviceCompliancePolicyDeviceStateSummary", self.device_compliance_policy_device_state_summary)
        writer.write_collection_of_object_values("deviceCompliancePolicySettingStateSummaries", self.device_compliance_policy_setting_state_summaries)
        writer.write_object_value("deviceConfigurationDeviceStateSummaries", self.device_configuration_device_state_summaries)
        writer.write_collection_of_object_values("deviceConfigurations", self.device_configurations)
        writer.write_collection_of_object_values("deviceEnrollmentConfigurations", self.device_enrollment_configurations)
        writer.write_collection_of_object_values("deviceManagementPartners", self.device_management_partners)
        writer.write_object_value("deviceProtectionOverview", self.device_protection_overview)
        writer.write_collection_of_object_values("exchangeConnectors", self.exchange_connectors)
        writer.write_collection_of_object_values("importedWindowsAutopilotDeviceIdentities", self.imported_windows_autopilot_device_identities)
        writer.write_uuid_value("intuneAccountId", self.intune_account_id)
        writer.write_object_value("intuneBrand", self.intune_brand)
        writer.write_collection_of_object_values("iosUpdateStatuses", self.ios_update_statuses)
        writer.write_object_value("managedDeviceOverview", self.managed_device_overview)
        writer.write_collection_of_object_values("managedDevices", self.managed_devices)
        writer.write_collection_of_object_values("mobileAppTroubleshootingEvents", self.mobile_app_troubleshooting_events)
        writer.write_collection_of_object_values("mobileThreatDefenseConnectors", self.mobile_threat_defense_connectors)
        writer.write_collection_of_object_values("notificationMessageTemplates", self.notification_message_templates)
        writer.write_collection_of_object_values("remoteAssistancePartners", self.remote_assistance_partners)
        writer.write_object_value("reports", self.reports)
        writer.write_collection_of_object_values("resourceOperations", self.resource_operations)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_object_value("settings", self.settings)
        writer.write_object_value("softwareUpdateStatusSummary", self.software_update_status_summary)
        writer.write_enum_value("subscriptionState", self.subscription_state)
        writer.write_collection_of_object_values("termsAndConditions", self.terms_and_conditions)
        writer.write_collection_of_object_values("troubleshootingEvents", self.troubleshooting_events)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthApplicationPerformance", self.user_experience_analytics_app_health_application_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails", self.user_experience_analytics_app_health_application_performance_by_app_version_details)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId", self.user_experience_analytics_app_health_application_performance_by_app_version_device_id)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion", self.user_experience_analytics_app_health_application_performance_by_o_s_version)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthDeviceModelPerformance", self.user_experience_analytics_app_health_device_model_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthDevicePerformance", self.user_experience_analytics_app_health_device_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthDevicePerformanceDetails", self.user_experience_analytics_app_health_device_performance_details)
        writer.write_collection_of_object_values("userExperienceAnalyticsAppHealthOSVersionPerformance", self.user_experience_analytics_app_health_o_s_version_performance)
        writer.write_object_value("userExperienceAnalyticsAppHealthOverview", self.user_experience_analytics_app_health_overview)
        writer.write_collection_of_object_values("userExperienceAnalyticsBaselines", self.user_experience_analytics_baselines)
        writer.write_collection_of_object_values("userExperienceAnalyticsCategories", self.user_experience_analytics_categories)
        writer.write_collection_of_object_values("userExperienceAnalyticsDevicePerformance", self.user_experience_analytics_device_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceScores", self.user_experience_analytics_device_scores)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceStartupHistory", self.user_experience_analytics_device_startup_history)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceStartupProcessPerformance", self.user_experience_analytics_device_startup_process_performance)
        writer.write_collection_of_object_values("userExperienceAnalyticsDeviceStartupProcesses", self.user_experience_analytics_device_startup_processes)
        writer.write_collection_of_object_values("userExperienceAnalyticsMetricHistory", self.user_experience_analytics_metric_history)
        writer.write_collection_of_object_values("userExperienceAnalyticsModelScores", self.user_experience_analytics_model_scores)
        writer.write_object_value("userExperienceAnalyticsOverview", self.user_experience_analytics_overview)
        writer.write_collection_of_object_values("userExperienceAnalyticsScoreHistory", self.user_experience_analytics_score_history)
        writer.write_object_value("userExperienceAnalyticsSettings", self.user_experience_analytics_settings)
        writer.write_object_value("userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric", self.user_experience_analytics_work_from_anywhere_hardware_readiness_metric)
        writer.write_collection_of_object_values("userExperienceAnalyticsWorkFromAnywhereMetrics", self.user_experience_analytics_work_from_anywhere_metrics)
        writer.write_collection_of_object_values("userExperienceAnalyticsWorkFromAnywhereModelPerformance", self.user_experience_analytics_work_from_anywhere_model_performance)
        writer.write_object_value("virtualEndpoint", self.virtual_endpoint)
        writer.write_collection_of_object_values("windowsAutopilotDeviceIdentities", self.windows_autopilot_device_identities)
        writer.write_collection_of_object_values("windowsInformationProtectionAppLearningSummaries", self.windows_information_protection_app_learning_summaries)
        writer.write_collection_of_object_values("windowsInformationProtectionNetworkLearningSummaries", self.windows_information_protection_network_learning_summaries)
        writer.write_collection_of_object_values("windowsMalwareInformation", self.windows_malware_information)
        writer.write_object_value("windowsMalwareOverview", self.windows_malware_overview)
    

