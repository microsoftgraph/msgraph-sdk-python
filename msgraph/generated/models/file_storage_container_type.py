from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .entity import Entity
    from .file_storage_container_billing_classification import FileStorageContainerBillingClassification
    from .file_storage_container_billing_status import FileStorageContainerBillingStatus
    from .file_storage_container_type_settings import FileStorageContainerTypeSettings

from .entity import Entity

@dataclass
class FileStorageContainerType(Entity, Parsable):
    # The billingClassification property
    billing_classification: Optional[FileStorageContainerBillingClassification] = None
    # The billingStatus property
    billing_status: Optional[FileStorageContainerBillingStatus] = None
    # The creation date. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # Used in update scenarios for optimistic concurrency control. Read-only.
    etag: Optional[str] = None
    # The expiration date. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    expiration_date_time: Optional[datetime.datetime] = None
    # The name of the fileStorageContainerType.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # ID of the application that owns the fileStorageContainerType.
    owning_app_id: Optional[UUID] = None
    # The settings property
    settings: Optional[FileStorageContainerTypeSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileStorageContainerType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileStorageContainerType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileStorageContainerType()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .file_storage_container_billing_classification import FileStorageContainerBillingClassification
        from .file_storage_container_billing_status import FileStorageContainerBillingStatus
        from .file_storage_container_type_settings import FileStorageContainerTypeSettings

        from .entity import Entity
        from .file_storage_container_billing_classification import FileStorageContainerBillingClassification
        from .file_storage_container_billing_status import FileStorageContainerBillingStatus
        from .file_storage_container_type_settings import FileStorageContainerTypeSettings

        fields: dict[str, Callable[[Any], None]] = {
            "billingClassification": lambda n : setattr(self, 'billing_classification', n.get_enum_value(FileStorageContainerBillingClassification)),
            "billingStatus": lambda n : setattr(self, 'billing_status', n.get_enum_value(FileStorageContainerBillingStatus)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "etag": lambda n : setattr(self, 'etag', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "owningAppId": lambda n : setattr(self, 'owning_app_id', n.get_uuid_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(FileStorageContainerTypeSettings)),
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
        writer.write_enum_value("billingClassification", self.billing_classification)
        writer.write_enum_value("billingStatus", self.billing_status)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("etag", self.etag)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("name", self.name)
        writer.write_uuid_value("owningAppId", self.owning_app_id)
        writer.write_object_value("settings", self.settings)
    

