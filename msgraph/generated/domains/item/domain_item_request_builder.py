from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models import domain
    from ...models.o_data_errors import o_data_error
    from .domain_name_references import domain_name_references_request_builder
    from .federation_configuration import federation_configuration_request_builder
    from .force_delete import force_delete_request_builder
    from .promote import promote_request_builder
    from .service_configuration_records import service_configuration_records_request_builder
    from .verification_dns_records import verification_dns_records_request_builder
    from .verify import verify_request_builder

class DomainItemRequestBuilder():
    """
    Provides operations to manage the collection of domain entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DomainItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/domains/{domain%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[DomainItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Deletes a domain from a tenant.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[DomainItemRequestBuilderGetRequestConfiguration] = None) -> Optional[domain.Domain]:
        """
        Retrieve the properties and relationships of domain object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[domain.Domain]
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
        from ...models import domain

        return await self.request_adapter.send_async(request_info, domain.Domain, error_mapping)
    
    async def patch(self,body: Optional[domain.Domain] = None, request_configuration: Optional[DomainItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[domain.Domain]:
        """
        Update the properties of domain object.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[domain.Domain]
        """
        if not body:
            raise TypeError("body cannot be null.")
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
        from ...models import domain

        return await self.request_adapter.send_async(request_info, domain.Domain, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[DomainItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Deletes a domain from a tenant.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[DomainItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the properties and relationships of domain object.
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
    
    def to_patch_request_information(self,body: Optional[domain.Domain] = None, request_configuration: Optional[DomainItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of domain object.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
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
    def domain_name_references(self) -> domain_name_references_request_builder.DomainNameReferencesRequestBuilder:
        """
        Provides operations to manage the domainNameReferences property of the microsoft.graph.domain entity.
        """
        from .domain_name_references import domain_name_references_request_builder

        return domain_name_references_request_builder.DomainNameReferencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def federation_configuration(self) -> federation_configuration_request_builder.FederationConfigurationRequestBuilder:
        """
        Provides operations to manage the federationConfiguration property of the microsoft.graph.domain entity.
        """
        from .federation_configuration import federation_configuration_request_builder

        return federation_configuration_request_builder.FederationConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def force_delete(self) -> force_delete_request_builder.ForceDeleteRequestBuilder:
        """
        Provides operations to call the forceDelete method.
        """
        from .force_delete import force_delete_request_builder

        return force_delete_request_builder.ForceDeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def promote(self) -> promote_request_builder.PromoteRequestBuilder:
        """
        Provides operations to call the promote method.
        """
        from .promote import promote_request_builder

        return promote_request_builder.PromoteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_configuration_records(self) -> service_configuration_records_request_builder.ServiceConfigurationRecordsRequestBuilder:
        """
        Provides operations to manage the serviceConfigurationRecords property of the microsoft.graph.domain entity.
        """
        from .service_configuration_records import service_configuration_records_request_builder

        return service_configuration_records_request_builder.ServiceConfigurationRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def verification_dns_records(self) -> verification_dns_records_request_builder.VerificationDnsRecordsRequestBuilder:
        """
        Provides operations to manage the verificationDnsRecords property of the microsoft.graph.domain entity.
        """
        from .verification_dns_records import verification_dns_records_request_builder

        return verification_dns_records_request_builder.VerificationDnsRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def verify(self) -> verify_request_builder.VerifyRequestBuilder:
        """
        Provides operations to call the verify method.
        """
        from .verify import verify_request_builder

        return verify_request_builder.VerifyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DomainItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DomainItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of domain object.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
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

    
    @dataclass
    class DomainItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[DomainItemRequestBuilder.DomainItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class DomainItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

