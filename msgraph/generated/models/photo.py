from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class Photo(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def camera_make(self,) -> Optional[str]:
        """
        Gets the cameraMake property value. Camera manufacturer. Read-only.
        Returns: Optional[str]
        """
        return self._camera_make
    
    @camera_make.setter
    def camera_make(self,value: Optional[str] = None) -> None:
        """
        Sets the cameraMake property value. Camera manufacturer. Read-only.
        Args:
            value: Value to set for the cameraMake property.
        """
        self._camera_make = value
    
    @property
    def camera_model(self,) -> Optional[str]:
        """
        Gets the cameraModel property value. Camera model. Read-only.
        Returns: Optional[str]
        """
        return self._camera_model
    
    @camera_model.setter
    def camera_model(self,value: Optional[str] = None) -> None:
        """
        Sets the cameraModel property value. Camera model. Read-only.
        Args:
            value: Value to set for the cameraModel property.
        """
        self._camera_model = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new photo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Camera manufacturer. Read-only.
        self._camera_make: Optional[str] = None
        # Camera model. Read-only.
        self._camera_model: Optional[str] = None
        # The denominator for the exposure time fraction from the camera. Read-only.
        self._exposure_denominator: Optional[float] = None
        # The numerator for the exposure time fraction from the camera. Read-only.
        self._exposure_numerator: Optional[float] = None
        # The F-stop value from the camera. Read-only.
        self._f_number: Optional[float] = None
        # The focal length from the camera. Read-only.
        self._focal_length: Optional[float] = None
        # The ISO value from the camera. Read-only.
        self._iso: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The orientation value from the camera. Writable on OneDrive Personal.
        self._orientation: Optional[int] = None
        # Represents the date and time the photo was taken. Read-only.
        self._taken_date_time: Optional[datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Photo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Photo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Photo()
    
    @property
    def exposure_denominator(self,) -> Optional[float]:
        """
        Gets the exposureDenominator property value. The denominator for the exposure time fraction from the camera. Read-only.
        Returns: Optional[float]
        """
        return self._exposure_denominator
    
    @exposure_denominator.setter
    def exposure_denominator(self,value: Optional[float] = None) -> None:
        """
        Sets the exposureDenominator property value. The denominator for the exposure time fraction from the camera. Read-only.
        Args:
            value: Value to set for the exposureDenominator property.
        """
        self._exposure_denominator = value
    
    @property
    def exposure_numerator(self,) -> Optional[float]:
        """
        Gets the exposureNumerator property value. The numerator for the exposure time fraction from the camera. Read-only.
        Returns: Optional[float]
        """
        return self._exposure_numerator
    
    @exposure_numerator.setter
    def exposure_numerator(self,value: Optional[float] = None) -> None:
        """
        Sets the exposureNumerator property value. The numerator for the exposure time fraction from the camera. Read-only.
        Args:
            value: Value to set for the exposureNumerator property.
        """
        self._exposure_numerator = value
    
    @property
    def f_number(self,) -> Optional[float]:
        """
        Gets the fNumber property value. The F-stop value from the camera. Read-only.
        Returns: Optional[float]
        """
        return self._f_number
    
    @f_number.setter
    def f_number(self,value: Optional[float] = None) -> None:
        """
        Sets the fNumber property value. The F-stop value from the camera. Read-only.
        Args:
            value: Value to set for the fNumber property.
        """
        self._f_number = value
    
    @property
    def focal_length(self,) -> Optional[float]:
        """
        Gets the focalLength property value. The focal length from the camera. Read-only.
        Returns: Optional[float]
        """
        return self._focal_length
    
    @focal_length.setter
    def focal_length(self,value: Optional[float] = None) -> None:
        """
        Sets the focalLength property value. The focal length from the camera. Read-only.
        Args:
            value: Value to set for the focalLength property.
        """
        self._focal_length = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
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
    
    @property
    def iso(self,) -> Optional[int]:
        """
        Gets the iso property value. The ISO value from the camera. Read-only.
        Returns: Optional[int]
        """
        return self._iso
    
    @iso.setter
    def iso(self,value: Optional[int] = None) -> None:
        """
        Sets the iso property value. The ISO value from the camera. Read-only.
        Args:
            value: Value to set for the iso property.
        """
        self._iso = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def orientation(self,) -> Optional[int]:
        """
        Gets the orientation property value. The orientation value from the camera. Writable on OneDrive Personal.
        Returns: Optional[int]
        """
        return self._orientation
    
    @orientation.setter
    def orientation(self,value: Optional[int] = None) -> None:
        """
        Sets the orientation property value. The orientation value from the camera. Writable on OneDrive Personal.
        Args:
            value: Value to set for the orientation property.
        """
        self._orientation = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("cameraMake", self.camera_make)
        writer.write_str_value("cameraModel", self.camera_model)
        writer.write_float_value("exposureDenominator", self.exposure_denominator)
        writer.write_float_value("exposureNumerator", self.exposure_numerator)
        writer.write_float_value("fNumber", self.f_number)
        writer.write_float_value("focalLength", self.focal_length)
        writer.write_int_value("iso", self.iso)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("orientation", self.orientation)
        writer.write_datetime_value("takenDateTime", self.taken_date_time)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def taken_date_time(self,) -> Optional[datetime]:
        """
        Gets the takenDateTime property value. Represents the date and time the photo was taken. Read-only.
        Returns: Optional[datetime]
        """
        return self._taken_date_time
    
    @taken_date_time.setter
    def taken_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the takenDateTime property value. Represents the date and time the photo was taken. Read-only.
        Args:
            value: Value to set for the takenDateTime property.
        """
        self._taken_date_time = value
    

