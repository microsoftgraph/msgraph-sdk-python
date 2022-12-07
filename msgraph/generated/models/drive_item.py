from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

audio = lazy_import('msgraph.generated.models.audio')
base_item = lazy_import('msgraph.generated.models.base_item')
bundle = lazy_import('msgraph.generated.models.bundle')
deleted = lazy_import('msgraph.generated.models.deleted')
drive_item_version = lazy_import('msgraph.generated.models.drive_item_version')
file = lazy_import('msgraph.generated.models.file')
file_system_info = lazy_import('msgraph.generated.models.file_system_info')
folder = lazy_import('msgraph.generated.models.folder')
geo_coordinates = lazy_import('msgraph.generated.models.geo_coordinates')
image = lazy_import('msgraph.generated.models.image')
item_analytics = lazy_import('msgraph.generated.models.item_analytics')
list_item = lazy_import('msgraph.generated.models.list_item')
malware = lazy_import('msgraph.generated.models.malware')
package = lazy_import('msgraph.generated.models.package')
pending_operations = lazy_import('msgraph.generated.models.pending_operations')
permission = lazy_import('msgraph.generated.models.permission')
photo = lazy_import('msgraph.generated.models.photo')
publication_facet = lazy_import('msgraph.generated.models.publication_facet')
remote_item = lazy_import('msgraph.generated.models.remote_item')
root = lazy_import('msgraph.generated.models.root')
search_result = lazy_import('msgraph.generated.models.search_result')
shared = lazy_import('msgraph.generated.models.shared')
sharepoint_ids = lazy_import('msgraph.generated.models.sharepoint_ids')
special_folder = lazy_import('msgraph.generated.models.special_folder')
subscription = lazy_import('msgraph.generated.models.subscription')
thumbnail_set = lazy_import('msgraph.generated.models.thumbnail_set')
video = lazy_import('msgraph.generated.models.video')
workbook = lazy_import('msgraph.generated.models.workbook')

class DriveItem(base_item.BaseItem):
    """
    Provides operations to manage the collection of agreement entities.
    """
    @property
    def analytics(self,) -> Optional[item_analytics.ItemAnalytics]:
        """
        Gets the analytics property value. Analytics about the view activities that took place on this item.
        Returns: Optional[item_analytics.ItemAnalytics]
        """
        return self._analytics
    
    @analytics.setter
    def analytics(self,value: Optional[item_analytics.ItemAnalytics] = None) -> None:
        """
        Sets the analytics property value. Analytics about the view activities that took place on this item.
        Args:
            value: Value to set for the analytics property.
        """
        self._analytics = value
    
    @property
    def audio(self,) -> Optional[audio.Audio]:
        """
        Gets the audio property value. Audio metadata, if the item is an audio file. Read-only. Read-only. Only on OneDrive Personal.
        Returns: Optional[audio.Audio]
        """
        return self._audio
    
    @audio.setter
    def audio(self,value: Optional[audio.Audio] = None) -> None:
        """
        Sets the audio property value. Audio metadata, if the item is an audio file. Read-only. Read-only. Only on OneDrive Personal.
        Args:
            value: Value to set for the audio property.
        """
        self._audio = value
    
    @property
    def bundle(self,) -> Optional[bundle.Bundle]:
        """
        Gets the bundle property value. Bundle metadata, if the item is a bundle. Read-only.
        Returns: Optional[bundle.Bundle]
        """
        return self._bundle
    
    @bundle.setter
    def bundle(self,value: Optional[bundle.Bundle] = None) -> None:
        """
        Sets the bundle property value. Bundle metadata, if the item is a bundle. Read-only.
        Args:
            value: Value to set for the bundle property.
        """
        self._bundle = value
    
    @property
    def children(self,) -> Optional[List[DriveItem]]:
        """
        Gets the children property value. Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.
        Returns: Optional[List[DriveItem]]
        """
        return self._children
    
    @children.setter
    def children(self,value: Optional[List[DriveItem]] = None) -> None:
        """
        Sets the children property value. Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.
        Args:
            value: Value to set for the children property.
        """
        self._children = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new driveItem and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.driveItem"
        # Analytics about the view activities that took place on this item.
        self._analytics: Optional[item_analytics.ItemAnalytics] = None
        # Audio metadata, if the item is an audio file. Read-only. Read-only. Only on OneDrive Personal.
        self._audio: Optional[audio.Audio] = None
        # Bundle metadata, if the item is a bundle. Read-only.
        self._bundle: Optional[bundle.Bundle] = None
        # Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.
        self._children: Optional[List[DriveItem]] = None
        # The content stream, if the item represents a file.
        self._content: Optional[bytes] = None
        # An eTag for the content of the item. This eTag is not changed if only the metadata is changed. Note This property is not returned if the item is a folder. Read-only.
        self._c_tag: Optional[str] = None
        # Information about the deleted state of the item. Read-only.
        self._deleted: Optional[deleted.Deleted] = None
        # File metadata, if the item is a file. Read-only.
        self._file: Optional[file.File] = None
        # File system information on client. Read-write.
        self._file_system_info: Optional[file_system_info.FileSystemInfo] = None
        # Folder metadata, if the item is a folder. Read-only.
        self._folder: Optional[folder.Folder] = None
        # Image metadata, if the item is an image. Read-only.
        self._image: Optional[image.Image] = None
        # For drives in SharePoint, the associated document library list item. Read-only. Nullable.
        self._list_item: Optional[list_item.ListItem] = None
        # Location metadata, if the item has location data. Read-only.
        self._location: Optional[geo_coordinates.GeoCoordinates] = None
        # Malware metadata, if the item was detected to contain malware. Read-only.
        self._malware: Optional[malware.Malware] = None
        # If present, indicates that this item is a package instead of a folder or file. Packages are treated like files in some contexts and folders in others. Read-only.
        self._package: Optional[package.Package] = None
        # If present, indicates that one or more operations that might affect the state of the driveItem are pending completion. Read-only.
        self._pending_operations: Optional[pending_operations.PendingOperations] = None
        # The set of permissions for the item. Read-only. Nullable.
        self._permissions: Optional[List[permission.Permission]] = None
        # Photo metadata, if the item is a photo. Read-only.
        self._photo: Optional[photo.Photo] = None
        # Provides information about the published or checked-out state of an item, in locations that support such actions. This property is not returned by default. Read-only.
        self._publication: Optional[publication_facet.PublicationFacet] = None
        # Remote item data, if the item is shared from a drive other than the one being accessed. Read-only.
        self._remote_item: Optional[remote_item.RemoteItem] = None
        # If this property is non-null, it indicates that the driveItem is the top-most driveItem in the drive.
        self._root: Optional[root.Root] = None
        # Search metadata, if the item is from a search result. Read-only.
        self._search_result: Optional[search_result.SearchResult] = None
        # Indicates that the item has been shared with others and provides information about the shared state of the item. Read-only.
        self._shared: Optional[shared.Shared] = None
        # Returns identifiers useful for SharePoint REST compatibility. Read-only.
        self._sharepoint_ids: Optional[sharepoint_ids.SharepointIds] = None
        # Size of the item in bytes. Read-only.
        self._size: Optional[int] = None
        # If the current item is also available as a special folder, this facet is returned. Read-only.
        self._special_folder: Optional[special_folder.SpecialFolder] = None
        # The set of subscriptions on the item. Only supported on the root of a drive.
        self._subscriptions: Optional[List[subscription.Subscription]] = None
        # Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.
        self._thumbnails: Optional[List[thumbnail_set.ThumbnailSet]] = None
        # The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.
        self._versions: Optional[List[drive_item_version.DriveItemVersion]] = None
        # Video metadata, if the item is a video. Read-only.
        self._video: Optional[video.Video] = None
        # WebDAV compatible URL for the item.
        self._web_dav_url: Optional[str] = None
        # For files that are Excel spreadsheets, accesses the workbook API to work with the spreadsheet's contents. Nullable.
        self._workbook: Optional[workbook.Workbook] = None
    
    @property
    def content(self,) -> Optional[bytes]:
        """
        Gets the content property value. The content stream, if the item represents a file.
        Returns: Optional[bytes]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[bytes] = None) -> None:
        """
        Sets the content property value. The content stream, if the item represents a file.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DriveItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DriveItem
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DriveItem()
    
    @property
    def c_tag(self,) -> Optional[str]:
        """
        Gets the cTag property value. An eTag for the content of the item. This eTag is not changed if only the metadata is changed. Note This property is not returned if the item is a folder. Read-only.
        Returns: Optional[str]
        """
        return self._c_tag
    
    @c_tag.setter
    def c_tag(self,value: Optional[str] = None) -> None:
        """
        Sets the cTag property value. An eTag for the content of the item. This eTag is not changed if only the metadata is changed. Note This property is not returned if the item is a folder. Read-only.
        Args:
            value: Value to set for the cTag property.
        """
        self._c_tag = value
    
    @property
    def deleted(self,) -> Optional[deleted.Deleted]:
        """
        Gets the deleted property value. Information about the deleted state of the item. Read-only.
        Returns: Optional[deleted.Deleted]
        """
        return self._deleted
    
    @deleted.setter
    def deleted(self,value: Optional[deleted.Deleted] = None) -> None:
        """
        Sets the deleted property value. Information about the deleted state of the item. Read-only.
        Args:
            value: Value to set for the deleted property.
        """
        self._deleted = value
    
    @property
    def file(self,) -> Optional[file.File]:
        """
        Gets the file property value. File metadata, if the item is a file. Read-only.
        Returns: Optional[file.File]
        """
        return self._file
    
    @file.setter
    def file(self,value: Optional[file.File] = None) -> None:
        """
        Sets the file property value. File metadata, if the item is a file. Read-only.
        Args:
            value: Value to set for the file property.
        """
        self._file = value
    
    @property
    def file_system_info(self,) -> Optional[file_system_info.FileSystemInfo]:
        """
        Gets the fileSystemInfo property value. File system information on client. Read-write.
        Returns: Optional[file_system_info.FileSystemInfo]
        """
        return self._file_system_info
    
    @file_system_info.setter
    def file_system_info(self,value: Optional[file_system_info.FileSystemInfo] = None) -> None:
        """
        Sets the fileSystemInfo property value. File system information on client. Read-write.
        Args:
            value: Value to set for the fileSystemInfo property.
        """
        self._file_system_info = value
    
    @property
    def folder(self,) -> Optional[folder.Folder]:
        """
        Gets the folder property value. Folder metadata, if the item is a folder. Read-only.
        Returns: Optional[folder.Folder]
        """
        return self._folder
    
    @folder.setter
    def folder(self,value: Optional[folder.Folder] = None) -> None:
        """
        Sets the folder property value. Folder metadata, if the item is a folder. Read-only.
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
            "analytics": lambda n : setattr(self, 'analytics', n.get_object_value(item_analytics.ItemAnalytics)),
            "audio": lambda n : setattr(self, 'audio', n.get_object_value(audio.Audio)),
            "bundle": lambda n : setattr(self, 'bundle', n.get_object_value(bundle.Bundle)),
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(DriveItem)),
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "c_tag": lambda n : setattr(self, 'c_tag', n.get_str_value()),
            "deleted": lambda n : setattr(self, 'deleted', n.get_object_value(deleted.Deleted)),
            "file": lambda n : setattr(self, 'file', n.get_object_value(file.File)),
            "file_system_info": lambda n : setattr(self, 'file_system_info', n.get_object_value(file_system_info.FileSystemInfo)),
            "folder": lambda n : setattr(self, 'folder', n.get_object_value(folder.Folder)),
            "image": lambda n : setattr(self, 'image', n.get_object_value(image.Image)),
            "list_item": lambda n : setattr(self, 'list_item', n.get_object_value(list_item.ListItem)),
            "location": lambda n : setattr(self, 'location', n.get_object_value(geo_coordinates.GeoCoordinates)),
            "malware": lambda n : setattr(self, 'malware', n.get_object_value(malware.Malware)),
            "package": lambda n : setattr(self, 'package', n.get_object_value(package.Package)),
            "pending_operations": lambda n : setattr(self, 'pending_operations', n.get_object_value(pending_operations.PendingOperations)),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_object_values(permission.Permission)),
            "photo": lambda n : setattr(self, 'photo', n.get_object_value(photo.Photo)),
            "publication": lambda n : setattr(self, 'publication', n.get_object_value(publication_facet.PublicationFacet)),
            "remote_item": lambda n : setattr(self, 'remote_item', n.get_object_value(remote_item.RemoteItem)),
            "root": lambda n : setattr(self, 'root', n.get_object_value(root.Root)),
            "search_result": lambda n : setattr(self, 'search_result', n.get_object_value(search_result.SearchResult)),
            "shared": lambda n : setattr(self, 'shared', n.get_object_value(shared.Shared)),
            "sharepoint_ids": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(sharepoint_ids.SharepointIds)),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "special_folder": lambda n : setattr(self, 'special_folder', n.get_object_value(special_folder.SpecialFolder)),
            "subscriptions": lambda n : setattr(self, 'subscriptions', n.get_collection_of_object_values(subscription.Subscription)),
            "thumbnails": lambda n : setattr(self, 'thumbnails', n.get_collection_of_object_values(thumbnail_set.ThumbnailSet)),
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(drive_item_version.DriveItemVersion)),
            "video": lambda n : setattr(self, 'video', n.get_object_value(video.Video)),
            "web_dav_url": lambda n : setattr(self, 'web_dav_url', n.get_str_value()),
            "workbook": lambda n : setattr(self, 'workbook', n.get_object_value(workbook.Workbook)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
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
    def list_item(self,) -> Optional[list_item.ListItem]:
        """
        Gets the listItem property value. For drives in SharePoint, the associated document library list item. Read-only. Nullable.
        Returns: Optional[list_item.ListItem]
        """
        return self._list_item
    
    @list_item.setter
    def list_item(self,value: Optional[list_item.ListItem] = None) -> None:
        """
        Sets the listItem property value. For drives in SharePoint, the associated document library list item. Read-only. Nullable.
        Args:
            value: Value to set for the listItem property.
        """
        self._list_item = value
    
    @property
    def location(self,) -> Optional[geo_coordinates.GeoCoordinates]:
        """
        Gets the location property value. Location metadata, if the item has location data. Read-only.
        Returns: Optional[geo_coordinates.GeoCoordinates]
        """
        return self._location
    
    @location.setter
    def location(self,value: Optional[geo_coordinates.GeoCoordinates] = None) -> None:
        """
        Sets the location property value. Location metadata, if the item has location data. Read-only.
        Args:
            value: Value to set for the location property.
        """
        self._location = value
    
    @property
    def malware(self,) -> Optional[malware.Malware]:
        """
        Gets the malware property value. Malware metadata, if the item was detected to contain malware. Read-only.
        Returns: Optional[malware.Malware]
        """
        return self._malware
    
    @malware.setter
    def malware(self,value: Optional[malware.Malware] = None) -> None:
        """
        Sets the malware property value. Malware metadata, if the item was detected to contain malware. Read-only.
        Args:
            value: Value to set for the malware property.
        """
        self._malware = value
    
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
    def pending_operations(self,) -> Optional[pending_operations.PendingOperations]:
        """
        Gets the pendingOperations property value. If present, indicates that one or more operations that might affect the state of the driveItem are pending completion. Read-only.
        Returns: Optional[pending_operations.PendingOperations]
        """
        return self._pending_operations
    
    @pending_operations.setter
    def pending_operations(self,value: Optional[pending_operations.PendingOperations] = None) -> None:
        """
        Sets the pendingOperations property value. If present, indicates that one or more operations that might affect the state of the driveItem are pending completion. Read-only.
        Args:
            value: Value to set for the pendingOperations property.
        """
        self._pending_operations = value
    
    @property
    def permissions(self,) -> Optional[List[permission.Permission]]:
        """
        Gets the permissions property value. The set of permissions for the item. Read-only. Nullable.
        Returns: Optional[List[permission.Permission]]
        """
        return self._permissions
    
    @permissions.setter
    def permissions(self,value: Optional[List[permission.Permission]] = None) -> None:
        """
        Sets the permissions property value. The set of permissions for the item. Read-only. Nullable.
        Args:
            value: Value to set for the permissions property.
        """
        self._permissions = value
    
    @property
    def photo(self,) -> Optional[photo.Photo]:
        """
        Gets the photo property value. Photo metadata, if the item is a photo. Read-only.
        Returns: Optional[photo.Photo]
        """
        return self._photo
    
    @photo.setter
    def photo(self,value: Optional[photo.Photo] = None) -> None:
        """
        Sets the photo property value. Photo metadata, if the item is a photo. Read-only.
        Args:
            value: Value to set for the photo property.
        """
        self._photo = value
    
    @property
    def publication(self,) -> Optional[publication_facet.PublicationFacet]:
        """
        Gets the publication property value. Provides information about the published or checked-out state of an item, in locations that support such actions. This property is not returned by default. Read-only.
        Returns: Optional[publication_facet.PublicationFacet]
        """
        return self._publication
    
    @publication.setter
    def publication(self,value: Optional[publication_facet.PublicationFacet] = None) -> None:
        """
        Sets the publication property value. Provides information about the published or checked-out state of an item, in locations that support such actions. This property is not returned by default. Read-only.
        Args:
            value: Value to set for the publication property.
        """
        self._publication = value
    
    @property
    def remote_item(self,) -> Optional[remote_item.RemoteItem]:
        """
        Gets the remoteItem property value. Remote item data, if the item is shared from a drive other than the one being accessed. Read-only.
        Returns: Optional[remote_item.RemoteItem]
        """
        return self._remote_item
    
    @remote_item.setter
    def remote_item(self,value: Optional[remote_item.RemoteItem] = None) -> None:
        """
        Sets the remoteItem property value. Remote item data, if the item is shared from a drive other than the one being accessed. Read-only.
        Args:
            value: Value to set for the remoteItem property.
        """
        self._remote_item = value
    
    @property
    def root(self,) -> Optional[root.Root]:
        """
        Gets the root property value. If this property is non-null, it indicates that the driveItem is the top-most driveItem in the drive.
        Returns: Optional[root.Root]
        """
        return self._root
    
    @root.setter
    def root(self,value: Optional[root.Root] = None) -> None:
        """
        Sets the root property value. If this property is non-null, it indicates that the driveItem is the top-most driveItem in the drive.
        Args:
            value: Value to set for the root property.
        """
        self._root = value
    
    @property
    def search_result(self,) -> Optional[search_result.SearchResult]:
        """
        Gets the searchResult property value. Search metadata, if the item is from a search result. Read-only.
        Returns: Optional[search_result.SearchResult]
        """
        return self._search_result
    
    @search_result.setter
    def search_result(self,value: Optional[search_result.SearchResult] = None) -> None:
        """
        Sets the searchResult property value. Search metadata, if the item is from a search result. Read-only.
        Args:
            value: Value to set for the searchResult property.
        """
        self._search_result = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("analytics", self.analytics)
        writer.write_object_value("audio", self.audio)
        writer.write_object_value("bundle", self.bundle)
        writer.write_collection_of_object_values("children", self.children)
        writer.write_object_value("content", self.content)
        writer.write_str_value("cTag", self.c_tag)
        writer.write_object_value("deleted", self.deleted)
        writer.write_object_value("file", self.file)
        writer.write_object_value("fileSystemInfo", self.file_system_info)
        writer.write_object_value("folder", self.folder)
        writer.write_object_value("image", self.image)
        writer.write_object_value("listItem", self.list_item)
        writer.write_object_value("location", self.location)
        writer.write_object_value("malware", self.malware)
        writer.write_object_value("package", self.package)
        writer.write_object_value("pendingOperations", self.pending_operations)
        writer.write_collection_of_object_values("permissions", self.permissions)
        writer.write_object_value("photo", self.photo)
        writer.write_object_value("publication", self.publication)
        writer.write_object_value("remoteItem", self.remote_item)
        writer.write_object_value("root", self.root)
        writer.write_object_value("searchResult", self.search_result)
        writer.write_object_value("shared", self.shared)
        writer.write_object_value("sharepointIds", self.sharepoint_ids)
        writer.write_int_value("size", self.size)
        writer.write_object_value("specialFolder", self.special_folder)
        writer.write_collection_of_object_values("subscriptions", self.subscriptions)
        writer.write_collection_of_object_values("thumbnails", self.thumbnails)
        writer.write_collection_of_object_values("versions", self.versions)
        writer.write_object_value("video", self.video)
        writer.write_str_value("webDavUrl", self.web_dav_url)
        writer.write_object_value("workbook", self.workbook)
    
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
        Gets the sharepointIds property value. Returns identifiers useful for SharePoint REST compatibility. Read-only.
        Returns: Optional[sharepoint_ids.SharepointIds]
        """
        return self._sharepoint_ids
    
    @sharepoint_ids.setter
    def sharepoint_ids(self,value: Optional[sharepoint_ids.SharepointIds] = None) -> None:
        """
        Sets the sharepointIds property value. Returns identifiers useful for SharePoint REST compatibility. Read-only.
        Args:
            value: Value to set for the sharepointIds property.
        """
        self._sharepoint_ids = value
    
    @property
    def size(self,) -> Optional[int]:
        """
        Gets the size property value. Size of the item in bytes. Read-only.
        Returns: Optional[int]
        """
        return self._size
    
    @size.setter
    def size(self,value: Optional[int] = None) -> None:
        """
        Sets the size property value. Size of the item in bytes. Read-only.
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
    def subscriptions(self,) -> Optional[List[subscription.Subscription]]:
        """
        Gets the subscriptions property value. The set of subscriptions on the item. Only supported on the root of a drive.
        Returns: Optional[List[subscription.Subscription]]
        """
        return self._subscriptions
    
    @subscriptions.setter
    def subscriptions(self,value: Optional[List[subscription.Subscription]] = None) -> None:
        """
        Sets the subscriptions property value. The set of subscriptions on the item. Only supported on the root of a drive.
        Args:
            value: Value to set for the subscriptions property.
        """
        self._subscriptions = value
    
    @property
    def thumbnails(self,) -> Optional[List[thumbnail_set.ThumbnailSet]]:
        """
        Gets the thumbnails property value. Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.
        Returns: Optional[List[thumbnail_set.ThumbnailSet]]
        """
        return self._thumbnails
    
    @thumbnails.setter
    def thumbnails(self,value: Optional[List[thumbnail_set.ThumbnailSet]] = None) -> None:
        """
        Sets the thumbnails property value. Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.
        Args:
            value: Value to set for the thumbnails property.
        """
        self._thumbnails = value
    
    @property
    def versions(self,) -> Optional[List[drive_item_version.DriveItemVersion]]:
        """
        Gets the versions property value. The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.
        Returns: Optional[List[drive_item_version.DriveItemVersion]]
        """
        return self._versions
    
    @versions.setter
    def versions(self,value: Optional[List[drive_item_version.DriveItemVersion]] = None) -> None:
        """
        Sets the versions property value. The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.
        Args:
            value: Value to set for the versions property.
        """
        self._versions = value
    
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
        Gets the webDavUrl property value. WebDAV compatible URL for the item.
        Returns: Optional[str]
        """
        return self._web_dav_url
    
    @web_dav_url.setter
    def web_dav_url(self,value: Optional[str] = None) -> None:
        """
        Sets the webDavUrl property value. WebDAV compatible URL for the item.
        Args:
            value: Value to set for the webDavUrl property.
        """
        self._web_dav_url = value
    
    @property
    def workbook(self,) -> Optional[workbook.Workbook]:
        """
        Gets the workbook property value. For files that are Excel spreadsheets, accesses the workbook API to work with the spreadsheet's contents. Nullable.
        Returns: Optional[workbook.Workbook]
        """
        return self._workbook
    
    @workbook.setter
    def workbook(self,value: Optional[workbook.Workbook] = None) -> None:
        """
        Sets the workbook property value. For files that are Excel spreadsheets, accesses the workbook API to work with the spreadsheet's contents. Nullable.
        Args:
            value: Value to set for the workbook property.
        """
        self._workbook = value
    

