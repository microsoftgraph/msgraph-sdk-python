from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....models import item_body, key_value_pair, teamwork_activity_topic, teamwork_notification_recipient

@dataclass
class SendActivityNotificationPostRequestBody(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The activityType property
    activity_type: Optional[str] = None
    # The chainId property
    chain_id: Optional[int] = None
    # The previewText property
    preview_text: Optional[item_body.ItemBody] = None
    # The recipient property
    recipient: Optional[teamwork_notification_recipient.TeamworkNotificationRecipient] = None
    # The templateParameters property
    template_parameters: Optional[List[key_value_pair.KeyValuePair]] = None
    # The topic property
    topic: Optional[teamwork_activity_topic.TeamworkActivityTopic] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SendActivityNotificationPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SendActivityNotificationPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SendActivityNotificationPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....models import item_body, key_value_pair, teamwork_activity_topic, teamwork_notification_recipient

        fields: Dict[str, Callable[[Any], None]] = {
            "activityType": lambda n : setattr(self, 'activity_type', n.get_str_value()),
            "chainId": lambda n : setattr(self, 'chain_id', n.get_int_value()),
            "previewText": lambda n : setattr(self, 'preview_text', n.get_object_value(item_body.ItemBody)),
            "recipient": lambda n : setattr(self, 'recipient', n.get_object_value(teamwork_notification_recipient.TeamworkNotificationRecipient)),
            "templateParameters": lambda n : setattr(self, 'template_parameters', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "topic": lambda n : setattr(self, 'topic', n.get_object_value(teamwork_activity_topic.TeamworkActivityTopic)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("activityType", self.activity_type)
        writer.write_int_value("chainId", self.chain_id)
        writer.write_object_value("previewText", self.preview_text)
        writer.write_object_value("recipient", self.recipient)
        writer.write_collection_of_object_values("templateParameters", self.template_parameters)
        writer.write_object_value("topic", self.topic)
        writer.write_additional_data_value(self.additional_data)
    

