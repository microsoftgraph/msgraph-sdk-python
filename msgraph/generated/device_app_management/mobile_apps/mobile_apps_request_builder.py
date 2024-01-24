from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.mobile_app import MobileApp
    from ...models.mobile_app_collection_response import MobileAppCollectionResponse
    from ...models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .graph_android_lob_app.graph_android_lob_app_request_builder import GraphAndroidLobAppRequestBuilder
    from .graph_android_store_app.graph_android_store_app_request_builder import GraphAndroidStoreAppRequestBuilder
    from .graph_ios_lob_app.graph_ios_lob_app_request_builder import GraphIosLobAppRequestBuilder
    from .graph_ios_store_app.graph_ios_store_app_request_builder import GraphIosStoreAppRequestBuilder
    from .graph_ios_vpp_app.graph_ios_vpp_app_request_builder import GraphIosVppAppRequestBuilder
    from .graph_mac_o_s_dmg_app.graph_mac_o_s_dmg_app_request_builder import GraphMacOSDmgAppRequestBuilder
    from .graph_mac_o_s_lob_app.graph_mac_o_s_lob_app_request_builder import GraphMacOSLobAppRequestBuilder
    from .graph_managed_android_lob_app.graph_managed_android_lob_app_request_builder import GraphManagedAndroidLobAppRequestBuilder
    from .graph_managed_i_o_s_lob_app.graph_managed_i_o_s_lob_app_request_builder import GraphManagedIOSLobAppRequestBuilder
    from .graph_managed_mobile_lob_app.graph_managed_mobile_lob_app_request_builder import GraphManagedMobileLobAppRequestBuilder
    from .graph_microsoft_store_for_business_app.graph_microsoft_store_for_business_app_request_builder import GraphMicrosoftStoreForBusinessAppRequestBuilder
    from .graph_win32_lob_app.graph_win32_lob_app_request_builder import GraphWin32LobAppRequestBuilder
    from .graph_windows_app_x.graph_windows_app_x_request_builder import GraphWindowsAppXRequestBuilder
    from .graph_windows_mobile_m_s_i.graph_windows_mobile_m_s_i_request_builder import GraphWindowsMobileMSIRequestBuilder
    from .graph_windows_universal_app_x.graph_windows_universal_app_x_request_builder import GraphWindowsUniversalAppXRequestBuilder
    from .graph_windows_web_app.graph_windows_web_app_request_builder import GraphWindowsWebAppRequestBuilder
    from .item.mobile_app_item_request_builder import MobileAppItemRequestBuilder

class MobileAppsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the mobileApps property of the microsoft.graph.deviceAppManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new MobileAppsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/mobileApps{?%24top,%24skip,%24search,%24filter,%24count,%24orderby,%24select,%24expand}", path_parameters)
    
    def by_mobile_app_id(self,mobile_app_id: str) -> MobileAppItemRequestBuilder:
        """
        Provides operations to manage the mobileApps property of the microsoft.graph.deviceAppManagement entity.
        param mobile_app_id: The unique identifier of mobileApp
        Returns: MobileAppItemRequestBuilder
        """
        if not mobile_app_id:
            raise TypeError("mobile_app_id cannot be null.")
        from .item.mobile_app_item_request_builder import MobileAppItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mobileApp%2Did"] = mobile_app_id
        return MobileAppItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[MobileAppsRequestBuilderGetRequestConfiguration] = None) -> Optional[MobileAppCollectionResponse]:
        """
        List properties and relationships of the macOSLobApp objects.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MobileAppCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/intune-apps-macoslobapp-list?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.mobile_app_collection_response import MobileAppCollectionResponse

        return await self.request_adapter.send_async(request_info, MobileAppCollectionResponse, error_mapping)
    
    async def post(self,body: Optional[MobileApp] = None, request_configuration: Optional[MobileAppsRequestBuilderPostRequestConfiguration] = None) -> Optional[MobileApp]:
        """
        Create a new macOSMicrosoftEdgeApp object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[MobileApp]
        Find more info here: https://learn.microsoft.com/graph/api/intune-apps-macosmicrosoftedgeapp-create?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.mobile_app import MobileApp

        return await self.request_adapter.send_async(request_info, MobileApp, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[MobileAppsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        List properties and relationships of the macOSLobApp objects.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: Optional[MobileApp] = None, request_configuration: Optional[MobileAppsRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Create a new macOSMicrosoftEdgeApp object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> MobileAppsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MobileAppsRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return MobileAppsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_android_lob_app(self) -> GraphAndroidLobAppRequestBuilder:
        """
        Casts the previous resource to androidLobApp.
        """
        from .graph_android_lob_app.graph_android_lob_app_request_builder import GraphAndroidLobAppRequestBuilder

        return GraphAndroidLobAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_android_store_app(self) -> GraphAndroidStoreAppRequestBuilder:
        """
        Casts the previous resource to androidStoreApp.
        """
        from .graph_android_store_app.graph_android_store_app_request_builder import GraphAndroidStoreAppRequestBuilder

        return GraphAndroidStoreAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_ios_lob_app(self) -> GraphIosLobAppRequestBuilder:
        """
        Casts the previous resource to iosLobApp.
        """
        from .graph_ios_lob_app.graph_ios_lob_app_request_builder import GraphIosLobAppRequestBuilder

        return GraphIosLobAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_ios_store_app(self) -> GraphIosStoreAppRequestBuilder:
        """
        Casts the previous resource to iosStoreApp.
        """
        from .graph_ios_store_app.graph_ios_store_app_request_builder import GraphIosStoreAppRequestBuilder

        return GraphIosStoreAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_ios_vpp_app(self) -> GraphIosVppAppRequestBuilder:
        """
        Casts the previous resource to iosVppApp.
        """
        from .graph_ios_vpp_app.graph_ios_vpp_app_request_builder import GraphIosVppAppRequestBuilder

        return GraphIosVppAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_mac_o_s_dmg_app(self) -> GraphMacOSDmgAppRequestBuilder:
        """
        Casts the previous resource to macOSDmgApp.
        """
        from .graph_mac_o_s_dmg_app.graph_mac_o_s_dmg_app_request_builder import GraphMacOSDmgAppRequestBuilder

        return GraphMacOSDmgAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_mac_o_s_lob_app(self) -> GraphMacOSLobAppRequestBuilder:
        """
        Casts the previous resource to macOSLobApp.
        """
        from .graph_mac_o_s_lob_app.graph_mac_o_s_lob_app_request_builder import GraphMacOSLobAppRequestBuilder

        return GraphMacOSLobAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_managed_android_lob_app(self) -> GraphManagedAndroidLobAppRequestBuilder:
        """
        Casts the previous resource to managedAndroidLobApp.
        """
        from .graph_managed_android_lob_app.graph_managed_android_lob_app_request_builder import GraphManagedAndroidLobAppRequestBuilder

        return GraphManagedAndroidLobAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_managed_i_o_s_lob_app(self) -> GraphManagedIOSLobAppRequestBuilder:
        """
        Casts the previous resource to managedIOSLobApp.
        """
        from .graph_managed_i_o_s_lob_app.graph_managed_i_o_s_lob_app_request_builder import GraphManagedIOSLobAppRequestBuilder

        return GraphManagedIOSLobAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_managed_mobile_lob_app(self) -> GraphManagedMobileLobAppRequestBuilder:
        """
        Casts the previous resource to managedMobileLobApp.
        """
        from .graph_managed_mobile_lob_app.graph_managed_mobile_lob_app_request_builder import GraphManagedMobileLobAppRequestBuilder

        return GraphManagedMobileLobAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_microsoft_store_for_business_app(self) -> GraphMicrosoftStoreForBusinessAppRequestBuilder:
        """
        Casts the previous resource to microsoftStoreForBusinessApp.
        """
        from .graph_microsoft_store_for_business_app.graph_microsoft_store_for_business_app_request_builder import GraphMicrosoftStoreForBusinessAppRequestBuilder

        return GraphMicrosoftStoreForBusinessAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_win32_lob_app(self) -> GraphWin32LobAppRequestBuilder:
        """
        Casts the previous resource to win32LobApp.
        """
        from .graph_win32_lob_app.graph_win32_lob_app_request_builder import GraphWin32LobAppRequestBuilder

        return GraphWin32LobAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_windows_app_x(self) -> GraphWindowsAppXRequestBuilder:
        """
        Casts the previous resource to windowsAppX.
        """
        from .graph_windows_app_x.graph_windows_app_x_request_builder import GraphWindowsAppXRequestBuilder

        return GraphWindowsAppXRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_windows_mobile_m_s_i(self) -> GraphWindowsMobileMSIRequestBuilder:
        """
        Casts the previous resource to windowsMobileMSI.
        """
        from .graph_windows_mobile_m_s_i.graph_windows_mobile_m_s_i_request_builder import GraphWindowsMobileMSIRequestBuilder

        return GraphWindowsMobileMSIRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_windows_universal_app_x(self) -> GraphWindowsUniversalAppXRequestBuilder:
        """
        Casts the previous resource to windowsUniversalAppX.
        """
        from .graph_windows_universal_app_x.graph_windows_universal_app_x_request_builder import GraphWindowsUniversalAppXRequestBuilder

        return GraphWindowsUniversalAppXRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def graph_windows_web_app(self) -> GraphWindowsWebAppRequestBuilder:
        """
        Casts the previous resource to windowsWebApp.
        """
        from .graph_windows_web_app.graph_windows_web_app_request_builder import GraphWindowsWebAppRequestBuilder

        return GraphWindowsWebAppRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class MobileAppsRequestBuilderGetQueryParameters():
        """
        List properties and relationships of the macOSLobApp objects.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "expand":
                return "%24expand"
            if original_name == "filter":
                return "%24filter"
            if original_name == "orderby":
                return "%24orderby"
            if original_name == "search":
                return "%24search"
            if original_name == "select":
                return "%24select"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Expand related entities
        expand: Optional[List[str]] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Order items by property values
        orderby: Optional[List[str]] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class MobileAppsRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[MobileAppsRequestBuilder.MobileAppsRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class MobileAppsRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

