from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert_evidence = lazy_import('msgraph.generated.models.security.alert_evidence')

class IpEvidence(alert_evidence.AlertEvidence):
    def __init__(self,) -> None:
        """
        Instantiates a new IpEvidence and sets the default values.
        """
        super().__init__()
        # The two-letter country code according to ISO 3166 format, for example: US, UK, CA, etc..).
        self._country_letter_code: Optional[str] = None
        # The value of the IP Address, can be either in V4 address or V6 address format.
        self._ip_address: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @property
    def country_letter_code(self,) -> Optional[str]:
        """
        Gets the countryLetterCode property value. The two-letter country code according to ISO 3166 format, for example: US, UK, CA, etc..).
        Returns: Optional[str]
        """
        return self._country_letter_code
    
    @country_letter_code.setter
    def country_letter_code(self,value: Optional[str] = None) -> None:
        """
        Sets the countryLetterCode property value. The two-letter country code according to ISO 3166 format, for example: US, UK, CA, etc..).
        Args:
            value: Value to set for the countryLetterCode property.
        """
        self._country_letter_code = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IpEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IpEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IpEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "country_letter_code": lambda n : setattr(self, 'country_letter_code', n.get_str_value()),
            "ip_address": lambda n : setattr(self, 'ip_address', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def ip_address(self,) -> Optional[str]:
        """
        Gets the ipAddress property value. The value of the IP Address, can be either in V4 address or V6 address format.
        Returns: Optional[str]
        """
        return self._ip_address
    
    @ip_address.setter
    def ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ipAddress property value. The value of the IP Address, can be either in V4 address or V6 address format.
        Args:
            value: Value to set for the ipAddress property.
        """
        self._ip_address = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("countryLetterCode", self.country_letter_code)
        writer.write_str_value("ipAddress", self.ip_address)
    

