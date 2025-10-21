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
    from ..models.device_app_management import DeviceAppManagement
    from ..models.o_data_errors.o_data_error import ODataError
    from .android_managed_app_protections.android_managed_app_protections_request_builder import AndroidManagedAppProtectionsRequestBuilder
    from .default_managed_app_protections.default_managed_app_protections_request_builder import DefaultManagedAppProtectionsRequestBuilder
    from .ios_managed_app_protections.ios_managed_app_protections_request_builder import IosManagedAppProtectionsRequestBuilder
    from .managed_app_policies.managed_app_policies_request_builder import ManagedAppPoliciesRequestBuilder
    from .managed_app_registrations.managed_app_registrations_request_builder import ManagedAppRegistrationsRequestBuilder
    from .managed_app_statuses.managed_app_statuses_request_builder import ManagedAppStatusesRequestBuilder
    from .managed_e_books.managed_e_books_request_builder import ManagedEBooksRequestBuilder
    from .mdm_windows_information_protection_policies.mdm_windows_information_protection_policies_request_builder import MdmWindowsInformationProtectionPoliciesRequestBuilder
    from .mobile_apps.mobile_apps_request_builder import MobileAppsRequestBuilder
    from .mobile_app_categories.mobile_app_categories_request_builder import MobileAppCategoriesRequestBuilder
    from .mobile_app_configurations.mobile_app_configurations_request_builder import MobileAppConfigurationsRequestBuilder
    from .mobile_app_relationships.mobile_app_relationships_request_builder import MobileAppRelationshipsRequestBuilder
    from .sync_microsoft_store_for_business_apps.sync_microsoft_store_for_business_apps_request_builder import SyncMicrosoftStoreForBusinessAppsRequestBuilder
    from .targeted_managed_app_configurations.targeted_managed_app_configurations_request_builder import TargetedManagedAppConfigurationsRequestBuilder
    from .vpp_tokens.vpp_tokens_request_builder import VppTokensRequestBuilder
    from .windows_information_protection_policies.windows_information_protection_policies_request_builder import WindowsInformationProtectionPoliciesRequestBuilder

class DeviceAppManagementRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the deviceAppManagement singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DeviceAppManagementRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceAppManagement{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DeviceAppManagementRequestBuilderGetQueryParameters]] = None) -> Optional[DeviceAppManagement]:
        """
        Read properties and relationships of the deviceAppManagement object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceAppManagement]
        Find more info here: https://learn.microsoft.com/graph/api/intune-policyset-deviceappmanagement-get?view=graph-rest-1.0
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
        from ..models.device_app_management import DeviceAppManagement

        return await self.request_adapter.send_async(request_info, DeviceAppManagement, error_mapping)
    
    async def patch(self,body: DeviceAppManagement, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DeviceAppManagement]:
        """
        Update the properties of a deviceAppManagement object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DeviceAppManagement]
        Find more info here: https://learn.microsoft.com/graph/api/intune-policyset-deviceappmanagement-update?view=graph-rest-1.0
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
        from ..models.device_app_management import DeviceAppManagement

        return await self.request_adapter.send_async(request_info, DeviceAppManagement, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DeviceAppManagementRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read properties and relationships of the deviceAppManagement object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: DeviceAppManagement, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of a deviceAppManagement object.
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
    
    def with_url(self,raw_url: str) -> DeviceAppManagementRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DeviceAppManagementRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DeviceAppManagementRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def android_managed_app_protections(self) -> AndroidManagedAppProtectionsRequestBuilder:
        """
        Provides operations to manage the androidManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        """
        from .android_managed_app_protections.android_managed_app_protections_request_builder import AndroidManagedAppProtectionsRequestBuilder

        return AndroidManagedAppProtectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def default_managed_app_protections(self) -> DefaultManagedAppProtectionsRequestBuilder:
        """
        Provides operations to manage the defaultManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        """
        from .default_managed_app_protections.default_managed_app_protections_request_builder import DefaultManagedAppProtectionsRequestBuilder

        return DefaultManagedAppProtectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ios_managed_app_protections(self) -> IosManagedAppProtectionsRequestBuilder:
        """
        Provides operations to manage the iosManagedAppProtections property of the microsoft.graph.deviceAppManagement entity.
        """
        from .ios_managed_app_protections.ios_managed_app_protections_request_builder import IosManagedAppProtectionsRequestBuilder

        return IosManagedAppProtectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_app_policies(self) -> ManagedAppPoliciesRequestBuilder:
        """
        Provides operations to manage the managedAppPolicies property of the microsoft.graph.deviceAppManagement entity.
        """
        from .managed_app_policies.managed_app_policies_request_builder import ManagedAppPoliciesRequestBuilder

        return ManagedAppPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_app_registrations(self) -> ManagedAppRegistrationsRequestBuilder:
        """
        Provides operations to manage the managedAppRegistrations property of the microsoft.graph.deviceAppManagement entity.
        """
        from .managed_app_registrations.managed_app_registrations_request_builder import ManagedAppRegistrationsRequestBuilder

        return ManagedAppRegistrationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_app_statuses(self) -> ManagedAppStatusesRequestBuilder:
        """
        Provides operations to manage the managedAppStatuses property of the microsoft.graph.deviceAppManagement entity.
        """
        from .managed_app_statuses.managed_app_statuses_request_builder import ManagedAppStatusesRequestBuilder

        return ManagedAppStatusesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def managed_e_books(self) -> ManagedEBooksRequestBuilder:
        """
        Provides operations to manage the managedEBooks property of the microsoft.graph.deviceAppManagement entity.
        """
        from .managed_e_books.managed_e_books_request_builder import ManagedEBooksRequestBuilder

        return ManagedEBooksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mdm_windows_information_protection_policies(self) -> MdmWindowsInformationProtectionPoliciesRequestBuilder:
        """
        Provides operations to manage the mdmWindowsInformationProtectionPolicies property of the microsoft.graph.deviceAppManagement entity.
        """
        from .mdm_windows_information_protection_policies.mdm_windows_information_protection_policies_request_builder import MdmWindowsInformationProtectionPoliciesRequestBuilder

        return MdmWindowsInformationProtectionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_categories(self) -> MobileAppCategoriesRequestBuilder:
        """
        Provides operations to manage the mobileAppCategories property of the microsoft.graph.deviceAppManagement entity.
        """
        from .mobile_app_categories.mobile_app_categories_request_builder import MobileAppCategoriesRequestBuilder

        return MobileAppCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_configurations(self) -> MobileAppConfigurationsRequestBuilder:
        """
        Provides operations to manage the mobileAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
        """
        from .mobile_app_configurations.mobile_app_configurations_request_builder import MobileAppConfigurationsRequestBuilder

        return MobileAppConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_app_relationships(self) -> MobileAppRelationshipsRequestBuilder:
        """
        Provides operations to manage the mobileAppRelationships property of the microsoft.graph.deviceAppManagement entity.
        """
        from .mobile_app_relationships.mobile_app_relationships_request_builder import MobileAppRelationshipsRequestBuilder

        return MobileAppRelationshipsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mobile_apps(self) -> MobileAppsRequestBuilder:
        """
        Provides operations to manage the mobileApps property of the microsoft.graph.deviceAppManagement entity.
        """
        from .mobile_apps.mobile_apps_request_builder import MobileAppsRequestBuilder

        return MobileAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sync_microsoft_store_for_business_apps(self) -> SyncMicrosoftStoreForBusinessAppsRequestBuilder:
        """
        Provides operations to call the syncMicrosoftStoreForBusinessApps method.
        """
        from .sync_microsoft_store_for_business_apps.sync_microsoft_store_for_business_apps_request_builder import SyncMicrosoftStoreForBusinessAppsRequestBuilder

        return SyncMicrosoftStoreForBusinessAppsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def targeted_managed_app_configurations(self) -> TargetedManagedAppConfigurationsRequestBuilder:
        """
        Provides operations to manage the targetedManagedAppConfigurations property of the microsoft.graph.deviceAppManagement entity.
        """
        from .targeted_managed_app_configurations.targeted_managed_app_configurations_request_builder import TargetedManagedAppConfigurationsRequestBuilder

        return TargetedManagedAppConfigurationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vpp_tokens(self) -> VppTokensRequestBuilder:
        """
        Provides operations to manage the vppTokens property of the microsoft.graph.deviceAppManagement entity.
        """
        from .vpp_tokens.vpp_tokens_request_builder import VppTokensRequestBuilder

        return VppTokensRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def windows_information_protection_policies(self) -> WindowsInformationProtectionPoliciesRequestBuilder:
        """
        Provides operations to manage the windowsInformationProtectionPolicies property of the microsoft.graph.deviceAppManagement entity.
        """
        from .windows_information_protection_policies.windows_information_protection_policies_request_builder import WindowsInformationProtectionPoliciesRequestBuilder

        return WindowsInformationProtectionPoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DeviceAppManagementRequestBuilderGetQueryParameters():
        """
        Read properties and relationships of the deviceAppManagement object.
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
    class DeviceAppManagementRequestBuilderGetRequestConfiguration(RequestConfiguration[DeviceAppManagementRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DeviceAppManagementRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

