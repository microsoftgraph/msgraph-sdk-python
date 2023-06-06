from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import storage_plan_information

@dataclass
class Quota(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Total space consumed by files in the recycle bin, in bytes. Read-only.
    deleted: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Total space remaining before reaching the quota limit, in bytes. Read-only.
    remaining: Optional[int] = None
    # Enumeration value that indicates the state of the storage space. Read-only.
    state: Optional[str] = None
    # Information about the drive's storage quota plans. Only in Personal OneDrive.
    storage_plan_information: Optional[storage_plan_information.StoragePlanInformation] = None
    # Total allowed storage space, in bytes. Read-only.
    total: Optional[int] = None
    # Total space used, in bytes. Read-only.
    used: Optional[int] = None
    
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
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import storage_plan_information

        fields: Dict[str, Callable[[Any], None]] = {
            "deleted": lambda n : setattr(self, 'deleted', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "remaining": lambda n : setattr(self, 'remaining', n.get_int_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "storagePlanInformation": lambda n : setattr(self, 'storage_plan_information', n.get_object_value(storage_plan_information.StoragePlanInformation)),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
            "used": lambda n : setattr(self, 'used', n.get_int_value()),
        }
        return fields
    
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
    

