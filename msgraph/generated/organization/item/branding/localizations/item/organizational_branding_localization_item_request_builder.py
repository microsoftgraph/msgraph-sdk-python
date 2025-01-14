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
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OrganizationalBrandingLocalizationItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/organization/{organization%2Did}/branding/localizations/{organizationalBrandingLocalization%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
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

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[OrganizationalBrandingLocalizationItemRequestBuilderGetQueryParameters]] = None) -> Optional[OrganizationalBrandingLocalization]:
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

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.organizational_branding_localization import OrganizationalBrandingLocalization

        return await self.request_adapter.send_async(request_info, OrganizationalBrandingLocalization, error_mapping)
    
    async def patch(self,body: OrganizationalBrandingLocalization, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[OrganizationalBrandingLocalization]:
        """
        Update the properties of an organizationalBrandingLocalization object for a specific localization.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OrganizationalBrandingLocalization]
        Find more info here: https://learn.microsoft.com/graph/api/organizationalbrandinglocalization-update?view=graph-rest-1.0
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.organizational_branding_localization import OrganizationalBrandingLocalization

        return await self.request_adapter.send_async(request_info, OrganizationalBrandingLocalization, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete a localized branding object. To delete the organizationalBrandingLocalization object, all images (Stream types) must first be removed from the object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[OrganizationalBrandingLocalizationItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Read the properties and relationships of an organizationalBrandingLocalization object. To retrieve a localization branding object, specify the value of id in the URL.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: OrganizationalBrandingLocalization, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of an organizationalBrandingLocalization object for a specific localization.
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
    
    def with_url(self,raw_url: str) -> OrganizationalBrandingLocalizationItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: OrganizationalBrandingLocalizationItemRequestBuilder
        """
        if raw_url is None:
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
    
    @dataclass
    class OrganizationalBrandingLocalizationItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OrganizationalBrandingLocalizationItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of an organizationalBrandingLocalization object. To retrieve a localization branding object, specify the value of id in the URL.
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
    class OrganizationalBrandingLocalizationItemRequestBuilderGetRequestConfiguration(RequestConfiguration[OrganizationalBrandingLocalizationItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class OrganizationalBrandingLocalizationItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

