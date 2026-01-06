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
    from .file_storage_container_type_app_permission_grant import FileStorageContainerTypeAppPermissionGrant
    from .file_storage_container_type_registration_settings import FileStorageContainerTypeRegistrationSettings

from .entity import Entity

@dataclass
class FileStorageContainerTypeRegistration(Entity, Parsable):
    # Access privileges of applications on containers.
    application_permission_grants: Optional[list[FileStorageContainerTypeAppPermissionGrant]] = None
    # The billingClassification property
    billing_classification: Optional[FileStorageContainerBillingClassification] = None
    # The billingStatus property
    billing_status: Optional[FileStorageContainerBillingStatus] = None
    # Used in update scenarios for optimistic concurrency control. Read-only.
    etag: Optional[str] = None
    # The expiration date. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    expiration_date_time: Optional[datetime.datetime] = None
    # The name of the fileStorageContainerTypeRegistration. Read-only.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # ID of the application that owns the fileStorageContainerType. Read-only.
    owning_app_id: Optional[UUID] = None
    # The registration date. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
    registered_date_time: Optional[datetime.datetime] = None
    # The settings property
    settings: Optional[FileStorageContainerTypeRegistrationSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileStorageContainerTypeRegistration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileStorageContainerTypeRegistration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileStorageContainerTypeRegistration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .file_storage_container_billing_classification import FileStorageContainerBillingClassification
        from .file_storage_container_billing_status import FileStorageContainerBillingStatus
        from .file_storage_container_type_app_permission_grant import FileStorageContainerTypeAppPermissionGrant
        from .file_storage_container_type_registration_settings import FileStorageContainerTypeRegistrationSettings

        from .entity import Entity
        from .file_storage_container_billing_classification import FileStorageContainerBillingClassification
        from .file_storage_container_billing_status import FileStorageContainerBillingStatus
        from .file_storage_container_type_app_permission_grant import FileStorageContainerTypeAppPermissionGrant
        from .file_storage_container_type_registration_settings import FileStorageContainerTypeRegistrationSettings

        fields: dict[str, Callable[[Any], None]] = {
            "applicationPermissionGrants": lambda n : setattr(self, 'application_permission_grants', n.get_collection_of_object_values(FileStorageContainerTypeAppPermissionGrant)),
            "billingClassification": lambda n : setattr(self, 'billing_classification', n.get_enum_value(FileStorageContainerBillingClassification)),
            "billingStatus": lambda n : setattr(self, 'billing_status', n.get_enum_value(FileStorageContainerBillingStatus)),
            "etag": lambda n : setattr(self, 'etag', n.get_str_value()),
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "owningAppId": lambda n : setattr(self, 'owning_app_id', n.get_uuid_value()),
            "registeredDateTime": lambda n : setattr(self, 'registered_date_time', n.get_datetime_value()),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(FileStorageContainerTypeRegistrationSettings)),
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
        writer.write_collection_of_object_values("applicationPermissionGrants", self.application_permission_grants)
        writer.write_enum_value("billingClassification", self.billing_classification)
        writer.write_enum_value("billingStatus", self.billing_status)
        writer.write_str_value("etag", self.etag)
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_str_value("name", self.name)
        writer.write_uuid_value("owningAppId", self.owning_app_id)
        writer.write_datetime_value("registeredDateTime", self.registered_date_time)
        writer.write_object_value("settings", self.settings)
    

