from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .subject_set import SubjectSet

from .subject_set import SubjectSet

@dataclass
class GroupMembers(SubjectSet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.groupMembers"
    # The name of the group in Microsoft Entra ID. Read only.
    description: Optional[str] = None
    # The ID of the group in Microsoft Entra ID.
    group_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupMembers:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupMembers
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupMembers()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .subject_set import SubjectSet

        from .subject_set import SubjectSet

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "groupId": lambda n : setattr(self, 'group_id', n.get_str_value()),
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
        from .subject_set import SubjectSet

        writer.write_str_value("description", self.description)
        writer.write_str_value("groupId", self.group_id)
    

