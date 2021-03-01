# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.2665
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class VersionSummaryDto(object):
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
        'api_version': 'str',
        'build_version': 'str',
        'excel_version': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'build_version': 'buildVersion',
        'excel_version': 'excelVersion',
        'links': 'links'
    }

    required_map = {
        'api_version': 'optional',
        'build_version': 'optional',
        'excel_version': 'optional',
        'links': 'optional'
    }

    def __init__(self, api_version=None, build_version=None, excel_version=None, links=None):  # noqa: E501
        """
        VersionSummaryDto - a model defined in OpenAPI

        :param api_version: 
        :type api_version: str
        :param build_version: 
        :type build_version: str
        :param excel_version: 
        :type excel_version: str
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._api_version = None
        self._build_version = None
        self._excel_version = None
        self._links = None
        self.discriminator = None

        self.api_version = api_version
        self.build_version = build_version
        self.excel_version = excel_version
        self.links = links

    @property
    def api_version(self):
        """Gets the api_version of this VersionSummaryDto.  # noqa: E501


        :return: The api_version of this VersionSummaryDto.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this VersionSummaryDto.


        :param api_version: The api_version of this VersionSummaryDto.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def build_version(self):
        """Gets the build_version of this VersionSummaryDto.  # noqa: E501


        :return: The build_version of this VersionSummaryDto.  # noqa: E501
        :rtype: str
        """
        return self._build_version

    @build_version.setter
    def build_version(self, build_version):
        """Sets the build_version of this VersionSummaryDto.


        :param build_version: The build_version of this VersionSummaryDto.  # noqa: E501
        :type: str
        """

        self._build_version = build_version

    @property
    def excel_version(self):
        """Gets the excel_version of this VersionSummaryDto.  # noqa: E501


        :return: The excel_version of this VersionSummaryDto.  # noqa: E501
        :rtype: str
        """
        return self._excel_version

    @excel_version.setter
    def excel_version(self, excel_version):
        """Sets the excel_version of this VersionSummaryDto.


        :param excel_version: The excel_version of this VersionSummaryDto.  # noqa: E501
        :type: str
        """

        self._excel_version = excel_version

    @property
    def links(self):
        """Gets the links of this VersionSummaryDto.  # noqa: E501


        :return: The links of this VersionSummaryDto.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this VersionSummaryDto.


        :param links: The links of this VersionSummaryDto.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if not isinstance(other, VersionSummaryDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
