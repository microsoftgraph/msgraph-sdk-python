from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
volume_type = lazy_import('msgraph.generated.models.volume_type')

class BitlockerRecoveryKey(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new bitlockerRecoveryKey and sets the default values.
        """
        super().__init__()
        # The date and time when the key was originally backed up to Azure Active Directory. Not nullable.
        self._created_date_time: Optional[datetime] = None
        # Identifier of the device the BitLocker key is originally backed up from. Supports $filter (eq).
        self._device_id: Optional[str] = None
        # The BitLocker recovery key. Returned only on $select. Not nullable.
        self._key: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Indicates the type of volume the BitLocker key is associated with. The possible values are: 1 (for operatingSystemVolume), 2 (for fixedDataVolume), 3 (for removableDataVolume), and 4 (for unknownFutureValue).
        self._volume_type: Optional[volume_type.VolumeType] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. The date and time when the key was originally backed up to Azure Active Directory. Not nullable.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. The date and time when the key was originally backed up to Azure Active Directory. Not nullable.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> BitlockerRecoveryKey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: BitlockerRecoveryKey
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return BitlockerRecoveryKey()
    
    @property
    def device_id(self,) -> Optional[str]:
        """
        Gets the deviceId property value. Identifier of the device the BitLocker key is originally backed up from. Supports $filter (eq).
        Returns: Optional[str]
        """
        return self._device_id
    
    @device_id.setter
    def device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceId property value. Identifier of the device the BitLocker key is originally backed up from. Supports $filter (eq).
        Args:
            value: Value to set for the deviceId property.
        """
        self._device_id = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "device_id": lambda n : setattr(self, 'device_id', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "volume_type": lambda n : setattr(self, 'volume_type', n.get_enum_value(volume_type.VolumeType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def key(self,) -> Optional[str]:
        """
        Gets the key property value. The BitLocker recovery key. Returned only on $select. Not nullable.
        Returns: Optional[str]
        """
        return self._key
    
    @key.setter
    def key(self,value: Optional[str] = None) -> None:
        """
        Sets the key property value. The BitLocker recovery key. Returned only on $select. Not nullable.
        Args:
            value: Value to set for the key property.
        """
        self._key = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("deviceId", self.device_id)
        writer.write_str_value("key", self.key)
        writer.write_enum_value("volumeType", self.volume_type)
    
    @property
    def volume_type(self,) -> Optional[volume_type.VolumeType]:
        """
        Gets the volumeType property value. Indicates the type of volume the BitLocker key is associated with. The possible values are: 1 (for operatingSystemVolume), 2 (for fixedDataVolume), 3 (for removableDataVolume), and 4 (for unknownFutureValue).
        Returns: Optional[volume_type.VolumeType]
        """
        return self._volume_type
    
    @volume_type.setter
    def volume_type(self,value: Optional[volume_type.VolumeType] = None) -> None:
        """
        Sets the volumeType property value. Indicates the type of volume the BitLocker key is associated with. The possible values are: 1 (for operatingSystemVolume), 2 (for fixedDataVolume), 3 (for removableDataVolume), and 4 (for unknownFutureValue).
        Args:
            value: Value to set for the volumeType property.
        """
        self._volume_type = value
    

