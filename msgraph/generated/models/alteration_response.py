from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .search_alteration import SearchAlteration
    from .search_alteration_type import SearchAlterationType

@dataclass
class AlterationResponse(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Defines the original user query string.
    original_query_string: Optional[str] = None
    # Defines the details of the alteration information for the spelling correction.
    query_alteration: Optional[SearchAlteration] = None
    # Defines the type of the spelling correction. The possible values are: suggestion, modification.
    query_alteration_type: Optional[SearchAlterationType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AlterationResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AlterationResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AlterationResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .search_alteration import SearchAlteration
        from .search_alteration_type import SearchAlterationType

        from .search_alteration import SearchAlteration
        from .search_alteration_type import SearchAlterationType

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "originalQueryString": lambda n : setattr(self, 'original_query_string', n.get_str_value()),
            "queryAlteration": lambda n : setattr(self, 'query_alteration', n.get_object_value(SearchAlteration)),
            "queryAlterationType": lambda n : setattr(self, 'query_alteration_type', n.get_enum_value(SearchAlterationType)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("originalQueryString", self.original_query_string)
        writer.write_object_value("queryAlteration", self.query_alteration)
        writer.write_enum_value("queryAlterationType", self.query_alteration_type)
        writer.write_additional_data_value(self.additional_data)
    

