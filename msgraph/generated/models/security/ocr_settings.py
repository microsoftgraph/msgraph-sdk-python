from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class OcrSettings(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Indicates whether or not OCR is enabled for the case.
    is_enabled: Optional[bool] = None
    # Maximum image size that will be processed in KB).
    max_image_size: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The timeout duration for the OCR engine. A longer timeout might increase success of OCR, but might add to the total processing time.
    timeout: Optional[datetime.timedelta] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OcrSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OcrSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OcrSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "maxImageSize": lambda n : setattr(self, 'max_image_size', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "timeout": lambda n : setattr(self, 'timeout', n.get_timedelta_value()),
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
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_int_value("maxImageSize", self.max_image_size)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_timedelta_value("timeout", self.timeout)
        writer.write_additional_data_value(self.additional_data)
    

