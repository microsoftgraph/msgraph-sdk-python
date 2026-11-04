from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_custom_details import AlertCustomDetails
    from .alert_severity import AlertSeverity
    from .entity_mapping_configuration import EntityMappingConfiguration
    from .mitre_tactic import MitreTactic

@dataclass
class AlertTemplate(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Custom key-value detail pairs to include in the alert. Each value identifies the detection query column that supplies the corresponding custom detail.
    custom_details: Optional[AlertCustomDetails] = None
    # Description of the alert triggered by the custom detection rule.
    description: Optional[str] = None
    # The entityMappings property
    entity_mappings: Optional[EntityMappingConfiguration] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Recommended actions to mitigate the threat related to the alert triggered by the custom detection rule.
    recommended_actions: Optional[str] = None
    # The severity property
    severity: Optional[AlertSeverity] = None
    # The MITRE ATT&CK tactics framing for this alert.
    tactics: Optional[list[MitreTactic]] = None
    # Name of the alert triggered by the custom detection rule.
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AlertTemplate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AlertTemplate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AlertTemplate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_custom_details import AlertCustomDetails
        from .alert_severity import AlertSeverity
        from .entity_mapping_configuration import EntityMappingConfiguration
        from .mitre_tactic import MitreTactic

        from .alert_custom_details import AlertCustomDetails
        from .alert_severity import AlertSeverity
        from .entity_mapping_configuration import EntityMappingConfiguration
        from .mitre_tactic import MitreTactic

        fields: dict[str, Callable[[Any], None]] = {
            "customDetails": lambda n : setattr(self, 'custom_details', n.get_object_value(AlertCustomDetails)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "entityMappings": lambda n : setattr(self, 'entity_mappings', n.get_object_value(EntityMappingConfiguration)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "recommendedActions": lambda n : setattr(self, 'recommended_actions', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_enum_value(AlertSeverity)),
            "tactics": lambda n : setattr(self, 'tactics', n.get_collection_of_object_values(MitreTactic)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_object_value("customDetails", self.custom_details)
        writer.write_str_value("description", self.description)
        writer.write_object_value("entityMappings", self.entity_mappings)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("recommendedActions", self.recommended_actions)
        writer.write_enum_value("severity", self.severity)
        writer.write_collection_of_object_values("tactics", self.tactics)
        writer.write_str_value("title", self.title)
        writer.write_additional_data_value(self.additional_data)
    

