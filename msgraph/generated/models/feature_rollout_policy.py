from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .directory_object import DirectoryObject
    from .entity import Entity
    from .staged_feature_name import StagedFeatureName

from .entity import Entity

@dataclass
class FeatureRolloutPolicy(Entity):
    # Nullable. Specifies a list of directoryObject resources that feature is enabled for.
    applies_to: Optional[List[DirectoryObject]] = None
    # A description for this feature rollout policy.
    description: Optional[str] = None
    # The display name for this  feature rollout policy.
    display_name: Optional[str] = None
    # The feature property
    feature: Optional[StagedFeatureName] = None
    # Indicates whether this feature rollout policy should be applied to the entire organization.
    is_applied_to_organization: Optional[bool] = None
    # Indicates whether the feature rollout is enabled.
    is_enabled: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FeatureRolloutPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FeatureRolloutPolicy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FeatureRolloutPolicy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .directory_object import DirectoryObject
        from .entity import Entity
        from .staged_feature_name import StagedFeatureName

        from .directory_object import DirectoryObject
        from .entity import Entity
        from .staged_feature_name import StagedFeatureName

        fields: Dict[str, Callable[[Any], None]] = {
            "appliesTo": lambda n : setattr(self, 'applies_to', n.get_collection_of_object_values(DirectoryObject)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "feature": lambda n : setattr(self, 'feature', n.get_enum_value(StagedFeatureName)),
            "isAppliedToOrganization": lambda n : setattr(self, 'is_applied_to_organization', n.get_bool_value()),
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
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
        writer.write_collection_of_object_values("appliesTo", self.applies_to)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("feature", self.feature)
        writer.write_bool_value("isAppliedToOrganization", self.is_applied_to_organization)
        writer.write_bool_value("isEnabled", self.is_enabled)
    

