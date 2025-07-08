from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.store import BackedModel, BackingStore, BackingStoreFactorySingleton
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......models.device_metadata import DeviceMetadata
    from ......models.integrated_application_metadata import IntegratedApplicationMetadata
    from ......models.policy_location import PolicyLocation
    from ......models.policy_pivot_property import PolicyPivotProperty
    from ......models.user_activity_types import UserActivityTypes

@dataclass
class ComputePostRequestBody(AdditionalDataHolder, BackedModel, Parsable):
    # Stores model information.
    backing_store: BackingStore = field(default_factory=BackingStoreFactorySingleton(backing_store_factory=None).backing_store_factory.create_backing_store, repr=False)

    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)
    # The activities property
    activities: Optional[UserActivityTypes] = None
    # The deviceMetadata property
    device_metadata: Optional[DeviceMetadata] = None
    # The integratedAppMetadata property
    integrated_app_metadata: Optional[IntegratedApplicationMetadata] = None
    # The locations property
    locations: Optional[list[PolicyLocation]] = None
    # The pivotOn property
    pivot_on: Optional[PolicyPivotProperty] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ComputePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ComputePostRequestBody
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ComputePostRequestBody()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ......models.device_metadata import DeviceMetadata
        from ......models.integrated_application_metadata import IntegratedApplicationMetadata
        from ......models.policy_location import PolicyLocation
        from ......models.policy_pivot_property import PolicyPivotProperty
        from ......models.user_activity_types import UserActivityTypes

        from ......models.device_metadata import DeviceMetadata
        from ......models.integrated_application_metadata import IntegratedApplicationMetadata
        from ......models.policy_location import PolicyLocation
        from ......models.policy_pivot_property import PolicyPivotProperty
        from ......models.user_activity_types import UserActivityTypes

        fields: dict[str, Callable[[Any], None]] = {
            "activities": lambda n : setattr(self, 'activities', n.get_collection_of_enum_values(UserActivityTypes)),
            "deviceMetadata": lambda n : setattr(self, 'device_metadata', n.get_object_value(DeviceMetadata)),
            "integratedAppMetadata": lambda n : setattr(self, 'integrated_app_metadata', n.get_object_value(IntegratedApplicationMetadata)),
            "locations": lambda n : setattr(self, 'locations', n.get_collection_of_object_values(PolicyLocation)),
            "pivotOn": lambda n : setattr(self, 'pivot_on', n.get_enum_value(PolicyPivotProperty)),
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
        writer.write_enum_value("activities", self.activities)
        writer.write_object_value("deviceMetadata", self.device_metadata)
        writer.write_object_value("integratedAppMetadata", self.integrated_app_metadata)
        writer.write_collection_of_object_values("locations", self.locations)
        writer.write_enum_value("pivotOn", self.pivot_on)
        writer.write_additional_data_value(self.additional_data)
    

