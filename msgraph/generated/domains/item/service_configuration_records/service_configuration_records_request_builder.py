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
    from ....models.domain_dns_record import DomainDnsRecord
    from ....models.domain_dns_record_collection_response import DomainDnsRecordCollectionResponse
    from ....models.o_data_errors.o_data_error import ODataError
    from .count.count_request_builder import CountRequestBuilder
    from .item.domain_dns_record_item_request_builder import DomainDnsRecordItemRequestBuilder

class ServiceConfigurationRecordsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the serviceConfigurationRecords property of the microsoft.graph.domain entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ServiceConfigurationRecordsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/domains/{domain%2Did}/serviceConfigurationRecords{?%24count,%24expand,%24filter,%24orderby,%24search,%24select,%24skip,%24top}", path_parameters)
    
    def by_domain_dns_record_id(self,domain_dns_record_id: str) -> DomainDnsRecordItemRequestBuilder:
        """
        Provides operations to manage the serviceConfigurationRecords property of the microsoft.graph.domain entity.
        param domain_dns_record_id: The unique identifier of domainDnsRecord
        Returns: DomainDnsRecordItemRequestBuilder
        """
        if domain_dns_record_id is None:
            raise TypeError("domain_dns_record_id cannot be null.")
        from .item.domain_dns_record_item_request_builder import DomainDnsRecordItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["domainDnsRecord%2Did"] = domain_dns_record_id
        return DomainDnsRecordItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ServiceConfigurationRecordsRequestBuilderGetQueryParameters]] = None) -> Optional[DomainDnsRecordCollectionResponse]:
        """
        Retrieves a list of domainDnsRecord objects needed to enable services for the domain. Use the returned list to add records to the zone file of the domain. This can be done through the domain registrar or DNS server configuration.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DomainDnsRecordCollectionResponse]
        Find more info here: https://learn.microsoft.com/graph/api/domain-list-serviceconfigurationrecords?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.domain_dns_record_collection_response import DomainDnsRecordCollectionResponse

        return await self.request_adapter.send_async(request_info, DomainDnsRecordCollectionResponse, error_mapping)
    
    async def post(self,body: DomainDnsRecord, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DomainDnsRecord]:
        """
        Create new navigation property to serviceConfigurationRecords for domains
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DomainDnsRecord]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.domain_dns_record import DomainDnsRecord

        return await self.request_adapter.send_async(request_info, DomainDnsRecord, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ServiceConfigurationRecordsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieves a list of domainDnsRecord objects needed to enable services for the domain. Use the returned list to add records to the zone file of the domain. This can be done through the domain registrar or DNS server configuration.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: DomainDnsRecord, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create new navigation property to serviceConfigurationRecords for domains
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> ServiceConfigurationRecordsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ServiceConfigurationRecordsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ServiceConfigurationRecordsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def count(self) -> CountRequestBuilder:
        """
        Provides operations to count the resources in the collection.
        """
        from .count.count_request_builder import CountRequestBuilder

        return CountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ServiceConfigurationRecordsRequestBuilderGetQueryParameters():
        """
        Retrieves a list of domainDnsRecord objects needed to enable services for the domain. Use the returned list to add records to the zone file of the domain. This can be done through the domain registrar or DNS server configuration.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
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

    
    @dataclass
    class ServiceConfigurationRecordsRequestBuilderGetRequestConfiguration(RequestConfiguration[ServiceConfigurationRecordsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ServiceConfigurationRecordsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

