from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .endpoint_type import EndpointType
    from .identity import Identity
    from .identity_set import IdentitySet

from .identity_set import IdentitySet

@dataclass
class CommunicationsIdentitySet(IdentitySet):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.communicationsIdentitySet"
    # The applicationInstance property
    application_instance: Optional[Identity] = None
    # The assertedIdentity property
    asserted_identity: Optional[Identity] = None
    # The azureCommunicationServicesUser property
    azure_communication_services_user: Optional[Identity] = None
    # The encrypted property
    encrypted: Optional[Identity] = None
    # The endpointType property
    endpoint_type: Optional[EndpointType] = None
    # The guest property
    guest: Optional[Identity] = None
    # The onPremises property
    on_premises: Optional[Identity] = None
    # The phone property
    phone: Optional[Identity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CommunicationsIdentitySet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CommunicationsIdentitySet
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CommunicationsIdentitySet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .endpoint_type import EndpointType
        from .identity import Identity
        from .identity_set import IdentitySet

        from .endpoint_type import EndpointType
        from .identity import Identity
        from .identity_set import IdentitySet

        fields: Dict[str, Callable[[Any], None]] = {
            "application_instance": lambda n : setattr(self, 'application_instance', n.get_object_value(Identity)),
            "asserted_identity": lambda n : setattr(self, 'asserted_identity', n.get_object_value(Identity)),
            "azure_communication_services_user": lambda n : setattr(self, 'azure_communication_services_user', n.get_object_value(Identity)),
            "encrypted": lambda n : setattr(self, 'encrypted', n.get_object_value(Identity)),
            "endpoint_type": lambda n : setattr(self, 'endpoint_type', n.get_enum_value(EndpointType)),
            "guest": lambda n : setattr(self, 'guest', n.get_object_value(Identity)),
            "on_premises": lambda n : setattr(self, 'on_premises', n.get_object_value(Identity)),
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
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_object_value("application_instance", self.application_instance)
        writer.write_object_value("asserted_identity", self.asserted_identity)
        writer.write_object_value("azure_communication_services_user", self.azure_communication_services_user)
        writer.write_object_value("encrypted", self.encrypted)
        writer.write_enum_value("endpoint_type", self.endpoint_type)
        writer.write_object_value("guest", self.guest)
        writer.write_object_value("on_premises", self.on_premises)
        writer.write_object_value("phone", self.phone)
    

