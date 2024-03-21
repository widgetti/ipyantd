import playwright.sync_api
from IPython.display import display


def test_antd_in_jupyter(ipywidgets_runner, page_session: playwright.sync_api.Page, assert_solara_snapshot):
    def kernel_code():
        import ipyantd.widgets as antd

        # this is not ideal, we need the button to want on the library somehow
        # import time
        # time.sleep(2)
        def click_handler(*event):
            b.children = ["Clicked"]

        b = antd.Button(children=["Click me"], events={"onClick": click_handler})
        display(b)

    ipywidgets_runner(kernel_code)
    button = page_session.locator("button >> text=Click me")
    button.click()
    button = page_session.locator("button >> text=Clicked")
    button.wait_for()
    page_session.wait_for_timeout(500)  # let animations play out
    assert_solara_snapshot(button.screenshot())
