from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .share_point_group_member import SharePointGroupMember

from .entity import Entity

@dataclass
class SharePointGroup(Entity, Parsable):
    # The user-visible description of the sharePointGroup. Read-write.
    description: Optional[str] = None
    # The set of members in the sharePointGroup. Read-write.
    members: Optional[list[SharePointGroupMember]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The principal ID of the SharePoint group in the tenant. Read-only.
    principal_id: Optional[str] = None
    # The user-visible title of the sharePointGroup. Read-write.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharePointGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharePointGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharePointGroup()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .share_point_group_member import SharePointGroupMember

        from .entity import Entity
        from .share_point_group_member import SharePointGroupMember

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(SharePointGroupMember)),
            "principalId": lambda n : setattr(self, 'principal_id', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_str_value("principalId", self.principal_id)
        writer.write_str_value("title", self.title)
    

