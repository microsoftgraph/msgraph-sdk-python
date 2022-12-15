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

agreement_acceptances_request_builder = lazy_import('msgraph.generated.identity_governance.terms_of_use.agreement_acceptances.agreement_acceptances_request_builder')
agreement_acceptance_item_request_builder = lazy_import('msgraph.generated.identity_governance.terms_of_use.agreement_acceptances.item.agreement_acceptance_item_request_builder')
agreements_request_builder = lazy_import('msgraph.generated.identity_governance.terms_of_use.agreements.agreements_request_builder')
agreement_item_request_builder = lazy_import('msgraph.generated.identity_governance.terms_of_use.agreements.item.agreement_item_request_builder')
terms_of_use_container = lazy_import('msgraph.generated.models.terms_of_use_container')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class TermsOfUseRequestBuilder():
    """
    Provides operations to manage the termsOfUse property of the microsoft.graph.identityGovernance entity.
    """
    @property
    def agreement_acceptances(self) -> agreement_acceptances_request_builder.AgreementAcceptancesRequestBuilder:
        """
        Provides operations to manage the agreementAcceptances property of the microsoft.graph.termsOfUseContainer entity.
        """
        return agreement_acceptances_request_builder.AgreementAcceptancesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def agreements(self) -> agreements_request_builder.AgreementsRequestBuilder:
        """
        Provides operations to manage the agreements property of the microsoft.graph.termsOfUseContainer entity.
        """
        return agreements_request_builder.AgreementsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def agreement_acceptances_by_id(self,id: str) -> agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder:
        """
        Provides operations to manage the agreementAcceptances property of the microsoft.graph.termsOfUseContainer entity.
        Args:
            id: Unique identifier of the item
        Returns: agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agreementAcceptance%2Did"] = id
        return agreement_acceptance_item_request_builder.AgreementAcceptanceItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def agreements_by_id(self,id: str) -> agreement_item_request_builder.AgreementItemRequestBuilder:
        """
        Provides operations to manage the agreements property of the microsoft.graph.termsOfUseContainer entity.
        Args:
            id: Unique identifier of the item
        Returns: agreement_item_request_builder.AgreementItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["agreement%2Did"] = id
        return agreement_item_request_builder.AgreementItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new TermsOfUseRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityGovernance/termsOfUse{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_delete_request_information(self,request_configuration: Optional[TermsOfUseRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property termsOfUse for identityGovernance
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
    
    def create_get_request_information(self,request_configuration: Optional[TermsOfUseRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get termsOfUse from identityGovernance
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
    
    def create_patch_request_information(self,body: Optional[terms_of_use_container.TermsOfUseContainer] = None, request_configuration: Optional[TermsOfUseRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property termsOfUse in identityGovernance
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
        request_info.headers["Accept"] = "application/json"
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    async def delete(self,request_configuration: Optional[TermsOfUseRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property termsOfUse for identityGovernance
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
    
    async def get(self,request_configuration: Optional[TermsOfUseRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[terms_of_use_container.TermsOfUseContainer]:
        """
        Get termsOfUse from identityGovernance
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[terms_of_use_container.TermsOfUseContainer]
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
        return await self.request_adapter.send_async(request_info, terms_of_use_container.TermsOfUseContainer, response_handler, error_mapping)
    
    async def patch(self,body: Optional[terms_of_use_container.TermsOfUseContainer] = None, request_configuration: Optional[TermsOfUseRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[terms_of_use_container.TermsOfUseContainer]:
        """
        Update the navigation property termsOfUse in identityGovernance
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[terms_of_use_container.TermsOfUseContainer]
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
        return await self.request_adapter.send_async(request_info, terms_of_use_container.TermsOfUseContainer, response_handler, error_mapping)
    
    @dataclass
    class TermsOfUseRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class TermsOfUseRequestBuilderGetQueryParameters():
        """
        Get termsOfUse from identityGovernance
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
    class TermsOfUseRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[TermsOfUseRequestBuilder.TermsOfUseRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class TermsOfUseRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

