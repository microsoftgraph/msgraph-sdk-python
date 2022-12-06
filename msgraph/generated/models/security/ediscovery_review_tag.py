from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

child_selectability = lazy_import('msgraph.generated.models.security.child_selectability')
tag = lazy_import('msgraph.generated.models.security.tag')

class EdiscoveryReviewTag(tag.Tag):
    @property
    def child_selectability(self,) -> Optional[child_selectability.ChildSelectability]:
        """
        Gets the childSelectability property value. Indicates whether a single or multiple child tags can be associated with a document. Possible values are: One, Many.  This value controls whether the UX presents the tags as checkboxes or a radio button group.
        Returns: Optional[child_selectability.ChildSelectability]
        """
        return self._child_selectability
    
    @child_selectability.setter
    def child_selectability(self,value: Optional[child_selectability.ChildSelectability] = None) -> None:
        """
        Sets the childSelectability property value. Indicates whether a single or multiple child tags can be associated with a document. Possible values are: One, Many.  This value controls whether the UX presents the tags as checkboxes or a radio button group.
        Args:
            value: Value to set for the childSelectability property.
        """
        self._child_selectability = value
    
    @property
    def child_tags(self,) -> Optional[List[ediscovery_review_tag.EdiscoveryReviewTag]]:
        """
        Gets the childTags property value. Returns the tags that are a child of a tag.
        Returns: Optional[List[ediscovery_review_tag.EdiscoveryReviewTag]]
        """
        return self._child_tags
    
    @child_tags.setter
    def child_tags(self,value: Optional[List[ediscovery_review_tag.EdiscoveryReviewTag]] = None) -> None:
        """
        Sets the childTags property value. Returns the tags that are a child of a tag.
        Args:
            value: Value to set for the childTags property.
        """
        self._child_tags = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new EdiscoveryReviewTag and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.security.ediscoveryReviewTag"
        # Indicates whether a single or multiple child tags can be associated with a document. Possible values are: One, Many.  This value controls whether the UX presents the tags as checkboxes or a radio button group.
        self._child_selectability: Optional[child_selectability.ChildSelectability] = None
        # Returns the tags that are a child of a tag.
        self._child_tags: Optional[List[ediscovery_review_tag.EdiscoveryReviewTag]] = None
        # Returns the parent tag of the specified tag.
        self._parent: Optional[ediscovery_review_tag.EdiscoveryReviewTag] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EdiscoveryReviewTag:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EdiscoveryReviewTag
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return EdiscoveryReviewTag()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "child_selectability": lambda n : setattr(self, 'child_selectability', n.get_enum_value(child_selectability.ChildSelectability)),
            "child_tags": lambda n : setattr(self, 'child_tags', n.get_collection_of_object_values(ediscovery_review_tag.EdiscoveryReviewTag)),
            "parent": lambda n : setattr(self, 'parent', n.get_object_value(ediscovery_review_tag.EdiscoveryReviewTag)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def parent(self,) -> Optional[ediscovery_review_tag.EdiscoveryReviewTag]:
        """
        Gets the parent property value. Returns the parent tag of the specified tag.
        Returns: Optional[ediscovery_review_tag.EdiscoveryReviewTag]
        """
        return self._parent
    
    @parent.setter
    def parent(self,value: Optional[ediscovery_review_tag.EdiscoveryReviewTag] = None) -> None:
        """
        Sets the parent property value. Returns the parent tag of the specified tag.
        Args:
            value: Value to set for the parent property.
        """
        self._parent = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("childSelectability", self.child_selectability)
        writer.write_collection_of_object_values("childTags", self.child_tags)
        writer.write_object_value("parent", self.parent)
    

