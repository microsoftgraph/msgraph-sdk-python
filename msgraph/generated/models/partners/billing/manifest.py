from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...entity import Entity
    from .blob import Blob

from ...entity import Entity

@dataclass
class Manifest(Entity, Parsable):
    # The total file count for this partner tenant ID.
    blob_count: Optional[int] = None
    # A collection of blob objects that contain details of all the files for the partner tenant ID.
    blobs: Optional[list[Blob]] = None
    # The date and time when a manifest resource was created. The timestamp type represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The billing data file format. The possible value is: compressedJSONLines. Each blob is a compressed file and data in the file is in JSON lines format. Decompress the file to access the data.
    data_format: Optional[str] = None
    # Version of data represented by the manifest. Any change in eTag indicates a new data version.
    e_tag: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the division of data. If a given partition has more than the supported number, the data is split into multiple files, each file representing a specific partitionValue. By default, the data in the file is partitioned by the number of line items.
    partition_type: Optional[str] = None
    # The Microsoft Entra tenant ID of the partner.
    partner_tenant_id: Optional[str] = None
    # The root directory that contains all the files.
    root_directory: Optional[str] = None
    # The SAS token for accessing the directory or an individual file in the directory.
    sas_token: Optional[str] = None
    # The version of the manifest schema.
    schema_version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Manifest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Manifest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Manifest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ...entity import Entity
        from .blob import Blob

        from ...entity import Entity
        from .blob import Blob

        fields: dict[str, Callable[[Any], None]] = {
            "blobCount": lambda n : setattr(self, 'blob_count', n.get_int_value()),
            "blobs": lambda n : setattr(self, 'blobs', n.get_collection_of_object_values(Blob)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "dataFormat": lambda n : setattr(self, 'data_format', n.get_str_value()),
            "eTag": lambda n : setattr(self, 'e_tag', n.get_str_value()),
            "partitionType": lambda n : setattr(self, 'partition_type', n.get_str_value()),
            "partnerTenantId": lambda n : setattr(self, 'partner_tenant_id', n.get_str_value()),
            "rootDirectory": lambda n : setattr(self, 'root_directory', n.get_str_value()),
            "sasToken": lambda n : setattr(self, 'sas_token', n.get_str_value()),
            "schemaVersion": lambda n : setattr(self, 'schema_version', n.get_str_value()),
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
        writer.write_int_value("blobCount", self.blob_count)
        writer.write_collection_of_object_values("blobs", self.blobs)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("dataFormat", self.data_format)
        writer.write_str_value("eTag", self.e_tag)
        writer.write_str_value("partitionType", self.partition_type)
        writer.write_str_value("partnerTenantId", self.partner_tenant_id)
        writer.write_str_value("rootDirectory", self.root_directory)
        writer.write_str_value("sasToken", self.sas_token)
        writer.write_str_value("schemaVersion", self.schema_version)
    

