from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

search_alteration = lazy_import('msgraph.generated.models.search_alteration')
search_alteration_type = lazy_import('msgraph.generated.models.search_alteration_type')

class AlterationResponse(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new alterationResponse and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # Defines the original user query string.
        self._original_query_string: Optional[str] = None
        # Defines the details of the alteration information for the spelling correction.
        self._query_alteration: Optional[search_alteration.SearchAlteration] = None
        # Defines the type of the spelling correction. Possible values are: suggestion, modification.
        self._query_alteration_type: Optional[search_alteration_type.SearchAlterationType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AlterationResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AlterationResponse
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AlterationResponse()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "original_query_string": lambda n : setattr(self, 'original_query_string', n.get_str_value()),
            "query_alteration": lambda n : setattr(self, 'query_alteration', n.get_object_value(search_alteration.SearchAlteration)),
            "query_alteration_type": lambda n : setattr(self, 'query_alteration_type', n.get_enum_value(search_alteration_type.SearchAlterationType)),
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
    
    @property
    def original_query_string(self,) -> Optional[str]:
        """
        Gets the originalQueryString property value. Defines the original user query string.
        Returns: Optional[str]
        """
        return self._original_query_string
    
    @original_query_string.setter
    def original_query_string(self,value: Optional[str] = None) -> None:
        """
        Sets the originalQueryString property value. Defines the original user query string.
        Args:
            value: Value to set for the originalQueryString property.
        """
        self._original_query_string = value
    
    @property
    def query_alteration(self,) -> Optional[search_alteration.SearchAlteration]:
        """
        Gets the queryAlteration property value. Defines the details of the alteration information for the spelling correction.
        Returns: Optional[search_alteration.SearchAlteration]
        """
        return self._query_alteration
    
    @query_alteration.setter
    def query_alteration(self,value: Optional[search_alteration.SearchAlteration] = None) -> None:
        """
        Sets the queryAlteration property value. Defines the details of the alteration information for the spelling correction.
        Args:
            value: Value to set for the queryAlteration property.
        """
        self._query_alteration = value
    
    @property
    def query_alteration_type(self,) -> Optional[search_alteration_type.SearchAlterationType]:
        """
        Gets the queryAlterationType property value. Defines the type of the spelling correction. Possible values are: suggestion, modification.
        Returns: Optional[search_alteration_type.SearchAlterationType]
        """
        return self._query_alteration_type
    
    @query_alteration_type.setter
    def query_alteration_type(self,value: Optional[search_alteration_type.SearchAlterationType] = None) -> None:
        """
        Sets the queryAlterationType property value. Defines the type of the spelling correction. Possible values are: suggestion, modification.
        Args:
            value: Value to set for the queryAlterationType property.
        """
        self._query_alteration_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("originalQueryString", self.original_query_string)
        writer.write_object_value("queryAlteration", self.query_alteration)
        writer.write_enum_value("queryAlterationType", self.query_alteration_type)
        writer.write_additional_data_value(self.additional_data)
    

