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

class BookingBusinessItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the bookingBusinesses property of the microsoft.graph.solutionsRoot entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BookingBusinessItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/solutions/bookingBusinesses/{bookingBusiness%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> None:
        """
        Delete a bookingBusiness object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/bookingbusiness-delete?view=graph-rest-1.0
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[BookingBusinessItemRequestBuilderGetQueryParameters]] = None) -> Optional[BookingBusiness]:
        """
        Get the properties and relationships of a bookingBusiness object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BookingBusiness]
        Find more info here: https://learn.microsoft.com/graph/api/bookingbusiness-get?view=graph-rest-1.0
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
        from ....models.booking_business import BookingBusiness

        return await self.request_adapter.send_async(request_info, BookingBusiness, error_mapping)
    
    async def patch(self,body: BookingBusiness, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[BookingBusiness]:
        """
        Update the properties of a bookingBusiness object.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[BookingBusiness]
        Find more info here: https://learn.microsoft.com/graph/api/bookingbusiness-update?view=graph-rest-1.0
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
        from ....models.booking_business import BookingBusiness

        return await self.request_adapter.send_async(request_info, BookingBusiness, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Delete a bookingBusiness object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[BookingBusinessItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Get the properties and relationships of a bookingBusiness object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: BookingBusiness, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update the properties of a bookingBusiness object.
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
    
    def with_url(self,raw_url: str) -> BookingBusinessItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: BookingBusinessItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return BookingBusinessItemRequestBuilder(self.request_adapter, raw_url)
    
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
    def custom_questions(self) -> CustomQuestionsRequestBuilder:
        """
        Provides operations to manage the customQuestions property of the microsoft.graph.bookingBusiness entity.
        """
        from .custom_questions.custom_questions_request_builder import CustomQuestionsRequestBuilder

        return CustomQuestionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def customers(self) -> CustomersRequestBuilder:
        """
        Provides operations to manage the customers property of the microsoft.graph.bookingBusiness entity.
        """
        from .customers.customers_request_builder import CustomersRequestBuilder

        return CustomersRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    class BookingBusinessItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class BookingBusinessItemRequestBuilderGetQueryParameters():
        """
        Get the properties and relationships of a bookingBusiness object.
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
    class BookingBusinessItemRequestBuilderGetRequestConfiguration(RequestConfiguration[BookingBusinessItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class BookingBusinessItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

