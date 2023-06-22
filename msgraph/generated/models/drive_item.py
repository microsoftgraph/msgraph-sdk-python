from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import audio, base_item, bundle, deleted, drive_item_version, file, file_system_info, folder, geo_coordinates, image, item_analytics, list_item, malware, package, pending_operations, permission, photo, publication_facet, remote_item, root, search_result, shared, sharepoint_ids, special_folder, subscription, thumbnail_set, video, workbook

from . import base_item

@dataclass
class DriveItem(base_item.BaseItem):
    odata_type = "#microsoft.graph.driveItem"
    # Analytics about the view activities that took place on this item.
    analytics: Optional[item_analytics.ItemAnalytics] = None
    # Audio metadata, if the item is an audio file. Read-only. Read-only. Only on OneDrive Personal.
    audio: Optional[audio.Audio] = None
    # Bundle metadata, if the item is a bundle. Read-only.
    bundle: Optional[bundle.Bundle] = None
    # An eTag for the content of the item. This eTag is not changed if only the metadata is changed. Note This property is not returned if the item is a folder. Read-only.
    c_tag: Optional[str] = None
    # Collection containing Item objects for the immediate children of Item. Only items representing folders have children. Read-only. Nullable.
    children: Optional[List[DriveItem]] = None
    # The content stream, if the item represents a file.
    content: Optional[bytes] = None
    # Information about the deleted state of the item. Read-only.
    deleted: Optional[deleted.Deleted] = None
    # File metadata, if the item is a file. Read-only.
    file: Optional[file.File] = None
    # File system information on client. Read-write.
    file_system_info: Optional[file_system_info.FileSystemInfo] = None
    # Folder metadata, if the item is a folder. Read-only.
    folder: Optional[folder.Folder] = None
    # Image metadata, if the item is an image. Read-only.
    image: Optional[image.Image] = None
    # For drives in SharePoint, the associated document library list item. Read-only. Nullable.
    list_item: Optional[list_item.ListItem] = None
    # Location metadata, if the item has location data. Read-only.
    location: Optional[geo_coordinates.GeoCoordinates] = None
    # Malware metadata, if the item was detected to contain malware. Read-only.
    malware: Optional[malware.Malware] = None
    # If present, indicates that this item is a package instead of a folder or file. Packages are treated like files in some contexts and folders in others. Read-only.
    package: Optional[package.Package] = None
    # If present, indicates that one or more operations that might affect the state of the driveItem are pending completion. Read-only.
    pending_operations: Optional[pending_operations.PendingOperations] = None
    # The set of permissions for the item. Read-only. Nullable.
    permissions: Optional[List[permission.Permission]] = None
    # Photo metadata, if the item is a photo. Read-only.
    photo: Optional[photo.Photo] = None
    # Provides information about the published or checked-out state of an item, in locations that support such actions. This property is not returned by default. Read-only.
    publication: Optional[publication_facet.PublicationFacet] = None
    # Remote item data, if the item is shared from a drive other than the one being accessed. Read-only.
    remote_item: Optional[remote_item.RemoteItem] = None
    # If this property is non-null, it indicates that the driveItem is the top-most driveItem in the drive.
    root: Optional[root.Root] = None
    # Search metadata, if the item is from a search result. Read-only.
    search_result: Optional[search_result.SearchResult] = None
    # Indicates that the item has been shared with others and provides information about the shared state of the item. Read-only.
    shared: Optional[shared.Shared] = None
    # Returns identifiers useful for SharePoint REST compatibility. Read-only.
    sharepoint_ids: Optional[sharepoint_ids.SharepointIds] = None
    # Size of the item in bytes. Read-only.
    size: Optional[int] = None
    # If the current item is also available as a special folder, this facet is returned. Read-only.
    special_folder: Optional[special_folder.SpecialFolder] = None
    # The set of subscriptions on the item. Only supported on the root of a drive.
    subscriptions: Optional[List[subscription.Subscription]] = None
    # Collection containing [ThumbnailSet][] objects associated with the item. For more info, see [getting thumbnails][]. Read-only. Nullable.
    thumbnails: Optional[List[thumbnail_set.ThumbnailSet]] = None
    # The list of previous versions of the item. For more info, see [getting previous versions][]. Read-only. Nullable.
    versions: Optional[List[drive_item_version.DriveItemVersion]] = None
    # Video metadata, if the item is a video. Read-only.
    video: Optional[video.Video] = None
    # WebDAV compatible URL for the item.
    web_dav_url: Optional[str] = None
    # For files that are Excel spreadsheets, accesses the workbook API to work with the spreadsheet's contents. Nullable.
    workbook: Optional[workbook.Workbook] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DriveItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DriveItem
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return DriveItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import audio, base_item, bundle, deleted, drive_item_version, file, file_system_info, folder, geo_coordinates, image, item_analytics, list_item, malware, package, pending_operations, permission, photo, publication_facet, remote_item, root, search_result, shared, sharepoint_ids, special_folder, subscription, thumbnail_set, video, workbook

        from . import audio, base_item, bundle, deleted, drive_item_version, file, file_system_info, folder, geo_coordinates, image, item_analytics, list_item, malware, package, pending_operations, permission, photo, publication_facet, remote_item, root, search_result, shared, sharepoint_ids, special_folder, subscription, thumbnail_set, video, workbook

        fields: Dict[str, Callable[[Any], None]] = {
            "analytics": lambda n : setattr(self, 'analytics', n.get_object_value(item_analytics.ItemAnalytics)),
            "audio": lambda n : setattr(self, 'audio', n.get_object_value(audio.Audio)),
            "bundle": lambda n : setattr(self, 'bundle', n.get_object_value(bundle.Bundle)),
            "cTag": lambda n : setattr(self, 'c_tag', n.get_str_value()),
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(DriveItem)),
            "content": lambda n : setattr(self, 'content', n.get_bytes_value()),
            "deleted": lambda n : setattr(self, 'deleted', n.get_object_value(deleted.Deleted)),
            "file": lambda n : setattr(self, 'file', n.get_object_value(file.File)),
            "fileSystemInfo": lambda n : setattr(self, 'file_system_info', n.get_object_value(file_system_info.FileSystemInfo)),
            "folder": lambda n : setattr(self, 'folder', n.get_object_value(folder.Folder)),
            "image": lambda n : setattr(self, 'image', n.get_object_value(image.Image)),
            "listItem": lambda n : setattr(self, 'list_item', n.get_object_value(list_item.ListItem)),
            "location": lambda n : setattr(self, 'location', n.get_object_value(geo_coordinates.GeoCoordinates)),
            "malware": lambda n : setattr(self, 'malware', n.get_object_value(malware.Malware)),
            "package": lambda n : setattr(self, 'package', n.get_object_value(package.Package)),
            "pendingOperations": lambda n : setattr(self, 'pending_operations', n.get_object_value(pending_operations.PendingOperations)),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_object_values(permission.Permission)),
            "photo": lambda n : setattr(self, 'photo', n.get_object_value(photo.Photo)),
            "publication": lambda n : setattr(self, 'publication', n.get_object_value(publication_facet.PublicationFacet)),
            "remoteItem": lambda n : setattr(self, 'remote_item', n.get_object_value(remote_item.RemoteItem)),
            "root": lambda n : setattr(self, 'root', n.get_object_value(root.Root)),
            "searchResult": lambda n : setattr(self, 'search_result', n.get_object_value(search_result.SearchResult)),
            "shared": lambda n : setattr(self, 'shared', n.get_object_value(shared.Shared)),
            "sharepointIds": lambda n : setattr(self, 'sharepoint_ids', n.get_object_value(sharepoint_ids.SharepointIds)),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "specialFolder": lambda n : setattr(self, 'special_folder', n.get_object_value(special_folder.SpecialFolder)),
            "subscriptions": lambda n : setattr(self, 'subscriptions', n.get_collection_of_object_values(subscription.Subscription)),
            "thumbnails": lambda n : setattr(self, 'thumbnails', n.get_collection_of_object_values(thumbnail_set.ThumbnailSet)),
            "versions": lambda n : setattr(self, 'versions', n.get_collection_of_object_values(drive_item_version.DriveItemVersion)),
            "video": lambda n : setattr(self, 'video', n.get_object_value(video.Video)),
            "webDavUrl": lambda n : setattr(self, 'web_dav_url', n.get_str_value()),
            "workbook": lambda n : setattr(self, 'workbook', n.get_object_value(workbook.Workbook)),
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
        writer.write_object_value("analytics", self.analytics)
        writer.write_object_value("audio", self.audio)
        writer.write_object_value("bundle", self.bundle)
        writer.write_str_value("cTag", self.c_tag)
        writer.write_collection_of_object_values("children", self.children)
        writer.write_object_value("content", self.content)
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
    

