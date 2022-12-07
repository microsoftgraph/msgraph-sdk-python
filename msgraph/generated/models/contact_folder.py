from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

contact = lazy_import('msgraph.generated.models.contact')
entity = lazy_import('msgraph.generated.models.entity')
multi_value_legacy_extended_property = lazy_import('msgraph.generated.models.multi_value_legacy_extended_property')
single_value_legacy_extended_property = lazy_import('msgraph.generated.models.single_value_legacy_extended_property')

class ContactFolder(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def child_folders(self,) -> Optional[List[ContactFolder]]:
        """
        Gets the childFolders property value. The collection of child folders in the folder. Navigation property. Read-only. Nullable.
        Returns: Optional[List[ContactFolder]]
        """
        return self._child_folders
    
    @child_folders.setter
    def child_folders(self,value: Optional[List[ContactFolder]] = None) -> None:
        """
        Sets the childFolders property value. The collection of child folders in the folder. Navigation property. Read-only. Nullable.
        Args:
            value: Value to set for the childFolders property.
        """
        self._child_folders = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new contactFolder and sets the default values.
        """
        super().__init__()
        # The collection of child folders in the folder. Navigation property. Read-only. Nullable.
        self._child_folders: Optional[List[ContactFolder]] = None
        # The contacts in the folder. Navigation property. Read-only. Nullable.
        self._contacts: Optional[List[contact.Contact]] = None
        # The folder's display name.
        self._display_name: Optional[str] = None
        # The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.
        self._multi_value_extended_properties: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The ID of the folder's parent folder.
        self._parent_folder_id: Optional[str] = None
        # The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.
        self._single_value_extended_properties: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None
    
    @property
    def contacts(self,) -> Optional[List[contact.Contact]]:
        """
        Gets the contacts property value. The contacts in the folder. Navigation property. Read-only. Nullable.
        Returns: Optional[List[contact.Contact]]
        """
        return self._contacts
    
    @contacts.setter
    def contacts(self,value: Optional[List[contact.Contact]] = None) -> None:
        """
        Sets the contacts property value. The contacts in the folder. Navigation property. Read-only. Nullable.
        Args:
            value: Value to set for the contacts property.
        """
        self._contacts = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ContactFolder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ContactFolder
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ContactFolder()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The folder's display name.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The folder's display name.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "child_folders": lambda n : setattr(self, 'child_folders', n.get_collection_of_object_values(ContactFolder)),
            "contacts": lambda n : setattr(self, 'contacts', n.get_collection_of_object_values(contact.Contact)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "multi_value_extended_properties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty)),
            "parent_folder_id": lambda n : setattr(self, 'parent_folder_id', n.get_str_value()),
            "single_value_extended_properties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(single_value_legacy_extended_property.SingleValueLegacyExtendedProperty)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def multi_value_extended_properties(self,) -> Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]:
        """
        Gets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.
        Returns: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]]
        """
        return self._multi_value_extended_properties
    
    @multi_value_extended_properties.setter
    def multi_value_extended_properties(self,value: Optional[List[multi_value_legacy_extended_property.MultiValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the multiValueExtendedProperties property value. The collection of multi-value extended properties defined for the contactFolder. Read-only. Nullable.
        Args:
            value: Value to set for the multiValueExtendedProperties property.
        """
        self._multi_value_extended_properties = value
    
    @property
    def parent_folder_id(self,) -> Optional[str]:
        """
        Gets the parentFolderId property value. The ID of the folder's parent folder.
        Returns: Optional[str]
        """
        return self._parent_folder_id
    
    @parent_folder_id.setter
    def parent_folder_id(self,value: Optional[str] = None) -> None:
        """
        Sets the parentFolderId property value. The ID of the folder's parent folder.
        Args:
            value: Value to set for the parentFolderId property.
        """
        self._parent_folder_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("childFolders", self.child_folders)
        writer.write_collection_of_object_values("contacts", self.contacts)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("multiValueExtendedProperties", self.multi_value_extended_properties)
        writer.write_str_value("parentFolderId", self.parent_folder_id)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
    
    @property
    def single_value_extended_properties(self,) -> Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]:
        """
        Gets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.
        Returns: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]]
        """
        return self._single_value_extended_properties
    
    @single_value_extended_properties.setter
    def single_value_extended_properties(self,value: Optional[List[single_value_legacy_extended_property.SingleValueLegacyExtendedProperty]] = None) -> None:
        """
        Sets the singleValueExtendedProperties property value. The collection of single-value extended properties defined for the contactFolder. Read-only. Nullable.
        Args:
            value: Value to set for the singleValueExtendedProperties property.
        """
        self._single_value_extended_properties = value
    

