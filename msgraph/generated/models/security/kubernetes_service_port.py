from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .container_port_protocol import ContainerPortProtocol

@dataclass
class KubernetesServicePort(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The application protocol for this port.
    app_protocol: Optional[str] = None
    # The name of this port within the service.
    name: Optional[str] = None
    # The port on each node on which this service is exposed when the type is either NodePort or LoadBalancer.
    node_port: Optional[int] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The port that this service exposes.
    port: Optional[int] = None
    # The protocol name. The possible values are: udp, tcp, sctp, unknownFutureValue.
    protocol: Optional[ContainerPortProtocol] = None
    # The name or number of the port to access on the pods targeted by the service. The port number must be in the range 1 to 65535. The name must be an IANASVCNAME.
    target_port: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KubernetesServicePort:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KubernetesServicePort
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return KubernetesServicePort()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .container_port_protocol import ContainerPortProtocol

        from .container_port_protocol import ContainerPortProtocol

        fields: dict[str, Callable[[Any], None]] = {
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
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("appProtocol", self.app_protocol)
        writer.write_str_value("name", self.name)
        writer.write_int_value("nodePort", self.node_port)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("port", self.port)
        writer.write_enum_value("protocol", self.protocol)
        writer.write_str_value("targetPort", self.target_port)
        writer.write_additional_data_value(self.additional_data)
    

