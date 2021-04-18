from ipyleaflet import Map, AntPath, Marker, AwesomeIcon
from ipywidgets import IntSlider, jslink

m = Map(center = (47.22235164475102,39.71868753433228), zoom = 30)

'''ant_path = AntPath(
    locations=[
        [47.21949870807924,39.720217921163965], [47.21924072542653,39.720126772464305],
        [47.21941615614319,39.7210279946933], [47.21957696712041,39.72205796295503],
        [47.21978163492707,39.72269096428255], [47.219803563573485,39.722862625659495],
        [47.22024944407145,39.72265877777437], [47.22076110556756,39.72246565872529],
        [47.22138971146107,39.72218670898774], [47.22183557853707,39.72199358993866],
        [47.22232529704315,39.72178974205353], [47.222829629254555,39.721564436496294],
        [47.223085448096086,39.721424961627505], [47.22273461051135,39.71968689018586],
        [47.222551881677376,39.718785667956865], [47.22229606024517,39.71766986900666],
        [47.222113329890256,39.71674718910554], [47.221864815590564,39.71554555946686],
        [47.22158706292733,39.7142902856479], [47.22144087672701,39.7135714536319],
        [47.22110464692704,39.712155247272044], [47.22084881846801,39.71087851578097],
        [47.22042487142981,39.70900096947054], [47.22018365866147,39.7076813226352],
        [47.22095115000068,39.707391644061595], [47.222018309855244,39.706876659930735],
        [47.22284424750753,39.706490421832605], [47.22323162973356,39.70631876045563],
        [47.22343628334465,39.707391644061595], [47.223714026259614,39.70861473137238],
        [47.224094093139,39.71044936233858], [47.22440837714131,39.711811924518145],
        [47.224123328939235,39.711962128222964]
    ],
    dash_array = [1, 10],
    delay = 1000,
    color = '#7590ba',
    pulse_color = '#3f6fba'
)
m.add_layer(ant_path)'''

Icon_incosation = AwesomeIcon(
    name = 'fa-truck',
    marker_color='green',
    icon_color='#ffffff')
Icon_incosation = Marker(icon = Icon_incosation, location=(47.22403572482481,39.71201985093974), draggable=False)
m.add_layer(Icon_incosation);

Icon_m1 = AwesomeIcon(
    name = 'bank',
    marker_color='black',
    icon_color='#ffffff')
m1 = Marker(icon = Icon_m1, location=(47.222880478168456, 39.71807133227662), draggable=False)
m.add_layer(m1);

Icon_m2 = AwesomeIcon(
    name = 'bank',
    marker_color='black',
    icon_color='#ffffff')
m2 = Marker(icon = Icon_m2,location=(47.21861169148149, 39.713827923278785), draggable=False)
m.add_layer(m2);

Icon_m3 = AwesomeIcon(
    name = 'bank',
    marker_color='black',
    icon_color='#ffffff')
m3 = Marker(icon = Icon_m3, location=(47.22114800928688, 39.71284073614226), draggable=False)
m.add_layer(m3);

Icon_m4 = AwesomeIcon(
    name = 'bank',
    marker_color='black',
    icon_color='#ffffff')
m4 = Marker(icon = Icon_m4, location=(47.224256154284916, 39.71149963163482), draggable=False)
m.add_layer(m4);

Icon_m5 = AwesomeIcon(
    name = 'bank',
    marker_color='black',
    icon_color='#ffffff')
m5 = Marker(icon = Icon_m5, location=(47.22005563636405, 39.72014707349884), draggable=False)
m.add_layer(m5);

'''markerSTART = Marker(location=(47.21949870807924,39.720217921163965), draggable=False)
m.add_layer(markerSTART);
markerFINISH = Marker(location=(47.224123328939235,39.711962128222964), draggable=False)
m.add_layer(markerFINISH);'''

zoom_slider = IntSlider(description='Масштаб:', min=11, max=15, value=14)
jslink((zoom_slider, 'value'), (m, 'zoom'))

m.save("map1.html")