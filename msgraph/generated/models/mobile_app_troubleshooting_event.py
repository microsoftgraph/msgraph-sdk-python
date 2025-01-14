from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .app_log_collection_request import AppLogCollectionRequest
    from .entity import Entity

from .entity import Entity

@dataclass
class MobileAppTroubleshootingEvent(Entity, Parsable):
    # Indicates collection of App Log Upload Request.
    app_log_collection_requests: Optional[list[AppLogCollectionRequest]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppTroubleshootingEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppTroubleshootingEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileAppTroubleshootingEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .app_log_collection_request import AppLogCollectionRequest
        from .entity import Entity

        from .app_log_collection_request import AppLogCollectionRequest
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "appLogCollectionRequests": lambda n : setattr(self, 'app_log_collection_requests', n.get_collection_of_object_values(AppLogCollectionRequest)),
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
        writer.write_collection_of_object_values("appLogCollectionRequests", self.app_log_collection_requests)
    

