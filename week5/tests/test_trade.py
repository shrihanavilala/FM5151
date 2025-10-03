from unittest import mock

from trade import AlwaysBuyStrategy, Broker, TradingStrategy


class FakeBroker(Broker):
    """
    Test double broker to assist in testing. We can use this as a mock or
    stub.
    """

    def __init__(self) -> None:
        self.orders = []

    def post_order(self, order: str) -> None:
        self.orders.append(order)


class TestTradingStrategy:
    def test_on_data_saves_results(self):
        """Example test that tests state changes"""
        broker = FakeBroker()
        strategy = TradingStrategy(broker)

        strategy.on_data(123)
        assert strategy.history == [123]

    def test_submit_order_posts_to_broker(self):
        """Example test that tests interactions between components"""
        broker = FakeBroker()
        strategy = TradingStrategy(broker)

        order = "My order"
        strategy.post_order(order)
        # Ensure broker received data we meant to send
        assert broker.orders == [order]

    def test_submit_order_posts_to_broker_magic_mock(self):
        """Example test that tests interactions between components using a mock"""
        broker = mock.create_autospec(Broker)
        strategy = TradingStrategy(broker)

        order = "My order"
        strategy.post_order(order)
        # Ensure broker received data we meant to send
        broker.post_order.assert_called_with(order)

        # This would fail
        # broker.post_order.assert_called_with("Not my order")


class TestAlwaysBuyStrategy:
    def test_signal_is_always_buy(self):
        """Example test that tests output from function"""
        broker = FakeBroker()
        strategy = AlwaysBuyStrategy(broker)
        assert strategy.compute_signal() == "BUY"
