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
    from ....models.inference_classification import InferenceClassification
    from ....models.o_data_errors.o_data_error import ODataError
    from .overrides.overrides_request_builder import OverridesRequestBuilder

class InferenceClassificationRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the inferenceClassification property of the microsoft.graph.user entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new InferenceClassificationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/users/{user%2Did}/inferenceClassification{?%24select}", path_parameters)
    
    async def get(self,request_configuration: Optional[InferenceClassificationRequestBuilderGetRequestConfiguration] = None) -> Optional[InferenceClassification]:
        """
        Relevance classification of the user's messages based on explicit designations that override inferred relevance or importance.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InferenceClassification]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.inference_classification import InferenceClassification

        return await self.request_adapter.send_async(request_info, InferenceClassification, error_mapping)
    
    async def patch(self,body: Optional[InferenceClassification] = None, request_configuration: Optional[InferenceClassificationRequestBuilderPatchRequestConfiguration] = None) -> Optional[InferenceClassification]:
        """
        Update the navigation property inferenceClassification in users
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[InferenceClassification]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.inference_classification import InferenceClassification

        return await self.request_adapter.send_async(request_info, InferenceClassification, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[InferenceClassificationRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Relevance classification of the user's messages based on explicit designations that override inferred relevance or importance.
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
    
    def to_patch_request_information(self,body: Optional[InferenceClassification] = None, request_configuration: Optional[InferenceClassificationRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property inferenceClassification in users
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
    
    def with_url(self,raw_url: Optional[str] = None) -> InferenceClassificationRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: InferenceClassificationRequestBuilder
        """
        if not raw_url:
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
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class InferenceClassificationRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[InferenceClassificationRequestBuilder.InferenceClassificationRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class InferenceClassificationRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

