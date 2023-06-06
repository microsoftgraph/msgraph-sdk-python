from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from . import apple_push_notification_certificate, audit_event, compliance_management_partner, detected_app, device_and_app_management_role_assignment, device_category, device_compliance_policy, device_compliance_policy_device_state_summary, device_compliance_policy_setting_state_summary, device_configuration, device_configuration_device_state_summary, device_enrollment_configuration, device_management_exchange_connector, device_management_partner, device_management_reports, device_management_settings, device_management_subscription_state, device_management_troubleshooting_event, entity, imported_windows_autopilot_device_identity, intune_brand, ios_update_device_status, managed_device, managed_device_overview, mobile_threat_defense_connector, notification_message_template, on_premises_conditional_access_settings, remote_assistance_partner, resource_operation, role_definition, software_update_status_summary, telecom_expense_management_partner, terms_and_conditions, windows_autopilot_device_identity, windows_information_protection_app_learning_summary, windows_information_protection_network_learning_summary

from . import entity

@dataclass
class DeviceManagement(entity.Entity):
    # Apple push notification certificate.
    apple_push_notification_certificate: Optional[apple_push_notification_certificate.ApplePushNotificationCertificate] = None
    # The Audit Events
    audit_events: Optional[List[audit_event.AuditEvent]] = None
    # The list of Compliance Management Partners configured by the tenant.
    compliance_management_partners: Optional[List[compliance_management_partner.ComplianceManagementPartner]] = None
    # The Exchange on premises conditional access settings. On premises conditional access will require devices to be both enrolled and compliant for mail access
    conditional_access_settings: Optional[on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings] = None
    # The list of detected apps associated with a device.
    detected_apps: Optional[List[detected_app.DetectedApp]] = None
    # The list of device categories with the tenant.
    device_categories: Optional[List[device_category.DeviceCategory]] = None
    # The device compliance policies.
    device_compliance_policies: Optional[List[device_compliance_policy.DeviceCompliancePolicy]] = None
    # The device compliance state summary for this account.
    device_compliance_policy_device_state_summary: Optional[device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary] = None
    # The summary states of compliance policy settings for this account.
    device_compliance_policy_setting_state_summaries: Optional[List[device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary]] = None
    # The device configuration device state summary for this account.
    device_configuration_device_state_summaries: Optional[device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary] = None
    # The device configurations.
    device_configurations: Optional[List[device_configuration.DeviceConfiguration]] = None
    # The list of device enrollment configurations
    device_enrollment_configurations: Optional[List[device_enrollment_configuration.DeviceEnrollmentConfiguration]] = None
    # The list of Device Management Partners configured by the tenant.
    device_management_partners: Optional[List[device_management_partner.DeviceManagementPartner]] = None
    # The list of Exchange Connectors configured by the tenant.
    exchange_connectors: Optional[List[device_management_exchange_connector.DeviceManagementExchangeConnector]] = None
    # Collection of imported Windows autopilot devices.
    imported_windows_autopilot_device_identities: Optional[List[imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity]] = None
    # Intune Account Id for given tenant
    intune_account_id: Optional[UUID] = None
    # intuneBrand contains data which is used in customizing the appearance of the Company Portal applications as well as the end user web portal.
    intune_brand: Optional[intune_brand.IntuneBrand] = None
    # The IOS software update installation statuses for this account.
    ios_update_statuses: Optional[List[ios_update_device_status.IosUpdateDeviceStatus]] = None
    # Device overview
    managed_device_overview: Optional[managed_device_overview.ManagedDeviceOverview] = None
    # The list of managed devices.
    managed_devices: Optional[List[managed_device.ManagedDevice]] = None
    # The list of Mobile threat Defense connectors configured by the tenant.
    mobile_threat_defense_connectors: Optional[List[mobile_threat_defense_connector.MobileThreatDefenseConnector]] = None
    # The Notification Message Templates.
    notification_message_templates: Optional[List[notification_message_template.NotificationMessageTemplate]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The remote assist partners.
    remote_assistance_partners: Optional[List[remote_assistance_partner.RemoteAssistancePartner]] = None
    # Reports singleton
    reports: Optional[device_management_reports.DeviceManagementReports] = None
    # The Resource Operations.
    resource_operations: Optional[List[resource_operation.ResourceOperation]] = None
    # The Role Assignments.
    role_assignments: Optional[List[device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment]] = None
    # The Role Definitions.
    role_definitions: Optional[List[role_definition.RoleDefinition]] = None
    # Account level settings.
    settings: Optional[device_management_settings.DeviceManagementSettings] = None
    # The software update status summary.
    software_update_status_summary: Optional[software_update_status_summary.SoftwareUpdateStatusSummary] = None
    # Tenant mobile device management subscription state.
    subscription_state: Optional[device_management_subscription_state.DeviceManagementSubscriptionState] = None
    # The telecom expense management partners.
    telecom_expense_management_partners: Optional[List[telecom_expense_management_partner.TelecomExpenseManagementPartner]] = None
    # The terms and conditions associated with device management of the company.
    terms_and_conditions: Optional[List[terms_and_conditions.TermsAndConditions]] = None
    # The list of troubleshooting events for the tenant.
    troubleshooting_events: Optional[List[device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent]] = None
    # The Windows autopilot device identities contained collection.
    windows_autopilot_device_identities: Optional[List[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]] = None
    # The windows information protection app learning summaries.
    windows_information_protection_app_learning_summaries: Optional[List[windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary]] = None
    # The windows information protection network learning summaries.
    windows_information_protection_network_learning_summaries: Optional[List[windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagement
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import apple_push_notification_certificate, audit_event, compliance_management_partner, detected_app, device_and_app_management_role_assignment, device_category, device_compliance_policy, device_compliance_policy_device_state_summary, device_compliance_policy_setting_state_summary, device_configuration, device_configuration_device_state_summary, device_enrollment_configuration, device_management_exchange_connector, device_management_partner, device_management_reports, device_management_settings, device_management_subscription_state, device_management_troubleshooting_event, entity, imported_windows_autopilot_device_identity, intune_brand, ios_update_device_status, managed_device, managed_device_overview, mobile_threat_defense_connector, notification_message_template, on_premises_conditional_access_settings, remote_assistance_partner, resource_operation, role_definition, software_update_status_summary, telecom_expense_management_partner, terms_and_conditions, windows_autopilot_device_identity, windows_information_protection_app_learning_summary, windows_information_protection_network_learning_summary

        fields: Dict[str, Callable[[Any], None]] = {
            "applePushNotificationCertificate": lambda n : setattr(self, 'apple_push_notification_certificate', n.get_object_value(apple_push_notification_certificate.ApplePushNotificationCertificate)),
            "auditEvents": lambda n : setattr(self, 'audit_events', n.get_collection_of_object_values(audit_event.AuditEvent)),
            "complianceManagementPartners": lambda n : setattr(self, 'compliance_management_partners', n.get_collection_of_object_values(compliance_management_partner.ComplianceManagementPartner)),
            "conditionalAccessSettings": lambda n : setattr(self, 'conditional_access_settings', n.get_object_value(on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings)),
            "detectedApps": lambda n : setattr(self, 'detected_apps', n.get_collection_of_object_values(detected_app.DetectedApp)),
            "deviceCategories": lambda n : setattr(self, 'device_categories', n.get_collection_of_object_values(device_category.DeviceCategory)),
            "deviceCompliancePolicies": lambda n : setattr(self, 'device_compliance_policies', n.get_collection_of_object_values(device_compliance_policy.DeviceCompliancePolicy)),
            "deviceCompliancePolicyDeviceStateSummary": lambda n : setattr(self, 'device_compliance_policy_device_state_summary', n.get_object_value(device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary)),
            "deviceCompliancePolicySettingStateSummaries": lambda n : setattr(self, 'device_compliance_policy_setting_state_summaries', n.get_collection_of_object_values(device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary)),
            "deviceConfigurations": lambda n : setattr(self, 'device_configurations', n.get_collection_of_object_values(device_configuration.DeviceConfiguration)),
            "deviceConfigurationDeviceStateSummaries": lambda n : setattr(self, 'device_configuration_device_state_summaries', n.get_object_value(device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary)),
            "deviceEnrollmentConfigurations": lambda n : setattr(self, 'device_enrollment_configurations', n.get_collection_of_object_values(device_enrollment_configuration.DeviceEnrollmentConfiguration)),
            "deviceManagementPartners": lambda n : setattr(self, 'device_management_partners', n.get_collection_of_object_values(device_management_partner.DeviceManagementPartner)),
            "exchangeConnectors": lambda n : setattr(self, 'exchange_connectors', n.get_collection_of_object_values(device_management_exchange_connector.DeviceManagementExchangeConnector)),
            "importedWindowsAutopilotDeviceIdentities": lambda n : setattr(self, 'imported_windows_autopilot_device_identities', n.get_collection_of_object_values(imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity)),
            "intuneAccountId": lambda n : setattr(self, 'intune_account_id', n.get_uuid_value()),
            "intuneBrand": lambda n : setattr(self, 'intune_brand', n.get_object_value(intune_brand.IntuneBrand)),
            "iosUpdateStatuses": lambda n : setattr(self, 'ios_update_statuses', n.get_collection_of_object_values(ios_update_device_status.IosUpdateDeviceStatus)),
            "managedDevices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(managed_device.ManagedDevice)),
            "managedDeviceOverview": lambda n : setattr(self, 'managed_device_overview', n.get_object_value(managed_device_overview.ManagedDeviceOverview)),
            "mobileThreatDefenseConnectors": lambda n : setattr(self, 'mobile_threat_defense_connectors', n.get_collection_of_object_values(mobile_threat_defense_connector.MobileThreatDefenseConnector)),
            "notificationMessageTemplates": lambda n : setattr(self, 'notification_message_templates', n.get_collection_of_object_values(notification_message_template.NotificationMessageTemplate)),
            "remoteAssistancePartners": lambda n : setattr(self, 'remote_assistance_partners', n.get_collection_of_object_values(remote_assistance_partner.RemoteAssistancePartner)),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(device_management_reports.DeviceManagementReports)),
            "resourceOperations": lambda n : setattr(self, 'resource_operations', n.get_collection_of_object_values(resource_operation.ResourceOperation)),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment)),
            "roleDefinitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(role_definition.RoleDefinition)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(device_management_settings.DeviceManagementSettings)),
            "softwareUpdateStatusSummary": lambda n : setattr(self, 'software_update_status_summary', n.get_object_value(software_update_status_summary.SoftwareUpdateStatusSummary)),
            "subscriptionState": lambda n : setattr(self, 'subscription_state', n.get_enum_value(device_management_subscription_state.DeviceManagementSubscriptionState)),
            "telecomExpenseManagementPartners": lambda n : setattr(self, 'telecom_expense_management_partners', n.get_collection_of_object_values(telecom_expense_management_partner.TelecomExpenseManagementPartner)),
            "termsAndConditions": lambda n : setattr(self, 'terms_and_conditions', n.get_collection_of_object_values(terms_and_conditions.TermsAndConditions)),
            "troubleshootingEvents": lambda n : setattr(self, 'troubleshooting_events', n.get_collection_of_object_values(device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent)),
            "windowsAutopilotDeviceIdentities": lambda n : setattr(self, 'windows_autopilot_device_identities', n.get_collection_of_object_values(windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity)),
            "windowsInformationProtectionAppLearningSummaries": lambda n : setattr(self, 'windows_information_protection_app_learning_summaries', n.get_collection_of_object_values(windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary)),
            "windowsInformationProtectionNetworkLearningSummaries": lambda n : setattr(self, 'windows_information_protection_network_learning_summaries', n.get_collection_of_object_values(windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary)),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
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
        writer.write_collection_of_object_values("deviceConfigurations", self.device_configurations)
        writer.write_object_value("deviceConfigurationDeviceStateSummaries", self.device_configuration_device_state_summaries)
        writer.write_collection_of_object_values("deviceEnrollmentConfigurations", self.device_enrollment_configurations)
        writer.write_collection_of_object_values("deviceManagementPartners", self.device_management_partners)
        writer.write_collection_of_object_values("exchangeConnectors", self.exchange_connectors)
        writer.write_collection_of_object_values("importedWindowsAutopilotDeviceIdentities", self.imported_windows_autopilot_device_identities)
        writer.write_uuid_value("intuneAccountId", self.intune_account_id)
        writer.write_object_value("intuneBrand", self.intune_brand)
        writer.write_collection_of_object_values("iosUpdateStatuses", self.ios_update_statuses)
        writer.write_collection_of_object_values("managedDevices", self.managed_devices)
        writer.write_object_value("managedDeviceOverview", self.managed_device_overview)
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
    

