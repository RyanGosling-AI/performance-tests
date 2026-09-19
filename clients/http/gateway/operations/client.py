from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций по счёту.
    """
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения сводки по операциям счёта.
    """
    accountId: str


class MakeFeeOperationRequestDict(TypedDict):
    """
    Структура данных для выполнения операции списания комиссии.
    """
    status: str
    amount: int | float
    cardId: str
    accountId: str


class MakeTopUpOperationsRequestDict(TypedDict):
    """
    Структура данных для выполнения операции пополнения счёта.
    """
    status: str
    amount: int | float
    cardId: str
    accountId: str


class MakeCashbackOperationRequestDict(TypedDict):
    """
    Структура данных для выполнения операции начисления кэшбэка.
    """
    status: str
    amount: int | float
    cardId: str
    accountId: str


class MakeTransferOperationRequestDict(TypedDict):
    """
    Структура данных для выполнения операции перевода.
    """
    status: str
    amount: int | float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(MakeTransferOperationRequestDict):
    """
    Структура данных для выполнения операции покупки.
    """
    category: str


class MakeBillPaymentOperationRequestDict(TypedDict):
    """
    Структура данных для выполнения операции оплаты счёта.
    """
    status: str
    amount: int | float
    cardId: str
    accountId: str


class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """
    Структура данных для выполнения операции снятия наличных.
    """
    status: str
    amount: int | float
    cardId: str
    accountId: str


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Получить данные операции по её идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.get(f'/api/v1/operations/{operation_id}')

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Получить чек по операции по её идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.get(f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Получить список операций по счёту.

        :param query: Словарь с параметрами запроса.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.get('/api/v1/operations', params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Получить сводку по операциям счёта.

        :param query: Словарь с параметрами запроса.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.get('/api/v1/operations/operations-summary', params=QueryParams(**query))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Выполнить операцию списания комиссии.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.post('/api/v1/operations/make-fee-operation', json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationsRequestDict) -> Response:
        """
        Выполнить операцию пополнения счёта.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.post('/api/v1/operations/make-top-up-operation', json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполнить операцию начисления кэшбэка.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.post('/api/v1/operations/make-cashback-operation', json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        Выполнить операцию перевода.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.post('/api/v1/operations/make-transfer-operation', json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполнить операцию покупки.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.post('/api/v1/operations/make-purchase-operation', json=request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполнить операцию оплаты счёта.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.post('/api/v1/operations/make-bill-payment-operation', json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполнить операцию снятия наличных.

        :param request: Словарь с данными операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.client.post('/api/v1/operations/make-cash-withdrawal-operation', json=request)
