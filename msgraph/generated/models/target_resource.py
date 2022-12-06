from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

group_type = lazy_import('msgraph.generated.models.group_type')
modified_property = lazy_import('msgraph.generated.models.modified_property')

class TargetResource(AdditionalDataHolder, Parsable):
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
        Instantiates a new targetResource and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates the visible name defined for the resource. Typically specified when the resource is created.
        self._display_name: Optional[str] = None
        # When type is set to Group, this indicates the group type. Possible values are: unifiedGroups, azureAD, and unknownFutureValue
        self._group_type: Optional[group_type.GroupType] = None
        # Indicates the unique ID of the resource.
        self._id: Optional[str] = None
        # Indicates name, old value and new value of each attribute that changed. Property values depend on the operation type.
        self._modified_properties: Optional[List[modified_property.ModifiedProperty]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # Describes the resource type.  Example values include Application, Group, ServicePrincipal, and User.
        self._type: Optional[str] = None
        # When type is set to User, this includes the user name that initiated the action; null for other types.
        self._user_principal_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> TargetResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: TargetResource
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return TargetResource()
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Indicates the visible name defined for the resource. Typically specified when the resource is created.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Indicates the visible name defined for the resource. Typically specified when the resource is created.
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
            "display_name": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "group_type": lambda n : setattr(self, 'group_type', n.get_enum_value(group_type.GroupType)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "modified_properties": lambda n : setattr(self, 'modified_properties', n.get_collection_of_object_values(modified_property.ModifiedProperty)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "user_principal_name": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
        }
        return fields
    
    @property
    def group_type(self,) -> Optional[group_type.GroupType]:
        """
        Gets the groupType property value. When type is set to Group, this indicates the group type. Possible values are: unifiedGroups, azureAD, and unknownFutureValue
        Returns: Optional[group_type.GroupType]
        """
        return self._group_type
    
    @group_type.setter
    def group_type(self,value: Optional[group_type.GroupType] = None) -> None:
        """
        Sets the groupType property value. When type is set to Group, this indicates the group type. Possible values are: unifiedGroups, azureAD, and unknownFutureValue
        Args:
            value: Value to set for the groupType property.
        """
        self._group_type = value
    
    @property
    def id(self,) -> Optional[str]:
        """
        Gets the id property value. Indicates the unique ID of the resource.
        Returns: Optional[str]
        """
        return self._id
    
    @id.setter
    def id(self,value: Optional[str] = None) -> None:
        """
        Sets the id property value. Indicates the unique ID of the resource.
        Args:
            value: Value to set for the id property.
        """
        self._id = value
    
    @property
    def modified_properties(self,) -> Optional[List[modified_property.ModifiedProperty]]:
        """
        Gets the modifiedProperties property value. Indicates name, old value and new value of each attribute that changed. Property values depend on the operation type.
        Returns: Optional[List[modified_property.ModifiedProperty]]
        """
        return self._modified_properties
    
    @modified_properties.setter
    def modified_properties(self,value: Optional[List[modified_property.ModifiedProperty]] = None) -> None:
        """
        Sets the modifiedProperties property value. Indicates name, old value and new value of each attribute that changed. Property values depend on the operation type.
        Args:
            value: Value to set for the modifiedProperties property.
        """
        self._modified_properties = value
    
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
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_str_value("displayName", self.display_name)
        writer.write_enum_value("groupType", self.group_type)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_object_values("modifiedProperties", self.modified_properties)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("type", self.type)
        writer.write_str_value("userPrincipalName", self.user_principal_name)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[str]:
        """
        Gets the type property value. Describes the resource type.  Example values include Application, Group, ServicePrincipal, and User.
        Returns: Optional[str]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[str] = None) -> None:
        """
        Sets the type property value. Describes the resource type.  Example values include Application, Group, ServicePrincipal, and User.
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. When type is set to User, this includes the user name that initiated the action; null for other types.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. When type is set to User, this includes the user name that initiated the action; null for other types.
        Args:
            value: Value to set for the userPrincipalName property.
        """
        self._user_principal_name = value
    

