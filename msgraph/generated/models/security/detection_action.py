from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert_template import AlertTemplate
    from .automated_action_set import AutomatedActionSet
    from .organizational_scope import OrganizationalScope

@dataclass
class DetectionAction(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The alertTemplate property
    alert_template: Optional[AlertTemplate] = None
    # The set of automated actions to run against entities that match the detection.
    automated_actions: Optional[AutomatedActionSet] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The set of groups (for example, device groups) to which the parent custom detection rule applies.
    organizational_scope: Optional[OrganizationalScope] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DetectionAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DetectionAction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DetectionAction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert_template import AlertTemplate
        from .automated_action_set import AutomatedActionSet
        from .organizational_scope import OrganizationalScope

        from .alert_template import AlertTemplate
        from .automated_action_set import AutomatedActionSet
        from .organizational_scope import OrganizationalScope

        fields: dict[str, Callable[[Any], None]] = {
            "alertTemplate": lambda n : setattr(self, 'alert_template', n.get_object_value(AlertTemplate)),
            "automatedActions": lambda n : setattr(self, 'automated_actions', n.get_object_value(AutomatedActionSet)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "organizationalScope": lambda n : setattr(self, 'organizational_scope', n.get_object_value(OrganizationalScope)),
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
        writer.write_object_value("alertTemplate", self.alert_template)
        writer.write_object_value("automatedActions", self.automated_actions)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("organizationalScope", self.organizational_scope)
        writer.write_additional_data_value(self.additional_data)
    

