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
    from .....models.android_lob_app import AndroidLobApp
    from .....models.o_data_errors.o_data_error import ODataError
    from .assignments.assignments_request_builder import AssignmentsRequestBuilder
    from .categories.categories_request_builder import CategoriesRequestBuilder
    from .content_versions.content_versions_request_builder import ContentVersionsRequestBuilder

class GraphAndroidLobAppRequestBuilder(BaseRequestBuilder):
    """
    Casts the previous resource to androidLobApp.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new GraphAndroidLobAppRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceAppManagement/mobileApps/{mobileApp%2Did}/graph.androidLobApp{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[GraphAndroidLobAppRequestBuilderGetRequestConfiguration] = None) -> Optional[AndroidLobApp]:
        """
        Get the item of type microsoft.graph.mobileApp as microsoft.graph.androidLobApp
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AndroidLobApp]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.android_lob_app import AndroidLobApp

        return await self.request_adapter.send_async(request_info, AndroidLobApp, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[GraphAndroidLobAppRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the item of type microsoft.graph.mobileApp as microsoft.graph.androidLobApp
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
    
    def with_url(self,raw_url: Optional[str] = None) -> GraphAndroidLobAppRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GraphAndroidLobAppRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return GraphAndroidLobAppRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def assignments(self) -> AssignmentsRequestBuilder:
        """
        Provides operations to manage the assignments property of the microsoft.graph.mobileApp entity.
        """
        from .assignments.assignments_request_builder import AssignmentsRequestBuilder

        return AssignmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def categories(self) -> CategoriesRequestBuilder:
        """
        Provides operations to manage the categories property of the microsoft.graph.mobileApp entity.
        """
        from .categories.categories_request_builder import CategoriesRequestBuilder

        return CategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def content_versions(self) -> ContentVersionsRequestBuilder:
        """
        Provides operations to manage the contentVersions property of the microsoft.graph.mobileLobApp entity.
        """
        from .content_versions.content_versions_request_builder import ContentVersionsRequestBuilder

        return ContentVersionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class GraphAndroidLobAppRequestBuilderGetQueryParameters():
        """
        Get the item of type microsoft.graph.mobileApp as microsoft.graph.androidLobApp
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
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
    class GraphAndroidLobAppRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[GraphAndroidLobAppRequestBuilder.GraphAndroidLobAppRequestBuilderGetQueryParameters] = None

    

