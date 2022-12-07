from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ProxiedDomain(AdditionalDataHolder, Parsable):
    """
    Proxied Domain
    """
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
        Instantiates a new proxiedDomain and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The IP address or FQDN
        self._ip_address_or_f_q_d_n: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Proxy IP or FQDN
        self._proxy: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ProxiedDomain:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ProxiedDomain
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ProxiedDomain()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "ip_address_or_f_q_d_n": lambda n : setattr(self, 'ip_address_or_f_q_d_n', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "proxy": lambda n : setattr(self, 'proxy', n.get_str_value()),
        }
        return fields
    
    @property
    def ip_address_or_f_q_d_n(self,) -> Optional[str]:
        """
        Gets the ipAddressOrFQDN property value. The IP address or FQDN
        Returns: Optional[str]
        """
        return self._ip_address_or_f_q_d_n
    
    @ip_address_or_f_q_d_n.setter
    def ip_address_or_f_q_d_n(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddressOrFQDN property value. The IP address or FQDN
        Args:
            value: Value to set for the ipAddressOrFQDN property.
        """
        self._ip_address_or_f_q_d_n = value
    
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
    def proxy(self,) -> Optional[str]:
        """
        Gets the proxy property value. Proxy IP or FQDN
        Returns: Optional[str]
        """
        return self._proxy
    
    @proxy.setter
    def proxy(self,value: Optional[str] = None) -> None:
        """
        Sets the proxy property value. Proxy IP or FQDN
        Args:
            value: Value to set for the proxy property.
        """
        self._proxy = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("ipAddressOrFQDN", self.ip_address_or_f_q_d_n)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("proxy", self.proxy)
        writer.write_additional_data_value(self.additional_data)
    

