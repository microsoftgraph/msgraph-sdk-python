from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models import site
    from ...models.o_data_errors import o_data_error
    from .analytics import analytics_request_builder
    from .columns import columns_request_builder
    from .content_types import content_types_request_builder
    from .drive import drive_request_builder
    from .drives import drives_request_builder
    from .external_columns import external_columns_request_builder
    from .get_activities_by_interval import get_activities_by_interval_request_builder
    from .get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval import get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder
    from .get_applicable_content_types_for_list_with_list_id import get_applicable_content_types_for_list_with_list_id_request_builder
    from .get_by_path_with_path import get_by_path_with_path_request_builder
    from .items import items_request_builder
    from .lists import lists_request_builder
    from .onenote import onenote_request_builder
    from .operations import operations_request_builder
    from .permissions import permissions_request_builder
    from .sites import sites_request_builder
    from .term_store import term_store_request_builder
    from .term_stores import term_stores_request_builder

class SiteItemRequestBuilder():
    """
    Provides operations to manage the collection of site entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new SiteItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/sites/{site%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[SiteItemRequestBuilderGetRequestConfiguration] = None) -> Optional[site.Site]:
        """
        Retrieve properties and relationships for a [site][] resource.A **site** resource represents a team site in SharePoint.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[site.Site]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import site

        return await self.request_adapter.send_async(request_info, site.Site, error_mapping)
    
    def get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval(self,end_date_time: Optional[str] = None, interval: Optional[str] = None, start_date_time: Optional[str] = None) -> get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder.GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder:
        """
        Provides operations to call the getActivitiesByInterval method.
        Args:
            endDateTime: Usage: endDateTime='{endDateTime}'
            interval: Usage: interval='{interval}'
            startDateTime: Usage: startDateTime='{startDateTime}'
        Returns: get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder.GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder
        """
        if end_date_time is None:
            raise Exception("end_date_time cannot be undefined")
        if interval is None:
            raise Exception("interval cannot be undefined")
        if start_date_time is None:
            raise Exception("start_date_time cannot be undefined")
        from .get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval import get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder

        return get_activities_by_interval_with_start_date_time_with_end_date_time_with_interval_request_builder.GetActivitiesByIntervalWithStartDateTimeWithEndDateTimeWithIntervalRequestBuilder(self.request_adapter, self.path_parameters, end_date_time, interval, start_date_time)
    
    def get_applicable_content_types_for_list_with_list_id(self,list_id: Optional[str] = None) -> get_applicable_content_types_for_list_with_list_id_request_builder.GetApplicableContentTypesForListWithListIdRequestBuilder:
        """
        Provides operations to call the getApplicableContentTypesForList method.
        Args:
            listId: Usage: listId='{listId}'
        Returns: get_applicable_content_types_for_list_with_list_id_request_builder.GetApplicableContentTypesForListWithListIdRequestBuilder
        """
        if list_id is None:
            raise Exception("list_id cannot be undefined")
        from .get_applicable_content_types_for_list_with_list_id import get_applicable_content_types_for_list_with_list_id_request_builder

        return get_applicable_content_types_for_list_with_list_id_request_builder.GetApplicableContentTypesForListWithListIdRequestBuilder(self.request_adapter, self.path_parameters, list_id)
    
    def get_by_path_with_path(self,path: Optional[str] = None) -> get_by_path_with_path_request_builder.GetByPathWithPathRequestBuilder:
        """
        Provides operations to call the getByPath method.
        Args:
            path: Usage: path='{path}'
        Returns: get_by_path_with_path_request_builder.GetByPathWithPathRequestBuilder
        """
        if path is None:
            raise Exception("path cannot be undefined")
        from .get_by_path_with_path import get_by_path_with_path_request_builder

        return get_by_path_with_path_request_builder.GetByPathWithPathRequestBuilder(self.request_adapter, self.path_parameters, path)
    
    async def patch(self,body: Optional[site.Site] = None, request_configuration: Optional[SiteItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[site.Site]:
        """
        Update entity in sites
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[site.Site]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import site

        return await self.request_adapter.send_async(request_info, site.Site, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[SiteItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve properties and relationships for a [site][] resource.A **site** resource represents a team site in SharePoint.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[site.Site] = None, request_configuration: Optional[SiteItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update entity in sites
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def analytics(self) -> analytics_request_builder.AnalyticsRequestBuilder:
        """
        Provides operations to manage the analytics property of the microsoft.graph.site entity.
        """
        from .analytics import analytics_request_builder

        return analytics_request_builder.AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def columns(self) -> columns_request_builder.ColumnsRequestBuilder:
        """
        Provides operations to manage the columns property of the microsoft.graph.site entity.
        """
        from .columns import columns_request_builder

        return columns_request_builder.ColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def content_types(self) -> content_types_request_builder.ContentTypesRequestBuilder:
        """
        Provides operations to manage the contentTypes property of the microsoft.graph.site entity.
        """
        from .content_types import content_types_request_builder

        return content_types_request_builder.ContentTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drive(self) -> drive_request_builder.DriveRequestBuilder:
        """
        Provides operations to manage the drive property of the microsoft.graph.site entity.
        """
        from .drive import drive_request_builder

        return drive_request_builder.DriveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def drives(self) -> drives_request_builder.DrivesRequestBuilder:
        """
        Provides operations to manage the drives property of the microsoft.graph.site entity.
        """
        from .drives import drives_request_builder

        return drives_request_builder.DrivesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def external_columns(self) -> external_columns_request_builder.ExternalColumnsRequestBuilder:
        """
        Provides operations to manage the externalColumns property of the microsoft.graph.site entity.
        """
        from .external_columns import external_columns_request_builder

        return external_columns_request_builder.ExternalColumnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_activities_by_interval(self) -> get_activities_by_interval_request_builder.GetActivitiesByIntervalRequestBuilder:
        """
        Provides operations to call the getActivitiesByInterval method.
        """
        from .get_activities_by_interval import get_activities_by_interval_request_builder

        return get_activities_by_interval_request_builder.GetActivitiesByIntervalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def items(self) -> items_request_builder.ItemsRequestBuilder:
        """
        Provides operations to manage the items property of the microsoft.graph.site entity.
        """
        from .items import items_request_builder

        return items_request_builder.ItemsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lists(self) -> lists_request_builder.ListsRequestBuilder:
        """
        Provides operations to manage the lists property of the microsoft.graph.site entity.
        """
        from .lists import lists_request_builder

        return lists_request_builder.ListsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def onenote(self) -> onenote_request_builder.OnenoteRequestBuilder:
        """
        Provides operations to manage the onenote property of the microsoft.graph.site entity.
        """
        from .onenote import onenote_request_builder

        return onenote_request_builder.OnenoteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def operations(self) -> operations_request_builder.OperationsRequestBuilder:
        """
        Provides operations to manage the operations property of the microsoft.graph.site entity.
        """
        from .operations import operations_request_builder

        return operations_request_builder.OperationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def permissions(self) -> permissions_request_builder.PermissionsRequestBuilder:
        """
        Provides operations to manage the permissions property of the microsoft.graph.site entity.
        """
        from .permissions import permissions_request_builder

        return permissions_request_builder.PermissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sites(self) -> sites_request_builder.SitesRequestBuilder:
        """
        Provides operations to manage the sites property of the microsoft.graph.site entity.
        """
        from .sites import sites_request_builder

        return sites_request_builder.SitesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def term_store(self) -> term_store_request_builder.TermStoreRequestBuilder:
        """
        Provides operations to manage the termStore property of the microsoft.graph.site entity.
        """
        from .term_store import term_store_request_builder

        return term_store_request_builder.TermStoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def term_stores(self) -> term_stores_request_builder.TermStoresRequestBuilder:
        """
        Provides operations to manage the termStores property of the microsoft.graph.site entity.
        """
        from .term_stores import term_stores_request_builder

        return term_stores_request_builder.TermStoresRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SiteItemRequestBuilderGetQueryParameters():
        """
        Retrieve properties and relationships for a [site][] resource.A **site** resource represents a team site in SharePoint.
        """
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class SiteItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[SiteItemRequestBuilder.SiteItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class SiteItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

