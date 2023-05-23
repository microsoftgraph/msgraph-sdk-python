from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import directory_definition, entity, synchronization_rule

from . import entity

class SynchronizationSchema(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new synchronizationSchema and sets the default values.
        """
        super().__init__()
        # The directories property
        self._directories: Optional[List[directory_definition.DirectoryDefinition]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The synchronizationRules property
        self._synchronization_rules: Optional[List[synchronization_rule.SynchronizationRule]] = None
        # The version property
        self._version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SynchronizationSchema:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SynchronizationSchema
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SynchronizationSchema()
    
    @property
    def directories(self,) -> Optional[List[directory_definition.DirectoryDefinition]]:
        """
        Gets the directories property value. The directories property
        Returns: Optional[List[directory_definition.DirectoryDefinition]]
        """
        return self._directories
    
    @directories.setter
    def directories(self,value: Optional[List[directory_definition.DirectoryDefinition]] = None) -> None:
        """
        Sets the directories property value. The directories property
        Args:
            value: Value to set for the directories property.
        """
        self._directories = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import directory_definition, entity, synchronization_rule

        fields: Dict[str, Callable[[Any], None]] = {
            "directories": lambda n : setattr(self, 'directories', n.get_collection_of_object_values(directory_definition.DirectoryDefinition)),
            "synchronizationRules": lambda n : setattr(self, 'synchronization_rules', n.get_collection_of_object_values(synchronization_rule.SynchronizationRule)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("directories", self.directories)
        writer.write_collection_of_object_values("synchronizationRules", self.synchronization_rules)
        writer.write_str_value("version", self.version)
    
    @property
    def synchronization_rules(self,) -> Optional[List[synchronization_rule.SynchronizationRule]]:
        """
        Gets the synchronizationRules property value. The synchronizationRules property
        Returns: Optional[List[synchronization_rule.SynchronizationRule]]
        """
        return self._synchronization_rules
    
    @synchronization_rules.setter
    def synchronization_rules(self,value: Optional[List[synchronization_rule.SynchronizationRule]] = None) -> None:
        """
        Sets the synchronizationRules property value. The synchronizationRules property
        Args:
            value: Value to set for the synchronization_rules property.
        """
        self._synchronization_rules = value
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. The version property
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. The version property
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

