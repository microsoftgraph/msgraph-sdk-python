from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .end_user_notification_preference import EndUserNotificationPreference
    from .end_user_notification_setting_type import EndUserNotificationSettingType
    from .no_training_notification_setting import NoTrainingNotificationSetting
    from .positive_reinforcement_notification import PositiveReinforcementNotification
    from .training_notification_setting import TrainingNotificationSetting

@dataclass
class EndUserNotificationSetting(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)
    # Notification preference. Possible values are: unknown, microsoft, custom, unknownFutureValue.
    notification_preference: Optional[EndUserNotificationPreference] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Positive reinforcement detail.
    positive_reinforcement: Optional[PositiveReinforcementNotification] = None
    # End user notification type. Possible values are: unknown, noTraining, trainingSelected, noNotification, unknownFutureValue.
    setting_type: Optional[EndUserNotificationSettingType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EndUserNotificationSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EndUserNotificationSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            mapping_value = parse_node.get_child_node("@odata.type").get_str_value()
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.noTrainingNotificationSetting".casefold():
            from .no_training_notification_setting import NoTrainingNotificationSetting

            return NoTrainingNotificationSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.trainingNotificationSetting".casefold():
            from .training_notification_setting import TrainingNotificationSetting

            return TrainingNotificationSetting()
        return EndUserNotificationSetting()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .end_user_notification_preference import EndUserNotificationPreference
        from .end_user_notification_setting_type import EndUserNotificationSettingType
        from .no_training_notification_setting import NoTrainingNotificationSetting
        from .positive_reinforcement_notification import PositiveReinforcementNotification
        from .training_notification_setting import TrainingNotificationSetting

        from .end_user_notification_preference import EndUserNotificationPreference
        from .end_user_notification_setting_type import EndUserNotificationSettingType
        from .no_training_notification_setting import NoTrainingNotificationSetting
        from .positive_reinforcement_notification import PositiveReinforcementNotification
        from .training_notification_setting import TrainingNotificationSetting

        fields: Dict[str, Callable[[Any], None]] = {
            "notificationPreference": lambda n : setattr(self, 'notification_preference', n.get_enum_value(EndUserNotificationPreference)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "positiveReinforcement": lambda n : setattr(self, 'positive_reinforcement', n.get_object_value(PositiveReinforcementNotification)),
            "settingType": lambda n : setattr(self, 'setting_type', n.get_enum_value(EndUserNotificationSettingType)),
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
        writer.write_enum_value("notificationPreference", self.notification_preference)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("positiveReinforcement", self.positive_reinforcement)
        writer.write_enum_value("settingType", self.setting_type)
        writer.write_additional_data_value(self.additional_data)
    

