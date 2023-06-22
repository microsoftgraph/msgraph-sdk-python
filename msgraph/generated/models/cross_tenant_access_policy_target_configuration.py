from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import cross_tenant_access_policy_target, cross_tenant_access_policy_target_configuration_access_type

@dataclass
class CrossTenantAccessPolicyTargetConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # Defines whether access is allowed or blocked. The possible values are: allowed, blocked, unknownFutureValue.
    access_type: Optional[cross_tenant_access_policy_target_configuration_access_type.CrossTenantAccessPolicyTargetConfigurationAccessType] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Specifies whether to target users, groups, or applications with this rule.
    targets: Optional[List[cross_tenant_access_policy_target.CrossTenantAccessPolicyTarget]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CrossTenantAccessPolicyTargetConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CrossTenantAccessPolicyTargetConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CrossTenantAccessPolicyTargetConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import cross_tenant_access_policy_target, cross_tenant_access_policy_target_configuration_access_type

        from . import cross_tenant_access_policy_target, cross_tenant_access_policy_target_configuration_access_type

        fields: Dict[str, Callable[[Any], None]] = {
            "accessType": lambda n : setattr(self, 'access_type', n.get_enum_value(cross_tenant_access_policy_target_configuration_access_type.CrossTenantAccessPolicyTargetConfigurationAccessType)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_object_values(cross_tenant_access_policy_target.CrossTenantAccessPolicyTarget)),
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
        writer.write_enum_value("accessType", self.access_type)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("targets", self.targets)
        writer.write_additional_data_value(self.additional_data)
    

