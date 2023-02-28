from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

on_premises_accidental_deletion_prevention = lazy_import('msgraph.generated.models.on_premises_accidental_deletion_prevention')

class OnPremisesDirectorySynchronizationConfiguration(AdditionalDataHolder, Parsable):
    @property
    def accidental_deletion_prevention(self,) -> Optional[on_premises_accidental_deletion_prevention.OnPremisesAccidentalDeletionPrevention]:
        """
        Gets the accidentalDeletionPrevention property value. Contains the accidental deletion prevention configuration for a tenant.
        Returns: Optional[on_premises_accidental_deletion_prevention.OnPremisesAccidentalDeletionPrevention]
        """
        return self._accidental_deletion_prevention
    
    @accidental_deletion_prevention.setter
    def accidental_deletion_prevention(self,value: Optional[on_premises_accidental_deletion_prevention.OnPremisesAccidentalDeletionPrevention] = None) -> None:
        """
        Sets the accidentalDeletionPrevention property value. Contains the accidental deletion prevention configuration for a tenant.
        Args:
            value: Value to set for the accidental_deletion_prevention property.
        """
        self._accidental_deletion_prevention = value
    
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
        Instantiates a new onPremisesDirectorySynchronizationConfiguration and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Contains the accidental deletion prevention configuration for a tenant.
        self._accidental_deletion_prevention: Optional[on_premises_accidental_deletion_prevention.OnPremisesAccidentalDeletionPrevention] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OnPremisesDirectorySynchronizationConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OnPremisesDirectorySynchronizationConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return OnPremisesDirectorySynchronizationConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "accidentalDeletionPrevention": lambda n : setattr(self, 'accidental_deletion_prevention', n.get_object_value(on_premises_accidental_deletion_prevention.OnPremisesAccidentalDeletionPrevention)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_object_value("accidentalDeletionPrevention", self.accidental_deletion_prevention)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

