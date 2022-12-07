from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class ManagedAppDiagnosticStatus(AdditionalDataHolder, Parsable):
    """
    Represents diagnostics status.
    """
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
        Instantiates a new managedAppDiagnosticStatus and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Instruction on how to mitigate a failed validation
        self._mitigation_instruction: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The state of the operation
        self._state: Optional[str] = None
        # The validation friendly name
        self._validation_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAppDiagnosticStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppDiagnosticStatus
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedAppDiagnosticStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "mitigation_instruction": lambda n : setattr(self, 'mitigation_instruction', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "validation_name": lambda n : setattr(self, 'validation_name', n.get_str_value()),
        }
        return fields
    
    @property
    def mitigation_instruction(self,) -> Optional[str]:
        """
        Gets the mitigationInstruction property value. Instruction on how to mitigate a failed validation
        Returns: Optional[str]
        """
        return self._mitigation_instruction
    
    @mitigation_instruction.setter
    def mitigation_instruction(self,value: Optional[str] = None) -> None:
        """
        Sets the mitigationInstruction property value. Instruction on how to mitigate a failed validation
        Args:
            value: Value to set for the mitigationInstruction property.
        """
        self._mitigation_instruction = value
    
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
        writer.write_str_value("mitigationInstruction", self.mitigation_instruction)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("state", self.state)
        writer.write_str_value("validationName", self.validation_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def state(self,) -> Optional[str]:
        """
        Gets the state property value. The state of the operation
        Returns: Optional[str]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[str] = None) -> None:
        """
        Sets the state property value. The state of the operation
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def validation_name(self,) -> Optional[str]:
        """
        Gets the validationName property value. The validation friendly name
        Returns: Optional[str]
        """
        return self._validation_name
    
    @validation_name.setter
    def validation_name(self,value: Optional[str] = None) -> None:
        """
        Sets the validationName property value. The validation friendly name
        Args:
            value: Value to set for the validationName property.
        """
        self._validation_name = value
    

