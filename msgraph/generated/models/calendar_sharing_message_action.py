from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

calendar_sharing_action = lazy_import('msgraph.generated.models.calendar_sharing_action')
calendar_sharing_action_importance = lazy_import('msgraph.generated.models.calendar_sharing_action_importance')
calendar_sharing_action_type = lazy_import('msgraph.generated.models.calendar_sharing_action_type')

class CalendarSharingMessageAction(AdditionalDataHolder, Parsable):
    @property
    def action(self,) -> Optional[calendar_sharing_action.CalendarSharingAction]:
        """
        Gets the action property value. The action property
        Returns: Optional[calendar_sharing_action.CalendarSharingAction]
        """
        return self._action
    
    @action.setter
    def action(self,value: Optional[calendar_sharing_action.CalendarSharingAction] = None) -> None:
        """
        Sets the action property value. The action property
        Args:
            value: Value to set for the action property.
        """
        self._action = value
    
    @property
    def action_type(self,) -> Optional[calendar_sharing_action_type.CalendarSharingActionType]:
        """
        Gets the actionType property value. The actionType property
        Returns: Optional[calendar_sharing_action_type.CalendarSharingActionType]
        """
        return self._action_type
    
    @action_type.setter
    def action_type(self,value: Optional[calendar_sharing_action_type.CalendarSharingActionType] = None) -> None:
        """
        Sets the actionType property value. The actionType property
        Args:
            value: Value to set for the actionType property.
        """
        self._action_type = value
    
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
        Instantiates a new calendarSharingMessageAction and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The action property
        self._action: Optional[calendar_sharing_action.CalendarSharingAction] = None
        # The actionType property
        self._action_type: Optional[calendar_sharing_action_type.CalendarSharingActionType] = None
        # The importance property
        self._importance: Optional[calendar_sharing_action_importance.CalendarSharingActionImportance] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CalendarSharingMessageAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CalendarSharingMessageAction
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return CalendarSharingMessageAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(calendar_sharing_action.CalendarSharingAction)),
            "action_type": lambda n : setattr(self, 'action_type', n.get_enum_value(calendar_sharing_action_type.CalendarSharingActionType)),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(calendar_sharing_action_importance.CalendarSharingActionImportance)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
        }
        return fields
    
    @property
    def importance(self,) -> Optional[calendar_sharing_action_importance.CalendarSharingActionImportance]:
        """
        Gets the importance property value. The importance property
        Returns: Optional[calendar_sharing_action_importance.CalendarSharingActionImportance]
        """
        return self._importance
    
    @importance.setter
    def importance(self,value: Optional[calendar_sharing_action_importance.CalendarSharingActionImportance] = None) -> None:
        """
        Sets the importance property value. The importance property
        Args:
            value: Value to set for the importance property.
        """
        self._importance = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("action", self.action)
        writer.write_enum_value("actionType", self.action_type)
        writer.write_enum_value("importance", self.importance)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

