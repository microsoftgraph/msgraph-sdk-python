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

inference_classification = lazy_import('msgraph.generated.models.inference_classification')
o_data_error = lazy_import('msgraph.generated.models.o_data_errors.o_data_error')
overrides_request_builder = lazy_import('msgraph.generated.users.item.inference_classification.overrides.overrides_request_builder')
inference_classification_override_item_request_builder = lazy_import('msgraph.generated.users.item.inference_classification.overrides.item.inference_classification_override_item_request_builder')

class InferenceClassificationRequestBuilder():
    """
    Provides operations to manage the inferenceClassification property of the microsoft.graph.user entity.
    """
    @property
    def overrides(self) -> overrides_request_builder.OverridesRequestBuilder:
        """
        Provides operations to manage the overrides property of the microsoft.graph.inferenceClassification entity.
        """
        return overrides_request_builder.OverridesRequestBuilder(self.request_adapter, self.path_parameters)
    
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new InferenceClassificationRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/users/{user%2Did}/inferenceClassification{?%24select}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def create_get_request_information(self,request_configuration: Optional[InferenceClassificationRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Relevance classification of the user's messages based on explicit designations which override inferred relevance or importance.
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
    
    def create_patch_request_information(self,body: Optional[inference_classification.InferenceClassification] = None, request_configuration: Optional[InferenceClassificationRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property inferenceClassification in users
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
    
    async def get(self,request_configuration: Optional[InferenceClassificationRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[inference_classification.InferenceClassification]:
        """
        Relevance classification of the user's messages based on explicit designations which override inferred relevance or importance.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[inference_classification.InferenceClassification]
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
        return await self.request_adapter.send_async(request_info, inference_classification.InferenceClassification, response_handler, error_mapping)
    
    def overrides_by_id(self,id: str) -> inference_classification_override_item_request_builder.InferenceClassificationOverrideItemRequestBuilder:
        """
        Provides operations to manage the overrides property of the microsoft.graph.inferenceClassification entity.
        Args:
            id: Unique identifier of the item
        Returns: inference_classification_override_item_request_builder.InferenceClassificationOverrideItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["inferenceClassificationOverride%2Did"] = id
        return inference_classification_override_item_request_builder.InferenceClassificationOverrideItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[inference_classification.InferenceClassification] = None, request_configuration: Optional[InferenceClassificationRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[inference_classification.InferenceClassification]:
        """
        Update the navigation property inferenceClassification in users
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[inference_classification.InferenceClassification]
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
        return await self.request_adapter.send_async(request_info, inference_classification.InferenceClassification, response_handler, error_mapping)
    
    @dataclass
    class InferenceClassificationRequestBuilderGetQueryParameters():
        """
        Relevance classification of the user's messages based on explicit designations which override inferred relevance or importance.
        """
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
            if original_name == "select":
                return "%24select"
            return original_name
        
    
    @dataclass
    class InferenceClassificationRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[InferenceClassificationRequestBuilder.InferenceClassificationRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class InferenceClassificationRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

