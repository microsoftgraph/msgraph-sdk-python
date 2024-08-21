from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .edge_search_engine_base import EdgeSearchEngineBase
    from .edge_search_engine_type import EdgeSearchEngineType

from .edge_search_engine_base import EdgeSearchEngineBase

@dataclass
class EdgeSearchEngine(EdgeSearchEngineBase):
    """
    Allows IT admins to set a predefined default search engine for MDM-Controlled devices.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.edgeSearchEngine"
    # Allows IT admind to set a predefined default search engine for MDM-Controlled devices
    edge_search_engine_type: Optional[EdgeSearchEngineType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EdgeSearchEngine:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdgeSearchEngine
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EdgeSearchEngine()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .edge_search_engine_base import EdgeSearchEngineBase
        from .edge_search_engine_type import EdgeSearchEngineType

        from .edge_search_engine_base import EdgeSearchEngineBase
        from .edge_search_engine_type import EdgeSearchEngineType

        fields: Dict[str, Callable[[Any], None]] = {
            "edgeSearchEngineType": lambda n : setattr(self, 'edge_search_engine_type', n.get_enum_value(EdgeSearchEngineType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_enum_value("edgeSearchEngineType", self.edge_search_engine_type)
    

