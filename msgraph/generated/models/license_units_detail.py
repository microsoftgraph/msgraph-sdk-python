from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class LicenseUnitsDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The number of units that are enabled for the active subscription of the service SKU.
    enabled: Optional[int] = None
    # The lockedOut property
    locked_out: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The number of units that are suspended because the subscription of the service SKU has been cancelled. The units cannot be assigned but can still be reactivated before they are deleted.
    suspended: Optional[int] = None
    # The number of units that are in warning status. When the subscription of the service SKU has expired, the customer has a grace period to renew their subscription before it is cancelled (moved to a suspended state).
    warning: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LicenseUnitsDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LicenseUnitsDetail
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return LicenseUnitsDetail()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_int_value()),
            "lockedOut": lambda n : setattr(self, 'locked_out', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "suspended": lambda n : setattr(self, 'suspended', n.get_int_value()),
            "warning": lambda n : setattr(self, 'warning', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("enabled", self.enabled)
        writer.write_int_value("lockedOut", self.locked_out)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("suspended", self.suspended)
        writer.write_int_value("warning", self.warning)
        writer.write_additional_data_value(self.additional_data)
    

