from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .workbook_comment_reply import WorkbookCommentReply

from .entity import Entity

@dataclass
class WorkbookComment(Entity, Parsable):
    # The content of the comment.
    content: Optional[str] = None
    # The content type of the comment.
    content_type: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The list of replies to the comment. Read-only. Nullable.
    replies: Optional[list[WorkbookCommentReply]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkbookComment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkbookComment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkbookComment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .workbook_comment_reply import WorkbookCommentReply

        from .entity import Entity
        from .workbook_comment_reply import WorkbookCommentReply

        fields: dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "contentType": lambda n : setattr(self, 'content_type', n.get_str_value()),
            "replies": lambda n : setattr(self, 'replies', n.get_collection_of_object_values(WorkbookCommentReply)),
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
        writer.write_str_value("content", self.content)
        writer.write_str_value("contentType", self.content_type)
        writer.write_collection_of_object_values("replies", self.replies)
    

