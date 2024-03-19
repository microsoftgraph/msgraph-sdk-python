from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_gallery_image_status import CloudPcGalleryImageStatus
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcGalleryImage(Entity):
    # The displayName property
    display_name: Optional[str] = None
    # The endDate property
    end_date: Optional[datetime.date] = None
    # The expirationDate property
    expiration_date: Optional[datetime.date] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The offerName property
    offer_name: Optional[str] = None
    # The publisherName property
    publisher_name: Optional[str] = None
    # The sizeInGB property
    size_in_g_b: Optional[int] = None
    # The skuName property
    sku_name: Optional[str] = None
    # The startDate property
    start_date: Optional[datetime.date] = None
    # The status property
    status: Optional[CloudPcGalleryImageStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcGalleryImage:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcGalleryImage
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcGalleryImage()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_gallery_image_status import CloudPcGalleryImageStatus
        from .entity import Entity

        from .cloud_pc_gallery_image_status import CloudPcGalleryImageStatus
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "endDate": lambda n : setattr(self, 'end_date', n.get_date_value()),
            "expirationDate": lambda n : setattr(self, 'expiration_date', n.get_date_value()),
            "offerName": lambda n : setattr(self, 'offer_name', n.get_str_value()),
            "publisherName": lambda n : setattr(self, 'publisher_name', n.get_str_value()),
            "sizeInGB": lambda n : setattr(self, 'size_in_g_b', n.get_int_value()),
            "skuName": lambda n : setattr(self, 'sku_name', n.get_str_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_date_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CloudPcGalleryImageStatus)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("displayName", self.display_name)
        writer.write_date_value("endDate", self.end_date)
        writer.write_date_value("expirationDate", self.expiration_date)
        writer.write_str_value("offerName", self.offer_name)
        writer.write_str_value("publisherName", self.publisher_name)
        writer.write_int_value("sizeInGB", self.size_in_g_b)
        writer.write_str_value("skuName", self.sku_name)
        writer.write_date_value("startDate", self.start_date)
        writer.write_enum_value("status", self.status)
    

