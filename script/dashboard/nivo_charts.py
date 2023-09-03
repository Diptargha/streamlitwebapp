import json

from streamlit_elements import nivo, mui
from script.dashboard.dashboard import Dashboard


class Pie(Dashboard.Item):
    DEFAULT_DATA = [
        {"id": "java", "label": "java", "value": 465, "color": "hsl(128, 70%, 50%)"},
        {"id": "rust", "label": "rust", "value": 140, "color": "hsl(178, 70%, 50%)"},
        {"id": "scala", "label": "scala", "value": 40, "color": "hsl(322, 70%, 50%)"},
        {"id": "ruby", "label": "ruby", "value": 439, "color": "hsl(117, 70%, 50%)"},
        {"id": "elixir", "label": "elixir", "value": 366, "color": "hsl(286, 70%, 50%)"}
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._theme = {
            "dark": {
                "background": "#252526",
                "textColor": "#FAFAFA",
                "tooltip": {
                    "container": {
                        "background": "#3F3F3F",
                        "color": "FAFAFA",
                    }
                }
            },
            "light": {
                "background": "#FFFFFF",
                "textColor": "#31333F",
                "tooltip": {
                    "container": {
                        "background": "#FFFFFF",
                        "color": "#31333F",
                    }
                }
            }
        }

    def __call__(self, json_data):
        try:
            data = json.loads(json_data)
        except json.JSONDecodeError:
            data = self.DEFAULT_DATA

        with mui.Paper(key=self._key,
                       sx={"display": "flex", "flexDirection": "column", "borderRadius": 3,
                           "overflow": "hidden"}, elevation=1):
            with self.title_bar():
                mui.icon.PieChart()
                mui.Typography("Pie chart", sx={"flex": 1})

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                nivo.Pie(
                    data=data,
                    theme=self._theme["dark" if self._dark_mode else "light"],
                    margin={"top": 40, "right": 80, "bottom": 80, "left": 80},
                    innerRadius=0.5,
                    padAngle=0.7,
                    cornerRadius=3,
                    activeOuterRadiusOffset=8,
                    borderWidth=1,
                    borderColor={
                        "from": "color",
                        "modifiers": [
                            [
                                "darker",
                                0.2,
                            ]
                        ]
                    },
                    arcLinkLabelsSkipAngle=10,
                    arcLinkLabelsTextColor="grey",
                    arcLinkLabelsThickness=2,
                    arcLinkLabelsColor={"from": "color"},
                    arcLabelsSkipAngle=10,
                    arcLabelsTextColor={
                        "from": "color",
                        "modifiers": [
                            [
                                "darker",
                                2
                            ]
                        ]
                    },
                    defs=[
                        {
                            "id": "dots",
                            "type": "patternDots",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "size": 4,
                            "padding": 1,
                            "stagger": True
                        },
                        {
                            "id": "lines",
                            "type": "patternLines",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "rotation": -45,
                            "lineWidth": 6,
                            "spacing": 10
                        }
                    ],
                    fill=[
                        {"match": {"id": "ruby"}, "id": "dots"},
                        {"match": {"id": "c"}, "id": "dots"},
                        {"match": {"id": "go"}, "id": "dots"},
                        {"match": {"id": "python"}, "id": "dots"},
                        {"match": {"id": "scala"}, "id": "lines"},
                        {"match": {"id": "lisp"}, "id": "lines"},
                        {"match": {"id": "elixir"}, "id": "lines"},
                        {"match": {"id": "javascript"}, "id": "lines"}
                    ],
                    legends=[
                        {
                            "anchor": "bottom",
                            "direction": "row",
                            "justify": False,
                            "translateX": 0,
                            "translateY": 56,
                            "itemsSpacing": 0,
                            "itemWidth": 100,
                            "itemHeight": 18,
                            "itemTextColor": "#999",
                            "itemDirection": "left-to-right",
                            "itemOpacity": 1,
                            "symbolSize": 18,
                            "symbolShape": "circle",
                            "effects": [
                                {
                                    "on": "hover",
                                    "style": {
                                        "itemTextColor": "#000"
                                    }
                                }
                            ]
                        }
                    ]
                )


class Line(Dashboard.Item):
    DEFAULT_DATA = [
        {
            "id": "japan",
            "color": "hsl(140, 70%, 50%)",
            "data": [
                {
                    "x": "plane",
                    "y": 78
                },
                {
                    "x": "helicopter",
                    "y": 33
                },
                {
                    "x": "boat",
                    "y": 153
                },
                {
                    "x": "train",
                    "y": 155
                },
                {
                    "x": "subway",
                    "y": 122
                },
                {
                    "x": "bus",
                    "y": 131
                },
                {
                    "x": "car",
                    "y": 149
                },
                {
                    "x": "moto",
                    "y": 79
                },
                {
                    "x": "bicycle",
                    "y": 92
                },
                {
                    "x": "horse",
                    "y": 204
                },
                {
                    "x": "skateboard",
                    "y": 118
                },
                {
                    "x": "others",
                    "y": 264
                }
            ]
        },
        {
            "id": "france",
            "color": "hsl(105, 70%, 50%)",
            "data": [
                {
                    "x": "plane",
                    "y": 279
                },
                {
                    "x": "helicopter",
                    "y": 17
                },
                {
                    "x": "boat",
                    "y": 108
                },
                {
                    "x": "train",
                    "y": 99
                },
                {
                    "x": "subway",
                    "y": 262
                },
                {
                    "x": "bus",
                    "y": 16
                },
                {
                    "x": "car",
                    "y": 254
                },
                {
                    "x": "moto",
                    "y": 239
                },
                {
                    "x": "bicycle",
                    "y": 107
                },
                {
                    "x": "horse",
                    "y": 108
                },
                {
                    "x": "skateboard",
                    "y": 246
                },
                {
                    "x": "others",
                    "y": 93
                }
            ]
        },
        {
            "id": "us",
            "color": "hsl(164, 70%, 50%)",
            "data": [
                {
                    "x": "plane",
                    "y": 248
                },
                {
                    "x": "helicopter",
                    "y": 24
                },
                {
                    "x": "boat",
                    "y": 56
                },
                {
                    "x": "train",
                    "y": 236
                },
                {
                    "x": "subway",
                    "y": 250
                },
                {
                    "x": "bus",
                    "y": 212
                },
                {
                    "x": "car",
                    "y": 169
                },
                {
                    "x": "moto",
                    "y": 129
                },
                {
                    "x": "bicycle",
                    "y": 300
                },
                {
                    "x": "horse",
                    "y": 194
                },
                {
                    "x": "skateboard",
                    "y": 218
                },
                {
                    "x": "others",
                    "y": 87
                }
            ]
        },
        {
            "id": "germany",
            "color": "hsl(340, 70%, 50%)",
            "data": [
                {
                    "x": "plane",
                    "y": 219
                },
                {
                    "x": "helicopter",
                    "y": 240
                },
                {
                    "x": "boat",
                    "y": 114
                },
                {
                    "x": "train",
                    "y": 68
                },
                {
                    "x": "subway",
                    "y": 22
                },
                {
                    "x": "bus",
                    "y": 24
                },
                {
                    "x": "car",
                    "y": 269
                },
                {
                    "x": "moto",
                    "y": 156
                },
                {
                    "x": "bicycle",
                    "y": 160
                },
                {
                    "x": "horse",
                    "y": 31
                },
                {
                    "x": "skateboard",
                    "y": 13
                },
                {
                    "x": "others",
                    "y": 80
                }
            ]
        },
        {
            "id": "norway",
            "color": "hsl(24, 70%, 50%)",
            "data": [
                {
                    "x": "plane",
                    "y": 29
                },
                {
                    "x": "helicopter",
                    "y": 42
                },
                {
                    "x": "boat",
                    "y": 217
                },
                {
                    "x": "train",
                    "y": 68
                },
                {
                    "x": "subway",
                    "y": 249
                },
                {
                    "x": "bus",
                    "y": 149
                },
                {
                    "x": "car",
                    "y": 48
                },
                {
                    "x": "moto",
                    "y": 155
                },
                {
                    "x": "bicycle",
                    "y": 270
                },
                {
                    "x": "horse",
                    "y": 25
                },
                {
                    "x": "skateboard",
                    "y": 168
                },
                {
                    "x": "others",
                    "y": 160
                }
            ]
        }
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._theme = {
            "dark": {
                "background": "#0f0f0f",
                "text": {
                    "fontSize": 11,
                    "fill": "#f3eded",
                    "outlineWidth": 0,
                    "outlineColor": "transparent",
                },
                "axis": {
                    "domain": {
                        "line": {
                            "stroke": "#777777",
                            "strokeWidth": 1,
                        }
                    },
                    "legend": {
                        "text": {
                            "fontSize": 12,
                            "fill": "#f5f5f5",
                            "outlineWidth": 0,
                            "outlineColor": "transparent",
                        }
                    },
                    "ticks": {
                        "line": {
                            "stroke": "#777777",
                            "strokeWidth": 1,
                        },
                        "text": {
                            "fontSize": 11,
                            "fill": "#fafafa",
                            "outlineWidth": 0,
                            "outlineColor": "transparent",
                        }
                    }
                },
                "grid": {
                    "line": {
                        "stroke": "#dddddd",
                        "strokeWidth": 1,
                    }
                },
                "legends": {
                    "title": {
                        "text": {
                            "fontSize": 11,
                            "fill": "#f4f1f1",
                            "outlineWidth": 0,
                            "outlineColor": "transparent",
                        }
                    },
                    "text": {
                        "fontSize": 11,
                        "fill": "#fffafa",
                        "outlineWidth": 0,
                        "outlineColor": "transparent",
                    },
                    "ticks": {
                        "line": {},
                        "text": {
                            "fontSize": 10,
                            "fill": "#333333",
                            "outlineWidth": 0,
                            "outlineColor": "transparent",
                        }
                    }
                },
                "annotations": {
                    "text": {
                        "fontSize": 13,
                        "fill": "#333333",
                        "outlineWidth": 2,
                        "outlineColor": "#ffffff",
                        "outlineOpacity": 1,
                    },
                    "link": {
                        "stroke": "#000000",
                        "strokeWidth": 1,
                        "outlineWidth": 2,
                        "outlineColor": "#ffffff",
                        "outlineOpacity": 1,
                    },
                    "outline": {
                        "stroke": "#000000",
                        "strokeWidth": 2,
                        "outlineWidth": 2,
                        "outlineColor": "#ffffff",
                        "outlineOpacity": 1,
                    },
                    "symbol": {
                        "fill": "#000000",
                        "outlineWidth": 2,
                        "outlineColor": "#ffffff",
                        "outlineOpacity": 1,
                    }
                },
                "tooltip": {
                    "container": {
                        "background": "#3F3F3F",
                        "color": "FAFAFA",
                        "fontSize": 12,
                    },
                    "basic": {},
                    "chip": {},
                    "table": {},
                    "tableCell": {},
                    "tableCellValue": {},
                }
            },
            "light": {
                "background": "#FFFFFF",
                "textColor": "#31333F",
                "tooltip": {
                    "container": {
                        "background": "#FFFFFF",
                        "color": "#31333F",
                    }
                }
            }
        }

    def __call__(self, json_data):
        try:
            data = json.loads(json_data)
        except json.JSONDecodeError:
            data = self.DEFAULT_DATA

        with mui.Paper(key=self._key,
                       sx={"display": "flex", "flexDirection": "column", "borderRadius": 3,
                           "overflow": "hidden"}, elevation=1):
            with self.title_bar():
                # mui.icon.LineChart()
                mui.Typography("Line chart", sx={"flex": 1})

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                nivo.Line(
                    data=data,
                    theme=self._theme["dark" if self._dark_mode else "light"],
                    margin={"top": 50, "right": 110, "bottom": 50, "left": 60},
                    xScale={"type": 'point'},
                    yScale={
                        "type": 'linear',
                        "min": 'auto',
                        "max": 'auto',
                        "stacked": True,
                        "reverse": False,
                    },
                    yFormat=" >-.2f",
                    axisTop={"null"},
                    axisRight={"null"},
                    axisBottom={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": 'transportation',
                        "legendOffset": 36,
                        "legendPosition": 'middle'
                    },
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": 'count',
                        "legendOffset": -40,
                        "legendPosition": 'middle'
                    },
                    pointSize=10,
                    pointColor={"from": 'color', "modifiers": []},
                    pointBorderWidth=2,
                    pointBorderColor={"from": 'color', "modifiers": []},
                    pointLabelYOffset=-12,
                    enableSlices="x",
                    useMesh=True,
                    legends=[
                        {
                            "anchor": 'bottom-right',
                            "direction": 'column',
                            "justify": False,
                            "translateX": 100,
                            "translateY": 0,
                            "itemsSpacing": 0,
                            "itemDirection": 'left-to-right',
                            "itemWidth": 80,
                            "itemHeight": 20,
                            "itemOpacity": 0.75,
                            "symbolSize": 12,
                            "symbolShape": 'circle',
                            "symbolBorderColor": 'rgba(0, 0, 0, .5)',
                            "effects": [
                                {
                                    "on": 'hover',
                                    "style": {
                                        # "itemBackground": 'rgba(0, 0, 0, .03)',
                                        "itemTextColor": "#000",
                                        # "itemOpacity": 1,
                                    }
                                }
                            ]
                        }
                    ]
                )


class Radar(Dashboard.Item):
    DEFAULT_DATA = [
        {"taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114},
        {"taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72},
        {"taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99},
        {"taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30},
        {"taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103},
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._theme = {
            "dark": {
                "background": "#252526",
                "textColor": "#FAFAFA",
                "tooltip": {
                    "container": {
                        "background": "#3F3F3F",
                        "color": "FAFAFA",
                    }
                }
            },
            "light": {
                "background": "#FFFFFF",
                "textColor": "#31333F",
                "tooltip": {
                    "container": {
                        "background": "#FFFFFF",
                        "color": "#31333F",
                    }
                }
            }
        }

    def __call__(self, json_data):
        try:
            data = json.loads(json_data)
        except json.JSONDecodeError:
            data = self.DEFAULT_DATA

        with mui.Paper(key=self._key,
                       sx={"display": "flex", "flexDirection": "column", "borderRadius": 3,
                           "overflow": "hidden"}, elevation=1):
            with self.title_bar():
                mui.icon.Radar()
                mui.Typography("Radar chart", sx={"flex": 1})

            with mui.Box(sx={"flex": 1, "minHeight": 0}):
                nivo.Radar(
                    data=data,
                    theme=self._theme["dark" if self._dark_mode else "light"],
                    keys=["chardonay", "carmenere", "syrah"],
                    indexBy="taste",
                    valueFormat=">-.2f",
                    margin={"top": 70, "right": 80, "bottom": 40, "left": 80},
                    borderColor={"from": "color"},
                    gridLabelOffset=36,
                    dotSize=10,
                    dotColor={"theme": "background"},
                    dotBorderWidth=2,
                    motionConfig="wobbly",
                    legends=[
                        {
                            "anchor": "top-left",
                            "direction": "column",
                            "translateX": -50,
                            "translateY": -40,
                            "itemWidth": 80,
                            "itemHeight": 20,
                            "itemTextColor": "#999",
                            "symbolSize": 12,
                            "symbolShape": "circle",
                            "effects": [
                                {
                                    "on": "hover",
                                    "style": {
                                        "itemTextColor": "#000"
                                    }
                                }
                            ]
                        }
                    ]
                )
