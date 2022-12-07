from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

altered_query_token = lazy_import('msgraph.generated.models.altered_query_token')

class SearchAlteration(AdditionalDataHolder, Parsable):
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
    def altered_highlighted_query_string(self,) -> Optional[str]:
        """
        Gets the alteredHighlightedQueryString property value. Defines the altered highlighted query string with spelling correction. The annotation around the corrected segment is: /ue000, /ue001.
        Returns: Optional[str]
        """
        return self._altered_highlighted_query_string
    
    @altered_highlighted_query_string.setter
    def altered_highlighted_query_string(self,value: Optional[str] = None) -> None:
        """
        Sets the alteredHighlightedQueryString property value. Defines the altered highlighted query string with spelling correction. The annotation around the corrected segment is: /ue000, /ue001.
        Args:
            value: Value to set for the alteredHighlightedQueryString property.
        """
        self._altered_highlighted_query_string = value
    
    @property
    def altered_query_string(self,) -> Optional[str]:
        """
        Gets the alteredQueryString property value. Defines the altered query string with spelling correction.
        Returns: Optional[str]
        """
        return self._altered_query_string
    
    @altered_query_string.setter
    def altered_query_string(self,value: Optional[str] = None) -> None:
        """
        Sets the alteredQueryString property value. Defines the altered query string with spelling correction.
        Args:
            value: Value to set for the alteredQueryString property.
        """
        self._altered_query_string = value
    
    @property
    def altered_query_tokens(self,) -> Optional[List[altered_query_token.AlteredQueryToken]]:
        """
        Gets the alteredQueryTokens property value. Represents changed segments related to an original user query.
        Returns: Optional[List[altered_query_token.AlteredQueryToken]]
        """
        return self._altered_query_tokens
    
    @altered_query_tokens.setter
    def altered_query_tokens(self,value: Optional[List[altered_query_token.AlteredQueryToken]] = None) -> None:
        """
        Sets the alteredQueryTokens property value. Represents changed segments related to an original user query.
        Args:
            value: Value to set for the alteredQueryTokens property.
        """
        self._altered_query_tokens = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new searchAlteration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Defines the altered highlighted query string with spelling correction. The annotation around the corrected segment is: /ue000, /ue001.
        self._altered_highlighted_query_string: Optional[str] = None
        # Defines the altered query string with spelling correction.
        self._altered_query_string: Optional[str] = None
        # Represents changed segments related to an original user query.
        self._altered_query_tokens: Optional[List[altered_query_token.AlteredQueryToken]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SearchAlteration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SearchAlteration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SearchAlteration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "altered_highlighted_query_string": lambda n : setattr(self, 'altered_highlighted_query_string', n.get_str_value()),
            "altered_query_string": lambda n : setattr(self, 'altered_query_string', n.get_str_value()),
            "altered_query_tokens": lambda n : setattr(self, 'altered_query_tokens', n.get_collection_of_object_values(altered_query_token.AlteredQueryToken)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("alteredHighlightedQueryString", self.altered_highlighted_query_string)
        writer.write_str_value("alteredQueryString", self.altered_query_string)
        writer.write_collection_of_object_values("alteredQueryTokens", self.altered_query_tokens)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

