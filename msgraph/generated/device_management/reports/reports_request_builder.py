from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

export_jobs_request_builder = lazy_import('msgraph.generated.device_management.reports.export_jobs.export_jobs_request_builder')
device_management_export_job_item_request_builder = lazy_import('msgraph.generated.device_management.reports.export_jobs.item.device_management_export_job_item_request_builder')
get_cached_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_cached_report.get_cached_report_request_builder')
get_compliance_policy_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_compliance_policy_non_compliance_report.get_compliance_policy_non_compliance_report_request_builder')
get_compliance_policy_non_compliance_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_compliance_policy_non_compliance_summary_report.get_compliance_policy_non_compliance_summary_report_request_builder')
get_compliance_setting_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_compliance_setting_non_compliance_report.get_compliance_setting_non_compliance_report_request_builder')
get_configuration_policy_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_configuration_policy_non_compliance_report.get_configuration_policy_non_compliance_report_request_builder')
get_configuration_policy_non_compliance_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_configuration_policy_non_compliance_summary_report.get_configuration_policy_non_compliance_summary_report_request_builder')
get_configuration_setting_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_configuration_setting_non_compliance_report.get_configuration_setting_non_compliance_report_request_builder')
get_device_management_intent_per_setting_contributing_profiles_request_builder = lazy_import('msgraph.generated.device_management.reports.get_device_management_intent_per_setting_contributing_profiles.get_device_management_intent_per_setting_contributing_profiles_request_builder')
get_device_management_intent_settings_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_device_management_intent_settings_report.get_device_management_intent_settings_report_request_builder')
get_device_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_device_non_compliance_report.get_device_non_compliance_report_request_builder')
get_historical_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_historical_report.get_historical_report_request_builder')
get_noncompliant_devices_and_settings_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_noncompliant_devices_and_settings_report.get_noncompliant_devices_and_settings_report_request_builder')
get_policy_non_compliance_metadata_request_builder = lazy_import('msgraph.generated.device_management.reports.get_policy_non_compliance_metadata.get_policy_non_compliance_metadata_request_builder')
get_policy_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_policy_non_compliance_report.get_policy_non_compliance_report_request_builder')
get_policy_non_compliance_summary_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_policy_non_compliance_summary_report.get_policy_non_compliance_summary_report_request_builder')
get_report_filters_request_builder = lazy_import('msgraph.generated.device_management.reports.get_report_filters.get_report_filters_request_builder')
get_setting_non_compliance_report_request_builder = lazy_import('msgraph.generated.device_management.reports.get_setting_non_compliance_report.get_setting_non_compliance_report_request_builder')
device_management_reports = lazy_import('msgraph.generated.models.device_management_reports')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class ReportsRequestBuilder():
    """
    Provides operations to manage the reports property of the microsoft.graph.deviceManagement entity.
    """
    def export_jobs(self) -> export_jobs_request_builder.ExportJobsRequestBuilder:
        """
        Provides operations to manage the exportJobs property of the microsoft.graph.deviceManagementReports entity.
        """
        return export_jobs_request_builder.ExportJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_cached_report(self) -> get_cached_report_request_builder.GetCachedReportRequestBuilder:
        """
        Provides operations to call the getCachedReport method.
        """
        return get_cached_report_request_builder.GetCachedReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_compliance_policy_non_compliance_report(self) -> get_compliance_policy_non_compliance_report_request_builder.GetCompliancePolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyNonComplianceReport method.
        """
        return get_compliance_policy_non_compliance_report_request_builder.GetCompliancePolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_compliance_policy_non_compliance_summary_report(self) -> get_compliance_policy_non_compliance_summary_report_request_builder.GetCompliancePolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyNonComplianceSummaryReport method.
        """
        return get_compliance_policy_non_compliance_summary_report_request_builder.GetCompliancePolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_compliance_setting_non_compliance_report(self) -> get_compliance_setting_non_compliance_report_request_builder.GetComplianceSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getComplianceSettingNonComplianceReport method.
        """
        return get_compliance_setting_non_compliance_report_request_builder.GetComplianceSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_configuration_policy_non_compliance_report(self) -> get_configuration_policy_non_compliance_report_request_builder.GetConfigurationPolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyNonComplianceReport method.
        """
        return get_configuration_policy_non_compliance_report_request_builder.GetConfigurationPolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_configuration_policy_non_compliance_summary_report(self) -> get_configuration_policy_non_compliance_summary_report_request_builder.GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyNonComplianceSummaryReport method.
        """
        return get_configuration_policy_non_compliance_summary_report_request_builder.GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_configuration_setting_non_compliance_report(self) -> get_configuration_setting_non_compliance_report_request_builder.GetConfigurationSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getConfigurationSettingNonComplianceReport method.
        """
        return get_configuration_setting_non_compliance_report_request_builder.GetConfigurationSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_device_management_intent_per_setting_contributing_profiles(self) -> get_device_management_intent_per_setting_contributing_profiles_request_builder.GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder:
        """
        Provides operations to call the getDeviceManagementIntentPerSettingContributingProfiles method.
        """
        return get_device_management_intent_per_setting_contributing_profiles_request_builder.GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_device_management_intent_settings_report(self) -> get_device_management_intent_settings_report_request_builder.GetDeviceManagementIntentSettingsReportRequestBuilder:
        """
        Provides operations to call the getDeviceManagementIntentSettingsReport method.
        """
        return get_device_management_intent_settings_report_request_builder.GetDeviceManagementIntentSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_device_non_compliance_report(self) -> get_device_non_compliance_report_request_builder.GetDeviceNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getDeviceNonComplianceReport method.
        """
        return get_device_non_compliance_report_request_builder.GetDeviceNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_historical_report(self) -> get_historical_report_request_builder.GetHistoricalReportRequestBuilder:
        """
        Provides operations to call the getHistoricalReport method.
        """
        return get_historical_report_request_builder.GetHistoricalReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_noncompliant_devices_and_settings_report(self) -> get_noncompliant_devices_and_settings_report_request_builder.GetNoncompliantDevicesAndSettingsReportRequestBuilder:
        """
        Provides operations to call the getNoncompliantDevicesAndSettingsReport method.
        """
        return get_noncompliant_devices_and_settings_report_request_builder.GetNoncompliantDevicesAndSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_policy_non_compliance_metadata(self) -> get_policy_non_compliance_metadata_request_builder.GetPolicyNonComplianceMetadataRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceMetadata method.
        """
        return get_policy_non_compliance_metadata_request_builder.GetPolicyNonComplianceMetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_policy_non_compliance_report(self) -> get_policy_non_compliance_report_request_builder.GetPolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceReport method.
        """
        return get_policy_non_compliance_report_request_builder.GetPolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_policy_non_compliance_summary_report(self) -> get_policy_non_compliance_summary_report_request_builder.GetPolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceSummaryReport method.
        """
        return get_policy_non_compliance_summary_report_request_builder.GetPolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_report_filters(self) -> get_report_filters_request_builder.GetReportFiltersRequestBuilder:
        """
        Provides operations to call the getReportFilters method.
        """
        return get_report_filters_request_builder.GetReportFiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    def get_setting_non_compliance_report(self) -> get_setting_non_compliance_report_request_builder.GetSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getSettingNonComplianceReport method.
        """
        return get_setting_non_compliance_report_request_builder.GetSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ReportsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/reports{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[ReportsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property reports for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_get_request_information(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Reports singleton
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
    
    def create_patch_request_information(self,body: Optional[device_management_reports.DeviceManagementReports] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property reports in deviceManagement
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
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
    
    async def delete(self,request_configuration: Optional[ReportsRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property reports for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    def export_jobs_by_id(self,id: str) -> device_management_export_job_item_request_builder.DeviceManagementExportJobItemRequestBuilder:
        """
        Provides operations to manage the exportJobs property of the microsoft.graph.deviceManagementReports entity.
        Args:
            id: Unique identifier of the item
        Returns: device_management_export_job_item_request_builder.DeviceManagementExportJobItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["deviceManagementExportJob%2Did"] = id
        return device_management_export_job_item_request_builder.DeviceManagementExportJobItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_management_reports.DeviceManagementReports]:
        """
        Reports singleton
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_management_reports.DeviceManagementReports]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, device_management_reports.DeviceManagementReports, response_handler, error_mapping)
    
    async def patch(self,body: Optional[device_management_reports.DeviceManagementReports] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[device_management_reports.DeviceManagementReports]:
        """
        Update the navigation property reports in deviceManagement
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[device_management_reports.DeviceManagementReports]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, device_management_reports.DeviceManagementReports, response_handler, error_mapping)
    
    @dataclass
    class ReportsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ReportsRequestBuilderGetQueryParameters():
        """
        Reports singleton
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
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class ReportsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ReportsRequestBuilder.ReportsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ReportsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

