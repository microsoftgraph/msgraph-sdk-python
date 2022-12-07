from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

case_operation = lazy_import('msgraph.generated.models.security.case_operation')
ediscovery_review_set = lazy_import('msgraph.generated.models.security.ediscovery_review_set')
ediscovery_search = lazy_import('msgraph.generated.models.security.ediscovery_search')

class EdiscoveryAddToReviewSetOperation(case_operation.CaseOperation):
    def __init__(self,) -> None:
        """
        Instantiates a new EdiscoveryAddToReviewSetOperation and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # eDiscovery review set to which items matching source collection query gets added.
        self._review_set: Optional[ediscovery_review_set.EdiscoveryReviewSet] = None
        # eDiscovery search that gets added to review set.
        self._search: Optional[ediscovery_search.EdiscoverySearch] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryAddToReviewSetOperation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryAddToReviewSetOperation
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdiscoveryAddToReviewSetOperation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "review_set": lambda n : setattr(self, 'review_set', n.get_object_value(ediscovery_review_set.EdiscoveryReviewSet)),
            "search": lambda n : setattr(self, 'search', n.get_object_value(ediscovery_search.EdiscoverySearch)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def review_set(self,) -> Optional[ediscovery_review_set.EdiscoveryReviewSet]:
        """
        Gets the reviewSet property value. eDiscovery review set to which items matching source collection query gets added.
        Returns: Optional[ediscovery_review_set.EdiscoveryReviewSet]
        """
        return self._review_set
    
    @review_set.setter
    def review_set(self,value: Optional[ediscovery_review_set.EdiscoveryReviewSet] = None) -> None:
        """
        Sets the reviewSet property value. eDiscovery review set to which items matching source collection query gets added.
        Args:
            value: Value to set for the reviewSet property.
        """
        self._review_set = value
    
    @property
    def search(self,) -> Optional[ediscovery_search.EdiscoverySearch]:
        """
        Gets the search property value. eDiscovery search that gets added to review set.
        Returns: Optional[ediscovery_search.EdiscoverySearch]
        """
        return self._search
    
    @search.setter
    def search(self,value: Optional[ediscovery_search.EdiscoverySearch] = None) -> None:
        """
        Sets the search property value. eDiscovery search that gets added to review set.
        Args:
            value: Value to set for the search property.
        """
        self._search = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("reviewSet", self.review_set)
        writer.write_object_value("search", self.search)
    

