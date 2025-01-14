from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_package_resource_attribute_destination import AccessPackageResourceAttributeDestination
    from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

@dataclass
class AccessPackageResourceAttribute(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # Information about how to set the attribute, currently a accessPackageUserDirectoryAttributeStore type.
    destination: Optional[AccessPackageResourceAttributeDestination] = None
    # The isEditable property
    is_editable: Optional[bool] = None
    # The isPersistedOnAssignmentRemoval property
    is_persisted_on_assignment_removal: Optional[bool] = None
    # The name of the attribute in the end system. If the destination is accessPackageUserDirectoryAttributeStore, then a user property such as jobTitle or a directory schema extension for the user object type, such as extension2b676109c7c74ae2b41549205f1947edpersonalTitle.
    name: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # Information about how to populate the attribute value when an accessPackageAssignmentRequest is being fulfilled, currently a accessPackageResourceAttributeQuestion type.
    source: Optional[AccessPackageResourceAttributeSource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccessPackageResourceAttribute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageResourceAttribute
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccessPackageResourceAttribute()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .access_package_resource_attribute_destination import AccessPackageResourceAttributeDestination
        from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

        from .access_package_resource_attribute_destination import AccessPackageResourceAttributeDestination
        from .access_package_resource_attribute_source import AccessPackageResourceAttributeSource

        fields: dict[str, Callable[[Any], None]] = {
            "destination": lambda n : setattr(self, 'destination', n.get_object_value(AccessPackageResourceAttributeDestination)),
            "isEditable": lambda n : setattr(self, 'is_editable', n.get_bool_value()),
            "isPersistedOnAssignmentRemoval": lambda n : setattr(self, 'is_persisted_on_assignment_removal', n.get_bool_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "source": lambda n : setattr(self, 'source', n.get_object_value(AccessPackageResourceAttributeSource)),
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
        writer.write_object_value("destination", self.destination)
        writer.write_bool_value("isEditable", self.is_editable)
        writer.write_bool_value("isPersistedOnAssignmentRemoval", self.is_persisted_on_assignment_removal)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("source", self.source)
        writer.write_additional_data_value(self.additional_data)
    

