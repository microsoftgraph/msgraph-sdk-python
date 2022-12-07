from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class HostSecurityState(AdditionalDataHolder, Parsable):
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
        Instantiates a new hostSecurityState and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Host FQDN (Fully Qualified Domain Name) (for example, machine.company.com).
        self._fqdn: Optional[str] = None
        # The isAzureAdJoined property
        self._is_azure_ad_joined: Optional[bool] = None
        # The isAzureAdRegistered property
        self._is_azure_ad_registered: Optional[bool] = None
        # True if the host is domain joined to an on-premises Active Directory domain.
        self._is_hybrid_azure_domain_joined: Optional[bool] = None
        # The local host name, without the DNS domain name.
        self._net_bios_name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Host Operating System. (For example, Windows10, MacOS, RHEL, etc.).
        self._os: Optional[str] = None
        # Private (not routable) IPv4 or IPv6 address (see RFC 1918) at the time of the alert.
        self._private_ip_address: Optional[str] = None
        # Publicly routable IPv4 or IPv6 address (see RFC 1918) at time of the alert.
        self._public_ip_address: Optional[str] = None
        # Provider-generated/calculated risk score of the host.  Recommended value range of 0-1, which equates to a percentage.
        self._risk_score: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HostSecurityState:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HostSecurityState
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return HostSecurityState()
    
    @property
    def fqdn(self,) -> Optional[str]:
        """
        Gets the fqdn property value. Host FQDN (Fully Qualified Domain Name) (for example, machine.company.com).
        Returns: Optional[str]
        """
        return self._fqdn
    
    @fqdn.setter
    def fqdn(self,value: Optional[str] = None) -> None:
        """
        Sets the fqdn property value. Host FQDN (Fully Qualified Domain Name) (for example, machine.company.com).
        Args:
            value: Value to set for the fqdn property.
        """
        self._fqdn = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "fqdn": lambda n : setattr(self, 'fqdn', n.get_str_value()),
            "is_azure_ad_joined": lambda n : setattr(self, 'is_azure_ad_joined', n.get_bool_value()),
            "is_azure_ad_registered": lambda n : setattr(self, 'is_azure_ad_registered', n.get_bool_value()),
            "is_hybrid_azure_domain_joined": lambda n : setattr(self, 'is_hybrid_azure_domain_joined', n.get_bool_value()),
            "net_bios_name": lambda n : setattr(self, 'net_bios_name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "os": lambda n : setattr(self, 'os', n.get_str_value()),
            "private_ip_address": lambda n : setattr(self, 'private_ip_address', n.get_str_value()),
            "public_ip_address": lambda n : setattr(self, 'public_ip_address', n.get_str_value()),
            "risk_score": lambda n : setattr(self, 'risk_score', n.get_str_value()),
        }
        return fields
    
    @property
    def is_azure_ad_joined(self,) -> Optional[bool]:
        """
        Gets the isAzureAdJoined property value. The isAzureAdJoined property
        Returns: Optional[bool]
        """
        return self._is_azure_ad_joined
    
    @is_azure_ad_joined.setter
    def is_azure_ad_joined(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAzureAdJoined property value. The isAzureAdJoined property
        Args:
            value: Value to set for the isAzureAdJoined property.
        """
        self._is_azure_ad_joined = value
    
    @property
    def is_azure_ad_registered(self,) -> Optional[bool]:
        """
        Gets the isAzureAdRegistered property value. The isAzureAdRegistered property
        Returns: Optional[bool]
        """
        return self._is_azure_ad_registered
    
    @is_azure_ad_registered.setter
    def is_azure_ad_registered(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAzureAdRegistered property value. The isAzureAdRegistered property
        Args:
            value: Value to set for the isAzureAdRegistered property.
        """
        self._is_azure_ad_registered = value
    
    @property
    def is_hybrid_azure_domain_joined(self,) -> Optional[bool]:
        """
        Gets the isHybridAzureDomainJoined property value. True if the host is domain joined to an on-premises Active Directory domain.
        Returns: Optional[bool]
        """
        return self._is_hybrid_azure_domain_joined
    
    @is_hybrid_azure_domain_joined.setter
    def is_hybrid_azure_domain_joined(self,value: Optional[bool] = None) -> None:
        """
        Sets the isHybridAzureDomainJoined property value. True if the host is domain joined to an on-premises Active Directory domain.
        Args:
            value: Value to set for the isHybridAzureDomainJoined property.
        """
        self._is_hybrid_azure_domain_joined = value
    
    @property
    def net_bios_name(self,) -> Optional[str]:
        """
        Gets the netBiosName property value. The local host name, without the DNS domain name.
        Returns: Optional[str]
        """
        return self._net_bios_name
    
    @net_bios_name.setter
    def net_bios_name(self,value: Optional[str] = None) -> None:
        """
        Sets the netBiosName property value. The local host name, without the DNS domain name.
        Args:
            value: Value to set for the netBiosName property.
        """
        self._net_bios_name = value
    
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
    def os(self,) -> Optional[str]:
        """
        Gets the os property value. Host Operating System. (For example, Windows10, MacOS, RHEL, etc.).
        Returns: Optional[str]
        """
        return self._os
    
    @os.setter
    def os(self,value: Optional[str] = None) -> None:
        """
        Sets the os property value. Host Operating System. (For example, Windows10, MacOS, RHEL, etc.).
        Args:
            value: Value to set for the os property.
        """
        self._os = value
    
    @property
    def private_ip_address(self,) -> Optional[str]:
        """
        Gets the privateIpAddress property value. Private (not routable) IPv4 or IPv6 address (see RFC 1918) at the time of the alert.
        Returns: Optional[str]
        """
        return self._private_ip_address
    
    @private_ip_address.setter
    def private_ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the privateIpAddress property value. Private (not routable) IPv4 or IPv6 address (see RFC 1918) at the time of the alert.
        Args:
            value: Value to set for the privateIpAddress property.
        """
        self._private_ip_address = value
    
    @property
    def public_ip_address(self,) -> Optional[str]:
        """
        Gets the publicIpAddress property value. Publicly routable IPv4 or IPv6 address (see RFC 1918) at time of the alert.
        Returns: Optional[str]
        """
        return self._public_ip_address
    
    @public_ip_address.setter
    def public_ip_address(self,value: Optional[str] = None) -> None:
        """
        Sets the publicIpAddress property value. Publicly routable IPv4 or IPv6 address (see RFC 1918) at time of the alert.
        Args:
            value: Value to set for the publicIpAddress property.
        """
        self._public_ip_address = value
    
    @property
    def risk_score(self,) -> Optional[str]:
        """
        Gets the riskScore property value. Provider-generated/calculated risk score of the host.  Recommended value range of 0-1, which equates to a percentage.
        Returns: Optional[str]
        """
        return self._risk_score
    
    @risk_score.setter
    def risk_score(self,value: Optional[str] = None) -> None:
        """
        Sets the riskScore property value. Provider-generated/calculated risk score of the host.  Recommended value range of 0-1, which equates to a percentage.
        Args:
            value: Value to set for the riskScore property.
        """
        self._risk_score = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("fqdn", self.fqdn)
        writer.write_bool_value("isAzureAdJoined", self.is_azure_ad_joined)
        writer.write_bool_value("isAzureAdRegistered", self.is_azure_ad_registered)
        writer.write_bool_value("isHybridAzureDomainJoined", self.is_hybrid_azure_domain_joined)
        writer.write_str_value("netBiosName", self.net_bios_name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("os", self.os)
        writer.write_str_value("privateIpAddress", self.private_ip_address)
        writer.write_str_value("publicIpAddress", self.public_ip_address)
        writer.write_str_value("riskScore", self.risk_score)
        writer.write_additional_data_value(self.additional_data)
    

