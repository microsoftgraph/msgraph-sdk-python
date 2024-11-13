from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .edge_search_engine_base import EdgeSearchEngineBase

from .edge_search_engine_base import EdgeSearchEngineBase

@dataclass
class EdgeSearchEngineCustom(EdgeSearchEngineBase, Parsable):
    """
    Allows IT admins to set a custom default search engine for MDM-Controlled devices.
    """
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.edgeSearchEngineCustom"
    # Points to a https link containing the OpenSearch xml file that contains, at minimum, the short name and the URL to the search Engine.
    edge_search_engine_open_search_xml_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EdgeSearchEngineCustom:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EdgeSearchEngineCustom
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EdgeSearchEngineCustom()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .edge_search_engine_base import EdgeSearchEngineBase

        from .edge_search_engine_base import EdgeSearchEngineBase

        fields: Dict[str, Callable[[Any], None]] = {
            "edgeSearchEngineOpenSearchXmlUrl": lambda n : setattr(self, 'edge_search_engine_open_search_xml_url', n.get_str_value()),
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
        from .edge_search_engine_base import EdgeSearchEngineBase

        writer.write_str_value("edgeSearchEngineOpenSearchXmlUrl", self.edge_search_engine_open_search_xml_url)
    

