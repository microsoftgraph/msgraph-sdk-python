from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identity_set import IdentitySet
    from .notebook import Notebook
    from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
    from .onenote_section import OnenoteSection
    from .section_group import SectionGroup

from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel

@dataclass
class OnenoteEntityHierarchyModel(OnenoteEntitySchemaObjectModel, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.onenoteEntityHierarchyModel"
    # Identity of the user, device, and application that created the item. Read-only.
    created_by: Optional[IdentitySet] = None
    # The name of the notebook.
    display_name: Optional[str] = None
    # Identity of the user, device, and application that created the item. Read-only.
    last_modified_by: Optional[IdentitySet] = None
    # The date and time when the notebook was last modified. The timestamp represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    last_modified_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OnenoteEntityHierarchyModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OnenoteEntityHierarchyModel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.notebook".casefold():
            from .notebook import Notebook

            return Notebook()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.onenoteSection".casefold():
            from .onenote_section import OnenoteSection

            return OnenoteSection()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sectionGroup".casefold():
            from .section_group import SectionGroup

            return SectionGroup()
        return OnenoteEntityHierarchyModel()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identity_set import IdentitySet
        from .notebook import Notebook
        from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
        from .onenote_section import OnenoteSection
        from .section_group import SectionGroup

        from .identity_set import IdentitySet
        from .notebook import Notebook
        from .onenote_entity_schema_object_model import OnenoteEntitySchemaObjectModel
        from .onenote_section import OnenoteSection
        from .section_group import SectionGroup

        fields: dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(IdentitySet)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
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
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
    

