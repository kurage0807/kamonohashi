# coding: utf-8

"""
    KAMONOHASHI API

    A platform for deep learning  # noqa: E501

    OpenAPI spec version: v2
    Contact: kamonohashi-support@jp.nssol.nipponsteel.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InfosTenantInfo(object):
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
        'default': 'bool',
        'display_name': 'str',
        'id': 'int',
        'name': 'str',
        'roles': 'list[InfosRoleInfo]'
    }

    attribute_map = {
        'default': 'default',
        'display_name': 'displayName',
        'id': 'id',
        'name': 'name',
        'roles': 'roles'
    }

    def __init__(self, default=None, display_name=None, id=None, name=None, roles=None):  # noqa: E501
        """InfosTenantInfo - a model defined in Swagger"""  # noqa: E501

        self._default = None
        self._display_name = None
        self._id = None
        self._name = None
        self._roles = None
        self.discriminator = None

        if default is not None:
            self.default = default
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if roles is not None:
            self.roles = roles

    @property
    def default(self):
        """Gets the default of this InfosTenantInfo.  # noqa: E501


        :return: The default of this InfosTenantInfo.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this InfosTenantInfo.


        :param default: The default of this InfosTenantInfo.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def display_name(self):
        """Gets the display_name of this InfosTenantInfo.  # noqa: E501


        :return: The display_name of this InfosTenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this InfosTenantInfo.


        :param display_name: The display_name of this InfosTenantInfo.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this InfosTenantInfo.  # noqa: E501


        :return: The id of this InfosTenantInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InfosTenantInfo.


        :param id: The id of this InfosTenantInfo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InfosTenantInfo.  # noqa: E501


        :return: The name of this InfosTenantInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InfosTenantInfo.


        :param name: The name of this InfosTenantInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def roles(self):
        """Gets the roles of this InfosTenantInfo.  # noqa: E501


        :return: The roles of this InfosTenantInfo.  # noqa: E501
        :rtype: list[InfosRoleInfo]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this InfosTenantInfo.


        :param roles: The roles of this InfosTenantInfo.  # noqa: E501
        :type: list[InfosRoleInfo]
        """

        self._roles = roles

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
        if issubclass(InfosTenantInfo, dict):
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
        if not isinstance(other, InfosTenantInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
