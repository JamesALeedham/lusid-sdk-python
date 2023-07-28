# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.389
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class CdsProtectionDetailSpecification(object):
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
        'seniority': 'str',
        'restructuring_type': 'str',
        'protect_start_day': 'bool',
        'pay_accrued_interest_on_default': 'bool'
    }

    attribute_map = {
        'seniority': 'seniority',
        'restructuring_type': 'restructuringType',
        'protect_start_day': 'protectStartDay',
        'pay_accrued_interest_on_default': 'payAccruedInterestOnDefault'
    }

    required_map = {
        'seniority': 'required',
        'restructuring_type': 'required',
        'protect_start_day': 'required',
        'pay_accrued_interest_on_default': 'required'
    }

    def __init__(self, seniority=None, restructuring_type=None, protect_start_day=None, pay_accrued_interest_on_default=None, local_vars_configuration=None):  # noqa: E501
        """CdsProtectionDetailSpecification - a model defined in OpenAPI"
        
        :param seniority:  The seniority level of the CDS.    Supported string (enumeration) values are: [SNR, SUB, JRSUBUT2, PREFT1, SECDOM, SNRFOR, SUBLT2]. (required)
        :type seniority: str
        :param restructuring_type:  The restructuring clause.  Supported string (enumeration) values are: [CR, MR, MM, XR]. (required)
        :type restructuring_type: str
        :param protect_start_day:  Does the protection leg pay out in the case of default on the start date. (required)
        :type protect_start_day: bool
        :param pay_accrued_interest_on_default:  Should accrued interest on the premium leg be paid if a credit event occurs. (required)
        :type pay_accrued_interest_on_default: bool

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._seniority = None
        self._restructuring_type = None
        self._protect_start_day = None
        self._pay_accrued_interest_on_default = None
        self.discriminator = None

        self.seniority = seniority
        self.restructuring_type = restructuring_type
        self.protect_start_day = protect_start_day
        self.pay_accrued_interest_on_default = pay_accrued_interest_on_default

    @property
    def seniority(self):
        """Gets the seniority of this CdsProtectionDetailSpecification.  # noqa: E501

        The seniority level of the CDS.    Supported string (enumeration) values are: [SNR, SUB, JRSUBUT2, PREFT1, SECDOM, SNRFOR, SUBLT2].  # noqa: E501

        :return: The seniority of this CdsProtectionDetailSpecification.  # noqa: E501
        :rtype: str
        """
        return self._seniority

    @seniority.setter
    def seniority(self, seniority):
        """Sets the seniority of this CdsProtectionDetailSpecification.

        The seniority level of the CDS.    Supported string (enumeration) values are: [SNR, SUB, JRSUBUT2, PREFT1, SECDOM, SNRFOR, SUBLT2].  # noqa: E501

        :param seniority: The seniority of this CdsProtectionDetailSpecification.  # noqa: E501
        :type seniority: str
        """
        if self.local_vars_configuration.client_side_validation and seniority is None:  # noqa: E501
            raise ValueError("Invalid value for `seniority`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                seniority is not None and len(seniority) < 1):
            raise ValueError("Invalid value for `seniority`, length must be greater than or equal to `1`")  # noqa: E501

        self._seniority = seniority

    @property
    def restructuring_type(self):
        """Gets the restructuring_type of this CdsProtectionDetailSpecification.  # noqa: E501

        The restructuring clause.  Supported string (enumeration) values are: [CR, MR, MM, XR].  # noqa: E501

        :return: The restructuring_type of this CdsProtectionDetailSpecification.  # noqa: E501
        :rtype: str
        """
        return self._restructuring_type

    @restructuring_type.setter
    def restructuring_type(self, restructuring_type):
        """Sets the restructuring_type of this CdsProtectionDetailSpecification.

        The restructuring clause.  Supported string (enumeration) values are: [CR, MR, MM, XR].  # noqa: E501

        :param restructuring_type: The restructuring_type of this CdsProtectionDetailSpecification.  # noqa: E501
        :type restructuring_type: str
        """
        if self.local_vars_configuration.client_side_validation and restructuring_type is None:  # noqa: E501
            raise ValueError("Invalid value for `restructuring_type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                restructuring_type is not None and len(restructuring_type) < 1):
            raise ValueError("Invalid value for `restructuring_type`, length must be greater than or equal to `1`")  # noqa: E501

        self._restructuring_type = restructuring_type

    @property
    def protect_start_day(self):
        """Gets the protect_start_day of this CdsProtectionDetailSpecification.  # noqa: E501

        Does the protection leg pay out in the case of default on the start date.  # noqa: E501

        :return: The protect_start_day of this CdsProtectionDetailSpecification.  # noqa: E501
        :rtype: bool
        """
        return self._protect_start_day

    @protect_start_day.setter
    def protect_start_day(self, protect_start_day):
        """Sets the protect_start_day of this CdsProtectionDetailSpecification.

        Does the protection leg pay out in the case of default on the start date.  # noqa: E501

        :param protect_start_day: The protect_start_day of this CdsProtectionDetailSpecification.  # noqa: E501
        :type protect_start_day: bool
        """
        if self.local_vars_configuration.client_side_validation and protect_start_day is None:  # noqa: E501
            raise ValueError("Invalid value for `protect_start_day`, must not be `None`")  # noqa: E501

        self._protect_start_day = protect_start_day

    @property
    def pay_accrued_interest_on_default(self):
        """Gets the pay_accrued_interest_on_default of this CdsProtectionDetailSpecification.  # noqa: E501

        Should accrued interest on the premium leg be paid if a credit event occurs.  # noqa: E501

        :return: The pay_accrued_interest_on_default of this CdsProtectionDetailSpecification.  # noqa: E501
        :rtype: bool
        """
        return self._pay_accrued_interest_on_default

    @pay_accrued_interest_on_default.setter
    def pay_accrued_interest_on_default(self, pay_accrued_interest_on_default):
        """Sets the pay_accrued_interest_on_default of this CdsProtectionDetailSpecification.

        Should accrued interest on the premium leg be paid if a credit event occurs.  # noqa: E501

        :param pay_accrued_interest_on_default: The pay_accrued_interest_on_default of this CdsProtectionDetailSpecification.  # noqa: E501
        :type pay_accrued_interest_on_default: bool
        """
        if self.local_vars_configuration.client_side_validation and pay_accrued_interest_on_default is None:  # noqa: E501
            raise ValueError("Invalid value for `pay_accrued_interest_on_default`, must not be `None`")  # noqa: E501

        self._pay_accrued_interest_on_default = pay_accrued_interest_on_default

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CdsProtectionDetailSpecification):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CdsProtectionDetailSpecification):
            return True

        return self.to_dict() != other.to_dict()
