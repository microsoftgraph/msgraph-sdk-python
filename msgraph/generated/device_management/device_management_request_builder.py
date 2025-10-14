from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

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
    from .device_configurations.device_configurations_request_builder import DeviceConfigurationsRequestBuilder
    from .device_configuration_device_state_summaries.device_configuration_device_state_summaries_request_builder import DeviceConfigurationDeviceStateSummariesRequestBuilder
    from .device_enrollment_configurations.device_enrollment_configurations_request_builder import DeviceEnrollmentConfigurationsRequestBuilder
    from .device_management_partners.device_management_partners_request_builder import DeviceManagementPartnersRequestBuilder
    from .exchange_connectors.exchange_connectors_request_builder import ExchangeConnectorsRequestBuilder
    from .get_effective_permissions_with_scope.get_effective_permissions_with_scope_request_builder import GetEffectivePermissionsWithScopeRequestBuilder
    from .imported_windows_autopilot_device_identities.imported_windows_autopilot_device_identities_request_builder import ImportedWindowsAutopilotDeviceIdentitiesRequestBuilder
    from .ios_update_statuses.ios_update_statuses_request_builder import IosUpdateStatusesRequestBuilder
    from .managed_devices.managed_devices_request_builder import ManagedDevicesRequestBuilder
    from .managed_device_overview.managed_device_overview_request_builder import ManagedDeviceOverviewRequestBuilder
    from .mobile_app_troubleshooting_events.mobile_app_troubleshooting_events_request_builder import MobileAppTroubleshootingEventsRequestBuilder
    from .mobile_threat_defense_connectors.mobile_threat_defense_connectors_request_builder import MobileThreatDefenseConnectorsRequestBuilder
    from .notification_message_templates.notification_message_templates_request_builder import NotificationMessageTemplatesRequestBuilder
    from .remote_assistance_partners.remote_assistance_partners_request_builder import RemoteAssistancePartnersRequestBuilder
    from .reports.reports_request_builder import ReportsRequestBuilder
    from .resource_operations.resource_operations_request_builder import ResourceOperationsRequestBuilder
    from .role_assignments.role_assignments_request_builder import RoleAssignmentsRequestBuilder
    from .role_definitions.role_definitions_request_builder import RoleDefinitionsRequestBuilder
    from .software_update_status_summary.software_update_status_summary_request_builder import SoftwareUpdateStatusSummaryRequestBuilder
    from .terms_and_conditions.terms_and_conditions_request_builder import TermsAndConditionsRequestBuilder
    from .troubleshooting_events.troubleshooting_events_request_builder import TroubleshootingEventsRequestBuilder
    from .user_experience_analytics_app_health_application_performance.user_experience_analytics_app_health_application_performance_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceRequestBuilder
    from .user_experience_analytics_app_health_application_performance_by_app_version_details.user_experience_analytics_app_health_application_performance_by_app_version_details_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilder
    from .user_experience_analytics_app_health_application_performance_by_app_version_device_id.user_experience_analytics_app_health_application_performance_by_app_version_device_id_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequestBuilder
    from .user_experience_analytics_app_health_application_performance_by_o_s_version.user_experience_analytics_app_health_application_performance_by_o_s_version_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceByOSVersionRequestBuilder
    from .user_experience_analytics_app_health_device_model_performance.user_experience_analytics_app_health_device_model_performance_request_builder import UserExperienceAnalyticsAppHealthDeviceModelPerformanceRequestBuilder
    from .user_experience_analytics_app_health_device_performance.user_experience_analytics_app_health_device_performance_request_builder import UserExperienceAnalyticsAppHealthDevicePerformanceRequestBuilder
    from .user_experience_analytics_app_health_device_performance_details.user_experience_analytics_app_health_device_performance_details_request_builder import UserExperienceAnalyticsAppHealthDevicePerformanceDetailsRequestBuilder
    from .user_experience_analytics_app_health_overview.user_experience_analytics_app_health_overview_request_builder import UserExperienceAnalyticsAppHealthOverviewRequestBuilder
    from .user_experience_analytics_app_health_o_s_version_performance.user_experience_analytics_app_health_o_s_version_performance_request_builder import UserExperienceAnalyticsAppHealthOSVersionPerformanceRequestBuilder
    from .user_experience_analytics_baselines.user_experience_analytics_baselines_request_builder import UserExperienceAnalyticsBaselinesRequestBuilder
    from .user_experience_analytics_categories.user_experience_analytics_categories_request_builder import UserExperienceAnalyticsCategoriesRequestBuilder
    from .user_experience_analytics_device_performance.user_experience_analytics_device_performance_request_builder import UserExperienceAnalyticsDevicePerformanceRequestBuilder
    from .user_experience_analytics_device_scores.user_experience_analytics_device_scores_request_builder import UserExperienceAnalyticsDeviceScoresRequestBuilder
    from .user_experience_analytics_device_startup_history.user_experience_analytics_device_startup_history_request_builder import UserExperienceAnalyticsDeviceStartupHistoryRequestBuilder
    from .user_experience_analytics_device_startup_processes.user_experience_analytics_device_startup_processes_request_builder import UserExperienceAnalyticsDeviceStartupProcessesRequestBuilder
    from .user_experience_analytics_device_startup_process_performance.user_experience_analytics_device_startup_process_performance_request_builder import UserExperienceAnalyticsDeviceStartupProcessPerformanceRequestBuilder
    from .user_experience_analytics_metric_history.user_experience_analytics_metric_history_request_builder import UserExperienceAnalyticsMetricHistoryRequestBuilder
    from .user_experience_analytics_model_scores.user_experience_analytics_model_scores_request_builder import UserExperienceAnalyticsModelScoresRequestBuilder
    from .user_experience_analytics_overview.user_experience_analytics_overview_request_builder import UserExperienceAnalyticsOverviewRequestBuilder
    from .user_experience_analytics_score_history.user_experience_analytics_score_history_request_builder import UserExperienceAnalyticsScoreHistoryRequestBuilder
    from .user_experience_analytics_summarize_work_from_anywhere_devices.user_experience_analytics_summarize_work_from_anywhere_devices_request_builder import UserExperienceAnalyticsSummarizeWorkFromAnywhereDevicesRequestBuilder
    from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric.user_experience_analytics_work_from_anywhere_hardware_readiness_metric_request_builder import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetricRequestBuilder
    from .user_experience_analytics_work_from_anywhere_metrics.user_experience_analytics_work_from_anywhere_metrics_request_builder import UserExperienceAnalyticsWorkFromAnywhereMetricsRequestBuilder
    from .user_experience_analytics_work_from_anywhere_model_performance.user_experience_analytics_work_from_anywhere_model_performance_request_builder import UserExperienceAnalyticsWorkFromAnywhereModelPerformanceRequestBuilder
    from .verify_windows_enrollment_auto_discovery_with_domain_name.verify_windows_enrollment_auto_discovery_with_domain_name_request_builder import VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder
    from .virtual_endpoint.virtual_endpoint_request_builder import VirtualEndpointRequestBuilder
    from .windows_autopilot_device_identities.windows_autopilot_device_identities_request_builder import WindowsAutopilotDeviceIdentitiesRequestBuilder
    from .windows_information_protection_app_learning_summaries.windows_information_protection_app_learning_summaries_request_builder import WindowsInformationProtectionAppLearningSummariesRequestBuilder
    from .windows_information_protection_network_learning_summaries.windows_information_protection_network_learning_summaries_request_builder import WindowsInformationProtectionNetworkLearningSummariesRequestBuilder
    from .windows_malware_information.windows_malware_information_request_builder import WindowsMalwareInformationRequestBuilder

class DeviceManagementRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the deviceManagement singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DeviceManagementRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DeviceManagementRequestBuilderGetQueryParameters]] = None) -> Optional[DeviceManagement]:
        """
        Get deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagement]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.device_management import DeviceManagement

        return await self.request_adapter.send_async(request_info, DeviceManagement, error_mapping)
    
    def get_effective_permissions_with_scope(self,scope: str) -> GetEffectivePermissionsWithScopeRequestBuilder:
        """
        Provides operations to call the getEffectivePermissions method.
        param scope: Usage: scope='{scope}'
        Returns: GetEffectivePermissionsWithScopeRequestBuilder
        """
        if scope is None:
            raise TypeError("scope cannot be null.")
        from .get_effective_permissions_with_scope.get_effective_permissions_with_scope_request_builder import GetEffectivePermissionsWithScopeRequestBuilder

        return GetEffectivePermissionsWithScopeRequestBuilder(self.request_adapter, self.path_parameters, scope)
    
    async def patch(self,body: DeviceManagement, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DeviceManagement]:
        """
        Update deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagement]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.device_management import DeviceManagement

        return await self.request_adapter.send_async(request_info, DeviceManagement, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DeviceManagementRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: DeviceManagement, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def verify_windows_enrollment_auto_discovery_with_domain_name(self,domain_name: str) -> VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder:
        """
        Provides operations to call the verifyWindowsEnrollmentAutoDiscovery method.
        param domain_name: Usage: domainName='{domainName}'
        Returns: VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder
        """
        if domain_name is None:
            raise TypeError("domain_name cannot be null.")
        from .verify_windows_enrollment_auto_discovery_with_domain_name.verify_windows_enrollment_auto_discovery_with_domain_name_request_builder import VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder

        return VerifyWindowsEnrollmentAutoDiscoveryWithDomainNameRequestBuilder(self.request_adapter, self.path_parameters, domain_name)
    
    def with_url(self,raw_url: str) -> DeviceManagementRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DeviceManagementRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DeviceManagementRequestBuilder(self.request_adapter, raw_url)
    
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
    def mobile_app_troubleshooting_events(self) -> MobileAppTroubleshootingEventsRequestBuilder:
        """
        Provides operations to manage the mobileAppTroubleshootingEvents property of the microsoft.graph.deviceManagement entity.
        """
        from .mobile_app_troubleshooting_events.mobile_app_troubleshooting_events_request_builder import MobileAppTroubleshootingEventsRequestBuilder

        return MobileAppTroubleshootingEventsRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    def user_experience_analytics_app_health_application_performance(self) -> UserExperienceAnalyticsAppHealthApplicationPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_application_performance.user_experience_analytics_app_health_application_performance_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceRequestBuilder

        return UserExperienceAnalyticsAppHealthApplicationPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_application_performance_by_app_version_details(self) -> UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetails property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_application_performance_by_app_version_details.user_experience_analytics_app_health_application_performance_by_app_version_details_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilder

        return UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_application_performance_by_app_version_device_id(self) -> UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceId property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_application_performance_by_app_version_device_id.user_experience_analytics_app_health_application_performance_by_app_version_device_id_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequestBuilder

        return UserExperienceAnalyticsAppHealthApplicationPerformanceByAppVersionDeviceIdRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_application_performance_by_o_s_version(self) -> UserExperienceAnalyticsAppHealthApplicationPerformanceByOSVersionRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthApplicationPerformanceByOSVersion property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_application_performance_by_o_s_version.user_experience_analytics_app_health_application_performance_by_o_s_version_request_builder import UserExperienceAnalyticsAppHealthApplicationPerformanceByOSVersionRequestBuilder

        return UserExperienceAnalyticsAppHealthApplicationPerformanceByOSVersionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_device_model_performance(self) -> UserExperienceAnalyticsAppHealthDeviceModelPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthDeviceModelPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_device_model_performance.user_experience_analytics_app_health_device_model_performance_request_builder import UserExperienceAnalyticsAppHealthDeviceModelPerformanceRequestBuilder

        return UserExperienceAnalyticsAppHealthDeviceModelPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_device_performance(self) -> UserExperienceAnalyticsAppHealthDevicePerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthDevicePerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_device_performance.user_experience_analytics_app_health_device_performance_request_builder import UserExperienceAnalyticsAppHealthDevicePerformanceRequestBuilder

        return UserExperienceAnalyticsAppHealthDevicePerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_device_performance_details(self) -> UserExperienceAnalyticsAppHealthDevicePerformanceDetailsRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthDevicePerformanceDetails property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_device_performance_details.user_experience_analytics_app_health_device_performance_details_request_builder import UserExperienceAnalyticsAppHealthDevicePerformanceDetailsRequestBuilder

        return UserExperienceAnalyticsAppHealthDevicePerformanceDetailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_o_s_version_performance(self) -> UserExperienceAnalyticsAppHealthOSVersionPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthOSVersionPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_o_s_version_performance.user_experience_analytics_app_health_o_s_version_performance_request_builder import UserExperienceAnalyticsAppHealthOSVersionPerformanceRequestBuilder

        return UserExperienceAnalyticsAppHealthOSVersionPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_app_health_overview(self) -> UserExperienceAnalyticsAppHealthOverviewRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsAppHealthOverview property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_app_health_overview.user_experience_analytics_app_health_overview_request_builder import UserExperienceAnalyticsAppHealthOverviewRequestBuilder

        return UserExperienceAnalyticsAppHealthOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_baselines(self) -> UserExperienceAnalyticsBaselinesRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsBaselines property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_baselines.user_experience_analytics_baselines_request_builder import UserExperienceAnalyticsBaselinesRequestBuilder

        return UserExperienceAnalyticsBaselinesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_categories(self) -> UserExperienceAnalyticsCategoriesRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsCategories property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_categories.user_experience_analytics_categories_request_builder import UserExperienceAnalyticsCategoriesRequestBuilder

        return UserExperienceAnalyticsCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_performance(self) -> UserExperienceAnalyticsDevicePerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDevicePerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_performance.user_experience_analytics_device_performance_request_builder import UserExperienceAnalyticsDevicePerformanceRequestBuilder

        return UserExperienceAnalyticsDevicePerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_scores(self) -> UserExperienceAnalyticsDeviceScoresRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceScores property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_scores.user_experience_analytics_device_scores_request_builder import UserExperienceAnalyticsDeviceScoresRequestBuilder

        return UserExperienceAnalyticsDeviceScoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_startup_history(self) -> UserExperienceAnalyticsDeviceStartupHistoryRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceStartupHistory property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_startup_history.user_experience_analytics_device_startup_history_request_builder import UserExperienceAnalyticsDeviceStartupHistoryRequestBuilder

        return UserExperienceAnalyticsDeviceStartupHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_startup_process_performance(self) -> UserExperienceAnalyticsDeviceStartupProcessPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceStartupProcessPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_startup_process_performance.user_experience_analytics_device_startup_process_performance_request_builder import UserExperienceAnalyticsDeviceStartupProcessPerformanceRequestBuilder

        return UserExperienceAnalyticsDeviceStartupProcessPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_device_startup_processes(self) -> UserExperienceAnalyticsDeviceStartupProcessesRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsDeviceStartupProcesses property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_device_startup_processes.user_experience_analytics_device_startup_processes_request_builder import UserExperienceAnalyticsDeviceStartupProcessesRequestBuilder

        return UserExperienceAnalyticsDeviceStartupProcessesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_metric_history(self) -> UserExperienceAnalyticsMetricHistoryRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsMetricHistory property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_metric_history.user_experience_analytics_metric_history_request_builder import UserExperienceAnalyticsMetricHistoryRequestBuilder

        return UserExperienceAnalyticsMetricHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_model_scores(self) -> UserExperienceAnalyticsModelScoresRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsModelScores property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_model_scores.user_experience_analytics_model_scores_request_builder import UserExperienceAnalyticsModelScoresRequestBuilder

        return UserExperienceAnalyticsModelScoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_overview(self) -> UserExperienceAnalyticsOverviewRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsOverview property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_overview.user_experience_analytics_overview_request_builder import UserExperienceAnalyticsOverviewRequestBuilder

        return UserExperienceAnalyticsOverviewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_score_history(self) -> UserExperienceAnalyticsScoreHistoryRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsScoreHistory property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_score_history.user_experience_analytics_score_history_request_builder import UserExperienceAnalyticsScoreHistoryRequestBuilder

        return UserExperienceAnalyticsScoreHistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_summarize_work_from_anywhere_devices(self) -> UserExperienceAnalyticsSummarizeWorkFromAnywhereDevicesRequestBuilder:
        """
        Provides operations to call the userExperienceAnalyticsSummarizeWorkFromAnywhereDevices method.
        """
        from .user_experience_analytics_summarize_work_from_anywhere_devices.user_experience_analytics_summarize_work_from_anywhere_devices_request_builder import UserExperienceAnalyticsSummarizeWorkFromAnywhereDevicesRequestBuilder

        return UserExperienceAnalyticsSummarizeWorkFromAnywhereDevicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_work_from_anywhere_hardware_readiness_metric(self) -> UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetricRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetric property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_work_from_anywhere_hardware_readiness_metric.user_experience_analytics_work_from_anywhere_hardware_readiness_metric_request_builder import UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetricRequestBuilder

        return UserExperienceAnalyticsWorkFromAnywhereHardwareReadinessMetricRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_work_from_anywhere_metrics(self) -> UserExperienceAnalyticsWorkFromAnywhereMetricsRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsWorkFromAnywhereMetrics property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_work_from_anywhere_metrics.user_experience_analytics_work_from_anywhere_metrics_request_builder import UserExperienceAnalyticsWorkFromAnywhereMetricsRequestBuilder

        return UserExperienceAnalyticsWorkFromAnywhereMetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user_experience_analytics_work_from_anywhere_model_performance(self) -> UserExperienceAnalyticsWorkFromAnywhereModelPerformanceRequestBuilder:
        """
        Provides operations to manage the userExperienceAnalyticsWorkFromAnywhereModelPerformance property of the microsoft.graph.deviceManagement entity.
        """
        from .user_experience_analytics_work_from_anywhere_model_performance.user_experience_analytics_work_from_anywhere_model_performance_request_builder import UserExperienceAnalyticsWorkFromAnywhereModelPerformanceRequestBuilder

        return UserExperienceAnalyticsWorkFromAnywhereModelPerformanceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def virtual_endpoint(self) -> VirtualEndpointRequestBuilder:
        """
        Provides operations to manage the virtualEndpoint property of the microsoft.graph.deviceManagement entity.
        """
        from .virtual_endpoint.virtual_endpoint_request_builder import VirtualEndpointRequestBuilder

        return VirtualEndpointRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    
    @property
    def windows_malware_information(self) -> WindowsMalwareInformationRequestBuilder:
        """
        Provides operations to manage the windowsMalwareInformation property of the microsoft.graph.deviceManagement entity.
        """
        from .windows_malware_information.windows_malware_information_request_builder import WindowsMalwareInformationRequestBuilder

        return WindowsMalwareInformationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DeviceManagementRequestBuilderGetQueryParameters():
        """
        Get deviceManagement
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[list[str]] = None

        # Select properties to be returned
        select: Optional[list[str]] = None

    
    @dataclass
    class DeviceManagementRequestBuilderGetRequestConfiguration(RequestConfiguration[DeviceManagementRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DeviceManagementRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

