from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import participant_endpoint, service_endpoint, user_agent

class Endpoint(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new endpoint and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # User-agent reported by this endpoint.
        self._user_agent: Optional[user_agent.UserAgent] = None
    
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
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Endpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Endpoint
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.callRecords.participantEndpoint":
                from . import participant_endpoint

                return participant_endpoint.ParticipantEndpoint()
            if mapping_value == "#microsoft.graph.callRecords.serviceEndpoint":
                from . import service_endpoint

                return service_endpoint.ServiceEndpoint()
        return Endpoint()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import participant_endpoint, service_endpoint, user_agent

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "userAgent": lambda n : setattr(self, 'user_agent', n.get_object_value(user_agent.UserAgent)),
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
            value: Value to set for the odata_type property.
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("userAgent", self.user_agent)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_agent(self,) -> Optional[user_agent.UserAgent]:
        """
        Gets the userAgent property value. User-agent reported by this endpoint.
        Returns: Optional[user_agent.UserAgent]
        """
        return self._user_agent
    
    @user_agent.setter
    def user_agent(self,value: Optional[user_agent.UserAgent] = None) -> None:
        """
        Sets the userAgent property value. User-agent reported by this endpoint.
        Args:
            value: Value to set for the user_agent property.
        """
        self._user_agent = value
    

