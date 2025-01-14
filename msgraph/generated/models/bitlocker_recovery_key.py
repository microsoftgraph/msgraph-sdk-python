from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .volume_type import VolumeType

from .entity import Entity

@dataclass
class BitlockerRecoveryKey(Entity, Parsable):
    # The date and time when the key was originally backed up to Microsoft Entra ID. Not nullable.
    created_date_time: Optional[datetime.datetime] = None
    # Identifier of the device the BitLocker key is originally backed up from. Supports $filter (eq).
    device_id: Optional[str] = None
    # The BitLocker recovery key. Returned only on $select. Not nullable.
    key: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates the type of volume the BitLocker key is associated with. The possible values are: 1 (for operatingSystemVolume), 2 (for fixedDataVolume), 3 (for removableDataVolume), and 4 (for unknownFutureValue).
    volume_type: Optional[VolumeType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BitlockerRecoveryKey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BitlockerRecoveryKey
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BitlockerRecoveryKey()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .volume_type import VolumeType

        from .entity import Entity
        from .volume_type import VolumeType

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deviceId": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "volumeType": lambda n : setattr(self, 'volume_type', n.get_enum_value(VolumeType)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("key", self.key)
        writer.write_enum_value("volumeType", self.volume_type)
    

