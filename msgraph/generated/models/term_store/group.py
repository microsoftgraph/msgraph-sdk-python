from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .set import Set
    from .term_group_scope import TermGroupScope

from ..entity import Entity

@dataclass
class Group(Entity):
    # Date and time of the group creation. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Description that gives details on the term usage.
    description: Optional[str] = None
    # Name of the group.
    display_name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # ID of the parent site of this group.
    parent_site_id: Optional[str] = None
    # Returns the type of the group. Possible values are: global, system, and siteCollection.
    scope: Optional[TermGroupScope] = None
    # All sets under the group in a term [store].
    sets: Optional[List[Set]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Group:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Group
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Group()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .set import Set
        from .term_group_scope import TermGroupScope

        from ..entity import Entity
        from .set import Set
        from .term_group_scope import TermGroupScope

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "parentSiteId": lambda n : setattr(self, 'parent_site_id', n.get_str_value()),
            "scope": lambda n : setattr(self, 'scope', n.get_enum_value(TermGroupScope)),
            "sets": lambda n : setattr(self, 'sets', n.get_collection_of_object_values(Set)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("parentSiteId", self.parent_site_id)
        writer.write_enum_value("scope", self.scope)
        writer.write_collection_of_object_values("sets", self.sets)
    

