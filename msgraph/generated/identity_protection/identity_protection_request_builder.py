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

risk_detections_request_builder = lazy_import('msgraph.generated.identity_protection.risk_detections.risk_detections_request_builder')
risk_detection_item_request_builder = lazy_import('msgraph.generated.identity_protection.risk_detections.item.risk_detection_item_request_builder')
risky_service_principals_request_builder = lazy_import('msgraph.generated.identity_protection.risky_service_principals.risky_service_principals_request_builder')
risky_service_principal_item_request_builder = lazy_import('msgraph.generated.identity_protection.risky_service_principals.item.risky_service_principal_item_request_builder')
risky_users_request_builder = lazy_import('msgraph.generated.identity_protection.risky_users.risky_users_request_builder')
risky_user_item_request_builder = lazy_import('msgraph.generated.identity_protection.risky_users.item.risky_user_item_request_builder')
service_principal_risk_detections_request_builder = lazy_import('msgraph.generated.identity_protection.service_principal_risk_detections.service_principal_risk_detections_request_builder')
service_principal_risk_detection_item_request_builder = lazy_import('msgraph.generated.identity_protection.service_principal_risk_detections.item.service_principal_risk_detection_item_request_builder')
identity_protection_root = lazy_import('msgraph.generated.models.identity_protection_root')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')

class IdentityProtectionRequestBuilder():
    """
    Provides operations to manage the identityProtectionRoot singleton.
    """
    @property
    def risk_detections(self) -> risk_detections_request_builder.RiskDetectionsRequestBuilder:
        """
        Provides operations to manage the riskDetections property of the microsoft.graph.identityProtectionRoot entity.
        """
        return risk_detections_request_builder.RiskDetectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def risky_service_principals(self) -> risky_service_principals_request_builder.RiskyServicePrincipalsRequestBuilder:
        """
        Provides operations to manage the riskyServicePrincipals property of the microsoft.graph.identityProtectionRoot entity.
        """
        return risky_service_principals_request_builder.RiskyServicePrincipalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def risky_users(self) -> risky_users_request_builder.RiskyUsersRequestBuilder:
        """
        Provides operations to manage the riskyUsers property of the microsoft.graph.identityProtectionRoot entity.
        """
        return risky_users_request_builder.RiskyUsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_principal_risk_detections(self) -> service_principal_risk_detections_request_builder.ServicePrincipalRiskDetectionsRequestBuilder:
        """
        Provides operations to manage the servicePrincipalRiskDetections property of the microsoft.graph.identityProtectionRoot entity.
        """
        return service_principal_risk_detections_request_builder.ServicePrincipalRiskDetectionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new IdentityProtectionRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identityProtection{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[IdentityProtectionRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get identityProtection
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
    
    def create_patch_request_information(self,body: Optional[identity_protection_root.IdentityProtectionRoot] = None, request_configuration: Optional[IdentityProtectionRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update identityProtection
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
    
    async def get(self,request_configuration: Optional[IdentityProtectionRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[identity_protection_root.IdentityProtectionRoot]:
        """
        Get identityProtection
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[identity_protection_root.IdentityProtectionRoot]
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
        return await self.request_adapter.send_async(request_info, identity_protection_root.IdentityProtectionRoot, response_handler, error_mapping)
    
    async def patch(self,body: Optional[identity_protection_root.IdentityProtectionRoot] = None, request_configuration: Optional[IdentityProtectionRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[identity_protection_root.IdentityProtectionRoot]:
        """
        Update identityProtection
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[identity_protection_root.IdentityProtectionRoot]
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
        return await self.request_adapter.send_async(request_info, identity_protection_root.IdentityProtectionRoot, response_handler, error_mapping)
    
    def risk_detections_by_id(self,id: str) -> risk_detection_item_request_builder.RiskDetectionItemRequestBuilder:
        """
        Provides operations to manage the riskDetections property of the microsoft.graph.identityProtectionRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: risk_detection_item_request_builder.RiskDetectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["riskDetection%2Did"] = id
        return risk_detection_item_request_builder.RiskDetectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def risky_service_principals_by_id(self,id: str) -> risky_service_principal_item_request_builder.RiskyServicePrincipalItemRequestBuilder:
        """
        Provides operations to manage the riskyServicePrincipals property of the microsoft.graph.identityProtectionRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: risky_service_principal_item_request_builder.RiskyServicePrincipalItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["riskyServicePrincipal%2Did"] = id
        return risky_service_principal_item_request_builder.RiskyServicePrincipalItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def risky_users_by_id(self,id: str) -> risky_user_item_request_builder.RiskyUserItemRequestBuilder:
        """
        Provides operations to manage the riskyUsers property of the microsoft.graph.identityProtectionRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: risky_user_item_request_builder.RiskyUserItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["riskyUser%2Did"] = id
        return risky_user_item_request_builder.RiskyUserItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    def service_principal_risk_detections_by_id(self,id: str) -> service_principal_risk_detection_item_request_builder.ServicePrincipalRiskDetectionItemRequestBuilder:
        """
        Provides operations to manage the servicePrincipalRiskDetections property of the microsoft.graph.identityProtectionRoot entity.
        Args:
            id: Unique identifier of the item
        Returns: service_principal_risk_detection_item_request_builder.ServicePrincipalRiskDetectionItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["servicePrincipalRiskDetection%2Did"] = id
        return service_principal_risk_detection_item_request_builder.ServicePrincipalRiskDetectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @dataclass
    class IdentityProtectionRequestBuilderGetQueryParameters():
        """
        Get identityProtection
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
    class IdentityProtectionRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[IdentityProtectionRequestBuilder.IdentityProtectionRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class IdentityProtectionRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

