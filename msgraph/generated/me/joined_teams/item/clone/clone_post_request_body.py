from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

clonable_team_parts = lazy_import('msgraph.generated.models.clonable_team_parts')
team_visibility_type = lazy_import('msgraph.generated.models.team_visibility_type')

class ClonePostRequestBody(AdditionalDataHolder, Parsable):
    """
    Provides operations to call the clone method.
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
    def classification(self,) -> Optional[str]:
        """
        Gets the classification property value. The classification property
        Returns: Optional[str]
        """
        return self._classification
    
    @classification.setter
    def classification(self,value: Optional[str] = None) -> None:
        """
        Sets the classification property value. The classification property
        Args:
            value: Value to set for the classification property.
        """
        self._classification = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new clonePostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The classification property
        self._classification: Optional[str] = None
        # The description property
        self._description: Optional[str] = None
        # The displayName property
        self._display_name: Optional[str] = None
        # The mailNickname property
        self._mail_nickname: Optional[str] = None
        # The partsToClone property
        self._parts_to_clone: Optional[clonable_team_parts.ClonableTeamParts] = None
        # The visibility property
        self._visibility: Optional[team_visibility_type.TeamVisibilityType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ClonePostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ClonePostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ClonePostRequestBody()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. The description property
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. The description property
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The displayName property
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The displayName property
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
            "classification": lambda n : setattr(self, 'classification', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "mail_nickname": lambda n : setattr(self, 'mail_nickname', n.get_str_value()),
            "parts_to_clone": lambda n : setattr(self, 'parts_to_clone', n.get_enum_value(clonable_team_parts.ClonableTeamParts)),
            "visibility": lambda n : setattr(self, 'visibility', n.get_enum_value(team_visibility_type.TeamVisibilityType)),
        }
        return fields
    
    @property
    def mail_nickname(self,) -> Optional[str]:
        """
        Gets the mailNickname property value. The mailNickname property
        Returns: Optional[str]
        """
        return self._mail_nickname
    
    @mail_nickname.setter
    def mail_nickname(self,value: Optional[str] = None) -> None:
        """
        Sets the mailNickname property value. The mailNickname property
        Args:
            value: Value to set for the mailNickname property.
        """
        self._mail_nickname = value
    
    @property
    def parts_to_clone(self,) -> Optional[clonable_team_parts.ClonableTeamParts]:
        """
        Gets the partsToClone property value. The partsToClone property
        Returns: Optional[clonable_team_parts.ClonableTeamParts]
        """
        return self._parts_to_clone
    
    @parts_to_clone.setter
    def parts_to_clone(self,value: Optional[clonable_team_parts.ClonableTeamParts] = None) -> None:
        """
        Sets the partsToClone property value. The partsToClone property
        Args:
            value: Value to set for the partsToClone property.
        """
        self._parts_to_clone = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("classification", self.classification)
        writer.write_str_value("description", self.description)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("mailNickname", self.mail_nickname)
        writer.write_enum_value("partsToClone", self.parts_to_clone)
        writer.write_enum_value("visibility", self.visibility)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def visibility(self,) -> Optional[team_visibility_type.TeamVisibilityType]:
        """
        Gets the visibility property value. The visibility property
        Returns: Optional[team_visibility_type.TeamVisibilityType]
        """
        return self._visibility
    
    @visibility.setter
    def visibility(self,value: Optional[team_visibility_type.TeamVisibilityType] = None) -> None:
        """
        Sets the visibility property value. The visibility property
        Args:
            value: Value to set for the visibility property.
        """
        self._visibility = value
    

