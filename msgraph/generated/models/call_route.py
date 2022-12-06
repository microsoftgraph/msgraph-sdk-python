from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity_set = lazy_import('msgraph.generated.models.identity_set')
routing_type = lazy_import('msgraph.generated.models.routing_type')

class CallRoute(AdditionalDataHolder, Parsable):
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
        Instantiates a new callRoute and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The final property
        self._final: Optional[identity_set.IdentitySet] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The original property
        self._original: Optional[identity_set.IdentitySet] = None
        # The routingType property
        self._routing_type: Optional[routing_type.RoutingType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CallRoute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CallRoute
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CallRoute()
    
    @property
    def final(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the final property value. The final property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._final
    
    @final.setter
    def final(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the final property value. The final property
        Args:
            value: Value to set for the final property.
        """
        self._final = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "final": lambda n : setattr(self, 'final', n.get_object_value(identity_set.IdentitySet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "original": lambda n : setattr(self, 'original', n.get_object_value(identity_set.IdentitySet)),
            "routing_type": lambda n : setattr(self, 'routing_type', n.get_enum_value(routing_type.RoutingType)),
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
    def original(self,) -> Optional[identity_set.IdentitySet]:
        """
        Gets the original property value. The original property
        Returns: Optional[identity_set.IdentitySet]
        """
        return self._original
    
    @original.setter
    def original(self,value: Optional[identity_set.IdentitySet] = None) -> None:
        """
        Sets the original property value. The original property
        Args:
            value: Value to set for the original property.
        """
        self._original = value
    
    @property
    def routing_type(self,) -> Optional[routing_type.RoutingType]:
        """
        Gets the routingType property value. The routingType property
        Returns: Optional[routing_type.RoutingType]
        """
        return self._routing_type
    
    @routing_type.setter
    def routing_type(self,value: Optional[routing_type.RoutingType] = None) -> None:
        """
        Sets the routingType property value. The routingType property
        Args:
            value: Value to set for the routingType property.
        """
        self._routing_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("final", self.final)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("original", self.original)
        writer.write_enum_value("routingType", self.routing_type)
        writer.write_additional_data_value(self.additional_data)
    

