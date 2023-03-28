from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import on_premises_directory_synchronization_deletion_prevention_type

class OnPremisesAccidentalDeletionPrevention(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new onPremisesAccidentalDeletionPrevention and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Threshold value which triggers accidental deletion prevention. The threshold is either an absolute number of objects or a percentage number of objects.
        self._alert_threshold: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The status of the accidental deletion prevention feature. The possible values are: disabled, enabledForCount, enabledForPercentage, unknownFutureValue.
        self._synchronization_prevention_type: Optional[on_premises_directory_synchronization_deletion_prevention_type.OnPremisesDirectorySynchronizationDeletionPreventionType] = None
    
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
    def alert_threshold(self,) -> Optional[int]:
        """
        Gets the alertThreshold property value. Threshold value which triggers accidental deletion prevention. The threshold is either an absolute number of objects or a percentage number of objects.
        Returns: Optional[int]
        """
        return self._alert_threshold
    
    @alert_threshold.setter
    def alert_threshold(self,value: Optional[int] = None) -> None:
        """
        Sets the alertThreshold property value. Threshold value which triggers accidental deletion prevention. The threshold is either an absolute number of objects or a percentage number of objects.
        Args:
            value: Value to set for the alert_threshold property.
        """
        self._alert_threshold = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesAccidentalDeletionPrevention:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesAccidentalDeletionPrevention
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesAccidentalDeletionPrevention()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import on_premises_directory_synchronization_deletion_prevention_type

        fields: Dict[str, Callable[[Any], None]] = {
            "alertThreshold": lambda n : setattr(self, 'alert_threshold', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "synchronizationPreventionType": lambda n : setattr(self, 'synchronization_prevention_type', n.get_enum_value(on_premises_directory_synchronization_deletion_prevention_type.OnPremisesDirectorySynchronizationDeletionPreventionType)),
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
            value: Value to set for the odata_type property.
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
        writer.write_int_value("alertThreshold", self.alert_threshold)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("synchronizationPreventionType", self.synchronization_prevention_type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def synchronization_prevention_type(self,) -> Optional[on_premises_directory_synchronization_deletion_prevention_type.OnPremisesDirectorySynchronizationDeletionPreventionType]:
        """
        Gets the synchronizationPreventionType property value. The status of the accidental deletion prevention feature. The possible values are: disabled, enabledForCount, enabledForPercentage, unknownFutureValue.
        Returns: Optional[on_premises_directory_synchronization_deletion_prevention_type.OnPremisesDirectorySynchronizationDeletionPreventionType]
        """
        return self._synchronization_prevention_type
    
    @synchronization_prevention_type.setter
    def synchronization_prevention_type(self,value: Optional[on_premises_directory_synchronization_deletion_prevention_type.OnPremisesDirectorySynchronizationDeletionPreventionType] = None) -> None:
        """
        Sets the synchronizationPreventionType property value. The status of the accidental deletion prevention feature. The possible values are: disabled, enabledForCount, enabledForPercentage, unknownFutureValue.
        Args:
            value: Value to set for the synchronization_prevention_type property.
        """
        self._synchronization_prevention_type = value
    

