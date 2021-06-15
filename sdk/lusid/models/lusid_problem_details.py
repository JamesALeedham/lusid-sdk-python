# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3148
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class LusidProblemDetails(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'name': 'str',
        'error_details': 'list[dict(str, str)]',
        'code': 'int',
        'type': 'str',
        'title': 'str',
        'status': 'int',
        'detail': 'str',
        'instance': 'str',
        'extensions': 'dict(str, object)'
    }

    attribute_map = {
        'name': 'name',
        'error_details': 'errorDetails',
        'code': 'code',
        'type': 'type',
        'title': 'title',
        'status': 'status',
        'detail': 'detail',
        'instance': 'instance',
        'extensions': 'extensions'
    }

    required_map = {
        'name': 'required',
        'error_details': 'optional',
        'code': 'required',
        'type': 'optional',
        'title': 'optional',
        'status': 'optional',
        'detail': 'optional',
        'instance': 'optional',
        'extensions': 'optional'
    }

    def __init__(self, name=None, error_details=None, code=None, type=None, title=None, status=None, detail=None, instance=None, extensions=None):  # noqa: E501
        """
        LusidProblemDetails - a model defined in OpenAPI

        :param name:  (required)
        :type name: str
        :param error_details: 
        :type error_details: list[dict(str, str)]
        :param code:  (required)
        :type code: int
        :param type: 
        :type type: str
        :param title: 
        :type title: str
        :param status: 
        :type status: int
        :param detail: 
        :type detail: str
        :param instance: 
        :type instance: str
        :param extensions: 
        :type extensions: dict(str, object)

        """  # noqa: E501

        self._name = None
        self._error_details = None
        self._code = None
        self._type = None
        self._title = None
        self._status = None
        self._detail = None
        self._instance = None
        self._extensions = None
        self.discriminator = None

        self.name = name
        self.error_details = error_details
        self.code = code
        self.type = type
        self.title = title
        self.status = status
        self.detail = detail
        self.instance = instance
        self.extensions = extensions

    @property
    def name(self):
        """Gets the name of this LusidProblemDetails.  # noqa: E501


        :return: The name of this LusidProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LusidProblemDetails.


        :param name: The name of this LusidProblemDetails.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def error_details(self):
        """Gets the error_details of this LusidProblemDetails.  # noqa: E501


        :return: The error_details of this LusidProblemDetails.  # noqa: E501
        :rtype: list[dict(str, str)]
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this LusidProblemDetails.


        :param error_details: The error_details of this LusidProblemDetails.  # noqa: E501
        :type: list[dict(str, str)]
        """

        self._error_details = error_details

    @property
    def code(self):
        """Gets the code of this LusidProblemDetails.  # noqa: E501


        :return: The code of this LusidProblemDetails.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this LusidProblemDetails.


        :param code: The code of this LusidProblemDetails.  # noqa: E501
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def type(self):
        """Gets the type of this LusidProblemDetails.  # noqa: E501


        :return: The type of this LusidProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LusidProblemDetails.


        :param type: The type of this LusidProblemDetails.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def title(self):
        """Gets the title of this LusidProblemDetails.  # noqa: E501


        :return: The title of this LusidProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LusidProblemDetails.


        :param title: The title of this LusidProblemDetails.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def status(self):
        """Gets the status of this LusidProblemDetails.  # noqa: E501


        :return: The status of this LusidProblemDetails.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LusidProblemDetails.


        :param status: The status of this LusidProblemDetails.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def detail(self):
        """Gets the detail of this LusidProblemDetails.  # noqa: E501


        :return: The detail of this LusidProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this LusidProblemDetails.


        :param detail: The detail of this LusidProblemDetails.  # noqa: E501
        :type: str
        """

        self._detail = detail

    @property
    def instance(self):
        """Gets the instance of this LusidProblemDetails.  # noqa: E501


        :return: The instance of this LusidProblemDetails.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this LusidProblemDetails.


        :param instance: The instance of this LusidProblemDetails.  # noqa: E501
        :type: str
        """

        self._instance = instance

    @property
    def extensions(self):
        """Gets the extensions of this LusidProblemDetails.  # noqa: E501


        :return: The extensions of this LusidProblemDetails.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this LusidProblemDetails.


        :param extensions: The extensions of this LusidProblemDetails.  # noqa: E501
        :type: dict(str, object)
        """

        self._extensions = extensions

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LusidProblemDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
