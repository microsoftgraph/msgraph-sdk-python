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
    from ......models.o_data_errors.o_data_error import ODataError
    from .preview_task_failures_post_response import PreviewTaskFailuresPostResponse

class MicrosoftGraphIdentityGovernancePreviewTaskFailuresRequ_71c2adef(BaseRequestBuilder):
    """
    Provides operations to call the previewTaskFailures method. Original name: MicrosoftGraphIdentityGovernancePreviewTaskFailuresRequestBuilder
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MicrosoftGraphIdentityGovernancePreviewTaskFailuresRequ_71c2adef and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/identityGovernance/lifecycleWorkflows/workflows/{workflow%2Did}/microsoft.graph.identityGovernance.previewTaskFailures", path_parameters)
    
    async def post(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[PreviewTaskFailuresPostResponse]:
        """
        Validate the tasks configured in a workflow to check for configuration errors. This action identifies any tasks that would fail during execution, allowing you to fix issues before running the workflow. Returns an empty collection if no task failures are detected.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[PreviewTaskFailuresPostResponse]
        Find more info here: https://learn.microsoft.com/graph/api/identitygovernance-workflow-previewtaskfailures?view=graph-rest-1.0
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .preview_task_failures_post_response import PreviewTaskFailuresPostResponse

        return await self.request_adapter.send_async(request_info, PreviewTaskFailuresPostResponse, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Validate the tasks configured in a workflow to check for configuration errors. This action identifies any tasks that would fail during execution, allowing you to fix issues before running the workflow. Returns an empty collection if no task failures are detected.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> MicrosoftGraphIdentityGovernancePreviewTaskFailuresRequ_71c2adef:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MicrosoftGraphIdentityGovernancePreviewTaskFailuresRequ_71c2adef
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MicrosoftGraphIdentityGovernancePreviewTaskFailuresRequ_71c2adef(self.request_adapter, raw_url)
    
    @dataclass
    class MicrosoftGraphIdentityGovernancePreviewTaskFailuresRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

