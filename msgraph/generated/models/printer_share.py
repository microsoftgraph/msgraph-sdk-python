from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .group import Group
    from .printer import Printer
    from .printer_base import PrinterBase
    from .printer_share_viewpoint import PrinterShareViewpoint
    from .user import User

from .printer_base import PrinterBase

@dataclass
class PrinterShare(PrinterBase):
    # The OdataType property
    odata_type: Optional[str] = "#microsoft.graph.printerShare"
    # If true, all users and groups will be granted access to this printer share. This supersedes the allow lists defined by the allowedUsers and allowedGroups navigation properties.
    allow_all_users: Optional[bool] = None
    # The groups whose users have access to print using the printer.
    allowed_groups: Optional[List[Group]] = None
    # The users who have access to print using the printer.
    allowed_users: Optional[List[User]] = None
    # The DateTimeOffset when the printer share was created. Read-only.
    created_date_time: Optional[datetime.datetime] = None
    # The printer that this printer share is related to.
    printer: Optional[Printer] = None
    # Additional data for a printer share as viewed by the signed-in user.
    view_point: Optional[PrinterShareViewpoint] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PrinterShare:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PrinterShare
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PrinterShare()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .group import Group
        from .printer import Printer
        from .printer_base import PrinterBase
        from .printer_share_viewpoint import PrinterShareViewpoint
        from .user import User

        from .group import Group
        from .printer import Printer
        from .printer_base import PrinterBase
        from .printer_share_viewpoint import PrinterShareViewpoint
        from .user import User

        fields: Dict[str, Callable[[Any], None]] = {
            "allowAllUsers": lambda n : setattr(self, 'allow_all_users', n.get_bool_value()),
            "allowedGroups": lambda n : setattr(self, 'allowed_groups', n.get_collection_of_object_values(Group)),
            "allowedUsers": lambda n : setattr(self, 'allowed_users', n.get_collection_of_object_values(User)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "printer": lambda n : setattr(self, 'printer', n.get_object_value(Printer)),
            "viewPoint": lambda n : setattr(self, 'view_point', n.get_object_value(PrinterShareViewpoint)),
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
        writer.write_bool_value("allowAllUsers", self.allow_all_users)
        writer.write_collection_of_object_values("allowedGroups", self.allowed_groups)
        writer.write_collection_of_object_values("allowedUsers", self.allowed_users)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_object_value("printer", self.printer)
        writer.write_object_value("viewPoint", self.view_point)
    

