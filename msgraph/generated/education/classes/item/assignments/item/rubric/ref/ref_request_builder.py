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
    from ........models.o_data_errors.o_data_error import ODataError
    from ........models.reference_update import ReferenceUpdate

class RefRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the collection of educationRoot entities.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new RefRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/education/classes/{educationClass%2Did}/assignments/{educationAssignment%2Did}/rubric/$ref", path_parameters)
    
    async def delete(self,request_configuration: Optional[RefRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Remove an educationRubric from an educationAssignment. This method doesn't delete the rubric itself and can only be performed by teachers.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/educationassignment-delete-rubric?view=graph-rest-1.0
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[RefRequestBuilderGetRequestConfiguration] = None) -> Optional[str]:
        """
        Get the educationRubric object attached to an educationAssignment, if one exists. Only teachers, students, and applications with application permissions can perform this operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[str]
        Find more info here: https://learn.microsoft.com/graph/api/educationassignment-get-rubric?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "str", error_mapping)
    
    async def put(self,body: Optional[ReferenceUpdate] = None, request_configuration: Optional[RefRequestBuilderPutRequestConfiguration] = None) -> None:
        """
        Attach an existing educationRubric object to an educationAssignment. Only teachers can perform this operation.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        Find more info here: https://learn.microsoft.com/graph/api/educationassignment-put-rubric?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RefRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Remove an educationRubric from an educationAssignment. This method doesn't delete the rubric itself and can only be performed by teachers.
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
    
    def to_get_request_information(self,request_configuration: Optional[RefRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get the educationRubric object attached to an educationAssignment, if one exists. Only teachers, students, and applications with application permissions can perform this operation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: Optional[ReferenceUpdate] = None, request_configuration: Optional[RefRequestBuilderPutRequestConfiguration] = None) -> RequestInformation:
        """
        Attach an existing educationRubric object to an educationAssignment. Only teachers can perform this operation.
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
        request_info.http_method = Method.PUT
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> RefRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RefRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return RefRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class RefRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class RefRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class RefRequestBuilderPutRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

