import json
from typing import List, Optional

from beartype import beartype

from flet import padding
from flet.constrained_control import ConstrainedControl
from flet.control import Control, OptionalNumber, PaddingValue
from flet.embed_json_encoder import EmbedJsonEncoder
from flet.ref import Ref


class GridView(ConstrainedControl):
    def __init__(
        self,
        controls: List[Control] = None,
        ref: Ref = None,
        width: OptionalNumber = None,
        height: OptionalNumber = None,
        expand: int = None,
        opacity: OptionalNumber = None,
        visible: bool = None,
        disabled: bool = None,
        data: any = None,
        #
        # Specific
        #
        horizontal: bool = None,
        runs_count: int = None,
        spacing: OptionalNumber = None,
        run_spacing: OptionalNumber = None,
        padding: PaddingValue = None,
    ):
        ConstrainedControl.__init__(
            self,
            ref=ref,
            width=width,
            height=height,
            expand=expand,
            opacity=opacity,
            visible=visible,
            disabled=disabled,
            data=data,
        )

        self.__controls: List[Control] = []
        self.controls = controls
        self.horizontal = horizontal
        self.runs_count = runs_count
        self.spacing = spacing
        self.run_spacing = run_spacing
        self.padding = padding

    def _get_control_name(self):
        return "gridview"

    def _get_children(self):
        return self.__controls

    # horizontal
    @property
    def horizontal(self):
        return self._get_attr("horizontal")

    @horizontal.setter
    @beartype
    def horizontal(self, value: Optional[bool]):
        self._set_attr("horizontal", value)

    # runs_count
    @property
    def runs_count(self):
        return self._get_attr("runsCount")

    @runs_count.setter
    @beartype
    def runs_count(self, value: Optional[int]):
        self._set_attr("runsCount", value)

    # spacing
    @property
    def spacing(self):
        return self._get_attr("spacing")

    @spacing.setter
    @beartype
    def spacing(self, value: OptionalNumber):
        self._set_attr("spacing", value)

    # run_spacing
    @property
    def run_spacing(self):
        return self._get_attr("runSpacing")

    @run_spacing.setter
    @beartype
    def run_spacing(self, value: OptionalNumber):
        self._set_attr("runSpacing", value)

    # padding
    @property
    def padding(self):
        return self.__padding

    @padding.setter
    @beartype
    def padding(self, value: PaddingValue):
        self.__padding = value
        if value and isinstance(value, (int, float)):
            value = padding.all(value)
        self._set_attr(
            "padding", json.dumps(value, cls=EmbedJsonEncoder) if value else None
        )

    # controls
    @property
    def controls(self):
        return self.__controls

    @controls.setter
    def controls(self, value):
        self.__controls = value or []
