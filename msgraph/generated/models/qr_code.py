from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .qr_code_image_details import QrCodeImageDetails

from .entity import Entity

@dataclass
class QrCode(Entity, Parsable):
    # The date and time when the QR code was created. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The date and time when the QR code expires. For standard QR codes, the lifetime is in days with a maximum of 395 days (13 months) and a default of 365 days. For temporary QR codes, the lifetime must be between 1-12 hours. The expireDateTime can be edited for standard QR codes but not for temporary QR codes.
    expire_date_time: Optional[datetime.datetime] = None
    # The QR code image data. This property is only returned at the time of creating or resetting the QR code because the private key isn't stored on the server.
    image: Optional[QrCodeImageDetails] = None
    # The date and time when the QR code was last successfully used for authentication. Read-only.
    last_used_date_time: Optional[datetime.datetime] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The date and time when the QR code becomes available for use.
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> QrCode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QrCode
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return QrCode()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .qr_code_image_details import QrCodeImageDetails

        from .entity import Entity
        from .qr_code_image_details import QrCodeImageDetails

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "expireDateTime": lambda n : setattr(self, 'expire_date_time', n.get_datetime_value()),
            "image": lambda n : setattr(self, 'image', n.get_object_value(QrCodeImageDetails)),
            "lastUsedDateTime": lambda n : setattr(self, 'last_used_date_time', n.get_datetime_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_datetime_value("expireDateTime", self.expire_date_time)
        writer.write_object_value("image", self.image)
        writer.write_datetime_value("lastUsedDateTime", self.last_used_date_time)
        writer.write_datetime_value("startDateTime", self.start_date_time)
    

