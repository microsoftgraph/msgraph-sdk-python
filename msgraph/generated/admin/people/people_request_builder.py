from __future__ import annotations
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
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.people_admin_settings import PeopleAdminSettings
    from .item_insights.item_insights_request_builder import ItemInsightsRequestBuilder
    from .profile_card_properties.profile_card_properties_request_builder import ProfileCardPropertiesRequestBuilder
    from .pronouns.pronouns_request_builder import PronounsRequestBuilder

class PeopleRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the people property of the microsoft.graph.admin entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PeopleRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/admin/people{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PeopleRequestBuilderGetQueryParameters]] = None) -> Optional[PeopleAdminSettings]:
        """
        Retrieve the properties and relationships of a peopleAdminSettings object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PeopleAdminSettings]
        Find more info here: https://learn.microsoft.com/graph/api/peopleadminsettings-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.people_admin_settings import PeopleAdminSettings

        return await self.request_adapter.send_async(request_info, PeopleAdminSettings, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PeopleRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of a peopleAdminSettings object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> PeopleRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PeopleRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PeopleRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def item_insights(self) -> ItemInsightsRequestBuilder:
        """
        Provides operations to manage the itemInsights property of the microsoft.graph.peopleAdminSettings entity.
        """
        from .item_insights.item_insights_request_builder import ItemInsightsRequestBuilder

        return ItemInsightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def profile_card_properties(self) -> ProfileCardPropertiesRequestBuilder:
        """
        Provides operations to manage the profileCardProperties property of the microsoft.graph.peopleAdminSettings entity.
        """
        from .profile_card_properties.profile_card_properties_request_builder import ProfileCardPropertiesRequestBuilder

        return ProfileCardPropertiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pronouns(self) -> PronounsRequestBuilder:
        """
        Provides operations to manage the pronouns property of the microsoft.graph.peopleAdminSettings entity.
        """
        from .pronouns.pronouns_request_builder import PronounsRequestBuilder

        return PronounsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PeopleRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of a peopleAdminSettings object.
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
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class PeopleRequestBuilderGetRequestConfiguration(RequestConfiguration[PeopleRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

