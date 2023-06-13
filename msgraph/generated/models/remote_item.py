from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import file, file_system_info, folder, identity_set, image, item_reference, package, shared, sharepoint_ids, special_folder, video

@dataclass
class RemoteItem(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Identity of the user, device, and application which created the item. Read-only.
    created_by: Optional[identity_set.IdentitySet] = None
    # Date and time of item creation. Read-only.
    created_date_time: Optional[datetime] = None
    # Indicates that the remote item is a file. Read-only.
    file: Optional[file.File] = None
    # Information about the remote item from the local file system. Read-only.
    file_system_info: Optional[file_system_info.FileSystemInfo] = None
    # Indicates that the remote item is a folder. Read-only.
    folder: Optional[folder.Folder] = None
    # Unique identifier for the remote item in its drive. Read-only.
    id: Optional[str] = None
    # Image metadata, if the item is an image. Read-only.
    image: Optional[image.Image] = None
    # Identity of the user, device, and application which last modified the item. Read-only.
    last_modified_by: Optional[identity_set.IdentitySet] = None
    # Date and time the item was last modified. Read-only.
    last_modified_date_time: Optional[datetime] = None
    # Optional. Filename of the remote item. Read-only.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # If present, indicates that this item is a package instead of a folder or file. Packages are treated like files in some contexts and folders in others. Read-only.
    package: Optional[package.Package] = None
    # Properties of the parent of the remote item. Read-only.
    parent_reference: Optional[item_reference.ItemReference] = None
    # Indicates that the item has been shared with others and provides information about the shared state of the item. Read-only.
    shared: Optional[shared.Shared] = None
    # Provides interop between items in OneDrive for Business and SharePoint with the full set of item identifiers. Read-only.
    sharepoint_ids: Optional[sharepoint_ids.SharepointIds] = None
    # Size of the remote item. Read-only.
    size: Optional[int] = None
    # If the current item is also available as a special folder, this facet is returned. Read-only.
    special_folder: Optional[special_folder.SpecialFolder] = None
    # Video metadata, if the item is a video. Read-only.
    video: Optional[video.Video] = None
    # DAV compatible URL for the item.
    web_dav_url: Optional[str] = None
    # URL that displays the resource in the browser. Read-only.
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RemoteItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RemoteItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RemoteItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import file, file_system_info, folder, identity_set, image, item_reference, package, shared, sharepoint_ids, special_folder, video

        fields: Dict[str, Callable[[Any], None]] = {
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "file": lambda n : setattr(self, 'file', n.get_object_value(file.File)),
            "fileSystemInfo": lambda n : setattr(self, 'file_system_info', n.get_object_value(file_system_info.FileSystemInfo)),
            "folder": lambda n : setattr(self, 'folder', n.get_object_value(folder.Folder)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "image": lambda n : setattr(self, 'image', n.get_object_value(image.Image)),
            "lastModifiedBy": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "package": lambda n : setattr(self, 'package', n.get_object_value(package.Package)),
            "parentReference": lambda n : setattr(self, 'parent_reference', n.get_object_value(item_reference.ItemReference)),
            "shared": lambda n : setattr(self, 'shared', n.get_object_value(shared.Shared)),
            "sharepointIds": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(sharepoint_ids.SharepointIds)),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "specialFolder": lambda n : setattr(self, 'special_folder', n.get_object_value(special_folder.SpecialFolder)),
            "video": lambda n : setattr(self, 'video', n.get_object_value(video.Video)),
            "webDavUrl": lambda n : setattr(self, 'web_dav_url', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("createdBy", self.created_by)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("file", self.file)
        writer.write_object_value("fileSystemInfo", self.file_system_info)
        writer.write_object_value("folder", self.folder)
        writer.write_str_value("id", self.id)
        writer.write_object_value("image", self.image)
        writer.write_object_value("lastModifiedBy", self.last_modified_by)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("package", self.package)
        writer.write_object_value("parentReference", self.parent_reference)
        writer.write_object_value("shared", self.shared)
        writer.write_object_value("sharepointIds", self.sharepoint_ids)
        writer.write_int_value("size", self.size)
        writer.write_object_value("specialFolder", self.special_folder)
        writer.write_object_value("video", self.video)
        writer.write_str_value("webDavUrl", self.web_dav_url)
        writer.write_str_value("webUrl", self.web_url)
        writer.write_additional_data_value(self.additional_data)
    

