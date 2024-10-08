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
    from ...models.security.threat_intelligence import ThreatIntelligence
    from .articles.articles_request_builder import ArticlesRequestBuilder
    from .article_indicators.article_indicators_request_builder import ArticleIndicatorsRequestBuilder
    from .hosts.hosts_request_builder import HostsRequestBuilder
    from .host_components.host_components_request_builder import HostComponentsRequestBuilder
    from .host_cookies.host_cookies_request_builder import HostCookiesRequestBuilder
    from .host_pairs.host_pairs_request_builder import HostPairsRequestBuilder
    from .host_ports.host_ports_request_builder import HostPortsRequestBuilder
    from .host_ssl_certificates.host_ssl_certificates_request_builder import HostSslCertificatesRequestBuilder
    from .host_trackers.host_trackers_request_builder import HostTrackersRequestBuilder
    from .intelligence_profile_indicators.intelligence_profile_indicators_request_builder import IntelligenceProfileIndicatorsRequestBuilder
    from .intel_profiles.intel_profiles_request_builder import IntelProfilesRequestBuilder
    from .passive_dns_records.passive_dns_records_request_builder import PassiveDnsRecordsRequestBuilder
    from .ssl_certificates.ssl_certificates_request_builder import SslCertificatesRequestBuilder
    from .subdomains.subdomains_request_builder import SubdomainsRequestBuilder
    from .vulnerabilities.vulnerabilities_request_builder import VulnerabilitiesRequestBuilder
    from .whois_history_records.whois_history_records_request_builder import WhoisHistoryRecordsRequestBuilder
    from .whois_records.whois_records_request_builder import WhoisRecordsRequestBuilder

class ThreatIntelligenceRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the threatIntelligence property of the microsoft.graph.security entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ThreatIntelligenceRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/security/threatIntelligence{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete navigation property threatIntelligence for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ThreatIntelligenceRequestBuilderGetQueryParameters]] = None) -> Optional[ThreatIntelligence]:
        """
        Get threatIntelligence from security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ThreatIntelligence]
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
        from ...models.security.threat_intelligence import ThreatIntelligence

        return await self.request_adapter.send_async(request_info, ThreatIntelligence, error_mapping)
    
    async def patch(self,body: ThreatIntelligence, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ThreatIntelligence]:
        """
        Update the navigation property threatIntelligence in security
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ThreatIntelligence]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.security.threat_intelligence import ThreatIntelligence

        return await self.request_adapter.send_async(request_info, ThreatIntelligence, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete navigation property threatIntelligence for security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ThreatIntelligenceRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get threatIntelligence from security
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: ThreatIntelligence, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property threatIntelligence in security
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
    
    def with_url(self,raw_url: str) -> ThreatIntelligenceRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ThreatIntelligenceRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ThreatIntelligenceRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def article_indicators(self) -> ArticleIndicatorsRequestBuilder:
        """
        Provides operations to manage the articleIndicators property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .article_indicators.article_indicators_request_builder import ArticleIndicatorsRequestBuilder

        return ArticleIndicatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def articles(self) -> ArticlesRequestBuilder:
        """
        Provides operations to manage the articles property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .articles.articles_request_builder import ArticlesRequestBuilder

        return ArticlesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def host_components(self) -> HostComponentsRequestBuilder:
        """
        Provides operations to manage the hostComponents property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .host_components.host_components_request_builder import HostComponentsRequestBuilder

        return HostComponentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def host_cookies(self) -> HostCookiesRequestBuilder:
        """
        Provides operations to manage the hostCookies property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .host_cookies.host_cookies_request_builder import HostCookiesRequestBuilder

        return HostCookiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def host_pairs(self) -> HostPairsRequestBuilder:
        """
        Provides operations to manage the hostPairs property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .host_pairs.host_pairs_request_builder import HostPairsRequestBuilder

        return HostPairsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def host_ports(self) -> HostPortsRequestBuilder:
        """
        Provides operations to manage the hostPorts property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .host_ports.host_ports_request_builder import HostPortsRequestBuilder

        return HostPortsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def host_ssl_certificates(self) -> HostSslCertificatesRequestBuilder:
        """
        Provides operations to manage the hostSslCertificates property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .host_ssl_certificates.host_ssl_certificates_request_builder import HostSslCertificatesRequestBuilder

        return HostSslCertificatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def host_trackers(self) -> HostTrackersRequestBuilder:
        """
        Provides operations to manage the hostTrackers property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .host_trackers.host_trackers_request_builder import HostTrackersRequestBuilder

        return HostTrackersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def hosts(self) -> HostsRequestBuilder:
        """
        Provides operations to manage the hosts property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .hosts.hosts_request_builder import HostsRequestBuilder

        return HostsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def intel_profiles(self) -> IntelProfilesRequestBuilder:
        """
        Provides operations to manage the intelProfiles property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .intel_profiles.intel_profiles_request_builder import IntelProfilesRequestBuilder

        return IntelProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def intelligence_profile_indicators(self) -> IntelligenceProfileIndicatorsRequestBuilder:
        """
        Provides operations to manage the intelligenceProfileIndicators property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .intelligence_profile_indicators.intelligence_profile_indicators_request_builder import IntelligenceProfileIndicatorsRequestBuilder

        return IntelligenceProfileIndicatorsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def passive_dns_records(self) -> PassiveDnsRecordsRequestBuilder:
        """
        Provides operations to manage the passiveDnsRecords property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .passive_dns_records.passive_dns_records_request_builder import PassiveDnsRecordsRequestBuilder

        return PassiveDnsRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ssl_certificates(self) -> SslCertificatesRequestBuilder:
        """
        Provides operations to manage the sslCertificates property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .ssl_certificates.ssl_certificates_request_builder import SslCertificatesRequestBuilder

        return SslCertificatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subdomains(self) -> SubdomainsRequestBuilder:
        """
        Provides operations to manage the subdomains property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .subdomains.subdomains_request_builder import SubdomainsRequestBuilder

        return SubdomainsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vulnerabilities(self) -> VulnerabilitiesRequestBuilder:
        """
        Provides operations to manage the vulnerabilities property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .vulnerabilities.vulnerabilities_request_builder import VulnerabilitiesRequestBuilder

        return VulnerabilitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def whois_history_records(self) -> WhoisHistoryRecordsRequestBuilder:
        """
        Provides operations to manage the whoisHistoryRecords property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .whois_history_records.whois_history_records_request_builder import WhoisHistoryRecordsRequestBuilder

        return WhoisHistoryRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def whois_records(self) -> WhoisRecordsRequestBuilder:
        """
        Provides operations to manage the whoisRecords property of the microsoft.graph.security.threatIntelligence entity.
        """
        from .whois_records.whois_records_request_builder import WhoisRecordsRequestBuilder

        return WhoisRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ThreatIntelligenceRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ThreatIntelligenceRequestBuilderGetQueryParameters():
        """
        Get threatIntelligence from security
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
    class ThreatIntelligenceRequestBuilderGetRequestConfiguration(RequestConfiguration[ThreatIntelligenceRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ThreatIntelligenceRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

