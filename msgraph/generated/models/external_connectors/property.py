from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

label = lazy_import('msgraph.generated.models.external_connectors.label')
property_type = lazy_import('msgraph.generated.models.external_connectors.property_type')

class Property(AdditionalDataHolder, Parsable):
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
    def aliases(self,) -> Optional[List[str]]:
        """
        Gets the aliases property value. A set of aliases or a friendly names for the property. Maximum 32 characters. Only alphanumeric characters allowed. For example, each string may not contain control characters, whitespace, or any of the following: :, ;, ,, (, ), [, ], {, }, %, $, +, !, *, =, &, ?, @, #, /, ~, ', ', <, >, `, ^. Optional.
        Returns: Optional[List[str]]
        """
        return self._aliases
    
    @aliases.setter
    def aliases(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the aliases property value. A set of aliases or a friendly names for the property. Maximum 32 characters. Only alphanumeric characters allowed. For example, each string may not contain control characters, whitespace, or any of the following: :, ;, ,, (, ), [, ], {, }, %, $, +, !, *, =, &, ?, @, #, /, ~, ', ', <, >, `, ^. Optional.
        Args:
            value: Value to set for the aliases property.
        """
        self._aliases = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new property and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # A set of aliases or a friendly names for the property. Maximum 32 characters. Only alphanumeric characters allowed. For example, each string may not contain control characters, whitespace, or any of the following: :, ;, ,, (, ), [, ], {, }, %, $, +, !, *, =, &, ?, @, #, /, ~, ', ', <, >, `, ^. Optional.
        self._aliases: Optional[List[str]] = None
        # Specifies if the property is queryable. Queryable properties can be used in Keyword Query Language (KQL) queries. Optional.
        self._is_queryable: Optional[bool] = None
        # Specifies if the property is refinable.  Refinable properties can be used to filter search results in the Search API and add a refiner control in the Microsoft Search user experience. Optional.
        self._is_refinable: Optional[bool] = None
        # Specifies if the property is retrievable. Retrievable properties are returned in the result set when items are returned by the search API. Retrievable properties are also available to add to the display template used to render search results. Optional.
        self._is_retrievable: Optional[bool] = None
        # Specifies if the property is searchable. Only properties of type String or StringCollection can be searchable. Non-searchable properties are not added to the search index. Optional.
        self._is_searchable: Optional[bool] = None
        # Specifies one or more well-known tags added against a property. Labels help Microsoft Search understand the semantics of the data in the connection. Adding appropriate labels would result in an enhanced search experience (e.g. better relevance). The possible values are: title, url, createdBy, lastModifiedBy, authors, createdDateTime, lastModifiedDateTime, fileName, fileExtension, unknownFutureValue. Optional.
        self._labels: Optional[List[label.Label]] = None
        # The name of the property. Maximum 32 characters. Only alphanumeric characters allowed. For example, each string may not contain control characters, whitespace, or any of the following: :, ;, ,, (, ), [, ], {, }, %, $, +, !, *, =, &, ?, @, #, /, ~, ', ', <, >, `, ^.  Required.
        self._name: Optional[str] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The type property
        self._type: Optional[property_type.PropertyType] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Property:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Property
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Property()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "aliases": lambda n : setattr(self, 'aliases', n.get_collection_of_primitive_values(str)),
            "is_queryable": lambda n : setattr(self, 'is_queryable', n.get_bool_value()),
            "is_refinable": lambda n : setattr(self, 'is_refinable', n.get_bool_value()),
            "is_retrievable": lambda n : setattr(self, 'is_retrievable', n.get_bool_value()),
            "is_searchable": lambda n : setattr(self, 'is_searchable', n.get_bool_value()),
            "labels": lambda n : setattr(self, 'labels', n.get_collection_of_enum_values(label.Label)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(property_type.PropertyType)),
        }
        return fields
    
    @property
    def is_queryable(self,) -> Optional[bool]:
        """
        Gets the isQueryable property value. Specifies if the property is queryable. Queryable properties can be used in Keyword Query Language (KQL) queries. Optional.
        Returns: Optional[bool]
        """
        return self._is_queryable
    
    @is_queryable.setter
    def is_queryable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isQueryable property value. Specifies if the property is queryable. Queryable properties can be used in Keyword Query Language (KQL) queries. Optional.
        Args:
            value: Value to set for the isQueryable property.
        """
        self._is_queryable = value
    
    @property
    def is_refinable(self,) -> Optional[bool]:
        """
        Gets the isRefinable property value. Specifies if the property is refinable.  Refinable properties can be used to filter search results in the Search API and add a refiner control in the Microsoft Search user experience. Optional.
        Returns: Optional[bool]
        """
        return self._is_refinable
    
    @is_refinable.setter
    def is_refinable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRefinable property value. Specifies if the property is refinable.  Refinable properties can be used to filter search results in the Search API and add a refiner control in the Microsoft Search user experience. Optional.
        Args:
            value: Value to set for the isRefinable property.
        """
        self._is_refinable = value
    
    @property
    def is_retrievable(self,) -> Optional[bool]:
        """
        Gets the isRetrievable property value. Specifies if the property is retrievable. Retrievable properties are returned in the result set when items are returned by the search API. Retrievable properties are also available to add to the display template used to render search results. Optional.
        Returns: Optional[bool]
        """
        return self._is_retrievable
    
    @is_retrievable.setter
    def is_retrievable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isRetrievable property value. Specifies if the property is retrievable. Retrievable properties are returned in the result set when items are returned by the search API. Retrievable properties are also available to add to the display template used to render search results. Optional.
        Args:
            value: Value to set for the isRetrievable property.
        """
        self._is_retrievable = value
    
    @property
    def is_searchable(self,) -> Optional[bool]:
        """
        Gets the isSearchable property value. Specifies if the property is searchable. Only properties of type String or StringCollection can be searchable. Non-searchable properties are not added to the search index. Optional.
        Returns: Optional[bool]
        """
        return self._is_searchable
    
    @is_searchable.setter
    def is_searchable(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSearchable property value. Specifies if the property is searchable. Only properties of type String or StringCollection can be searchable. Non-searchable properties are not added to the search index. Optional.
        Args:
            value: Value to set for the isSearchable property.
        """
        self._is_searchable = value
    
    @property
    def labels(self,) -> Optional[List[label.Label]]:
        """
        Gets the labels property value. Specifies one or more well-known tags added against a property. Labels help Microsoft Search understand the semantics of the data in the connection. Adding appropriate labels would result in an enhanced search experience (e.g. better relevance). The possible values are: title, url, createdBy, lastModifiedBy, authors, createdDateTime, lastModifiedDateTime, fileName, fileExtension, unknownFutureValue. Optional.
        Returns: Optional[List[label.Label]]
        """
        return self._labels
    
    @labels.setter
    def labels(self,value: Optional[List[label.Label]] = None) -> None:
        """
        Sets the labels property value. Specifies one or more well-known tags added against a property. Labels help Microsoft Search understand the semantics of the data in the connection. Adding appropriate labels would result in an enhanced search experience (e.g. better relevance). The possible values are: title, url, createdBy, lastModifiedBy, authors, createdDateTime, lastModifiedDateTime, fileName, fileExtension, unknownFutureValue. Optional.
        Args:
            value: Value to set for the labels property.
        """
        self._labels = value
    
    @property
    def name(self,) -> Optional[str]:
        """
        Gets the name property value. The name of the property. Maximum 32 characters. Only alphanumeric characters allowed. For example, each string may not contain control characters, whitespace, or any of the following: :, ;, ,, (, ), [, ], {, }, %, $, +, !, *, =, &, ?, @, #, /, ~, ', ', <, >, `, ^.  Required.
        Returns: Optional[str]
        """
        return self._name
    
    @name.setter
    def name(self,value: Optional[str] = None) -> None:
        """
        Sets the name property value. The name of the property. Maximum 32 characters. Only alphanumeric characters allowed. For example, each string may not contain control characters, whitespace, or any of the following: :, ;, ,, (, ), [, ], {, }, %, $, +, !, *, =, &, ?, @, #, /, ~, ', ', <, >, `, ^.  Required.
        Args:
            value: Value to set for the name property.
        """
        self._name = value
    
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
        writer.write_collection_of_primitive_values("aliases", self.aliases)
        writer.write_bool_value("isQueryable", self.is_queryable)
        writer.write_bool_value("isRefinable", self.is_refinable)
        writer.write_bool_value("isRetrievable", self.is_retrievable)
        writer.write_bool_value("isSearchable", self.is_searchable)
        writer.write_enum_value("labels", self.labels)
        writer.write_str_value("name", self.name)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def type(self,) -> Optional[property_type.PropertyType]:
        """
        Gets the type property value. The type property
        Returns: Optional[property_type.PropertyType]
        """
        return self._type
    
    @type.setter
    def type(self,value: Optional[property_type.PropertyType] = None) -> None:
        """
        Sets the type property value. The type property
        Args:
            value: Value to set for the type property.
        """
        self._type = value
    

