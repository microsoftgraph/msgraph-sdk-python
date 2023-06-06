from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import identity, teamwork_application_identity_type

from . import identity

@dataclass
class TeamworkApplicationIdentity(identity.Identity):
    odata_type = "#microsoft.graph.teamworkApplicationIdentity"
    # Type of application that is referenced. Possible values are: aadApplication, bot, tenantBot, office365Connector, outgoingWebhook, and unknownFutureValue.
    application_identity_type: Optional[teamwork_application_identity_type.TeamworkApplicationIdentityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkApplicationIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkApplicationIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkApplicationIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import identity, teamwork_application_identity_type

        fields: Dict[str, Callable[[Any], None]] = {
            "applicationIdentityType": lambda n : setattr(self, 'application_identity_type', n.get_enum_value(teamwork_application_identity_type.TeamworkApplicationIdentityType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("applicationIdentityType", self.application_identity_type)
    

