from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence

from .alert_evidence import AlertEvidence

@dataclass
class GitHubUserEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.gitHubUserEvidence"
    # The email property
    email: Optional[str] = None
    # The login property
    login: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The userId property
    user_id: Optional[str] = None
    # The webUrl property
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GitHubUserEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GitHubUserEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GitHubUserEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence

        from .alert_evidence import AlertEvidence

        fields: Dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "login": lambda n : setattr(self, 'login', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        writer.write_str_value("email", self.email)
        writer.write_str_value("login", self.login)
        writer.write_str_value("name", self.name)
        writer.write_str_value("userId", self.user_id)
        writer.write_str_value("webUrl", self.web_url)
    

