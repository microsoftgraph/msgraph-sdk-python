from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, Union

from ....models import booking_business
from ....models.o_data_errors import o_data_error
from .appointments import appointments_request_builder
from .appointments.item import booking_appointment_item_request_builder
from .calendar_view import calendar_view_request_builder
from .calendar_view.item import booking_appointment_item_request_builder
from .customers import customers_request_builder
from .customers.item import booking_customer_base_item_request_builder
from .custom_questions import custom_questions_request_builder
from .custom_questions.item import booking_custom_question_item_request_builder
from .get_staff_availability import get_staff_availability_request_builder
from .publish import publish_request_builder
from .services import services_request_builder
from .services.item import booking_service_item_request_builder
from .staff_members import staff_members_request_builder
from .staff_members.item import booking_staff_member_base_item_request_builder
from .unpublish import unpublish_request_builder

class BookingBusinessItemRequestBuilder():
    """
    Provides operations to manage the bookingBusinesses property of the microsoft.graph.solutionsRoot entity.
    """
    def appointments(self) -> appointments_request_builder.AppointmentsRequestBuilder:
        """
        Provides operations to manage the appointments property of the microsoft.graph.bookingBusiness entity.
        """
        return appointments_request_builder.AppointmentsRequestBuilder(self.request_adapter, self.path_parameters)

    def calendar_view(self) -> calendar_view_request_builder.CalendarViewRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.bookingBusiness entity.
        """
        return calendar_view_request_builder.CalendarViewRequestBuilder(self.request_adapter, self.path_parameters)

    def customers(self) -> customers_request_builder.CustomersRequestBuilder:
        """
        Provides operations to manage the customers property of the microsoft.graph.bookingBusiness entity.
        """
        return customers_request_builder.CustomersRequestBuilder(self.request_adapter, self.path_parameters)

    def custom_questions(self) -> custom_questions_request_builder.CustomQuestionsRequestBuilder:
        """
        Provides operations to manage the customQuestions property of the microsoft.graph.bookingBusiness entity.
        """
        return custom_questions_request_builder.CustomQuestionsRequestBuilder(self.request_adapter, self.path_parameters)

    def get_staff_availability(self) -> get_staff_availability_request_builder.GetStaffAvailabilityRequestBuilder:
        """
        Provides operations to call the getStaffAvailability method.
        """
        return get_staff_availability_request_builder.GetStaffAvailabilityRequestBuilder(self.request_adapter, self.path_parameters)

    def publish(self) -> publish_request_builder.PublishRequestBuilder:
        """
        Provides operations to call the publish method.
        """
        return publish_request_builder.PublishRequestBuilder(self.request_adapter, self.path_parameters)

    def services(self) -> services_request_builder.ServicesRequestBuilder:
        """
        Provides operations to manage the services property of the microsoft.graph.bookingBusiness entity.
        """
        return services_request_builder.ServicesRequestBuilder(self.request_adapter, self.path_parameters)

    def staff_members(self) -> staff_members_request_builder.StaffMembersRequestBuilder:
        """
        Provides operations to manage the staffMembers property of the microsoft.graph.bookingBusiness entity.
        """
        return staff_members_request_builder.StaffMembersRequestBuilder(self.request_adapter, self.path_parameters)

    def unpublish(self) -> unpublish_request_builder.UnpublishRequestBuilder:
        """
        Provides operations to call the unpublish method.
        """
        return unpublish_request_builder.UnpublishRequestBuilder(self.request_adapter, self.path_parameters)

    def appointments_by_id(self,id: str) -> booking_appointment_item_request_builder.BookingAppointmentItemRequestBuilder:
        """
        Provides operations to manage the appointments property of the microsoft.graph.bookingBusiness entity.
        Args:
            id: Unique identifier of the item
        Returns: booking_appointment_item_request_builder.BookingAppointmentItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["bookingAppointment%2Did"] = id
        return booking_appointment_item_request_builder.BookingAppointmentItemRequestBuilder(self.request_adapter, url_tpl_params)

    def calendar_view_by_id(self,id: str) -> booking_appointment_item_request_builder.BookingAppointmentItemRequestBuilder:
        """
        Provides operations to manage the calendarView property of the microsoft.graph.bookingBusiness entity.
        Args:
            id: Unique identifier of the item
        Returns: booking_appointment_item_request_builder.BookingAppointmentItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["bookingAppointment%2Did"] = id
        return booking_appointment_item_request_builder.BookingAppointmentItemRequestBuilder(self.request_adapter, url_tpl_params)

    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new BookingBusinessItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise Exception("path_parameters cannot be undefined")
        if not request_adapter:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/solutions/bookingBusinesses/{bookingBusiness%2Did}{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter

    def create_delete_request_information(self,request_configuration: Optional[BookingBusinessItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property bookingBusinesses for solutions
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

    def create_get_request_information(self,request_configuration: Optional[BookingBusinessItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get bookingBusinesses from solutions
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

    def create_patch_request_information(self,body: Optional[booking_business.BookingBusiness] = None, request_configuration: Optional[BookingBusinessItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property bookingBusinesses in solutions
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
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

    def customers_by_id(self,id: str) -> booking_customer_base_item_request_builder.BookingCustomerBaseItemRequestBuilder:
        """
        Provides operations to manage the customers property of the microsoft.graph.bookingBusiness entity.
        Args:
            id: Unique identifier of the item
        Returns: booking_customer_base_item_request_builder.BookingCustomerBaseItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["bookingCustomerBase%2Did"] = id
        return booking_customer_base_item_request_builder.BookingCustomerBaseItemRequestBuilder(self.request_adapter, url_tpl_params)

    def custom_questions_by_id(self,id: str) -> booking_custom_question_item_request_builder.BookingCustomQuestionItemRequestBuilder:
        """
        Provides operations to manage the customQuestions property of the microsoft.graph.bookingBusiness entity.
        Args:
            id: Unique identifier of the item
        Returns: booking_custom_question_item_request_builder.BookingCustomQuestionItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["bookingCustomQuestion%2Did"] = id
        return booking_custom_question_item_request_builder.BookingCustomQuestionItemRequestBuilder(self.request_adapter, url_tpl_params)

    async def delete(self,request_configuration: Optional[BookingBusinessItemRequestBuilderDeleteRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> None:
        """
        Delete navigation property bookingBusinesses for solutions
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        """
        request_info = self.create_delete_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, response_handler, error_mapping)

    async def get(self,request_configuration: Optional[BookingBusinessItemRequestBuilderGetRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[booking_business.BookingBusiness]:
        """
        Get bookingBusinesses from solutions
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[booking_business.BookingBusiness]
        """
        request_info = self.create_get_request_information(
            request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, booking_business.BookingBusiness, response_handler, error_mapping)

    async def patch(self,body: Optional[booking_business.BookingBusiness] = None, request_configuration: Optional[BookingBusinessItemRequestBuilderPatchRequestConfiguration] = None, response_handler: Optional[ResponseHandler] = None) -> Optional[booking_business.BookingBusiness]:
        """
        Update the navigation property bookingBusinesses in solutions
        Args:
            body: 
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
            responseHandler: Response handler to use in place of the default response handling provided by the core service
        Returns: Optional[booking_business.BookingBusiness]
        """
        if not body:
            raise Exception("body cannot be undefined")
        request_info = self.create_patch_request_information(
            body, request_configuration
        )
        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError.get_from_discriminator_value(),
            "5XX": o_data_error.ODataError.get_from_discriminator_value(),
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_async(request_info, booking_business.BookingBusiness, response_handler, error_mapping)

    def services_by_id(self,id: str) -> booking_service_item_request_builder.BookingServiceItemRequestBuilder:
        """
        Provides operations to manage the services property of the microsoft.graph.bookingBusiness entity.
        Args:
            id: Unique identifier of the item
        Returns: booking_service_item_request_builder.BookingServiceItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["bookingService%2Did"] = id
        return booking_service_item_request_builder.BookingServiceItemRequestBuilder(self.request_adapter, url_tpl_params)

    def staff_members_by_id(self,id: str) -> booking_staff_member_base_item_request_builder.BookingStaffMemberBaseItemRequestBuilder:
        """
        Provides operations to manage the staffMembers property of the microsoft.graph.bookingBusiness entity.
        Args:
            id: Unique identifier of the item
        Returns: booking_staff_member_base_item_request_builder.BookingStaffMemberBaseItemRequestBuilder
        """
        if not id:
            raise Exception("id cannot be undefined")
        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["bookingStaffMemberBase%2Did"] = id
        return booking_staff_member_base_item_request_builder.BookingStaffMemberBaseItemRequestBuilder(self.request_adapter, url_tpl_params)

    @dataclass
    class BookingBusinessItemRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class BookingBusinessItemRequestBuilderGetQueryParameters():
        """
        Get bookingBusinesses from solutions
        """
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name

    
    @dataclass
    class BookingBusinessItemRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, str]] = None

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
        headers: Optional[Dict[str, str]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

