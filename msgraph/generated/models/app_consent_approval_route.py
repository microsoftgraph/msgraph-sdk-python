from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_consent_request, entity

from . import entity

@dataclass
class AppConsentApprovalRoute(entity.Entity):
    # A collection of userConsentRequest objects for a specific application.
    app_consent_requests: Optional[List[app_consent_request.AppConsentRequest]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
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
        from . import app_consent_request, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "appConsentRequests": lambda n : setattr(self, 'app_consent_requests', n.get_collection_of_object_values(app_consent_request.AppConsentRequest)),
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
    

