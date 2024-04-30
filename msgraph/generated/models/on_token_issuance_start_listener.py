from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_event_listener import AuthenticationEventListener
    from .on_token_issuance_start_handler import OnTokenIssuanceStartHandler

from .authentication_event_listener import AuthenticationEventListener

@dataclass
class OnTokenIssuanceStartListener(AuthenticationEventListener):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onTokenIssuanceStartListener"
    # The handler to invoke when conditions are met for this onTokenIssuanceStartListener.
    handler: Optional[OnTokenIssuanceStartHandler] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnTokenIssuanceStartListener:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnTokenIssuanceStartListener
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OnTokenIssuanceStartListener()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_event_listener import AuthenticationEventListener
        from .on_token_issuance_start_handler import OnTokenIssuanceStartHandler

        from .authentication_event_listener import AuthenticationEventListener
        from .on_token_issuance_start_handler import OnTokenIssuanceStartHandler

        fields: Dict[str, Callable[[Any], None]] = {
            "handler": lambda n : setattr(self, 'handler', n.get_object_value(OnTokenIssuanceStartHandler)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("handler", self.handler)
    

