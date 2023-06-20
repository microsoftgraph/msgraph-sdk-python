from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import group, printer, printer_base, user

from . import printer_base

@dataclass
class PrinterShare(printer_base.PrinterBase):
    odata_type = "#microsoft.graph.printerShare"
    # If true, all users and groups will be granted access to this printer share. This supersedes the allow lists defined by the allowedUsers and allowedGroups navigation properties.
    allow_all_users: Optional[bool] = None
    # The groups whose users have access to print using the printer.
    allowed_groups: Optional[List[group.Group]] = None
    # The users who have access to print using the printer.
    allowed_users: Optional[List[user.User]] = None
    # The DateTimeOffset when the printer share was created. Read-only.
    created_date_time: Optional[datetime] = None
    # The printer that this printer share is related to.
    printer: Optional[printer.Printer] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrinterShare:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrinterShare
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PrinterShare()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import group, printer, printer_base, user

        from . import group, printer, printer_base, user

        fields: Dict[str, Callable[[Any], None]] = {
            "allowAllUsers": lambda n : setattr(self, 'allow_all_users', n.get_bool_value()),
            "allowedGroups": lambda n : setattr(self, 'allowed_groups', n.get_collection_of_object_values(group.Group)),
            "allowedUsers": lambda n : setattr(self, 'allowed_users', n.get_collection_of_object_values(user.User)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "printer": lambda n : setattr(self, 'printer', n.get_object_value(printer.Printer)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_bool_value("allowAllUsers", self.allow_all_users)
        writer.write_collection_of_object_values("allowedGroups", self.allowed_groups)
        writer.write_collection_of_object_values("allowedUsers", self.allowed_users)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("printer", self.printer)
    

