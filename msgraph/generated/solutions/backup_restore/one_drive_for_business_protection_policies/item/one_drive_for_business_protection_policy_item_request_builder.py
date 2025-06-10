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
    from .....models.one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy
    from .....models.o_data_errors.o_data_error import ODataError
    from .drive_inclusion_rules.drive_inclusion_rules_request_builder import DriveInclusionRulesRequestBuilder
    from .drive_protection_units.drive_protection_units_request_builder import DriveProtectionUnitsRequestBuilder
    from .drive_protection_units_bulk_addition_jobs.drive_protection_units_bulk_addition_jobs_request_builder import DriveProtectionUnitsBulkAdditionJobsRequestBuilder

class OneDriveForBusinessProtectionPolicyItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the oneDriveForBusinessProtectionPolicies property of the microsoft.graph.backupRestoreRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OneDriveForBusinessProtectionPolicyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/solutions/backupRestore/oneDriveForBusinessProtectionPolicies/{oneDriveForBusinessProtectionPolicy%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property oneDriveForBusinessProtectionPolicies for solutions
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[OneDriveForBusinessProtectionPolicyItemRequestBuilderGetQueryParameters]] = None) -> Optional[OneDriveForBusinessProtectionPolicy]:
        """
        The list of OneDrive for Business protection policies in the tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OneDriveForBusinessProtectionPolicy]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy

        return await self.request_adapter.send_async(request_info, OneDriveForBusinessProtectionPolicy, error_mapping)
    
    async def patch(self,body: OneDriveForBusinessProtectionPolicy, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[OneDriveForBusinessProtectionPolicy]:
        """
        Update the protection policy for the OneDrive service in Microsoft 365. This method adds a driveProtectionUnit to or removes it from a oneDriveForBusinessProtectionPolicy object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OneDriveForBusinessProtectionPolicy]
        Find more info here: https://learn.microsoft.com/graph/api/onedriveforbusinessprotectionpolicy-update?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.one_drive_for_business_protection_policy import OneDriveForBusinessProtectionPolicy

        return await self.request_adapter.send_async(request_info, OneDriveForBusinessProtectionPolicy, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property oneDriveForBusinessProtectionPolicies for solutions
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[OneDriveForBusinessProtectionPolicyItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        The list of OneDrive for Business protection policies in the tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: OneDriveForBusinessProtectionPolicy, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the protection policy for the OneDrive service in Microsoft 365. This method adds a driveProtectionUnit to or removes it from a oneDriveForBusinessProtectionPolicy object.
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
    
    def with_url(self,raw_url: str) -> OneDriveForBusinessProtectionPolicyItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OneDriveForBusinessProtectionPolicyItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return OneDriveForBusinessProtectionPolicyItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def drive_inclusion_rules(self) -> DriveInclusionRulesRequestBuilder:
        """
        Provides operations to manage the driveInclusionRules property of the microsoft.graph.oneDriveForBusinessProtectionPolicy entity.
        """
        from .drive_inclusion_rules.drive_inclusion_rules_request_builder import DriveInclusionRulesRequestBuilder

        return DriveInclusionRulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive_protection_units(self) -> DriveProtectionUnitsRequestBuilder:
        """
        Provides operations to manage the driveProtectionUnits property of the microsoft.graph.oneDriveForBusinessProtectionPolicy entity.
        """
        from .drive_protection_units.drive_protection_units_request_builder import DriveProtectionUnitsRequestBuilder

        return DriveProtectionUnitsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive_protection_units_bulk_addition_jobs(self) -> DriveProtectionUnitsBulkAdditionJobsRequestBuilder:
        """
        Provides operations to manage the driveProtectionUnitsBulkAdditionJobs property of the microsoft.graph.oneDriveForBusinessProtectionPolicy entity.
        """
        from .drive_protection_units_bulk_addition_jobs.drive_protection_units_bulk_addition_jobs_request_builder import DriveProtectionUnitsBulkAdditionJobsRequestBuilder

        return DriveProtectionUnitsBulkAdditionJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class OneDriveForBusinessProtectionPolicyItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OneDriveForBusinessProtectionPolicyItemRequestBuilderGetQueryParameters():
        """
        The list of OneDrive for Business protection policies in the tenant.
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
    class OneDriveForBusinessProtectionPolicyItemRequestBuilderGetRequestConfiguration(RequestConfiguration[OneDriveForBusinessProtectionPolicyItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OneDriveForBusinessProtectionPolicyItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

