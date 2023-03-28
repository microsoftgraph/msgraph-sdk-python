from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

chat = lazy_import('msgraph.generated.models.chat')
teams_app_installation = lazy_import('msgraph.generated.models.teams_app_installation')

class UserScopeTeamsAppInstallation(teams_app_installation.TeamsAppInstallation):
    @property
    def chat(self,) -> Optional[chat.Chat]:
        """
        Gets the chat property value. The chat between the user and Teams app.
        Returns: Optional[chat.Chat]
        """
        return self._chat
    
    @chat.setter
    def chat(self,value: Optional[chat.Chat] = None) -> None:
        """
        Sets the chat property value. The chat between the user and Teams app.
        Args:
            value: Value to set for the chat property.
        """
        self._chat = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new UserScopeTeamsAppInstallation and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.userScopeTeamsAppInstallation"
        # The chat between the user and Teams app.
        self._chat: Optional[chat.Chat] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> UserScopeTeamsAppInstallation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: UserScopeTeamsAppInstallation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return UserScopeTeamsAppInstallation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "chat": lambda n : setattr(self, 'chat', n.get_object_value(chat.Chat)),
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
        writer.write_object_value("chat", self.chat)
    

