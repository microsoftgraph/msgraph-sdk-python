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
    from ..models.identity_governance.identity_governance import IdentityGovernance
    from ..models.o_data_errors.o_data_error import ODataError
    from .access_reviews.access_reviews_request_builder import AccessReviewsRequestBuilder
    from .app_consent.app_consent_request_builder import AppConsentRequestBuilder
    from .entitlement_management.entitlement_management_request_builder import EntitlementManagementRequestBuilder
    from .lifecycle_workflows.lifecycle_workflows_request_builder import LifecycleWorkflowsRequestBuilder
    from .privileged_access.privileged_access_request_builder import PrivilegedAccessRequestBuilder
    from .terms_of_use.terms_of_use_request_builder import TermsOfUseRequestBuilder

class IdentityGovernanceRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the identityGovernance singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IdentityGovernanceRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[IdentityGovernanceRequestBuilderGetQueryParameters]] = None) -> Optional[IdentityGovernance]:
        """
        Get identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IdentityGovernance]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.identity_governance.identity_governance import IdentityGovernance

        return await self.request_adapter.send_async(request_info, IdentityGovernance, error_mapping)
    
    async def patch(self,body: IdentityGovernance, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[IdentityGovernance]:
        """
        Update identityGovernance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IdentityGovernance]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.identity_governance.identity_governance import IdentityGovernance

        return await self.request_adapter.send_async(request_info, IdentityGovernance, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[IdentityGovernanceRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: IdentityGovernance, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update identityGovernance
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
    
    def with_url(self,raw_url: str) -> IdentityGovernanceRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IdentityGovernanceRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return IdentityGovernanceRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def access_reviews(self) -> AccessReviewsRequestBuilder:
        """
        Provides operations to manage the accessReviews property of the microsoft.graph.identityGovernance entity.
        """
        from .access_reviews.access_reviews_request_builder import AccessReviewsRequestBuilder

        return AccessReviewsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def app_consent(self) -> AppConsentRequestBuilder:
        """
        Provides operations to manage the appConsent property of the microsoft.graph.identityGovernance entity.
        """
        from .app_consent.app_consent_request_builder import AppConsentRequestBuilder

        return AppConsentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def entitlement_management(self) -> EntitlementManagementRequestBuilder:
        """
        Provides operations to manage the entitlementManagement property of the microsoft.graph.identityGovernance entity.
        """
        from .entitlement_management.entitlement_management_request_builder import EntitlementManagementRequestBuilder

        return EntitlementManagementRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lifecycle_workflows(self) -> LifecycleWorkflowsRequestBuilder:
        """
        Provides operations to manage the lifecycleWorkflows property of the microsoft.graph.identityGovernance entity.
        """
        from .lifecycle_workflows.lifecycle_workflows_request_builder import LifecycleWorkflowsRequestBuilder

        return LifecycleWorkflowsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privileged_access(self) -> PrivilegedAccessRequestBuilder:
        """
        Provides operations to manage the privilegedAccess property of the microsoft.graph.identityGovernance entity.
        """
        from .privileged_access.privileged_access_request_builder import PrivilegedAccessRequestBuilder

        return PrivilegedAccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def terms_of_use(self) -> TermsOfUseRequestBuilder:
        """
        Provides operations to manage the termsOfUse property of the microsoft.graph.identityGovernance entity.
        """
        from .terms_of_use.terms_of_use_request_builder import TermsOfUseRequestBuilder

        return TermsOfUseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class IdentityGovernanceRequestBuilderGetQueryParameters():
        """
        Get identityGovernance
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
    class IdentityGovernanceRequestBuilderGetRequestConfiguration(RequestConfiguration[IdentityGovernanceRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class IdentityGovernanceRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

