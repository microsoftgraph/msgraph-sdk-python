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
    from ....models import booking_business
    from ....models.o_data_errors import o_data_error
    from .appointments import appointments_request_builder
    from .calendar_view import calendar_view_request_builder
    from .customers import customers_request_builder
    from .custom_questions import custom_questions_request_builder
    from .get_staff_availability import get_staff_availability_request_builder
    from .publish import publish_request_builder
    from .services import services_request_builder
    from .staff_members import staff_members_request_builder
    from .unpublish import unpublish_request_builder

class BookingBusinessItemRequestBuilder():
    """
    Provides operations to manage the bookingBusinesses property of the microsoft.graph.solutionsRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new BookingBusinessItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/solutions/bookingBusinesses/{bookingBusiness%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[BookingBusinessItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete a bookingBusiness object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[BookingBusinessItemRequestBuilderGetRequestConfiguration] = None) -> Optional[booking_business.BookingBusiness]:
        """
        Get the properties and relationships of a bookingBusiness object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[booking_business.BookingBusiness]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import booking_business

        return await self.request_adapter.send_async(request_info, booking_business.BookingBusiness, error_mapping)
    
    async def patch(self,body: Optional[booking_business.BookingBusiness] = None, request_configuration: Optional[BookingBusinessItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[booking_business.BookingBusiness]:
        """
        Update the properties of a bookingBusiness object.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[booking_business.BookingBusiness]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ....models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models import booking_business

        return await self.request_adapter.send_async(request_info, booking_business.BookingBusiness, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[BookingBusinessItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete a bookingBusiness object.
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
    
    def to_get_request_information(self,request_configuration: Optional[BookingBusinessItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the properties and relationships of a bookingBusiness object.
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
    
    def to_patch_request_information(self,body: Optional[booking_business.BookingBusiness] = None, request_configuration: Optional[BookingBusinessItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a bookingBusiness object.
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
    def appointments(self) -> appointments_request_builder.AppointmentsRequestBuilder:
        """
        Provides operations to manage the appointments property of the microsoft.graph.bookingBusiness entity.
        """
        from .appointments import appointments_request_builder

        return appointments_request_builder.AppointmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar_view(self) -> calendar_view_request_builder.CalendarViewRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.bookingBusiness entity.
        """
        from .calendar_view import calendar_view_request_builder

        return calendar_view_request_builder.CalendarViewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customers(self) -> customers_request_builder.CustomersRequestBuilder:
        """
        Provides operations to manage the customers property of the microsoft.graph.bookingBusiness entity.
        """
        from .customers import customers_request_builder

        return customers_request_builder.CustomersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custom_questions(self) -> custom_questions_request_builder.CustomQuestionsRequestBuilder:
        """
        Provides operations to manage the customQuestions property of the microsoft.graph.bookingBusiness entity.
        """
        from .custom_questions import custom_questions_request_builder

        return custom_questions_request_builder.CustomQuestionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_staff_availability(self) -> get_staff_availability_request_builder.GetStaffAvailabilityRequestBuilder:
        """
        Provides operations to call the getStaffAvailability method.
        """
        from .get_staff_availability import get_staff_availability_request_builder

        return get_staff_availability_request_builder.GetStaffAvailabilityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def publish(self) -> publish_request_builder.PublishRequestBuilder:
        """
        Provides operations to call the publish method.
        """
        from .publish import publish_request_builder

        return publish_request_builder.PublishRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def services(self) -> services_request_builder.ServicesRequestBuilder:
        """
        Provides operations to manage the services property of the microsoft.graph.bookingBusiness entity.
        """
        from .services import services_request_builder

        return services_request_builder.ServicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def staff_members(self) -> staff_members_request_builder.StaffMembersRequestBuilder:
        """
        Provides operations to manage the staffMembers property of the microsoft.graph.bookingBusiness entity.
        """
        from .staff_members import staff_members_request_builder

        return staff_members_request_builder.StaffMembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unpublish(self) -> unpublish_request_builder.UnpublishRequestBuilder:
        """
        Provides operations to call the unpublish method.
        """
        from .unpublish import unpublish_request_builder

        return unpublish_request_builder.UnpublishRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class BookingBusinessItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class BookingBusinessItemRequestBuilderGetQueryParameters():
        """
        Get the properties and relationships of a bookingBusiness object.
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
    class BookingBusinessItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[BookingBusinessItemRequestBuilder.BookingBusinessItemRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class BookingBusinessItemRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

