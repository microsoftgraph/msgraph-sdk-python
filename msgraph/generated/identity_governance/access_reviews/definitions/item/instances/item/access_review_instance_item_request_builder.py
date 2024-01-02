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
    from .......models.access_review_instance import AccessReviewInstance
    from .......models.o_data_errors.o_data_error import ODataError
    from .accept_recommendations.accept_recommendations_request_builder import AcceptRecommendationsRequestBuilder
    from .apply_decisions.apply_decisions_request_builder import ApplyDecisionsRequestBuilder
    from .batch_record_decisions.batch_record_decisions_request_builder import BatchRecordDecisionsRequestBuilder
    from .contacted_reviewers.contacted_reviewers_request_builder import ContactedReviewersRequestBuilder
    from .decisions.decisions_request_builder import DecisionsRequestBuilder
    from .reset_decisions.reset_decisions_request_builder import ResetDecisionsRequestBuilder
    from .send_reminder.send_reminder_request_builder import SendReminderRequestBuilder
    from .stages.stages_request_builder import StagesRequestBuilder
    from .stop.stop_request_builder import StopRequestBuilder

class AccessReviewInstanceItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the instances property of the microsoft.graph.accessReviewScheduleDefinition entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new AccessReviewInstanceItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/accessReviews/definitions/{accessReviewScheduleDefinition%2Did}/instances/{accessReviewInstance%2Did}{?%24select,%24expand}", path_parameters)
    
    async def delete(self,request_configuration: Optional[AccessReviewInstanceItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property instances for identityGovernance
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[AccessReviewInstanceItemRequestBuilderGetRequestConfiguration] = None) -> Optional[AccessReviewInstance]:
        """
        Read the properties and relationships of an accessReviewInstance object.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessReviewInstance]
        Find more info here: https://learn.microsoft.com/graph/api/accessreviewinstance-get?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.access_review_instance import AccessReviewInstance

        return await self.request_adapter.send_async(request_info, AccessReviewInstance, error_mapping)
    
    async def patch(self,body: Optional[AccessReviewInstance] = None, request_configuration: Optional[AccessReviewInstanceItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[AccessReviewInstance]:
        """
        Update the properties of an accessReviewInstance object. Only the reviewers and fallbackReviewers properties can be updated but the scope property is also required in the request body. You can only add reviewers to the fallbackReviewers property but can't remove existing fallbackReviewers. To update an accessReviewInstance, it's status must be InProgress.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AccessReviewInstance]
        Find more info here: https://learn.microsoft.com/graph/api/accessreviewinstance-update?view=graph-rest-1.0
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.access_review_instance import AccessReviewInstance

        return await self.request_adapter.send_async(request_info, AccessReviewInstance, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[AccessReviewInstanceItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property instances for identityGovernance
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
    
    def to_get_request_information(self,request_configuration: Optional[AccessReviewInstanceItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Read the properties and relationships of an accessReviewInstance object.
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
    
    def to_patch_request_information(self,body: Optional[AccessReviewInstance] = None, request_configuration: Optional[AccessReviewInstanceItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the properties of an accessReviewInstance object. Only the reviewers and fallbackReviewers properties can be updated but the scope property is also required in the request body. You can only add reviewers to the fallbackReviewers property but can't remove existing fallbackReviewers. To update an accessReviewInstance, it's status must be InProgress.
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
    
    def with_url(self,raw_url: Optional[str] = None) -> AccessReviewInstanceItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AccessReviewInstanceItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return AccessReviewInstanceItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def accept_recommendations(self) -> AcceptRecommendationsRequestBuilder:
        """
        Provides operations to call the acceptRecommendations method.
        """
        from .accept_recommendations.accept_recommendations_request_builder import AcceptRecommendationsRequestBuilder

        return AcceptRecommendationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def apply_decisions(self) -> ApplyDecisionsRequestBuilder:
        """
        Provides operations to call the applyDecisions method.
        """
        from .apply_decisions.apply_decisions_request_builder import ApplyDecisionsRequestBuilder

        return ApplyDecisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def batch_record_decisions(self) -> BatchRecordDecisionsRequestBuilder:
        """
        Provides operations to call the batchRecordDecisions method.
        """
        from .batch_record_decisions.batch_record_decisions_request_builder import BatchRecordDecisionsRequestBuilder

        return BatchRecordDecisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def contacted_reviewers(self) -> ContactedReviewersRequestBuilder:
        """
        Provides operations to manage the contactedReviewers property of the microsoft.graph.accessReviewInstance entity.
        """
        from .contacted_reviewers.contacted_reviewers_request_builder import ContactedReviewersRequestBuilder

        return ContactedReviewersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def decisions(self) -> DecisionsRequestBuilder:
        """
        Provides operations to manage the decisions property of the microsoft.graph.accessReviewInstance entity.
        """
        from .decisions.decisions_request_builder import DecisionsRequestBuilder

        return DecisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reset_decisions(self) -> ResetDecisionsRequestBuilder:
        """
        Provides operations to call the resetDecisions method.
        """
        from .reset_decisions.reset_decisions_request_builder import ResetDecisionsRequestBuilder

        return ResetDecisionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def send_reminder(self) -> SendReminderRequestBuilder:
        """
        Provides operations to call the sendReminder method.
        """
        from .send_reminder.send_reminder_request_builder import SendReminderRequestBuilder

        return SendReminderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def stages(self) -> StagesRequestBuilder:
        """
        Provides operations to manage the stages property of the microsoft.graph.accessReviewInstance entity.
        """
        from .stages.stages_request_builder import StagesRequestBuilder

        return StagesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def stop(self) -> StopRequestBuilder:
        """
        Provides operations to call the stop method.
        """
        from .stop.stop_request_builder import StopRequestBuilder

        return StopRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AccessReviewInstanceItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class AccessReviewInstanceItemRequestBuilderGetQueryParameters():
        """
        Read the properties and relationships of an accessReviewInstance object.
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
    class AccessReviewInstanceItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[AccessReviewInstanceItemRequestBuilder.AccessReviewInstanceItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class AccessReviewInstanceItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

