from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..long_running_operation_status import LongRunningOperationStatus

@dataclass
class TelephoneNumberLongRunningOperationDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Location of the asynchronous operation. It includes the operation identifier.
    resource_location: Optional[str] = None
    # status of the asynchronous operation. The possible values are: notStarted, running, succeeded, failed, unknownFutureValue.
    status: Optional[LongRunningOperationStatus] = None
    # Indicates the asynchronous operation details.
    status_detail: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TelephoneNumberLongRunningOperationDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TelephoneNumberLongRunningOperationDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TelephoneNumberLongRunningOperationDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..long_running_operation_status import LongRunningOperationStatus

        from ..long_running_operation_status import LongRunningOperationStatus

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceLocation": lambda n : setattr(self, 'resource_location', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(LongRunningOperationStatus)),
            "statusDetail": lambda n : setattr(self, 'status_detail', n.get_str_value()),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("resourceLocation", self.resource_location)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("statusDetail", self.status_detail)
        writer.write_additional_data_value(self.additional_data)
    

