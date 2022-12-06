from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

identity = lazy_import('msgraph.generated.models.identity')
teamwork_user_identity_type = lazy_import('msgraph.generated.models.teamwork_user_identity_type')

class TeamworkUserIdentity(identity.Identity):
    def __init__(self,) -> None:
        """
        Instantiates a new TeamworkUserIdentity and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.teamworkUserIdentity"
        # Type of user. Possible values are: aadUser, onPremiseAadUser, anonymousGuest, federatedUser, personalMicrosoftAccountUser, skypeUser, phoneUser, unknownFutureValue and emailUser.
        self._user_identity_type: Optional[teamwork_user_identity_type.TeamworkUserIdentityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamworkUserIdentity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamworkUserIdentity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamworkUserIdentity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "user_identity_type": lambda n : setattr(self, 'user_identity_type', n.get_enum_value(teamwork_user_identity_type.TeamworkUserIdentityType)),
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
        writer.write_enum_value("userIdentityType", self.user_identity_type)
    
    @property
    def user_identity_type(self,) -> Optional[teamwork_user_identity_type.TeamworkUserIdentityType]:
        """
        Gets the userIdentityType property value. Type of user. Possible values are: aadUser, onPremiseAadUser, anonymousGuest, federatedUser, personalMicrosoftAccountUser, skypeUser, phoneUser, unknownFutureValue and emailUser.
        Returns: Optional[teamwork_user_identity_type.TeamworkUserIdentityType]
        """
        return self._user_identity_type
    
    @user_identity_type.setter
    def user_identity_type(self,value: Optional[teamwork_user_identity_type.TeamworkUserIdentityType] = None) -> None:
        """
        Sets the userIdentityType property value. Type of user. Possible values are: aadUser, onPremiseAadUser, anonymousGuest, federatedUser, personalMicrosoftAccountUser, skypeUser, phoneUser, unknownFutureValue and emailUser.
        Args:
            value: Value to set for the userIdentityType property.
        """
        self._user_identity_type = value
    

