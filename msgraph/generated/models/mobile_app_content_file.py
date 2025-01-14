from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mobile_app_content_file_upload_state import MobileAppContentFileUploadState

from .entity import Entity

@dataclass
class MobileAppContentFile(Entity, Parsable):
    """
    Contains properties for a single installer file that is associated with a given mobileAppContent version.
    """
    # The Azure Storage URI.
    azure_storage_uri: Optional[str] = None
    # The time the Azure storage Uri expires.
    azure_storage_uri_expiration_date_time: Optional[datetime.datetime] = None
    # The time the file was created.
    created_date_time: Optional[datetime.datetime] = None
    # A value indicating whether the file is committed.
    is_committed: Optional[bool] = None
    # Indicates whether this content file is a dependency for the main content file. TRUE means that the content file is a dependency, FALSE means that the content file is not a dependency and is the main content file. Defaults to FALSE.
    is_dependency: Optional[bool] = None
    # The manifest information.
    manifest: Optional[bytes] = None
    # the file name.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The size of the file prior to encryption.
    size: Optional[int] = None
    # The size of the file after encryption.
    size_encrypted: Optional[int] = None
    # Contains properties for upload request states.
    upload_state: Optional[MobileAppContentFileUploadState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MobileAppContentFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MobileAppContentFile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MobileAppContentFile()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mobile_app_content_file_upload_state import MobileAppContentFileUploadState

        from .entity import Entity
        from .mobile_app_content_file_upload_state import MobileAppContentFileUploadState

        fields: dict[str, Callable[[Any], None]] = {
            "azureStorageUri": lambda n : setattr(self, 'azure_storage_uri', n.get_str_value()),
            "azureStorageUriExpirationDateTime": lambda n : setattr(self, 'azure_storage_uri_expiration_date_time', n.get_datetime_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "isCommitted": lambda n : setattr(self, 'is_committed', n.get_bool_value()),
            "isDependency": lambda n : setattr(self, 'is_dependency', n.get_bool_value()),
            "manifest": lambda n : setattr(self, 'manifest', n.get_bytes_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "sizeEncrypted": lambda n : setattr(self, 'size_encrypted', n.get_int_value()),
            "uploadState": lambda n : setattr(self, 'upload_state', n.get_enum_value(MobileAppContentFileUploadState)),
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
        writer.write_bool_value("isDependency", self.is_dependency)
        writer.write_bytes_value("manifest", self.manifest)
        writer.write_str_value("name", self.name)
        writer.write_int_value("size", self.size)
        writer.write_int_value("sizeEncrypted", self.size_encrypted)
        writer.write_enum_value("uploadState", self.upload_state)
    

