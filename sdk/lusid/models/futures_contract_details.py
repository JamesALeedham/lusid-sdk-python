# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.0.485
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


class FuturesContractDetails(object):
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
        'dom_ccy': 'str',
        'fgn_ccy': 'str',
        'asset_class': 'str',
        'contract_code': 'str',
        'contract_month': 'str',
        'contract_size': 'float',
        'convention': 'str',
        'country': 'str',
        'description': 'str',
        'exchange_code': 'str',
        'exchange_name': 'str',
        'ticker_step': 'float',
        'unit_value': 'float',
        'calendars': 'list[str]'
    }

    attribute_map = {
        'dom_ccy': 'domCcy',
        'fgn_ccy': 'fgnCcy',
        'asset_class': 'assetClass',
        'contract_code': 'contractCode',
        'contract_month': 'contractMonth',
        'contract_size': 'contractSize',
        'convention': 'convention',
        'country': 'country',
        'description': 'description',
        'exchange_code': 'exchangeCode',
        'exchange_name': 'exchangeName',
        'ticker_step': 'tickerStep',
        'unit_value': 'unitValue',
        'calendars': 'calendars'
    }

    required_map = {
        'dom_ccy': 'required',
        'fgn_ccy': 'optional',
        'asset_class': 'optional',
        'contract_code': 'required',
        'contract_month': 'required',
        'contract_size': 'required',
        'convention': 'optional',
        'country': 'optional',
        'description': 'optional',
        'exchange_code': 'required',
        'exchange_name': 'optional',
        'ticker_step': 'optional',
        'unit_value': 'optional',
        'calendars': 'optional'
    }

    def __init__(self, dom_ccy=None, fgn_ccy=None, asset_class=None, contract_code=None, contract_month=None, contract_size=None, convention=None, country=None, description=None, exchange_code=None, exchange_name=None, ticker_step=None, unit_value=None, calendars=None, local_vars_configuration=None):  # noqa: E501
        """FuturesContractDetails - a model defined in OpenAPI"
        
        :param dom_ccy:  Currency in which the contract is paid. (required)
        :type dom_ccy: str
        :param fgn_ccy:  Currency of the underlying, for use with FX Futures
        :type fgn_ccy: str
        :param asset_class:  The asset class of the underlying. Optional and will default to Unknown if not set.    Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money].
        :type asset_class: str
        :param contract_code:  The contract code used by the exchange, e.g. “CL” for Crude Oil, “ES” for E-mini SP 500, “FGBL” for Bund Futures, etc. (required)
        :type contract_code: str
        :param contract_month:  Which month does the contract trade for.    Supported string (enumeration) values are: [F, G, H, J, K, M, N, Q, U, V, X, Z]. (required)
        :type contract_month: str
        :param contract_size:  Size of a single contract. (required)
        :type contract_size: float
        :param convention:  If appropriate, the day count convention method used in pricing (rates futures).  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM].
        :type convention: str
        :param country:  Country (code) for the exchange.
        :type country: str
        :param description:  Description of contract.
        :type description: str
        :param exchange_code:  Exchange code for contract. This can be any string to uniquely identify the exchange (e.g. Exchange Name, MIC, BBG code). (required)
        :type exchange_code: str
        :param exchange_name:  Exchange name (for when code is not automatically recognised).
        :type exchange_name: str
        :param ticker_step:  Minimal step size change in ticker.
        :type ticker_step: float
        :param unit_value:  The value in the currency of a 1 unit change in the contract price.
        :type unit_value: float
        :param calendars:  Holiday calendars that apply to yield-to-price conversions (i.e. for BRL futures).
        :type calendars: list[str]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._dom_ccy = None
        self._fgn_ccy = None
        self._asset_class = None
        self._contract_code = None
        self._contract_month = None
        self._contract_size = None
        self._convention = None
        self._country = None
        self._description = None
        self._exchange_code = None
        self._exchange_name = None
        self._ticker_step = None
        self._unit_value = None
        self._calendars = None
        self.discriminator = None

        self.dom_ccy = dom_ccy
        self.fgn_ccy = fgn_ccy
        self.asset_class = asset_class
        self.contract_code = contract_code
        self.contract_month = contract_month
        self.contract_size = contract_size
        self.convention = convention
        self.country = country
        self.description = description
        self.exchange_code = exchange_code
        self.exchange_name = exchange_name
        if ticker_step is not None:
            self.ticker_step = ticker_step
        if unit_value is not None:
            self.unit_value = unit_value
        self.calendars = calendars

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this FuturesContractDetails.  # noqa: E501

        Currency in which the contract is paid.  # noqa: E501

        :return: The dom_ccy of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this FuturesContractDetails.

        Currency in which the contract is paid.  # noqa: E501

        :param dom_ccy: The dom_ccy of this FuturesContractDetails.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def fgn_ccy(self):
        """Gets the fgn_ccy of this FuturesContractDetails.  # noqa: E501

        Currency of the underlying, for use with FX Futures  # noqa: E501

        :return: The fgn_ccy of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._fgn_ccy

    @fgn_ccy.setter
    def fgn_ccy(self, fgn_ccy):
        """Sets the fgn_ccy of this FuturesContractDetails.

        Currency of the underlying, for use with FX Futures  # noqa: E501

        :param fgn_ccy: The fgn_ccy of this FuturesContractDetails.  # noqa: E501
        :type fgn_ccy: str
        """

        self._fgn_ccy = fgn_ccy

    @property
    def asset_class(self):
        """Gets the asset_class of this FuturesContractDetails.  # noqa: E501

        The asset class of the underlying. Optional and will default to Unknown if not set.    Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money].  # noqa: E501

        :return: The asset_class of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._asset_class

    @asset_class.setter
    def asset_class(self, asset_class):
        """Sets the asset_class of this FuturesContractDetails.

        The asset class of the underlying. Optional and will default to Unknown if not set.    Supported string (enumeration) values are: [InterestRates, FX, Inflation, Equities, Credit, Commodities, Money].  # noqa: E501

        :param asset_class: The asset_class of this FuturesContractDetails.  # noqa: E501
        :type asset_class: str
        """

        self._asset_class = asset_class

    @property
    def contract_code(self):
        """Gets the contract_code of this FuturesContractDetails.  # noqa: E501

        The contract code used by the exchange, e.g. “CL” for Crude Oil, “ES” for E-mini SP 500, “FGBL” for Bund Futures, etc.  # noqa: E501

        :return: The contract_code of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._contract_code

    @contract_code.setter
    def contract_code(self, contract_code):
        """Sets the contract_code of this FuturesContractDetails.

        The contract code used by the exchange, e.g. “CL” for Crude Oil, “ES” for E-mini SP 500, “FGBL” for Bund Futures, etc.  # noqa: E501

        :param contract_code: The contract_code of this FuturesContractDetails.  # noqa: E501
        :type contract_code: str
        """
        if self.local_vars_configuration.client_side_validation and contract_code is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                contract_code is not None and len(contract_code) < 1):
            raise ValueError("Invalid value for `contract_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._contract_code = contract_code

    @property
    def contract_month(self):
        """Gets the contract_month of this FuturesContractDetails.  # noqa: E501

        Which month does the contract trade for.    Supported string (enumeration) values are: [F, G, H, J, K, M, N, Q, U, V, X, Z].  # noqa: E501

        :return: The contract_month of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._contract_month

    @contract_month.setter
    def contract_month(self, contract_month):
        """Sets the contract_month of this FuturesContractDetails.

        Which month does the contract trade for.    Supported string (enumeration) values are: [F, G, H, J, K, M, N, Q, U, V, X, Z].  # noqa: E501

        :param contract_month: The contract_month of this FuturesContractDetails.  # noqa: E501
        :type contract_month: str
        """
        if self.local_vars_configuration.client_side_validation and contract_month is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_month`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                contract_month is not None and len(contract_month) < 1):
            raise ValueError("Invalid value for `contract_month`, length must be greater than or equal to `1`")  # noqa: E501

        self._contract_month = contract_month

    @property
    def contract_size(self):
        """Gets the contract_size of this FuturesContractDetails.  # noqa: E501

        Size of a single contract.  # noqa: E501

        :return: The contract_size of this FuturesContractDetails.  # noqa: E501
        :rtype: float
        """
        return self._contract_size

    @contract_size.setter
    def contract_size(self, contract_size):
        """Sets the contract_size of this FuturesContractDetails.

        Size of a single contract.  # noqa: E501

        :param contract_size: The contract_size of this FuturesContractDetails.  # noqa: E501
        :type contract_size: float
        """
        if self.local_vars_configuration.client_side_validation and contract_size is None:  # noqa: E501
            raise ValueError("Invalid value for `contract_size`, must not be `None`")  # noqa: E501

        self._contract_size = contract_size

    @property
    def convention(self):
        """Gets the convention of this FuturesContractDetails.  # noqa: E501

        If appropriate, the day count convention method used in pricing (rates futures).  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM].  # noqa: E501

        :return: The convention of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._convention

    @convention.setter
    def convention(self, convention):
        """Sets the convention of this FuturesContractDetails.

        If appropriate, the day count convention method used in pricing (rates futures).  For more information on day counts, see [knowledge base article KA-01798](https://support.lusid.com/knowledgebase/article/KA-01798)                Supported string (enumeration) values are: [Actual360, Act360, MoneyMarket, Actual365, Act365, Thirty360, ThirtyU360, Bond, ThirtyE360, EuroBond, ActualActual, ActAct, ActActIsda, ActActIsma, ActActIcma, OneOne, Act364, Act365F, Act365L, Act365_25, Act252, Bus252, NL360, NL365, ActActAFB, Act365Cad, ThirtyActIsda, Thirty365Isda, ThirtyEActIsda, ThirtyE360Isda, ThirtyE365Isda, ThirtyU360EOM].  # noqa: E501

        :param convention: The convention of this FuturesContractDetails.  # noqa: E501
        :type convention: str
        """

        self._convention = convention

    @property
    def country(self):
        """Gets the country of this FuturesContractDetails.  # noqa: E501

        Country (code) for the exchange.  # noqa: E501

        :return: The country of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this FuturesContractDetails.

        Country (code) for the exchange.  # noqa: E501

        :param country: The country of this FuturesContractDetails.  # noqa: E501
        :type country: str
        """

        self._country = country

    @property
    def description(self):
        """Gets the description of this FuturesContractDetails.  # noqa: E501

        Description of contract.  # noqa: E501

        :return: The description of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FuturesContractDetails.

        Description of contract.  # noqa: E501

        :param description: The description of this FuturesContractDetails.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def exchange_code(self):
        """Gets the exchange_code of this FuturesContractDetails.  # noqa: E501

        Exchange code for contract. This can be any string to uniquely identify the exchange (e.g. Exchange Name, MIC, BBG code).  # noqa: E501

        :return: The exchange_code of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._exchange_code

    @exchange_code.setter
    def exchange_code(self, exchange_code):
        """Sets the exchange_code of this FuturesContractDetails.

        Exchange code for contract. This can be any string to uniquely identify the exchange (e.g. Exchange Name, MIC, BBG code).  # noqa: E501

        :param exchange_code: The exchange_code of this FuturesContractDetails.  # noqa: E501
        :type exchange_code: str
        """
        if self.local_vars_configuration.client_side_validation and exchange_code is None:  # noqa: E501
            raise ValueError("Invalid value for `exchange_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                exchange_code is not None and len(exchange_code) < 1):
            raise ValueError("Invalid value for `exchange_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._exchange_code = exchange_code

    @property
    def exchange_name(self):
        """Gets the exchange_name of this FuturesContractDetails.  # noqa: E501

        Exchange name (for when code is not automatically recognised).  # noqa: E501

        :return: The exchange_name of this FuturesContractDetails.  # noqa: E501
        :rtype: str
        """
        return self._exchange_name

    @exchange_name.setter
    def exchange_name(self, exchange_name):
        """Sets the exchange_name of this FuturesContractDetails.

        Exchange name (for when code is not automatically recognised).  # noqa: E501

        :param exchange_name: The exchange_name of this FuturesContractDetails.  # noqa: E501
        :type exchange_name: str
        """

        self._exchange_name = exchange_name

    @property
    def ticker_step(self):
        """Gets the ticker_step of this FuturesContractDetails.  # noqa: E501

        Minimal step size change in ticker.  # noqa: E501

        :return: The ticker_step of this FuturesContractDetails.  # noqa: E501
        :rtype: float
        """
        return self._ticker_step

    @ticker_step.setter
    def ticker_step(self, ticker_step):
        """Sets the ticker_step of this FuturesContractDetails.

        Minimal step size change in ticker.  # noqa: E501

        :param ticker_step: The ticker_step of this FuturesContractDetails.  # noqa: E501
        :type ticker_step: float
        """

        self._ticker_step = ticker_step

    @property
    def unit_value(self):
        """Gets the unit_value of this FuturesContractDetails.  # noqa: E501

        The value in the currency of a 1 unit change in the contract price.  # noqa: E501

        :return: The unit_value of this FuturesContractDetails.  # noqa: E501
        :rtype: float
        """
        return self._unit_value

    @unit_value.setter
    def unit_value(self, unit_value):
        """Sets the unit_value of this FuturesContractDetails.

        The value in the currency of a 1 unit change in the contract price.  # noqa: E501

        :param unit_value: The unit_value of this FuturesContractDetails.  # noqa: E501
        :type unit_value: float
        """

        self._unit_value = unit_value

    @property
    def calendars(self):
        """Gets the calendars of this FuturesContractDetails.  # noqa: E501

        Holiday calendars that apply to yield-to-price conversions (i.e. for BRL futures).  # noqa: E501

        :return: The calendars of this FuturesContractDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._calendars

    @calendars.setter
    def calendars(self, calendars):
        """Sets the calendars of this FuturesContractDetails.

        Holiday calendars that apply to yield-to-price conversions (i.e. for BRL futures).  # noqa: E501

        :param calendars: The calendars of this FuturesContractDetails.  # noqa: E501
        :type calendars: list[str]
        """

        self._calendars = calendars

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
        if not isinstance(other, FuturesContractDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FuturesContractDetails):
            return True

        return self.to_dict() != other.to_dict()
