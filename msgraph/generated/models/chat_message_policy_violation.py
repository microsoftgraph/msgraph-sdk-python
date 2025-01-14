from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .chat_message_policy_violation_dlp_action_types import ChatMessagePolicyViolationDlpActionTypes
    from .chat_message_policy_violation_policy_tip import ChatMessagePolicyViolationPolicyTip
    from .chat_message_policy_violation_user_action_types import ChatMessagePolicyViolationUserActionTypes
    from .chat_message_policy_violation_verdict_details_types import ChatMessagePolicyViolationVerdictDetailsTypes

@dataclass
class ChatMessagePolicyViolation(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The action taken by the DLP provider on the message with sensitive content. Supported values are: NoneNotifySender -- Inform the sender of the violation but allow readers to read the message.BlockAccess -- Block readers from reading the message.BlockAccessExternal -- Block users outside the organization from reading the message, while allowing users within the organization to read the message.
    dlp_action: Optional[ChatMessagePolicyViolationDlpActionTypes] = None
    # Justification text provided by the sender of the message when overriding a policy violation.
    justification_text: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Information to display to the message sender about why the message was flagged as a violation.
    policy_tip: Optional[ChatMessagePolicyViolationPolicyTip] = None
    # Indicates the action taken by the user on a message blocked by the DLP provider. Supported values are: NoneOverrideReportFalsePositiveWhen the DLP provider is updating the message for blocking sensitive content, userAction isn't required.
    user_action: Optional[ChatMessagePolicyViolationUserActionTypes] = None
    # Indicates what actions the sender may take in response to the policy violation. Supported values are: NoneAllowFalsePositiveOverride -- Allows the sender to declare the policyViolation to be an error in the DLP app and its rules, and allow readers to see the message again if the dlpAction hides it.AllowOverrideWithoutJustification -- Allows the sender to override the DLP violation and allow readers to see the message again if the dlpAction hides it, without needing to provide an explanation for doing so. AllowOverrideWithJustification -- Allows the sender to override the DLP violation and allow readers to see the message again if the dlpAction hides it, after providing an explanation for doing so.AllowOverrideWithoutJustification and AllowOverrideWithJustification are mutually exclusive.
    verdict_details: Optional[ChatMessagePolicyViolationVerdictDetailsTypes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChatMessagePolicyViolation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessagePolicyViolation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChatMessagePolicyViolation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .chat_message_policy_violation_dlp_action_types import ChatMessagePolicyViolationDlpActionTypes
        from .chat_message_policy_violation_policy_tip import ChatMessagePolicyViolationPolicyTip
        from .chat_message_policy_violation_user_action_types import ChatMessagePolicyViolationUserActionTypes
        from .chat_message_policy_violation_verdict_details_types import ChatMessagePolicyViolationVerdictDetailsTypes

        from .chat_message_policy_violation_dlp_action_types import ChatMessagePolicyViolationDlpActionTypes
        from .chat_message_policy_violation_policy_tip import ChatMessagePolicyViolationPolicyTip
        from .chat_message_policy_violation_user_action_types import ChatMessagePolicyViolationUserActionTypes
        from .chat_message_policy_violation_verdict_details_types import ChatMessagePolicyViolationVerdictDetailsTypes

        fields: dict[str, Callable[[Any], None]] = {
            "dlpAction": lambda n : setattr(self, 'dlp_action', n.get_collection_of_enum_values(ChatMessagePolicyViolationDlpActionTypes)),
            "justificationText": lambda n : setattr(self, 'justification_text', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyTip": lambda n : setattr(self, 'policy_tip', n.get_object_value(ChatMessagePolicyViolationPolicyTip)),
            "userAction": lambda n : setattr(self, 'user_action', n.get_collection_of_enum_values(ChatMessagePolicyViolationUserActionTypes)),
            "verdictDetails": lambda n : setattr(self, 'verdict_details', n.get_collection_of_enum_values(ChatMessagePolicyViolationVerdictDetailsTypes)),
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
        writer.write_enum_value("dlpAction", self.dlp_action)
        writer.write_str_value("justificationText", self.justification_text)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("policyTip", self.policy_tip)
        writer.write_enum_value("userAction", self.user_action)
        writer.write_enum_value("verdictDetails", self.verdict_details)
        writer.write_additional_data_value(self.additional_data)
    

