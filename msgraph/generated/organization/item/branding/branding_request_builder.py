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
    from ....models.organizational_branding import OrganizationalBranding
    from ....models.o_data_errors.o_data_error import ODataError
    from .background_image.background_image_request_builder import BackgroundImageRequestBuilder
    from .banner_logo.banner_logo_request_builder import BannerLogoRequestBuilder
    from .custom_c_s_s.custom_c_s_s_request_builder import CustomCSSRequestBuilder
    from .favicon.favicon_request_builder import FaviconRequestBuilder
    from .header_logo.header_logo_request_builder import HeaderLogoRequestBuilder
    from .localizations.localizations_request_builder import LocalizationsRequestBuilder
    from .square_logo.square_logo_request_builder import SquareLogoRequestBuilder
    from .square_logo_dark.square_logo_dark_request_builder import SquareLogoDarkRequestBuilder

class BrandingRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the branding property of the microsoft.graph.organization entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BrandingRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/organization/{organization%2Did}/branding{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete the default organizational branding object. To delete the organizationalBranding object, all images (Stream types) must first be removed from the object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/organizationalbranding-delete?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[BrandingRequestBuilderGetQueryParameters]] = None) -> Optional[OrganizationalBranding]:
        """
        Retrieve the default organizational branding object, if the Accept-Language header is set to 0 or default. If no default organizational branding object exists, this method returns a 404 Not Found error. If the Accept-Language header is set to an existing locale identified by the value of its id, this method retrieves the branding for the specified locale. This method retrieves only non-Stream properties, for example, usernameHintText and signInPageText. To retrieve Stream types of the default branding, for example, bannerLogo and backgroundImage, use the GET organizationalBrandingLocalization method.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OrganizationalBranding]
        Find more info here: https://learn.microsoft.com/graph/api/organizationalbranding-get?view=graph-rest-1.0
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
        from ....models.organizational_branding import OrganizationalBranding

        return await self.request_adapter.send_async(request_info, OrganizationalBranding, error_mapping)
    
    async def patch(self,body: OrganizationalBranding, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[OrganizationalBranding]:
        """
        Update the properties of the default branding object specified by the organizationalBranding resource.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OrganizationalBranding]
        Find more info here: https://learn.microsoft.com/graph/api/organizationalbranding-update?view=graph-rest-1.0
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
        from ....models.organizational_branding import OrganizationalBranding

        return await self.request_adapter.send_async(request_info, OrganizationalBranding, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete the default organizational branding object. To delete the organizationalBranding object, all images (Stream types) must first be removed from the object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[BrandingRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Retrieve the default organizational branding object, if the Accept-Language header is set to 0 or default. If no default organizational branding object exists, this method returns a 404 Not Found error. If the Accept-Language header is set to an existing locale identified by the value of its id, this method retrieves the branding for the specified locale. This method retrieves only non-Stream properties, for example, usernameHintText and signInPageText. To retrieve Stream types of the default branding, for example, bannerLogo and backgroundImage, use the GET organizationalBrandingLocalization method.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: OrganizationalBranding, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of the default branding object specified by the organizationalBranding resource.
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
    
    def with_url(self,raw_url: str) -> BrandingRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: BrandingRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return BrandingRequestBuilder(self.request_adapter, raw_url)
    
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
    def localizations(self) -> LocalizationsRequestBuilder:
        """
        Provides operations to manage the localizations property of the microsoft.graph.organizationalBranding entity.
        """
        from .localizations.localizations_request_builder import LocalizationsRequestBuilder

        return LocalizationsRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    class BrandingRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class BrandingRequestBuilderGetQueryParameters():
        """
        Retrieve the default organizational branding object, if the Accept-Language header is set to 0 or default. If no default organizational branding object exists, this method returns a 404 Not Found error. If the Accept-Language header is set to an existing locale identified by the value of its id, this method retrieves the branding for the specified locale. This method retrieves only non-Stream properties, for example, usernameHintText and signInPageText. To retrieve Stream types of the default branding, for example, bannerLogo and backgroundImage, use the GET organizationalBrandingLocalization method.
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
    class BrandingRequestBuilderGetRequestConfiguration(RequestConfiguration[BrandingRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class BrandingRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

