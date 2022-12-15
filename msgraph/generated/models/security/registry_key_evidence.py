from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

alert_evidence = lazy_import('msgraph.generated.models.security.alert_evidence')

class RegistryKeyEvidence(alert_evidence.AlertEvidence):
    def __init__(self,) -> None:
        """
        Instantiates a new RegistryKeyEvidence and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Registry hive of the key that the recorded action was applied to.
        self._registry_hive: Optional[str] = None
        # Registry key that the recorded action was applied to.
        self._registry_key: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RegistryKeyEvidence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RegistryKeyEvidence
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RegistryKeyEvidence()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "registry_hive": lambda n : setattr(self, 'registry_hive', n.get_str_value()),
            "registry_key": lambda n : setattr(self, 'registry_key', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def registry_hive(self,) -> Optional[str]:
        """
        Gets the registryHive property value. Registry hive of the key that the recorded action was applied to.
        Returns: Optional[str]
        """
        return self._registry_hive
    
    @registry_hive.setter
    def registry_hive(self,value: Optional[str] = None) -> None:
        """
        Sets the registryHive property value. Registry hive of the key that the recorded action was applied to.
        Args:
            value: Value to set for the registryHive property.
        """
        self._registry_hive = value
    
    @property
    def registry_key(self,) -> Optional[str]:
        """
        Gets the registryKey property value. Registry key that the recorded action was applied to.
        Returns: Optional[str]
        """
        return self._registry_key
    
    @registry_key.setter
    def registry_key(self,value: Optional[str] = None) -> None:
        """
        Sets the registryKey property value. Registry key that the recorded action was applied to.
        Args:
            value: Value to set for the registryKey property.
        """
        self._registry_key = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("registryHive", self.registry_hive)
        writer.write_str_value("registryKey", self.registry_key)
    

