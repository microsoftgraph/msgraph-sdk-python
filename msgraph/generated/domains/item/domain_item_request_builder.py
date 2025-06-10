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
    from ...models.domain import Domain
    from ...models.o_data_errors.o_data_error import ODataError
    from .domain_name_references.domain_name_references_request_builder import DomainNameReferencesRequestBuilder
    from .federation_configuration.federation_configuration_request_builder import FederationConfigurationRequestBuilder
    from .force_delete.force_delete_request_builder import ForceDeleteRequestBuilder
    from .promote.promote_request_builder import PromoteRequestBuilder
    from .root_domain.root_domain_request_builder import RootDomainRequestBuilder
    from .service_configuration_records.service_configuration_records_request_builder import ServiceConfigurationRecordsRequestBuilder
    from .verification_dns_records.verification_dns_records_request_builder import VerificationDnsRecordsRequestBuilder
    from .verify.verify_request_builder import VerifyRequestBuilder

class DomainItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of domain entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DomainItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/domains/{domain%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete a domain from a tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/domain-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DomainItemRequestBuilderGetQueryParameters]] = None) -> Optional[Domain]:
        """
        Retrieve the properties and relationships of domain object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Domain]
        Find more info here: https://learn.microsoft.com/graph/api/domain-get?view=graph-rest-1.0
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
        from ...models.domain import Domain

        return await self.request_adapter.send_async(request_info, Domain, error_mapping)
    
    async def patch(self,body: Domain, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Domain]:
        """
        Update the properties of domain object. Only verified domains can be updated.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Domain]
        Find more info here: https://learn.microsoft.com/graph/api/domain-update?view=graph-rest-1.0
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
        from ...models.domain import Domain

        return await self.request_adapter.send_async(request_info, Domain, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete a domain from a tenant.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DomainItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of domain object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Domain, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of domain object. Only verified domains can be updated.
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
    
    def with_url(self,raw_url: str) -> DomainItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DomainItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DomainItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def domain_name_references(self) -> DomainNameReferencesRequestBuilder:
        """
        Provides operations to manage the domainNameReferences property of the microsoft.graph.domain entity.
        """
        from .domain_name_references.domain_name_references_request_builder import DomainNameReferencesRequestBuilder

        return DomainNameReferencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def federation_configuration(self) -> FederationConfigurationRequestBuilder:
        """
        Provides operations to manage the federationConfiguration property of the microsoft.graph.domain entity.
        """
        from .federation_configuration.federation_configuration_request_builder import FederationConfigurationRequestBuilder

        return FederationConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def force_delete(self) -> ForceDeleteRequestBuilder:
        """
        Provides operations to call the forceDelete method.
        """
        from .force_delete.force_delete_request_builder import ForceDeleteRequestBuilder

        return ForceDeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def promote(self) -> PromoteRequestBuilder:
        """
        Provides operations to call the promote method.
        """
        from .promote.promote_request_builder import PromoteRequestBuilder

        return PromoteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def root_domain(self) -> RootDomainRequestBuilder:
        """
        Provides operations to manage the rootDomain property of the microsoft.graph.domain entity.
        """
        from .root_domain.root_domain_request_builder import RootDomainRequestBuilder

        return RootDomainRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_configuration_records(self) -> ServiceConfigurationRecordsRequestBuilder:
        """
        Provides operations to manage the serviceConfigurationRecords property of the microsoft.graph.domain entity.
        """
        from .service_configuration_records.service_configuration_records_request_builder import ServiceConfigurationRecordsRequestBuilder

        return ServiceConfigurationRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def verification_dns_records(self) -> VerificationDnsRecordsRequestBuilder:
        """
        Provides operations to manage the verificationDnsRecords property of the microsoft.graph.domain entity.
        """
        from .verification_dns_records.verification_dns_records_request_builder import VerificationDnsRecordsRequestBuilder

        return VerificationDnsRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def verify(self) -> VerifyRequestBuilder:
        """
        Provides operations to call the verify method.
        """
        from .verify.verify_request_builder import VerifyRequestBuilder

        return VerifyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DomainItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DomainItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of domain object.
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
    class DomainItemRequestBuilderGetRequestConfiguration(RequestConfiguration[DomainItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DomainItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

