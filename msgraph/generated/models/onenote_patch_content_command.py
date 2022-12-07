from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

onenote_patch_action_type = lazy_import('msgraph.generated.models.onenote_patch_action_type')
onenote_patch_insert_position = lazy_import('msgraph.generated.models.onenote_patch_insert_position')

class OnenotePatchContentCommand(AdditionalDataHolder, Parsable):
    @property
    def action(self,) -> Optional[onenote_patch_action_type.OnenotePatchActionType]:
        """
        Gets the action property value. The action property
        Returns: Optional[onenote_patch_action_type.OnenotePatchActionType]
        """
        return self._action
    
    @action.setter
    def action(self,value: Optional[onenote_patch_action_type.OnenotePatchActionType] = None) -> None:
        """
        Sets the action property value. The action property
        Args:
            value: Value to set for the action property.
        """
        self._action = value
    
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new onenotePatchContentCommand and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The action property
        self._action: Optional[onenote_patch_action_type.OnenotePatchActionType] = None
        # A string of well-formed HTML to add to the page, and any image or file binary data. If the content contains binary data, the request must be sent using the multipart/form-data content type with a 'Commands' part.
        self._content: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The location to add the supplied content, relative to the target element. The possible values are: after (default) or before.
        self._position: Optional[onenote_patch_insert_position.OnenotePatchInsertPosition] = None
        # The element to update. Must be the #<data-id> or the generated <id> of the element, or the body or title keyword.
        self._target: Optional[str] = None
    
    @property
    def content(self,) -> Optional[str]:
        """
        Gets the content property value. A string of well-formed HTML to add to the page, and any image or file binary data. If the content contains binary data, the request must be sent using the multipart/form-data content type with a 'Commands' part.
        Returns: Optional[str]
        """
        return self._content
    
    @content.setter
    def content(self,value: Optional[str] = None) -> None:
        """
        Sets the content property value. A string of well-formed HTML to add to the page, and any image or file binary data. If the content contains binary data, the request must be sent using the multipart/form-data content type with a 'Commands' part.
        Args:
            value: Value to set for the content property.
        """
        self._content = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnenotePatchContentCommand:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnenotePatchContentCommand
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnenotePatchContentCommand()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(onenote_patch_action_type.OnenotePatchActionType)),
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "position": lambda n : setattr(self, 'position', n.get_enum_value(onenote_patch_insert_position.OnenotePatchInsertPosition)),
            "target": lambda n : setattr(self, 'target', n.get_str_value()),
        }
        return fields
    
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
    def position(self,) -> Optional[onenote_patch_insert_position.OnenotePatchInsertPosition]:
        """
        Gets the position property value. The location to add the supplied content, relative to the target element. The possible values are: after (default) or before.
        Returns: Optional[onenote_patch_insert_position.OnenotePatchInsertPosition]
        """
        return self._position
    
    @position.setter
    def position(self,value: Optional[onenote_patch_insert_position.OnenotePatchInsertPosition] = None) -> None:
        """
        Sets the position property value. The location to add the supplied content, relative to the target element. The possible values are: after (default) or before.
        Args:
            value: Value to set for the position property.
        """
        self._position = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("action", self.action)
        writer.write_str_value("content", self.content)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("position", self.position)
        writer.write_str_value("target", self.target)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def target(self,) -> Optional[str]:
        """
        Gets the target property value. The element to update. Must be the #<data-id> or the generated <id> of the element, or the body or title keyword.
        Returns: Optional[str]
        """
        return self._target
    
    @target.setter
    def target(self,value: Optional[str] = None) -> None:
        """
        Sets the target property value. The element to update. Must be the #<data-id> or the generated <id> of the element, or the body or title keyword.
        Args:
            value: Value to set for the target property.
        """
        self._target = value
    

