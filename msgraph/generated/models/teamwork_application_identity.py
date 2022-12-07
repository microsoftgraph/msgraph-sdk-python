from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity = lazy_import('msgraph.generated.models.identity')
teamwork_application_identity_type = lazy_import('msgraph.generated.models.teamwork_application_identity_type')

class TeamworkApplicationIdentity(identity.Identity):
    @property
    def application_identity_type(self,) -> Optional[teamwork_application_identity_type.TeamworkApplicationIdentityType]:
        """
        Gets the applicationIdentityType property value. Type of application that is referenced. Possible values are: aadApplication, bot, tenantBot, office365Connector, outgoingWebhook, and unknownFutureValue.
        Returns: Optional[teamwork_application_identity_type.TeamworkApplicationIdentityType]
        """
        return self._application_identity_type
    
    @application_identity_type.setter
    def application_identity_type(self,value: Optional[teamwork_application_identity_type.TeamworkApplicationIdentityType] = None) -> None:
        """
        Sets the applicationIdentityType property value. Type of application that is referenced. Possible values are: aadApplication, bot, tenantBot, office365Connector, outgoingWebhook, and unknownFutureValue.
        Args:
            value: Value to set for the applicationIdentityType property.
        """
        self._application_identity_type = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new TeamworkApplicationIdentity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.teamworkApplicationIdentity"
        # Type of application that is referenced. Possible values are: aadApplication, bot, tenantBot, office365Connector, outgoingWebhook, and unknownFutureValue.
        self._application_identity_type: Optional[teamwork_application_identity_type.TeamworkApplicationIdentityType] = None
    
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
        fields = {
            "application_identity_type": lambda n : setattr(self, 'application_identity_type', n.get_enum_value(teamwork_application_identity_type.TeamworkApplicationIdentityType)),
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
    

