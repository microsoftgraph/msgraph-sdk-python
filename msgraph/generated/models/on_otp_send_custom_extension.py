from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_authentication_extension import CustomAuthenticationExtension

from .custom_authentication_extension import CustomAuthenticationExtension

@dataclass
class OnOtpSendCustomExtension(CustomAuthenticationExtension, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onOtpSendCustomExtension"
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnOtpSendCustomExtension:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnOtpSendCustomExtension
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OnOtpSendCustomExtension()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_authentication_extension import CustomAuthenticationExtension

        from .custom_authentication_extension import CustomAuthenticationExtension

        fields: dict[str, Callable[[Any], None]] = {
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
    

