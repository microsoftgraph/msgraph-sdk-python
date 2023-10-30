from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Photo(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Camera manufacturer. Read-only.
    camera_make: Optional[str] = None
    # Camera model. Read-only.
    camera_model: Optional[str] = None
    # The denominator for the exposure time fraction from the camera. Read-only.
    exposure_denominator: Optional[float] = None
    # The numerator for the exposure time fraction from the camera. Read-only.
    exposure_numerator: Optional[float] = None
    # The F-stop value from the camera. Read-only.
    f_number: Optional[float] = None
    # The focal length from the camera. Read-only.
    focal_length: Optional[float] = None
    # The ISO value from the camera. Read-only.
    iso: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The orientation value from the camera. Writable on OneDrive Personal.
    orientation: Optional[int] = None
    # Represents the date and time the photo was taken. Read-only.
    taken_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Photo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Photo
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Photo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "camera_make": lambda n : setattr(self, 'camera_make', n.get_str_value()),
            "camera_model": lambda n : setattr(self, 'camera_model', n.get_str_value()),
            "exposure_denominator": lambda n : setattr(self, 'exposure_denominator', n.get_float_value()),
            "exposure_numerator": lambda n : setattr(self, 'exposure_numerator', n.get_float_value()),
            "f_number": lambda n : setattr(self, 'f_number', n.get_float_value()),
            "focal_length": lambda n : setattr(self, 'focal_length', n.get_float_value()),
            "iso": lambda n : setattr(self, 'iso', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "orientation": lambda n : setattr(self, 'orientation', n.get_int_value()),
            "taken_date_time": lambda n : setattr(self, 'taken_date_time', n.get_datetime_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("camera_make", self.camera_make)
        writer.write_str_value("camera_model", self.camera_model)
        writer.write_float_value("exposure_denominator", self.exposure_denominator)
        writer.write_float_value("exposure_numerator", self.exposure_numerator)
        writer.write_float_value("f_number", self.f_number)
        writer.write_float_value("focal_length", self.focal_length)
        writer.write_int_value("iso", self.iso)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("orientation", self.orientation)
        writer.write_datetime_value("taken_date_time", self.taken_date_time)
        writer.write_additional_data_value(self.additional_data)
    

