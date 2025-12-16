from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_training_setting import CustomTrainingSetting
    from .microsoft_custom_training_setting import MicrosoftCustomTrainingSetting
    from .microsoft_managed_training_setting import MicrosoftManagedTrainingSetting
    from .microsoft_training_assignment_mapping import MicrosoftTrainingAssignmentMapping
    from .no_training_setting import NoTrainingSetting
    from .training_setting_type import TrainingSettingType

@dataclass
class TrainingSetting(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The OdataType property
    odata_type: Optional[str] = None
    # Type of setting. The possible values are: microsoftCustom, microsoftManaged, noTraining, custom, unknownFutureValue.
    setting_type: Optional[TrainingSettingType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TrainingSetting:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TrainingSetting
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("@odata.type")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.customTrainingSetting".casefold():
            from .custom_training_setting import CustomTrainingSetting

            return CustomTrainingSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftCustomTrainingSetting".casefold():
            from .microsoft_custom_training_setting import MicrosoftCustomTrainingSetting

            return MicrosoftCustomTrainingSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftManagedTrainingSetting".casefold():
            from .microsoft_managed_training_setting import MicrosoftManagedTrainingSetting

            return MicrosoftManagedTrainingSetting()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.microsoftTrainingAssignmentMapping".casefold():
            from .microsoft_training_assignment_mapping import MicrosoftTrainingAssignmentMapping

            return MicrosoftTrainingAssignmentMapping()
        if mapping_value and mapping_value.casefold() == "#microsoft.graph.noTrainingSetting".casefold():
            from .no_training_setting import NoTrainingSetting

            return NoTrainingSetting()
        return TrainingSetting()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .custom_training_setting import CustomTrainingSetting
        from .microsoft_custom_training_setting import MicrosoftCustomTrainingSetting
        from .microsoft_managed_training_setting import MicrosoftManagedTrainingSetting
        from .microsoft_training_assignment_mapping import MicrosoftTrainingAssignmentMapping
        from .no_training_setting import NoTrainingSetting
        from .training_setting_type import TrainingSettingType

        from .custom_training_setting import CustomTrainingSetting
        from .microsoft_custom_training_setting import MicrosoftCustomTrainingSetting
        from .microsoft_managed_training_setting import MicrosoftManagedTrainingSetting
        from .microsoft_training_assignment_mapping import MicrosoftTrainingAssignmentMapping
        from .no_training_setting import NoTrainingSetting
        from .training_setting_type import TrainingSettingType

        fields: dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "settingType": lambda n : setattr(self, 'setting_type', n.get_enum_value(TrainingSettingType)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("settingType", self.setting_type)
        writer.write_additional_data_value(self.additional_data)
    

