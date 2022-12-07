from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

directory_object = lazy_import('msgraph.generated.models.directory_object')
entity = lazy_import('msgraph.generated.models.entity')
staged_feature_name = lazy_import('msgraph.generated.models.staged_feature_name')

class FeatureRolloutPolicy(entity.Entity):
    """
    Provides operations to manage the admin singleton.
    """
    @property
    def applies_to(self,) -> Optional[List[directory_object.DirectoryObject]]:
        """
        Gets the appliesTo property value. Nullable. Specifies a list of directoryObjects that feature is enabled for.
        Returns: Optional[List[directory_object.DirectoryObject]]
        """
        return self._applies_to
    
    @applies_to.setter
    def applies_to(self,value: Optional[List[directory_object.DirectoryObject]] = None) -> None:
        """
        Sets the appliesTo property value. Nullable. Specifies a list of directoryObjects that feature is enabled for.
        Args:
            value: Value to set for the appliesTo property.
        """
        self._applies_to = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new featureRolloutPolicy and sets the default values.
        """
        super().__init__()
        # Nullable. Specifies a list of directoryObjects that feature is enabled for.
        self._applies_to: Optional[List[directory_object.DirectoryObject]] = None
        # A description for this feature rollout policy.
        self._description: Optional[str] = None
        # The display name for this  feature rollout policy.
        self._display_name: Optional[str] = None
        # The feature property
        self._feature: Optional[staged_feature_name.StagedFeatureName] = None
        # Indicates whether this feature rollout policy should be applied to the entire organization.
        self._is_applied_to_organization: Optional[bool] = None
        # Indicates whether the feature rollout is enabled.
        self._is_enabled: Optional[bool] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FeatureRolloutPolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: FeatureRolloutPolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return FeatureRolloutPolicy()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. A description for this feature rollout policy.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. A description for this feature rollout policy.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for this  feature rollout policy.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for this  feature rollout policy.
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    @property
    def feature(self,) -> Optional[staged_feature_name.StagedFeatureName]:
        """
        Gets the feature property value. The feature property
        Returns: Optional[staged_feature_name.StagedFeatureName]
        """
        return self._feature
    
    @feature.setter
    def feature(self,value: Optional[staged_feature_name.StagedFeatureName] = None) -> None:
        """
        Sets the feature property value. The feature property
        Args:
            value: Value to set for the feature property.
        """
        self._feature = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "applies_to": lambda n : setattr(self, 'applies_to', n.get_collection_of_object_values(directory_object.DirectoryObject)),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "feature": lambda n : setattr(self, 'feature', n.get_enum_value(staged_feature_name.StagedFeatureName)),
            "is_applied_to_organization": lambda n : setattr(self, 'is_applied_to_organization', n.get_bool_value()),
            "is_enabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def is_applied_to_organization(self,) -> Optional[bool]:
        """
        Gets the isAppliedToOrganization property value. Indicates whether this feature rollout policy should be applied to the entire organization.
        Returns: Optional[bool]
        """
        return self._is_applied_to_organization
    
    @is_applied_to_organization.setter
    def is_applied_to_organization(self,value: Optional[bool] = None) -> None:
        """
        Sets the isAppliedToOrganization property value. Indicates whether this feature rollout policy should be applied to the entire organization.
        Args:
            value: Value to set for the isAppliedToOrganization property.
        """
        self._is_applied_to_organization = value
    
    @property
    def is_enabled(self,) -> Optional[bool]:
        """
        Gets the isEnabled property value. Indicates whether the feature rollout is enabled.
        Returns: Optional[bool]
        """
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEnabled property value. Indicates whether the feature rollout is enabled.
        Args:
            value: Value to set for the isEnabled property.
        """
        self._is_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("appliesTo", self.applies_to)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("feature", self.feature)
        writer.write_bool_value("isAppliedToOrganization", self.is_applied_to_organization)
        writer.write_bool_value("isEnabled", self.is_enabled)
    

