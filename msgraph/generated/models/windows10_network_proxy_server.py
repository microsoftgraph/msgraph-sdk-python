from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class Windows10NetworkProxyServer(AdditionalDataHolder, Parsable):
    """
    Network Proxy Server Policy.
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
    
    @property
    def address(self,) -> Optional[str]:
        """
        Gets the address property value. Address to the proxy server. Specify an address in the format [':']
        Returns: Optional[str]
        """
        return self._address
    
    @address.setter
    def address(self,value: Optional[str] = None) -> None:
        """
        Sets the address property value. Address to the proxy server. Specify an address in the format [':']
        Args:
            value: Value to set for the address property.
        """
        self._address = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new windows10NetworkProxyServer and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Address to the proxy server. Specify an address in the format [':']
        self._address: Optional[str] = None
        # Addresses that should not use the proxy server. The system will not use the proxy server for addresses beginning with what is specified in this node.
        self._exceptions: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Specifies whether the proxy server should be used for local (intranet) addresses.
        self._use_for_local_addresses: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10NetworkProxyServer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10NetworkProxyServer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10NetworkProxyServer()
    
    @property
    def exceptions(self,) -> Optional[List[str]]:
        """
        Gets the exceptions property value. Addresses that should not use the proxy server. The system will not use the proxy server for addresses beginning with what is specified in this node.
        Returns: Optional[List[str]]
        """
        return self._exceptions
    
    @exceptions.setter
    def exceptions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the exceptions property value. Addresses that should not use the proxy server. The system will not use the proxy server for addresses beginning with what is specified in this node.
        Args:
            value: Value to set for the exceptions property.
        """
        self._exceptions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "exceptions": lambda n : setattr(self, 'exceptions', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "use_for_local_addresses": lambda n : setattr(self, 'use_for_local_addresses', n.get_bool_value()),
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
        writer.write_str_value("address", self.address)
        writer.write_collection_of_primitive_values("exceptions", self.exceptions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("useForLocalAddresses", self.use_for_local_addresses)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def use_for_local_addresses(self,) -> Optional[bool]:
        """
        Gets the useForLocalAddresses property value. Specifies whether the proxy server should be used for local (intranet) addresses.
        Returns: Optional[bool]
        """
        return self._use_for_local_addresses
    
    @use_for_local_addresses.setter
    def use_for_local_addresses(self,value: Optional[bool] = None) -> None:
        """
        Sets the useForLocalAddresses property value. Specifies whether the proxy server should be used for local (intranet) addresses.
        Args:
            value: Value to set for the useForLocalAddresses property.
        """
        self._use_for_local_addresses = value
    

