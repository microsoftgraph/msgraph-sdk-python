from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus
    from .cloud_pc_on_premises_connection_status_detail import CloudPcOnPremisesConnectionStatusDetail
    from .cloud_pc_on_premises_connection_type import CloudPcOnPremisesConnectionType
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcOnPremisesConnection(Entity):
    # The adDomainName property
    ad_domain_name: Optional[str] = None
    # The adDomainPassword property
    ad_domain_password: Optional[str] = None
    # The adDomainUsername property
    ad_domain_username: Optional[str] = None
    # The alternateResourceUrl property
    alternate_resource_url: Optional[str] = None
    # The connectionType property
    connection_type: Optional[CloudPcOnPremisesConnectionType] = None
    # The displayName property
    display_name: Optional[str] = None
    # The healthCheckStatus property
    health_check_status: Optional[CloudPcOnPremisesConnectionStatus] = None
    # The healthCheckStatusDetail property
    health_check_status_detail: Optional[CloudPcOnPremisesConnectionStatusDetail] = None
    # The inUse property
    in_use: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The organizationalUnit property
    organizational_unit: Optional[str] = None
    # The resourceGroupId property
    resource_group_id: Optional[str] = None
    # The subnetId property
    subnet_id: Optional[str] = None
    # The subscriptionId property
    subscription_id: Optional[str] = None
    # The subscriptionName property
    subscription_name: Optional[str] = None
    # The virtualNetworkId property
    virtual_network_id: Optional[str] = None
    # The virtualNetworkLocation property
    virtual_network_location: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CloudPcOnPremisesConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcOnPremisesConnection
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CloudPcOnPremisesConnection()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus
        from .cloud_pc_on_premises_connection_status_detail import CloudPcOnPremisesConnectionStatusDetail
        from .cloud_pc_on_premises_connection_type import CloudPcOnPremisesConnectionType
        from .entity import Entity

        from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus
        from .cloud_pc_on_premises_connection_status_detail import CloudPcOnPremisesConnectionStatusDetail
        from .cloud_pc_on_premises_connection_type import CloudPcOnPremisesConnectionType
        from .entity import Entity

        fields: Dict[str, Callable[[Any], None]] = {
            "adDomainName": lambda n : setattr(self, 'ad_domain_name', n.get_str_value()),
            "adDomainPassword": lambda n : setattr(self, 'ad_domain_password', n.get_str_value()),
            "adDomainUsername": lambda n : setattr(self, 'ad_domain_username', n.get_str_value()),
            "alternateResourceUrl": lambda n : setattr(self, 'alternate_resource_url', n.get_str_value()),
            "connectionType": lambda n : setattr(self, 'connection_type', n.get_enum_value(CloudPcOnPremisesConnectionType)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "healthCheckStatus": lambda n : setattr(self, 'health_check_status', n.get_enum_value(CloudPcOnPremisesConnectionStatus)),
            "healthCheckStatusDetail": lambda n : setattr(self, 'health_check_status_detail', n.get_object_value(CloudPcOnPremisesConnectionStatusDetail)),
            "inUse": lambda n : setattr(self, 'in_use', n.get_bool_value()),
            "organizationalUnit": lambda n : setattr(self, 'organizational_unit', n.get_str_value()),
            "resourceGroupId": lambda n : setattr(self, 'resource_group_id', n.get_str_value()),
            "subnetId": lambda n : setattr(self, 'subnet_id', n.get_str_value()),
            "subscriptionId": lambda n : setattr(self, 'subscription_id', n.get_str_value()),
            "subscriptionName": lambda n : setattr(self, 'subscription_name', n.get_str_value()),
            "virtualNetworkId": lambda n : setattr(self, 'virtual_network_id', n.get_str_value()),
            "virtualNetworkLocation": lambda n : setattr(self, 'virtual_network_location', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_str_value("adDomainName", self.ad_domain_name)
        writer.write_str_value("adDomainPassword", self.ad_domain_password)
        writer.write_str_value("adDomainUsername", self.ad_domain_username)
        writer.write_str_value("alternateResourceUrl", self.alternate_resource_url)
        writer.write_enum_value("connectionType", self.connection_type)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("healthCheckStatus", self.health_check_status)
        writer.write_object_value("healthCheckStatusDetail", self.health_check_status_detail)
        writer.write_bool_value("inUse", self.in_use)
        writer.write_str_value("organizationalUnit", self.organizational_unit)
        writer.write_str_value("resourceGroupId", self.resource_group_id)
        writer.write_str_value("subnetId", self.subnet_id)
        writer.write_str_value("subscriptionId", self.subscription_id)
        writer.write_str_value("subscriptionName", self.subscription_name)
        writer.write_str_value("virtualNetworkId", self.virtual_network_id)
        writer.write_str_value("virtualNetworkLocation", self.virtual_network_location)
    

