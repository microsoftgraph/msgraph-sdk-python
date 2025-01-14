from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .base_item import BaseItem
    from .drive_item import DriveItem
    from .identity_set import IdentitySet
    from .list_ import List_
    from .list_item import ListItem
    from .permission import Permission
    from .site import Site

from .base_item import BaseItem

@dataclass
class SharedDriveItem(BaseItem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.sharedDriveItem"
    # Used to access the underlying driveItem
    drive_item: Optional[DriveItem] = None
    # All driveItems contained in the sharing root. This collection cannot be enumerated.
    items: Optional[list[DriveItem]] = None
    # Used to access the underlying list
    list_: Optional[List_] = None
    # Used to access the underlying listItem
    list_item: Optional[ListItem] = None
    # Information about the owner of the shared item being referenced.
    owner: Optional[IdentitySet] = None
    # Used to access the permission representing the underlying sharing link
    permission: Optional[Permission] = None
    # Used to access the underlying driveItem. Deprecated -- use driveItem instead.
    root: Optional[DriveItem] = None
    # Used to access the underlying site
    site: Optional[Site] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SharedDriveItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SharedDriveItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SharedDriveItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .base_item import BaseItem
        from .drive_item import DriveItem
        from .identity_set import IdentitySet
        from .list_ import List_
        from .list_item import ListItem
        from .permission import Permission
        from .site import Site

        from .base_item import BaseItem
        from .drive_item import DriveItem
        from .identity_set import IdentitySet
        from .list_ import List_
        from .list_item import ListItem
        from .permission import Permission
        from .site import Site

        fields: dict[str, Callable[[Any], None]] = {
            "driveItem": lambda n : setattr(self, 'drive_item', n.get_object_value(DriveItem)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(DriveItem)),
            "list": lambda n : setattr(self, 'list_', n.get_object_value(List_)),
            "listItem": lambda n : setattr(self, 'list_item', n.get_object_value(ListItem)),
            "owner": lambda n : setattr(self, 'owner', n.get_object_value(IdentitySet)),
            "permission": lambda n : setattr(self, 'permission', n.get_object_value(Permission)),
            "root": lambda n : setattr(self, 'root', n.get_object_value(DriveItem)),
            "site": lambda n : setattr(self, 'site', n.get_object_value(Site)),
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
        writer.write_object_value("driveItem", self.drive_item)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_object_value("list", self.list_)
        writer.write_object_value("listItem", self.list_item)
        writer.write_object_value("owner", self.owner)
        writer.write_object_value("permission", self.permission)
        writer.write_object_value("root", self.root)
        writer.write_object_value("site", self.site)
    

