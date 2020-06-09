# coding: utf-8

"""
    KAMONOHASHI API

    A platform for deep learning  # noqa: E501

    OpenAPI spec version: v1
    Contact: kamonohashi-support@jp.nssol.nipponsteel.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TrainingApiModelsEditInputModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'favorite': 'bool',
        'memo': 'str',
        'name': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'favorite': 'favorite',
        'memo': 'memo',
        'name': 'name',
        'tags': 'tags'
    }

    def __init__(self, favorite=None, memo=None, name=None, tags=None):  # noqa: E501
        """TrainingApiModelsEditInputModel - a model defined in Swagger"""  # noqa: E501

        self._favorite = None
        self._memo = None
        self._name = None
        self._tags = None
        self.discriminator = None

        if favorite is not None:
            self.favorite = favorite
        if memo is not None:
            self.memo = memo
        if name is not None:
            self.name = name
        if tags is not None:
            self.tags = tags

    @property
    def favorite(self):
        """Gets the favorite of this TrainingApiModelsEditInputModel.  # noqa: E501


        :return: The favorite of this TrainingApiModelsEditInputModel.  # noqa: E501
        :rtype: bool
        """
        return self._favorite

    @favorite.setter
    def favorite(self, favorite):
        """Sets the favorite of this TrainingApiModelsEditInputModel.


        :param favorite: The favorite of this TrainingApiModelsEditInputModel.  # noqa: E501
        :type: bool
        """

        self._favorite = favorite

    @property
    def memo(self):
        """Gets the memo of this TrainingApiModelsEditInputModel.  # noqa: E501


        :return: The memo of this TrainingApiModelsEditInputModel.  # noqa: E501
        :rtype: str
        """
        return self._memo

    @memo.setter
    def memo(self, memo):
        """Sets the memo of this TrainingApiModelsEditInputModel.


        :param memo: The memo of this TrainingApiModelsEditInputModel.  # noqa: E501
        :type: str
        """

        self._memo = memo

    @property
    def name(self):
        """Gets the name of this TrainingApiModelsEditInputModel.  # noqa: E501


        :return: The name of this TrainingApiModelsEditInputModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrainingApiModelsEditInputModel.


        :param name: The name of this TrainingApiModelsEditInputModel.  # noqa: E501
        :type: str
        """
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def tags(self):
        """Gets the tags of this TrainingApiModelsEditInputModel.  # noqa: E501


        :return: The tags of this TrainingApiModelsEditInputModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TrainingApiModelsEditInputModel.


        :param tags: The tags of this TrainingApiModelsEditInputModel.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TrainingApiModelsEditInputModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TrainingApiModelsEditInputModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
