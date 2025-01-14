from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .email_address import EmailAddress
    from .entity import Entity
    from .inference_classification_type import InferenceClassificationType

from .entity import Entity

@dataclass
class InferenceClassificationOverride(Entity, Parsable):
    # Specifies how incoming messages from a specific sender should always be classified as. The possible values are: focused, other.
    classify_as: Optional[InferenceClassificationType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The email address information of the sender for whom the override is created.
    sender_email_address: Optional[EmailAddress] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InferenceClassificationOverride:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InferenceClassificationOverride
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InferenceClassificationOverride()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .email_address import EmailAddress
        from .entity import Entity
        from .inference_classification_type import InferenceClassificationType

        from .email_address import EmailAddress
        from .entity import Entity
        from .inference_classification_type import InferenceClassificationType

        fields: dict[str, Callable[[Any], None]] = {
            "classifyAs": lambda n : setattr(self, 'classify_as', n.get_enum_value(InferenceClassificationType)),
            "senderEmailAddress": lambda n : setattr(self, 'sender_email_address', n.get_object_value(EmailAddress)),
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
        writer.write_enum_value("classifyAs", self.classify_as)
        writer.write_object_value("senderEmailAddress", self.sender_email_address)
    

