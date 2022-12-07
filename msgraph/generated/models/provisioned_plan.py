from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ProvisionedPlan(AdditionalDataHolder, Parsable):
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
    def capability_status(self,) -> Optional[str]:
        """
        Gets the capabilityStatus property value. For example, 'Enabled'.
        Returns: Optional[str]
        """
        return self._capability_status
    
    @capability_status.setter
    def capability_status(self,value: Optional[str] = None) -> None:
        """
        Sets the capabilityStatus property value. For example, 'Enabled'.
        Args:
            value: Value to set for the capabilityStatus property.
        """
        self._capability_status = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new provisionedPlan and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # For example, 'Enabled'.
        self._capability_status: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # For example, 'Success'.
        self._provisioning_status: Optional[str] = None
        # The name of the service; for example, 'AccessControlS2S'
        self._service: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProvisionedPlan:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProvisionedPlan
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProvisionedPlan()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "capability_status": lambda n : setattr(self, 'capability_status', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "provisioning_status": lambda n : setattr(self, 'provisioning_status', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
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
    
    @property
    def provisioning_status(self,) -> Optional[str]:
        """
        Gets the provisioningStatus property value. For example, 'Success'.
        Returns: Optional[str]
        """
        return self._provisioning_status
    
    @provisioning_status.setter
    def provisioning_status(self,value: Optional[str] = None) -> None:
        """
        Sets the provisioningStatus property value. For example, 'Success'.
        Args:
            value: Value to set for the provisioningStatus property.
        """
        self._provisioning_status = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("capabilityStatus", self.capability_status)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("provisioningStatus", self.provisioning_status)
        writer.write_str_value("service", self.service)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def service(self,) -> Optional[str]:
        """
        Gets the service property value. The name of the service; for example, 'AccessControlS2S'
        Returns: Optional[str]
        """
        return self._service
    
    @service.setter
    def service(self,value: Optional[str] = None) -> None:
        """
        Sets the service property value. The name of the service; for example, 'AccessControlS2S'
        Args:
            value: Value to set for the service property.
        """
        self._service = value
    

