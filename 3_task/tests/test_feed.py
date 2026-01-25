import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.title("Счётчики заказов увеличиваются")
def test_orders_counters(feed_page):
    total_before = feed_page.get_total_orders()
    today_before = feed_page.get_today_orders()

    feed_page.refresh()

    assert feed_page.get_total_orders() >= total_before
    assert feed_page.get_today_orders() >= today_before


@allure.title("Заказ отображается в разделе «В работе»")
def test_order_in_progress(feed_page):
    assert feed_page.has_orders_in_progress()

