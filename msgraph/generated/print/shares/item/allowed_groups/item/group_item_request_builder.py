from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ref.ref_request_builder import RefRequestBuilder
    from .service_provisioning_errors.service_provisioning_errors_request_builder import ServiceProvisioningErrorsRequestBuilder

class GroupItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /print/shares/{printerShare-id}/allowedGroups/{group-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new GroupItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/print/shares/{printerShare%2Did}/allowedGroups/{group%2Did}", path_parameters)
    
    @property
    def ref(self) -> RefRequestBuilder:
        """
        Provides operations to manage the collection of print entities.
        """
        from .ref.ref_request_builder import RefRequestBuilder

        return RefRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_provisioning_errors(self) -> ServiceProvisioningErrorsRequestBuilder:
        """
        The serviceProvisioningErrors property
        """
        from .service_provisioning_errors.service_provisioning_errors_request_builder import ServiceProvisioningErrorsRequestBuilder

        return ServiceProvisioningErrorsRequestBuilder(self.request_adapter, self.path_parameters)
    

