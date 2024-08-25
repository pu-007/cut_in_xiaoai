import voicemeeterlib
import modules

vm = voicemeeterlib.api("potato")
vm.login()

keyboard = modules.Keyboard()


def is_PC():
    return __import__("screeninfo").get_monitors()[0].width == 2560


def MonitorHook(mode: str):
    ### resize IM
    from subprocess import call

    call(["taskkill", "/IM", "Yzime_UIA.exe", "/F"])

    ### kill zebar.exe, and run C:\Users\Administrator\.glzr\zebar\start.bat
    from screeninfo import get_monitors
    from ruamel.yaml import YAML

    yaml = YAML()
    yaml.preserve_quotes = True

    call(["taskkill", "/IM", "zebar.exe", "/F"])
    call([r"C:\Users\Administrator\.glzr\zebar\start.bat"])

    config = open(r"C:\Users\Administrator\.glzr\glazewm\config.yaml", "r")
    yaml_data = yaml.load(config)
    config.close()
    yaml_data["gaps"]["outer_gap"]["top"] = "3%" if is_PC() else "5%"
    config = open(r"C:\Users\Administrator\.glzr\glazewm\config.yaml", "w")
    yaml.dump(yaml_data, config)
    config.close()
    keyboard.redraw()

    #### voice meeter
    vm.bus[0].device.wdm = (
        "音响 (NVIDIA High Definition Audio)"
        if is_PC()
        else "Coocaa TV (NVIDIA High Definition Audio)"
    )


if __name__ == "__main__":
    MonitorHook("test")
