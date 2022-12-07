from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

file = lazy_import('msgraph.generated.models.file')
file_system_info = lazy_import('msgraph.generated.models.file_system_info')
folder = lazy_import('msgraph.generated.models.folder')
identity_set = lazy_import('msgraph.generated.models.identity_set')
image = lazy_import('msgraph.generated.models.image')
item_reference = lazy_import('msgraph.generated.models.item_reference')
package = lazy_import('msgraph.generated.models.package')
shared = lazy_import('msgraph.generated.models.shared')
sharepoint_ids = lazy_import('msgraph.generated.models.sharepoint_ids')
special_folder = lazy_import('msgraph.generated.models.special_folder')
video = lazy_import('msgraph.generated.models.video')

class RemoteItem(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new remoteItem and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Identity of the user, device, and application which created the item. Read-only.
        self._created_by: Optional[identity_set.IdentitySet] = None
        # Date and time of item creation. Read-only.
        self._created_date_time: Optional[datetime] = None
        # Indicates that the remote item is a file. Read-only.
        self._file: Optional[file.File] = None
        # Information about the remote item from the local file system. Read-only.
        self._file_system_info: Optional[file_system_info.FileSystemInfo] = None
        # Indicates that the remote item is a folder. Read-only.
        self._folder: Optional[folder.Folder] = None
        # Unique identifier for the remote item in its drive. Read-only.
        self._id: Optional[str] = None
        # Image metadata, if the item is an image. Read-only.
        self._image: Optional[image.Image] = None
        # Identity of the user, device, and application which last modified the item. Read-only.
        self._last_modified_by: Optional[identity_set.IdentitySet] = None
        # Date and time the item was last modified. Read-only.
        self._last_modified_date_time: Optional[datetime] = None
        # Optional. Filename of the remote item. Read-only.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # If present, indicates that this item is a package instead of a folder or file. Packages are treated like files in some contexts and folders in others. Read-only.
        self._package: Optional[package.Package] = None
        # Properties of the parent of the remote item. Read-only.
        self._parent_reference: Optional[item_reference.ItemReference] = None
        # Indicates that the item has been shared with others and provides information about the shared state of the item. Read-only.
        self._shared: Optional[shared.Shared] = None
        # Provides interop between items in OneDrive for Business and SharePoint with the full set of item identifiers. Read-only.
        self._sharepoint_ids: Optional[sharepoint_ids.SharepointIds] = None
        # Size of the remote item. Read-only.
        self._size: Optional[int] = None
        # If the current item is also available as a special folder, this facet is returned. Read-only.
        self._special_folder: Optional[special_folder.SpecialFolder] = None
        # Video metadata, if the item is a video. Read-only.
        self._video: Optional[video.Video] = None
        # DAV compatible URL for the item.
        self._web_dav_url: Optional[str] = None
        # URL that displays the resource in the browser. Read-only.
        self._web_url: Optional[str] = None
    
    @property
    def created_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the createdBy property value. Identity of the user, device, and application which created the item. Read-only.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._created_by
    
    @created_by.setter
    def created_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the createdBy property value. Identity of the user, device, and application which created the item. Read-only.
        Args:
            value: Value to set for the createdBy property.
        """
        self._created_by = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Date and time of item creation. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Date and time of item creation. Read-only.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
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
    
    @property
    def file(self,) -> Optional[file.File]:
        """
        Gets the file property value. Indicates that the remote item is a file. Read-only.
        Returns: Optional[file.File]
        """
        return self._file
    
    @file.setter
    def file(self,value: Optional[file.File] = None) -> None:
        """
        Sets the file property value. Indicates that the remote item is a file. Read-only.
        Args:
            value: Value to set for the file property.
        """
        self._file = value
    
    @property
    def file_system_info(self,) -> Optional[file_system_info.FileSystemInfo]:
        """
        Gets the fileSystemInfo property value. Information about the remote item from the local file system. Read-only.
        Returns: Optional[file_system_info.FileSystemInfo]
        """
        return self._file_system_info
    
    @file_system_info.setter
    def file_system_info(self,value: Optional[file_system_info.FileSystemInfo] = None) -> None:
        """
        Sets the fileSystemInfo property value. Information about the remote item from the local file system. Read-only.
        Args:
            value: Value to set for the fileSystemInfo property.
        """
        self._file_system_info = value
    
    @property
    def folder(self,) -> Optional[folder.Folder]:
        """
        Gets the folder property value. Indicates that the remote item is a folder. Read-only.
        Returns: Optional[folder.Folder]
        """
        return self._folder
    
    @folder.setter
    def folder(self,value: Optional[folder.Folder] = None) -> None:
        """
        Sets the folder property value. Indicates that the remote item is a folder. Read-only.
        Args:
            value: Value to set for the folder property.
        """
        self._folder = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_by": lambda n : setattr(self, 'created_by', n.get_object_value(identity_set.IdentitySet)),
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "file": lambda n : setattr(self, 'file', n.get_object_value(file.File)),
            "file_system_info": lambda n : setattr(self, 'file_system_info', n.get_object_value(file_system_info.FileSystemInfo)),
            "folder": lambda n : setattr(self, 'folder', n.get_object_value(folder.Folder)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "image": lambda n : setattr(self, 'image', n.get_object_value(image.Image)),
            "last_modified_by": lambda n : setattr(self, 'last_modified_by', n.get_object_value(identity_set.IdentitySet)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "package": lambda n : setattr(self, 'package', n.get_object_value(package.Package)),
            "parent_reference": lambda n : setattr(self, 'parent_reference', n.get_object_value(item_reference.ItemReference)),
            "shared": lambda n : setattr(self, 'shared', n.get_object_value(shared.Shared)),
            "sharepoint_ids": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(sharepoint_ids.SharepointIds)),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "special_folder": lambda n : setattr(self, 'special_folder', n.get_object_value(special_folder.SpecialFolder)),
            "video": lambda n : setattr(self, 'video', n.get_object_value(video.Video)),
            "web_dav_url": lambda n : setattr(self, 'web_dav_url', n.get_str_value()),
            "web_url": lambda n : setattr(self, 'web_url', n.get_str_value()),
        }
        return fields
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. Unique identifier for the remote item in its drive. Read-only.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. Unique identifier for the remote item in its drive. Read-only.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def image(self,) -> Optional[image.Image]:
        """
        Gets the image property value. Image metadata, if the item is an image. Read-only.
        Returns: Optional[image.Image]
        """
        return self._image
    
    @image.setter
    def image(self,value: Optional[image.Image] = None) -> None:
        """
        Sets the image property value. Image metadata, if the item is an image. Read-only.
        Args:
            value: Value to set for the image property.
        """
        self._image = value
    
    @property
    def last_modified_by(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the lastModifiedBy property value. Identity of the user, device, and application which last modified the item. Read-only.
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._last_modified_by
    
    @last_modified_by.setter
    def last_modified_by(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the lastModifiedBy property value. Identity of the user, device, and application which last modified the item. Read-only.
        Args:
            value: Value to set for the lastModifiedBy property.
        """
        self._last_modified_by = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Date and time the item was last modified. Read-only.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Date and time the item was last modified. Read-only.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. Optional. Filename of the remote item. Read-only.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. Optional. Filename of the remote item. Read-only.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def package(self,) -> Optional[package.Package]:
        """
        Gets the package property value. If present, indicates that this item is a package instead of a folder or file. Packages are treated like files in some contexts and folders in others. Read-only.
        Returns: Optional[package.Package]
        """
        return self._package
    
    @package.setter
    def package(self,value: Optional[package.Package] = None) -> None:
        """
        Sets the package property value. If present, indicates that this item is a package instead of a folder or file. Packages are treated like files in some contexts and folders in others. Read-only.
        Args:
            value: Value to set for the package property.
        """
        self._package = value
    
    @property
    def parent_reference(self,) -> Optional[item_reference.ItemReference]:
        """
        Gets the parentReference property value. Properties of the parent of the remote item. Read-only.
        Returns: Optional[item_reference.ItemReference]
        """
        return self._parent_reference
    
    @parent_reference.setter
    def parent_reference(self,value: Optional[item_reference.ItemReference] = None) -> None:
        """
        Sets the parentReference property value. Properties of the parent of the remote item. Read-only.
        Args:
            value: Value to set for the parentReference property.
        """
        self._parent_reference = value
    
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
    
    @property
    def shared(self,) -> Optional[shared.Shared]:
        """
        Gets the shared property value. Indicates that the item has been shared with others and provides information about the shared state of the item. Read-only.
        Returns: Optional[shared.Shared]
        """
        return self._shared
    
    @shared.setter
    def shared(self,value: Optional[shared.Shared] = None) -> None:
        """
        Sets the shared property value. Indicates that the item has been shared with others and provides information about the shared state of the item. Read-only.
        Args:
            value: Value to set for the shared property.
        """
        self._shared = value
    
    @property
    def sharepoint_ids(self,) -> Optional[sharepoint_ids.SharepointIds]:
        """
        Gets the sharepointIds property value. Provides interop between items in OneDrive for Business and SharePoint with the full set of item identifiers. Read-only.
        Returns: Optional[sharepoint_ids.SharepointIds]
        """
        return self._sharepoint_ids
    
    @sharepoint_ids.setter
    def sharepoint_ids(self,value: Optional[sharepoint_ids.SharepointIds] = None) -> None:
        """
        Sets the sharepointIds property value. Provides interop between items in OneDrive for Business and SharePoint with the full set of item identifiers. Read-only.
        Args:
            value: Value to set for the sharepointIds property.
        """
        self._sharepoint_ids = value
    
    @property
    def size(self,) -> Optional[int]:
        """
        Gets the size property value. Size of the remote item. Read-only.
        Returns: Optional[int]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[int] = None) -> None:
        """
        Sets the size property value. Size of the remote item. Read-only.
        Args:
            value: Value to set for the size property.
        """
        self._size = value
    
    @property
    def special_folder(self,) -> Optional[special_folder.SpecialFolder]:
        """
        Gets the specialFolder property value. If the current item is also available as a special folder, this facet is returned. Read-only.
        Returns: Optional[special_folder.SpecialFolder]
        """
        return self._special_folder
    
    @special_folder.setter
    def special_folder(self,value: Optional[special_folder.SpecialFolder] = None) -> None:
        """
        Sets the specialFolder property value. If the current item is also available as a special folder, this facet is returned. Read-only.
        Args:
            value: Value to set for the specialFolder property.
        """
        self._special_folder = value
    
    @property
    def video(self,) -> Optional[video.Video]:
        """
        Gets the video property value. Video metadata, if the item is a video. Read-only.
        Returns: Optional[video.Video]
        """
        return self._video
    
    @video.setter
    def video(self,value: Optional[video.Video] = None) -> None:
        """
        Sets the video property value. Video metadata, if the item is a video. Read-only.
        Args:
            value: Value to set for the video property.
        """
        self._video = value
    
    @property
    def web_dav_url(self,) -> Optional[str]:
        """
        Gets the webDavUrl property value. DAV compatible URL for the item.
        Returns: Optional[str]
        """
        return self._web_dav_url
    
    @web_dav_url.setter
    def web_dav_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webDavUrl property value. DAV compatible URL for the item.
        Args:
            value: Value to set for the webDavUrl property.
        """
        self._web_dav_url = value
    
    @property
    def web_url(self,) -> Optional[str]:
        """
        Gets the webUrl property value. URL that displays the resource in the browser. Read-only.
        Returns: Optional[str]
        """
        return self._web_url
    
    @web_url.setter
    def web_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webUrl property value. URL that displays the resource in the browser. Read-only.
        Args:
            value: Value to set for the webUrl property.
        """
        self._web_url = value
    

