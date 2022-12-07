from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class DeviceManagementSettings(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new deviceManagementSettings and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The number of days a device is allowed to go without checking in to remain compliant.
        self._device_compliance_checkin_threshold_days: Optional[int] = None
        # Is feature enabled or not for scheduled action for rule.
        self._is_scheduled_action_enabled: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Device should be noncompliant when there is no compliance policy targeted when this is true
        self._secure_by_default: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceManagementSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceManagementSettings
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DeviceManagementSettings()
    
    @property
    def device_compliance_checkin_threshold_days(self,) -> Optional[int]:
        """
        Gets the deviceComplianceCheckinThresholdDays property value. The number of days a device is allowed to go without checking in to remain compliant.
        Returns: Optional[int]
        """
        return self._device_compliance_checkin_threshold_days
    
    @device_compliance_checkin_threshold_days.setter
    def device_compliance_checkin_threshold_days(self,value: Optional[int] = None) -> None:
        """
        Sets the deviceComplianceCheckinThresholdDays property value. The number of days a device is allowed to go without checking in to remain compliant.
        Args:
            value: Value to set for the deviceComplianceCheckinThresholdDays property.
        """
        self._device_compliance_checkin_threshold_days = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "device_compliance_checkin_threshold_days": lambda n : setattr(self, 'device_compliance_checkin_threshold_days', n.get_int_value()),
            "is_scheduled_action_enabled": lambda n : setattr(self, 'is_scheduled_action_enabled', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "secure_by_default": lambda n : setattr(self, 'secure_by_default', n.get_bool_value()),
        }
        return fields
    
    @property
    def is_scheduled_action_enabled(self,) -> Optional[bool]:
        """
        Gets the isScheduledActionEnabled property value. Is feature enabled or not for scheduled action for rule.
        Returns: Optional[bool]
        """
        return self._is_scheduled_action_enabled
    
    @is_scheduled_action_enabled.setter
    def is_scheduled_action_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isScheduledActionEnabled property value. Is feature enabled or not for scheduled action for rule.
        Args:
            value: Value to set for the isScheduledActionEnabled property.
        """
        self._is_scheduled_action_enabled = value
    
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
    def secure_by_default(self,) -> Optional[bool]:
        """
        Gets the secureByDefault property value. Device should be noncompliant when there is no compliance policy targeted when this is true
        Returns: Optional[bool]
        """
        return self._secure_by_default
    
    @secure_by_default.setter
    def secure_by_default(self,value: Optional[bool] = None) -> None:
        """
        Sets the secureByDefault property value. Device should be noncompliant when there is no compliance policy targeted when this is true
        Args:
            value: Value to set for the secureByDefault property.
        """
        self._secure_by_default = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("deviceComplianceCheckinThresholdDays", self.device_compliance_checkin_threshold_days)
        writer.write_bool_value("isScheduledActionEnabled", self.is_scheduled_action_enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("secureByDefault", self.secure_by_default)
        writer.write_additional_data_value(self.additional_data)
    

