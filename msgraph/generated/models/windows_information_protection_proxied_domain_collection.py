from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

proxied_domain = lazy_import('msgraph.generated.models.proxied_domain')

class WindowsInformationProtectionProxiedDomainCollection(AdditionalDataHolder, Parsable):
    """
    Windows Information Protection Proxied Domain Collection
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
        Instantiates a new windowsInformationProtectionProxiedDomainCollection and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Display name
        self._display_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Collection of proxied domains
        self._proxied_domains: Optional[List[proxied_domain.ProxiedDomain]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> WindowsInformationProtectionProxiedDomainCollection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: WindowsInformationProtectionProxiedDomainCollection
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return WindowsInformationProtectionProxiedDomainCollection()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "proxied_domains": lambda n : setattr(self, 'proxied_domains', n.get_collection_of_object_values(proxied_domain.ProxiedDomain)),
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
    def proxied_domains(self,) -> Optional[List[proxied_domain.ProxiedDomain]]:
        """
        Gets the proxiedDomains property value. Collection of proxied domains
        Returns: Optional[List[proxied_domain.ProxiedDomain]]
        """
        return self._proxied_domains
    
    @proxied_domains.setter
    def proxied_domains(self,value: Optional[List[proxied_domain.ProxiedDomain]] = None) -> None:
        """
        Sets the proxiedDomains property value. Collection of proxied domains
        Args:
            value: Value to set for the proxiedDomains property.
        """
        self._proxied_domains = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("proxiedDomains", self.proxied_domains)
        writer.write_additional_data_value(self.additional_data)
    

