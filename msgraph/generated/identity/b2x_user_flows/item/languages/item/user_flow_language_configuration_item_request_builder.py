from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models import user_flow_language_configuration
    from ......models.o_data_errors import o_data_error
    from .default_pages import default_pages_request_builder
    from .default_pages.item import user_flow_language_page_item_request_builder
    from .overrides_pages import overrides_pages_request_builder
    from .overrides_pages.item import user_flow_language_page_item_request_builder

class UserFlowLanguageConfigurationItemRequestBuilder():
    """
    Provides operations to manage the languages property of the microsoft.graph.b2xIdentityUserFlow entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UserFlowLanguageConfigurationItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/identity/b2xUserFlows/{b2xIdentityUserFlow%2Did}/languages/{userFlowLanguageConfiguration%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    def default_pages_by_id(self,id: str) -> user_flow_language_page_item_request_builder.UserFlowLanguagePageItemRequestBuilder:
        """
        Provides operations to manage the defaultPages property of the microsoft.graph.userFlowLanguageConfiguration entity.
        Args:
            id: Unique identifier of the item
        Returns: user_flow_language_page_item_request_builder.UserFlowLanguagePageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .default_pages.item import user_flow_language_page_item_request_builder
        from .overrides_pages.item import user_flow_language_page_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userFlowLanguagePage%2Did"] = id
        return user_flow_language_page_item_request_builder.UserFlowLanguagePageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,request_configuration: Optional[UserFlowLanguageConfigurationItemRequestBuilderDeleteRequestConfiguration] = None) -> bytes:
        """
        Delete navigation property languages for identity
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    async def get(self,request_configuration: Optional[UserFlowLanguageConfigurationItemRequestBuilderGetRequestConfiguration] = None) -> Optional[user_flow_language_configuration.UserFlowLanguageConfiguration]:
        """
        The languages supported for customization within the user flow. Language customization is enabled by default in self-service sign-up user flow. You cannot create custom languages in self-service sign-up user flows.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[user_flow_language_configuration.UserFlowLanguageConfiguration]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import user_flow_language_configuration

        return await self.request_adapter.send_async(request_info, user_flow_language_configuration.UserFlowLanguageConfiguration, error_mapping)
    
    def overrides_pages_by_id(self,id: str) -> user_flow_language_page_item_request_builder.UserFlowLanguagePageItemRequestBuilder:
        """
        Provides operations to manage the overridesPages property of the microsoft.graph.userFlowLanguageConfiguration entity.
        Args:
            id: Unique identifier of the item
        Returns: user_flow_language_page_item_request_builder.UserFlowLanguagePageItemRequestBuilder
        """
        if id is None:
            raise Exception("id cannot be undefined")
        from .default_pages.item import user_flow_language_page_item_request_builder
        from .overrides_pages.item import user_flow_language_page_item_request_builder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userFlowLanguagePage%2Did"] = id
        return user_flow_language_page_item_request_builder.UserFlowLanguagePageItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def patch(self,body: Optional[user_flow_language_configuration.UserFlowLanguageConfiguration] = None, request_configuration: Optional[UserFlowLanguageConfigurationItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[user_flow_language_configuration.UserFlowLanguageConfiguration]:
        """
        Update the navigation property languages in identity
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[user_flow_language_configuration.UserFlowLanguageConfiguration]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models import user_flow_language_configuration

        return await self.request_adapter.send_async(request_info, user_flow_language_configuration.UserFlowLanguageConfiguration, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[UserFlowLanguageConfigurationItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property languages for identity
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
    
    def to_get_request_information(self,request_configuration: Optional[UserFlowLanguageConfigurationItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        The languages supported for customization within the user flow. Language customization is enabled by default in self-service sign-up user flow. You cannot create custom languages in self-service sign-up user flows.
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
    
    def to_patch_request_information(self,body: Optional[user_flow_language_configuration.UserFlowLanguageConfiguration] = None, request_configuration: Optional[UserFlowLanguageConfigurationItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property languages in identity
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
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def default_pages(self) -> default_pages_request_builder.DefaultPagesRequestBuilder:
        """
        Provides operations to manage the defaultPages property of the microsoft.graph.userFlowLanguageConfiguration entity.
        """
        from .default_pages import default_pages_request_builder

        return default_pages_request_builder.DefaultPagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def overrides_pages(self) -> overrides_pages_request_builder.OverridesPagesRequestBuilder:
        """
        Provides operations to manage the overridesPages property of the microsoft.graph.userFlowLanguageConfiguration entity.
        """
        from .overrides_pages import overrides_pages_request_builder

        return overrides_pages_request_builder.OverridesPagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class UserFlowLanguageConfigurationItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class UserFlowLanguageConfigurationItemRequestBuilderGetQueryParameters():
        """
        The languages supported for customization within the user flow. Language customization is enabled by default in self-service sign-up user flow. You cannot create custom languages in self-service sign-up user flows.
        """
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
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class UserFlowLanguageConfigurationItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[UserFlowLanguageConfigurationItemRequestBuilder.UserFlowLanguageConfigurationItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class UserFlowLanguageConfigurationItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

