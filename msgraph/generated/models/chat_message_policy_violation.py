from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

chat_message_policy_violation_dlp_action_types = lazy_import('msgraph.generated.models.chat_message_policy_violation_dlp_action_types')
chat_message_policy_violation_policy_tip = lazy_import('msgraph.generated.models.chat_message_policy_violation_policy_tip')
chat_message_policy_violation_user_action_types = lazy_import('msgraph.generated.models.chat_message_policy_violation_user_action_types')
chat_message_policy_violation_verdict_details_types = lazy_import('msgraph.generated.models.chat_message_policy_violation_verdict_details_types')

class ChatMessagePolicyViolation(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new chatMessagePolicyViolation and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The action taken by the DLP provider on the message with sensitive content. Supported values are: NoneNotifySender -- Inform the sender of the violation but allow readers to read the message.BlockAccess -- Block readers from reading the message.BlockAccessExternal -- Block users outside the organization from reading the message, while allowing users within the organization to read the message.
        self._dlp_action: Optional[chat_message_policy_violation_dlp_action_types.ChatMessagePolicyViolationDlpActionTypes] = None
        # Justification text provided by the sender of the message when overriding a policy violation.
        self._justification_text: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Information to display to the message sender about why the message was flagged as a violation.
        self._policy_tip: Optional[chat_message_policy_violation_policy_tip.ChatMessagePolicyViolationPolicyTip] = None
        # Indicates the action taken by the user on a message blocked by the DLP provider. Supported values are: NoneOverrideReportFalsePositiveWhen the DLP provider is updating the message for blocking sensitive content, userAction is not required.
        self._user_action: Optional[chat_message_policy_violation_user_action_types.ChatMessagePolicyViolationUserActionTypes] = None
        # Indicates what actions the sender may take in response to the policy violation. Supported values are: NoneAllowFalsePositiveOverride -- Allows the sender to declare the policyViolation to be an error in the DLP app and its rules, and allow readers to see the message again if the dlpAction had hidden it.AllowOverrideWithoutJustification -- Allows the sender to overriide the DLP violation and allow readers to see the message again if the dlpAction had hidden it, without needing to provide an explanation for doing so. AllowOverrideWithJustification -- Allows the sender to overriide the DLP violation and allow readers to see the message again if the dlpAction had hidden it, after providing an explanation for doing so.AllowOverrideWithoutJustification and AllowOverrideWithJustification are mutually exclusive.
        self._verdict_details: Optional[chat_message_policy_violation_verdict_details_types.ChatMessagePolicyViolationVerdictDetailsTypes] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatMessagePolicyViolation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessagePolicyViolation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChatMessagePolicyViolation()
    
    @property
    def dlp_action(self,) -> Optional[chat_message_policy_violation_dlp_action_types.ChatMessagePolicyViolationDlpActionTypes]:
        """
        Gets the dlpAction property value. The action taken by the DLP provider on the message with sensitive content. Supported values are: NoneNotifySender -- Inform the sender of the violation but allow readers to read the message.BlockAccess -- Block readers from reading the message.BlockAccessExternal -- Block users outside the organization from reading the message, while allowing users within the organization to read the message.
        Returns: Optional[chat_message_policy_violation_dlp_action_types.ChatMessagePolicyViolationDlpActionTypes]
        """
        return self._dlp_action
    
    @dlp_action.setter
    def dlp_action(self,value: Optional[chat_message_policy_violation_dlp_action_types.ChatMessagePolicyViolationDlpActionTypes] = None) -> None:
        """
        Sets the dlpAction property value. The action taken by the DLP provider on the message with sensitive content. Supported values are: NoneNotifySender -- Inform the sender of the violation but allow readers to read the message.BlockAccess -- Block readers from reading the message.BlockAccessExternal -- Block users outside the organization from reading the message, while allowing users within the organization to read the message.
        Args:
            value: Value to set for the dlpAction property.
        """
        self._dlp_action = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "dlp_action": lambda n : setattr(self, 'dlp_action', n.get_enum_value(chat_message_policy_violation_dlp_action_types.ChatMessagePolicyViolationDlpActionTypes)),
            "justification_text": lambda n : setattr(self, 'justification_text', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policy_tip": lambda n : setattr(self, 'policy_tip', n.get_object_value(chat_message_policy_violation_policy_tip.ChatMessagePolicyViolationPolicyTip)),
            "user_action": lambda n : setattr(self, 'user_action', n.get_enum_value(chat_message_policy_violation_user_action_types.ChatMessagePolicyViolationUserActionTypes)),
            "verdict_details": lambda n : setattr(self, 'verdict_details', n.get_enum_value(chat_message_policy_violation_verdict_details_types.ChatMessagePolicyViolationVerdictDetailsTypes)),
        }
        return fields
    
    @property
    def justification_text(self,) -> Optional[str]:
        """
        Gets the justificationText property value. Justification text provided by the sender of the message when overriding a policy violation.
        Returns: Optional[str]
        """
        return self._justification_text
    
    @justification_text.setter
    def justification_text(self,value: Optional[str] = None) -> None:
        """
        Sets the justificationText property value. Justification text provided by the sender of the message when overriding a policy violation.
        Args:
            value: Value to set for the justificationText property.
        """
        self._justification_text = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def policy_tip(self,) -> Optional[chat_message_policy_violation_policy_tip.ChatMessagePolicyViolationPolicyTip]:
        """
        Gets the policyTip property value. Information to display to the message sender about why the message was flagged as a violation.
        Returns: Optional[chat_message_policy_violation_policy_tip.ChatMessagePolicyViolationPolicyTip]
        """
        return self._policy_tip
    
    @policy_tip.setter
    def policy_tip(self,value: Optional[chat_message_policy_violation_policy_tip.ChatMessagePolicyViolationPolicyTip] = None) -> None:
        """
        Sets the policyTip property value. Information to display to the message sender about why the message was flagged as a violation.
        Args:
            value: Value to set for the policyTip property.
        """
        self._policy_tip = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("dlpAction", self.dlp_action)
        writer.write_str_value("justificationText", self.justification_text)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("policyTip", self.policy_tip)
        writer.write_enum_value("userAction", self.user_action)
        writer.write_enum_value("verdictDetails", self.verdict_details)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user_action(self,) -> Optional[chat_message_policy_violation_user_action_types.ChatMessagePolicyViolationUserActionTypes]:
        """
        Gets the userAction property value. Indicates the action taken by the user on a message blocked by the DLP provider. Supported values are: NoneOverrideReportFalsePositiveWhen the DLP provider is updating the message for blocking sensitive content, userAction is not required.
        Returns: Optional[chat_message_policy_violation_user_action_types.ChatMessagePolicyViolationUserActionTypes]
        """
        return self._user_action
    
    @user_action.setter
    def user_action(self,value: Optional[chat_message_policy_violation_user_action_types.ChatMessagePolicyViolationUserActionTypes] = None) -> None:
        """
        Sets the userAction property value. Indicates the action taken by the user on a message blocked by the DLP provider. Supported values are: NoneOverrideReportFalsePositiveWhen the DLP provider is updating the message for blocking sensitive content, userAction is not required.
        Args:
            value: Value to set for the userAction property.
        """
        self._user_action = value
    
    @property
    def verdict_details(self,) -> Optional[chat_message_policy_violation_verdict_details_types.ChatMessagePolicyViolationVerdictDetailsTypes]:
        """
        Gets the verdictDetails property value. Indicates what actions the sender may take in response to the policy violation. Supported values are: NoneAllowFalsePositiveOverride -- Allows the sender to declare the policyViolation to be an error in the DLP app and its rules, and allow readers to see the message again if the dlpAction had hidden it.AllowOverrideWithoutJustification -- Allows the sender to overriide the DLP violation and allow readers to see the message again if the dlpAction had hidden it, without needing to provide an explanation for doing so. AllowOverrideWithJustification -- Allows the sender to overriide the DLP violation and allow readers to see the message again if the dlpAction had hidden it, after providing an explanation for doing so.AllowOverrideWithoutJustification and AllowOverrideWithJustification are mutually exclusive.
        Returns: Optional[chat_message_policy_violation_verdict_details_types.ChatMessagePolicyViolationVerdictDetailsTypes]
        """
        return self._verdict_details
    
    @verdict_details.setter
    def verdict_details(self,value: Optional[chat_message_policy_violation_verdict_details_types.ChatMessagePolicyViolationVerdictDetailsTypes] = None) -> None:
        """
        Sets the verdictDetails property value. Indicates what actions the sender may take in response to the policy violation. Supported values are: NoneAllowFalsePositiveOverride -- Allows the sender to declare the policyViolation to be an error in the DLP app and its rules, and allow readers to see the message again if the dlpAction had hidden it.AllowOverrideWithoutJustification -- Allows the sender to overriide the DLP violation and allow readers to see the message again if the dlpAction had hidden it, without needing to provide an explanation for doing so. AllowOverrideWithJustification -- Allows the sender to overriide the DLP violation and allow readers to see the message again if the dlpAction had hidden it, after providing an explanation for doing so.AllowOverrideWithoutJustification and AllowOverrideWithJustification are mutually exclusive.
        Args:
            value: Value to set for the verdictDetails property.
        """
        self._verdict_details = value
    

