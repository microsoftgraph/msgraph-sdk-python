from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_inactive_users_query_scope import AccessReviewInactiveUsersQueryScope
    from .access_review_scope import AccessReviewScope

from .access_review_scope import AccessReviewScope

@dataclass
class AccessReviewQueryScope(AccessReviewScope):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.accessReviewQueryScope"
    # The query representing what will be reviewed in an access review.
    query: Optional[str] = None
    # In the scenario where reviewers need to be specified dynamically, this property is used to indicate the relative source of the query. This property is only required if a relative query is specified. For example, ./manager.
    query_root: Optional[str] = None
    # Indicates the type of query. Types include MicrosoftGraph and ARM.
    query_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessReviewQueryScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewQueryScope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.accessReviewInactiveUsersQueryScope".casefold():
            from .access_review_inactive_users_query_scope import AccessReviewInactiveUsersQueryScope

            return AccessReviewInactiveUsersQueryScope()
        return AccessReviewQueryScope()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_inactive_users_query_scope import AccessReviewInactiveUsersQueryScope
        from .access_review_scope import AccessReviewScope

        from .access_review_inactive_users_query_scope import AccessReviewInactiveUsersQueryScope
        from .access_review_scope import AccessReviewScope

        fields: Dict[str, Callable[[Any], None]] = {
            "query": lambda n : setattr(self, 'query', n.get_str_value()),
            "queryRoot": lambda n : setattr(self, 'query_root', n.get_str_value()),
            "queryType": lambda n : setattr(self, 'query_type', n.get_str_value()),
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
        writer.write_str_value("query", self.query)
        writer.write_str_value("queryRoot", self.query_root)
        writer.write_str_value("queryType", self.query_type)
    

