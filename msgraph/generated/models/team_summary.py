from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class TeamSummary(AdditionalDataHolder, Parsable):
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
    
    def __init__(self,) -> None:
        """
        Instantiates a new teamSummary and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Count of guests in a team.
        self._guests_count: Optional[int] = None
        # Count of members in a team.
        self._members_count: Optional[int] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Count of owners in a team.
        self._owners_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TeamSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TeamSummary
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TeamSummary()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "guests_count": lambda n : setattr(self, 'guests_count', n.get_int_value()),
            "members_count": lambda n : setattr(self, 'members_count', n.get_int_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "owners_count": lambda n : setattr(self, 'owners_count', n.get_int_value()),
        }
        return fields
    
    @property
    def guests_count(self,) -> Optional[int]:
        """
        Gets the guestsCount property value. Count of guests in a team.
        Returns: Optional[int]
        """
        return self._guests_count
    
    @guests_count.setter
    def guests_count(self,value: Optional[int] = None) -> None:
        """
        Sets the guestsCount property value. Count of guests in a team.
        Args:
            value: Value to set for the guestsCount property.
        """
        self._guests_count = value
    
    @property
    def members_count(self,) -> Optional[int]:
        """
        Gets the membersCount property value. Count of members in a team.
        Returns: Optional[int]
        """
        return self._members_count
    
    @members_count.setter
    def members_count(self,value: Optional[int] = None) -> None:
        """
        Sets the membersCount property value. Count of members in a team.
        Args:
            value: Value to set for the membersCount property.
        """
        self._members_count = value
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the OdataType property.
        """
        self._odata_type = value
    
    @property
    def owners_count(self,) -> Optional[int]:
        """
        Gets the ownersCount property value. Count of owners in a team.
        Returns: Optional[int]
        """
        return self._owners_count
    
    @owners_count.setter
    def owners_count(self,value: Optional[int] = None) -> None:
        """
        Sets the ownersCount property value. Count of owners in a team.
        Args:
            value: Value to set for the ownersCount property.
        """
        self._owners_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_int_value("guestsCount", self.guests_count)
        writer.write_int_value("membersCount", self.members_count)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_int_value("ownersCount", self.owners_count)
        writer.write_additional_data_value(self.additional_data)
    

