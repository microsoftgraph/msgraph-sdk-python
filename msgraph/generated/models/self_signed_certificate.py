from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class SelfSignedCertificate(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Custom key identifier.
    custom_key_identifier: Optional[bytes] = None
    # The friendly name for the key.
    display_name: Optional[str] = None
    # The date and time at which the credential expires. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z.
    end_date_time: Optional[datetime.datetime] = None
    # The value for the key credential. Should be a Base-64 encoded value.
    key: Optional[bytes] = None
    # The unique identifier (GUID) for the key.
    key_id: Optional[UUID] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time at which the credential becomes valid. The timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on January 1, 2014 is 2014-01-01T00:00:00Z.
    start_date_time: Optional[datetime.datetime] = None
    # The thumbprint value for the key.
    thumbprint: Optional[str] = None
    # The type of key credential. AsymmetricX509Cert.
    type: Optional[str] = None
    # A string that describes the purpose for which the key can be used. The possible value is Verify.
    usage: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SelfSignedCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SelfSignedCertificate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SelfSignedCertificate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "customKeyIdentifier": lambda n : setattr(self, 'custom_key_identifier', n.get_bytes_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "key": lambda n : setattr(self, 'key', n.get_bytes_value()),
            "keyId": lambda n : setattr(self, 'key_id', n.get_uuid_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "thumbprint": lambda n : setattr(self, 'thumbprint', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "usage": lambda n : setattr(self, 'usage', n.get_str_value()),
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
        writer.write_bytes_value("customKeyIdentifier", self.custom_key_identifier)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_bytes_value("key", self.key)
        writer.write_uuid_value("keyId", self.key_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("thumbprint", self.thumbprint)
        writer.write_str_value("type", self.type)
        writer.write_str_value("usage", self.usage)
        writer.write_additional_data_value(self.additional_data)
    

