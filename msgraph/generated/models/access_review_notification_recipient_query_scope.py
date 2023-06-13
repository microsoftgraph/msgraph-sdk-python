from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_review_notification_recipient_scope

from . import access_review_notification_recipient_scope

@dataclass
class AccessReviewNotificationRecipientQueryScope(access_review_notification_recipient_scope.AccessReviewNotificationRecipientScope):
    odata_type = "#microsoft.graph.accessReviewNotificationRecipientQueryScope"
    # Represents the query for who the recipients are. For example, /groups/{group id}/members for group members and /users/{user id} for a specific user.
    query: Optional[str] = None
    # In the scenario where reviewers need to be specified dynamically, indicates the relative source of the query. This property is only required if a relative query (that is, ./manager) is specified.
    query_root: Optional[str] = None
    # Indicates the type of query. Allowed value is MicrosoftGraph.
    query_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewNotificationRecipientQueryScope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewNotificationRecipientQueryScope
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessReviewNotificationRecipientQueryScope()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_review_notification_recipient_scope

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
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("query", self.query)
        writer.write_str_value("queryRoot", self.query_root)
        writer.write_str_value("queryType", self.query_type)
    

