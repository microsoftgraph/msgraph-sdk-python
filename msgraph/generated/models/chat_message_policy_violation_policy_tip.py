from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ChatMessagePolicyViolationPolicyTip(AdditionalDataHolder, Parsable):
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
    
    @property
    def compliance_url(self,) -> Optional[str]:
        """
        Gets the complianceUrl property value. The URL a user can visit to read about the data loss prevention policies for the organization. (ie, policies about what users shouldn't say in chats)
        Returns: Optional[str]
        """
        return self._compliance_url
    
    @compliance_url.setter
    def compliance_url(self,value: Optional[str] = None) -> None:
        """
        Sets the complianceUrl property value. The URL a user can visit to read about the data loss prevention policies for the organization. (ie, policies about what users shouldn't say in chats)
        Args:
            value: Value to set for the complianceUrl property.
        """
        self._compliance_url = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new chatMessagePolicyViolationPolicyTip and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The URL a user can visit to read about the data loss prevention policies for the organization. (ie, policies about what users shouldn't say in chats)
        self._compliance_url: Optional[str] = None
        # Explanatory text shown to the sender of the message.
        self._general_text: Optional[str] = None
        # The list of improper data in the message that was detected by the data loss prevention app. Each DLP app defines its own conditions, examples include 'Credit Card Number' and 'Social Security Number'.
        self._matched_condition_descriptions: Optional[List[str]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ChatMessagePolicyViolationPolicyTip:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ChatMessagePolicyViolationPolicyTip
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ChatMessagePolicyViolationPolicyTip()
    
    @property
    def general_text(self,) -> Optional[str]:
        """
        Gets the generalText property value. Explanatory text shown to the sender of the message.
        Returns: Optional[str]
        """
        return self._general_text
    
    @general_text.setter
    def general_text(self,value: Optional[str] = None) -> None:
        """
        Sets the generalText property value. Explanatory text shown to the sender of the message.
        Args:
            value: Value to set for the generalText property.
        """
        self._general_text = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "compliance_url": lambda n : setattr(self, 'compliance_url', n.get_str_value()),
            "general_text": lambda n : setattr(self, 'general_text', n.get_str_value()),
            "matched_condition_descriptions": lambda n : setattr(self, 'matched_condition_descriptions', n.get_collection_of_primitive_values(str)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def matched_condition_descriptions(self,) -> Optional[List[str]]:
        """
        Gets the matchedConditionDescriptions property value. The list of improper data in the message that was detected by the data loss prevention app. Each DLP app defines its own conditions, examples include 'Credit Card Number' and 'Social Security Number'.
        Returns: Optional[List[str]]
        """
        return self._matched_condition_descriptions
    
    @matched_condition_descriptions.setter
    def matched_condition_descriptions(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the matchedConditionDescriptions property value. The list of improper data in the message that was detected by the data loss prevention app. Each DLP app defines its own conditions, examples include 'Credit Card Number' and 'Social Security Number'.
        Args:
            value: Value to set for the matchedConditionDescriptions property.
        """
        self._matched_condition_descriptions = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("complianceUrl", self.compliance_url)
        writer.write_str_value("generalText", self.general_text)
        writer.write_collection_of_primitive_values("matchedConditionDescriptions", self.matched_condition_descriptions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

