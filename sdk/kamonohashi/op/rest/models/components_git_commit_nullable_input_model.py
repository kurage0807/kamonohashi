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


class ComponentsGitCommitNullableInputModel(object):
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
        'branch': 'str',
        'commit_id': 'str',
        'git_id': 'int',
        'owner': 'str',
        'repository': 'str'
    }

    attribute_map = {
        'branch': 'branch',
        'commit_id': 'commitId',
        'git_id': 'gitId',
        'owner': 'owner',
        'repository': 'repository'
    }

    def __init__(self, branch=None, commit_id=None, git_id=None, owner=None, repository=None):  # noqa: E501
        """ComponentsGitCommitNullableInputModel - a model defined in Swagger"""  # noqa: E501

        self._branch = None
        self._commit_id = None
        self._git_id = None
        self._owner = None
        self._repository = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        if commit_id is not None:
            self.commit_id = commit_id
        if git_id is not None:
            self.git_id = git_id
        if owner is not None:
            self.owner = owner
        if repository is not None:
            self.repository = repository

    @property
    def branch(self):
        """Gets the branch of this ComponentsGitCommitNullableInputModel.  # noqa: E501


        :return: The branch of this ComponentsGitCommitNullableInputModel.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this ComponentsGitCommitNullableInputModel.


        :param branch: The branch of this ComponentsGitCommitNullableInputModel.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def commit_id(self):
        """Gets the commit_id of this ComponentsGitCommitNullableInputModel.  # noqa: E501


        :return: The commit_id of this ComponentsGitCommitNullableInputModel.  # noqa: E501
        :rtype: str
        """
        return self._commit_id

    @commit_id.setter
    def commit_id(self, commit_id):
        """Sets the commit_id of this ComponentsGitCommitNullableInputModel.


        :param commit_id: The commit_id of this ComponentsGitCommitNullableInputModel.  # noqa: E501
        :type: str
        """

        self._commit_id = commit_id

    @property
    def git_id(self):
        """Gets the git_id of this ComponentsGitCommitNullableInputModel.  # noqa: E501


        :return: The git_id of this ComponentsGitCommitNullableInputModel.  # noqa: E501
        :rtype: int
        """
        return self._git_id

    @git_id.setter
    def git_id(self, git_id):
        """Sets the git_id of this ComponentsGitCommitNullableInputModel.


        :param git_id: The git_id of this ComponentsGitCommitNullableInputModel.  # noqa: E501
        :type: int
        """

        self._git_id = git_id

    @property
    def owner(self):
        """Gets the owner of this ComponentsGitCommitNullableInputModel.  # noqa: E501


        :return: The owner of this ComponentsGitCommitNullableInputModel.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ComponentsGitCommitNullableInputModel.


        :param owner: The owner of this ComponentsGitCommitNullableInputModel.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def repository(self):
        """Gets the repository of this ComponentsGitCommitNullableInputModel.  # noqa: E501


        :return: The repository of this ComponentsGitCommitNullableInputModel.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this ComponentsGitCommitNullableInputModel.


        :param repository: The repository of this ComponentsGitCommitNullableInputModel.  # noqa: E501
        :type: str
        """

        self._repository = repository

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
        if issubclass(ComponentsGitCommitNullableInputModel, dict):
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
        if not isinstance(other, ComponentsGitCommitNullableInputModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
