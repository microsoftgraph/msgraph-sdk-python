from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .drive_item_source import DriveItemSource
    from .file_system_info import FileSystemInfo
    from .media_source import MediaSource

@dataclass
class DriveItemUploadableProperties(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Provides a user-visible description of the item. Read-write. Only on OneDrive Personal.
    description: Optional[str] = None
    # Information about the drive item source. Read-write. Only on OneDrive for Business and SharePoint.
    drive_item_source: Optional[DriveItemSource] = None
    # Provides an expected file size to perform a quota check before uploading. Only on OneDrive Personal.
    file_size: Optional[int] = None
    # File system information on client. Read-write.
    file_system_info: Optional[FileSystemInfo] = None
    # Media source information. Read-write. Only on OneDrive for Business and SharePoint.
    media_source: Optional[MediaSource] = None
    # The name of the item (filename and extension). Read-write.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DriveItemUploadableProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DriveItemUploadableProperties
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DriveItemUploadableProperties()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .drive_item_source import DriveItemSource
        from .file_system_info import FileSystemInfo
        from .media_source import MediaSource

        from .drive_item_source import DriveItemSource
        from .file_system_info import FileSystemInfo
        from .media_source import MediaSource

        fields: dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "driveItemSource": lambda n : setattr(self, 'drive_item_source', n.get_object_value(DriveItemSource)),
            "fileSize": lambda n : setattr(self, 'file_size', n.get_int_value()),
            "fileSystemInfo": lambda n : setattr(self, 'file_system_info', n.get_object_value(FileSystemInfo)),
            "mediaSource": lambda n : setattr(self, 'media_source', n.get_object_value(MediaSource)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("description", self.description)
        writer.write_object_value("driveItemSource", self.drive_item_source)
        writer.write_int_value("fileSize", self.file_size)
        writer.write_object_value("fileSystemInfo", self.file_system_info)
        writer.write_object_value("mediaSource", self.media_source)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

