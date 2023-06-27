from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models.o_data_errors.o_data_error import ODataError
    from ....models.organizational_branding import OrganizationalBranding
    from .background_image.background_image_request_builder import BackgroundImageRequestBuilder
    from .banner_logo.banner_logo_request_builder import BannerLogoRequestBuilder
    from .custom_c_s_s.custom_c_s_s_request_builder import CustomCSSRequestBuilder
    from .favicon.favicon_request_builder import FaviconRequestBuilder
    from .header_logo.header_logo_request_builder import HeaderLogoRequestBuilder
    from .localizations.localizations_request_builder import LocalizationsRequestBuilder
    from .square_logo.square_logo_request_builder import SquareLogoRequestBuilder
    from .square_logo_dark.square_logo_dark_request_builder import SquareLogoDarkRequestBuilder

class BrandingRequestBuilder():
    """
    Provides operations to manage the branding property of the microsoft.graph.organization entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new BrandingRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/organization/{organization%2Did}/branding{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[BrandingRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete the default organizational branding object. To delete the organizationalBranding object, all images (Stream types) must first be removed from the object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[BrandingRequestBuilderGetRequestConfiguration] = None) -> Optional[OrganizationalBranding]:
        """
        Retrieve the default organizational branding object, if the **Accept-Language** header is set to `0` or `default`. If no default organizational branding object exists, this method returns a `404 Not Found` error. If the **Accept-Language** header is set to an existing locale identified by the value of its **id**, this method retrieves the branding for the specified locale. This method retrieves only non-Stream properties, for example, **usernameHintText** and **signInPageText**. To retrieve Stream types of the default branding, for example, **bannerLogo** and **backgroundImage**, use the GET organizationalBrandingLocalization method.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OrganizationalBranding]
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
        from ....models.organizational_branding import OrganizationalBranding

        return await self.request_adapter.send_async(request_info, OrganizationalBranding, error_mapping)
    
    async def patch(self,body: Optional[OrganizationalBranding] = None, request_configuration: Optional[BrandingRequestBuilderPatchRequestConfiguration] = None) -> Optional[OrganizationalBranding]:
        """
        Update the properties of the default branding object specified by the organizationalBranding resource.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[OrganizationalBranding]
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
        from ....models.organizational_branding import OrganizationalBranding

        return await self.request_adapter.send_async(request_info, OrganizationalBranding, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[BrandingRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete the default organizational branding object. To delete the organizationalBranding object, all images (Stream types) must first be removed from the object.
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
    
    def to_get_request_information(self,request_configuration: Optional[BrandingRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Retrieve the default organizational branding object, if the **Accept-Language** header is set to `0` or `default`. If no default organizational branding object exists, this method returns a `404 Not Found` error. If the **Accept-Language** header is set to an existing locale identified by the value of its **id**, this method retrieves the branding for the specified locale. This method retrieves only non-Stream properties, for example, **usernameHintText** and **signInPageText**. To retrieve Stream types of the default branding, for example, **bannerLogo** and **backgroundImage**, use the GET organizationalBrandingLocalization method.
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
    
    def to_patch_request_information(self,body: Optional[OrganizationalBranding] = None, request_configuration: Optional[BrandingRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of the default branding object specified by the organizationalBranding resource.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
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
    class BrandingRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class BrandingRequestBuilderGetQueryParameters():
        """
        Retrieve the default organizational branding object, if the **Accept-Language** header is set to `0` or `default`. If no default organizational branding object exists, this method returns a `404 Not Found` error. If the **Accept-Language** header is set to an existing locale identified by the value of its **id**, this method retrieves the branding for the specified locale. This method retrieves only non-Stream properties, for example, **usernameHintText** and **signInPageText**. To retrieve Stream types of the default branding, for example, **bannerLogo** and **backgroundImage**, use the GET organizationalBrandingLocalization method.
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
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

    
    @dataclass
    class BrandingRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[BrandingRequestBuilder.BrandingRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class BrandingRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

