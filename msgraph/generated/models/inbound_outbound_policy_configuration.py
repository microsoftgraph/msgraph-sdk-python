from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

class InboundOutboundPolicyConfiguration(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new inboundOutboundPolicyConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Defines whether external users coming inbound are allowed.
        self._inbound_allowed: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Defines whether internal users are allowed to go outbound.
        self._outbound_allowed: Optional[bool] = None
    
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
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> InboundOutboundPolicyConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: InboundOutboundPolicyConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return InboundOutboundPolicyConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "inboundAllowed": lambda n : setattr(self, 'inbound_allowed', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "outboundAllowed": lambda n : setattr(self, 'outbound_allowed', n.get_bool_value()),
        }
        return fields
    
    @property
    def inbound_allowed(self,) -> Optional[bool]:
        """
        Gets the inboundAllowed property value. Defines whether external users coming inbound are allowed.
        Returns: Optional[bool]
        """
        return self._inbound_allowed
    
    @inbound_allowed.setter
    def inbound_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the inboundAllowed property value. Defines whether external users coming inbound are allowed.
        Args:
            value: Value to set for the inbound_allowed property.
        """
        self._inbound_allowed = value
    
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
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    @property
    def outbound_allowed(self,) -> Optional[bool]:
        """
        Gets the outboundAllowed property value. Defines whether internal users are allowed to go outbound.
        Returns: Optional[bool]
        """
        return self._outbound_allowed
    
    @outbound_allowed.setter
    def outbound_allowed(self,value: Optional[bool] = None) -> None:
        """
        Sets the outboundAllowed property value. Defines whether internal users are allowed to go outbound.
        Args:
            value: Value to set for the outbound_allowed property.
        """
        self._outbound_allowed = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("inboundAllowed", self.inbound_allowed)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("outboundAllowed", self.outbound_allowed)
        writer.write_additional_data_value(self.additional_data)
    

