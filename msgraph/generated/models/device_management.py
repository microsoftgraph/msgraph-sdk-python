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
    from .entity import Entity
    from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
    from .intune_brand import IntuneBrand
    from .ios_update_device_status import IosUpdateDeviceStatus
    from .managed_device import ManagedDevice
    from .managed_device_overview import ManagedDeviceOverview
    from .mobile_threat_defense_connector import MobileThreatDefenseConnector
    from .notification_message_template import NotificationMessageTemplate
    from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
    from .remote_assistance_partner import RemoteAssistancePartner
    from .resource_operation import ResourceOperation
    from .role_definition import RoleDefinition
    from .software_update_status_summary import SoftwareUpdateStatusSummary
    from .telecom_expense_management_partner import TelecomExpenseManagementPartner
    from .terms_and_conditions import TermsAndConditions
    from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
    from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
    from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary

from .entity import Entity

@dataclass
class DeviceManagement(Entity):
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
    # The Windows autopilot device identities contained collection.
    windows_autopilot_device_identities: Optional[List[WindowsAutopilotDeviceIdentity]] = None
    # The windows information protection app learning summaries.
    windows_information_protection_app_learning_summaries: Optional[List[WindowsInformationProtectionAppLearningSummary]] = None
    # The windows information protection network learning summaries.
    windows_information_protection_network_learning_summaries: Optional[List[WindowsInformationProtectionNetworkLearningSummary]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
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
        from .entity import Entity
        from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
        from .intune_brand import IntuneBrand
        from .ios_update_device_status import IosUpdateDeviceStatus
        from .managed_device import ManagedDevice
        from .managed_device_overview import ManagedDeviceOverview
        from .mobile_threat_defense_connector import MobileThreatDefenseConnector
        from .notification_message_template import NotificationMessageTemplate
        from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
        from .remote_assistance_partner import RemoteAssistancePartner
        from .resource_operation import ResourceOperation
        from .role_definition import RoleDefinition
        from .software_update_status_summary import SoftwareUpdateStatusSummary
        from .telecom_expense_management_partner import TelecomExpenseManagementPartner
        from .terms_and_conditions import TermsAndConditions
        from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
        from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
        from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary

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
        from .entity import Entity
        from .imported_windows_autopilot_device_identity import ImportedWindowsAutopilotDeviceIdentity
        from .intune_brand import IntuneBrand
        from .ios_update_device_status import IosUpdateDeviceStatus
        from .managed_device import ManagedDevice
        from .managed_device_overview import ManagedDeviceOverview
        from .mobile_threat_defense_connector import MobileThreatDefenseConnector
        from .notification_message_template import NotificationMessageTemplate
        from .on_premises_conditional_access_settings import OnPremisesConditionalAccessSettings
        from .remote_assistance_partner import RemoteAssistancePartner
        from .resource_operation import ResourceOperation
        from .role_definition import RoleDefinition
        from .software_update_status_summary import SoftwareUpdateStatusSummary
        from .telecom_expense_management_partner import TelecomExpenseManagementPartner
        from .terms_and_conditions import TermsAndConditions
        from .windows_autopilot_device_identity import WindowsAutopilotDeviceIdentity
        from .windows_information_protection_app_learning_summary import WindowsInformationProtectionAppLearningSummary
        from .windows_information_protection_network_learning_summary import WindowsInformationProtectionNetworkLearningSummary

        fields: Dict[str, Callable[[Any], None]] = {
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
            "exchangeConnectors": lambda n : setattr(self, 'exchange_connectors', n.get_collection_of_object_values(DeviceManagementExchangeConnector)),
            "importedWindowsAutopilotDeviceIdentities": lambda n : setattr(self, 'imported_windows_autopilot_device_identities', n.get_collection_of_object_values(ImportedWindowsAutopilotDeviceIdentity)),
            "intuneAccountId": lambda n : setattr(self, 'intune_account_id', n.get_uuid_value()),
            "intuneBrand": lambda n : setattr(self, 'intune_brand', n.get_object_value(IntuneBrand)),
            "iosUpdateStatuses": lambda n : setattr(self, 'ios_update_statuses', n.get_collection_of_object_values(IosUpdateDeviceStatus)),
            "managedDeviceOverview": lambda n : setattr(self, 'managed_device_overview', n.get_object_value(ManagedDeviceOverview)),
            "managedDevices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(ManagedDevice)),
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
            "telecomExpenseManagementPartners": lambda n : setattr(self, 'telecom_expense_management_partners', n.get_collection_of_object_values(TelecomExpenseManagementPartner)),
            "termsAndConditions": lambda n : setattr(self, 'terms_and_conditions', n.get_collection_of_object_values(TermsAndConditions)),
            "troubleshootingEvents": lambda n : setattr(self, 'troubleshooting_events', n.get_collection_of_object_values(DeviceManagementTroubleshootingEvent)),
            "windowsAutopilotDeviceIdentities": lambda n : setattr(self, 'windows_autopilot_device_identities', n.get_collection_of_object_values(WindowsAutopilotDeviceIdentity)),
            "windowsInformationProtectionAppLearningSummaries": lambda n : setattr(self, 'windows_information_protection_app_learning_summaries', n.get_collection_of_object_values(WindowsInformationProtectionAppLearningSummary)),
            "windowsInformationProtectionNetworkLearningSummaries": lambda n : setattr(self, 'windows_information_protection_network_learning_summaries', n.get_collection_of_object_values(WindowsInformationProtectionNetworkLearningSummary)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
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
        writer.write_collection_of_object_values("exchangeConnectors", self.exchange_connectors)
        writer.write_collection_of_object_values("importedWindowsAutopilotDeviceIdentities", self.imported_windows_autopilot_device_identities)
        writer.write_uuid_value("intuneAccountId", self.intune_account_id)
        writer.write_object_value("intuneBrand", self.intune_brand)
        writer.write_collection_of_object_values("iosUpdateStatuses", self.ios_update_statuses)
        writer.write_object_value("managedDeviceOverview", self.managed_device_overview)
        writer.write_collection_of_object_values("managedDevices", self.managed_devices)
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
        writer.write_collection_of_object_values("telecomExpenseManagementPartners", self.telecom_expense_management_partners)
        writer.write_collection_of_object_values("termsAndConditions", self.terms_and_conditions)
        writer.write_collection_of_object_values("troubleshootingEvents", self.troubleshooting_events)
        writer.write_collection_of_object_values("windowsAutopilotDeviceIdentities", self.windows_autopilot_device_identities)
        writer.write_collection_of_object_values("windowsInformationProtectionAppLearningSummaries", self.windows_information_protection_app_learning_summaries)
        writer.write_collection_of_object_values("windowsInformationProtectionNetworkLearningSummaries", self.windows_information_protection_network_learning_summaries)
    

