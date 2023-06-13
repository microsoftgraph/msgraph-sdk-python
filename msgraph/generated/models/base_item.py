from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import drive, drive_item, entity, identity_set, item_reference, list, list_item, shared_drive_item, site, user

from . import entity

@dataclass
class BaseItem(entity.Entity):
    # Identity of the user, device, or application which created the item. Read-only.
    created_by: Optional[identity_set.IdentitySet] = None
    # Identity of the user who created the item. Read-only.
    created_by_user: Optional[user.User] = None
    # Date and time of item creation. Read-only.
    created_date_time: Optional[datetime] = None
    # Provides a user-visible description of the item. Optional.
    description: Optional[str] = None
    # ETag for the item. Read-only.
    e_tag: Optional[str] = None
    # Identity of the user, device, and application which last modified the item. Read-only.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # Identity of the user who last modified the item. Read-only.
    last_modified_by_user: Optional[user.User] = None
    # Date and time the item was last modified. Read-only.
    last_modified_date_time: Optional[datetime] = None
    # The name of the item. Read-write.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Parent information, if the item has a parent. Read-write.
    parent_reference: Optional[item_reference.ItemReference] = None
    # URL that displays the resource in the browser. Read-only.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BaseItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BaseItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.drive":
                from . import drive

                return drive.Drive()
            if mapping_value == "#microsoft.graph.driveItem":
                from . import drive_item

                return drive_item.DriveItem()
            if mapping_value == "#microsoft.graph.list":
                from . import list

                return list.List()
            if mapping_value == "#microsoft.graph.listItem":
                from . import list_item

                return list_item.ListItem()
            if mapping_value == "#microsoft.graph.sharedDriveItem":
                from . import shared_drive_item

                return shared_drive_item.SharedDriveItem()
            if mapping_value == "#microsoft.graph.site":
                from . import site

                return site.Site()
        return BaseItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import drive, drive_item, entity, identity_set, item_reference, list, list_item, shared_drive_item, site, user

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdByUser": lambda n : setattr(self, 'created_by_user', n.get_object_value(user.User)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "eTag": lambda n : setattr(self, 'e_tag', n.get_str_value()),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedByUser": lambda n : setattr(self, 'last_modified_by_user', n.get_object_value(user.User)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parentReference": lambda n : setattr(self, 'parent_reference', n.get_object_value(item_reference.ItemReference)),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_object_value("createdByUser", self.created_by_user)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("eTag", self.e_tag)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_object_value("lastModifiedByUser", self.last_modified_by_user)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_object_value("parentReference", self.parent_reference)
        writer.write_str_value("webUrl", self.web_url)
    

