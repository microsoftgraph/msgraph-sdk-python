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
    from .......models.o_data_errors.o_data_error import ODataError
    from .......models.sensitivity_label import SensitivityLabel

class ComputeInheritanceWithLabelIdsWithLocaleWithContentFormatsRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the computeInheritance method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]], content_formats: Optional[str] = None, label_ids: Optional[str] = None, locale: Optional[str] = None) -> None:
        """
        Instantiates a new ComputeInheritanceWithLabelIdsWithLocaleWithContentFormatsRequestBuilder and sets the default values.
        param content_formats: Usage: contentFormats={contentFormats}
        param label_ids: Usage: labelIds={labelIds}
        param locale: Usage: locale='{locale}'
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if isinstance(path_parameters, dict):
            path_parameters['contentFormats'] = content_formats
            path_parameters['labelIds'] = label_ids
            path_parameters['locale'] = locale
        super().__init__(request_adapter, "{+baseurl}/security/dataSecurityAndGovernance/sensitivityLabels/{sensitivityLabel%2Did}/sublabels/computeInheritance(labelIds={labelIds},locale='{locale}',contentFormats={contentFormats})", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SensitivityLabel]:
        """
        Calculate the sensitivity label that should be inherited by an output artifact, given a set of sensitivity labels from input or referenced artifacts.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SensitivityLabel]
        Find more info here: https://learn.microsoft.com/graph/api/sensitivitylabel-computeinheritance?view=graph-rest-1.0
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .......models.o_data_errors.o_data_error import ODataError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.sensitivity_label import SensitivityLabel

        return await self.request_adapter.send_async(request_info, SensitivityLabel, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Calculate the sensitivity label that should be inherited by an output artifact, given a set of sensitivity labels from input or referenced artifacts.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ComputeInheritanceWithLabelIdsWithLocaleWithContentFormatsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ComputeInheritanceWithLabelIdsWithLocaleWithContentFormatsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ComputeInheritanceWithLabelIdsWithLocaleWithContentFormatsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ComputeInheritanceWithLabelIdsWithLocaleWithContentFormatsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

