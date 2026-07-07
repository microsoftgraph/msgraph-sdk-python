from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .analyzed_email import AnalyzedEmail

from ..entity import Entity

@dataclass
class CollaborationRoot(Entity, Parsable):
    # Contains metadata for analyzed emails.
    analyzed_emails: Optional[list[AnalyzedEmail]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CollaborationRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CollaborationRoot
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CollaborationRoot()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .analyzed_email import AnalyzedEmail

        from ..entity import Entity
        from .analyzed_email import AnalyzedEmail

        fields: dict[str, Callable[[Any], None]] = {
            "analyzedEmails": lambda n : setattr(self, 'analyzed_emails', n.get_collection_of_object_values(AnalyzedEmail)),
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
        writer.write_collection_of_object_values("analyzedEmails", self.analyzed_emails)
    

