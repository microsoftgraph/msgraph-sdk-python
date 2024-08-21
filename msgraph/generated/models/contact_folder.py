from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .contact import Contact
    from .entity import Entity
    from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
    from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

from .entity import Entity

@dataclass
class ContactFolder(Entity):
    # The collection of child folders in the folder. Navigation property. Read-only. Nullable.
    child_folders: Optional[List[ContactFolder]] = None
    # The contacts in the folder. Navigation property. Read-only. Nullable.
    contacts: Optional[List[Contact]] = None
    # The folder's display name.
    display_name: Optional[str] = None
    # The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.
    multi_value_extended_properties: Optional[List[MultiValueLegacyExtendedProperty]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The ID of the folder's parent folder.
    parent_folder_id: Optional[str] = None
    # The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.
    single_value_extended_properties: Optional[List[SingleValueLegacyExtendedProperty]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContactFolder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContactFolder
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContactFolder()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .contact import Contact
        from .entity import Entity
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        from .contact import Contact
        from .entity import Entity
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        fields: Dict[str, Callable[[Any], None]] = {
            "childFolders": lambda n : setattr(self, 'child_folders', n.get_collection_of_object_values(ContactFolder)),
            "contacts": lambda n : setattr(self, 'contacts', n.get_collection_of_object_values(Contact)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "multiValueExtendedProperties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(MultiValueLegacyExtendedProperty)),
            "parentFolderId": lambda n : setattr(self, 'parent_folder_id', n.get_str_value()),
            "singleValueExtendedProperties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(SingleValueLegacyExtendedProperty)),
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
        writer.write_collection_of_object_values("childFolders", self.child_folders)
        writer.write_collection_of_object_values("contacts", self.contacts)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("multiValueExtendedProperties", self.multi_value_extended_properties)
        writer.write_str_value("parentFolderId", self.parent_folder_id)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
    

