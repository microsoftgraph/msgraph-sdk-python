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
    from ...models.o_data_errors.o_data_error import ODataError
    from ...models.site import Site
    from .analytics.analytics_request_builder import AnalyticsRequestBuilder
    from .columns.columns_request_builder import ColumnsRequestBuilder
    from .content_types.content_types_request_builder import ContentTypesRequestBuilder
    from .created_by_user.created_by_user_request_builder import CreatedByUserRequestBuilder
    from .drive.drive_request_builder import DriveRequestBuilder
    from .drives.drives_request_builder import DrivesRequestBuilder
    from .external_columns.external_columns_request_builder import ExternalColumnsRequestBuilder
    from .get_activities_by_interval.get_activities_by_interval_request_builder import GetActivitiesByIntervalRequestBuilder
    from .get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval.get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder import GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder
    from .get_applicable_content_types_for_list_with_list_id.get_applicable_content_types_for_list_with_list_id_request_builder import GetApplicableContentTypesForListWithListIdRequestBuilder
    from .get_by_path_with_path.get_by_path_with_path_request_builder import GetByPathWithPathRequestBuilder
    from .items.items_request_builder import ItemsRequestBuilder
    from .last_modified_by_user.last_modified_by_user_request_builder import LastModifiedByUserRequestBuilder
    from .lists.lists_request_builder import ListsRequestBuilder
    from .onenote.onenote_request_builder import OnenoteRequestBuilder
    from .operations.operations_request_builder import OperationsRequestBuilder
    from .pages.pages_request_builder import PagesRequestBuilder
    from .permissions.permissions_request_builder import PermissionsRequestBuilder
    from .sites.sites_request_builder import SitesRequestBuilder
    from .term_store.term_store_request_builder import TermStoreRequestBuilder
    from .term_stores.term_stores_request_builder import TermStoresRequestBuilder

class SiteItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of site entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SiteItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/sites/{site%2Did}{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SiteItemRequestBuilderGetQueryParameters]] = None) -> Optional[Site]:
        """
        Retrieve properties and relationships for a site resource.A site resource represents a team site in SharePoint.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Site]
        Find more info here: https://learn.microsoft.com/graph/api/site-get?view=graph-rest-1.0
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
        from ...models.site import Site

        return await self.request_adapter.send_async(request_info, Site, error_mapping)
    
    def get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval(self,end_date_time: str, interval: str, start_date_time: str) -> GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder:
        """
        Provides operations to call the getActivitiesByInterval method.
        param end_date_time: Usage: endDateTime='{endDateTime}'
        param interval: Usage: interval='{interval}'
        param start_date_time: Usage: startDateTime='{startDateTime}'
        Returns: GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder
        """
        if end_date_time is None:
            raise TypeError("end_date_time cannot be null.")
        if interval is None:
            raise TypeError("interval cannot be null.")
        if start_date_time is None:
            raise TypeError("start_date_time cannot be null.")
        from .get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval.get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder import GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder

        return GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, interval, start_date_time)
    
    def get_applicable_content_types_for_list_with_list_id(self,list_id: str) -> GetApplicableContentTypesForListWithListIdRequestBuilder:
        """
        Provides operations to call the getApplicableContentTypesForList method.
        param list_id: Usage: listId='{listId}'
        Returns: GetApplicableContentTypesForListWithListIdRequestBuilder
        """
        if list_id is None:
            raise TypeError("list_id cannot be null.")
        from .get_applicable_content_types_for_list_with_list_id.get_applicable_content_types_for_list_with_list_id_request_builder import GetApplicableContentTypesForListWithListIdRequestBuilder

        return GetApplicableContentTypesForListWithListIdRequestBuilder(self.request_adapter, self.path_parameters, list_id)
    
    def get_by_path_with_path(self,path: str) -> GetByPathWithPathRequestBuilder:
        """
        Provides operations to call the getByPath method.
        param path: Usage: path='{path}'
        Returns: GetByPathWithPathRequestBuilder
        """
        if path is None:
            raise TypeError("path cannot be null.")
        from .get_by_path_with_path.get_by_path_with_path_request_builder import GetByPathWithPathRequestBuilder

        return GetByPathWithPathRequestBuilder(self.request_adapter, self.path_parameters, path)
    
    async def patch(self,body: Site, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Site]:
        """
        Update entity in sites
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Site]
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
        from ...models.site import Site

        return await self.request_adapter.send_async(request_info, Site, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SiteItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve properties and relationships for a site resource.A site resource represents a team site in SharePoint.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Site, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update entity in sites
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
    
    def with_url(self,raw_url: str) -> SiteItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SiteItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SiteItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def analytics(self) -> AnalyticsRequestBuilder:
        """
        Provides operations to manage the analytics property of the microsoft.graph.site entity.
        """
        from .analytics.analytics_request_builder import AnalyticsRequestBuilder

        return AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def columns(self) -> ColumnsRequestBuilder:
        """
        Provides operations to manage the columns property of the microsoft.graph.site entity.
        """
        from .columns.columns_request_builder import ColumnsRequestBuilder

        return ColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def content_types(self) -> ContentTypesRequestBuilder:
        """
        Provides operations to manage the contentTypes property of the microsoft.graph.site entity.
        """
        from .content_types.content_types_request_builder import ContentTypesRequestBuilder

        return ContentTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def created_by_user(self) -> CreatedByUserRequestBuilder:
        """
        Provides operations to manage the createdByUser property of the microsoft.graph.baseItem entity.
        """
        from .created_by_user.created_by_user_request_builder import CreatedByUserRequestBuilder

        return CreatedByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive(self) -> DriveRequestBuilder:
        """
        Provides operations to manage the drive property of the microsoft.graph.site entity.
        """
        from .drive.drive_request_builder import DriveRequestBuilder

        return DriveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drives(self) -> DrivesRequestBuilder:
        """
        Provides operations to manage the drives property of the microsoft.graph.site entity.
        """
        from .drives.drives_request_builder import DrivesRequestBuilder

        return DrivesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def external_columns(self) -> ExternalColumnsRequestBuilder:
        """
        Provides operations to manage the externalColumns property of the microsoft.graph.site entity.
        """
        from .external_columns.external_columns_request_builder import ExternalColumnsRequestBuilder

        return ExternalColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_activities_by_interval(self) -> GetActivitiesByIntervalRequestBuilder:
        """
        Provides operations to call the getActivitiesByInterval method.
        """
        from .get_activities_by_interval.get_activities_by_interval_request_builder import GetActivitiesByIntervalRequestBuilder

        return GetActivitiesByIntervalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def items(self) -> ItemsRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.site entity.
        """
        from .items.items_request_builder import ItemsRequestBuilder

        return ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last_modified_by_user(self) -> LastModifiedByUserRequestBuilder:
        """
        Provides operations to manage the lastModifiedByUser property of the microsoft.graph.baseItem entity.
        """
        from .last_modified_by_user.last_modified_by_user_request_builder import LastModifiedByUserRequestBuilder

        return LastModifiedByUserRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lists(self) -> ListsRequestBuilder:
        """
        Provides operations to manage the lists property of the microsoft.graph.site entity.
        """
        from .lists.lists_request_builder import ListsRequestBuilder

        return ListsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def onenote(self) -> OnenoteRequestBuilder:
        """
        Provides operations to manage the onenote property of the microsoft.graph.site entity.
        """
        from .onenote.onenote_request_builder import OnenoteRequestBuilder

        return OnenoteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.site entity.
        """
        from .operations.operations_request_builder import OperationsRequestBuilder

        return OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pages(self) -> PagesRequestBuilder:
        """
        Provides operations to manage the pages property of the microsoft.graph.site entity.
        """
        from .pages.pages_request_builder import PagesRequestBuilder

        return PagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permissions(self) -> PermissionsRequestBuilder:
        """
        Provides operations to manage the permissions property of the microsoft.graph.site entity.
        """
        from .permissions.permissions_request_builder import PermissionsRequestBuilder

        return PermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sites(self) -> SitesRequestBuilder:
        """
        Provides operations to manage the sites property of the microsoft.graph.site entity.
        """
        from .sites.sites_request_builder import SitesRequestBuilder

        return SitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def term_store(self) -> TermStoreRequestBuilder:
        """
        Provides operations to manage the termStore property of the microsoft.graph.site entity.
        """
        from .term_store.term_store_request_builder import TermStoreRequestBuilder

        return TermStoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def term_stores(self) -> TermStoresRequestBuilder:
        """
        Provides operations to manage the termStores property of the microsoft.graph.site entity.
        """
        from .term_stores.term_stores_request_builder import TermStoresRequestBuilder

        return TermStoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SiteItemRequestBuilderGetQueryParameters():
        """
        Retrieve properties and relationships for a site resource.A site resource represents a team site in SharePoint.
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
    class SiteItemRequestBuilderGetRequestConfiguration(RequestConfiguration[SiteItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SiteItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

