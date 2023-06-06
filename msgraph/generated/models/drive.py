from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import base_item, drive_item, identity_set, list, quota, sharepoint_ids, system_facet

from . import base_item

@dataclass
class Drive(base_item.BaseItem):
    odata_type = "#microsoft.graph.drive"
    # Collection of [bundles][bundle] (albums and multi-select-shared sets of items). Only in personal OneDrive.
    bundles: Optional[List[drive_item.DriveItem]] = None
    # Describes the type of drive represented by this resource. OneDrive personal drives will return personal. OneDrive for Business will return business. SharePoint document libraries will return documentLibrary. Read-only.
    drive_type: Optional[str] = None
    # The list of items the user is following. Only in OneDrive for Business.
    following: Optional[List[drive_item.DriveItem]] = None
    # All items contained in the drive. Read-only. Nullable.
    items: Optional[List[drive_item.DriveItem]] = None
    # For drives in SharePoint, the underlying document library list. Read-only. Nullable.
    list: Optional[list.List] = None
    # Optional. The user account that owns the drive. Read-only.
    owner: Optional[identity_set.IdentitySet] = None
    # Optional. Information about the drive's storage space quota. Read-only.
    quota: Optional[quota.Quota] = None
    # The root folder of the drive. Read-only.
    root: Optional[drive_item.DriveItem] = None
    # The sharePointIds property
    share_point_ids: Optional[sharepoint_ids.SharepointIds] = None
    # Collection of common folders available in OneDrive. Read-only. Nullable.
    special: Optional[List[drive_item.DriveItem]] = None
    # If present, indicates that this is a system-managed drive. Read-only.
    system: Optional[system_facet.SystemFacet] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Drive:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Drive
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Drive()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import base_item, drive_item, identity_set, list, quota, sharepoint_ids, system_facet

        fields: Dict[str, Callable[[Any], None]] = {
            "bundles": lambda n : setattr(self, 'bundles', n.get_collection_of_object_values(drive_item.DriveItem)),
            "driveType": lambda n : setattr(self, 'drive_type', n.get_str_value()),
            "following": lambda n : setattr(self, 'following', n.get_collection_of_object_values(drive_item.DriveItem)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(drive_item.DriveItem)),
            "list": lambda n : setattr(self, 'list', n.get_object_value(list.List)),
            "owner": lambda n : setattr(self, 'owner', n.get_object_value(identity_set.IdentitySet)),
            "quota": lambda n : setattr(self, 'quota', n.get_object_value(quota.Quota)),
            "root": lambda n : setattr(self, 'root', n.get_object_value(drive_item.DriveItem)),
            "sharePointIds": lambda n : setattr(self, 'share_point_ids', n.get_object_value(sharepoint_ids.SharepointIds)),
            "special": lambda n : setattr(self, 'special', n.get_collection_of_object_values(drive_item.DriveItem)),
            "system": lambda n : setattr(self, 'system', n.get_object_value(system_facet.SystemFacet)),
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
        writer.write_collection_of_object_values("bundles", self.bundles)
        writer.write_str_value("driveType", self.drive_type)
        writer.write_collection_of_object_values("following", self.following)
        writer.write_collection_of_object_values("items", self.items)
        writer.write_object_value("list", self.list)
        writer.write_object_value("owner", self.owner)
        writer.write_object_value("quota", self.quota)
        writer.write_object_value("root", self.root)
        writer.write_object_value("sharePointIds", self.share_point_ids)
        writer.write_collection_of_object_values("special", self.special)
        writer.write_object_value("system", self.system)
    

