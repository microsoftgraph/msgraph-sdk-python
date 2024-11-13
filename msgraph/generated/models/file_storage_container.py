from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .drive import Drive
    from .entity import Entity
    from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary
    from .file_storage_container_settings import FileStorageContainerSettings
    from .file_storage_container_status import FileStorageContainerStatus
    from .file_storage_container_viewpoint import FileStorageContainerViewpoint
    from .permission import Permission

from .entity import Entity

@dataclass
class FileStorageContainer(Entity, Parsable):
    # Container type ID of the fileStorageContainer. For details about container types, see Container Types. Each container must have only one container type. Read-only.
    container_type_id: Optional[UUID] = None
    # Date and time of the fileStorageContainer creation. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Custom property collection for the fileStorageContainer. Read-write.
    custom_properties: Optional[FileStorageContainerCustomPropertyDictionary] = None
    # Provides a user-visible description of the fileStorageContainer. Read-write.
    description: Optional[str] = None
    # The display name of the fileStorageContainer. Read-write.
    display_name: Optional[str] = None
    # The drive of the resource fileStorageContainer. Read-only.
    drive: Optional[Drive] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The set of permissions for users in the fileStorageContainer. Permission for each user is set by the roles property. The possible values are: reader, writer, manager, and owner. Read-write.
    permissions: Optional[List[Permission]] = None
    # The settings property
    settings: Optional[FileStorageContainerSettings] = None
    # Status of the fileStorageContainer. Containers are created as inactive and require activation. Inactive containers are subjected to automatic deletion in 24 hours. The possible values are: inactive, active. Read-only.
    status: Optional[FileStorageContainerStatus] = None
    # Data specific to the current user. Read-only.
    viewpoint: Optional[FileStorageContainerViewpoint] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileStorageContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileStorageContainer
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileStorageContainer()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .drive import Drive
        from .entity import Entity
        from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary
        from .file_storage_container_settings import FileStorageContainerSettings
        from .file_storage_container_status import FileStorageContainerStatus
        from .file_storage_container_viewpoint import FileStorageContainerViewpoint
        from .permission import Permission

        from .drive import Drive
        from .entity import Entity
        from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary
        from .file_storage_container_settings import FileStorageContainerSettings
        from .file_storage_container_status import FileStorageContainerStatus
        from .file_storage_container_viewpoint import FileStorageContainerViewpoint
        from .permission import Permission

        fields: Dict[str, Callable[[Any], None]] = {
            "containerTypeId": lambda n : setattr(self, 'container_type_id', n.get_uuid_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "customProperties": lambda n : setattr(self, 'custom_properties', n.get_object_value(FileStorageContainerCustomPropertyDictionary)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "drive": lambda n : setattr(self, 'drive', n.get_object_value(Drive)),
            "permissions": lambda n : setattr(self, 'permissions', n.get_collection_of_object_values(Permission)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(FileStorageContainerSettings)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(FileStorageContainerStatus)),
            "viewpoint": lambda n : setattr(self, 'viewpoint', n.get_object_value(FileStorageContainerViewpoint)),
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
        from .drive import Drive
        from .entity import Entity
        from .file_storage_container_custom_property_dictionary import FileStorageContainerCustomPropertyDictionary
        from .file_storage_container_settings import FileStorageContainerSettings
        from .file_storage_container_status import FileStorageContainerStatus
        from .file_storage_container_viewpoint import FileStorageContainerViewpoint
        from .permission import Permission

        writer.write_uuid_value("containerTypeId", self.container_type_id)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("customProperties", self.custom_properties)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_object_value("drive", self.drive)
        writer.write_collection_of_object_values("permissions", self.permissions)
        writer.write_object_value("settings", self.settings)
        writer.write_enum_value("status", self.status)
        writer.write_object_value("viewpoint", self.viewpoint)
    

