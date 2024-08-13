from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_evidence import AlertEvidence

from .alert_evidence import AlertEvidence

@dataclass
class GitHubRepoEvidence(AlertEvidence):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.gitHubRepoEvidence"
    # The baseUrl property
    base_url: Optional[str] = None
    # The login property
    login: Optional[str] = None
    # The owner property
    owner: Optional[str] = None
    # The ownerType property
    owner_type: Optional[str] = None
    # The repoId property
    repo_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GitHubRepoEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GitHubRepoEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GitHubRepoEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .alert_evidence import AlertEvidence

        from .alert_evidence import AlertEvidence

        fields: Dict[str, Callable[[Any], None]] = {
            "baseUrl": lambda n : setattr(self, 'base_url', n.get_str_value()),
            "login": lambda n : setattr(self, 'login', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "ownerType": lambda n : setattr(self, 'owner_type', n.get_str_value()),
            "repoId": lambda n : setattr(self, 'repo_id', n.get_str_value()),
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
        writer.write_str_value("baseUrl", self.base_url)
        writer.write_str_value("login", self.login)
        writer.write_str_value("owner", self.owner)
        writer.write_str_value("ownerType", self.owner_type)
        writer.write_str_value("repoId", self.repo_id)
    

