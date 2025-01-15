from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .calendar_sharing_action import CalendarSharingAction
    from .calendar_sharing_action_importance import CalendarSharingActionImportance
    from .calendar_sharing_action_type import CalendarSharingActionType

@dataclass
class CalendarSharingMessageAction(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The action property
    action: Optional[CalendarSharingAction] = None
    # The actionType property
    action_type: Optional[CalendarSharingActionType] = None
    # The importance property
    importance: Optional[CalendarSharingActionImportance] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CalendarSharingMessageAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CalendarSharingMessageAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CalendarSharingMessageAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .calendar_sharing_action import CalendarSharingAction
        from .calendar_sharing_action_importance import CalendarSharingActionImportance
        from .calendar_sharing_action_type import CalendarSharingActionType

        from .calendar_sharing_action import CalendarSharingAction
        from .calendar_sharing_action_importance import CalendarSharingActionImportance
        from .calendar_sharing_action_type import CalendarSharingActionType

        fields: dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(CalendarSharingAction)),
            "actionType": lambda n : setattr(self, 'action_type', n.get_enum_value(CalendarSharingActionType)),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(CalendarSharingActionImportance)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("action", self.action)
        writer.write_enum_value("actionType", self.action_type)
        writer.write_enum_value("importance", self.importance)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

