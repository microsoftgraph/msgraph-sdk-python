from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.security.analyzed_email import AnalyzedEmail
    from .....models.security.remediation_action import RemediationAction
    from .....models.security.remediation_severity import RemediationSeverity

@dataclass
class RemediatePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The remediateSendersCopy property
    remediate_senders_copy: Optional[bool] = False
    # The action property
    action: Optional[RemediationAction] = None
    # The analyzedEmails property
    analyzed_emails: Optional[list[AnalyzedEmail]] = None
    # The description property
    description: Optional[str] = None
    # The displayName property
    display_name: Optional[str] = None
    # The severity property
    severity: Optional[RemediationSeverity] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RemediatePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RemediatePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RemediatePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.security.analyzed_email import AnalyzedEmail
        from .....models.security.remediation_action import RemediationAction
        from .....models.security.remediation_severity import RemediationSeverity

        from .....models.security.analyzed_email import AnalyzedEmail
        from .....models.security.remediation_action import RemediationAction
        from .....models.security.remediation_severity import RemediationSeverity

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(RemediationAction)),
            "analyzedEmails": lambda n : setattr(self, 'analyzed_emails', n.get_collection_of_object_values(AnalyzedEmail)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "remediateSendersCopy": lambda n : setattr(self, 'remediate_senders_copy', n.get_bool_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(RemediationSeverity)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_enum_value("action", self.action)
        writer.write_collection_of_object_values("analyzedEmails", self.analyzed_emails)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("remediateSendersCopy", self.remediate_senders_copy)
        writer.write_enum_value("severity", self.severity)
        writer.write_additional_data_value(self.additional_data)
    

