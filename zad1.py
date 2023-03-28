import math


def iloscPaneli(x_podloga, y_podloga, x_panel, y_panel, opakowanie_ilosc):
    return math.ceil(((x_podloga * y_podloga) * 1.1) // (x_panel * y_panel) // opakowanie_ilosc)
