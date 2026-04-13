from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .error_correction_level import ErrorCorrectionLevel

@dataclass
class QrCodeImageDetails(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The binary representation of the QR code image.
    binary_value: Optional[bytes] = None
    # The error correction level of the QR code, which determines how much of the QR code can be damaged while still being readable. The possible values are: l, m, q, h, unknownFutureValue.
    error_correction_level: Optional[ErrorCorrectionLevel] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The raw encoded content embedded in the QR code.
    raw_content: Optional[bytes] = None
    # The version number of the QR code, which determines its size and data capacity.
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> QrCodeImageDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QrCodeImageDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return QrCodeImageDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .error_correction_level import ErrorCorrectionLevel

        from .error_correction_level import ErrorCorrectionLevel

        fields: dict[str, Callable[[Any], None]] = {
            "binaryValue": lambda n : setattr(self, 'binary_value', n.get_bytes_value()),
            "errorCorrectionLevel": lambda n : setattr(self, 'error_correction_level', n.get_enum_value(ErrorCorrectionLevel)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rawContent": lambda n : setattr(self, 'raw_content', n.get_bytes_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_bytes_value("binaryValue", self.binary_value)
        writer.write_enum_value("errorCorrectionLevel", self.error_correction_level)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bytes_value("rawContent", self.raw_content)
        writer.write_int_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    

