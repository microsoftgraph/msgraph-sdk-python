from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UploadSession(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The date and time in UTC that the upload session expires. The complete file must be uploaded before this expiration time is reached. Each fragment uploaded during the session extends the expiration time.
    expiration_date_time: Optional[datetime.datetime] = None
    # A collection of byte ranges that the server is missing for the file. These ranges are zero indexed and of the format 'start-end' (for example '0-26' to indicate the first 27 bytes of the file). When uploading files as Outlook attachments, instead of a collection of ranges, this property always indicates a single value '{start}', the location in the file where the next upload should begin.
    next_expected_ranges: Optional[list[str]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The URL endpoint that accepts PUT requests for byte ranges of the file.
    upload_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UploadSession:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UploadSession
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UploadSession()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "expirationDateTime": lambda n : setattr(self, 'expiration_date_time', n.get_datetime_value()),
            "nextExpectedRanges": lambda n : setattr(self, 'next_expected_ranges', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "uploadUrl": lambda n : setattr(self, 'upload_url', n.get_str_value()),
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
        writer.write_datetime_value("expirationDateTime", self.expiration_date_time)
        writer.write_collection_of_primitive_values("nextExpectedRanges", self.next_expected_ranges)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("uploadUrl", self.upload_url)
        writer.write_additional_data_value(self.additional_data)
    

