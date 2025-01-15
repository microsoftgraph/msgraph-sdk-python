from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus
    from .cloud_pc_on_premises_connection_status_detail import CloudPcOnPremisesConnectionStatusDetail
    from .cloud_pc_on_premises_connection_type import CloudPcOnPremisesConnectionType
    from .entity import Entity

from .entity import Entity

@dataclass
class CloudPcOnPremisesConnection(Entity, Parsable):
    # The fully qualified domain name (FQDN) of the Active Directory domain you want to join. Maximum length is 255. Optional.
    ad_domain_name: Optional[str] = None
    # The password associated with the username of an Active Directory account (adDomainUsername).
    ad_domain_password: Optional[str] = None
    # The username of an Active Directory account (user or service account) that has permission to create computer objects in Active Directory. Required format: admin@contoso.com. Optional.
    ad_domain_username: Optional[str] = None
    # The interface URL of the partner service's resource that links to this Azure network connection. Returned only on $select.
    alternate_resource_url: Optional[str] = None
    # Specifies how the provisioned Cloud PC joins to Microsoft Entra. It includes different types, one is Microsoft Entra ID join, which means there's no on-premises Active Directory (AD) in the current tenant, and the Cloud PC device is joined by Microsoft Entra. Another one is hybridAzureADJoin, which means there's also an on-premises Active Directory (AD) in the current tenant and the Cloud PC device joins to on-premises Active Directory (AD) and Microsoft Entra. The type also determines which types of users can be assigned and can sign into a Cloud PC. The azureADJoin type indicates that cloud-only and hybrid users can be assigned and signed into the Cloud PC. hybridAzureADJoin indicates only hybrid users can be assigned and signed into the Cloud PC. The default value is hybridAzureADJoin.
    connection_type: Optional[CloudPcOnPremisesConnectionType] = None
    # The display name for the Azure network connection.
    display_name: Optional[str] = None
    # The healthCheckStatus property
    health_check_status: Optional[CloudPcOnPremisesConnectionStatus] = None
    # Indicates the results of health checks performed on the on-premises connection. Read-only. Returned only on $select. For an example that shows how to get the inUse property, see Example 2: Get the selected properties of an Azure network connection, including healthCheckStatusDetail. Read-only.
    health_check_status_detail: Optional[CloudPcOnPremisesConnectionStatusDetail] = None
    # When true, the Azure network connection is in use. When false, the connection isn't in use. You can't delete a connection that’s in use. Returned only on $select. For an example that shows how to get the inUse property, see Example 2: Get the selected properties of an Azure network connection, including healthCheckStatusDetail. Read-only.
    in_use: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The organizational unit (OU) in which the computer account is created. If left null, the OU configured as the default (a well-known computer object container) in the tenant's Active Directory domain (OU) is used. Optional.
    organizational_unit: Optional[str] = None
    # The unique identifier of the target resource group used associated with the on-premises network connectivity for Cloud PCs. Required format: '/subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}'
    resource_group_id: Optional[str] = None
    # The unique identifier of the target subnet used associated with the on-premises network connectivity for Cloud PCs. Required format: '/subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkId}/subnets/{subnetName}'
    subnet_id: Optional[str] = None
    # The unique identifier of the Azure subscription associated with the tenant.
    subscription_id: Optional[str] = None
    # The name of the Azure subscription is used to create an Azure network connection. Read-only.
    subscription_name: Optional[str] = None
    # The unique identifier of the target virtual network used associated with the on-premises network connectivity for Cloud PCs. Required format: '/subscriptions/{subscription-id}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/virtualNetworks/{virtualNetworkName}'
    virtual_network_id: Optional[str] = None
    # Indicates the resource location of the target virtual network. For example, the location can be eastus2, westeurope, etc. Read-only (computed value).
    virtual_network_location: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CloudPcOnPremisesConnection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CloudPcOnPremisesConnection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CloudPcOnPremisesConnection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus
        from .cloud_pc_on_premises_connection_status_detail import CloudPcOnPremisesConnectionStatusDetail
        from .cloud_pc_on_premises_connection_type import CloudPcOnPremisesConnectionType
        from .entity import Entity

        from .cloud_pc_on_premises_connection_status import CloudPcOnPremisesConnectionStatus
        from .cloud_pc_on_premises_connection_status_detail import CloudPcOnPremisesConnectionStatusDetail
        from .cloud_pc_on_premises_connection_type import CloudPcOnPremisesConnectionType
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
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
        if writer is None:
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
    

