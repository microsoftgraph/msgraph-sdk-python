from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .entity import Entity
    from .mail_search_folder import MailSearchFolder
    from .message import Message
    from .message_rule import MessageRule
    from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
    from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

from .entity import Entity

@dataclass
class MailFolder(Entity, Parsable):
    # The number of immediate child mailFolders in the current mailFolder.
    child_folder_count: Optional[int] = None
    # The collection of child folders in the mailFolder.
    child_folders: Optional[list[MailFolder]] = None
    # The mailFolder's display name.
    display_name: Optional[str] = None
    # Indicates whether the mailFolder is hidden. This property can be set only when creating the folder. Find more information in Hidden mail folders.
    is_hidden: Optional[bool] = None
    # The collection of rules that apply to the user's Inbox folder.
    message_rules: Optional[list[MessageRule]] = None
    # The collection of messages in the mailFolder.
    messages: Optional[list[Message]] = None
    # The collection of multi-value extended properties defined for the mailFolder. Read-only. Nullable.
    multi_value_extended_properties: Optional[list[MultiValueLegacyExtendedProperty]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The unique identifier for the mailFolder's parent mailFolder.
    parent_folder_id: Optional[str] = None
    # The collection of single-value extended properties defined for the mailFolder. Read-only. Nullable.
    single_value_extended_properties: Optional[list[SingleValueLegacyExtendedProperty]] = None
    # The number of items in the mailFolder.
    total_item_count: Optional[int] = None
    # The number of items in the mailFolder marked as unread.
    unread_item_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MailFolder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MailFolder
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.mailSearchFolder".casefold():
            from .mail_search_folder import MailSearchFolder

            return MailSearchFolder()
        return MailFolder()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .entity import Entity
        from .mail_search_folder import MailSearchFolder
        from .message import Message
        from .message_rule import MessageRule
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        from .entity import Entity
        from .mail_search_folder import MailSearchFolder
        from .message import Message
        from .message_rule import MessageRule
        from .multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
        from .single_value_legacy_extended_property import SingleValueLegacyExtendedProperty

        fields: dict[str, Callable[[Any], None]] = {
            "childFolderCount": lambda n : setattr(self, 'child_folder_count', n.get_int_value()),
            "childFolders": lambda n : setattr(self, 'child_folders', n.get_collection_of_object_values(MailFolder)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "isHidden": lambda n : setattr(self, 'is_hidden', n.get_bool_value()),
            "messageRules": lambda n : setattr(self, 'message_rules', n.get_collection_of_object_values(MessageRule)),
            "messages": lambda n : setattr(self, 'messages', n.get_collection_of_object_values(Message)),
            "multiValueExtendedProperties": lambda n : setattr(self, 'multi_value_extended_properties', n.get_collection_of_object_values(MultiValueLegacyExtendedProperty)),
            "parentFolderId": lambda n : setattr(self, 'parent_folder_id', n.get_str_value()),
            "singleValueExtendedProperties": lambda n : setattr(self, 'single_value_extended_properties', n.get_collection_of_object_values(SingleValueLegacyExtendedProperty)),
            "totalItemCount": lambda n : setattr(self, 'total_item_count', n.get_int_value()),
            "unreadItemCount": lambda n : setattr(self, 'unread_item_count', n.get_int_value()),
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
        writer.write_int_value("childFolderCount", self.child_folder_count)
        writer.write_collection_of_object_values("childFolders", self.child_folders)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("isHidden", self.is_hidden)
        writer.write_collection_of_object_values("messageRules", self.message_rules)
        writer.write_collection_of_object_values("messages", self.messages)
        writer.write_collection_of_object_values("multiValueExtendedProperties", self.multi_value_extended_properties)
        writer.write_str_value("parentFolderId", self.parent_folder_id)
        writer.write_collection_of_object_values("singleValueExtendedProperties", self.single_value_extended_properties)
        writer.write_int_value("totalItemCount", self.total_item_count)
        writer.write_int_value("unreadItemCount", self.unread_item_count)
    

