from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item_body import ItemBody
    from .post_type import PostType

@dataclass
class ServiceHealthIssuePost(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # The published time of the post.
    created_date_time: Optional[datetime.datetime] = None
    # The content of the service issue post. The supported value for the contentType property is html.
    description: Optional[ItemBody] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The post type of the service issue historical post. Possible values are: regular, quick, strategic, unknownFutureValue.
    post_type: Optional[PostType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServiceHealthIssuePost:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServiceHealthIssuePost
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServiceHealthIssuePost()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .item_body import ItemBody
        from .post_type import PostType

        from .item_body import ItemBody
        from .post_type import PostType

        fields: Dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_object_value(ItemBody)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "postType": lambda n : setattr(self, 'post_type', n.get_enum_value(PostType)),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("description", self.description)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("postType", self.post_type)
        writer.write_additional_data_value(self.additional_data)
    

