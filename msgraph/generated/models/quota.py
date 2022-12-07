from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

storage_plan_information = lazy_import('msgraph.generated.models.storage_plan_information')

class Quota(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new quota and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Total space consumed by files in the recycle bin, in bytes. Read-only.
        self._deleted: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Total space remaining before reaching the quota limit, in bytes. Read-only.
        self._remaining: Optional[int] = None
        # Enumeration value that indicates the state of the storage space. Read-only.
        self._state: Optional[str] = None
        # Information about the drive's storage quota plans. Only in Personal OneDrive.
        self._storage_plan_information: Optional[storage_plan_information.StoragePlanInformation] = None
        # Total allowed storage space, in bytes. Read-only.
        self._total: Optional[int] = None
        # Total space used, in bytes. Read-only.
        self._used: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Quota:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Quota
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Quota()
    
    @property
    def deleted(self,) -> Optional[int]:
        """
        Gets the deleted property value. Total space consumed by files in the recycle bin, in bytes. Read-only.
        Returns: Optional[int]
        """
        return self._deleted
    
    @deleted.setter
    def deleted(self,value: Optional[int] = None) -> None:
        """
        Sets the deleted property value. Total space consumed by files in the recycle bin, in bytes. Read-only.
        Args:
            value: Value to set for the deleted property.
        """
        self._deleted = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "deleted": lambda n : setattr(self, 'deleted', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remaining": lambda n : setattr(self, 'remaining', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "storage_plan_information": lambda n : setattr(self, 'storage_plan_information', n.get_object_value(storage_plan_information.StoragePlanInformation)),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
            "used": lambda n : setattr(self, 'used', n.get_int_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def remaining(self,) -> Optional[int]:
        """
        Gets the remaining property value. Total space remaining before reaching the quota limit, in bytes. Read-only.
        Returns: Optional[int]
        """
        return self._remaining
    
    @remaining.setter
    def remaining(self,value: Optional[int] = None) -> None:
        """
        Sets the remaining property value. Total space remaining before reaching the quota limit, in bytes. Read-only.
        Args:
            value: Value to set for the remaining property.
        """
        self._remaining = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("deleted", self.deleted)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("remaining", self.remaining)
        writer.write_str_value("state", self.state)
        writer.write_object_value("storagePlanInformation", self.storage_plan_information)
        writer.write_int_value("total", self.total)
        writer.write_int_value("used", self.used)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[str]:
        """
        Gets the state property value. Enumeration value that indicates the state of the storage space. Read-only.
        Returns: Optional[str]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[str] = None) -> None:
        """
        Sets the state property value. Enumeration value that indicates the state of the storage space. Read-only.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def storage_plan_information(self,) -> Optional[storage_plan_information.StoragePlanInformation]:
        """
        Gets the storagePlanInformation property value. Information about the drive's storage quota plans. Only in Personal OneDrive.
        Returns: Optional[storage_plan_information.StoragePlanInformation]
        """
        return self._storage_plan_information
    
    @storage_plan_information.setter
    def storage_plan_information(self,value: Optional[storage_plan_information.StoragePlanInformation] = None) -> None:
        """
        Sets the storagePlanInformation property value. Information about the drive's storage quota plans. Only in Personal OneDrive.
        Args:
            value: Value to set for the storagePlanInformation property.
        """
        self._storage_plan_information = value
    
    @property
    def total(self,) -> Optional[int]:
        """
        Gets the total property value. Total allowed storage space, in bytes. Read-only.
        Returns: Optional[int]
        """
        return self._total
    
    @total.setter
    def total(self,value: Optional[int] = None) -> None:
        """
        Sets the total property value. Total allowed storage space, in bytes. Read-only.
        Args:
            value: Value to set for the total property.
        """
        self._total = value
    
    @property
    def used(self,) -> Optional[int]:
        """
        Gets the used property value. Total space used, in bytes. Read-only.
        Returns: Optional[int]
        """
        return self._used
    
    @used.setter
    def used(self,value: Optional[int] = None) -> None:
        """
        Sets the used property value. Total space used, in bytes. Read-only.
        Args:
            value: Value to set for the used property.
        """
        self._used = value
    

