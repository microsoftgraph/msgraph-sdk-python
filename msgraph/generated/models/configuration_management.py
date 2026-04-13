from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .configuration_baseline import ConfigurationBaseline
    from .configuration_drift import ConfigurationDrift
    from .configuration_monitor import ConfigurationMonitor
    from .configuration_monitoring_result import ConfigurationMonitoringResult
    from .configuration_snapshot_job import ConfigurationSnapshotJob
    from .entity import Entity

from .entity import Entity

@dataclass
class ConfigurationManagement(Entity, Parsable):
    # A container for configuration drift resources.
    configuration_drifts: Optional[list[ConfigurationDrift]] = None
    # A container for configuration monitoring results resources.
    configuration_monitoring_results: Optional[list[ConfigurationMonitoringResult]] = None
    # A container for configuration monitor resources.
    configuration_monitors: Optional[list[ConfigurationMonitor]] = None
    # A container for snapshot job resources.
    configuration_snapshot_jobs: Optional[list[ConfigurationSnapshotJob]] = None
    # A container for configuration snapshot baselines.
    configuration_snapshots: Optional[list[ConfigurationBaseline]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConfigurationManagement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfigurationManagement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConfigurationManagement()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .configuration_baseline import ConfigurationBaseline
        from .configuration_drift import ConfigurationDrift
        from .configuration_monitor import ConfigurationMonitor
        from .configuration_monitoring_result import ConfigurationMonitoringResult
        from .configuration_snapshot_job import ConfigurationSnapshotJob
        from .entity import Entity

        from .configuration_baseline import ConfigurationBaseline
        from .configuration_drift import ConfigurationDrift
        from .configuration_monitor import ConfigurationMonitor
        from .configuration_monitoring_result import ConfigurationMonitoringResult
        from .configuration_snapshot_job import ConfigurationSnapshotJob
        from .entity import Entity

        fields: dict[str, Callable[[Any], None]] = {
            "configurationDrifts": lambda n : setattr(self, 'configuration_drifts', n.get_collection_of_object_values(ConfigurationDrift)),
            "configurationMonitoringResults": lambda n : setattr(self, 'configuration_monitoring_results', n.get_collection_of_object_values(ConfigurationMonitoringResult)),
            "configurationMonitors": lambda n : setattr(self, 'configuration_monitors', n.get_collection_of_object_values(ConfigurationMonitor)),
            "configurationSnapshotJobs": lambda n : setattr(self, 'configuration_snapshot_jobs', n.get_collection_of_object_values(ConfigurationSnapshotJob)),
            "configurationSnapshots": lambda n : setattr(self, 'configuration_snapshots', n.get_collection_of_object_values(ConfigurationBaseline)),
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
        writer.write_collection_of_object_values("configurationDrifts", self.configuration_drifts)
        writer.write_collection_of_object_values("configurationMonitoringResults", self.configuration_monitoring_results)
        writer.write_collection_of_object_values("configurationMonitors", self.configuration_monitors)
        writer.write_collection_of_object_values("configurationSnapshotJobs", self.configuration_snapshot_jobs)
        writer.write_collection_of_object_values("configurationSnapshots", self.configuration_snapshots)
    

