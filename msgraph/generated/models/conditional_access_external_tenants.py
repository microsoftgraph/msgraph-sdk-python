from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import conditional_access_all_external_tenants, conditional_access_enumerated_external_tenants, conditional_access_external_tenants_membership_kind

@dataclass
class ConditionalAccessExternalTenants(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The membership kind. Possible values are: all, enumerated, unknownFutureValue. The enumerated member references an conditionalAccessEnumeratedExternalTenants object.
    membership_kind: Optional[conditional_access_external_tenants_membership_kind.ConditionalAccessExternalTenantsMembershipKind] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ConditionalAccessExternalTenants:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ConditionalAccessExternalTenants
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.conditionalAccessAllExternalTenants":
                from . import conditional_access_all_external_tenants

                return conditional_access_all_external_tenants.ConditionalAccessAllExternalTenants()
            if mapping_value == "#microsoft.graph.conditionalAccessEnumeratedExternalTenants":
                from . import conditional_access_enumerated_external_tenants

                return conditional_access_enumerated_external_tenants.ConditionalAccessEnumeratedExternalTenants()
        return ConditionalAccessExternalTenants()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import conditional_access_all_external_tenants, conditional_access_enumerated_external_tenants, conditional_access_external_tenants_membership_kind

        fields: Dict[str, Callable[[Any], None]] = {
            "membershipKind": lambda n : setattr(self, 'membership_kind', n.get_enum_value(conditional_access_external_tenants_membership_kind.ConditionalAccessExternalTenantsMembershipKind)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("membershipKind", self.membership_kind)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

