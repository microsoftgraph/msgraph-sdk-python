from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import attribute_rule_members, connected_organization_members, external_sponsors, group_members, internal_sponsors, requestor_manager, single_service_principal, single_user, target_application_owners, target_manager

@dataclass
class SubjectSet(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SubjectSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SubjectSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.attributeRuleMembers":
                from . import attribute_rule_members

                return attribute_rule_members.AttributeRuleMembers()
            if mapping_value == "#microsoft.graph.connectedOrganizationMembers":
                from . import connected_organization_members

                return connected_organization_members.ConnectedOrganizationMembers()
            if mapping_value == "#microsoft.graph.externalSponsors":
                from . import external_sponsors

                return external_sponsors.ExternalSponsors()
            if mapping_value == "#microsoft.graph.groupMembers":
                from . import group_members

                return group_members.GroupMembers()
            if mapping_value == "#microsoft.graph.internalSponsors":
                from . import internal_sponsors

                return internal_sponsors.InternalSponsors()
            if mapping_value == "#microsoft.graph.requestorManager":
                from . import requestor_manager

                return requestor_manager.RequestorManager()
            if mapping_value == "#microsoft.graph.singleServicePrincipal":
                from . import single_service_principal

                return single_service_principal.SingleServicePrincipal()
            if mapping_value == "#microsoft.graph.singleUser":
                from . import single_user

                return single_user.SingleUser()
            if mapping_value == "#microsoft.graph.targetApplicationOwners":
                from . import target_application_owners

                return target_application_owners.TargetApplicationOwners()
            if mapping_value == "#microsoft.graph.targetManager":
                from . import target_manager

                return target_manager.TargetManager()
        return SubjectSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attribute_rule_members, connected_organization_members, external_sponsors, group_members, internal_sponsors, requestor_manager, single_service_principal, single_user, target_application_owners, target_manager

        fields: Dict[str, Callable[[Any], None]] = {
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

