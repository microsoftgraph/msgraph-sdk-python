from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import external_activity_result, external_activity_type, identity
    from .. import entity

from .. import entity

class ExternalActivity(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new externalActivity and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Represents an identity used to identify who is responsible for the activity.
        self._performed_by: Optional[identity.Identity] = None
        # The date and time when the particular activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        self._start_date_time: Optional[datetime] = None
        # The type property
        self._type: Optional[external_activity_type.ExternalActivityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ExternalActivity:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ExternalActivity
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.externalConnectors.externalActivityResult":
                from . import external_activity_result

                return external_activity_result.ExternalActivityResult()
        return ExternalActivity()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import external_activity_result, external_activity_type, identity
        from .. import entity

        fields: Dict[str, Callable[[Any], None]] = {
            "performedBy": lambda n : setattr(self, 'performed_by', n.get_object_value(identity.Identity)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(external_activity_type.ExternalActivityType)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def performed_by(self,) -> Optional[identity.Identity]:
        """
        Gets the performedBy property value. Represents an identity used to identify who is responsible for the activity.
        Returns: Optional[identity.Identity]
        """
        return self._performed_by
    
    @performed_by.setter
    def performed_by(self,value: Optional[identity.Identity] = None) -> None:
        """
        Sets the performedBy property value. Represents an identity used to identify who is responsible for the activity.
        Args:
            value: Value to set for the performed_by property.
        """
        self._performed_by = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("performedBy", self.performed_by)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_enum_value("type", self.type)
    
    @property
    def start_date_time(self,) -> Optional[datetime]:
        """
        Gets the startDateTime property value. The date and time when the particular activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Returns: Optional[datetime]
        """
        return self._start_date_time
    
    @start_date_time.setter
    def start_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the startDateTime property value. The date and time when the particular activity occurred. The DateTimeOffset type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z.
        Args:
            value: Value to set for the start_date_time property.
        """
        self._start_date_time = value
    
    @property
    def type(self,) -> Optional[external_activity_type.ExternalActivityType]:
        """
        Gets the type property value. The type property
        Returns: Optional[external_activity_type.ExternalActivityType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[external_activity_type.ExternalActivityType] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

