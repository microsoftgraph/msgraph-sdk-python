from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class LicenseUnitsDetail(AdditionalDataHolder, Parsable):
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
        Instantiates a new licenseUnitsDetail and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The number of units that are enabled for the active subscription of the service SKU.
        self._enabled: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The number of units that are suspended because the subscription of the service SKU has been cancelled. The units cannot be assigned but can still be reactivated before they are deleted.
        self._suspended: Optional[int] = None
        # The number of units that are in warning status. When the subscription of the service SKU has expired, the customer has a grace period to renew their subscription before it is cancelled (moved to a suspended state).
        self._warning: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LicenseUnitsDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LicenseUnitsDetail
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LicenseUnitsDetail()
    
    @property
    def enabled(self,) -> Optional[int]:
        """
        Gets the enabled property value. The number of units that are enabled for the active subscription of the service SKU.
        Returns: Optional[int]
        """
        return self._enabled
    
    @enabled.setter
    def enabled(self,value: Optional[int] = None) -> None:
        """
        Sets the enabled property value. The number of units that are enabled for the active subscription of the service SKU.
        Args:
            value: Value to set for the enabled property.
        """
        self._enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "suspended": lambda n : setattr(self, 'suspended', n.get_int_value()),
            "warning": lambda n : setattr(self, 'warning', n.get_int_value()),
        }
        return fields
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("enabled", self.enabled)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("suspended", self.suspended)
        writer.write_int_value("warning", self.warning)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def suspended(self,) -> Optional[int]:
        """
        Gets the suspended property value. The number of units that are suspended because the subscription of the service SKU has been cancelled. The units cannot be assigned but can still be reactivated before they are deleted.
        Returns: Optional[int]
        """
        return self._suspended
    
    @suspended.setter
    def suspended(self,value: Optional[int] = None) -> None:
        """
        Sets the suspended property value. The number of units that are suspended because the subscription of the service SKU has been cancelled. The units cannot be assigned but can still be reactivated before they are deleted.
        Args:
            value: Value to set for the suspended property.
        """
        self._suspended = value
    
    @property
    def warning(self,) -> Optional[int]:
        """
        Gets the warning property value. The number of units that are in warning status. When the subscription of the service SKU has expired, the customer has a grace period to renew their subscription before it is cancelled (moved to a suspended state).
        Returns: Optional[int]
        """
        return self._warning
    
    @warning.setter
    def warning(self,value: Optional[int] = None) -> None:
        """
        Sets the warning property value. The number of units that are in warning status. When the subscription of the service SKU has expired, the customer has a grace period to renew their subscription before it is cancelled (moved to a suspended state).
        Args:
            value: Value to set for the warning property.
        """
        self._warning = value
    

