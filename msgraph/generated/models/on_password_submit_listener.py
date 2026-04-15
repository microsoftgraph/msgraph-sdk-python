from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_event_listener import AuthenticationEventListener
    from .on_password_submit_handler import OnPasswordSubmitHandler

from .authentication_event_listener import AuthenticationEventListener

@dataclass
class OnPasswordSubmitListener(AuthenticationEventListener, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onPasswordSubmitListener"
    # Configuration for the handler to invoke when this listener is triggered. For JIT migration scenarios, this is typically an onPasswordMigrationCustomExtensionHandler.
    handler: Optional[OnPasswordSubmitHandler] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnPasswordSubmitListener:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnPasswordSubmitListener
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnPasswordSubmitListener()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_event_listener import AuthenticationEventListener
        from .on_password_submit_handler import OnPasswordSubmitHandler

        from .authentication_event_listener import AuthenticationEventListener
        from .on_password_submit_handler import OnPasswordSubmitHandler

        fields: dict[str, Callable[[Any], None]] = {
            "handler": lambda n : setattr(self, 'handler', n.get_object_value(OnPasswordSubmitHandler)),
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
        writer.write_object_value("handler", self.handler)
    

