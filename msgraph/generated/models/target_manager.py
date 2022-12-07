from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

subject_set = lazy_import('msgraph.generated.models.subject_set')

class TargetManager(subject_set.SubjectSet):
    def __init__(self,) -> None:
        """
        Instantiates a new TargetManager and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.targetManager"
        # Manager level, between 1 and 4. The direct manager is 1.
        self._manager_level: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TargetManager:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TargetManager
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TargetManager()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "manager_level": lambda n : setattr(self, 'manager_level', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def manager_level(self,) -> Optional[int]:
        """
        Gets the managerLevel property value. Manager level, between 1 and 4. The direct manager is 1.
        Returns: Optional[int]
        """
        return self._manager_level
    
    @manager_level.setter
    def manager_level(self,value: Optional[int] = None) -> None:
        """
        Sets the managerLevel property value. Manager level, between 1 and 4. The direct manager is 1.
        Args:
            value: Value to set for the managerLevel property.
        """
        self._manager_level = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("managerLevel", self.manager_level)
    

