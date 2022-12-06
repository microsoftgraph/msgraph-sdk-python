from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

apple_push_notification_certificate = lazy_import('msgraph.generated.models.apple_push_notification_certificate')
audit_event = lazy_import('msgraph.generated.models.audit_event')
compliance_management_partner = lazy_import('msgraph.generated.models.compliance_management_partner')
detected_app = lazy_import('msgraph.generated.models.detected_app')
device_and_app_management_role_assignment = lazy_import('msgraph.generated.models.device_and_app_management_role_assignment')
device_category = lazy_import('msgraph.generated.models.device_category')
device_compliance_policy = lazy_import('msgraph.generated.models.device_compliance_policy')
device_compliance_policy_device_state_summary = lazy_import('msgraph.generated.models.device_compliance_policy_device_state_summary')
device_compliance_policy_setting_state_summary = lazy_import('msgraph.generated.models.device_compliance_policy_setting_state_summary')
device_configuration = lazy_import('msgraph.generated.models.device_configuration')
device_configuration_device_state_summary = lazy_import('msgraph.generated.models.device_configuration_device_state_summary')
device_enrollment_configuration = lazy_import('msgraph.generated.models.device_enrollment_configuration')
device_management_exchange_connector = lazy_import('msgraph.generated.models.device_management_exchange_connector')
device_management_partner = lazy_import('msgraph.generated.models.device_management_partner')
device_management_reports = lazy_import('msgraph.generated.models.device_management_reports')
device_management_settings = lazy_import('msgraph.generated.models.device_management_settings')
device_management_subscription_state = lazy_import('msgraph.generated.models.device_management_subscription_state')
device_management_troubleshooting_event = lazy_import('msgraph.generated.models.device_management_troubleshooting_event')
entity = lazy_import('msgraph.generated.models.entity')
imported_windows_autopilot_device_identity = lazy_import('msgraph.generated.models.imported_windows_autopilot_device_identity')
intune_brand = lazy_import('msgraph.generated.models.intune_brand')
ios_update_device_status = lazy_import('msgraph.generated.models.ios_update_device_status')
managed_device = lazy_import('msgraph.generated.models.managed_device')
managed_device_overview = lazy_import('msgraph.generated.models.managed_device_overview')
mobile_threat_defense_connector = lazy_import('msgraph.generated.models.mobile_threat_defense_connector')
notification_message_template = lazy_import('msgraph.generated.models.notification_message_template')
on_premises_conditional_access_settings = lazy_import('msgraph.generated.models.on_premises_conditional_access_settings')
remote_assistance_partner = lazy_import('msgraph.generated.models.remote_assistance_partner')
resource_operation = lazy_import('msgraph.generated.models.resource_operation')
role_definition = lazy_import('msgraph.generated.models.role_definition')
software_update_status_summary = lazy_import('msgraph.generated.models.software_update_status_summary')
telecom_expense_management_partner = lazy_import('msgraph.generated.models.telecom_expense_management_partner')
terms_and_conditions = lazy_import('msgraph.generated.models.terms_and_conditions')
windows_autopilot_device_identity = lazy_import('msgraph.generated.models.windows_autopilot_device_identity')
windows_information_protection_app_learning_summary = lazy_import('msgraph.generated.models.windows_information_protection_app_learning_summary')
windows_information_protection_network_learning_summary = lazy_import('msgraph.generated.models.windows_information_protection_network_learning_summary')

class DeviceManagement(entity.Entity):
    @property
    def apple_push_notification_certificate(self,) -> Optional[apple_push_notification_certificate.ApplePushNotificationCertificate]:
        """
        Gets the applePushNotificationCertificate property value. Apple push notification certificate.
        Returns: Optional[apple_push_notification_certificate.ApplePushNotificationCertificate]
        """
        return self._apple_push_notification_certificate
    
    @apple_push_notification_certificate.setter
    def apple_push_notification_certificate(self,value: Optional[apple_push_notification_certificate.ApplePushNotificationCertificate] = None) -> None:
        """
        Sets the applePushNotificationCertificate property value. Apple push notification certificate.
        Args:
            value: Value to set for the applePushNotificationCertificate property.
        """
        self._apple_push_notification_certificate = value
    
    @property
    def audit_events(self,) -> Optional[List[audit_event.AuditEvent]]:
        """
        Gets the auditEvents property value. The Audit Events
        Returns: Optional[List[audit_event.AuditEvent]]
        """
        return self._audit_events
    
    @audit_events.setter
    def audit_events(self,value: Optional[List[audit_event.AuditEvent]] = None) -> None:
        """
        Sets the auditEvents property value. The Audit Events
        Args:
            value: Value to set for the auditEvents property.
        """
        self._audit_events = value
    
    @property
    def compliance_management_partners(self,) -> Optional[List[compliance_management_partner.ComplianceManagementPartner]]:
        """
        Gets the complianceManagementPartners property value. The list of Compliance Management Partners configured by the tenant.
        Returns: Optional[List[compliance_management_partner.ComplianceManagementPartner]]
        """
        return self._compliance_management_partners
    
    @compliance_management_partners.setter
    def compliance_management_partners(self,value: Optional[List[compliance_management_partner.ComplianceManagementPartner]] = None) -> None:
        """
        Sets the complianceManagementPartners property value. The list of Compliance Management Partners configured by the tenant.
        Args:
            value: Value to set for the complianceManagementPartners property.
        """
        self._compliance_management_partners = value
    
    @property
    def conditional_access_settings(self,) -> Optional[on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings]:
        """
        Gets the conditionalAccessSettings property value. The Exchange on premises conditional access settings. On premises conditional access will require devices to be both enrolled and compliant for mail access
        Returns: Optional[on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings]
        """
        return self._conditional_access_settings
    
    @conditional_access_settings.setter
    def conditional_access_settings(self,value: Optional[on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings] = None) -> None:
        """
        Sets the conditionalAccessSettings property value. The Exchange on premises conditional access settings. On premises conditional access will require devices to be both enrolled and compliant for mail access
        Args:
            value: Value to set for the conditionalAccessSettings property.
        """
        self._conditional_access_settings = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new DeviceManagement and sets the default values.
        """
        super().__init__()
        # Apple push notification certificate.
        self._apple_push_notification_certificate: Optional[apple_push_notification_certificate.ApplePushNotificationCertificate] = None
        # The Audit Events
        self._audit_events: Optional[List[audit_event.AuditEvent]] = None
        # The list of Compliance Management Partners configured by the tenant.
        self._compliance_management_partners: Optional[List[compliance_management_partner.ComplianceManagementPartner]] = None
        # The Exchange on premises conditional access settings. On premises conditional access will require devices to be both enrolled and compliant for mail access
        self._conditional_access_settings: Optional[on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings] = None
        # The list of detected apps associated with a device.
        self._detected_apps: Optional[List[detected_app.DetectedApp]] = None
        # The list of device categories with the tenant.
        self._device_categories: Optional[List[device_category.DeviceCategory]] = None
        # The device compliance policies.
        self._device_compliance_policies: Optional[List[device_compliance_policy.DeviceCompliancePolicy]] = None
        # The device compliance state summary for this account.
        self._device_compliance_policy_device_state_summary: Optional[device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary] = None
        # The summary states of compliance policy settings for this account.
        self._device_compliance_policy_setting_state_summaries: Optional[List[device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary]] = None
        # The device configuration device state summary for this account.
        self._device_configuration_device_state_summaries: Optional[device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary] = None
        # The device configurations.
        self._device_configurations: Optional[List[device_configuration.DeviceConfiguration]] = None
        # The list of device enrollment configurations
        self._device_enrollment_configurations: Optional[List[device_enrollment_configuration.DeviceEnrollmentConfiguration]] = None
        # The list of Device Management Partners configured by the tenant.
        self._device_management_partners: Optional[List[device_management_partner.DeviceManagementPartner]] = None
        # The list of Exchange Connectors configured by the tenant.
        self._exchange_connectors: Optional[List[device_management_exchange_connector.DeviceManagementExchangeConnector]] = None
        # Collection of imported Windows autopilot devices.
        self._imported_windows_autopilot_device_identities: Optional[List[imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity]] = None
        # Intune Account Id for given tenant
        self._intune_account_id: Optional[str] = None
        # intuneBrand contains data which is used in customizing the appearance of the Company Portal applications as well as the end user web portal.
        self._intune_brand: Optional[intune_brand.IntuneBrand] = None
        # The IOS software update installation statuses for this account.
        self._ios_update_statuses: Optional[List[ios_update_device_status.IosUpdateDeviceStatus]] = None
        # Device overview
        self._managed_device_overview: Optional[managed_device_overview.ManagedDeviceOverview] = None
        # The list of managed devices.
        self._managed_devices: Optional[List[managed_device.ManagedDevice]] = None
        # The list of Mobile threat Defense connectors configured by the tenant.
        self._mobile_threat_defense_connectors: Optional[List[mobile_threat_defense_connector.MobileThreatDefenseConnector]] = None
        # The Notification Message Templates.
        self._notification_message_templates: Optional[List[notification_message_template.NotificationMessageTemplate]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The remote assist partners.
        self._remote_assistance_partners: Optional[List[remote_assistance_partner.RemoteAssistancePartner]] = None
        # Reports singleton
        self._reports: Optional[device_management_reports.DeviceManagementReports] = None
        # The Resource Operations.
        self._resource_operations: Optional[List[resource_operation.ResourceOperation]] = None
        # The Role Assignments.
        self._role_assignments: Optional[List[device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment]] = None
        # The Role Definitions.
        self._role_definitions: Optional[List[role_definition.RoleDefinition]] = None
        # Account level settings.
        self._settings: Optional[device_management_settings.DeviceManagementSettings] = None
        # The software update status summary.
        self._software_update_status_summary: Optional[software_update_status_summary.SoftwareUpdateStatusSummary] = None
        # Tenant mobile device management subscription state.
        self._subscription_state: Optional[device_management_subscription_state.DeviceManagementSubscriptionState] = None
        # The telecom expense management partners.
        self._telecom_expense_management_partners: Optional[List[telecom_expense_management_partner.TelecomExpenseManagementPartner]] = None
        # The terms and conditions associated with device management of the company.
        self._terms_and_conditions: Optional[List[terms_and_conditions.TermsAndConditions]] = None
        # The list of troubleshooting events for the tenant.
        self._troubleshooting_events: Optional[List[device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent]] = None
        # The Windows autopilot device identities contained collection.
        self._windows_autopilot_device_identities: Optional[List[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]] = None
        # The windows information protection app learning summaries.
        self._windows_information_protection_app_learning_summaries: Optional[List[windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary]] = None
        # The windows information protection network learning summaries.
        self._windows_information_protection_network_learning_summaries: Optional[List[windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary]] = None
    
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
    
    @property
    def detected_apps(self,) -> Optional[List[detected_app.DetectedApp]]:
        """
        Gets the detectedApps property value. The list of detected apps associated with a device.
        Returns: Optional[List[detected_app.DetectedApp]]
        """
        return self._detected_apps
    
    @detected_apps.setter
    def detected_apps(self,value: Optional[List[detected_app.DetectedApp]] = None) -> None:
        """
        Sets the detectedApps property value. The list of detected apps associated with a device.
        Args:
            value: Value to set for the detectedApps property.
        """
        self._detected_apps = value
    
    @property
    def device_categories(self,) -> Optional[List[device_category.DeviceCategory]]:
        """
        Gets the deviceCategories property value. The list of device categories with the tenant.
        Returns: Optional[List[device_category.DeviceCategory]]
        """
        return self._device_categories
    
    @device_categories.setter
    def device_categories(self,value: Optional[List[device_category.DeviceCategory]] = None) -> None:
        """
        Sets the deviceCategories property value. The list of device categories with the tenant.
        Args:
            value: Value to set for the deviceCategories property.
        """
        self._device_categories = value
    
    @property
    def device_compliance_policies(self,) -> Optional[List[device_compliance_policy.DeviceCompliancePolicy]]:
        """
        Gets the deviceCompliancePolicies property value. The device compliance policies.
        Returns: Optional[List[device_compliance_policy.DeviceCompliancePolicy]]
        """
        return self._device_compliance_policies
    
    @device_compliance_policies.setter
    def device_compliance_policies(self,value: Optional[List[device_compliance_policy.DeviceCompliancePolicy]] = None) -> None:
        """
        Sets the deviceCompliancePolicies property value. The device compliance policies.
        Args:
            value: Value to set for the deviceCompliancePolicies property.
        """
        self._device_compliance_policies = value
    
    @property
    def device_compliance_policy_device_state_summary(self,) -> Optional[device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary]:
        """
        Gets the deviceCompliancePolicyDeviceStateSummary property value. The device compliance state summary for this account.
        Returns: Optional[device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary]
        """
        return self._device_compliance_policy_device_state_summary
    
    @device_compliance_policy_device_state_summary.setter
    def device_compliance_policy_device_state_summary(self,value: Optional[device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary] = None) -> None:
        """
        Sets the deviceCompliancePolicyDeviceStateSummary property value. The device compliance state summary for this account.
        Args:
            value: Value to set for the deviceCompliancePolicyDeviceStateSummary property.
        """
        self._device_compliance_policy_device_state_summary = value
    
    @property
    def device_compliance_policy_setting_state_summaries(self,) -> Optional[List[device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary]]:
        """
        Gets the deviceCompliancePolicySettingStateSummaries property value. The summary states of compliance policy settings for this account.
        Returns: Optional[List[device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary]]
        """
        return self._device_compliance_policy_setting_state_summaries
    
    @device_compliance_policy_setting_state_summaries.setter
    def device_compliance_policy_setting_state_summaries(self,value: Optional[List[device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary]] = None) -> None:
        """
        Sets the deviceCompliancePolicySettingStateSummaries property value. The summary states of compliance policy settings for this account.
        Args:
            value: Value to set for the deviceCompliancePolicySettingStateSummaries property.
        """
        self._device_compliance_policy_setting_state_summaries = value
    
    @property
    def device_configuration_device_state_summaries(self,) -> Optional[device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary]:
        """
        Gets the deviceConfigurationDeviceStateSummaries property value. The device configuration device state summary for this account.
        Returns: Optional[device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary]
        """
        return self._device_configuration_device_state_summaries
    
    @device_configuration_device_state_summaries.setter
    def device_configuration_device_state_summaries(self,value: Optional[device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary] = None) -> None:
        """
        Sets the deviceConfigurationDeviceStateSummaries property value. The device configuration device state summary for this account.
        Args:
            value: Value to set for the deviceConfigurationDeviceStateSummaries property.
        """
        self._device_configuration_device_state_summaries = value
    
    @property
    def device_configurations(self,) -> Optional[List[device_configuration.DeviceConfiguration]]:
        """
        Gets the deviceConfigurations property value. The device configurations.
        Returns: Optional[List[device_configuration.DeviceConfiguration]]
        """
        return self._device_configurations
    
    @device_configurations.setter
    def device_configurations(self,value: Optional[List[device_configuration.DeviceConfiguration]] = None) -> None:
        """
        Sets the deviceConfigurations property value. The device configurations.
        Args:
            value: Value to set for the deviceConfigurations property.
        """
        self._device_configurations = value
    
    @property
    def device_enrollment_configurations(self,) -> Optional[List[device_enrollment_configuration.DeviceEnrollmentConfiguration]]:
        """
        Gets the deviceEnrollmentConfigurations property value. The list of device enrollment configurations
        Returns: Optional[List[device_enrollment_configuration.DeviceEnrollmentConfiguration]]
        """
        return self._device_enrollment_configurations
    
    @device_enrollment_configurations.setter
    def device_enrollment_configurations(self,value: Optional[List[device_enrollment_configuration.DeviceEnrollmentConfiguration]] = None) -> None:
        """
        Sets the deviceEnrollmentConfigurations property value. The list of device enrollment configurations
        Args:
            value: Value to set for the deviceEnrollmentConfigurations property.
        """
        self._device_enrollment_configurations = value
    
    @property
    def device_management_partners(self,) -> Optional[List[device_management_partner.DeviceManagementPartner]]:
        """
        Gets the deviceManagementPartners property value. The list of Device Management Partners configured by the tenant.
        Returns: Optional[List[device_management_partner.DeviceManagementPartner]]
        """
        return self._device_management_partners
    
    @device_management_partners.setter
    def device_management_partners(self,value: Optional[List[device_management_partner.DeviceManagementPartner]] = None) -> None:
        """
        Sets the deviceManagementPartners property value. The list of Device Management Partners configured by the tenant.
        Args:
            value: Value to set for the deviceManagementPartners property.
        """
        self._device_management_partners = value
    
    @property
    def exchange_connectors(self,) -> Optional[List[device_management_exchange_connector.DeviceManagementExchangeConnector]]:
        """
        Gets the exchangeConnectors property value. The list of Exchange Connectors configured by the tenant.
        Returns: Optional[List[device_management_exchange_connector.DeviceManagementExchangeConnector]]
        """
        return self._exchange_connectors
    
    @exchange_connectors.setter
    def exchange_connectors(self,value: Optional[List[device_management_exchange_connector.DeviceManagementExchangeConnector]] = None) -> None:
        """
        Sets the exchangeConnectors property value. The list of Exchange Connectors configured by the tenant.
        Args:
            value: Value to set for the exchangeConnectors property.
        """
        self._exchange_connectors = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "apple_push_notification_certificate": lambda n : setattr(self, 'apple_push_notification_certificate', n.get_object_value(apple_push_notification_certificate.ApplePushNotificationCertificate)),
            "audit_events": lambda n : setattr(self, 'audit_events', n.get_collection_of_object_values(audit_event.AuditEvent)),
            "compliance_management_partners": lambda n : setattr(self, 'compliance_management_partners', n.get_collection_of_object_values(compliance_management_partner.ComplianceManagementPartner)),
            "conditional_access_settings": lambda n : setattr(self, 'conditional_access_settings', n.get_object_value(on_premises_conditional_access_settings.OnPremisesConditionalAccessSettings)),
            "detected_apps": lambda n : setattr(self, 'detected_apps', n.get_collection_of_object_values(detected_app.DetectedApp)),
            "device_categories": lambda n : setattr(self, 'device_categories', n.get_collection_of_object_values(device_category.DeviceCategory)),
            "device_compliance_policies": lambda n : setattr(self, 'device_compliance_policies', n.get_collection_of_object_values(device_compliance_policy.DeviceCompliancePolicy)),
            "device_compliance_policy_device_state_summary": lambda n : setattr(self, 'device_compliance_policy_device_state_summary', n.get_object_value(device_compliance_policy_device_state_summary.DeviceCompliancePolicyDeviceStateSummary)),
            "device_compliance_policy_setting_state_summaries": lambda n : setattr(self, 'device_compliance_policy_setting_state_summaries', n.get_collection_of_object_values(device_compliance_policy_setting_state_summary.DeviceCompliancePolicySettingStateSummary)),
            "device_configuration_device_state_summaries": lambda n : setattr(self, 'device_configuration_device_state_summaries', n.get_object_value(device_configuration_device_state_summary.DeviceConfigurationDeviceStateSummary)),
            "device_configurations": lambda n : setattr(self, 'device_configurations', n.get_collection_of_object_values(device_configuration.DeviceConfiguration)),
            "device_enrollment_configurations": lambda n : setattr(self, 'device_enrollment_configurations', n.get_collection_of_object_values(device_enrollment_configuration.DeviceEnrollmentConfiguration)),
            "device_management_partners": lambda n : setattr(self, 'device_management_partners', n.get_collection_of_object_values(device_management_partner.DeviceManagementPartner)),
            "exchange_connectors": lambda n : setattr(self, 'exchange_connectors', n.get_collection_of_object_values(device_management_exchange_connector.DeviceManagementExchangeConnector)),
            "imported_windows_autopilot_device_identities": lambda n : setattr(self, 'imported_windows_autopilot_device_identities', n.get_collection_of_object_values(imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity)),
            "intune_account_id": lambda n : setattr(self, 'intune_account_id', n.get_str_value()),
            "intune_brand": lambda n : setattr(self, 'intune_brand', n.get_object_value(intune_brand.IntuneBrand)),
            "ios_update_statuses": lambda n : setattr(self, 'ios_update_statuses', n.get_collection_of_object_values(ios_update_device_status.IosUpdateDeviceStatus)),
            "managed_device_overview": lambda n : setattr(self, 'managed_device_overview', n.get_object_value(managed_device_overview.ManagedDeviceOverview)),
            "managed_devices": lambda n : setattr(self, 'managed_devices', n.get_collection_of_object_values(managed_device.ManagedDevice)),
            "mobile_threat_defense_connectors": lambda n : setattr(self, 'mobile_threat_defense_connectors', n.get_collection_of_object_values(mobile_threat_defense_connector.MobileThreatDefenseConnector)),
            "notification_message_templates": lambda n : setattr(self, 'notification_message_templates', n.get_collection_of_object_values(notification_message_template.NotificationMessageTemplate)),
            "remote_assistance_partners": lambda n : setattr(self, 'remote_assistance_partners', n.get_collection_of_object_values(remote_assistance_partner.RemoteAssistancePartner)),
            "reports": lambda n : setattr(self, 'reports', n.get_object_value(device_management_reports.DeviceManagementReports)),
            "resource_operations": lambda n : setattr(self, 'resource_operations', n.get_collection_of_object_values(resource_operation.ResourceOperation)),
            "role_assignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment)),
            "role_definitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(role_definition.RoleDefinition)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(device_management_settings.DeviceManagementSettings)),
            "software_update_status_summary": lambda n : setattr(self, 'software_update_status_summary', n.get_object_value(software_update_status_summary.SoftwareUpdateStatusSummary)),
            "subscription_state": lambda n : setattr(self, 'subscription_state', n.get_enum_value(device_management_subscription_state.DeviceManagementSubscriptionState)),
            "telecom_expense_management_partners": lambda n : setattr(self, 'telecom_expense_management_partners', n.get_collection_of_object_values(telecom_expense_management_partner.TelecomExpenseManagementPartner)),
            "terms_and_conditions": lambda n : setattr(self, 'terms_and_conditions', n.get_collection_of_object_values(terms_and_conditions.TermsAndConditions)),
            "troubleshooting_events": lambda n : setattr(self, 'troubleshooting_events', n.get_collection_of_object_values(device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent)),
            "windows_autopilot_device_identities": lambda n : setattr(self, 'windows_autopilot_device_identities', n.get_collection_of_object_values(windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity)),
            "windows_information_protection_app_learning_summaries": lambda n : setattr(self, 'windows_information_protection_app_learning_summaries', n.get_collection_of_object_values(windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary)),
            "windows_information_protection_network_learning_summaries": lambda n : setattr(self, 'windows_information_protection_network_learning_summaries', n.get_collection_of_object_values(windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def imported_windows_autopilot_device_identities(self,) -> Optional[List[imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity]]:
        """
        Gets the importedWindowsAutopilotDeviceIdentities property value. Collection of imported Windows autopilot devices.
        Returns: Optional[List[imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity]]
        """
        return self._imported_windows_autopilot_device_identities
    
    @imported_windows_autopilot_device_identities.setter
    def imported_windows_autopilot_device_identities(self,value: Optional[List[imported_windows_autopilot_device_identity.ImportedWindowsAutopilotDeviceIdentity]] = None) -> None:
        """
        Sets the importedWindowsAutopilotDeviceIdentities property value. Collection of imported Windows autopilot devices.
        Args:
            value: Value to set for the importedWindowsAutopilotDeviceIdentities property.
        """
        self._imported_windows_autopilot_device_identities = value
    
    @property
    def intune_account_id(self,) -> Optional[str]:
        """
        Gets the intuneAccountId property value. Intune Account Id for given tenant
        Returns: Optional[str]
        """
        return self._intune_account_id
    
    @intune_account_id.setter
    def intune_account_id(self,value: Optional[str] = None) -> None:
        """
        Sets the intuneAccountId property value. Intune Account Id for given tenant
        Args:
            value: Value to set for the intuneAccountId property.
        """
        self._intune_account_id = value
    
    @property
    def intune_brand(self,) -> Optional[intune_brand.IntuneBrand]:
        """
        Gets the intuneBrand property value. intuneBrand contains data which is used in customizing the appearance of the Company Portal applications as well as the end user web portal.
        Returns: Optional[intune_brand.IntuneBrand]
        """
        return self._intune_brand
    
    @intune_brand.setter
    def intune_brand(self,value: Optional[intune_brand.IntuneBrand] = None) -> None:
        """
        Sets the intuneBrand property value. intuneBrand contains data which is used in customizing the appearance of the Company Portal applications as well as the end user web portal.
        Args:
            value: Value to set for the intuneBrand property.
        """
        self._intune_brand = value
    
    @property
    def ios_update_statuses(self,) -> Optional[List[ios_update_device_status.IosUpdateDeviceStatus]]:
        """
        Gets the iosUpdateStatuses property value. The IOS software update installation statuses for this account.
        Returns: Optional[List[ios_update_device_status.IosUpdateDeviceStatus]]
        """
        return self._ios_update_statuses
    
    @ios_update_statuses.setter
    def ios_update_statuses(self,value: Optional[List[ios_update_device_status.IosUpdateDeviceStatus]] = None) -> None:
        """
        Sets the iosUpdateStatuses property value. The IOS software update installation statuses for this account.
        Args:
            value: Value to set for the iosUpdateStatuses property.
        """
        self._ios_update_statuses = value
    
    @property
    def managed_device_overview(self,) -> Optional[managed_device_overview.ManagedDeviceOverview]:
        """
        Gets the managedDeviceOverview property value. Device overview
        Returns: Optional[managed_device_overview.ManagedDeviceOverview]
        """
        return self._managed_device_overview
    
    @managed_device_overview.setter
    def managed_device_overview(self,value: Optional[managed_device_overview.ManagedDeviceOverview] = None) -> None:
        """
        Sets the managedDeviceOverview property value. Device overview
        Args:
            value: Value to set for the managedDeviceOverview property.
        """
        self._managed_device_overview = value
    
    @property
    def managed_devices(self,) -> Optional[List[managed_device.ManagedDevice]]:
        """
        Gets the managedDevices property value. The list of managed devices.
        Returns: Optional[List[managed_device.ManagedDevice]]
        """
        return self._managed_devices
    
    @managed_devices.setter
    def managed_devices(self,value: Optional[List[managed_device.ManagedDevice]] = None) -> None:
        """
        Sets the managedDevices property value. The list of managed devices.
        Args:
            value: Value to set for the managedDevices property.
        """
        self._managed_devices = value
    
    @property
    def mobile_threat_defense_connectors(self,) -> Optional[List[mobile_threat_defense_connector.MobileThreatDefenseConnector]]:
        """
        Gets the mobileThreatDefenseConnectors property value. The list of Mobile threat Defense connectors configured by the tenant.
        Returns: Optional[List[mobile_threat_defense_connector.MobileThreatDefenseConnector]]
        """
        return self._mobile_threat_defense_connectors
    
    @mobile_threat_defense_connectors.setter
    def mobile_threat_defense_connectors(self,value: Optional[List[mobile_threat_defense_connector.MobileThreatDefenseConnector]] = None) -> None:
        """
        Sets the mobileThreatDefenseConnectors property value. The list of Mobile threat Defense connectors configured by the tenant.
        Args:
            value: Value to set for the mobileThreatDefenseConnectors property.
        """
        self._mobile_threat_defense_connectors = value
    
    @property
    def notification_message_templates(self,) -> Optional[List[notification_message_template.NotificationMessageTemplate]]:
        """
        Gets the notificationMessageTemplates property value. The Notification Message Templates.
        Returns: Optional[List[notification_message_template.NotificationMessageTemplate]]
        """
        return self._notification_message_templates
    
    @notification_message_templates.setter
    def notification_message_templates(self,value: Optional[List[notification_message_template.NotificationMessageTemplate]] = None) -> None:
        """
        Sets the notificationMessageTemplates property value. The Notification Message Templates.
        Args:
            value: Value to set for the notificationMessageTemplates property.
        """
        self._notification_message_templates = value
    
    @property
    def remote_assistance_partners(self,) -> Optional[List[remote_assistance_partner.RemoteAssistancePartner]]:
        """
        Gets the remoteAssistancePartners property value. The remote assist partners.
        Returns: Optional[List[remote_assistance_partner.RemoteAssistancePartner]]
        """
        return self._remote_assistance_partners
    
    @remote_assistance_partners.setter
    def remote_assistance_partners(self,value: Optional[List[remote_assistance_partner.RemoteAssistancePartner]] = None) -> None:
        """
        Sets the remoteAssistancePartners property value. The remote assist partners.
        Args:
            value: Value to set for the remoteAssistancePartners property.
        """
        self._remote_assistance_partners = value
    
    @property
    def reports(self,) -> Optional[device_management_reports.DeviceManagementReports]:
        """
        Gets the reports property value. Reports singleton
        Returns: Optional[device_management_reports.DeviceManagementReports]
        """
        return self._reports
    
    @reports.setter
    def reports(self,value: Optional[device_management_reports.DeviceManagementReports] = None) -> None:
        """
        Sets the reports property value. Reports singleton
        Args:
            value: Value to set for the reports property.
        """
        self._reports = value
    
    @property
    def resource_operations(self,) -> Optional[List[resource_operation.ResourceOperation]]:
        """
        Gets the resourceOperations property value. The Resource Operations.
        Returns: Optional[List[resource_operation.ResourceOperation]]
        """
        return self._resource_operations
    
    @resource_operations.setter
    def resource_operations(self,value: Optional[List[resource_operation.ResourceOperation]] = None) -> None:
        """
        Sets the resourceOperations property value. The Resource Operations.
        Args:
            value: Value to set for the resourceOperations property.
        """
        self._resource_operations = value
    
    @property
    def role_assignments(self,) -> Optional[List[device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment]]:
        """
        Gets the roleAssignments property value. The Role Assignments.
        Returns: Optional[List[device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment]]
        """
        return self._role_assignments
    
    @role_assignments.setter
    def role_assignments(self,value: Optional[List[device_and_app_management_role_assignment.DeviceAndAppManagementRoleAssignment]] = None) -> None:
        """
        Sets the roleAssignments property value. The Role Assignments.
        Args:
            value: Value to set for the roleAssignments property.
        """
        self._role_assignments = value
    
    @property
    def role_definitions(self,) -> Optional[List[role_definition.RoleDefinition]]:
        """
        Gets the roleDefinitions property value. The Role Definitions.
        Returns: Optional[List[role_definition.RoleDefinition]]
        """
        return self._role_definitions
    
    @role_definitions.setter
    def role_definitions(self,value: Optional[List[role_definition.RoleDefinition]] = None) -> None:
        """
        Sets the roleDefinitions property value. The Role Definitions.
        Args:
            value: Value to set for the roleDefinitions property.
        """
        self._role_definitions = value
    
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
        writer.write_object_value("deviceConfigurationDeviceStateSummaries", self.device_configuration_device_state_summaries)
        writer.write_collection_of_object_values("deviceConfigurations", self.device_configurations)
        writer.write_collection_of_object_values("deviceEnrollmentConfigurations", self.device_enrollment_configurations)
        writer.write_collection_of_object_values("deviceManagementPartners", self.device_management_partners)
        writer.write_collection_of_object_values("exchangeConnectors", self.exchange_connectors)
        writer.write_collection_of_object_values("importedWindowsAutopilotDeviceIdentities", self.imported_windows_autopilot_device_identities)
        writer.write_str_value("intuneAccountId", self.intune_account_id)
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
    
    @property
    def settings(self,) -> Optional[device_management_settings.DeviceManagementSettings]:
        """
        Gets the settings property value. Account level settings.
        Returns: Optional[device_management_settings.DeviceManagementSettings]
        """
        return self._settings
    
    @settings.setter
    def settings(self,value: Optional[device_management_settings.DeviceManagementSettings] = None) -> None:
        """
        Sets the settings property value. Account level settings.
        Args:
            value: Value to set for the settings property.
        """
        self._settings = value
    
    @property
    def software_update_status_summary(self,) -> Optional[software_update_status_summary.SoftwareUpdateStatusSummary]:
        """
        Gets the softwareUpdateStatusSummary property value. The software update status summary.
        Returns: Optional[software_update_status_summary.SoftwareUpdateStatusSummary]
        """
        return self._software_update_status_summary
    
    @software_update_status_summary.setter
    def software_update_status_summary(self,value: Optional[software_update_status_summary.SoftwareUpdateStatusSummary] = None) -> None:
        """
        Sets the softwareUpdateStatusSummary property value. The software update status summary.
        Args:
            value: Value to set for the softwareUpdateStatusSummary property.
        """
        self._software_update_status_summary = value
    
    @property
    def subscription_state(self,) -> Optional[device_management_subscription_state.DeviceManagementSubscriptionState]:
        """
        Gets the subscriptionState property value. Tenant mobile device management subscription state.
        Returns: Optional[device_management_subscription_state.DeviceManagementSubscriptionState]
        """
        return self._subscription_state
    
    @subscription_state.setter
    def subscription_state(self,value: Optional[device_management_subscription_state.DeviceManagementSubscriptionState] = None) -> None:
        """
        Sets the subscriptionState property value. Tenant mobile device management subscription state.
        Args:
            value: Value to set for the subscriptionState property.
        """
        self._subscription_state = value
    
    @property
    def telecom_expense_management_partners(self,) -> Optional[List[telecom_expense_management_partner.TelecomExpenseManagementPartner]]:
        """
        Gets the telecomExpenseManagementPartners property value. The telecom expense management partners.
        Returns: Optional[List[telecom_expense_management_partner.TelecomExpenseManagementPartner]]
        """
        return self._telecom_expense_management_partners
    
    @telecom_expense_management_partners.setter
    def telecom_expense_management_partners(self,value: Optional[List[telecom_expense_management_partner.TelecomExpenseManagementPartner]] = None) -> None:
        """
        Sets the telecomExpenseManagementPartners property value. The telecom expense management partners.
        Args:
            value: Value to set for the telecomExpenseManagementPartners property.
        """
        self._telecom_expense_management_partners = value
    
    @property
    def terms_and_conditions(self,) -> Optional[List[terms_and_conditions.TermsAndConditions]]:
        """
        Gets the termsAndConditions property value. The terms and conditions associated with device management of the company.
        Returns: Optional[List[terms_and_conditions.TermsAndConditions]]
        """
        return self._terms_and_conditions
    
    @terms_and_conditions.setter
    def terms_and_conditions(self,value: Optional[List[terms_and_conditions.TermsAndConditions]] = None) -> None:
        """
        Sets the termsAndConditions property value. The terms and conditions associated with device management of the company.
        Args:
            value: Value to set for the termsAndConditions property.
        """
        self._terms_and_conditions = value
    
    @property
    def troubleshooting_events(self,) -> Optional[List[device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent]]:
        """
        Gets the troubleshootingEvents property value. The list of troubleshooting events for the tenant.
        Returns: Optional[List[device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent]]
        """
        return self._troubleshooting_events
    
    @troubleshooting_events.setter
    def troubleshooting_events(self,value: Optional[List[device_management_troubleshooting_event.DeviceManagementTroubleshootingEvent]] = None) -> None:
        """
        Sets the troubleshootingEvents property value. The list of troubleshooting events for the tenant.
        Args:
            value: Value to set for the troubleshootingEvents property.
        """
        self._troubleshooting_events = value
    
    @property
    def windows_autopilot_device_identities(self,) -> Optional[List[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]]:
        """
        Gets the windowsAutopilotDeviceIdentities property value. The Windows autopilot device identities contained collection.
        Returns: Optional[List[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]]
        """
        return self._windows_autopilot_device_identities
    
    @windows_autopilot_device_identities.setter
    def windows_autopilot_device_identities(self,value: Optional[List[windows_autopilot_device_identity.WindowsAutopilotDeviceIdentity]] = None) -> None:
        """
        Sets the windowsAutopilotDeviceIdentities property value. The Windows autopilot device identities contained collection.
        Args:
            value: Value to set for the windowsAutopilotDeviceIdentities property.
        """
        self._windows_autopilot_device_identities = value
    
    @property
    def windows_information_protection_app_learning_summaries(self,) -> Optional[List[windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary]]:
        """
        Gets the windowsInformationProtectionAppLearningSummaries property value. The windows information protection app learning summaries.
        Returns: Optional[List[windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary]]
        """
        return self._windows_information_protection_app_learning_summaries
    
    @windows_information_protection_app_learning_summaries.setter
    def windows_information_protection_app_learning_summaries(self,value: Optional[List[windows_information_protection_app_learning_summary.WindowsInformationProtectionAppLearningSummary]] = None) -> None:
        """
        Sets the windowsInformationProtectionAppLearningSummaries property value. The windows information protection app learning summaries.
        Args:
            value: Value to set for the windowsInformationProtectionAppLearningSummaries property.
        """
        self._windows_information_protection_app_learning_summaries = value
    
    @property
    def windows_information_protection_network_learning_summaries(self,) -> Optional[List[windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary]]:
        """
        Gets the windowsInformationProtectionNetworkLearningSummaries property value. The windows information protection network learning summaries.
        Returns: Optional[List[windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary]]
        """
        return self._windows_information_protection_network_learning_summaries
    
    @windows_information_protection_network_learning_summaries.setter
    def windows_information_protection_network_learning_summaries(self,value: Optional[List[windows_information_protection_network_learning_summary.WindowsInformationProtectionNetworkLearningSummary]] = None) -> None:
        """
        Sets the windowsInformationProtectionNetworkLearningSummaries property value. The windows information protection network learning summaries.
        Args:
            value: Value to set for the windowsInformationProtectionNetworkLearningSummaries property.
        """
        self._windows_information_protection_network_learning_summaries = value
    

