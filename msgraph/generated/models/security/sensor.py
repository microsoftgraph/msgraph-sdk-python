from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..entity import Entity
    from .deployment_status import DeploymentStatus
    from .health_issue import HealthIssue
    from .sensor_health_status import SensorHealthStatus
    from .sensor_settings import SensorSettings
    from .sensor_type import SensorType
    from .service_status import ServiceStatus

from ..entity import Entity

@dataclass
class Sensor(Entity, Parsable):
    # The date and time when the sensor was generated. The Timestamp represents date and time information using ISO 8601 format and is always in UTC. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
    created_date_time: Optional[datetime.datetime] = None
    # The deploymentStatus property
    deployment_status: Optional[DeploymentStatus] = None
    # The display name of the sensor.
    display_name: Optional[str] = None
    # The fully qualified domain name of the sensor.
    domain_name: Optional[str] = None
    # Represents potential issues within a customer's Microsoft Defender for Identity configuration that Microsoft Defender for Identity identified related to the sensor.
    health_issues: Optional[list[HealthIssue]] = None
    # The healthStatus property
    health_status: Optional[SensorHealthStatus] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # This field displays the count of health issues related to this sensor.
    open_health_issues_count: Optional[int] = None
    # The sensorType property
    sensor_type: Optional[SensorType] = None
    # The serviceStatus property
    service_status: Optional[ServiceStatus] = None
    # The settings property
    settings: Optional[SensorSettings] = None
    # The version of the sensor.
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Sensor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Sensor
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Sensor()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..entity import Entity
        from .deployment_status import DeploymentStatus
        from .health_issue import HealthIssue
        from .sensor_health_status import SensorHealthStatus
        from .sensor_settings import SensorSettings
        from .sensor_type import SensorType
        from .service_status import ServiceStatus

        from ..entity import Entity
        from .deployment_status import DeploymentStatus
        from .health_issue import HealthIssue
        from .sensor_health_status import SensorHealthStatus
        from .sensor_settings import SensorSettings
        from .sensor_type import SensorType
        from .service_status import ServiceStatus

        fields: dict[str, Callable[[Any], None]] = {
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "deploymentStatus": lambda n : setattr(self, 'deployment_status', n.get_enum_value(DeploymentStatus)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "domainName": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "healthIssues": lambda n : setattr(self, 'health_issues', n.get_collection_of_object_values(HealthIssue)),
            "healthStatus": lambda n : setattr(self, 'health_status', n.get_enum_value(SensorHealthStatus)),
            "openHealthIssuesCount": lambda n : setattr(self, 'open_health_issues_count', n.get_int_value()),
            "sensorType": lambda n : setattr(self, 'sensor_type', n.get_enum_value(SensorType)),
            "serviceStatus": lambda n : setattr(self, 'service_status', n.get_enum_value(ServiceStatus)),
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(SensorSettings)),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_enum_value("deploymentStatus", self.deployment_status)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_collection_of_object_values("healthIssues", self.health_issues)
        writer.write_enum_value("healthStatus", self.health_status)
        writer.write_int_value("openHealthIssuesCount", self.open_health_issues_count)
        writer.write_enum_value("sensorType", self.sensor_type)
        writer.write_enum_value("serviceStatus", self.service_status)
        writer.write_object_value("settings", self.settings)
        writer.write_str_value("version", self.version)
    

