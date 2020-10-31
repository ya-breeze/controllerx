import pytest
from cx_devices.aqara import (
    MFKZQ01LMLightController,
    WXKG01LMLightController,
    WXKG11LMLightController,
)


@pytest.mark.parametrize(
    "data, expected_action",
    [
        ({"command": "shake"}, "shake"),
        ({"command": "knock"}, "knock"),
        ({"command": "slide"}, "slide"),
        ({"command": "flip", "args": {"flip_degrees": 90}}, "flip90"),
        ({"command": "flip", "args": {"flip_degrees": 180}}, "flip180"),
        ({"command": "rotate_left"}, "rotate_left"),
        ({"command": "rotate_right"}, "rotate_right"),
    ],
)
def test_zha_action_MFKZQ01LMLightController(data, expected_action):
    sut = MFKZQ01LMLightController()  # type: ignore
    action = sut.get_zha_action(data)
    assert action == expected_action


@pytest.mark.parametrize(
    "data, expected_action",
    [
        ({"command": "click", "args": {"click_type": "single"}}, "single"),
        ({"command": "click", "args": {"click_type": "double"}}, "double"),
        ({"command": "click", "args": {"click_type": "triple"}}, "triple"),
        ({"command": "click", "args": {"click_type": "quadruple"}}, "quadruple"),
        ({"command": "click", "args": {"click_type": "furious"}}, "furious"),
    ],
)
def test_zha_action_WXKG01LMLightController(data, expected_action):
    sut = WXKG01LMLightController()  # type: ignore
    action = sut.get_zha_action(data)
    assert action == expected_action


@pytest.mark.parametrize(
    "data, expected_action",
    [
        ({"args": {"value": 0}}, ""),
        ({"args": {"value": 1}}, "single"),
        ({"args": {"value": 2}}, "double"),
        ({"args": {"value": 3}}, "triple"),
        ({"args": {"value": 4}}, "quadruple"),
    ],
)
def test_zha_action_WXKG11LMLightController(data, expected_action):
    sut = WXKG11LMLightController()
    action = sut.get_zha_action(data)
    assert action == expected_action
