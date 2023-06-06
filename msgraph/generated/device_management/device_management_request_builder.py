from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models import device_management
    from ..models.o_data_errors import o_data_error
    from .apple_push_notification_certificate import apple_push_notification_certificate_request_builder
    from .audit_events import audit_events_request_builder
    from .compliance_management_partners import compliance_management_partners_request_builder
    from .conditional_access_settings import conditional_access_settings_request_builder
    from .detected_apps import detected_apps_request_builder
    from .device_categories import device_categories_request_builder
    from .device_compliance_policies import device_compliance_policies_request_builder
    from .device_compliance_policy_device_state_summary import device_compliance_policy_device_state_summary_request_builder
    from .device_compliance_policy_setting_state_summaries import device_compliance_policy_setting_state_summaries_request_builder
    from .device_configuration_device_state_summaries import device_configuration_device_state_summaries_request_builder
    from .device_configurations import device_configurations_request_builder
    from .device_enrollment_configurations import device_enrollment_configurations_request_builder
    from .device_management_partners import device_management_partners_request_builder
    from .exchange_connectors import exchange_connectors_request_builder
    from .get_effective_permissions_with_scope import get_effective_permissions_with_scope_request_builder
    from .imported_windows_autopilot_device_identities import imported_windows_autopilot_device_identities_request_builder
    from .ios_update_statuses import ios_update_statuses_request_builder
    from .managed_device_overview import managed_device_overview_request_builder
    from .managed_devices import managed_devices_request_builder
    from .mobile_threat_defense_connectors import mobile_threat_defense_connectors_request_builder
    from .notification_message_templates import notification_message_templates_request_builder
    from .remote_assistance_partners import remote_assistance_partners_request_builder
    from .reports import reports_request_builder
    from .resource_operations import resource_operations_request_builder
    from .role_assignments import role_assignments_request_builder
    from .role_definitions import role_definitions_request_builder
    from .software_update_status_summary import software_update_status_summary_request_builder
    from .telecom_expense_management_partners import telecom_expense_management_partners_request_builder
    from .terms_and_conditions import terms_and_conditions_request_builder
    from .troubleshooting_events import troubleshooting_events_request_builder
    from .verify_windows_enrollment_auto_discovery_with_domain_name import verify_windows_enrollment_auto_discovery_with_domain_name_request_builder
    from .windows_autopilot_device_identities import windows_autopilot_device_identities_request_builder
    from .windows_information_protection_app_learning_summaries import windows_information_protection_app_learning_summaries_request_builder
    from .windows_information_protection_network_learning_summaries import windows_information_protection_network_learning_summaries_request_builder

class DeviceManagementRequestBuilder():
    """
    Provides operations to manage the deviceManagement singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DeviceManagementRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[DeviceManagementRequestBuilderGetRequestConfiguration] = None) -> Optional[device_management.DeviceManagement]:
        """
        Get deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management.DeviceManagement]
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
        from ..models import device_management

        return await self.request_adapter.send_async(request_info, device_management.DeviceManagement, error_mapping)
    
    def get_effective_permissions_with_scope(self,scope: Optional[str] = None) -> get_effective_permissions_with_scope_request_builder.GetEffectivePermissionsWithScopeRequestBuilder:
        """
        Provides operations to call the getEffectivePermissions method.
        Args:
            scope: Usage: scope='{scope}'
        Returns: get_effective_permissions_with_scope_request_builder.GetEffectivePermissionsWithScopeRequestBuilder
        """
        if scope is None:
            raise Exception("scope cannot be undefined")
        from .get_effective_permissions_with_scope import get_effective_permissions_with_scope_request_builder

        return get_effective_permissions_with_scope_request_builder.GetEffectivePermissionsWithScopeRequestBuilder(self.request_adapter, self.path_parameters, scope)
    
    async def patch(self,body: Optional[device_management.DeviceManagement] = None, request_configuration: Optional[DeviceManagementRequestBuilderPatchRequestConfiguration] = None) -> Optional[device_management.DeviceManagement]:
        """
        Update deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management.DeviceManagement]
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
        from ..models import device_management

        return await self.request_adapter.send_async(request_info, device_management.DeviceManagement, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[DeviceManagementRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[device_management.DeviceManagement] = None, request_configuration: Optional[DeviceManagementRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update deviceManagement
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
    
    def verify_windows_enrollment_auto_discovery_with_domain_name(self,domain_name: Optional[str] = None) -> verify_windows_enrollment_auto_discovery_with_domain_name_request_builder.VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder:
        """
        Provides operations to call the verifyWindowsEnrollmentAutoDiscovery method.
        Args:
            domainName: Usage: domainName='{domainName}'
        Returns: verify_windows_enrollment_auto_discovery_with_domain_name_request_builder.VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder
        """
        if domain_name is None:
            raise Exception("domain_name cannot be undefined")
        from .verify_windows_enrollment_auto_discovery_with_domain_name import verify_windows_enrollment_auto_discovery_with_domain_name_request_builder

        return verify_windows_enrollment_auto_discovery_with_domain_name_request_builder.VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder(self.request_adapter, self.path_parameters, domain_name)
    
    @property
    def apple_push_notification_certificate(self) -> apple_push_notification_certificate_request_builder.ApplePushNotificationCertificateRequestBuilder:
        """
        Provides operations to manage the applePushNotificationCertificate property of the microsoft.graph.deviceManagement entity.
        """
        from .apple_push_notification_certificate import apple_push_notification_certificate_request_builder

        return apple_push_notification_certificate_request_builder.ApplePushNotificationCertificateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def audit_events(self) -> audit_events_request_builder.AuditEventsRequestBuilder:
        """
        Provides operations to manage the auditEvents property of the microsoft.graph.deviceManagement entity.
        """
        from .audit_events import audit_events_request_builder

        return audit_events_request_builder.AuditEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def compliance_management_partners(self) -> compliance_management_partners_request_builder.ComplianceManagementPartnersRequestBuilder:
        """
        Provides operations to manage the complianceManagementPartners property of the microsoft.graph.deviceManagement entity.
        """
        from .compliance_management_partners import compliance_management_partners_request_builder

        return compliance_management_partners_request_builder.ComplianceManagementPartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def conditional_access_settings(self) -> conditional_access_settings_request_builder.ConditionalAccessSettingsRequestBuilder:
        """
        Provides operations to manage the conditionalAccessSettings property of the microsoft.graph.deviceManagement entity.
        """
        from .conditional_access_settings import conditional_access_settings_request_builder

        return conditional_access_settings_request_builder.ConditionalAccessSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def detected_apps(self) -> detected_apps_request_builder.DetectedAppsRequestBuilder:
        """
        Provides operations to manage the detectedApps property of the microsoft.graph.deviceManagement entity.
        """
        from .detected_apps import detected_apps_request_builder

        return detected_apps_request_builder.DetectedAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_categories(self) -> device_categories_request_builder.DeviceCategoriesRequestBuilder:
        """
        Provides operations to manage the deviceCategories property of the microsoft.graph.deviceManagement entity.
        """
        from .device_categories import device_categories_request_builder

        return device_categories_request_builder.DeviceCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policies(self) -> device_compliance_policies_request_builder.DeviceCompliancePoliciesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicies property of the microsoft.graph.deviceManagement entity.
        """
        from .device_compliance_policies import device_compliance_policies_request_builder

        return device_compliance_policies_request_builder.DeviceCompliancePoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policy_device_state_summary(self) -> device_compliance_policy_device_state_summary_request_builder.DeviceCompliancePolicyDeviceStateSummaryRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicyDeviceStateSummary property of the microsoft.graph.deviceManagement entity.
        """
        from .device_compliance_policy_device_state_summary import device_compliance_policy_device_state_summary_request_builder

        return device_compliance_policy_device_state_summary_request_builder.DeviceCompliancePolicyDeviceStateSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_compliance_policy_setting_state_summaries(self) -> device_compliance_policy_setting_state_summaries_request_builder.DeviceCompliancePolicySettingStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceCompliancePolicySettingStateSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .device_compliance_policy_setting_state_summaries import device_compliance_policy_setting_state_summaries_request_builder

        return device_compliance_policy_setting_state_summaries_request_builder.DeviceCompliancePolicySettingStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configuration_device_state_summaries(self) -> device_configuration_device_state_summaries_request_builder.DeviceConfigurationDeviceStateSummariesRequestBuilder:
        """
        Provides operations to manage the deviceConfigurationDeviceStateSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configuration_device_state_summaries import device_configuration_device_state_summaries_request_builder

        return device_configuration_device_state_summaries_request_builder.DeviceConfigurationDeviceStateSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_configurations(self) -> device_configurations_request_builder.DeviceConfigurationsRequestBuilder:
        """
        Provides operations to manage the deviceConfigurations property of the microsoft.graph.deviceManagement entity.
        """
        from .device_configurations import device_configurations_request_builder

        return device_configurations_request_builder.DeviceConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_enrollment_configurations(self) -> device_enrollment_configurations_request_builder.DeviceEnrollmentConfigurationsRequestBuilder:
        """
        Provides operations to manage the deviceEnrollmentConfigurations property of the microsoft.graph.deviceManagement entity.
        """
        from .device_enrollment_configurations import device_enrollment_configurations_request_builder

        return device_enrollment_configurations_request_builder.DeviceEnrollmentConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def device_management_partners(self) -> device_management_partners_request_builder.DeviceManagementPartnersRequestBuilder:
        """
        Provides operations to manage the deviceManagementPartners property of the microsoft.graph.deviceManagement entity.
        """
        from .device_management_partners import device_management_partners_request_builder

        return device_management_partners_request_builder.DeviceManagementPartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exchange_connectors(self) -> exchange_connectors_request_builder.ExchangeConnectorsRequestBuilder:
        """
        Provides operations to manage the exchangeConnectors property of the microsoft.graph.deviceManagement entity.
        """
        from .exchange_connectors import exchange_connectors_request_builder

        return exchange_connectors_request_builder.ExchangeConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def imported_windows_autopilot_device_identities(self) -> imported_windows_autopilot_device_identities_request_builder.ImportedWindowsAutopilotDeviceIdentitiesRequestBuilder:
        """
        Provides operations to manage the importedWindowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        """
        from .imported_windows_autopilot_device_identities import imported_windows_autopilot_device_identities_request_builder

        return imported_windows_autopilot_device_identities_request_builder.ImportedWindowsAutopilotDeviceIdentitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ios_update_statuses(self) -> ios_update_statuses_request_builder.IosUpdateStatusesRequestBuilder:
        """
        Provides operations to manage the iosUpdateStatuses property of the microsoft.graph.deviceManagement entity.
        """
        from .ios_update_statuses import ios_update_statuses_request_builder

        return ios_update_statuses_request_builder.IosUpdateStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_device_overview(self) -> managed_device_overview_request_builder.ManagedDeviceOverviewRequestBuilder:
        """
        Provides operations to manage the managedDeviceOverview property of the microsoft.graph.deviceManagement entity.
        """
        from .managed_device_overview import managed_device_overview_request_builder

        return managed_device_overview_request_builder.ManagedDeviceOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_devices(self) -> managed_devices_request_builder.ManagedDevicesRequestBuilder:
        """
        Provides operations to manage the managedDevices property of the microsoft.graph.deviceManagement entity.
        """
        from .managed_devices import managed_devices_request_builder

        return managed_devices_request_builder.ManagedDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_threat_defense_connectors(self) -> mobile_threat_defense_connectors_request_builder.MobileThreatDefenseConnectorsRequestBuilder:
        """
        Provides operations to manage the mobileThreatDefenseConnectors property of the microsoft.graph.deviceManagement entity.
        """
        from .mobile_threat_defense_connectors import mobile_threat_defense_connectors_request_builder

        return mobile_threat_defense_connectors_request_builder.MobileThreatDefenseConnectorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def notification_message_templates(self) -> notification_message_templates_request_builder.NotificationMessageTemplatesRequestBuilder:
        """
        Provides operations to manage the notificationMessageTemplates property of the microsoft.graph.deviceManagement entity.
        """
        from .notification_message_templates import notification_message_templates_request_builder

        return notification_message_templates_request_builder.NotificationMessageTemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remote_assistance_partners(self) -> remote_assistance_partners_request_builder.RemoteAssistancePartnersRequestBuilder:
        """
        Provides operations to manage the remoteAssistancePartners property of the microsoft.graph.deviceManagement entity.
        """
        from .remote_assistance_partners import remote_assistance_partners_request_builder

        return remote_assistance_partners_request_builder.RemoteAssistancePartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reports(self) -> reports_request_builder.ReportsRequestBuilder:
        """
        Provides operations to manage the reports property of the microsoft.graph.deviceManagement entity.
        """
        from .reports import reports_request_builder

        return reports_request_builder.ReportsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resource_operations(self) -> resource_operations_request_builder.ResourceOperationsRequestBuilder:
        """
        Provides operations to manage the resourceOperations property of the microsoft.graph.deviceManagement entity.
        """
        from .resource_operations import resource_operations_request_builder

        return resource_operations_request_builder.ResourceOperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_assignments(self) -> role_assignments_request_builder.RoleAssignmentsRequestBuilder:
        """
        Provides operations to manage the roleAssignments property of the microsoft.graph.deviceManagement entity.
        """
        from .role_assignments import role_assignments_request_builder

        return role_assignments_request_builder.RoleAssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def role_definitions(self) -> role_definitions_request_builder.RoleDefinitionsRequestBuilder:
        """
        Provides operations to manage the roleDefinitions property of the microsoft.graph.deviceManagement entity.
        """
        from .role_definitions import role_definitions_request_builder

        return role_definitions_request_builder.RoleDefinitionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def software_update_status_summary(self) -> software_update_status_summary_request_builder.SoftwareUpdateStatusSummaryRequestBuilder:
        """
        Provides operations to manage the softwareUpdateStatusSummary property of the microsoft.graph.deviceManagement entity.
        """
        from .software_update_status_summary import software_update_status_summary_request_builder

        return software_update_status_summary_request_builder.SoftwareUpdateStatusSummaryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def telecom_expense_management_partners(self) -> telecom_expense_management_partners_request_builder.TelecomExpenseManagementPartnersRequestBuilder:
        """
        Provides operations to manage the telecomExpenseManagementPartners property of the microsoft.graph.deviceManagement entity.
        """
        from .telecom_expense_management_partners import telecom_expense_management_partners_request_builder

        return telecom_expense_management_partners_request_builder.TelecomExpenseManagementPartnersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def terms_and_conditions(self) -> terms_and_conditions_request_builder.TermsAndConditionsRequestBuilder:
        """
        Provides operations to manage the termsAndConditions property of the microsoft.graph.deviceManagement entity.
        """
        from .terms_and_conditions import terms_and_conditions_request_builder

        return terms_and_conditions_request_builder.TermsAndConditionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def troubleshooting_events(self) -> troubleshooting_events_request_builder.TroubleshootingEventsRequestBuilder:
        """
        Provides operations to manage the troubleshootingEvents property of the microsoft.graph.deviceManagement entity.
        """
        from .troubleshooting_events import troubleshooting_events_request_builder

        return troubleshooting_events_request_builder.TroubleshootingEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_autopilot_device_identities(self) -> windows_autopilot_device_identities_request_builder.WindowsAutopilotDeviceIdentitiesRequestBuilder:
        """
        Provides operations to manage the windowsAutopilotDeviceIdentities property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_autopilot_device_identities import windows_autopilot_device_identities_request_builder

        return windows_autopilot_device_identities_request_builder.WindowsAutopilotDeviceIdentitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_app_learning_summaries(self) -> windows_information_protection_app_learning_summaries_request_builder.WindowsInformationProtectionAppLearningSummariesRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionAppLearningSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_information_protection_app_learning_summaries import windows_information_protection_app_learning_summaries_request_builder

        return windows_information_protection_app_learning_summaries_request_builder.WindowsInformationProtectionAppLearningSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_network_learning_summaries(self) -> windows_information_protection_network_learning_summaries_request_builder.WindowsInformationProtectionNetworkLearningSummariesRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionNetworkLearningSummaries property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_information_protection_network_learning_summaries import windows_information_protection_network_learning_summaries_request_builder

        return windows_information_protection_network_learning_summaries_request_builder.WindowsInformationProtectionNetworkLearningSummariesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DeviceManagementRequestBuilderGetQueryParameters():
        """
        Get deviceManagement
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
    class DeviceManagementRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

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
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

