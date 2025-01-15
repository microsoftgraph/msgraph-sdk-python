from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity

@dataclass
class SearchHit(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The name of the content source that the externalItem is part of.
    content_source: Optional[str] = None
    # The internal identifier for the item. The format of the identifier varies based on the entity type. For details, see hitId format.
    hit_id: Optional[str] = None
    # Indicates whether the current result is collapsed when the collapseProperties property in the searchRequest is used.
    is_collapsed: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The rank or the order of the result.
    rank: Optional[int] = None
    # The resource property
    resource: Optional[Entity] = None
    # ID of the result template used to render the search result. This ID must map to a display layout in the resultTemplates dictionary that is also included in the searchResponse.
    result_template_id: Optional[str] = None
    # A summary of the result, if a summary is available.
    summary: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SearchHit:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SearchHit
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SearchHit()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity

        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "contentSource": lambda n : setattr(self, 'content_source', n.get_str_value()),
            "hitId": lambda n : setattr(self, 'hit_id', n.get_str_value()),
            "isCollapsed": lambda n : setattr(self, 'is_collapsed', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "rank": lambda n : setattr(self, 'rank', n.get_int_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(Entity)),
            "resultTemplateId": lambda n : setattr(self, 'result_template_id', n.get_str_value()),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
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
        writer.write_str_value("contentSource", self.content_source)
        writer.write_str_value("hitId", self.hit_id)
        writer.write_bool_value("isCollapsed", self.is_collapsed)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("rank", self.rank)
        writer.write_object_value("resource", self.resource)
        writer.write_str_value("resultTemplateId", self.result_template_id)
        writer.write_str_value("summary", self.summary)
        writer.write_additional_data_value(self.additional_data)
    

