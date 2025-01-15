from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .audio import Audio
    from .base_item import BaseItem
    from .bundle import Bundle
    from .deleted import Deleted
    from .drive_item_version import DriveItemVersion
    from .file import File
    from .file_system_info import FileSystemInfo
    from .folder import Folder
    from .geo_coordinates import GeoCoordinates
    from .image import Image
    from .item_analytics import ItemAnalytics
    from .item_retention_label import ItemRetentionLabel
    from .list_item import ListItem
    from .malware import Malware
    from .package import Package
    from .pending_operations import PendingOperations
    from .permission import Permission
    from .photo import Photo
    from .publication_facet import PublicationFacet
    from .remote_item import RemoteItem
    from .root import Root
    from .search_result import SearchResult
    from .shared import Shared
    from .sharepoint_ids import SharepointIds
    from .special_folder import SpecialFolder
    from .subscription import Subscription
    from .thumbnail_set import ThumbnailSet
    from .video import Video
    from .workbook import Workbook

from .base_item import BaseItem

@dataclass
class DriveItem(BaseItem, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.driveItem"
    # Analytics about the view activities that took place on this item.
    analytics: Optional[ItemAnalytics] = None
    # Audio metadata, if the item is an audio file. Read-only. Read-only. Only on OneDrive Personal.
    audio: Optional[Audio] = None
    # Bundle metadata, if the item is a bundle. Read-only.
    bundle: Optional[Bundle] = None
    # An eTag for the content of the item. This eTag isn't changed if only the metadata is changed. Note This property isn't returned if the item is a folder. Read-only.
    c_tag: Optional[str] = None
    # Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.
    children: Optional[list[DriveItem]] = None
    # The content stream, if the item represents a file.
    content: Optional[bytes] = None
    # Information about the deleted state of the item. Read-only.
    deleted: Optional[Deleted] = None
    # File metadata, if the item is a file. Read-only.
    file: Optional[File] = None
    # File system information on client. Read-write.
    file_system_info: Optional[FileSystemInfo] = None
    # Folder metadata, if the item is a folder. Read-only.
    folder: Optional[Folder] = None
    # Image metadata, if the item is an image. Read-only.
    image: Optional[Image] = None
    # For drives in SharePoint, the associated document library list item. Read-only. Nullable.
    list_item: Optional[ListItem] = None
    # Location metadata, if the item has location data. Read-only.
    location: Optional[GeoCoordinates] = None
    # Malware metadata, if the item was detected to contain malware. Read-only.
    malware: Optional[Malware] = None
    # If present, indicates that this item is a package instead of a folder or file. Packages are treated like files in some contexts and folders in others. Read-only.
    package: Optional[Package] = None
    # If present, indicates that one or more operations that might affect the state of the driveItem are pending completion. Read-only.
    pending_operations: Optional[PendingOperations] = None
    # The set of permissions for the item. Read-only. Nullable.
    permissions: Optional[list[Permission]] = None
    # Photo metadata, if the item is a photo. Read-only.
    photo: Optional[Photo] = None
    # Provides information about the published or checked-out state of an item, in locations that support such actions. This property isn't returned by default. Read-only.
    publication: Optional[PublicationFacet] = None
    # Remote item data, if the item is shared from a drive other than the one being accessed. Read-only.
    remote_item: Optional[RemoteItem] = None
    # Information about retention label and settings enforced on the driveItem. Read-write.
    retention_label: Optional[ItemRetentionLabel] = None
    # If this property is non-null, it indicates that the driveItem is the top-most driveItem in the drive.
    root: Optional[Root] = None
    # Search metadata, if the item is from a search result. Read-only.
    search_result: Optional[SearchResult] = None
    # Indicates that the item was shared with others and provides information about the shared state of the item. Read-only.
    shared: Optional[Shared] = None
    # Returns identifiers useful for SharePoint REST compatibility. Read-only.
    sharepoint_ids: Optional[SharepointIds] = None
    # Size of the item in bytes. Read-only.
    size: Optional[int] = None
    # If the current item is also available as a special folder, this facet is returned. Read-only.
    special_folder: Optional[SpecialFolder] = None
    # The set of subscriptions on the item. Only supported on the root of a drive.
    subscriptions: Optional[list[Subscription]] = None
    # Collection of thumbnailSet objects associated with the item. For more information, see getting thumbnails. Read-only. Nullable.
    thumbnails: Optional[list[ThumbnailSet]] = None
    # The list of previous versions of the item. For more info, see getting previous versions. Read-only. Nullable.
    versions: Optional[list[DriveItemVersion]] = None
    # Video metadata, if the item is a video. Read-only.
    video: Optional[Video] = None
    # WebDAV compatible URL for the item.
    web_dav_url: Optional[str] = None
    # For files that are Excel spreadsheets, access to the workbook API to work with the spreadsheet's contents. Nullable.
    workbook: Optional[Workbook] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DriveItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DriveItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DriveItem()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .audio import Audio
        from .base_item import BaseItem
        from .bundle import Bundle
        from .deleted import Deleted
        from .drive_item_version import DriveItemVersion
        from .file import File
        from .file_system_info import FileSystemInfo
        from .folder import Folder
        from .geo_coordinates import GeoCoordinates
        from .image import Image
        from .item_analytics import ItemAnalytics
        from .item_retention_label import ItemRetentionLabel
        from .list_item import ListItem
        from .malware import Malware
        from .package import Package
        from .pending_operations import PendingOperations
        from .permission import Permission
        from .photo import Photo
        from .publication_facet import PublicationFacet
        from .remote_item import RemoteItem
        from .root import Root
        from .search_result import SearchResult
        from .shared import Shared
        from .sharepoint_ids import SharepointIds
        from .special_folder import SpecialFolder
        from .subscription import Subscription
        from .thumbnail_set import ThumbnailSet
        from .video import Video
        from .workbook import Workbook

        from .audio import Audio
        from .base_item import BaseItem
        from .bundle import Bundle
        from .deleted import Deleted
        from .drive_item_version import DriveItemVersion
        from .file import File
        from .file_system_info import FileSystemInfo
        from .folder import Folder
        from .geo_coordinates import GeoCoordinates
        from .image import Image
        from .item_analytics import ItemAnalytics
        from .item_retention_label import ItemRetentionLabel
        from .list_item import ListItem
        from .malware import Malware
        from .package import Package
        from .pending_operations import PendingOperations
        from .permission import Permission
        from .photo import Photo
        from .publication_facet import PublicationFacet
        from .remote_item import RemoteItem
        from .root import Root
        from .search_result import SearchResult
        from .shared import Shared
        from .sharepoint_ids import SharepointIds
        from .special_folder import SpecialFolder
        from .subscription import Subscription
        from .thumbnail_set import ThumbnailSet
        from .video import Video
        from .workbook import Workbook

        fields: dict[str, Callable[[Any], None]] = {
            "analytics": lambda n : setattr(self, 'analytics', n.get_object_value(ItemAnalytics)),
            "audio": lambda n : setattr(self, 'audio', n.get_object_value(Audio)),
            "bundle": lambda n : setattr(self, 'bundle', n.get_object_value(Bundle)),
            "cTag": lambda n : setattr(self, 'c_tag', n.get_str_value()),
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(DriveItem)),
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "deleted": lambda n : setattr(self, 'deleted', n.get_object_value(Deleted)),
            "file": lambda n : setattr(self, 'file', n.get_object_value(File)),
            "fileSystemInfo": lambda n : setattr(self, 'file_system_info', n.get_object_value(FileSystemInfo)),
            "folder": lambda n : setattr(self, 'folder', n.get_object_value(Folder)),
            "image": lambda n : setattr(self, 'image', n.get_object_value(Image)),
            "listItem": lambda n : setattr(self, 'list_item', n.get_object_value(ListItem)),
            "location": lambda n : setattr(self, 'location', n.get_object_value(GeoCoordinates)),
            "malware": lambda n : setattr(self, 'malware', n.get_object_value(Malware)),
            "package": lambda n : setattr(self, 'package', n.get_object_value(Package)),
            "pendingOperations": lambda n : setattr(self, 'pending_operations', n.get_object_value(PendingOperations)),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_object_values(Permission)),
            "photo": lambda n : setattr(self, 'photo', n.get_object_value(Photo)),
            "publication": lambda n : setattr(self, 'publication', n.get_object_value(PublicationFacet)),
            "remoteItem": lambda n : setattr(self, 'remote_item', n.get_object_value(RemoteItem)),
            "retentionLabel": lambda n : setattr(self, 'retention_label', n.get_object_value(ItemRetentionLabel)),
            "root": lambda n : setattr(self, 'root', n.get_object_value(Root)),
            "searchResult": lambda n : setattr(self, 'search_result', n.get_object_value(SearchResult)),
            "shared": lambda n : setattr(self, 'shared', n.get_object_value(Shared)),
            "sharepointIds": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(SharepointIds)),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "specialFolder": lambda n : setattr(self, 'special_folder', n.get_object_value(SpecialFolder)),
            "subscriptions": lambda n : setattr(self, 'subscriptions', n.get_collection_of_object_values(Subscription)),
            "thumbnails": lambda n : setattr(self, 'thumbnails', n.get_collection_of_object_values(ThumbnailSet)),
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(DriveItemVersion)),
            "video": lambda n : setattr(self, 'video', n.get_object_value(Video)),
            "webDavUrl": lambda n : setattr(self, 'web_dav_url', n.get_str_value()),
            "workbook": lambda n : setattr(self, 'workbook', n.get_object_value(Workbook)),
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
        writer.write_object_value("analytics", self.analytics)
        writer.write_object_value("audio", self.audio)
        writer.write_object_value("bundle", self.bundle)
        writer.write_str_value("cTag", self.c_tag)
        writer.write_collection_of_object_values("children", self.children)
        writer.write_bytes_value("content", self.content)
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
        writer.write_object_value("retentionLabel", self.retention_label)
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
    

