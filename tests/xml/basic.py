import sys
import asyncio
import os

sys.path.append("..")
sys.path.append(os.getcwd())
import testrunner
import lvgl as lv  # noqa

# This is a basic UI XML test.


async def demo(scr, display=None):
    # display.debug_display(True)
    red_button_xml = """
        <component>
          <api>
            <prop name="button_text" type="string" default="None"/>
          </api>
          <view extends="lv_button" radius="0" style_bg_color="0xa91500">
            <lv_label text="$button_text" align="center"/>
          </view>
        </component>
    """
    lv.xml_init()
    lv.xml_component_register_from_data("red_button", red_button_xml)
    red_button = lv.xml_create(scr, "red_button", None)
    rb = scr.get_child_by_name("red_button")

    def button_cb(event, name):
        print(f"{name} PRESSED")

    rb.add_event_cb(
        lambda event, button_name="red_button": button_cb(event, button_name),
        lv.EVENT.CLICKED,
        None,
    )

    await asyncio.sleep_ms(500)  # await so the frame can be rendered

    await asyncio.sleep_ms(200)
    print("EVENT TEST:")
    rb.send_event(lv.EVENT.CLICKED, None)
    _rst = lv.obj()
    # lv.screen_load(_rst)
    while True:
        for i in range(10):
            await asyncio.sleep_ms(200)
    # lv.screen_load(scr)
    await asyncio.sleep_ms(2000)


__file__ = globals().get("__file__", "test")

try:
    import display_config

    display_config.MODE = "interactive"
    display_config.POINTER = "interactive"
    display_config.SHOW_INFO = False
except Exception:
    display_config = testrunner.display_config

testrunner.run(demo, __file__, disp_config=display_config)
testrunner.devicereset()
