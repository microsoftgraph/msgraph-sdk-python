from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .ai_agent_platform import AiAgentPlatform
    from .alert_evidence import AlertEvidence

from .alert_evidence import AlertEvidence

@dataclass
class AiAgentEvidence(AlertEvidence, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.security.aiAgentEvidence"
    # The unique identifier for the AI agent.
    agent_id: Optional[str] = None
    # The display name for the AI agent.
    agent_name: Optional[str] = None
    # Type of the platform the agent runs on. The possible values are: unknown, azureAIFoundry, copilotStudio, copilot, unknownFutureValue.
    hosting_platform_type: Optional[AiAgentPlatform] = None
    # The instructions of the agent.
    instructions: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AiAgentEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AiAgentEvidence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AiAgentEvidence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .ai_agent_platform import AiAgentPlatform
        from .alert_evidence import AlertEvidence

        from .ai_agent_platform import AiAgentPlatform
        from .alert_evidence import AlertEvidence

        fields: dict[str, Callable[[Any], None]] = {
            "agentId": lambda n : setattr(self, 'agent_id', n.get_str_value()),
            "agentName": lambda n : setattr(self, 'agent_name', n.get_str_value()),
            "hostingPlatformType": lambda n : setattr(self, 'hosting_platform_type', n.get_enum_value(AiAgentPlatform)),
            "instructions": lambda n : setattr(self, 'instructions', n.get_str_value()),
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
        writer.write_str_value("agentId", self.agent_id)
        writer.write_str_value("agentName", self.agent_name)
        writer.write_enum_value("hostingPlatformType", self.hosting_platform_type)
        writer.write_str_value("instructions", self.instructions)
    

