from pydantic import BaseModel, Field, ConfigDict, EmailStr
from enum import StrEnum
from tools.fakers import fake


class OperationType(StrEnum):
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций по счёту.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения сводки по операциям счёта.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class MakeOperationRequestSchema(BaseModel):
    """
    Базовая структура данных для выполнения операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: int | float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для выполнения операции списания комиссии."""


class MakeTopUpOperationsRequestSchema(MakeOperationRequestSchema):
    """Структура данных для выполнения операции пополнения счёта."""


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для выполнения операции начисления кэшбэка."""


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для выполнения операции перевода."""


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для выполнения операции покупки.
    """
    category: str = Field(default_factory=fake.category)


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для выполнения операции оплаты счёта."""


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """Структура данных для выполнения операции снятия наличных."""


class OperationSchema(BaseModel):
    """
    Описание структуры операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: int | float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """
    Описание структуры чека по операции.
    """
    url: str
    document: str


class OperationsSummarySchema(BaseModel):
    """
    Описание структуры сводки по операциям.
    """
    spent_amount: int | float = Field(alias="spentAmount")
    receive_amount: int | float = Field(alias="receivedAmount")
    cashback_amount: int | float = Field(alias="cashbackAmount")


class GetOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа получения операции.
    """
    operation: OperationSchema


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Описание структуры ответа получения чека по операции.
    """
    receipt: OperationReceiptSchema


class GetOperationsResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка операций.
    """
    operations: list[OperationStatus]


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Описание структуры ответа получения сводки по операциям.
    """
    summary: OperationsSummarySchema


class MakeFeeOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции списания комиссии.
    """
    operation: OperationSchema


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции пополнения счёта.
    """
    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции начисления кэшбэка.
    """
    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции перевода.
    """
    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции покупки.
    """
    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции оплаты счёта.
    """
    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Описание структуры ответа операции снятия наличных.
    """
    operation: OperationSchema
