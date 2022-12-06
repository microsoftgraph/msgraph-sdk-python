from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class UserTrainingContentEventInfo(AdditionalDataHolder, Parsable):
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
    def browser(self,) -> Optional[str]:
        """
        Gets the browser property value. Browser of the user from where the training event was generated.
        Returns: Optional[str]
        """
        return self._browser
    
    @browser.setter
    def browser(self,value: Optional[str] = None) -> None:
        """
        Sets the browser property value. Browser of the user from where the training event was generated.
        Args:
            value: Value to set for the browser property.
        """
        self._browser = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new userTrainingContentEventInfo and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Browser of the user from where the training event was generated.
        self._browser: Optional[str] = None
        # Date and time of the training content playback by the user.
        self._content_date_time: Optional[datetime] = None
        # IP address of the user for the training event.
        self._ip_address: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The operating system, platform, and device details of the user for the training event.
        self._os_platform_device_details: Optional[str] = None
        # Potential improvement in the tenant security posture after completion of the training by the user.
        self._potential_score_impact: Optional[float] = None
    
    @property
    def content_date_time(self,) -> Optional[datetime]:
        """
        Gets the contentDateTime property value. Date and time of the training content playback by the user.
        Returns: Optional[datetime]
        """
        return self._content_date_time
    
    @content_date_time.setter
    def content_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the contentDateTime property value. Date and time of the training content playback by the user.
        Args:
            value: Value to set for the contentDateTime property.
        """
        self._content_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserTrainingContentEventInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserTrainingContentEventInfo
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserTrainingContentEventInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "browser": lambda n : setattr(self, 'browser', n.get_str_value()),
            "content_date_time": lambda n : setattr(self, 'content_date_time', n.get_datetime_value()),
            "ip_address": lambda n : setattr(self, 'ip_address', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "os_platform_device_details": lambda n : setattr(self, 'os_platform_device_details', n.get_str_value()),
            "potential_score_impact": lambda n : setattr(self, 'potential_score_impact', n.get_float_value()),
        }
        return fields
    
    @property
    def ip_address(self,) -> Optional[str]:
        """
        Gets the ipAddress property value. IP address of the user for the training event.
        Returns: Optional[str]
        """
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddress property value. IP address of the user for the training event.
        Args:
            value: Value to set for the ipAddress property.
        """
        self._ip_address = value
    
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
    def os_platform_device_details(self,) -> Optional[str]:
        """
        Gets the osPlatformDeviceDetails property value. The operating system, platform, and device details of the user for the training event.
        Returns: Optional[str]
        """
        return self._os_platform_device_details
    
    @os_platform_device_details.setter
    def os_platform_device_details(self,value: Optional[str] = None) -> None:
        """
        Sets the osPlatformDeviceDetails property value. The operating system, platform, and device details of the user for the training event.
        Args:
            value: Value to set for the osPlatformDeviceDetails property.
        """
        self._os_platform_device_details = value
    
    @property
    def potential_score_impact(self,) -> Optional[float]:
        """
        Gets the potentialScoreImpact property value. Potential improvement in the tenant security posture after completion of the training by the user.
        Returns: Optional[float]
        """
        return self._potential_score_impact
    
    @potential_score_impact.setter
    def potential_score_impact(self,value: Optional[float] = None) -> None:
        """
        Sets the potentialScoreImpact property value. Potential improvement in the tenant security posture after completion of the training by the user.
        Args:
            value: Value to set for the potentialScoreImpact property.
        """
        self._potential_score_impact = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("browser", self.browser)
        writer.write_datetime_value("contentDateTime", self.content_date_time)
        writer.write_str_value("ipAddress", self.ip_address)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("osPlatformDeviceDetails", self.os_platform_device_details)
        writer.write_float_value("potentialScoreImpact", self.potential_score_impact)
        writer.write_additional_data_value(self.additional_data)
    

