from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .azure_communication_services_user_identity import AzureCommunicationServicesUserIdentity
    from .call_records.user_identity import UserIdentity
    from .communications_application_identity import CommunicationsApplicationIdentity
    from .communications_application_instance_identity import CommunicationsApplicationInstanceIdentity
    from .communications_encrypted_identity import CommunicationsEncryptedIdentity
    from .communications_guest_identity import CommunicationsGuestIdentity
    from .communications_phone_identity import CommunicationsPhoneIdentity
    from .communications_user_identity import CommunicationsUserIdentity
    from .email_identity import EmailIdentity
    from .initiator import Initiator
    from .provisioned_identity import ProvisionedIdentity
    from .provisioning_service_principal import ProvisioningServicePrincipal
    from .provisioning_system import ProvisioningSystem
    from .service_principal_identity import ServicePrincipalIdentity
    from .share_point_identity import SharePointIdentity
    from .teamwork_application_identity import TeamworkApplicationIdentity
    from .teamwork_conversation_identity import TeamworkConversationIdentity
    from .teamwork_tag_identity import TeamworkTagIdentity
    from .teamwork_user_identity import TeamworkUserIdentity
    from .user_identity import UserIdentity

@dataclass
class Identity(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The display name of the identity.For drive items, the display name might not always be available or up to date. For example, if a user changes their display name the API might show the new value in a future response, but the items associated with the user don't show up as changed when using delta.
    display_name: Optional[str] = None
    # Unique identifier for the identity or actor. For example, in the access reviews decisions API, this property might record the id of the principal, that is, the group, user, or application that's subject to review.
    id: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Identity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Identity
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.azureCommunicationServicesUserIdentity".casefold():
            from .azure_communication_services_user_identity import AzureCommunicationServicesUserIdentity

            return AzureCommunicationServicesUserIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.callRecords.userIdentity".casefold():
            from .call_records.user_identity import UserIdentity
            from .user_identity import UserIdentity

            return UserIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.communicationsApplicationIdentity".casefold():
            from .communications_application_identity import CommunicationsApplicationIdentity

            return CommunicationsApplicationIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.communicationsApplicationInstanceIdentity".casefold():
            from .communications_application_instance_identity import CommunicationsApplicationInstanceIdentity

            return CommunicationsApplicationInstanceIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.communicationsEncryptedIdentity".casefold():
            from .communications_encrypted_identity import CommunicationsEncryptedIdentity

            return CommunicationsEncryptedIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.communicationsGuestIdentity".casefold():
            from .communications_guest_identity import CommunicationsGuestIdentity

            return CommunicationsGuestIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.communicationsPhoneIdentity".casefold():
            from .communications_phone_identity import CommunicationsPhoneIdentity

            return CommunicationsPhoneIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.communicationsUserIdentity".casefold():
            from .communications_user_identity import CommunicationsUserIdentity

            return CommunicationsUserIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.emailIdentity".casefold():
            from .email_identity import EmailIdentity

            return EmailIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.initiator".casefold():
            from .initiator import Initiator

            return Initiator()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.provisionedIdentity".casefold():
            from .provisioned_identity import ProvisionedIdentity

            return ProvisionedIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.provisioningServicePrincipal".casefold():
            from .provisioning_service_principal import ProvisioningServicePrincipal

            return ProvisioningServicePrincipal()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.provisioningSystem".casefold():
            from .provisioning_system import ProvisioningSystem

            return ProvisioningSystem()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.servicePrincipalIdentity".casefold():
            from .service_principal_identity import ServicePrincipalIdentity

            return ServicePrincipalIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.sharePointIdentity".casefold():
            from .share_point_identity import SharePointIdentity

            return SharePointIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkApplicationIdentity".casefold():
            from .teamwork_application_identity import TeamworkApplicationIdentity

            return TeamworkApplicationIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkConversationIdentity".casefold():
            from .teamwork_conversation_identity import TeamworkConversationIdentity

            return TeamworkConversationIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkTagIdentity".casefold():
            from .teamwork_tag_identity import TeamworkTagIdentity

            return TeamworkTagIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.teamworkUserIdentity".casefold():
            from .teamwork_user_identity import TeamworkUserIdentity

            return TeamworkUserIdentity()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.userIdentity".casefold():
            from .call_records.user_identity import UserIdentity
            from .user_identity import UserIdentity

            return UserIdentity()
        return Identity()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .azure_communication_services_user_identity import AzureCommunicationServicesUserIdentity
        from .call_records.user_identity import UserIdentity
        from .communications_application_identity import CommunicationsApplicationIdentity
        from .communications_application_instance_identity import CommunicationsApplicationInstanceIdentity
        from .communications_encrypted_identity import CommunicationsEncryptedIdentity
        from .communications_guest_identity import CommunicationsGuestIdentity
        from .communications_phone_identity import CommunicationsPhoneIdentity
        from .communications_user_identity import CommunicationsUserIdentity
        from .email_identity import EmailIdentity
        from .initiator import Initiator
        from .provisioned_identity import ProvisionedIdentity
        from .provisioning_service_principal import ProvisioningServicePrincipal
        from .provisioning_system import ProvisioningSystem
        from .service_principal_identity import ServicePrincipalIdentity
        from .share_point_identity import SharePointIdentity
        from .teamwork_application_identity import TeamworkApplicationIdentity
        from .teamwork_conversation_identity import TeamworkConversationIdentity
        from .teamwork_tag_identity import TeamworkTagIdentity
        from .teamwork_user_identity import TeamworkUserIdentity
        from .user_identity import UserIdentity

        from .azure_communication_services_user_identity import AzureCommunicationServicesUserIdentity
        from .call_records.user_identity import UserIdentity
        from .communications_application_identity import CommunicationsApplicationIdentity
        from .communications_application_instance_identity import CommunicationsApplicationInstanceIdentity
        from .communications_encrypted_identity import CommunicationsEncryptedIdentity
        from .communications_guest_identity import CommunicationsGuestIdentity
        from .communications_phone_identity import CommunicationsPhoneIdentity
        from .communications_user_identity import CommunicationsUserIdentity
        from .email_identity import EmailIdentity
        from .initiator import Initiator
        from .provisioned_identity import ProvisionedIdentity
        from .provisioning_service_principal import ProvisioningServicePrincipal
        from .provisioning_system import ProvisioningSystem
        from .service_principal_identity import ServicePrincipalIdentity
        from .share_point_identity import SharePointIdentity
        from .teamwork_application_identity import TeamworkApplicationIdentity
        from .teamwork_conversation_identity import TeamworkConversationIdentity
        from .teamwork_tag_identity import TeamworkTagIdentity
        from .teamwork_user_identity import TeamworkUserIdentity
        from .user_identity import UserIdentity

        fields: dict[str, Callable[[Any], None]] = {
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

