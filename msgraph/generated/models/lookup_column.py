from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

class LookupColumn(AdditionalDataHolder, Parsable):
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
    def allow_multiple_values(self,) -> Optional[bool]:
        """
        Gets the allowMultipleValues property value. Indicates whether multiple values can be selected from the source.
        Returns: Optional[bool]
        """
        return self._allow_multiple_values
    
    @allow_multiple_values.setter
    def allow_multiple_values(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowMultipleValues property value. Indicates whether multiple values can be selected from the source.
        Args:
            value: Value to set for the allowMultipleValues property.
        """
        self._allow_multiple_values = value
    
    @property
    def allow_unlimited_length(self,) -> Optional[bool]:
        """
        Gets the allowUnlimitedLength property value. Indicates whether values in the column should be able to exceed the standard limit of 255 characters.
        Returns: Optional[bool]
        """
        return self._allow_unlimited_length
    
    @allow_unlimited_length.setter
    def allow_unlimited_length(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowUnlimitedLength property value. Indicates whether values in the column should be able to exceed the standard limit of 255 characters.
        Args:
            value: Value to set for the allowUnlimitedLength property.
        """
        self._allow_unlimited_length = value
    
    @property
    def column_name(self,) -> Optional[str]:
        """
        Gets the columnName property value. The name of the lookup source column.
        Returns: Optional[str]
        """
        return self._column_name
    
    @column_name.setter
    def column_name(self,value: Optional[str] = None) -> None:
        """
        Sets the columnName property value. The name of the lookup source column.
        Args:
            value: Value to set for the columnName property.
        """
        self._column_name = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new lookupColumn and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether multiple values can be selected from the source.
        self._allow_multiple_values: Optional[bool] = None
        # Indicates whether values in the column should be able to exceed the standard limit of 255 characters.
        self._allow_unlimited_length: Optional[bool] = None
        # The name of the lookup source column.
        self._column_name: Optional[str] = None
        # The unique identifier of the lookup source list.
        self._list_id: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # If specified, this column is a secondary lookup, pulling an additional field from the list item looked up by the primary lookup. Use the list item looked up by the primary as the source for the column named here.
        self._primary_lookup_column_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> LookupColumn:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: LookupColumn
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return LookupColumn()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "allow_multiple_values": lambda n : setattr(self, 'allow_multiple_values', n.get_bool_value()),
            "allow_unlimited_length": lambda n : setattr(self, 'allow_unlimited_length', n.get_bool_value()),
            "column_name": lambda n : setattr(self, 'column_name', n.get_str_value()),
            "list_id": lambda n : setattr(self, 'list_id', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "primary_lookup_column_id": lambda n : setattr(self, 'primary_lookup_column_id', n.get_str_value()),
        }
        return fields
    
    @property
    def list_id(self,) -> Optional[str]:
        """
        Gets the listId property value. The unique identifier of the lookup source list.
        Returns: Optional[str]
        """
        return self._list_id
    
    @list_id.setter
    def list_id(self,value: Optional[str] = None) -> None:
        """
        Sets the listId property value. The unique identifier of the lookup source list.
        Args:
            value: Value to set for the listId property.
        """
        self._list_id = value
    
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
    def primary_lookup_column_id(self,) -> Optional[str]:
        """
        Gets the primaryLookupColumnId property value. If specified, this column is a secondary lookup, pulling an additional field from the list item looked up by the primary lookup. Use the list item looked up by the primary as the source for the column named here.
        Returns: Optional[str]
        """
        return self._primary_lookup_column_id
    
    @primary_lookup_column_id.setter
    def primary_lookup_column_id(self,value: Optional[str] = None) -> None:
        """
        Sets the primaryLookupColumnId property value. If specified, this column is a secondary lookup, pulling an additional field from the list item looked up by the primary lookup. Use the list item looked up by the primary as the source for the column named here.
        Args:
            value: Value to set for the primaryLookupColumnId property.
        """
        self._primary_lookup_column_id = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allowMultipleValues", self.allow_multiple_values)
        writer.write_bool_value("allowUnlimitedLength", self.allow_unlimited_length)
        writer.write_str_value("columnName", self.column_name)
        writer.write_str_value("listId", self.list_id)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("primaryLookupColumnId", self.primary_lookup_column_id)
        writer.write_additional_data_value(self.additional_data)
    

