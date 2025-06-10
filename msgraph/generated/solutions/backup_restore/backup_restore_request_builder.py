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
    from ...models.backup_restore_root import BackupRestoreRoot
    from ...models.o_data_errors.o_data_error import ODataError
    from .drive_inclusion_rules.drive_inclusion_rules_request_builder import DriveInclusionRulesRequestBuilder
    from .drive_protection_units.drive_protection_units_request_builder import DriveProtectionUnitsRequestBuilder
    from .drive_protection_units_bulk_addition_jobs.drive_protection_units_bulk_addition_jobs_request_builder import DriveProtectionUnitsBulkAdditionJobsRequestBuilder
    from .enable.enable_request_builder import EnableRequestBuilder
    from .exchange_protection_policies.exchange_protection_policies_request_builder import ExchangeProtectionPoliciesRequestBuilder
    from .exchange_restore_sessions.exchange_restore_sessions_request_builder import ExchangeRestoreSessionsRequestBuilder
    from .mailbox_inclusion_rules.mailbox_inclusion_rules_request_builder import MailboxInclusionRulesRequestBuilder
    from .mailbox_protection_units.mailbox_protection_units_request_builder import MailboxProtectionUnitsRequestBuilder
    from .mailbox_protection_units_bulk_addition_jobs.mailbox_protection_units_bulk_addition_jobs_request_builder import MailboxProtectionUnitsBulkAdditionJobsRequestBuilder
    from .one_drive_for_business_protection_policies.one_drive_for_business_protection_policies_request_builder import OneDriveForBusinessProtectionPoliciesRequestBuilder
    from .one_drive_for_business_restore_sessions.one_drive_for_business_restore_sessions_request_builder import OneDriveForBusinessRestoreSessionsRequestBuilder
    from .protection_policies.protection_policies_request_builder import ProtectionPoliciesRequestBuilder
    from .protection_units.protection_units_request_builder import ProtectionUnitsRequestBuilder
    from .restore_points.restore_points_request_builder import RestorePointsRequestBuilder
    from .restore_sessions.restore_sessions_request_builder import RestoreSessionsRequestBuilder
    from .service_apps.service_apps_request_builder import ServiceAppsRequestBuilder
    from .share_point_protection_policies.share_point_protection_policies_request_builder import SharePointProtectionPoliciesRequestBuilder
    from .share_point_restore_sessions.share_point_restore_sessions_request_builder import SharePointRestoreSessionsRequestBuilder
    from .site_inclusion_rules.site_inclusion_rules_request_builder import SiteInclusionRulesRequestBuilder
    from .site_protection_units.site_protection_units_request_builder import SiteProtectionUnitsRequestBuilder
    from .site_protection_units_bulk_addition_jobs.site_protection_units_bulk_addition_jobs_request_builder import SiteProtectionUnitsBulkAdditionJobsRequestBuilder

class BackupRestoreRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the backupRestore property of the microsoft.graph.solutionsRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BackupRestoreRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property backupRestore for solutions
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[BackupRestoreRequestBuilderGetQueryParameters]] = None) -> Optional[BackupRestoreRoot]:
        """
        Get the serviceStatus of the Microsoft 365 Backup Storage service in a tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BackupRestoreRoot]
        Find more info here: https://learn.microsoft.com/graph/api/backuprestoreroot-get?view=graph-rest-1.0
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
        from ...models.backup_restore_root import BackupRestoreRoot

        return await self.request_adapter.send_async(request_info, BackupRestoreRoot, error_mapping)
    
    async def patch(self,body: BackupRestoreRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[BackupRestoreRoot]:
        """
        Update the navigation property backupRestore in solutions
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BackupRestoreRoot]
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
        from ...models.backup_restore_root import BackupRestoreRoot

        return await self.request_adapter.send_async(request_info, BackupRestoreRoot, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property backupRestore for solutions
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[BackupRestoreRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get the serviceStatus of the Microsoft 365 Backup Storage service in a tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: BackupRestoreRoot, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property backupRestore in solutions
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
    
    def with_url(self,raw_url: str) -> BackupRestoreRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: BackupRestoreRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return BackupRestoreRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def drive_inclusion_rules(self) -> DriveInclusionRulesRequestBuilder:
        """
        Provides operations to manage the driveInclusionRules property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .drive_inclusion_rules.drive_inclusion_rules_request_builder import DriveInclusionRulesRequestBuilder

        return DriveInclusionRulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive_protection_units(self) -> DriveProtectionUnitsRequestBuilder:
        """
        Provides operations to manage the driveProtectionUnits property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .drive_protection_units.drive_protection_units_request_builder import DriveProtectionUnitsRequestBuilder

        return DriveProtectionUnitsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive_protection_units_bulk_addition_jobs(self) -> DriveProtectionUnitsBulkAdditionJobsRequestBuilder:
        """
        Provides operations to manage the driveProtectionUnitsBulkAdditionJobs property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .drive_protection_units_bulk_addition_jobs.drive_protection_units_bulk_addition_jobs_request_builder import DriveProtectionUnitsBulkAdditionJobsRequestBuilder

        return DriveProtectionUnitsBulkAdditionJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def enable(self) -> EnableRequestBuilder:
        """
        Provides operations to call the enable method.
        """
        from .enable.enable_request_builder import EnableRequestBuilder

        return EnableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exchange_protection_policies(self) -> ExchangeProtectionPoliciesRequestBuilder:
        """
        Provides operations to manage the exchangeProtectionPolicies property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .exchange_protection_policies.exchange_protection_policies_request_builder import ExchangeProtectionPoliciesRequestBuilder

        return ExchangeProtectionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def exchange_restore_sessions(self) -> ExchangeRestoreSessionsRequestBuilder:
        """
        Provides operations to manage the exchangeRestoreSessions property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .exchange_restore_sessions.exchange_restore_sessions_request_builder import ExchangeRestoreSessionsRequestBuilder

        return ExchangeRestoreSessionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mailbox_inclusion_rules(self) -> MailboxInclusionRulesRequestBuilder:
        """
        Provides operations to manage the mailboxInclusionRules property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .mailbox_inclusion_rules.mailbox_inclusion_rules_request_builder import MailboxInclusionRulesRequestBuilder

        return MailboxInclusionRulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mailbox_protection_units(self) -> MailboxProtectionUnitsRequestBuilder:
        """
        Provides operations to manage the mailboxProtectionUnits property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .mailbox_protection_units.mailbox_protection_units_request_builder import MailboxProtectionUnitsRequestBuilder

        return MailboxProtectionUnitsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mailbox_protection_units_bulk_addition_jobs(self) -> MailboxProtectionUnitsBulkAdditionJobsRequestBuilder:
        """
        Provides operations to manage the mailboxProtectionUnitsBulkAdditionJobs property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .mailbox_protection_units_bulk_addition_jobs.mailbox_protection_units_bulk_addition_jobs_request_builder import MailboxProtectionUnitsBulkAdditionJobsRequestBuilder

        return MailboxProtectionUnitsBulkAdditionJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def one_drive_for_business_protection_policies(self) -> OneDriveForBusinessProtectionPoliciesRequestBuilder:
        """
        Provides operations to manage the oneDriveForBusinessProtectionPolicies property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .one_drive_for_business_protection_policies.one_drive_for_business_protection_policies_request_builder import OneDriveForBusinessProtectionPoliciesRequestBuilder

        return OneDriveForBusinessProtectionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def one_drive_for_business_restore_sessions(self) -> OneDriveForBusinessRestoreSessionsRequestBuilder:
        """
        Provides operations to manage the oneDriveForBusinessRestoreSessions property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .one_drive_for_business_restore_sessions.one_drive_for_business_restore_sessions_request_builder import OneDriveForBusinessRestoreSessionsRequestBuilder

        return OneDriveForBusinessRestoreSessionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def protection_policies(self) -> ProtectionPoliciesRequestBuilder:
        """
        Provides operations to manage the protectionPolicies property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .protection_policies.protection_policies_request_builder import ProtectionPoliciesRequestBuilder

        return ProtectionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def protection_units(self) -> ProtectionUnitsRequestBuilder:
        """
        Provides operations to manage the protectionUnits property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .protection_units.protection_units_request_builder import ProtectionUnitsRequestBuilder

        return ProtectionUnitsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore_points(self) -> RestorePointsRequestBuilder:
        """
        Provides operations to manage the restorePoints property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .restore_points.restore_points_request_builder import RestorePointsRequestBuilder

        return RestorePointsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore_sessions(self) -> RestoreSessionsRequestBuilder:
        """
        Provides operations to manage the restoreSessions property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .restore_sessions.restore_sessions_request_builder import RestoreSessionsRequestBuilder

        return RestoreSessionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_apps(self) -> ServiceAppsRequestBuilder:
        """
        Provides operations to manage the serviceApps property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .service_apps.service_apps_request_builder import ServiceAppsRequestBuilder

        return ServiceAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def share_point_protection_policies(self) -> SharePointProtectionPoliciesRequestBuilder:
        """
        Provides operations to manage the sharePointProtectionPolicies property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .share_point_protection_policies.share_point_protection_policies_request_builder import SharePointProtectionPoliciesRequestBuilder

        return SharePointProtectionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def share_point_restore_sessions(self) -> SharePointRestoreSessionsRequestBuilder:
        """
        Provides operations to manage the sharePointRestoreSessions property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .share_point_restore_sessions.share_point_restore_sessions_request_builder import SharePointRestoreSessionsRequestBuilder

        return SharePointRestoreSessionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def site_inclusion_rules(self) -> SiteInclusionRulesRequestBuilder:
        """
        Provides operations to manage the siteInclusionRules property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .site_inclusion_rules.site_inclusion_rules_request_builder import SiteInclusionRulesRequestBuilder

        return SiteInclusionRulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def site_protection_units(self) -> SiteProtectionUnitsRequestBuilder:
        """
        Provides operations to manage the siteProtectionUnits property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .site_protection_units.site_protection_units_request_builder import SiteProtectionUnitsRequestBuilder

        return SiteProtectionUnitsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def site_protection_units_bulk_addition_jobs(self) -> SiteProtectionUnitsBulkAdditionJobsRequestBuilder:
        """
        Provides operations to manage the siteProtectionUnitsBulkAdditionJobs property of the microsoft.graph.backupRestoreRoot entity.
        """
        from .site_protection_units_bulk_addition_jobs.site_protection_units_bulk_addition_jobs_request_builder import SiteProtectionUnitsBulkAdditionJobsRequestBuilder

        return SiteProtectionUnitsBulkAdditionJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class BackupRestoreRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class BackupRestoreRequestBuilderGetQueryParameters():
        """
        Get the serviceStatus of the Microsoft 365 Backup Storage service in a tenant.
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
    class BackupRestoreRequestBuilderGetRequestConfiguration(RequestConfiguration[BackupRestoreRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class BackupRestoreRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

