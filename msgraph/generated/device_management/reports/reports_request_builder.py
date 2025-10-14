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
    from ...models.device_management_reports import DeviceManagementReports
    from ...models.o_data_errors.o_data_error import ODataError
    from .export_jobs.export_jobs_request_builder import ExportJobsRequestBuilder
    from .get_cached_report.get_cached_report_request_builder import GetCachedReportRequestBuilder
    from .get_compliance_policy_non_compliance_report.get_compliance_policy_non_compliance_report_request_builder import GetCompliancePolicyNonComplianceReportRequestBuilder
    from .get_compliance_policy_non_compliance_summary_report.get_compliance_policy_non_compliance_summary_report_request_builder import GetCompliancePolicyNonComplianceSummaryReportRequestBuilder
    from .get_compliance_setting_non_compliance_report.get_compliance_setting_non_compliance_report_request_builder import GetComplianceSettingNonComplianceReportRequestBuilder
    from .get_configuration_policy_non_compliance_report.get_configuration_policy_non_compliance_report_request_builder import GetConfigurationPolicyNonComplianceReportRequestBuilder
    from .get_configuration_policy_non_compliance_summary_report.get_configuration_policy_non_compliance_summary_report_request_builder import GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder
    from .get_configuration_setting_non_compliance_report.get_configuration_setting_non_compliance_report_request_builder import GetConfigurationSettingNonComplianceReportRequestBuilder
    from .get_devices_without_compliance_policy_report.get_devices_without_compliance_policy_report_request_builder import GetDevicesWithoutCompliancePolicyReportRequestBuilder
    from .get_device_management_intent_per_setting_contributing_profiles.get_device_management_intent_per_setting_contributing_profiles_request_builder import GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder
    from .get_device_management_intent_settings_report.get_device_management_intent_settings_report_request_builder import GetDeviceManagementIntentSettingsReportRequestBuilder
    from .get_device_non_compliance_report.get_device_non_compliance_report_request_builder import GetDeviceNonComplianceReportRequestBuilder
    from .get_historical_report.get_historical_report_request_builder import GetHistoricalReportRequestBuilder
    from .get_noncompliant_devices_and_settings_report.get_noncompliant_devices_and_settings_report_request_builder import GetNoncompliantDevicesAndSettingsReportRequestBuilder
    from .get_policy_non_compliance_metadata.get_policy_non_compliance_metadata_request_builder import GetPolicyNonComplianceMetadataRequestBuilder
    from .get_policy_non_compliance_report.get_policy_non_compliance_report_request_builder import GetPolicyNonComplianceReportRequestBuilder
    from .get_policy_non_compliance_summary_report.get_policy_non_compliance_summary_report_request_builder import GetPolicyNonComplianceSummaryReportRequestBuilder
    from .get_report_filters.get_report_filters_request_builder import GetReportFiltersRequestBuilder
    from .get_setting_non_compliance_report.get_setting_non_compliance_report_request_builder import GetSettingNonComplianceReportRequestBuilder
    from .retrieve_device_app_installation_status_report.retrieve_device_app_installation_status_report_request_builder import RetrieveDeviceAppInstallationStatusReportRequestBuilder

class ReportsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the reports property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ReportsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/reports{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property reports for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ReportsRequestBuilderGetQueryParameters]] = None) -> Optional[DeviceManagementReports]:
        """
        Get reports from deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagementReports]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.device_management_reports import DeviceManagementReports

        return await self.request_adapter.send_async(request_info, DeviceManagementReports, error_mapping)
    
    async def patch(self,body: DeviceManagementReports, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DeviceManagementReports]:
        """
        Update the navigation property reports in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceManagementReports]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.device_management_reports import DeviceManagementReports

        return await self.request_adapter.send_async(request_info, DeviceManagementReports, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property reports for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ReportsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get reports from deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: DeviceManagementReports, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property reports in deviceManagement
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
    
    def with_url(self,raw_url: str) -> ReportsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ReportsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ReportsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def export_jobs(self) -> ExportJobsRequestBuilder:
        """
        Provides operations to manage the exportJobs property of the microsoft.graph.deviceManagementReports entity.
        """
        from .export_jobs.export_jobs_request_builder import ExportJobsRequestBuilder

        return ExportJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_cached_report(self) -> GetCachedReportRequestBuilder:
        """
        Provides operations to call the getCachedReport method.
        """
        from .get_cached_report.get_cached_report_request_builder import GetCachedReportRequestBuilder

        return GetCachedReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_non_compliance_report(self) -> GetCompliancePolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyNonComplianceReport method.
        """
        from .get_compliance_policy_non_compliance_report.get_compliance_policy_non_compliance_report_request_builder import GetCompliancePolicyNonComplianceReportRequestBuilder

        return GetCompliancePolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_non_compliance_summary_report(self) -> GetCompliancePolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyNonComplianceSummaryReport method.
        """
        from .get_compliance_policy_non_compliance_summary_report.get_compliance_policy_non_compliance_summary_report_request_builder import GetCompliancePolicyNonComplianceSummaryReportRequestBuilder

        return GetCompliancePolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_setting_non_compliance_report(self) -> GetComplianceSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getComplianceSettingNonComplianceReport method.
        """
        from .get_compliance_setting_non_compliance_report.get_compliance_setting_non_compliance_report_request_builder import GetComplianceSettingNonComplianceReportRequestBuilder

        return GetComplianceSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_non_compliance_report(self) -> GetConfigurationPolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyNonComplianceReport method.
        """
        from .get_configuration_policy_non_compliance_report.get_configuration_policy_non_compliance_report_request_builder import GetConfigurationPolicyNonComplianceReportRequestBuilder

        return GetConfigurationPolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_non_compliance_summary_report(self) -> GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyNonComplianceSummaryReport method.
        """
        from .get_configuration_policy_non_compliance_summary_report.get_configuration_policy_non_compliance_summary_report_request_builder import GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder

        return GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_setting_non_compliance_report(self) -> GetConfigurationSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getConfigurationSettingNonComplianceReport method.
        """
        from .get_configuration_setting_non_compliance_report.get_configuration_setting_non_compliance_report_request_builder import GetConfigurationSettingNonComplianceReportRequestBuilder

        return GetConfigurationSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_management_intent_per_setting_contributing_profiles(self) -> GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder:
        """
        Provides operations to call the getDeviceManagementIntentPerSettingContributingProfiles method.
        """
        from .get_device_management_intent_per_setting_contributing_profiles.get_device_management_intent_per_setting_contributing_profiles_request_builder import GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder

        return GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_management_intent_settings_report(self) -> GetDeviceManagementIntentSettingsReportRequestBuilder:
        """
        Provides operations to call the getDeviceManagementIntentSettingsReport method.
        """
        from .get_device_management_intent_settings_report.get_device_management_intent_settings_report_request_builder import GetDeviceManagementIntentSettingsReportRequestBuilder

        return GetDeviceManagementIntentSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_non_compliance_report(self) -> GetDeviceNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getDeviceNonComplianceReport method.
        """
        from .get_device_non_compliance_report.get_device_non_compliance_report_request_builder import GetDeviceNonComplianceReportRequestBuilder

        return GetDeviceNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_devices_without_compliance_policy_report(self) -> GetDevicesWithoutCompliancePolicyReportRequestBuilder:
        """
        Provides operations to call the getDevicesWithoutCompliancePolicyReport method.
        """
        from .get_devices_without_compliance_policy_report.get_devices_without_compliance_policy_report_request_builder import GetDevicesWithoutCompliancePolicyReportRequestBuilder

        return GetDevicesWithoutCompliancePolicyReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_historical_report(self) -> GetHistoricalReportRequestBuilder:
        """
        Provides operations to call the getHistoricalReport method.
        """
        from .get_historical_report.get_historical_report_request_builder import GetHistoricalReportRequestBuilder

        return GetHistoricalReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_noncompliant_devices_and_settings_report(self) -> GetNoncompliantDevicesAndSettingsReportRequestBuilder:
        """
        Provides operations to call the getNoncompliantDevicesAndSettingsReport method.
        """
        from .get_noncompliant_devices_and_settings_report.get_noncompliant_devices_and_settings_report_request_builder import GetNoncompliantDevicesAndSettingsReportRequestBuilder

        return GetNoncompliantDevicesAndSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_policy_non_compliance_metadata(self) -> GetPolicyNonComplianceMetadataRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceMetadata method.
        """
        from .get_policy_non_compliance_metadata.get_policy_non_compliance_metadata_request_builder import GetPolicyNonComplianceMetadataRequestBuilder

        return GetPolicyNonComplianceMetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_policy_non_compliance_report(self) -> GetPolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceReport method.
        """
        from .get_policy_non_compliance_report.get_policy_non_compliance_report_request_builder import GetPolicyNonComplianceReportRequestBuilder

        return GetPolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_policy_non_compliance_summary_report(self) -> GetPolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceSummaryReport method.
        """
        from .get_policy_non_compliance_summary_report.get_policy_non_compliance_summary_report_request_builder import GetPolicyNonComplianceSummaryReportRequestBuilder

        return GetPolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_report_filters(self) -> GetReportFiltersRequestBuilder:
        """
        Provides operations to call the getReportFilters method.
        """
        from .get_report_filters.get_report_filters_request_builder import GetReportFiltersRequestBuilder

        return GetReportFiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_setting_non_compliance_report(self) -> GetSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getSettingNonComplianceReport method.
        """
        from .get_setting_non_compliance_report.get_setting_non_compliance_report_request_builder import GetSettingNonComplianceReportRequestBuilder

        return GetSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def retrieve_device_app_installation_status_report(self) -> RetrieveDeviceAppInstallationStatusReportRequestBuilder:
        """
        Provides operations to call the retrieveDeviceAppInstallationStatusReport method.
        """
        from .retrieve_device_app_installation_status_report.retrieve_device_app_installation_status_report_request_builder import RetrieveDeviceAppInstallationStatusReportRequestBuilder

        return RetrieveDeviceAppInstallationStatusReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ReportsRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ReportsRequestBuilderGetQueryParameters():
        """
        Get reports from deviceManagement
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
    class ReportsRequestBuilderGetRequestConfiguration(RequestConfiguration[ReportsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ReportsRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

