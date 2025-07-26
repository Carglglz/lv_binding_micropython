import sys
import asyncio
import os

sys.path.append("..")
sys.path.append(os.getcwd())
import testrunner
import lvgl as lv  # noqa

XML_FILE = sys.argv.pop()
if not XML_FILE.endswith(".xml"):
    XML_FILE = "button.xml"


# This is a basic UI XML test.
print(f"PREVIEW: {XML_FILE}")


async def demo(scr, display=None):
    # display.debug_display(True)
    scr.set_style_bg_color(lv.color_white(), 0)
    with open(XML_FILE, "r") as xmlf:
        xml_data = xmlf.read()
    print("#" * 50)
    print(xml_data)
    print("#" * 50)
    lv.xml_init()
    lv.xml_component_register_from_data("xml_comp", xml_data)
    res = lv.xml_create(scr, "xml_comp", None)
    xml_comp = scr.get_child_by_name("xml_comp")

    while True:
        await asyncio.sleep_ms(200)


__file__ = globals().get("__file__", "test")

try:
    import display_config

    display_config.MODE = "interactive"
    display_config.POINTER = "interactive"
    display_config.WIDTH = 720
    display_config.HEIGHT = 480
    display_config.SHOW_INFO = True
except Exception:
    display_config = testrunner.display_config

testrunner.run(demo, __file__, disp_config=display_config)
testrunner.devicereset()
