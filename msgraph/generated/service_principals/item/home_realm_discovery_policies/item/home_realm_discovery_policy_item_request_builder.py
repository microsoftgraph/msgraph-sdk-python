from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ref.ref_request_builder import RefRequestBuilder

class HomeRealmDiscoveryPolicyItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /servicePrincipals/{servicePrincipal-id}/homeRealmDiscoveryPolicies/{homeRealmDiscoveryPolicy-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new HomeRealmDiscoveryPolicyItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/servicePrincipals/{servicePrincipal%2Did}/homeRealmDiscoveryPolicies/{homeRealmDiscoveryPolicy%2Did}", path_parameters)
    
    @property
    def ref(self) -> RefRequestBuilder:
        """
        Provides operations to manage the collection of servicePrincipal entities.
        """
        from .ref.ref_request_builder import RefRequestBuilder

        return RefRequestBuilder(self.request_adapter, self.path_parameters)
    

