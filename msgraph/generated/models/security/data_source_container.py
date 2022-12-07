from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

entity = lazy_import('msgraph.generated.models.entity')
data_source_container_status = lazy_import('msgraph.generated.models.security.data_source_container_status')
data_source_hold_status = lazy_import('msgraph.generated.models.security.data_source_hold_status')

class DataSourceContainer(entity.Entity):
    """
    Provides operations to manage the collection of agreement entities.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new dataSourceContainer and sets the default values.
        """
        super().__init__()
        # Created date and time of the dataSourceContainer entity.
        self._created_date_time: Optional[datetime] = None
        # Display name of the dataSourceContainer entity.
        self._display_name: Optional[str] = None
        # The hold status of the dataSourceContainer. The possible values are: notApplied, applied, applying, removing, partial
        self._hold_status: Optional[data_source_hold_status.DataSourceHoldStatus] = None
        # Last modified date and time of the dataSourceContainer.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Date and time that the dataSourceContainer was released from the case.
        self._released_date_time: Optional[datetime] = None
        # Latest status of the dataSourceContainer. Possible values are: Active, Released.
        self._status: Optional[data_source_container_status.DataSourceContainerStatus] = None
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Created date and time of the dataSourceContainer entity.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Created date and time of the dataSourceContainer entity.
        Args:
            value: Value to set for the createdDateTime property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DataSourceContainer:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DataSourceContainer
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return DataSourceContainer()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Display name of the dataSourceContainer entity.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Display name of the dataSourceContainer entity.
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
            "created_date_time": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "hold_status": lambda n : setattr(self, 'hold_status', n.get_enum_value(data_source_hold_status.DataSourceHoldStatus)),
            "last_modified_date_time": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "released_date_time": lambda n : setattr(self, 'released_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(data_source_container_status.DataSourceContainerStatus)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def hold_status(self,) -> Optional[data_source_hold_status.DataSourceHoldStatus]:
        """
        Gets the holdStatus property value. The hold status of the dataSourceContainer. The possible values are: notApplied, applied, applying, removing, partial
        Returns: Optional[data_source_hold_status.DataSourceHoldStatus]
        """
        return self._hold_status
    
    @hold_status.setter
    def hold_status(self,value: Optional[data_source_hold_status.DataSourceHoldStatus] = None) -> None:
        """
        Sets the holdStatus property value. The hold status of the dataSourceContainer. The possible values are: notApplied, applied, applying, removing, partial
        Args:
            value: Value to set for the holdStatus property.
        """
        self._hold_status = value
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. Last modified date and time of the dataSourceContainer.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. Last modified date and time of the dataSourceContainer.
        Args:
            value: Value to set for the lastModifiedDateTime property.
        """
        self._last_modified_date_time = value
    
    @property
    def released_date_time(self,) -> Optional[datetime]:
        """
        Gets the releasedDateTime property value. Date and time that the dataSourceContainer was released from the case.
        Returns: Optional[datetime]
        """
        return self._released_date_time
    
    @released_date_time.setter
    def released_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the releasedDateTime property value. Date and time that the dataSourceContainer was released from the case.
        Args:
            value: Value to set for the releasedDateTime property.
        """
        self._released_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("holdStatus", self.hold_status)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_datetime_value("releasedDateTime", self.released_date_time)
        writer.write_enum_value("status", self.status)
    
    @property
    def status(self,) -> Optional[data_source_container_status.DataSourceContainerStatus]:
        """
        Gets the status property value. Latest status of the dataSourceContainer. Possible values are: Active, Released.
        Returns: Optional[data_source_container_status.DataSourceContainerStatus]
        """
        return self._status
    
    @status.setter
    def status(self,value: Optional[data_source_container_status.DataSourceContainerStatus] = None) -> None:
        """
        Sets the status property value. Latest status of the dataSourceContainer. Possible values are: Active, Released.
        Args:
            value: Value to set for the status property.
        """
        self._status = value
    

