"""
This module contains the definition of a Homebank transaction.

See the documentation at http://homebank.free.fr/help/misc-csvformat.html
for details.
"""

from dataclasses import dataclass, field
from datetime import date
from enum import IntEnum
from typing import List


class PaymentType(IntEnum):
    """Available Homebank payment types."""
    NONE = 0
    CREDIT_CARD = 1
    CHECK = 2
    CASH = 3
    BANK_TRANSFER = 4
    INTERNAL_TRANSFER = 5
    DEBIT_CARD = 6
    STANDING_ORDER = 7
    ELECTRONIC_PAYMENT = 8
    DEPOSIT = 9
    FINANCIAL_INSTITUTION_FEE = 10
    DIRECT_DEBIT = 11


@dataclass
class Transaction:
    """Representation of a Homebank transaction."""
    date: date
    payment: PaymentType
    info: str
    payee: str
    memo: str
    amount: float
    category: str = ""
    tags: List[str] = field(default_factory=list)
