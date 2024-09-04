from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .coachmark_location_type import CoachmarkLocationType

@dataclass
class CoachmarkLocation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Length of coachmark.
    length: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Offset of coachmark.
    offset: Optional[int] = None
    # Type of coachmark location. The possible values are: unknown, fromEmail, subject, externalTag, displayName, messageBody, unknownFutureValue.
    type: Optional[CoachmarkLocationType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CoachmarkLocation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CoachmarkLocation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CoachmarkLocation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .coachmark_location_type import CoachmarkLocationType

        from .coachmark_location_type import CoachmarkLocationType

        fields: Dict[str, Callable[[Any], None]] = {
            "length": lambda n : setattr(self, 'length', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "offset": lambda n : setattr(self, 'offset', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(CoachmarkLocationType)),
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
        writer.write_int_value("length", self.length)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("offset", self.offset)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

