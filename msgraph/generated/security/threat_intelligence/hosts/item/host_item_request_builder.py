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
    from .....models.o_data_errors.o_data_error import ODataError
    from .....models.security.host import Host
    from .child_host_pairs.child_host_pairs_request_builder import ChildHostPairsRequestBuilder
    from .components.components_request_builder import ComponentsRequestBuilder
    from .cookies.cookies_request_builder import CookiesRequestBuilder
    from .host_pairs.host_pairs_request_builder import HostPairsRequestBuilder
    from .parent_host_pairs.parent_host_pairs_request_builder import ParentHostPairsRequestBuilder
    from .passive_dns.passive_dns_request_builder import PassiveDnsRequestBuilder
    from .passive_dns_reverse.passive_dns_reverse_request_builder import PassiveDnsReverseRequestBuilder
    from .ports.ports_request_builder import PortsRequestBuilder
    from .reputation.reputation_request_builder import ReputationRequestBuilder
    from .ssl_certificates.ssl_certificates_request_builder import SslCertificatesRequestBuilder
    from .subdomains.subdomains_request_builder import SubdomainsRequestBuilder
    from .trackers.trackers_request_builder import TrackersRequestBuilder
    from .whois.whois_request_builder import WhoisRequestBuilder

class HostItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the hosts property of the microsoft.graph.security.threatIntelligence entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new HostItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/threatIntelligence/hosts/{host%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property hosts for security
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[HostItemRequestBuilderGetQueryParameters]] = None) -> Optional[Host]:
        """
        Read the properties and relationships of a host object. The host resource is the abstract base type that returns an implementation. A host can be of one of the following types:
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Host]
        Find more info here: https://learn.microsoft.com/graph/api/security-host-get?view=graph-rest-1.0
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
        from .....models.security.host import Host

        return await self.request_adapter.send_async(request_info, Host, error_mapping)
    
    async def patch(self,body: Host, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Host]:
        """
        Update the navigation property hosts in security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Host]
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
        from .....models.security.host import Host

        return await self.request_adapter.send_async(request_info, Host, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property hosts for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[HostItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read the properties and relationships of a host object. The host resource is the abstract base type that returns an implementation. A host can be of one of the following types:
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Host, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property hosts in security
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
    
    def with_url(self,raw_url: str) -> HostItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: HostItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return HostItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def child_host_pairs(self) -> ChildHostPairsRequestBuilder:
        """
        Provides operations to manage the childHostPairs property of the microsoft.graph.security.host entity.
        """
        from .child_host_pairs.child_host_pairs_request_builder import ChildHostPairsRequestBuilder

        return ChildHostPairsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def components(self) -> ComponentsRequestBuilder:
        """
        Provides operations to manage the components property of the microsoft.graph.security.host entity.
        """
        from .components.components_request_builder import ComponentsRequestBuilder

        return ComponentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cookies(self) -> CookiesRequestBuilder:
        """
        Provides operations to manage the cookies property of the microsoft.graph.security.host entity.
        """
        from .cookies.cookies_request_builder import CookiesRequestBuilder

        return CookiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def host_pairs(self) -> HostPairsRequestBuilder:
        """
        Provides operations to manage the hostPairs property of the microsoft.graph.security.host entity.
        """
        from .host_pairs.host_pairs_request_builder import HostPairsRequestBuilder

        return HostPairsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def parent_host_pairs(self) -> ParentHostPairsRequestBuilder:
        """
        Provides operations to manage the parentHostPairs property of the microsoft.graph.security.host entity.
        """
        from .parent_host_pairs.parent_host_pairs_request_builder import ParentHostPairsRequestBuilder

        return ParentHostPairsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def passive_dns(self) -> PassiveDnsRequestBuilder:
        """
        Provides operations to manage the passiveDns property of the microsoft.graph.security.host entity.
        """
        from .passive_dns.passive_dns_request_builder import PassiveDnsRequestBuilder

        return PassiveDnsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def passive_dns_reverse(self) -> PassiveDnsReverseRequestBuilder:
        """
        Provides operations to manage the passiveDnsReverse property of the microsoft.graph.security.host entity.
        """
        from .passive_dns_reverse.passive_dns_reverse_request_builder import PassiveDnsReverseRequestBuilder

        return PassiveDnsReverseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ports(self) -> PortsRequestBuilder:
        """
        Provides operations to manage the ports property of the microsoft.graph.security.host entity.
        """
        from .ports.ports_request_builder import PortsRequestBuilder

        return PortsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reputation(self) -> ReputationRequestBuilder:
        """
        Provides operations to manage the reputation property of the microsoft.graph.security.host entity.
        """
        from .reputation.reputation_request_builder import ReputationRequestBuilder

        return ReputationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ssl_certificates(self) -> SslCertificatesRequestBuilder:
        """
        Provides operations to manage the sslCertificates property of the microsoft.graph.security.host entity.
        """
        from .ssl_certificates.ssl_certificates_request_builder import SslCertificatesRequestBuilder

        return SslCertificatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subdomains(self) -> SubdomainsRequestBuilder:
        """
        Provides operations to manage the subdomains property of the microsoft.graph.security.host entity.
        """
        from .subdomains.subdomains_request_builder import SubdomainsRequestBuilder

        return SubdomainsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trackers(self) -> TrackersRequestBuilder:
        """
        Provides operations to manage the trackers property of the microsoft.graph.security.host entity.
        """
        from .trackers.trackers_request_builder import TrackersRequestBuilder

        return TrackersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def whois(self) -> WhoisRequestBuilder:
        """
        Provides operations to manage the whois property of the microsoft.graph.security.host entity.
        """
        from .whois.whois_request_builder import WhoisRequestBuilder

        return WhoisRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class HostItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class HostItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of a host object. The host resource is the abstract base type that returns an implementation. A host can be of one of the following types:
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
    class HostItemRequestBuilderGetRequestConfiguration(RequestConfiguration[HostItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class HostItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

