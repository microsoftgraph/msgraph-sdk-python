from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .inheritable_scopes import InheritableScopes

@dataclass
class InheritablePermission(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Inheritance configuration for delegated permission scopes published by the resource application. Supports three patterns: allAllowedScopes (inherit all available scopes), enumeratedScopes (inherit only the listed scopes), and noScopes (inherit none). Each pattern exposes a kind discriminator for filtering.
    inheritable_scopes: Optional[InheritableScopes] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The appId of the resource application that publishes these scopes. Primary key.
    resource_app_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InheritablePermission:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InheritablePermission
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InheritablePermission()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .inheritable_scopes import InheritableScopes

        from .inheritable_scopes import InheritableScopes

        fields: dict[str, Callable[[Any], None]] = {
            "inheritableScopes": lambda n : setattr(self, 'inheritable_scopes', n.get_object_value(InheritableScopes)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "resourceAppId": lambda n : setattr(self, 'resource_app_id', n.get_str_value()),
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
        writer.write_object_value("inheritableScopes", self.inheritable_scopes)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("resourceAppId", self.resource_app_id)
        writer.write_additional_data_value(self.additional_data)
    

