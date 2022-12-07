from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

domain_name_references_request_builder = lazy_import('msgraph.generated.domains.item.domain_name_references.domain_name_references_request_builder')
directory_object_item_request_builder = lazy_import('msgraph.generated.domains.item.domain_name_references.item.directory_object_item_request_builder')
federation_configuration_request_builder = lazy_import('msgraph.generated.domains.item.federation_configuration.federation_configuration_request_builder')
internal_domain_federation_item_request_builder = lazy_import('msgraph.generated.domains.item.federation_configuration.item.internal_domain_federation_item_request_builder')
force_delete_request_builder = lazy_import('msgraph.generated.domains.item.force_delete.force_delete_request_builder')
service_configuration_records_request_builder = lazy_import('msgraph.generated.domains.item.service_configuration_records.service_configuration_records_request_builder')
domain_dns_record_item_request_builder = lazy_import('msgraph.generated.domains.item.service_configuration_records.item.domain_dns_record_item_request_builder')
verification_dns_records_request_builder = lazy_import('msgraph.generated.domains.item.verification_dns_records.verification_dns_records_request_builder')
domain_dns_record_item_request_builder = lazy_import('msgraph.generated.domains.item.verification_dns_records.item.domain_dns_record_item_request_builder')
verify_request_builder = lazy_import('msgraph.generated.domains.item.verify.verify_request_builder')
domain = lazy_import('msgraph.generated.models.domain')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class DomainItemRequestBuilder():
    """
    Provides operations to manage the collection of domain entities.
    """
    def domain_name_references(self) -> domain_name_references_request_builder.DomainNameReferencesRequestBuilder:
        """
        Provides operations to manage the domainNameReferences property of the microsoft.graph.domain entity.
        """
        return domain_name_references_request_builder.DomainNameReferencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def federation_configuration(self) -> federation_configuration_request_builder.FederationConfigurationRequestBuilder:
        """
        Provides operations to manage the federationConfiguration property of the microsoft.graph.domain entity.
        """
        return federation_configuration_request_builder.FederationConfigurationRequestBuilder(self.request_adapter, self.path_parameters)
    
    def force_delete(self) -> force_delete_request_builder.ForceDeleteRequestBuilder:
        """
        Provides operations to call the forceDelete method.
        """
        return force_delete_request_builder.ForceDeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    def service_configuration_records(self) -> service_configuration_records_request_builder.ServiceConfigurationRecordsRequestBuilder:
        """
        Provides operations to manage the serviceConfigurationRecords property of the microsoft.graph.domain entity.
        """
        return service_configuration_records_request_builder.ServiceConfigurationRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def verification_dns_records(self) -> verification_dns_records_request_builder.VerificationDnsRecordsRequestBuilder:
        """
        Provides operations to manage the verificationDnsRecords property of the microsoft.graph.domain entity.
        """
        return verification_dns_records_request_builder.VerificationDnsRecordsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def verify(self) -> verify_request_builder.VerifyRequestBuilder:
        """
        Provides operations to call the verify method.
        """
        return verify_request_builder.VerifyRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new DomainItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/domains/{domain%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[DomainItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
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
    
    def create_get_request_information(self,request_configuration: Optional[DomainItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def create_patch_request_information(self,body: Optional[domain.Domain] = None, request_configuration: Optional[DomainItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of domain object.
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[DomainItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Deletes a domain from a tenant.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)
    
    def domain_name_references_by_id(self,id: str) -> directory_object_item_request_builder.DirectoryObjectItemRequestBuilder:
        """
        Provides operations to manage the domainNameReferences property of the microsoft.graph.domain entity.
        Args:
            id: Unique identifier of the item
        Returns: directory_object_item_request_builder.DirectoryObjectItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["directoryObject%2Did"] = id
        return directory_object_item_request_builder.DirectoryObjectItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def federation_configuration_by_id(self,id: str) -> internal_domain_federation_item_request_builder.InternalDomainFederationItemRequestBuilder:
        """
        Provides operations to manage the federationConfiguration property of the microsoft.graph.domain entity.
        Args:
            id: Unique identifier of the item
        Returns: internal_domain_federation_item_request_builder.InternalDomainFederationItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["internalDomainFederation%2Did"] = id
        return internal_domain_federation_item_request_builder.InternalDomainFederationItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[DomainItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[domain.Domain]:
        """
        Retrieve the properties and relationships of domain object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[domain.Domain]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, domain.Domain, response_handler, error_mapping)
    
    async def patch(self,body: Optional[domain.Domain] = None, request_configuration: Optional[DomainItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[domain.Domain]:
        """
        Update the properties of domain object.
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[domain.Domain]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, domain.Domain, response_handler, error_mapping)
    
    def service_configuration_records_by_id(self,id: str) -> domain_dns_record_item_request_builder.DomainDnsRecordItemRequestBuilder:
        """
        Provides operations to manage the serviceConfigurationRecords property of the microsoft.graph.domain entity.
        Args:
            id: Unique identifier of the item
        Returns: domain_dns_record_item_request_builder.DomainDnsRecordItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["domainDnsRecord%2Did"] = id
        return domain_dns_record_item_request_builder.DomainDnsRecordItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def verification_dns_records_by_id(self,id: str) -> domain_dns_record_item_request_builder.DomainDnsRecordItemRequestBuilder:
        """
        Provides operations to manage the verificationDnsRecords property of the microsoft.graph.domain entity.
        Args:
            id: Unique identifier of the item
        Returns: domain_dns_record_item_request_builder.DomainDnsRecordItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["domainDnsRecord%2Did"] = id
        return domain_dns_record_item_request_builder.DomainDnsRecordItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class DomainItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class DomainItemRequestBuilderGetQueryParameters():
        """
        Retrieve the properties and relationships of domain object.
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

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
        
    
    @dataclass
    class DomainItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

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
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

