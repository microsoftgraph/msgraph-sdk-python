from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..models.identity_protection_root import IdentityProtectionRoot
    from ..models.o_data_errors.o_data_error import ODataError
    from .risky_service_principals.risky_service_principals_request_builder import RiskyServicePrincipalsRequestBuilder
    from .risky_users.risky_users_request_builder import RiskyUsersRequestBuilder
    from .risk_detections.risk_detections_request_builder import RiskDetectionsRequestBuilder
    from .service_principal_risk_detections.service_principal_risk_detections_request_builder import ServicePrincipalRiskDetectionsRequestBuilder

class IdentityProtectionRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the identityProtectionRoot singleton.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new IdentityProtectionRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityProtection{?%24select,%24expand}", path_parameters)
    
    async def get(self,request_configuration: Optional[IdentityProtectionRequestBuilderGetRequestConfiguration] = None) -> Optional[IdentityProtectionRoot]:
        """
        Get identityProtection
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IdentityProtectionRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.identity_protection_root import IdentityProtectionRoot

        return await self.request_adapter.send_async(request_info, IdentityProtectionRoot, error_mapping)
    
    async def patch(self,body: Optional[IdentityProtectionRoot] = None, request_configuration: Optional[IdentityProtectionRequestBuilderPatchRequestConfiguration] = None) -> Optional[IdentityProtectionRoot]:
        """
        Update identityProtection
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[IdentityProtectionRoot]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ..models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.identity_protection_root import IdentityProtectionRoot

        return await self.request_adapter.send_async(request_info, IdentityProtectionRoot, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[IdentityProtectionRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get identityProtection
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[IdentityProtectionRoot] = None, request_configuration: Optional[IdentityProtectionRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update identityProtection
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> IdentityProtectionRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IdentityProtectionRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return IdentityProtectionRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def risk_detections(self) -> RiskDetectionsRequestBuilder:
        """
        Provides operations to manage the riskDetections property of the microsoft.graph.identityProtectionRoot entity.
        """
        from .risk_detections.risk_detections_request_builder import RiskDetectionsRequestBuilder

        return RiskDetectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def risky_service_principals(self) -> RiskyServicePrincipalsRequestBuilder:
        """
        Provides operations to manage the riskyServicePrincipals property of the microsoft.graph.identityProtectionRoot entity.
        """
        from .risky_service_principals.risky_service_principals_request_builder import RiskyServicePrincipalsRequestBuilder

        return RiskyServicePrincipalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def risky_users(self) -> RiskyUsersRequestBuilder:
        """
        Provides operations to manage the riskyUsers property of the microsoft.graph.identityProtectionRoot entity.
        """
        from .risky_users.risky_users_request_builder import RiskyUsersRequestBuilder

        return RiskyUsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_principal_risk_detections(self) -> ServicePrincipalRiskDetectionsRequestBuilder:
        """
        Provides operations to manage the servicePrincipalRiskDetections property of the microsoft.graph.identityProtectionRoot entity.
        """
        from .service_principal_risk_detections.service_principal_risk_detections_request_builder import ServicePrincipalRiskDetectionsRequestBuilder

        return ServicePrincipalRiskDetectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class IdentityProtectionRequestBuilderGetQueryParameters():
        """
        Get identityProtection
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
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

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class IdentityProtectionRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[IdentityProtectionRequestBuilder.IdentityProtectionRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class IdentityProtectionRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

