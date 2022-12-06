from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

app_consent_request = lazy_import('msgraph.generated.models.app_consent_request')
entity = lazy_import('msgraph.generated.models.entity')

class AppConsentApprovalRoute(entity.Entity):
    @property
    def app_consent_requests(self,) -> Optional[List[app_consent_request.AppConsentRequest]]:
        """
        Gets the appConsentRequests property value. A collection of userConsentRequest objects for a specific application.
        Returns: Optional[List[app_consent_request.AppConsentRequest]]
        """
        return self._app_consent_requests
    
    @app_consent_requests.setter
    def app_consent_requests(self,value: Optional[List[app_consent_request.AppConsentRequest]] = None) -> None:
        """
        Sets the appConsentRequests property value. A collection of userConsentRequest objects for a specific application.
        Args:
            value: Value to set for the appConsentRequests property.
        """
        self._app_consent_requests = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new AppConsentApprovalRoute and sets the default values.
        """
        super().__init__()
        # A collection of userConsentRequest objects for a specific application.
        self._app_consent_requests: Optional[List[app_consent_request.AppConsentRequest]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AppConsentApprovalRoute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AppConsentApprovalRoute
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AppConsentApprovalRoute()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_consent_requests": lambda n : setattr(self, 'app_consent_requests', n.get_collection_of_object_values(app_consent_request.AppConsentRequest)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("appConsentRequests", self.app_consent_requests)
    

