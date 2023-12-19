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
    from ......models.organizational_branding_localization import OrganizationalBrandingLocalization
    from ......models.o_data_errors.o_data_error import ODataError
    from .background_image.background_image_request_builder import BackgroundImageRequestBuilder
    from .banner_logo.banner_logo_request_builder import BannerLogoRequestBuilder
    from .custom_c_s_s.custom_c_s_s_request_builder import CustomCSSRequestBuilder
    from .favicon.favicon_request_builder import FaviconRequestBuilder
    from .header_logo.header_logo_request_builder import HeaderLogoRequestBuilder
    from .square_logo.square_logo_request_builder import SquareLogoRequestBuilder
    from .square_logo_dark.square_logo_dark_request_builder import SquareLogoDarkRequestBuilder

class OrganizationalBrandingLocalizationItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the localizations property of the microsoft.graph.organizationalBranding entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new OrganizationalBrandingLocalizationItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/organization/{organization%2Did}/branding/localizations/{organizationalBrandingLocalization%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete a localized branding object. To delete the organizationalBrandingLocalization object, all images (Stream types) must first be removed from the object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/organizationalbrandinglocalization-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderGetRequestConfiguration] = None) -> Optional[OrganizationalBrandingLocalization]:
        """
        Read the properties and relationships of an organizationalBrandingLocalization object. To retrieve a localization branding object, specify the value of id in the URL.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OrganizationalBrandingLocalization]
        Find more info here: https://learn.microsoft.com/graph/api/organizationalbrandinglocalization-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.organizational_branding_localization import OrganizationalBrandingLocalization

        return await self.request_adapter.send_async(request_info, OrganizationalBrandingLocalization, error_mapping)
    
    async def patch(self,body: Optional[OrganizationalBrandingLocalization] = None, request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[OrganizationalBrandingLocalization]:
        """
        Update the properties of an organizationalBrandingLocalization object for a specific localization.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OrganizationalBrandingLocalization]
        Find more info here: https://learn.microsoft.com/graph/api/organizationalbrandinglocalization-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.organizational_branding_localization import OrganizationalBrandingLocalization

        return await self.request_adapter.send_async(request_info, OrganizationalBrandingLocalization, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete a localized branding object. To delete the organizationalBrandingLocalization object, all images (Stream types) must first be removed from the object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of an organizationalBrandingLocalization object. To retrieve a localization branding object, specify the value of id in the URL.
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
    
    def to_patch_request_information(self,body: Optional[OrganizationalBrandingLocalization] = None, request_configuration: Optional[OrganizationalBrandingLocalizationItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of an organizationalBrandingLocalization object for a specific localization.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> OrganizationalBrandingLocalizationItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OrganizationalBrandingLocalizationItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return OrganizationalBrandingLocalizationItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def background_image(self) -> BackgroundImageRequestBuilder:
        """
        Provides operations to manage the media for the organization entity.
        """
        from .background_image.background_image_request_builder import BackgroundImageRequestBuilder

        return BackgroundImageRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def banner_logo(self) -> BannerLogoRequestBuilder:
        """
        Provides operations to manage the media for the organization entity.
        """
        from .banner_logo.banner_logo_request_builder import BannerLogoRequestBuilder

        return BannerLogoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custom_c_s_s(self) -> CustomCSSRequestBuilder:
        """
        Provides operations to manage the media for the organization entity.
        """
        from .custom_c_s_s.custom_c_s_s_request_builder import CustomCSSRequestBuilder

        return CustomCSSRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def favicon(self) -> FaviconRequestBuilder:
        """
        Provides operations to manage the media for the organization entity.
        """
        from .favicon.favicon_request_builder import FaviconRequestBuilder

        return FaviconRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def header_logo(self) -> HeaderLogoRequestBuilder:
        """
        Provides operations to manage the media for the organization entity.
        """
        from .header_logo.header_logo_request_builder import HeaderLogoRequestBuilder

        return HeaderLogoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def square_logo(self) -> SquareLogoRequestBuilder:
        """
        Provides operations to manage the media for the organization entity.
        """
        from .square_logo.square_logo_request_builder import SquareLogoRequestBuilder

        return SquareLogoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def square_logo_dark(self) -> SquareLogoDarkRequestBuilder:
        """
        Provides operations to manage the media for the organization entity.
        """
        from .square_logo_dark.square_logo_dark_request_builder import SquareLogoDarkRequestBuilder

        return SquareLogoDarkRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class OrganizationalBrandingLocalizationItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class OrganizationalBrandingLocalizationItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of an organizationalBrandingLocalization object. To retrieve a localization branding object, specify the value of id in the URL.
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
    class OrganizationalBrandingLocalizationItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[OrganizationalBrandingLocalizationItemRequestBuilder.OrganizationalBrandingLocalizationItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class OrganizationalBrandingLocalizationItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

