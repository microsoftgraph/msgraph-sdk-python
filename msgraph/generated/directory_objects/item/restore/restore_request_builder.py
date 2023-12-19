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
    from ....models.directory_object import DirectoryObject
    from ....models.o_data_errors.o_data_error import ODataError

class RestoreRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to call the restore method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new RestoreRequestBuilder and sets the default values.
        param path_parameters: The raw url or the Url template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/directoryObjects/{directoryObject%2Did}/restore", path_parameters)
    
    async def post(self,request_configuration: Optional[RestoreRequestBuilderPostRequestConfiguration] = None) -> Optional[DirectoryObject]:
        """
        Restore a recently deleted application, group, servicePrincipal, administrative unit, or user object from deleted items. If an item was accidentally deleted, you can fully restore the item. However, security groups cannot be restored. Also, restoring an application doesn't restore the associated service principal automatically. You must call this API to explicitly restore the deleted service principal. A recently deleted item remains available for up to 30 days. After 30 days, the item is permanently deleted.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DirectoryObject]
        Find more info here: https://learn.microsoft.com/graph/api/directory-deleteditems-restore?view=graph-rest-1.0
        """
        request_info = self.to_post_request_information(
            request_configuration
        )
        from ....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.directory_object import DirectoryObject

        return await self.request_adapter.send_async(request_info, DirectoryObject, error_mapping)
    
    def to_post_request_information(self,request_configuration: Optional[RestoreRequestBuilderPostRequestConfiguration] = None) -> RequestInformation:
        """
        Restore a recently deleted application, group, servicePrincipal, administrative unit, or user object from deleted items. If an item was accidentally deleted, you can fully restore the item. However, security groups cannot be restored. Also, restoring an application doesn't restore the associated service principal automatically. You must call this API to explicitly restore the deleted service principal. A recently deleted item remains available for up to 30 days. After 30 days, the item is permanently deleted.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        if request_configuration:
            request_info.headers.add_all(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.POST
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> RestoreRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RestoreRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return RestoreRequestBuilder(self.request_adapter, raw_url)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class RestoreRequestBuilderPostRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    

