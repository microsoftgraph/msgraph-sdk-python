from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import email_identity, initiator, provisioned_identity, provisioning_service_principal, provisioning_system, service_principal_identity, share_point_identity, teamwork_application_identity, teamwork_conversation_identity, teamwork_tag_identity, teamwork_user_identity, user_identity

@dataclass
class Identity(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The display name of the identity. Note that this might not always be available or up to date. For example, if a user changes their display name, the API might show the new value in a future response, but the items associated with the user won't show up as having changed when using delta.
    display_name: Optional[str] = None
    # Unique identifier for the identity.
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Identity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Identity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.emailIdentity":
                from . import email_identity

                return email_identity.EmailIdentity()
            if mapping_value == "#microsoft.graph.initiator":
                from . import initiator

                return initiator.Initiator()
            if mapping_value == "#microsoft.graph.provisionedIdentity":
                from . import provisioned_identity

                return provisioned_identity.ProvisionedIdentity()
            if mapping_value == "#microsoft.graph.provisioningServicePrincipal":
                from . import provisioning_service_principal

                return provisioning_service_principal.ProvisioningServicePrincipal()
            if mapping_value == "#microsoft.graph.provisioningSystem":
                from . import provisioning_system

                return provisioning_system.ProvisioningSystem()
            if mapping_value == "#microsoft.graph.servicePrincipalIdentity":
                from . import service_principal_identity

                return service_principal_identity.ServicePrincipalIdentity()
            if mapping_value == "#microsoft.graph.sharePointIdentity":
                from . import share_point_identity

                return share_point_identity.SharePointIdentity()
            if mapping_value == "#microsoft.graph.teamworkApplicationIdentity":
                from . import teamwork_application_identity

                return teamwork_application_identity.TeamworkApplicationIdentity()
            if mapping_value == "#microsoft.graph.teamworkConversationIdentity":
                from . import teamwork_conversation_identity

                return teamwork_conversation_identity.TeamworkConversationIdentity()
            if mapping_value == "#microsoft.graph.teamworkTagIdentity":
                from . import teamwork_tag_identity

                return teamwork_tag_identity.TeamworkTagIdentity()
            if mapping_value == "#microsoft.graph.teamworkUserIdentity":
                from . import teamwork_user_identity

                return teamwork_user_identity.TeamworkUserIdentity()
            if mapping_value == "#microsoft.graph.userIdentity":
                from . import user_identity

                return user_identity.UserIdentity()
        return Identity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import email_identity, initiator, provisioned_identity, provisioning_service_principal, provisioning_system, service_principal_identity, share_point_identity, teamwork_application_identity, teamwork_conversation_identity, teamwork_tag_identity, teamwork_user_identity, user_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
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
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

