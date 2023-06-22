from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import email_address, entity, inference_classification_type

from . import entity

@dataclass
class InferenceClassificationOverride(entity.Entity):
    # Specifies how incoming messages from a specific sender should always be classified as. The possible values are: focused, other.
    classify_as: Optional[inference_classification_type.InferenceClassificationType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The email address information of the sender for whom the override is created.
    sender_email_address: Optional[email_address.EmailAddress] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InferenceClassificationOverride:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InferenceClassificationOverride
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return InferenceClassificationOverride()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import email_address, entity, inference_classification_type

        from . import email_address, entity, inference_classification_type

        fields: Dict[str, Callable[[Any], None]] = {
            "classifyAs": lambda n : setattr(self, 'classify_as', n.get_enum_value(inference_classification_type.InferenceClassificationType)),
            "senderEmailAddress": lambda n : setattr(self, 'sender_email_address', n.get_object_value(email_address.EmailAddress)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("classifyAs", self.classify_as)
        writer.write_object_value("senderEmailAddress", self.sender_email_address)
    

