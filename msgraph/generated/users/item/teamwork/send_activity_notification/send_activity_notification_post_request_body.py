from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.item_body import ItemBody
    from .....models.key_value_pair import KeyValuePair
    from .....models.teamwork_activity_topic import TeamworkActivityTopic

@dataclass
class SendActivityNotificationPostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The activityType property
    activity_type: Optional[str] = None
    # The chainId property
    chain_id: Optional[int] = None
    # The iconId property
    icon_id: Optional[str] = None
    # The previewText property
    preview_text: Optional[ItemBody] = None
    # The teamsAppId property
    teams_app_id: Optional[str] = None
    # The templateParameters property
    template_parameters: Optional[list[KeyValuePair]] = None
    # The topic property
    topic: Optional[TeamworkActivityTopic] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SendActivityNotificationPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SendActivityNotificationPostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SendActivityNotificationPostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....models.item_body import ItemBody
        from .....models.key_value_pair import KeyValuePair
        from .....models.teamwork_activity_topic import TeamworkActivityTopic

        from .....models.item_body import ItemBody
        from .....models.key_value_pair import KeyValuePair
        from .....models.teamwork_activity_topic import TeamworkActivityTopic

        fields: dict[str, Callable[[Any], None]] = {
            "activityType": lambda n : setattr(self, 'activity_type', n.get_str_value()),
            "chainId": lambda n : setattr(self, 'chain_id', n.get_int_value()),
            "iconId": lambda n : setattr(self, 'icon_id', n.get_str_value()),
            "previewText": lambda n : setattr(self, 'preview_text', n.get_object_value(ItemBody)),
            "teamsAppId": lambda n : setattr(self, 'teams_app_id', n.get_str_value()),
            "templateParameters": lambda n : setattr(self, 'template_parameters', n.get_collection_of_object_values(KeyValuePair)),
            "topic": lambda n : setattr(self, 'topic', n.get_object_value(TeamworkActivityTopic)),
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
        writer.write_str_value("activityType", self.activity_type)
        writer.write_int_value("chainId", self.chain_id)
        writer.write_str_value("iconId", self.icon_id)
        writer.write_object_value("previewText", self.preview_text)
        writer.write_str_value("teamsAppId", self.teams_app_id)
        writer.write_collection_of_object_values("templateParameters", self.template_parameters)
        writer.write_object_value("topic", self.topic)
        writer.write_additional_data_value(self.additional_data)
    

