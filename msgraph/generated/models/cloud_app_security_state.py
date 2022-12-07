from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class CloudAppSecurityState(AdditionalDataHolder, Parsable):
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
        Instantiates a new cloudAppSecurityState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Destination IP Address of the connection to the cloud application/service.
        self._destination_service_ip: Optional[str] = None
        # Cloud application/service name (for example 'Salesforce', 'DropBox', etc.).
        self._destination_service_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Provider-generated/calculated risk score of the Cloud Application/Service. Recommended value range of 0-1, which equates to a percentage.
        self._risk_score: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudAppSecurityState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CloudAppSecurityState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CloudAppSecurityState()
    
    @property
    def destination_service_ip(self,) -> Optional[str]:
        """
        Gets the destinationServiceIp property value. Destination IP Address of the connection to the cloud application/service.
        Returns: Optional[str]
        """
        return self._destination_service_ip
    
    @destination_service_ip.setter
    def destination_service_ip(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationServiceIp property value. Destination IP Address of the connection to the cloud application/service.
        Args:
            value: Value to set for the destinationServiceIp property.
        """
        self._destination_service_ip = value
    
    @property
    def destination_service_name(self,) -> Optional[str]:
        """
        Gets the destinationServiceName property value. Cloud application/service name (for example 'Salesforce', 'DropBox', etc.).
        Returns: Optional[str]
        """
        return self._destination_service_name
    
    @destination_service_name.setter
    def destination_service_name(self,value: Optional[str] = None) -> None:
        """
        Sets the destinationServiceName property value. Cloud application/service name (for example 'Salesforce', 'DropBox', etc.).
        Args:
            value: Value to set for the destinationServiceName property.
        """
        self._destination_service_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "destination_service_ip": lambda n : setattr(self, 'destination_service_ip', n.get_str_value()),
            "destination_service_name": lambda n : setattr(self, 'destination_service_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "risk_score": lambda n : setattr(self, 'risk_score', n.get_str_value()),
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
    def risk_score(self,) -> Optional[str]:
        """
        Gets the riskScore property value. Provider-generated/calculated risk score of the Cloud Application/Service. Recommended value range of 0-1, which equates to a percentage.
        Returns: Optional[str]
        """
        return self._risk_score
    
    @risk_score.setter
    def risk_score(self,value: Optional[str] = None) -> None:
        """
        Sets the riskScore property value. Provider-generated/calculated risk score of the Cloud Application/Service. Recommended value range of 0-1, which equates to a percentage.
        Args:
            value: Value to set for the riskScore property.
        """
        self._risk_score = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("destinationServiceIp", self.destination_service_ip)
        writer.write_str_value("destinationServiceName", self.destination_service_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_additional_data_value(self.additional_data)
    

