from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class AccessReviewReviewerScope(AdditionalDataHolder, Parsable):
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
        Instantiates a new accessReviewReviewerScope and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The OdataType property
        self._odata_type: Optional[str] = None
        # The query specifying who will be the reviewer.
        self._query: Optional[str] = None
        # In the scenario where reviewers need to be specified dynamically, this property is used to indicate the relative source of the query. This property is only required if a relative query, for example, ./manager, is specified. Possible value: decisions.
        self._query_root: Optional[str] = None
        # The type of query. Examples include MicrosoftGraph and ARM.
        self._query_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewReviewerScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewReviewerScope
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewReviewerScope()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "query": lambda n : setattr(self, 'query', n.get_str_value()),
            "query_root": lambda n : setattr(self, 'query_root', n.get_str_value()),
            "query_type": lambda n : setattr(self, 'query_type', n.get_str_value()),
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
    def query(self,) -> Optional[str]:
        """
        Gets the query property value. The query specifying who will be the reviewer.
        Returns: Optional[str]
        """
        return self._query
    
    @query.setter
    def query(self,value: Optional[str] = None) -> None:
        """
        Sets the query property value. The query specifying who will be the reviewer.
        Args:
            value: Value to set for the query property.
        """
        self._query = value
    
    @property
    def query_root(self,) -> Optional[str]:
        """
        Gets the queryRoot property value. In the scenario where reviewers need to be specified dynamically, this property is used to indicate the relative source of the query. This property is only required if a relative query, for example, ./manager, is specified. Possible value: decisions.
        Returns: Optional[str]
        """
        return self._query_root
    
    @query_root.setter
    def query_root(self,value: Optional[str] = None) -> None:
        """
        Sets the queryRoot property value. In the scenario where reviewers need to be specified dynamically, this property is used to indicate the relative source of the query. This property is only required if a relative query, for example, ./manager, is specified. Possible value: decisions.
        Args:
            value: Value to set for the queryRoot property.
        """
        self._query_root = value
    
    @property
    def query_type(self,) -> Optional[str]:
        """
        Gets the queryType property value. The type of query. Examples include MicrosoftGraph and ARM.
        Returns: Optional[str]
        """
        return self._query_type
    
    @query_type.setter
    def query_type(self,value: Optional[str] = None) -> None:
        """
        Sets the queryType property value. The type of query. Examples include MicrosoftGraph and ARM.
        Args:
            value: Value to set for the queryType property.
        """
        self._query_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("query", self.query)
        writer.write_str_value("queryRoot", self.query_root)
        writer.write_str_value("queryType", self.query_type)
        writer.write_additional_data_value(self.additional_data)
    

