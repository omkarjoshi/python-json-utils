# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
from dataclasses import dataclass as dataclass
from typing import List
from unicodedata import decimal

from converter import writer, mapper
from converter.mapper import maptotypefromstring


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

@dataclass(init=True)
class Item:
    itemid: str
    quantity: float
    unitprice: decimal

@dataclass(init=True)
class Order:
    orderid: str

    items: List[Item] = None



# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    order = Order(orderid="ORDER1", items=items)

    print(writer.writetostring(items))

    orderstring = writer.writetostring(order)
    print(orderstring)

    returndata:Order = mapper.maptotypefromstring(orderstring,Order)

    print(returndata)