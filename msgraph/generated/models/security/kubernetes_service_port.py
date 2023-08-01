from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .container_port_protocol import ContainerPortProtocol

@dataclass
class KubernetesServicePort(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The appProtocol property
    app_protocol: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The nodePort property
    node_port: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The port property
    port: Optional[int] = None
    # The protocol property
    protocol: Optional[ContainerPortProtocol] = None
    # The targetPort property
    target_port: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> KubernetesServicePort:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KubernetesServicePort
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return KubernetesServicePort()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .container_port_protocol import ContainerPortProtocol

        from .container_port_protocol import ContainerPortProtocol

        fields: Dict[str, Callable[[Any], None]] = {
            "appProtocol": lambda n : setattr(self, 'app_protocol', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "nodePort": lambda n : setattr(self, 'node_port', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "protocol": lambda n : setattr(self, 'protocol', n.get_enum_value(ContainerPortProtocol)),
            "targetPort": lambda n : setattr(self, 'target_port', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("appProtocol", self.app_protocol)
        writer.write_str_value("name", self.name)
        writer.write_int_value("nodePort", self.node_port)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("port", self.port)
        writer.write_enum_value("protocol", self.protocol)
        writer.write_str_value("targetPort", self.target_port)
        writer.write_additional_data_value(self.additional_data)
    

