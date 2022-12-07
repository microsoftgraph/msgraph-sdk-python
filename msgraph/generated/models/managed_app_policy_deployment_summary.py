from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
managed_app_policy_deployment_summary_per_app = lazy_import('msgraph.generated.models.managed_app_policy_deployment_summary_per_app')

class ManagedAppPolicyDeploymentSummary(entity.Entity):
    @property
    def configuration_deployed_user_count(self,) -> Optional[int]:
        """
        Gets the configurationDeployedUserCount property value. Not yet documented
        Returns: Optional[int]
        """
        return self._configuration_deployed_user_count
    
    @configuration_deployed_user_count.setter
    def configuration_deployed_user_count(self,value: Optional[int] = None) -> None:
        """
        Sets the configurationDeployedUserCount property value. Not yet documented
        Args:
            value: Value to set for the configurationDeployedUserCount property.
        """
        self._configuration_deployed_user_count = value
    
    @property
    def configuration_deployment_summary_per_app(self,) -> Optional[List[managed_app_policy_deployment_summary_per_app.ManagedAppPolicyDeploymentSummaryPerApp]]:
        """
        Gets the configurationDeploymentSummaryPerApp property value. Not yet documented
        Returns: Optional[List[managed_app_policy_deployment_summary_per_app.ManagedAppPolicyDeploymentSummaryPerApp]]
        """
        return self._configuration_deployment_summary_per_app
    
    @configuration_deployment_summary_per_app.setter
    def configuration_deployment_summary_per_app(self,value: Optional[List[managed_app_policy_deployment_summary_per_app.ManagedAppPolicyDeploymentSummaryPerApp]] = None) -> None:
        """
        Sets the configurationDeploymentSummaryPerApp property value. Not yet documented
        Args:
            value: Value to set for the configurationDeploymentSummaryPerApp property.
        """
        self._configuration_deployment_summary_per_app = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new managedAppPolicyDeploymentSummary and sets the default values.
        """
        super().__init__()
        # Not yet documented
        self._configuration_deployed_user_count: Optional[int] = None
        # Not yet documented
        self._configuration_deployment_summary_per_app: Optional[List[managed_app_policy_deployment_summary_per_app.ManagedAppPolicyDeploymentSummaryPerApp]] = None
        # Not yet documented
        self._display_name: Optional[str] = None
        # Not yet documented
        self._last_refresh_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Version of the entity.
        self._version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAppPolicyDeploymentSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppPolicyDeploymentSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedAppPolicyDeploymentSummary()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Not yet documented
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Not yet documented
        Args:
            value: Value to set for the displayName property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "configuration_deployed_user_count": lambda n : setattr(self, 'configuration_deployed_user_count', n.get_int_value()),
            "configuration_deployment_summary_per_app": lambda n : setattr(self, 'configuration_deployment_summary_per_app', n.get_collection_of_object_values(managed_app_policy_deployment_summary_per_app.ManagedAppPolicyDeploymentSummaryPerApp)),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "last_refresh_time": lambda n : setattr(self, 'last_refresh_time', n.get_datetime_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_refresh_time(self,) -> Optional[datetime]:
        """
        Gets the lastRefreshTime property value. Not yet documented
        Returns: Optional[datetime]
        """
        return self._last_refresh_time
    
    @last_refresh_time.setter
    def last_refresh_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastRefreshTime property value. Not yet documented
        Args:
            value: Value to set for the lastRefreshTime property.
        """
        self._last_refresh_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_int_value("configurationDeployedUserCount", self.configuration_deployed_user_count)
        writer.write_collection_of_object_values("configurationDeploymentSummaryPerApp", self.configuration_deployment_summary_per_app)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastRefreshTime", self.last_refresh_time)
        writer.write_str_value("version", self.version)
    
    @property
    def version(self,) -> Optional[str]:
        """
        Gets the version property value. Version of the entity.
        Returns: Optional[str]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[str] = None) -> None:
        """
        Sets the version property value. Version of the entity.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

