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
    from ....models.booking_business import BookingBusiness
    from ....models.o_data_errors.o_data_error import ODataError
    from .appointments.appointments_request_builder import AppointmentsRequestBuilder
    from .calendar_view.calendar_view_request_builder import CalendarViewRequestBuilder
    from .customers.customers_request_builder import CustomersRequestBuilder
    from .custom_questions.custom_questions_request_builder import CustomQuestionsRequestBuilder
    from .get_staff_availability.get_staff_availability_request_builder import GetStaffAvailabilityRequestBuilder
    from .publish.publish_request_builder import PublishRequestBuilder
    from .services.services_request_builder import ServicesRequestBuilder
    from .staff_members.staff_members_request_builder import StaffMembersRequestBuilder
    from .unpublish.unpublish_request_builder import UnpublishRequestBuilder

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
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
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
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[BookingBusinessItemRequestBuilderGetRequestConfiguration] = None) -> Optional[BookingBusiness]:
        """
        Get the properties and relationships of a bookingBusiness object.
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BookingBusiness]
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
        from ....models.booking_business import BookingBusiness

        return await self.request_adapter.send_async(request_info, BookingBusiness, error_mapping)
    
    async def patch(self,body: Optional[BookingBusiness] = None, request_configuration: Optional[BookingBusinessItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[BookingBusiness]:
        """
        Update the properties of a bookingBusiness object.
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BookingBusiness]
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
        from ....models.booking_business import BookingBusiness

        return await self.request_adapter.send_async(request_info, BookingBusiness, error_mapping)
    
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
    
    def to_patch_request_information(self,body: Optional[BookingBusiness] = None, request_configuration: Optional[BookingBusinessItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of a bookingBusiness object.
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
    def appointments(self) -> AppointmentsRequestBuilder:
        """
        Provides operations to manage the appointments property of the microsoft.graph.bookingBusiness entity.
        """
        from .appointments.appointments_request_builder import AppointmentsRequestBuilder

        return AppointmentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def calendar_view(self) -> CalendarViewRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.bookingBusiness entity.
        """
        from .calendar_view.calendar_view_request_builder import CalendarViewRequestBuilder

        return CalendarViewRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customers(self) -> CustomersRequestBuilder:
        """
        Provides operations to manage the customers property of the microsoft.graph.bookingBusiness entity.
        """
        from .customers.customers_request_builder import CustomersRequestBuilder

        return CustomersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def custom_questions(self) -> CustomQuestionsRequestBuilder:
        """
        Provides operations to manage the customQuestions property of the microsoft.graph.bookingBusiness entity.
        """
        from .custom_questions.custom_questions_request_builder import CustomQuestionsRequestBuilder

        return CustomQuestionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_staff_availability(self) -> GetStaffAvailabilityRequestBuilder:
        """
        Provides operations to call the getStaffAvailability method.
        """
        from .get_staff_availability.get_staff_availability_request_builder import GetStaffAvailabilityRequestBuilder

        return GetStaffAvailabilityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def publish(self) -> PublishRequestBuilder:
        """
        Provides operations to call the publish method.
        """
        from .publish.publish_request_builder import PublishRequestBuilder

        return PublishRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def services(self) -> ServicesRequestBuilder:
        """
        Provides operations to manage the services property of the microsoft.graph.bookingBusiness entity.
        """
        from .services.services_request_builder import ServicesRequestBuilder

        return ServicesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def staff_members(self) -> StaffMembersRequestBuilder:
        """
        Provides operations to manage the staffMembers property of the microsoft.graph.bookingBusiness entity.
        """
        from .staff_members.staff_members_request_builder import StaffMembersRequestBuilder

        return StaffMembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unpublish(self) -> UnpublishRequestBuilder:
        """
        Provides operations to call the unpublish method.
        """
        from .unpublish.unpublish_request_builder import UnpublishRequestBuilder

        return UnpublishRequestBuilder(self.request_adapter, self.path_parameters)
    
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

    

