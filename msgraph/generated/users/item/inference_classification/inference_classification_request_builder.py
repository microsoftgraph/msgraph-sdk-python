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
    from ....models.inference_classification import InferenceClassification
    from ....models.o_data_errors.o_data_error import ODataError
    from .overrides.overrides_request_builder import OverridesRequestBuilder

class InferenceClassificationRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the inferenceClassification property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new InferenceClassificationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/inferenceClassification{?%24expand,%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[InferenceClassificationRequestBuilderGetQueryParameters]] = None) -> Optional[InferenceClassification]:
        """
        Relevance classification of the user's messages based on explicit designations that override inferred relevance or importance.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InferenceClassification]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.inference_classification import InferenceClassification

        return await self.request_adapter.send_async(request_info, InferenceClassification, error_mapping)
    
    async def patch(self,body: InferenceClassification, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[InferenceClassification]:
        """
        Update the navigation property inferenceClassification in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InferenceClassification]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.inference_classification import InferenceClassification

        return await self.request_adapter.send_async(request_info, InferenceClassification, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[InferenceClassificationRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Relevance classification of the user's messages based on explicit designations that override inferred relevance or importance.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: InferenceClassification, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the navigation property inferenceClassification in users
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
    
    def with_url(self,raw_url: str) -> InferenceClassificationRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: InferenceClassificationRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return InferenceClassificationRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def overrides(self) -> OverridesRequestBuilder:
        """
        Provides operations to manage the overrides property of the microsoft.graph.inferenceClassification entity.
        """
        from .overrides.overrides_request_builder import OverridesRequestBuilder

        return OverridesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class InferenceClassificationRequestBuilderGetQueryParameters():
        """
        Relevance classification of the user's messages based on explicit designations that override inferred relevance or importance.
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
    class InferenceClassificationRequestBuilderGetRequestConfiguration(RequestConfiguration[InferenceClassificationRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class InferenceClassificationRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

