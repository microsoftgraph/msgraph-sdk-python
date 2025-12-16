from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .endpoint_type import EndpointType
    from .identity import Identity
    from .identity_set import IdentitySet

from .identity_set import IdentitySet

@dataclass
class CommunicationsIdentitySet(IdentitySet, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.communicationsIdentitySet"
    # The application instance associated with this action.
    application_instance: Optional[Identity] = None
    # An identity the participant would like to present itself as to the other participants in the call.
    asserted_identity: Optional[Identity] = None
    # The Azure Communication Services user associated with this action.
    azure_communication_services_user: Optional[Identity] = None
    # The encrypted user associated with this action.
    encrypted: Optional[Identity] = None
    # Type of endpoint that the participant uses. The possible values are: default, voicemail, skypeForBusiness, skypeForBusinessVoipPhone, unknownFutureValue.
    endpoint_type: Optional[EndpointType] = None
    # The guest user associated with this action.
    guest: Optional[Identity] = None
    # The Skype for Business on-premises user associated with this action.
    on_premises: Optional[Identity] = None
    # The phone user associated with this action.
    phone: Optional[Identity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CommunicationsIdentitySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CommunicationsIdentitySet
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CommunicationsIdentitySet()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .endpoint_type import EndpointType
        from .identity import Identity
        from .identity_set import IdentitySet

        from .endpoint_type import EndpointType
        from .identity import Identity
        from .identity_set import IdentitySet

        fields: dict[str, Callable[[Any], None]] = {
            "applicationInstance": lambda n : setattr(self, 'application_instance', n.get_object_value(Identity)),
            "assertedIdentity": lambda n : setattr(self, 'asserted_identity', n.get_object_value(Identity)),
            "azureCommunicationServicesUser": lambda n : setattr(self, 'azure_communication_services_user', n.get_object_value(Identity)),
            "encrypted": lambda n : setattr(self, 'encrypted', n.get_object_value(Identity)),
            "endpointType": lambda n : setattr(self, 'endpoint_type', n.get_enum_value(EndpointType)),
            "guest": lambda n : setattr(self, 'guest', n.get_object_value(Identity)),
            "onPremises": lambda n : setattr(self, 'on_premises', n.get_object_value(Identity)),
            "phone": lambda n : setattr(self, 'phone', n.get_object_value(Identity)),
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
        writer.write_object_value("applicationInstance", self.application_instance)
        writer.write_object_value("assertedIdentity", self.asserted_identity)
        writer.write_object_value("azureCommunicationServicesUser", self.azure_communication_services_user)
        writer.write_object_value("encrypted", self.encrypted)
        writer.write_enum_value("endpointType", self.endpoint_type)
        writer.write_object_value("guest", self.guest)
        writer.write_object_value("onPremises", self.on_premises)
        writer.write_object_value("phone", self.phone)
    

