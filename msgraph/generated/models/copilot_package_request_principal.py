from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .copilot_package_request_principal_type import CopilotPackageRequestPrincipalType
    from .identity import Identity

from .identity import Identity

@dataclass
class CopilotPackageRequestPrincipal(Identity, Parsable):
    """
    A read-only snapshot of one explicit Governance assignee. Inherited id and displayName are the source identifier and resolved name, or null when unavailable. Identifier meaning depends on principalType and does not imply a resolvable directory-object URL. Openness is inherited from identity; the producer returns only the documented fields, never raw owner objects.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.copilotPackageRequestPrincipal"
    # The principalType property
    principal_type: Optional[CopilotPackageRequestPrincipalType] = None
    # The actual userPrincipalName returned by Governance for user or agentUser principals. Null when unavailable and for other principal kinds. Never inferred from an email address or creator identity.
    user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CopilotPackageRequestPrincipal:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CopilotPackageRequestPrincipal
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CopilotPackageRequestPrincipal()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .copilot_package_request_principal_type import CopilotPackageRequestPrincipalType
        from .identity import Identity

        from .copilot_package_request_principal_type import CopilotPackageRequestPrincipalType
        from .identity import Identity

        fields: dict[str, Callable[[Any], None]] = {
            "principalType": lambda n : setattr(self, 'principal_type', n.get_enum_value(CopilotPackageRequestPrincipalType)),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
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
        writer.write_enum_value("principalType", self.principal_type)
    

