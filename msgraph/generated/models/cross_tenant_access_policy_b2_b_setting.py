from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cross_tenant_access_policy_target_configuration

@dataclass
class CrossTenantAccessPolicyB2BSetting(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The list of applications targeted with your cross-tenant access policy.
    applications: Optional[cross_tenant_access_policy_target_configuration.CrossTenantAccessPolicyTargetConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of users and groups targeted with your cross-tenant access policy.
    users_and_groups: Optional[cross_tenant_access_policy_target_configuration.CrossTenantAccessPolicyTargetConfiguration] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantAccessPolicyB2BSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyB2BSetting
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantAccessPolicyB2BSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cross_tenant_access_policy_target_configuration

        from . import cross_tenant_access_policy_target_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "applications": lambda n : setattr(self, 'applications', n.get_object_value(cross_tenant_access_policy_target_configuration.CrossTenantAccessPolicyTargetConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "usersAndGroups": lambda n : setattr(self, 'users_and_groups', n.get_object_value(cross_tenant_access_policy_target_configuration.CrossTenantAccessPolicyTargetConfiguration)),
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
        writer.write_object_value("applications", self.applications)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("usersAndGroups", self.users_and_groups)
        writer.write_additional_data_value(self.additional_data)
    

