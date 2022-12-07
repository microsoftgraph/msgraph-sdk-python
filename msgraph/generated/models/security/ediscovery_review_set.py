from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

data_set = lazy_import('msgraph.generated.models.security.data_set')
ediscovery_review_set_query = lazy_import('msgraph.generated.models.security.ediscovery_review_set_query')

class EdiscoveryReviewSet(data_set.DataSet):
    def __init__(self,) -> None:
        """
        Instantiates a new EdiscoveryReviewSet and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.ediscoveryReviewSet"
        # Represents queries within the review set.
        self._queries: Optional[List[ediscovery_review_set_query.EdiscoveryReviewSetQuery]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryReviewSet:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryReviewSet
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdiscoveryReviewSet()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "queries": lambda n : setattr(self, 'queries', n.get_collection_of_object_values(ediscovery_review_set_query.EdiscoveryReviewSetQuery)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def queries(self,) -> Optional[List[ediscovery_review_set_query.EdiscoveryReviewSetQuery]]:
        """
        Gets the queries property value. Represents queries within the review set.
        Returns: Optional[List[ediscovery_review_set_query.EdiscoveryReviewSetQuery]]
        """
        return self._queries
    
    @queries.setter
    def queries(self,value: Optional[List[ediscovery_review_set_query.EdiscoveryReviewSetQuery]] = None) -> None:
        """
        Sets the queries property value. Represents queries within the review set.
        Args:
            value: Value to set for the queries property.
        """
        self._queries = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("queries", self.queries)
    

