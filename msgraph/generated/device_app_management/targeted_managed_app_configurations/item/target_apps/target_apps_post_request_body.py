from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

managed_mobile_app = lazy_import('msgraph.generated.models.managed_mobile_app')
targeted_managed_app_group_type = lazy_import('msgraph.generated.models.targeted_managed_app_group_type')

class TargetAppsPostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the targetApps method.
    """
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def app_group_type(self,) -> Optional[targeted_managed_app_group_type.TargetedManagedAppGroupType]:
        """
        Gets the appGroupType property value. The appGroupType property
        Returns: Optional[targeted_managed_app_group_type.TargetedManagedAppGroupType]
        """
        return self._app_group_type
    
    @app_group_type.setter
    def app_group_type(self,value: Optional[targeted_managed_app_group_type.TargetedManagedAppGroupType] = None) -> None:
        """
        Sets the appGroupType property value. The appGroupType property
        Args:
            value: Value to set for the appGroupType property.
        """
        self._app_group_type = value
    
    @property
    def apps(self,) -> Optional[List[managed_mobile_app.ManagedMobileApp]]:
        """
        Gets the apps property value. The apps property
        Returns: Optional[List[managed_mobile_app.ManagedMobileApp]]
        """
        return self._apps
    
    @apps.setter
    def apps(self,value: Optional[List[managed_mobile_app.ManagedMobileApp]] = None) -> None:
        """
        Sets the apps property value. The apps property
        Args:
            value: Value to set for the apps property.
        """
        self._apps = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new targetAppsPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The appGroupType property
        self._app_group_type: Optional[targeted_managed_app_group_type.TargetedManagedAppGroupType] = None
        # The apps property
        self._apps: Optional[List[managed_mobile_app.ManagedMobileApp]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TargetAppsPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TargetAppsPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TargetAppsPostRequestBody()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "app_group_type": lambda n : setattr(self, 'app_group_type', n.get_enum_value(targeted_managed_app_group_type.TargetedManagedAppGroupType)),
            "apps": lambda n : setattr(self, 'apps', n.get_collection_of_object_values(managed_mobile_app.ManagedMobileApp)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_enum_value("appGroupType", self.app_group_type)
        writer.write_collection_of_object_values("apps", self.apps)
        writer.write_additional_data_value(self.additional_data)
    

