from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

edge_search_engine_base = lazy_import('msgraph.generated.models.edge_search_engine_base')

class EdgeSearchEngineCustom(edge_search_engine_base.EdgeSearchEngineBase):
    def __init__(self,) -> None:
        """
        Instantiates a new EdgeSearchEngineCustom and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.edgeSearchEngineCustom"
        # Points to a https link containing the OpenSearch xml file that contains, at minimum, the short name and the URL to the search Engine.
        self._edge_search_engine_open_search_xml_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdgeSearchEngineCustom:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdgeSearchEngineCustom
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdgeSearchEngineCustom()
    
    @property
    def edge_search_engine_open_search_xml_url(self,) -> Optional[str]:
        """
        Gets the edgeSearchEngineOpenSearchXmlUrl property value. Points to a https link containing the OpenSearch xml file that contains, at minimum, the short name and the URL to the search Engine.
        Returns: Optional[str]
        """
        return self._edge_search_engine_open_search_xml_url
    
    @edge_search_engine_open_search_xml_url.setter
    def edge_search_engine_open_search_xml_url(self,value: Optional[str] = None) -> None:
        """
        Sets the edgeSearchEngineOpenSearchXmlUrl property value. Points to a https link containing the OpenSearch xml file that contains, at minimum, the short name and the URL to the search Engine.
        Args:
            value: Value to set for the edgeSearchEngineOpenSearchXmlUrl property.
        """
        self._edge_search_engine_open_search_xml_url = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "edge_search_engine_open_search_xml_url": lambda n : setattr(self, 'edge_search_engine_open_search_xml_url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("edgeSearchEngineOpenSearchXmlUrl", self.edge_search_engine_open_search_xml_url)
    

