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
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.attributeRuleMembers".casefold():
            from . import attribute_rule_members

            return attribute_rule_members.AttributeRuleMembers()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.connectedOrganizationMembers".casefold():
            from . import connected_organization_members

            return connected_organization_members.ConnectedOrganizationMembers()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.externalSponsors".casefold():
            from . import external_sponsors

            return external_sponsors.ExternalSponsors()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.groupMembers".casefold():
            from . import group_members

            return group_members.GroupMembers()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.internalSponsors".casefold():
            from . import internal_sponsors

            return internal_sponsors.InternalSponsors()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.requestorManager".casefold():
            from . import requestor_manager

            return requestor_manager.RequestorManager()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.singleServicePrincipal".casefold():
            from . import single_service_principal

            return single_service_principal.SingleServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.singleUser".casefold():
            from . import single_user

            return single_user.SingleUser()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetApplicationOwners".casefold():
            from . import target_application_owners

            return target_application_owners.TargetApplicationOwners()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.targetManager".casefold():
            from . import target_manager

            return target_manager.TargetManager()
        return SubjectSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import attribute_rule_members, connected_organization_members, external_sponsors, group_members, internal_sponsors, requestor_manager, single_service_principal, single_user, target_application_owners, target_manager

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
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

