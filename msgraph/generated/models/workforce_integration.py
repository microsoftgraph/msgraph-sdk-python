from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .change_tracked_entity import ChangeTrackedEntity
    from .eligibility_filtering_enabled_entities import EligibilityFilteringEnabledEntities
    from .workforce_integration_encryption import WorkforceIntegrationEncryption
    from .workforce_integration_supported_entities import WorkforceIntegrationSupportedEntities

from .change_tracked_entity import ChangeTrackedEntity

@dataclass
class WorkforceIntegration(ChangeTrackedEntity, Parsable):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.workforceIntegration"
    # API version for the callback URL. Start with 1.
    api_version: Optional[int] = None
    # Name of the workforce integration.
    display_name: Optional[str] = None
    # Support to view eligibility-filtered results. The possible values are: none, swapRequest, offerShiftRequest, unknownFutureValue, timeOffReason. Use the Prefer: include-unknown-enum-members request header to get the following members in this evolvable enum: timeOffReason.
    eligibility_filtering_enabled_entities: Optional[EligibilityFilteringEnabledEntities] = None
    # The workforce integration encryption resource.
    encryption: Optional[WorkforceIntegrationEncryption] = None
    # Indicates whether this workforce integration is currently active and available.
    is_active: Optional[bool] = None
    # The Shifts entities supported for synchronous change notifications. Shifts call back to the provided URL when client changes occur to the entities specified in this property. By default, no entities are supported for change notifications. The possible values are: none, shift, swapRequest, userShiftPreferences, openShift, openShiftRequest, offerShiftRequest, unknownFutureValue, timeCard, timeOffReason, timeOff, timeOffRequest. Use the Prefer: include-unknown-enum-members request header to get the following values in this evolvable enum: timeCard , timeOffReason , timeOff , timeOffRequest.
    supported_entities: Optional[WorkforceIntegrationSupportedEntities] = None
    # Workforce Integration URL for callbacks from the Shifts service.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WorkforceIntegration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WorkforceIntegration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WorkforceIntegration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .change_tracked_entity import ChangeTrackedEntity
        from .eligibility_filtering_enabled_entities import EligibilityFilteringEnabledEntities
        from .workforce_integration_encryption import WorkforceIntegrationEncryption
        from .workforce_integration_supported_entities import WorkforceIntegrationSupportedEntities

        from .change_tracked_entity import ChangeTrackedEntity
        from .eligibility_filtering_enabled_entities import EligibilityFilteringEnabledEntities
        from .workforce_integration_encryption import WorkforceIntegrationEncryption
        from .workforce_integration_supported_entities import WorkforceIntegrationSupportedEntities

        fields: dict[str, Callable[[Any], None]] = {
            "apiVersion": lambda n : setattr(self, 'api_version', n.get_int_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "eligibilityFilteringEnabledEntities": lambda n : setattr(self, 'eligibility_filtering_enabled_entities', n.get_collection_of_enum_values(EligibilityFilteringEnabledEntities)),
            "encryption": lambda n : setattr(self, 'encryption', n.get_object_value(WorkforceIntegrationEncryption)),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "supportedEntities": lambda n : setattr(self, 'supported_entities', n.get_collection_of_enum_values(WorkforceIntegrationSupportedEntities)),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_int_value("apiVersion", self.api_version)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("eligibilityFilteringEnabledEntities", self.eligibility_filtering_enabled_entities)
        writer.write_object_value("encryption", self.encryption)
        writer.write_bool_value("isActive", self.is_active)
        writer.write_enum_value("supportedEntities", self.supported_entities)
        writer.write_str_value("url", self.url)
    

