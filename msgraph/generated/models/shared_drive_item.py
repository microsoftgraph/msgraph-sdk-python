from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import base_item, drive_item, identity_set, list, list_item, permission, site

from . import base_item

@dataclass
class SharedDriveItem(base_item.BaseItem):
    odata_type = "#microsoft.graph.sharedDriveItem"
    # Used to access the underlying driveItem
    drive_item: Optional[drive_item.DriveItem] = None
    # All driveItems contained in the sharing root. This collection cannot be enumerated.
    items: Optional[List[drive_item.DriveItem]] = None
    # Used to access the underlying list
    list: Optional[list.List] = None
    # Used to access the underlying listItem
    list_item: Optional[list_item.ListItem] = None
    # Information about the owner of the shared item being referenced.
    owner: Optional[identity_set.IdentitySet] = None
    # Used to access the permission representing the underlying sharing link
    permission: Optional[permission.Permission] = None
    # Used to access the underlying driveItem. Deprecated -- use driveItem instead.
    root: Optional[drive_item.DriveItem] = None
    # Used to access the underlying site
    site: Optional[site.Site] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SharedDriveItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SharedDriveItem
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SharedDriveItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import base_item, drive_item, identity_set, list, list_item, permission, site

        from . import base_item, drive_item, identity_set, list, list_item, permission, site

        fields: Dict[str, Callable[[Any], None]] = {
            "driveItem": lambda n : setattr(self, 'drive_item', n.get_object_value(drive_item.DriveItem)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(drive_item.DriveItem)),
            "list": lambda n : setattr(self, 'list', n.get_object_value(list.List)),
            "listItem": lambda n : setattr(self, 'list_item', n.get_object_value(list_item.ListItem)),
            "owner": lambda n : setattr(self, 'owner', n.get_object_value(identity_set.IdentitySet)),
            "permission": lambda n : setattr(self, 'permission', n.get_object_value(permission.Permission)),
            "root": lambda n : setattr(self, 'root', n.get_object_value(drive_item.DriveItem)),
            "site": lambda n : setattr(self, 'site', n.get_object_value(site.Site)),
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
        writer.write_object_value("driveItem", self.drive_item)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_object_value("list", self.list)
        writer.write_object_value("listItem", self.list_item)
        writer.write_object_value("owner", self.owner)
        writer.write_object_value("permission", self.permission)
        writer.write_object_value("root", self.root)
        writer.write_object_value("site", self.site)
    

