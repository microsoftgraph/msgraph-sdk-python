from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

base_item = lazy_import('msgraph.generated.models.base_item')
drive_item = lazy_import('msgraph.generated.models.drive_item')
identity_set = lazy_import('msgraph.generated.models.identity_set')
list = lazy_import('msgraph.generated.models.list')
quota = lazy_import('msgraph.generated.models.quota')
sharepoint_ids = lazy_import('msgraph.generated.models.sharepoint_ids')
system_facet = lazy_import('msgraph.generated.models.system_facet')

class Drive(base_item.BaseItem):
    @property
    def bundles(self,) -> Optional[List[drive_item.DriveItem]]:
        """
        Gets the bundles property value. Collection of [bundles][bundle] (albums and multi-select-shared sets of items). Only in personal OneDrive.
        Returns: Optional[List[drive_item.DriveItem]]
        """
        return self._bundles
    
    @bundles.setter
    def bundles(self,value: Optional[List[drive_item.DriveItem]] = None) -> None:
        """
        Sets the bundles property value. Collection of [bundles][bundle] (albums and multi-select-shared sets of items). Only in personal OneDrive.
        Args:
            value: Value to set for the bundles property.
        """
        self._bundles = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new Drive and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.drive"
        # Collection of [bundles][bundle] (albums and multi-select-shared sets of items). Only in personal OneDrive.
        self._bundles: Optional[List[drive_item.DriveItem]] = None
        # Describes the type of drive represented by this resource. OneDrive personal drives will return personal. OneDrive for Business will return business. SharePoint document libraries will return documentLibrary. Read-only.
        self._drive_type: Optional[str] = None
        # The list of items the user is following. Only in OneDrive for Business.
        self._following: Optional[List[drive_item.DriveItem]] = None
        # All items contained in the drive. Read-only. Nullable.
        self._items: Optional[List[drive_item.DriveItem]] = None
        # For drives in SharePoint, the underlying document library list. Read-only. Nullable.
        self._list: Optional[list.List] = None
        # Optional. The user account that owns the drive. Read-only.
        self._owner: Optional[identity_set.IdentitySet] = None
        # Optional. Information about the drive's storage space quota. Read-only.
        self._quota: Optional[quota.Quota] = None
        # The root folder of the drive. Read-only.
        self._root: Optional[drive_item.DriveItem] = None
        # The sharePointIds property
        self._share_point_ids: Optional[sharepoint_ids.SharepointIds] = None
        # Collection of common folders available in OneDrive. Read-only. Nullable.
        self._special: Optional[List[drive_item.DriveItem]] = None
        # If present, indicates that this is a system-managed drive. Read-only.
        self._system: Optional[system_facet.SystemFacet] = None
    
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
    
    @property
    def drive_type(self,) -> Optional[str]:
        """
        Gets the driveType property value. Describes the type of drive represented by this resource. OneDrive personal drives will return personal. OneDrive for Business will return business. SharePoint document libraries will return documentLibrary. Read-only.
        Returns: Optional[str]
        """
        return self._drive_type
    
    @drive_type.setter
    def drive_type(self,value: Optional[str] = None) -> None:
        """
        Sets the driveType property value. Describes the type of drive represented by this resource. OneDrive personal drives will return personal. OneDrive for Business will return business. SharePoint document libraries will return documentLibrary. Read-only.
        Args:
            value: Value to set for the driveType property.
        """
        self._drive_type = value
    
    @property
    def following(self,) -> Optional[List[drive_item.DriveItem]]:
        """
        Gets the following property value. The list of items the user is following. Only in OneDrive for Business.
        Returns: Optional[List[drive_item.DriveItem]]
        """
        return self._following
    
    @following.setter
    def following(self,value: Optional[List[drive_item.DriveItem]] = None) -> None:
        """
        Sets the following property value. The list of items the user is following. Only in OneDrive for Business.
        Args:
            value: Value to set for the following property.
        """
        self._following = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "bundles": lambda n : setattr(self, 'bundles', n.get_collection_of_object_values(drive_item.DriveItem)),
            "drive_type": lambda n : setattr(self, 'drive_type', n.get_str_value()),
            "following": lambda n : setattr(self, 'following', n.get_collection_of_object_values(drive_item.DriveItem)),
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(drive_item.DriveItem)),
            "list": lambda n : setattr(self, 'list', n.get_object_value(list.List)),
            "owner": lambda n : setattr(self, 'owner', n.get_object_value(identity_set.IdentitySet)),
            "quota": lambda n : setattr(self, 'quota', n.get_object_value(quota.Quota)),
            "root": lambda n : setattr(self, 'root', n.get_object_value(drive_item.DriveItem)),
            "share_point_ids": lambda n : setattr(self, 'share_point_ids', n.get_object_value(sharepoint_ids.SharepointIds)),
            "special": lambda n : setattr(self, 'special', n.get_collection_of_object_values(drive_item.DriveItem)),
            "system": lambda n : setattr(self, 'system', n.get_object_value(system_facet.SystemFacet)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def items(self,) -> Optional[List[drive_item.DriveItem]]:
        """
        Gets the items property value. All items contained in the drive. Read-only. Nullable.
        Returns: Optional[List[drive_item.DriveItem]]
        """
        return self._items
    
    @items.setter
    def items(self,value: Optional[List[drive_item.DriveItem]] = None) -> None:
        """
        Sets the items property value. All items contained in the drive. Read-only. Nullable.
        Args:
            value: Value to set for the items property.
        """
        self._items = value
    
    @property
    def list(self,) -> Optional[list.List]:
        """
        Gets the list property value. For drives in SharePoint, the underlying document library list. Read-only. Nullable.
        Returns: Optional[list.List]
        """
        return self._list
    
    @list.setter
    def list(self,value: Optional[list.List] = None) -> None:
        """
        Sets the list property value. For drives in SharePoint, the underlying document library list. Read-only. Nullable.
        Args:
            value: Value to set for the list property.
        """
        self._list = value
    
    @property
    def owner(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the owner property value. Optional. The user account that owns the drive. Read-only.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._owner
    
    @owner.setter
    def owner(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the owner property value. Optional. The user account that owns the drive. Read-only.
        Args:
            value: Value to set for the owner property.
        """
        self._owner = value
    
    @property
    def quota(self,) -> Optional[quota.Quota]:
        """
        Gets the quota property value. Optional. Information about the drive's storage space quota. Read-only.
        Returns: Optional[quota.Quota]
        """
        return self._quota
    
    @quota.setter
    def quota(self,value: Optional[quota.Quota] = None) -> None:
        """
        Sets the quota property value. Optional. Information about the drive's storage space quota. Read-only.
        Args:
            value: Value to set for the quota property.
        """
        self._quota = value
    
    @property
    def root(self,) -> Optional[drive_item.DriveItem]:
        """
        Gets the root property value. The root folder of the drive. Read-only.
        Returns: Optional[drive_item.DriveItem]
        """
        return self._root
    
    @root.setter
    def root(self,value: Optional[drive_item.DriveItem] = None) -> None:
        """
        Sets the root property value. The root folder of the drive. Read-only.
        Args:
            value: Value to set for the root property.
        """
        self._root = value
    
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
    
    @property
    def share_point_ids(self,) -> Optional[sharepoint_ids.SharepointIds]:
        """
        Gets the sharePointIds property value. The sharePointIds property
        Returns: Optional[sharepoint_ids.SharepointIds]
        """
        return self._share_point_ids
    
    @share_point_ids.setter
    def share_point_ids(self,value: Optional[sharepoint_ids.SharepointIds] = None) -> None:
        """
        Sets the sharePointIds property value. The sharePointIds property
        Args:
            value: Value to set for the sharePointIds property.
        """
        self._share_point_ids = value
    
    @property
    def special(self,) -> Optional[List[drive_item.DriveItem]]:
        """
        Gets the special property value. Collection of common folders available in OneDrive. Read-only. Nullable.
        Returns: Optional[List[drive_item.DriveItem]]
        """
        return self._special
    
    @special.setter
    def special(self,value: Optional[List[drive_item.DriveItem]] = None) -> None:
        """
        Sets the special property value. Collection of common folders available in OneDrive. Read-only. Nullable.
        Args:
            value: Value to set for the special property.
        """
        self._special = value
    
    @property
    def system(self,) -> Optional[system_facet.SystemFacet]:
        """
        Gets the system property value. If present, indicates that this is a system-managed drive. Read-only.
        Returns: Optional[system_facet.SystemFacet]
        """
        return self._system
    
    @system.setter
    def system(self,value: Optional[system_facet.SystemFacet] = None) -> None:
        """
        Sets the system property value. If present, indicates that this is a system-managed drive. Read-only.
        Args:
            value: Value to set for the system property.
        """
        self._system = value
    

