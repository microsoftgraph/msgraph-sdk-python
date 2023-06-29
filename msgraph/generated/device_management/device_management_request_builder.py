from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.device_management import DeviceManagement
    from ..models.o_data_errors.o_data_error import ODataError
    from .apple_push_notification_certificate.apple_push_notification_certificate_request_builder import ApplePushNotificationCertificateRequestBuilder
    from .audit_events.audit_events_request_builder import AuditEventsRequestBuilder
    from .compliance_management_partners.compliance_management_partners_request_builder import ComplianceManagementPartnersRequestBuilder
    from .conditional_access_settings.conditional_access_settings_request_builder import ConditionalAccessSettingsRequestBuilder
    from .detected_apps.detected_apps_request_builder import DetectedAppsRequestBuilder
    from .device_categories.device_categories_request_builder import DeviceCategoriesRequestBuilder
    from .device_compliance_policies.device_compliance_policies_request_builder import DeviceCompliancePoliciesRequestBuilder
    from .device_compliance_policy_device_state_summary.device_compliance_policy_device_state_summary_request_builder import DeviceCompliancePolicyDeviceStateSummaryRequestBuilder
    from .device_compliance_policy_setting_state_summaries.device_compliance_policy_setting_state_summaries_request_builder import DeviceCompliancePolicySettingStateSummariesRequestBuilder
    from .device_configuration_device_state_summaries.device_configuration_device_state_summaries_request_builder import DeviceConfigurationDeviceStateSummariesRequestBuilder
    from .device_configurations.device_configurations_request_builder import DeviceConfigurationsRequestBuilder
    from .device_enrollment_configurations.device_enrollment_configurations_request_builder import DeviceEnrollmentConfigurationsRequestBuilder
    from .device_management_partners.device_management_partners_request_builder import DeviceManagementPartnersRequestBuilder
    from .exchange_connectors.exchange_connectors_request_builder import ExchangeConnectorsRequestBuilder
    from .get_effective_permissions_with_scope.get_effective_permissions_with_scope_request_builder import GetEffectivePermissionsWithScopeRequestBuilder
    from .imported_windows_autopilot_device_identities.imported_windows_autopilot_device_identities_request_builder import ImportedWindowsAutopilotDeviceIdentitiesRequestBuilder
    from .ios_update_statuses.ios_update_statuses_request_builder import IosUpdateStatusesRequestBuilder
    from .managed_device_overview.managed_device_overview_request_builder import ManagedDeviceOverviewRequestBuilder
    from .managed_devices.managed_devices_request_builder import ManagedDevicesRequestBuilder
    from .mobile_threat_defense_connectors.mobile_threat_defense_connectors_request_builder import MobileThreatDefenseConnectorsRequestBuilder
    from .notification_message_templates.notification_message_templates_request_builder import NotificationMessageTemplatesRequestBuilder
    from .remote_assistance_partners.remote_assistance_partners_request_builder import RemoteAssistancePartnersRequestBuilder
    from .reports.reports_request_builder import ReportsRequestBuilder
    from .resource_operations.resource_operations_request_builder import ResourceOperationsRequestBuilder
    from .role_assignments.role_assignments_request_builder import RoleAssignmentsRequestBuilder
    from .role_definitions.role_definitions_request_builder import RoleDefinitionsRequestBuilder
    from .software_update_status_summary.software_update_status_summary_request_builder import SoftwareUpdateStatusSummaryRequestBuilder
    from .telecom_expense_management_partners.telecom_expense_management_partners_request_builder import TelecomExpenseManagementPartnersRequestBuilder
    from .terms_and_conditions.terms_and_conditions_request_builder import TermsAndConditionsRequestBuilder
    from .troubleshooting_events.troubleshooting_events_request_builder import TroubleshootingEventsRequestBuilder
    from .verify_windows_enrollment_auto_discovery_with_domain_name.verify_windows_enrollment_auto_discovery_with_domain_name_request_builder import VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder
    from .windows_autopilot_device_identities.windows_autopilot_device_identities_request_builder import WindowsAutopilotDeviceIdentitiesRequestBuilder
    from .windows_information_protection_app_learning_summaries.windows_information_protection_app_learning_summaries_request_builder import WindowsInformationProtectionAppLearningSummariesRequestBuilder
    from .windows_information_protection_network_learning_summaries.windows_information_protection_network_learning_summaries_request_builder import WindowsInformationProtectionNetworkLearningSummariesRequestBuilder

class DeviceManagementRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the deviceManagement singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceManagementRequestBuilder and sets the default values.
        Args:
            path_parameters: The raw url or the Url template parameters for the request.
            request_adapter: The request adapter to use to execute the requests.
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[DeviceManagementRequestBuilderGetRequestConfiguration] = None) -> Optional[DeviceManagement]:
        """
        Read properties and relationships of the deviceManagement object.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagement]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.device_management import DeviceManagement

        return await self.request_adapter.send_async(request_info, DeviceManagement, error_mapping)
    
    def get_effective_permissions_with_scope(self,scope: Optional[str] = None) -> GetEffectivePermissionsWithScopeRequestBuilder:
        """
        Provides operations to call the getEffectivePermissions method.
        Args:
            scope: Usage: scope='{scope}'
        Returns: GetEffectivePermissionsWithScopeRequestBuilder
        """
        if not scope:
            raise TypeError("scope cannot be null.")
        from .get_effective_permissions_with_scope.get_effective_permissions_with_scope_request_builder import GetEffectivePermissionsWithScopeRequestBuilder

        return GetEffectivePermissionsWithScopeRequestBuilder(self.request_adapter, self.path_parameters, scope)
    
    async def patch(self,body: Optional[DeviceManagement] = None, request_configuration: Optional[DeviceManagementRequestBuilderPatchRequestConfiguration] = None) -> Optional[DeviceManagement]:
        """
        Update the properties of a deviceManagement object.
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagement]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.device_management import DeviceManagement

        return await self.request_adapter.send_async(request_info, DeviceManagement, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[DeviceManagementRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read properties and relationships of the deviceManagement object.
        Args:
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
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
    
    def to_patch_request_information(self,body: Optional[DeviceManagement] = None, request_configuration: Optional[DeviceManagementRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a deviceManagement object.
        Args:
            body: The request body
            request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
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
    
    def verify_windows_enrollment_auto_discovery_with_domain_name(self,domain_name: Optional[str] = None) -> VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder:
        """
        Provides operations to call the verifyWindowsEnrollmentAutoDiscovery method.
        Args:
            domain_name: Usage: domainName='{domainName}'
        Returns: VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder
        """
        if not domain_name:
            raise TypeError("domain_name cannot be null.")
        from .verify_windows_enrollment_auto_discovery_with_domain_name.verify_windows_enrollment_auto_discovery_with_domain_name_request_builder import VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder

        return VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder(self.request_adapter, self.path_parameters, domain_name)
    
    @property
    def apple_push_notification_certificate(self) -> ApplePushNotificationCertificateRequestBuilder:
        """
        Provides operations to manage the applePushNotificationCertificate property of the microsoft.graph.deviceManagement entity.
        """
        from .apple_push_notification_certificate.apple_push_notification_certificate_request_builder import ApplePushNotificationCertificateRequestBuilder

        return ApplePushNotificationCertificateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def audit_events(self) -> AuditEventsRequestBuilder:
        """
        Provides operations to manage the auditEvents property of the microsoft.graph.deviceManagement entity.
        """
        from .audit_events.audit_events_request_builder import AuditEventsRequestBuilder

        return AuditEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def compliance_management_partners(self) -> ComplianceManagementPartnersRequestBuilder:
        """
        Provides operations to manage the complianceManagementPartners property of the microsoft.graph.deviceManagement entity.
        """
        from .compliance_management_partners.compliance_management_partners_request_builder import ComplianceManagementPartnersRequestBuilder

        return ComplianceManagementPartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def conditional_access_settings(self) -> ConditionalAccessSettingsRequestBuilder:
        """
        Provides operations to manage the conditionalAccessSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .conditional_access_settings.conditional_access_settings_request_builder import ConditionalAccessSettingsRequestBuilder

        return ConditionalAccessSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def detected_apps(self) -> DetectedAppsRequestBuilder:
        """
        Provides operations to manage the detectedApps property of the microsoft.graph.deviceManagement entity.
        """
        from .detected_apps.detected_apps_request_builder import DetectedAppsRequestBuilder

        return DetectedAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_categories(self) -> DeviceCategoriesRequestBuilder:
        """
        Provides operations to manage the deviceCategories property of the microsoft.graph.deviceManagement entity.
        """
        from .device_categories.device_categories_request_builder import DeviceCategoriesRequestBuilder

        return DeviceCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policies(self) -> DeviceCompliancePoliciesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicies property of the microsoft.graph.deviceManagement entity.
        """
        from .device_compliance_policies.device_compliance_policies_request_builder import DeviceCompliancePoliciesRequestBuilder

        return DeviceCompliancePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policy_device_state_summary(self) -> DeviceCompliancePolicyDeviceStateSummaryRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicyDeviceStateSummary property of the microsoft.graph.deviceManagement entity.
        """
        from .device_compliance_policy_device_state_summary.device_compliance_policy_device_state_summary_request_builder import DeviceCompliancePolicyDeviceStateSummaryRequestBuilder

        return DeviceCompliancePolicyDeviceStateSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policy_setting_state_summaries(self) -> DeviceCompliancePolicySettingStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicySettingStateSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .device_compliance_policy_setting_state_summaries.device_compliance_policy_setting_state_summaries_request_builder import DeviceCompliancePolicySettingStateSummariesRequestBuilder

        return DeviceCompliancePolicySettingStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_device_state_summaries(self) -> DeviceConfigurationDeviceStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationDeviceStateSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configuration_device_state_summaries.device_configuration_device_state_summaries_request_builder import DeviceConfigurationDeviceStateSummariesRequestBuilder

        return DeviceConfigurationDeviceStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configurations(self) -> DeviceConfigurationsRequestBuilder:
        """
        Provides operations to manage the deviceConfigurations property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configurations.device_configurations_request_builder import DeviceConfigurationsRequestBuilder

        return DeviceConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_enrollment_configurations(self) -> DeviceEnrollmentConfigurationsRequestBuilder:
        """
        Provides operations to manage the deviceEnrollmentConfigurations property of the microsoft.graph.deviceManagement entity.
        """
        from .device_enrollment_configurations.device_enrollment_configurations_request_builder import DeviceEnrollmentConfigurationsRequestBuilder

        return DeviceEnrollmentConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_management_partners(self) -> DeviceManagementPartnersRequestBuilder:
        """
        Provides operations to manage the deviceManagementPartners property of the microsoft.graph.deviceManagement entity.
        """
        from .device_management_partners.device_management_partners_request_builder import DeviceManagementPartnersRequestBuilder

        return DeviceManagementPartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exchange_connectors(self) -> ExchangeConnectorsRequestBuilder:
        """
        Provides operations to manage the exchangeConnectors property of the microsoft.graph.deviceManagement entity.
        """
        from .exchange_connectors.exchange_connectors_request_builder import ExchangeConnectorsRequestBuilder

        return ExchangeConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def imported_windows_autopilot_device_identities(self) -> ImportedWindowsAutopilotDeviceIdentitiesRequestBuilder:
        """
        Provides operations to manage the importedWindowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        """
        from .imported_windows_autopilot_device_identities.imported_windows_autopilot_device_identities_request_builder import ImportedWindowsAutopilotDeviceIdentitiesRequestBuilder

        return ImportedWindowsAutopilotDeviceIdentitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ios_update_statuses(self) -> IosUpdateStatusesRequestBuilder:
        """
        Provides operations to manage the iosUpdateStatuses property of the microsoft.graph.deviceManagement entity.
        """
        from .ios_update_statuses.ios_update_statuses_request_builder import IosUpdateStatusesRequestBuilder

        return IosUpdateStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_overview(self) -> ManagedDeviceOverviewRequestBuilder:
        """
        Provides operations to manage the managedDeviceOverview property of the microsoft.graph.deviceManagement entity.
        """
        from .managed_device_overview.managed_device_overview_request_builder import ManagedDeviceOverviewRequestBuilder

        return ManagedDeviceOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_devices(self) -> ManagedDevicesRequestBuilder:
        """
        Provides operations to manage the managedDevices property of the microsoft.graph.deviceManagement entity.
        """
        from .managed_devices.managed_devices_request_builder import ManagedDevicesRequestBuilder

        return ManagedDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_threat_defense_connectors(self) -> MobileThreatDefenseConnectorsRequestBuilder:
        """
        Provides operations to manage the mobileThreatDefenseConnectors property of the microsoft.graph.deviceManagement entity.
        """
        from .mobile_threat_defense_connectors.mobile_threat_defense_connectors_request_builder import MobileThreatDefenseConnectorsRequestBuilder

        return MobileThreatDefenseConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notification_message_templates(self) -> NotificationMessageTemplatesRequestBuilder:
        """
        Provides operations to manage the notificationMessageTemplates property of the microsoft.graph.deviceManagement entity.
        """
        from .notification_message_templates.notification_message_templates_request_builder import NotificationMessageTemplatesRequestBuilder

        return NotificationMessageTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_assistance_partners(self) -> RemoteAssistancePartnersRequestBuilder:
        """
        Provides operations to manage the remoteAssistancePartners property of the microsoft.graph.deviceManagement entity.
        """
        from .remote_assistance_partners.remote_assistance_partners_request_builder import RemoteAssistancePartnersRequestBuilder

        return RemoteAssistancePartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reports(self) -> ReportsRequestBuilder:
        """
        Provides operations to manage the reports property of the microsoft.graph.deviceManagement entity.
        """
        from .reports.reports_request_builder import ReportsRequestBuilder

        return ReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_operations(self) -> ResourceOperationsRequestBuilder:
        """
        Provides operations to manage the resourceOperations property of the microsoft.graph.deviceManagement entity.
        """
        from .resource_operations.resource_operations_request_builder import ResourceOperationsRequestBuilder

        return ResourceOperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignments(self) -> RoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.deviceManagement entity.
        """
        from .role_assignments.role_assignments_request_builder import RoleAssignmentsRequestBuilder

        return RoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_definitions(self) -> RoleDefinitionsRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.deviceManagement entity.
        """
        from .role_definitions.role_definitions_request_builder import RoleDefinitionsRequestBuilder

        return RoleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def software_update_status_summary(self) -> SoftwareUpdateStatusSummaryRequestBuilder:
        """
        Provides operations to manage the softwareUpdateStatusSummary property of the microsoft.graph.deviceManagement entity.
        """
        from .software_update_status_summary.software_update_status_summary_request_builder import SoftwareUpdateStatusSummaryRequestBuilder

        return SoftwareUpdateStatusSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def telecom_expense_management_partners(self) -> TelecomExpenseManagementPartnersRequestBuilder:
        """
        Provides operations to manage the telecomExpenseManagementPartners property of the microsoft.graph.deviceManagement entity.
        """
        from .telecom_expense_management_partners.telecom_expense_management_partners_request_builder import TelecomExpenseManagementPartnersRequestBuilder

        return TelecomExpenseManagementPartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def terms_and_conditions(self) -> TermsAndConditionsRequestBuilder:
        """
        Provides operations to manage the termsAndConditions property of the microsoft.graph.deviceManagement entity.
        """
        from .terms_and_conditions.terms_and_conditions_request_builder import TermsAndConditionsRequestBuilder

        return TermsAndConditionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def troubleshooting_events(self) -> TroubleshootingEventsRequestBuilder:
        """
        Provides operations to manage the troubleshootingEvents property of the microsoft.graph.deviceManagement entity.
        """
        from .troubleshooting_events.troubleshooting_events_request_builder import TroubleshootingEventsRequestBuilder

        return TroubleshootingEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_autopilot_device_identities(self) -> WindowsAutopilotDeviceIdentitiesRequestBuilder:
        """
        Provides operations to manage the windowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_autopilot_device_identities.windows_autopilot_device_identities_request_builder import WindowsAutopilotDeviceIdentitiesRequestBuilder

        return WindowsAutopilotDeviceIdentitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_app_learning_summaries(self) -> WindowsInformationProtectionAppLearningSummariesRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionAppLearningSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_information_protection_app_learning_summaries.windows_information_protection_app_learning_summaries_request_builder import WindowsInformationProtectionAppLearningSummariesRequestBuilder

        return WindowsInformationProtectionAppLearningSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_network_learning_summaries(self) -> WindowsInformationProtectionNetworkLearningSummariesRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionNetworkLearningSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_information_protection_network_learning_summaries.windows_information_protection_network_learning_summaries_request_builder import WindowsInformationProtectionNetworkLearningSummariesRequestBuilder

        return WindowsInformationProtectionNetworkLearningSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DeviceManagementRequestBuilderGetQueryParameters():
        """
        Read properties and relationships of the deviceManagement object.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DeviceManagementRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[DeviceManagementRequestBuilder.DeviceManagementRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class DeviceManagementRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

