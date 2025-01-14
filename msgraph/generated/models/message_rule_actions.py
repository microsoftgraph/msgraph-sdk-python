from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .importance import Importance
    from .recipient import Recipient

@dataclass
class MessageRuleActions(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # A list of categories to be assigned to a message.
    assign_categories: Optional[list[str]] = None
    # The ID of a folder that a message is to be copied to.
    copy_to_folder: Optional[str] = None
    # Indicates whether a message should be moved to the Deleted Items folder.
    delete: Optional[bool] = None
    # The email addresses of the recipients to which a message should be forwarded as an attachment.
    forward_as_attachment_to: Optional[list[Recipient]] = None
    # The email addresses of the recipients to which a message should be forwarded.
    forward_to: Optional[list[Recipient]] = None
    # Indicates whether a message should be marked as read.
    mark_as_read: Optional[bool] = None
    # Sets the importance of the message, which can be: low, normal, high.
    mark_importance: Optional[Importance] = None
    # The ID of the folder that a message will be moved to.
    move_to_folder: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Indicates whether a message should be permanently deleted and not saved to the Deleted Items folder.
    permanent_delete: Optional[bool] = None
    # The email addresses to which a message should be redirected.
    redirect_to: Optional[list[Recipient]] = None
    # Indicates whether subsequent rules should be evaluated.
    stop_processing_rules: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MessageRuleActions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MessageRuleActions
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MessageRuleActions()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .importance import Importance
        from .recipient import Recipient

        from .importance import Importance
        from .recipient import Recipient

        fields: dict[str, Callable[[Any], None]] = {
            "assignCategories": lambda n : setattr(self, 'assign_categories', n.get_collection_of_primitive_values(str)),
            "copyToFolder": lambda n : setattr(self, 'copy_to_folder', n.get_str_value()),
            "delete": lambda n : setattr(self, 'delete', n.get_bool_value()),
            "forwardAsAttachmentTo": lambda n : setattr(self, 'forward_as_attachment_to', n.get_collection_of_object_values(Recipient)),
            "forwardTo": lambda n : setattr(self, 'forward_to', n.get_collection_of_object_values(Recipient)),
            "markAsRead": lambda n : setattr(self, 'mark_as_read', n.get_bool_value()),
            "markImportance": lambda n : setattr(self, 'mark_importance', n.get_enum_value(Importance)),
            "moveToFolder": lambda n : setattr(self, 'move_to_folder', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "permanentDelete": lambda n : setattr(self, 'permanent_delete', n.get_bool_value()),
            "redirectTo": lambda n : setattr(self, 'redirect_to', n.get_collection_of_object_values(Recipient)),
            "stopProcessingRules": lambda n : setattr(self, 'stop_processing_rules', n.get_bool_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_collection_of_primitive_values("assignCategories", self.assign_categories)
        writer.write_str_value("copyToFolder", self.copy_to_folder)
        writer.write_bool_value("delete", self.delete)
        writer.write_collection_of_object_values("forwardAsAttachmentTo", self.forward_as_attachment_to)
        writer.write_collection_of_object_values("forwardTo", self.forward_to)
        writer.write_bool_value("markAsRead", self.mark_as_read)
        writer.write_enum_value("markImportance", self.mark_importance)
        writer.write_str_value("moveToFolder", self.move_to_folder)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_bool_value("permanentDelete", self.permanent_delete)
        writer.write_collection_of_object_values("redirectTo", self.redirect_to)
        writer.write_bool_value("stopProcessingRules", self.stop_processing_rules)
        writer.write_additional_data_value(self.additional_data)
    

