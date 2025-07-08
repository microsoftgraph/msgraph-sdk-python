from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .process_content_request import ProcessContentRequest

from .entity import Entity

@dataclass
class ContentActivity(Entity, Parsable):
    # The contentMetadata property
    content_metadata: Optional[ProcessContentRequest] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The scope identified from computed protection scopes.
    scope_identifier: Optional[str] = None
    # ID of the user.
    user_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentActivity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContentActivity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .process_content_request import ProcessContentRequest

        from .entity import Entity
        from .process_content_request import ProcessContentRequest

        fields: dict[str, Callable[[Any], None]] = {
            "contentMetadata": lambda n : setattr(self, 'content_metadata', n.get_object_value(ProcessContentRequest)),
            "scopeIdentifier": lambda n : setattr(self, 'scope_identifier', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
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
        writer.write_object_value("contentMetadata", self.content_metadata)
        writer.write_str_value("scopeIdentifier", self.scope_identifier)
        writer.write_str_value("userId", self.user_id)
    

