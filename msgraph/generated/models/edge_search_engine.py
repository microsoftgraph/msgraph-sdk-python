from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

edge_search_engine_base = lazy_import('msgraph.generated.models.edge_search_engine_base')
edge_search_engine_type = lazy_import('msgraph.generated.models.edge_search_engine_type')

class EdgeSearchEngine(edge_search_engine_base.EdgeSearchEngineBase):
    def __init__(self,) -> None:
        """
        Instantiates a new EdgeSearchEngine and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.edgeSearchEngine"
        # Allows IT admind to set a predefined default search engine for MDM-Controlled devices
        self._edge_search_engine_type: Optional[edge_search_engine_type.EdgeSearchEngineType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdgeSearchEngine:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdgeSearchEngine
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdgeSearchEngine()
    
    @property
    def edge_search_engine_type(self,) -> Optional[edge_search_engine_type.EdgeSearchEngineType]:
        """
        Gets the edgeSearchEngineType property value. Allows IT admind to set a predefined default search engine for MDM-Controlled devices
        Returns: Optional[edge_search_engine_type.EdgeSearchEngineType]
        """
        return self._edge_search_engine_type
    
    @edge_search_engine_type.setter
    def edge_search_engine_type(self,value: Optional[edge_search_engine_type.EdgeSearchEngineType] = None) -> None:
        """
        Sets the edgeSearchEngineType property value. Allows IT admind to set a predefined default search engine for MDM-Controlled devices
        Args:
            value: Value to set for the edgeSearchEngineType property.
        """
        self._edge_search_engine_type = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "edge_search_engine_type": lambda n : setattr(self, 'edge_search_engine_type', n.get_enum_value(edge_search_engine_type.EdgeSearchEngineType)),
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
        writer.write_enum_value("edgeSearchEngineType", self.edge_search_engine_type)
    

