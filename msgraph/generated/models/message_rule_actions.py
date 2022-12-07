from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

importance = lazy_import('msgraph.generated.models.importance')
recipient = lazy_import('msgraph.generated.models.recipient')

class MessageRuleActions(AdditionalDataHolder, Parsable):
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
    
    @property
    def assign_categories(self,) -> Optional[List[str]]:
        """
        Gets the assignCategories property value. A list of categories to be assigned to a message.
        Returns: Optional[List[str]]
        """
        return self._assign_categories
    
    @assign_categories.setter
    def assign_categories(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the assignCategories property value. A list of categories to be assigned to a message.
        Args:
            value: Value to set for the assignCategories property.
        """
        self._assign_categories = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new messageRuleActions and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A list of categories to be assigned to a message.
        self._assign_categories: Optional[List[str]] = None
        # The ID of a folder that a message is to be copied to.
        self._copy_to_folder: Optional[str] = None
        # Indicates whether a message should be moved to the Deleted Items folder.
        self._delete: Optional[bool] = None
        # The email addresses of the recipients to which a message should be forwarded as an attachment.
        self._forward_as_attachment_to: Optional[List[recipient.Recipient]] = None
        # The email addresses of the recipients to which a message should be forwarded.
        self._forward_to: Optional[List[recipient.Recipient]] = None
        # Indicates whether a message should be marked as read.
        self._mark_as_read: Optional[bool] = None
        # Sets the importance of the message, which can be: low, normal, high.
        self._mark_importance: Optional[importance.Importance] = None
        # The ID of the folder that a message will be moved to.
        self._move_to_folder: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Indicates whether a message should be permanently deleted and not saved to the Deleted Items folder.
        self._permanent_delete: Optional[bool] = None
        # The email addresses to which a message should be redirected.
        self._redirect_to: Optional[List[recipient.Recipient]] = None
        # Indicates whether subsequent rules should be evaluated.
        self._stop_processing_rules: Optional[bool] = None
    
    @property
    def copy_to_folder(self,) -> Optional[str]:
        """
        Gets the copyToFolder property value. The ID of a folder that a message is to be copied to.
        Returns: Optional[str]
        """
        return self._copy_to_folder
    
    @copy_to_folder.setter
    def copy_to_folder(self,value: Optional[str] = None) -> None:
        """
        Sets the copyToFolder property value. The ID of a folder that a message is to be copied to.
        Args:
            value: Value to set for the copyToFolder property.
        """
        self._copy_to_folder = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> MessageRuleActions:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: MessageRuleActions
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return MessageRuleActions()
    
    @property
    def delete(self,) -> Optional[bool]:
        """
        Gets the delete property value. Indicates whether a message should be moved to the Deleted Items folder.
        Returns: Optional[bool]
        """
        return self._delete
    
    @delete.setter
    def delete(self,value: Optional[bool] = None) -> None:
        """
        Sets the delete property value. Indicates whether a message should be moved to the Deleted Items folder.
        Args:
            value: Value to set for the delete property.
        """
        self._delete = value
    
    @property
    def forward_as_attachment_to(self,) -> Optional[List[recipient.Recipient]]:
        """
        Gets the forwardAsAttachmentTo property value. The email addresses of the recipients to which a message should be forwarded as an attachment.
        Returns: Optional[List[recipient.Recipient]]
        """
        return self._forward_as_attachment_to
    
    @forward_as_attachment_to.setter
    def forward_as_attachment_to(self,value: Optional[List[recipient.Recipient]] = None) -> None:
        """
        Sets the forwardAsAttachmentTo property value. The email addresses of the recipients to which a message should be forwarded as an attachment.
        Args:
            value: Value to set for the forwardAsAttachmentTo property.
        """
        self._forward_as_attachment_to = value
    
    @property
    def forward_to(self,) -> Optional[List[recipient.Recipient]]:
        """
        Gets the forwardTo property value. The email addresses of the recipients to which a message should be forwarded.
        Returns: Optional[List[recipient.Recipient]]
        """
        return self._forward_to
    
    @forward_to.setter
    def forward_to(self,value: Optional[List[recipient.Recipient]] = None) -> None:
        """
        Sets the forwardTo property value. The email addresses of the recipients to which a message should be forwarded.
        Args:
            value: Value to set for the forwardTo property.
        """
        self._forward_to = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "assign_categories": lambda n : setattr(self, 'assign_categories', n.get_collection_of_primitive_values(str)),
            "copy_to_folder": lambda n : setattr(self, 'copy_to_folder', n.get_str_value()),
            "delete": lambda n : setattr(self, 'delete', n.get_bool_value()),
            "forward_as_attachment_to": lambda n : setattr(self, 'forward_as_attachment_to', n.get_collection_of_object_values(recipient.Recipient)),
            "forward_to": lambda n : setattr(self, 'forward_to', n.get_collection_of_object_values(recipient.Recipient)),
            "mark_as_read": lambda n : setattr(self, 'mark_as_read', n.get_bool_value()),
            "mark_importance": lambda n : setattr(self, 'mark_importance', n.get_enum_value(importance.Importance)),
            "move_to_folder": lambda n : setattr(self, 'move_to_folder', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "permanent_delete": lambda n : setattr(self, 'permanent_delete', n.get_bool_value()),
            "redirect_to": lambda n : setattr(self, 'redirect_to', n.get_collection_of_object_values(recipient.Recipient)),
            "stop_processing_rules": lambda n : setattr(self, 'stop_processing_rules', n.get_bool_value()),
        }
        return fields
    
    @property
    def mark_as_read(self,) -> Optional[bool]:
        """
        Gets the markAsRead property value. Indicates whether a message should be marked as read.
        Returns: Optional[bool]
        """
        return self._mark_as_read
    
    @mark_as_read.setter
    def mark_as_read(self,value: Optional[bool] = None) -> None:
        """
        Sets the markAsRead property value. Indicates whether a message should be marked as read.
        Args:
            value: Value to set for the markAsRead property.
        """
        self._mark_as_read = value
    
    @property
    def mark_importance(self,) -> Optional[importance.Importance]:
        """
        Gets the markImportance property value. Sets the importance of the message, which can be: low, normal, high.
        Returns: Optional[importance.Importance]
        """
        return self._mark_importance
    
    @mark_importance.setter
    def mark_importance(self,value: Optional[importance.Importance] = None) -> None:
        """
        Sets the markImportance property value. Sets the importance of the message, which can be: low, normal, high.
        Args:
            value: Value to set for the markImportance property.
        """
        self._mark_importance = value
    
    @property
    def move_to_folder(self,) -> Optional[str]:
        """
        Gets the moveToFolder property value. The ID of the folder that a message will be moved to.
        Returns: Optional[str]
        """
        return self._move_to_folder
    
    @move_to_folder.setter
    def move_to_folder(self,value: Optional[str] = None) -> None:
        """
        Sets the moveToFolder property value. The ID of the folder that a message will be moved to.
        Args:
            value: Value to set for the moveToFolder property.
        """
        self._move_to_folder = value
    
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
    def permanent_delete(self,) -> Optional[bool]:
        """
        Gets the permanentDelete property value. Indicates whether a message should be permanently deleted and not saved to the Deleted Items folder.
        Returns: Optional[bool]
        """
        return self._permanent_delete
    
    @permanent_delete.setter
    def permanent_delete(self,value: Optional[bool] = None) -> None:
        """
        Sets the permanentDelete property value. Indicates whether a message should be permanently deleted and not saved to the Deleted Items folder.
        Args:
            value: Value to set for the permanentDelete property.
        """
        self._permanent_delete = value
    
    @property
    def redirect_to(self,) -> Optional[List[recipient.Recipient]]:
        """
        Gets the redirectTo property value. The email addresses to which a message should be redirected.
        Returns: Optional[List[recipient.Recipient]]
        """
        return self._redirect_to
    
    @redirect_to.setter
    def redirect_to(self,value: Optional[List[recipient.Recipient]] = None) -> None:
        """
        Sets the redirectTo property value. The email addresses to which a message should be redirected.
        Args:
            value: Value to set for the redirectTo property.
        """
        self._redirect_to = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
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
    
    @property
    def stop_processing_rules(self,) -> Optional[bool]:
        """
        Gets the stopProcessingRules property value. Indicates whether subsequent rules should be evaluated.
        Returns: Optional[bool]
        """
        return self._stop_processing_rules
    
    @stop_processing_rules.setter
    def stop_processing_rules(self,value: Optional[bool] = None) -> None:
        """
        Sets the stopProcessingRules property value. Indicates whether subsequent rules should be evaluated.
        Args:
            value: Value to set for the stopProcessingRules property.
        """
        self._stop_processing_rules = value
    

