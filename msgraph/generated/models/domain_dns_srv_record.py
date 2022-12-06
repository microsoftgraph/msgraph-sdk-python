from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

domain_dns_record = lazy_import('msgraph.generated.models.domain_dns_record')

class DomainDnsSrvRecord(domain_dns_record.DomainDnsRecord):
    def __init__(self,) -> None:
        """
        Instantiates a new DomainDnsSrvRecord and sets the default values.
        """
        super().__init__()
        # Value to use when configuring the Target property of the SRV record at the DNS host.
        self._name_target: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Value to use when configuring the port property of the SRV record at the DNS host.
        self._port: Optional[int] = None
        # Value to use when configuring the priority property of the SRV record at the DNS host.
        self._priority: Optional[int] = None
        # Value to use when configuring the protocol property of the SRV record at the DNS host.
        self._protocol: Optional[str] = None
        # Value to use when configuring the service property of the SRV record at the DNS host.
        self._service: Optional[str] = None
        # Value to use when configuring the weight property of the SRV record at the DNS host.
        self._weight: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DomainDnsSrvRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DomainDnsSrvRecord
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DomainDnsSrvRecord()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "name_target": lambda n : setattr(self, 'name_target', n.get_str_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "priority": lambda n : setattr(self, 'priority', n.get_int_value()),
            "protocol": lambda n : setattr(self, 'protocol', n.get_str_value()),
            "service": lambda n : setattr(self, 'service', n.get_str_value()),
            "weight": lambda n : setattr(self, 'weight', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def name_target(self,) -> Optional[str]:
        """
        Gets the nameTarget property value. Value to use when configuring the Target property of the SRV record at the DNS host.
        Returns: Optional[str]
        """
        return self._name_target
    
    @name_target.setter
    def name_target(self,value: Optional[str] = None) -> None:
        """
        Sets the nameTarget property value. Value to use when configuring the Target property of the SRV record at the DNS host.
        Args:
            value: Value to set for the nameTarget property.
        """
        self._name_target = value
    
    @property
    def port(self,) -> Optional[int]:
        """
        Gets the port property value. Value to use when configuring the port property of the SRV record at the DNS host.
        Returns: Optional[int]
        """
        return self._port
    
    @port.setter
    def port(self,value: Optional[int] = None) -> None:
        """
        Sets the port property value. Value to use when configuring the port property of the SRV record at the DNS host.
        Args:
            value: Value to set for the port property.
        """
        self._port = value
    
    @property
    def priority(self,) -> Optional[int]:
        """
        Gets the priority property value. Value to use when configuring the priority property of the SRV record at the DNS host.
        Returns: Optional[int]
        """
        return self._priority
    
    @priority.setter
    def priority(self,value: Optional[int] = None) -> None:
        """
        Sets the priority property value. Value to use when configuring the priority property of the SRV record at the DNS host.
        Args:
            value: Value to set for the priority property.
        """
        self._priority = value
    
    @property
    def protocol(self,) -> Optional[str]:
        """
        Gets the protocol property value. Value to use when configuring the protocol property of the SRV record at the DNS host.
        Returns: Optional[str]
        """
        return self._protocol
    
    @protocol.setter
    def protocol(self,value: Optional[str] = None) -> None:
        """
        Sets the protocol property value. Value to use when configuring the protocol property of the SRV record at the DNS host.
        Args:
            value: Value to set for the protocol property.
        """
        self._protocol = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("nameTarget", self.name_target)
        writer.write_int_value("port", self.port)
        writer.write_int_value("priority", self.priority)
        writer.write_str_value("protocol", self.protocol)
        writer.write_str_value("service", self.service)
        writer.write_int_value("weight", self.weight)
    
    @property
    def service(self,) -> Optional[str]:
        """
        Gets the service property value. Value to use when configuring the service property of the SRV record at the DNS host.
        Returns: Optional[str]
        """
        return self._service
    
    @service.setter
    def service(self,value: Optional[str] = None) -> None:
        """
        Sets the service property value. Value to use when configuring the service property of the SRV record at the DNS host.
        Args:
            value: Value to set for the service property.
        """
        self._service = value
    
    @property
    def weight(self,) -> Optional[int]:
        """
        Gets the weight property value. Value to use when configuring the weight property of the SRV record at the DNS host.
        Returns: Optional[int]
        """
        return self._weight
    
    @weight.setter
    def weight(self,value: Optional[int] = None) -> None:
        """
        Sets the weight property value. Value to use when configuring the weight property of the SRV record at the DNS host.
        Args:
            value: Value to set for the weight property.
        """
        self._weight = value
    

