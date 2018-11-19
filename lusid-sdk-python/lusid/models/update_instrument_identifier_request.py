# coding=utf-8
# --------------------------------------------------------------------------
# Copyright © 2018 FINBOURNE TECHNOLOGY LTD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UpdateInstrumentIdentifierRequest(Model):
    """UpdateInstrumentIdentifierRequest.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: Possible values include: 'Undefined', 'LusidInstrumentId',
     'ReutersAssetId', 'CINS', 'Isin', 'Sedol', 'Cusip', 'Ticker',
     'ClientInternal', 'Figi', 'CompositeFigi', 'ShareClassFigi', 'Wertpapier'
    :vartype type: str or ~lusid.models.enum
    :ivar value:
    :vartype value: str
    :ivar effective_from:
    :vartype effective_from: datetime
    """

    _validation = {
        'type': {'readonly': True},
        'value': {'readonly': True},
        'effective_from': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'effective_from': {'key': 'effectiveFrom', 'type': 'iso-8601'},
    }

    def __init__(self):
        super(UpdateInstrumentIdentifierRequest, self).__init__()
        self.type = None
        self.value = None
        self.effective_from = None
