from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

access_review_scope = lazy_import('msgraph.generated.models.access_review_scope')

class AccessReviewQueryScope(access_review_scope.AccessReviewScope):
    def __init__(self,) -> None:
        """
        Instantiates a new AccessReviewQueryScope and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.accessReviewQueryScope"
        # The query representing what will be reviewed in an access review.
        self._query: Optional[str] = None
        # In the scenario where reviewers need to be specified dynamically, this property is used to indicate the relative source of the query. This property is only required if a relative query is specified. For example, ./manager.
        self._query_root: Optional[str] = None
        # Indicates the type of query. Types include MicrosoftGraph and ARM.
        self._query_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewQueryScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewQueryScope
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewQueryScope()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "query": lambda n : setattr(self, 'query', n.get_str_value()),
            "query_root": lambda n : setattr(self, 'query_root', n.get_str_value()),
            "query_type": lambda n : setattr(self, 'query_type', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def query(self,) -> Optional[str]:
        """
        Gets the query property value. The query representing what will be reviewed in an access review.
        Returns: Optional[str]
        """
        return self._query
    
    @query.setter
    def query(self,value: Optional[str] = None) -> None:
        """
        Sets the query property value. The query representing what will be reviewed in an access review.
        Args:
            value: Value to set for the query property.
        """
        self._query = value
    
    @property
    def query_root(self,) -> Optional[str]:
        """
        Gets the queryRoot property value. In the scenario where reviewers need to be specified dynamically, this property is used to indicate the relative source of the query. This property is only required if a relative query is specified. For example, ./manager.
        Returns: Optional[str]
        """
        return self._query_root
    
    @query_root.setter
    def query_root(self,value: Optional[str] = None) -> None:
        """
        Sets the queryRoot property value. In the scenario where reviewers need to be specified dynamically, this property is used to indicate the relative source of the query. This property is only required if a relative query is specified. For example, ./manager.
        Args:
            value: Value to set for the queryRoot property.
        """
        self._query_root = value
    
    @property
    def query_type(self,) -> Optional[str]:
        """
        Gets the queryType property value. Indicates the type of query. Types include MicrosoftGraph and ARM.
        Returns: Optional[str]
        """
        return self._query_type
    
    @query_type.setter
    def query_type(self,value: Optional[str] = None) -> None:
        """
        Sets the queryType property value. Indicates the type of query. Types include MicrosoftGraph and ARM.
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
        super().serialize(writer)
        writer.write_str_value("query", self.query)
        writer.write_str_value("queryRoot", self.query_root)
        writer.write_str_value("queryType", self.query_type)
    

