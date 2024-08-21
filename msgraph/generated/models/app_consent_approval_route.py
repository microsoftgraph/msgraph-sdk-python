from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_consent_request import AppConsentRequest
    from .entity import Entity

from .entity import Entity

@dataclass
class AppConsentApprovalRoute(Entity):
    # A collection of appConsentRequest objects representing apps for which admin consent has been requested by one or more users.
    app_consent_requests: Optional[List[AppConsentRequest]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AppConsentApprovalRoute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AppConsentApprovalRoute
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AppConsentApprovalRoute()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .app_consent_request import AppConsentRequest
        from .entity import Entity

        from .app_consent_request import AppConsentRequest
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "appConsentRequests": lambda n : setattr(self, 'app_consent_requests', n.get_collection_of_object_values(AppConsentRequest)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("appConsentRequests", self.app_consent_requests)
    

