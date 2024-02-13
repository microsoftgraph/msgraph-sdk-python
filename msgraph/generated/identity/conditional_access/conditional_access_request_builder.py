from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.conditional_access_root import ConditionalAccessRoot
    from ...models.o_data_errors.o_data_error import ODataError
    from .authentication_context_class_references.authentication_context_class_references_request_builder import AuthenticationContextClassReferencesRequestBuilder
    from .authentication_strength.authentication_strength_request_builder import AuthenticationStrengthRequestBuilder
    from .named_locations.named_locations_request_builder import NamedLocationsRequestBuilder
    from .policies.policies_request_builder import PoliciesRequestBuilder
    from .templates.templates_request_builder import TemplatesRequestBuilder

class ConditionalAccessRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the conditionalAccess property of the microsoft.graph.identityContainer entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ConditionalAccessRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identity/conditionalAccess{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration] = None) -> None:
        """
        Delete navigation property conditionalAccess for identity
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration] = None) -> Optional[ConditionalAccessRoot]:
        """
        the entry point for the Conditional Access (CA) object model.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConditionalAccessRoot]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.conditional_access_root import ConditionalAccessRoot

        return await self.request_adapter.send_async(request_info, ConditionalAccessRoot, error_mapping)
    
    async def patch(self,body: Optional[ConditionalAccessRoot] = None, request_configuration: Optional[RequestConfiguration] = None) -> Optional[ConditionalAccessRoot]:
        """
        Update the navigation property conditionalAccess in identity
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ConditionalAccessRoot]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.conditional_access_root import ConditionalAccessRoot

        return await self.request_adapter.send_async(request_info, ConditionalAccessRoot, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property conditionalAccess for identity
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/identity/conditionalAccess', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        the entry point for the Conditional Access (CA) object model.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[ConditionalAccessRoot] = None, request_configuration: Optional[RequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property conditionalAccess in identity
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, '{+baseurl}/identity/conditionalAccess', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> ConditionalAccessRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ConditionalAccessRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return ConditionalAccessRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def authentication_context_class_references(self) -> AuthenticationContextClassReferencesRequestBuilder:
        """
        Provides operations to manage the authenticationContextClassReferences property of the microsoft.graph.conditionalAccessRoot entity.
        """
        from .authentication_context_class_references.authentication_context_class_references_request_builder import AuthenticationContextClassReferencesRequestBuilder

        return AuthenticationContextClassReferencesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def authentication_strength(self) -> AuthenticationStrengthRequestBuilder:
        """
        Provides operations to manage the authenticationStrength property of the microsoft.graph.conditionalAccessRoot entity.
        """
        from .authentication_strength.authentication_strength_request_builder import AuthenticationStrengthRequestBuilder

        return AuthenticationStrengthRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def named_locations(self) -> NamedLocationsRequestBuilder:
        """
        Provides operations to manage the namedLocations property of the microsoft.graph.conditionalAccessRoot entity.
        """
        from .named_locations.named_locations_request_builder import NamedLocationsRequestBuilder

        return NamedLocationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def policies(self) -> PoliciesRequestBuilder:
        """
        Provides operations to manage the policies property of the microsoft.graph.conditionalAccessRoot entity.
        """
        from .policies.policies_request_builder import PoliciesRequestBuilder

        return PoliciesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def templates(self) -> TemplatesRequestBuilder:
        """
        Provides operations to manage the templates property of the microsoft.graph.conditionalAccessRoot entity.
        """
        from .templates.templates_request_builder import TemplatesRequestBuilder

        return TemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ConditionalAccessRequestBuilderGetQueryParameters():
        """
        the entry point for the Conditional Access (CA) object model.
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

    

