from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, Union

from ..models import device_management
from ..models.o_data_errors import o_data_error
from .apple_push_notification_certificate import apple_push_notification_certificate_request_builder
from .audit_events import audit_events_request_builder
from .audit_events.item import audit_event_item_request_builder
from .compliance_management_partners import compliance_management_partners_request_builder
from .compliance_management_partners.item import compliance_management_partner_item_request_builder
from .conditional_access_settings import conditional_access_settings_request_builder
from .detected_apps import detected_apps_request_builder
from .detected_apps.item import detected_app_item_request_builder
from .device_categories import device_categories_request_builder
from .device_categories.item import device_category_item_request_builder
from .device_compliance_policies import device_compliance_policies_request_builder
from .device_compliance_policies.item import device_compliance_policy_item_request_builder
from .device_compliance_policy_device_state_summary import device_compliance_policy_device_state_summary_request_builder
from .device_compliance_policy_setting_state_summaries import device_compliance_policy_setting_state_summaries_request_builder
from .device_compliance_policy_setting_state_summaries.item import device_compliance_policy_setting_state_summary_item_request_builder
from .device_configuration_device_state_summaries import device_configuration_device_state_summaries_request_builder
from .device_configurations import device_configurations_request_builder
from .device_configurations.item import device_configuration_item_request_builder
from .device_enrollment_configurations import device_enrollment_configurations_request_builder
from .device_enrollment_configurations.item import device_enrollment_configuration_item_request_builder
from .device_management_partners import device_management_partners_request_builder
from .device_management_partners.item import device_management_partner_item_request_builder
from .exchange_connectors import exchange_connectors_request_builder
from .exchange_connectors.item import device_management_exchange_connector_item_request_builder
from .get_effective_permissions_with_scope import get_effective_permissions_with_scope_request_builder
from .imported_windows_autopilot_device_identities import imported_windows_autopilot_device_identities_request_builder
from .imported_windows_autopilot_device_identities.item import imported_windows_autopilot_device_identity_item_request_builder
from .ios_update_statuses import ios_update_statuses_request_builder
from .ios_update_statuses.item import ios_update_device_status_item_request_builder
from .managed_device_overview import managed_device_overview_request_builder
from .managed_devices import managed_devices_request_builder
from .managed_devices.item import managed_device_item_request_builder
from .mobile_threat_defense_connectors import mobile_threat_defense_connectors_request_builder
from .mobile_threat_defense_connectors.item import mobile_threat_defense_connector_item_request_builder
from .notification_message_templates import notification_message_templates_request_builder
from .notification_message_templates.item import notification_message_template_item_request_builder
from .remote_assistance_partners import remote_assistance_partners_request_builder
from .remote_assistance_partners.item import remote_assistance_partner_item_request_builder
from .reports import reports_request_builder
from .resource_operations import resource_operations_request_builder
from .resource_operations.item import resource_operation_item_request_builder
from .role_assignments import role_assignments_request_builder
from .role_assignments.item import device_and_app_management_role_assignment_item_request_builder
from .role_definitions import role_definitions_request_builder
from .role_definitions.item import role_definition_item_request_builder
from .software_update_status_summary import software_update_status_summary_request_builder
from .telecom_expense_management_partners import telecom_expense_management_partners_request_builder
from .telecom_expense_management_partners.item import telecom_expense_management_partner_item_request_builder
from .terms_and_conditions import terms_and_conditions_request_builder
from .terms_and_conditions.item import terms_and_conditions_item_request_builder
from .troubleshooting_events import troubleshooting_events_request_builder
from .troubleshooting_events.item import device_management_troubleshooting_event_item_request_builder
from .verify_windows_enrollment_auto_discovery_with_domain_name import verify_windows_enrollment_auto_discovery_with_domain_name_request_builder
from .windows_autopilot_device_identities import windows_autopilot_device_identities_request_builder
from .windows_autopilot_device_identities.item import windows_autopilot_device_identity_item_request_builder
from .windows_information_protection_app_learning_summaries import windows_information_protection_app_learning_summaries_request_builder
from .windows_information_protection_app_learning_summaries.item import windows_information_protection_app_learning_summary_item_request_builder
from .windows_information_protection_network_learning_summaries import windows_information_protection_network_learning_summaries_request_builder
from .windows_information_protection_network_learning_summaries.item import windows_information_protection_network_learning_summary_item_request_builder

class DeviceManagementRequestBuilder():
    """
    Provides operations to manage the deviceManagement singleton.
    """
    def apple_push_notification_certificate(self) -> apple_push_notification_certificate_request_builder.ApplePushNotificationCertificateRequestBuilder:
        """
        Provides operations to manage the applePushNotificationCertificate property of the microsoft.graph.deviceManagement entity.
        """
        return apple_push_notification_certificate_request_builder.ApplePushNotificationCertificateRequestBuilder(self.request_adapter, self.path_parameters)

    def audit_events(self) -> audit_events_request_builder.AuditEventsRequestBuilder:
        """
        Provides operations to manage the auditEvents property of the microsoft.graph.deviceManagement entity.
        """
        return audit_events_request_builder.AuditEventsRequestBuilder(self.request_adapter, self.path_parameters)

    def compliance_management_partners(self) -> compliance_management_partners_request_builder.ComplianceManagementPartnersRequestBuilder:
        """
        Provides operations to manage the complianceManagementPartners property of the microsoft.graph.deviceManagement entity.
        """
        return compliance_management_partners_request_builder.ComplianceManagementPartnersRequestBuilder(self.request_adapter, self.path_parameters)

    def conditional_access_settings(self) -> conditional_access_settings_request_builder.ConditionalAccessSettingsRequestBuilder:
        """
        Provides operations to manage the conditionalAccessSettings property of the microsoft.graph.deviceManagement entity.
        """
        return conditional_access_settings_request_builder.ConditionalAccessSettingsRequestBuilder(self.request_adapter, self.path_parameters)

    def detected_apps(self) -> detected_apps_request_builder.DetectedAppsRequestBuilder:
        """
        Provides operations to manage the detectedApps property of the microsoft.graph.deviceManagement entity.
        """
        return detected_apps_request_builder.DetectedAppsRequestBuilder(self.request_adapter, self.path_parameters)

    def device_categories(self) -> device_categories_request_builder.DeviceCategoriesRequestBuilder:
        """
        Provides operations to manage the deviceCategories property of the microsoft.graph.deviceManagement entity.
        """
        return device_categories_request_builder.DeviceCategoriesRequestBuilder(self.request_adapter, self.path_parameters)

    def device_compliance_policies(self) -> device_compliance_policies_request_builder.DeviceCompliancePoliciesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicies property of the microsoft.graph.deviceManagement entity.
        """
        return device_compliance_policies_request_builder.DeviceCompliancePoliciesRequestBuilder(self.request_adapter, self.path_parameters)

    def device_compliance_policy_device_state_summary(self) -> device_compliance_policy_device_state_summary_request_builder.DeviceCompliancePolicyDeviceStateSummaryRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicyDeviceStateSummary property of the microsoft.graph.deviceManagement entity.
        """
        return device_compliance_policy_device_state_summary_request_builder.DeviceCompliancePolicyDeviceStateSummaryRequestBuilder(self.request_adapter, self.path_parameters)

    def device_compliance_policy_setting_state_summaries(self) -> device_compliance_policy_setting_state_summaries_request_builder.DeviceCompliancePolicySettingStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicySettingStateSummaries property of the microsoft.graph.deviceManagement entity.
        """
        return device_compliance_policy_setting_state_summaries_request_builder.DeviceCompliancePolicySettingStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)

    def device_configuration_device_state_summaries(self) -> device_configuration_device_state_summaries_request_builder.DeviceConfigurationDeviceStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationDeviceStateSummaries property of the microsoft.graph.deviceManagement entity.
        """
        return device_configuration_device_state_summaries_request_builder.DeviceConfigurationDeviceStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)

    def device_configurations(self) -> device_configurations_request_builder.DeviceConfigurationsRequestBuilder:
        """
        Provides operations to manage the deviceConfigurations property of the microsoft.graph.deviceManagement entity.
        """
        return device_configurations_request_builder.DeviceConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)

    def device_enrollment_configurations(self) -> device_enrollment_configurations_request_builder.DeviceEnrollmentConfigurationsRequestBuilder:
        """
        Provides operations to manage the deviceEnrollmentConfigurations property of the microsoft.graph.deviceManagement entity.
        """
        return device_enrollment_configurations_request_builder.DeviceEnrollmentConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)

    def device_management_partners(self) -> device_management_partners_request_builder.DeviceManagementPartnersRequestBuilder:
        """
        Provides operations to manage the deviceManagementPartners property of the microsoft.graph.deviceManagement entity.
        """
        return device_management_partners_request_builder.DeviceManagementPartnersRequestBuilder(self.request_adapter, self.path_parameters)

    def exchange_connectors(self) -> exchange_connectors_request_builder.ExchangeConnectorsRequestBuilder:
        """
        Provides operations to manage the exchangeConnectors property of the microsoft.graph.deviceManagement entity.
        """
        return exchange_connectors_request_builder.ExchangeConnectorsRequestBuilder(self.request_adapter, self.path_parameters)

    def imported_windows_autopilot_device_identities(self) -> imported_windows_autopilot_device_identities_request_builder.ImportedWindowsAutopilotDeviceIdentitiesRequestBuilder:
        """
        Provides operations to manage the importedWindowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        """
        return imported_windows_autopilot_device_identities_request_builder.ImportedWindowsAutopilotDeviceIdentitiesRequestBuilder(self.request_adapter, self.path_parameters)

    def ios_update_statuses(self) -> ios_update_statuses_request_builder.IosUpdateStatusesRequestBuilder:
        """
        Provides operations to manage the iosUpdateStatuses property of the microsoft.graph.deviceManagement entity.
        """
        return ios_update_statuses_request_builder.IosUpdateStatusesRequestBuilder(self.request_adapter, self.path_parameters)

    def managed_device_overview(self) -> managed_device_overview_request_builder.ManagedDeviceOverviewRequestBuilder:
        """
        Provides operations to manage the managedDeviceOverview property of the microsoft.graph.deviceManagement entity.
        """
        return managed_device_overview_request_builder.ManagedDeviceOverviewRequestBuilder(self.request_adapter, self.path_parameters)

    def managed_devices(self) -> managed_devices_request_builder.ManagedDevicesRequestBuilder:
        """
        Provides operations to manage the managedDevices property of the microsoft.graph.deviceManagement entity.
        """
        return managed_devices_request_builder.ManagedDevicesRequestBuilder(self.request_adapter, self.path_parameters)

    def mobile_threat_defense_connectors(self) -> mobile_threat_defense_connectors_request_builder.MobileThreatDefenseConnectorsRequestBuilder:
        """
        Provides operations to manage the mobileThreatDefenseConnectors property of the microsoft.graph.deviceManagement entity.
        """
        return mobile_threat_defense_connectors_request_builder.MobileThreatDefenseConnectorsRequestBuilder(self.request_adapter, self.path_parameters)

    def notification_message_templates(self) -> notification_message_templates_request_builder.NotificationMessageTemplatesRequestBuilder:
        """
        Provides operations to manage the notificationMessageTemplates property of the microsoft.graph.deviceManagement entity.
        """
        return notification_message_templates_request_builder.NotificationMessageTemplatesRequestBuilder(self.request_adapter, self.path_parameters)

    def remote_assistance_partners(self) -> remote_assistance_partners_request_builder.RemoteAssistancePartnersRequestBuilder:
        """
        Provides operations to manage the remoteAssistancePartners property of the microsoft.graph.deviceManagement entity.
        """
        return remote_assistance_partners_request_builder.RemoteAssistancePartnersRequestBuilder(self.request_adapter, self.path_parameters)

    def reports(self) -> reports_request_builder.ReportsRequestBuilder:
        """
        Provides operations to manage the reports property of the microsoft.graph.deviceManagement entity.
        """
        return reports_request_builder.ReportsRequestBuilder(self.request_adapter, self.path_parameters)

    def resource_operations(self) -> resource_operations_request_builder.ResourceOperationsRequestBuilder:
        """
        Provides operations to manage the resourceOperations property of the microsoft.graph.deviceManagement entity.
        """
        return resource_operations_request_builder.ResourceOperationsRequestBuilder(self.request_adapter, self.path_parameters)

    def role_assignments(self) -> role_assignments_request_builder.RoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.deviceManagement entity.
        """
        return role_assignments_request_builder.RoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)

    def role_definitions(self) -> role_definitions_request_builder.RoleDefinitionsRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.deviceManagement entity.
        """
        return role_definitions_request_builder.RoleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)

    def software_update_status_summary(self) -> software_update_status_summary_request_builder.SoftwareUpdateStatusSummaryRequestBuilder:
        """
        Provides operations to manage the softwareUpdateStatusSummary property of the microsoft.graph.deviceManagement entity.
        """
        return software_update_status_summary_request_builder.SoftwareUpdateStatusSummaryRequestBuilder(self.request_adapter, self.path_parameters)

    def telecom_expense_management_partners(self) -> telecom_expense_management_partners_request_builder.TelecomExpenseManagementPartnersRequestBuilder:
        """
        Provides operations to manage the telecomExpenseManagementPartners property of the microsoft.graph.deviceManagement entity.
        """
        return telecom_expense_management_partners_request_builder.TelecomExpenseManagementPartnersRequestBuilder(self.request_adapter, self.path_parameters)

    def terms_and_conditions(self) -> terms_and_conditions_request_builder.TermsAndConditionsRequestBuilder:
        """
        Provides operations to manage the termsAndConditions property of the microsoft.graph.deviceManagement entity.
        """
        return terms_and_conditions_request_builder.TermsAndConditionsRequestBuilder(self.request_adapter, self.path_parameters)

    def troubleshooting_events(self) -> troubleshooting_events_request_builder.TroubleshootingEventsRequestBuilder:
        """
        Provides operations to manage the troubleshootingEvents property of the microsoft.graph.deviceManagement entity.
        """
        return troubleshooting_events_request_builder.TroubleshootingEventsRequestBuilder(self.request_adapter, self.path_parameters)

    def windows_autopilot_device_identities(self) -> windows_autopilot_device_identities_request_builder.WindowsAutopilotDeviceIdentitiesRequestBuilder:
        """
        Provides operations to manage the windowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        """
        return windows_autopilot_device_identities_request_builder.WindowsAutopilotDeviceIdentitiesRequestBuilder(self.request_adapter, self.path_parameters)

    def windows_information_protection_app_learning_summaries(self) -> windows_information_protection_app_learning_summaries_request_builder.WindowsInformationProtectionAppLearningSummariesRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionAppLearningSummaries property of the microsoft.graph.deviceManagement entity.
        """
        return windows_information_protection_app_learning_summaries_request_builder.WindowsInformationProtectionAppLearningSummariesRequestBuilder(self.request_adapter, self.path_parameters)

    def windows_information_protection_network_learning_summaries(self) -> windows_information_protection_network_learning_summaries_request_builder.WindowsInformationProtectionNetworkLearningSummariesRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionNetworkLearningSummaries property of the microsoft.graph.deviceManagement entity.
        """
        return windows_information_protection_network_learning_summaries_request_builder.WindowsInformationProtectionNetworkLearningSummariesRequestBuilder(self.request_adapter, self.path_parameters)

    def audit_events_by_id(self,id: str) -> audit_event_item_request_builder.AuditEventItemRequestBuilder:
        """
        Provides operations to manage the auditEvents property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: audit_event_item_request_builder.AuditEventItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["auditEvent%2Did"] = id
        return audit_event_item_request_builder.AuditEventItemRequestBuilder(self.request_adapter, url_tpl_params)

    def compliance_management_partners_by_id(self,id: str) -> compliance_management_partner_item_request_builder.ComplianceManagementPartnerItemRequestBuilder:
        """
        Provides operations to manage the complianceManagementPartners property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: compliance_management_partner_item_request_builder.ComplianceManagementPartnerItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["complianceManagementPartner%2Did"] = id
        return compliance_management_partner_item_request_builder.ComplianceManagementPartnerItemRequestBuilder(self.request_adapter, url_tpl_params)

    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceManagementRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise Exception("path_parameters cannot be undefined")
        if not request_adapter:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter

    def create_get_request_information(self,request_configuration: Optional[DeviceManagementRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info

    def create_patch_request_information(self,body: Optional[device_management.DeviceManagement] = None, request_configuration: Optional[DeviceManagementRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update deviceManagement
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info

    def detected_apps_by_id(self,id: str) -> detected_app_item_request_builder.DetectedAppItemRequestBuilder:
        """
        Provides operations to manage the detectedApps property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: detected_app_item_request_builder.DetectedAppItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["detectedApp%2Did"] = id
        return detected_app_item_request_builder.DetectedAppItemRequestBuilder(self.request_adapter, url_tpl_params)

    def device_categories_by_id(self,id: str) -> device_category_item_request_builder.DeviceCategoryItemRequestBuilder:
        """
        Provides operations to manage the deviceCategories property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_category_item_request_builder.DeviceCategoryItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceCategory%2Did"] = id
        return device_category_item_request_builder.DeviceCategoryItemRequestBuilder(self.request_adapter, url_tpl_params)

    def device_compliance_policies_by_id(self,id: str) -> device_compliance_policy_item_request_builder.DeviceCompliancePolicyItemRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicies property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_compliance_policy_item_request_builder.DeviceCompliancePolicyItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceCompliancePolicy%2Did"] = id
        return device_compliance_policy_item_request_builder.DeviceCompliancePolicyItemRequestBuilder(self.request_adapter, url_tpl_params)

    def device_compliance_policy_setting_state_summaries_by_id(self,id: str) -> device_compliance_policy_setting_state_summary_item_request_builder.DeviceCompliancePolicySettingStateSummaryItemRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicySettingStateSummaries property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_compliance_policy_setting_state_summary_item_request_builder.DeviceCompliancePolicySettingStateSummaryItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceCompliancePolicySettingStateSummary%2Did"] = id
        return device_compliance_policy_setting_state_summary_item_request_builder.DeviceCompliancePolicySettingStateSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)

    def device_configurations_by_id(self,id: str) -> device_configuration_item_request_builder.DeviceConfigurationItemRequestBuilder:
        """
        Provides operations to manage the deviceConfigurations property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_configuration_item_request_builder.DeviceConfigurationItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceConfiguration%2Did"] = id
        return device_configuration_item_request_builder.DeviceConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)

    def device_enrollment_configurations_by_id(self,id: str) -> device_enrollment_configuration_item_request_builder.DeviceEnrollmentConfigurationItemRequestBuilder:
        """
        Provides operations to manage the deviceEnrollmentConfigurations property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_enrollment_configuration_item_request_builder.DeviceEnrollmentConfigurationItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceEnrollmentConfiguration%2Did"] = id
        return device_enrollment_configuration_item_request_builder.DeviceEnrollmentConfigurationItemRequestBuilder(self.request_adapter, url_tpl_params)

    def device_management_partners_by_id(self,id: str) -> device_management_partner_item_request_builder.DeviceManagementPartnerItemRequestBuilder:
        """
        Provides operations to manage the deviceManagementPartners property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_partner_item_request_builder.DeviceManagementPartnerItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementPartner%2Did"] = id
        return device_management_partner_item_request_builder.DeviceManagementPartnerItemRequestBuilder(self.request_adapter, url_tpl_params)

    def exchange_connectors_by_id(self,id: str) -> device_management_exchange_connector_item_request_builder.DeviceManagementExchangeConnectorItemRequestBuilder:
        """
        Provides operations to manage the exchangeConnectors property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_exchange_connector_item_request_builder.DeviceManagementExchangeConnectorItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementExchangeConnector%2Did"] = id
        return device_management_exchange_connector_item_request_builder.DeviceManagementExchangeConnectorItemRequestBuilder(self.request_adapter, url_tpl_params)

    async def get(self,request_configuration: Optional[DeviceManagementRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_management.DeviceManagement]:
        """
        Get deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_management.DeviceManagement]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, device_management.DeviceManagement, response_handler, error_mapping)

    def get_effective_permissions_with_scope(self,scope: Optional[str] = None) -> get_effective_permissions_with_scope_request_builder.GetEffectivePermissionsWithScopeRequestBuilder:
        """
        Provides operations to call the getEffectivePermissions method.
        Args:
            scope: Usage: scope='{scope}'
        Returns: get_effective_permissions_with_scope_request_builder.GetEffectivePermissionsWithScopeRequestBuilder
        """
        if not scope:
            raise Exception("scope cannot be undefined")
        return get_effective_permissions_with_scope_request_builder.GetEffectivePermissionsWithScopeRequestBuilder(self.request_adapter, self.path_parameters, scope)

    def imported_windows_autopilot_device_identities_by_id(self,id: str) -> imported_windows_autopilot_device_identity_item_request_builder.ImportedWindowsAutopilotDeviceIdentityItemRequestBuilder:
        """
        Provides operations to manage the importedWindowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: imported_windows_autopilot_device_identity_item_request_builder.ImportedWindowsAutopilotDeviceIdentityItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["importedWindowsAutopilotDeviceIdentity%2Did"] = id
        return imported_windows_autopilot_device_identity_item_request_builder.ImportedWindowsAutopilotDeviceIdentityItemRequestBuilder(self.request_adapter, url_tpl_params)

    def ios_update_statuses_by_id(self,id: str) -> ios_update_device_status_item_request_builder.IosUpdateDeviceStatusItemRequestBuilder:
        """
        Provides operations to manage the iosUpdateStatuses property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: ios_update_device_status_item_request_builder.IosUpdateDeviceStatusItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["iosUpdateDeviceStatus%2Did"] = id
        return ios_update_device_status_item_request_builder.IosUpdateDeviceStatusItemRequestBuilder(self.request_adapter, url_tpl_params)

    def managed_devices_by_id(self,id: str) -> managed_device_item_request_builder.ManagedDeviceItemRequestBuilder:
        """
        Provides operations to manage the managedDevices property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: managed_device_item_request_builder.ManagedDeviceItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["managedDevice%2Did"] = id
        return managed_device_item_request_builder.ManagedDeviceItemRequestBuilder(self.request_adapter, url_tpl_params)

    def mobile_threat_defense_connectors_by_id(self,id: str) -> mobile_threat_defense_connector_item_request_builder.MobileThreatDefenseConnectorItemRequestBuilder:
        """
        Provides operations to manage the mobileThreatDefenseConnectors property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: mobile_threat_defense_connector_item_request_builder.MobileThreatDefenseConnectorItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mobileThreatDefenseConnector%2Did"] = id
        return mobile_threat_defense_connector_item_request_builder.MobileThreatDefenseConnectorItemRequestBuilder(self.request_adapter, url_tpl_params)

    def notification_message_templates_by_id(self,id: str) -> notification_message_template_item_request_builder.NotificationMessageTemplateItemRequestBuilder:
        """
        Provides operations to manage the notificationMessageTemplates property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: notification_message_template_item_request_builder.NotificationMessageTemplateItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["notificationMessageTemplate%2Did"] = id
        return notification_message_template_item_request_builder.NotificationMessageTemplateItemRequestBuilder(self.request_adapter, url_tpl_params)

    async def patch(self,body: Optional[device_management.DeviceManagement] = None, request_configuration: Optional[DeviceManagementRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_management.DeviceManagement]:
        """
        Update deviceManagement
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_management.DeviceManagement]
        """
        if not body:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, device_management.DeviceManagement, response_handler, error_mapping)

    def remote_assistance_partners_by_id(self,id: str) -> remote_assistance_partner_item_request_builder.RemoteAssistancePartnerItemRequestBuilder:
        """
        Provides operations to manage the remoteAssistancePartners property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: remote_assistance_partner_item_request_builder.RemoteAssistancePartnerItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["remoteAssistancePartner%2Did"] = id
        return remote_assistance_partner_item_request_builder.RemoteAssistancePartnerItemRequestBuilder(self.request_adapter, url_tpl_params)

    def resource_operations_by_id(self,id: str) -> resource_operation_item_request_builder.ResourceOperationItemRequestBuilder:
        """
        Provides operations to manage the resourceOperations property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: resource_operation_item_request_builder.ResourceOperationItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["resourceOperation%2Did"] = id
        return resource_operation_item_request_builder.ResourceOperationItemRequestBuilder(self.request_adapter, url_tpl_params)

    def role_assignments_by_id(self,id: str) -> device_and_app_management_role_assignment_item_request_builder.DeviceAndAppManagementRoleAssignmentItemRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_and_app_management_role_assignment_item_request_builder.DeviceAndAppManagementRoleAssignmentItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceAndAppManagementRoleAssignment%2Did"] = id
        return device_and_app_management_role_assignment_item_request_builder.DeviceAndAppManagementRoleAssignmentItemRequestBuilder(self.request_adapter, url_tpl_params)

    def role_definitions_by_id(self,id: str) -> role_definition_item_request_builder.RoleDefinitionItemRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: role_definition_item_request_builder.RoleDefinitionItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["roleDefinition%2Did"] = id
        return role_definition_item_request_builder.RoleDefinitionItemRequestBuilder(self.request_adapter, url_tpl_params)

    def telecom_expense_management_partners_by_id(self,id: str) -> telecom_expense_management_partner_item_request_builder.TelecomExpenseManagementPartnerItemRequestBuilder:
        """
        Provides operations to manage the telecomExpenseManagementPartners property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: telecom_expense_management_partner_item_request_builder.TelecomExpenseManagementPartnerItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["telecomExpenseManagementPartner%2Did"] = id
        return telecom_expense_management_partner_item_request_builder.TelecomExpenseManagementPartnerItemRequestBuilder(self.request_adapter, url_tpl_params)

    def terms_and_conditions_by_id(self,id: str) -> terms_and_conditions_item_request_builder.TermsAndConditionsItemRequestBuilder:
        """
        Provides operations to manage the termsAndConditions property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: terms_and_conditions_item_request_builder.TermsAndConditionsItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["termsAndConditions%2Did"] = id
        return terms_and_conditions_item_request_builder.TermsAndConditionsItemRequestBuilder(self.request_adapter, url_tpl_params)

    def troubleshooting_events_by_id(self,id: str) -> device_management_troubleshooting_event_item_request_builder.DeviceManagementTroubleshootingEventItemRequestBuilder:
        """
        Provides operations to manage the troubleshootingEvents property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_troubleshooting_event_item_request_builder.DeviceManagementTroubleshootingEventItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementTroubleshootingEvent%2Did"] = id
        return device_management_troubleshooting_event_item_request_builder.DeviceManagementTroubleshootingEventItemRequestBuilder(self.request_adapter, url_tpl_params)

    def verify_windows_enrollment_auto_discovery_with_domain_name(self,domain_name: Optional[str] = None) -> verify_windows_enrollment_auto_discovery_with_domain_name_request_builder.VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder:
        """
        Provides operations to call the verifyWindowsEnrollmentAutoDiscovery method.
        Args:
            domainName: Usage: domainName='{domainName}'
        Returns: verify_windows_enrollment_auto_discovery_with_domain_name_request_builder.VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder
        """
        if not domain_name:
            raise Exception("domain_name cannot be undefined")
        return verify_windows_enrollment_auto_discovery_with_domain_name_request_builder.VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder(self.request_adapter, self.path_parameters, domainName)

    def windows_autopilot_device_identities_by_id(self,id: str) -> windows_autopilot_device_identity_item_request_builder.WindowsAutopilotDeviceIdentityItemRequestBuilder:
        """
        Provides operations to manage the windowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_autopilot_device_identity_item_request_builder.WindowsAutopilotDeviceIdentityItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsAutopilotDeviceIdentity%2Did"] = id
        return windows_autopilot_device_identity_item_request_builder.WindowsAutopilotDeviceIdentityItemRequestBuilder(self.request_adapter, url_tpl_params)

    def windows_information_protection_app_learning_summaries_by_id(self,id: str) -> windows_information_protection_app_learning_summary_item_request_builder.WindowsInformationProtectionAppLearningSummaryItemRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionAppLearningSummaries property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_information_protection_app_learning_summary_item_request_builder.WindowsInformationProtectionAppLearningSummaryItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsInformationProtectionAppLearningSummary%2Did"] = id
        return windows_information_protection_app_learning_summary_item_request_builder.WindowsInformationProtectionAppLearningSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)

    def windows_information_protection_network_learning_summaries_by_id(self,id: str) -> windows_information_protection_network_learning_summary_item_request_builder.WindowsInformationProtectionNetworkLearningSummaryItemRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionNetworkLearningSummaries property of the microsoft.graph.deviceManagement entity.
        Args:
            id: Unique identifier of the item
        Returns: windows_information_protection_network_learning_summary_item_request_builder.WindowsInformationProtectionNetworkLearningSummaryItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["windowsInformationProtectionNetworkLearningSummary%2Did"] = id
        return windows_information_protection_network_learning_summary_item_request_builder.WindowsInformationProtectionNetworkLearningSummaryItemRequestBuilder(self.request_adapter, url_tpl_params)

    @dataclass
    class DeviceManagementRequestBuilderGetQueryParameters():
        """
        Get deviceManagement
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name

    
    @dataclass
    class DeviceManagementRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DeviceManagementRequestBuilder.DeviceManagementRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DeviceManagementRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

