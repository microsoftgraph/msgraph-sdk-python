from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

item_body = lazy_import('msgraph.generated.models.item_body')
key_value_pair = lazy_import('msgraph.generated.models.key_value_pair')
teamwork_activity_topic = lazy_import('msgraph.generated.models.teamwork_activity_topic')

class SendActivityNotificationPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the sendActivityNotification method.
    """
    @property
    def activity_type(self,) -> Optional[str]:
        """
        Gets the activityType property value. The activityType property
        Returns: Optional[str]
        """
        return self._activity_type
    
    @activity_type.setter
    def activity_type(self,value: Optional[str] = None) -> None:
        """
        Sets the activityType property value. The activityType property
        Args:
            value: Value to set for the activityType property.
        """
        self._activity_type = value
    
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
    def chain_id(self,) -> Optional[int]:
        """
        Gets the chainId property value. The chainId property
        Returns: Optional[int]
        """
        return self._chain_id
    
    @chain_id.setter
    def chain_id(self,value: Optional[int] = None) -> None:
        """
        Sets the chainId property value. The chainId property
        Args:
            value: Value to set for the chainId property.
        """
        self._chain_id = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new sendActivityNotificationPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The activityType property
        self._activity_type: Optional[str] = None
        # The chainId property
        self._chain_id: Optional[int] = None
        # The previewText property
        self._preview_text: Optional[item_body.ItemBody] = None
        # The templateParameters property
        self._template_parameters: Optional[List[key_value_pair.KeyValuePair]] = None
        # The topic property
        self._topic: Optional[teamwork_activity_topic.TeamworkActivityTopic] = None
    
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
        fields = {
            "activity_type": lambda n : setattr(self, 'activity_type', n.get_str_value()),
            "chain_id": lambda n : setattr(self, 'chain_id', n.get_int_value()),
            "preview_text": lambda n : setattr(self, 'preview_text', n.get_object_value(item_body.ItemBody)),
            "template_parameters": lambda n : setattr(self, 'template_parameters', n.get_collection_of_object_values(key_value_pair.KeyValuePair)),
            "topic": lambda n : setattr(self, 'topic', n.get_object_value(teamwork_activity_topic.TeamworkActivityTopic)),
        }
        return fields
    
    @property
    def preview_text(self,) -> Optional[item_body.ItemBody]:
        """
        Gets the previewText property value. The previewText property
        Returns: Optional[item_body.ItemBody]
        """
        return self._preview_text
    
    @preview_text.setter
    def preview_text(self,value: Optional[item_body.ItemBody] = None) -> None:
        """
        Sets the previewText property value. The previewText property
        Args:
            value: Value to set for the previewText property.
        """
        self._preview_text = value
    
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
        writer.write_collection_of_object_values("templateParameters", self.template_parameters)
        writer.write_object_value("topic", self.topic)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def template_parameters(self,) -> Optional[List[key_value_pair.KeyValuePair]]:
        """
        Gets the templateParameters property value. The templateParameters property
        Returns: Optional[List[key_value_pair.KeyValuePair]]
        """
        return self._template_parameters
    
    @template_parameters.setter
    def template_parameters(self,value: Optional[List[key_value_pair.KeyValuePair]] = None) -> None:
        """
        Sets the templateParameters property value. The templateParameters property
        Args:
            value: Value to set for the templateParameters property.
        """
        self._template_parameters = value
    
    @property
    def topic(self,) -> Optional[teamwork_activity_topic.TeamworkActivityTopic]:
        """
        Gets the topic property value. The topic property
        Returns: Optional[teamwork_activity_topic.TeamworkActivityTopic]
        """
        return self._topic
    
    @topic.setter
    def topic(self,value: Optional[teamwork_activity_topic.TeamworkActivityTopic] = None) -> None:
        """
        Sets the topic property value. The topic property
        Args:
            value: Value to set for the topic property.
        """
        self._topic = value
    

