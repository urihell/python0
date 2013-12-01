# calculator with all buttons
# http://www.codeskulptor.org/#examples-buttons.py
# http://www.codeskulptor.org/#user26_buttons_2.py
    
import simplegui


# intialize globals
store = 12
operand = 3


# event handlers for calculator with a store and operand

def output():
    global store, operand
    print ("Store = ", store)
    print ("Operand = ", operand)

def swap():
    global store, operand
    store, operand  = operand, store
    output()
    
def add():
    global store, operand
    store += operand
    output()


def sub():
    global store, operand
    store -= operand
    output()

def mult():
    global store, operand
    store *= operand
    output()


def div():
    global store, operand
    store /= operand
    output()

# create frame
frame = Frame("Calculator", 300, 300)
# register event handlers
b_print = frame.add_button("Print", output,100)
b_swap = frame.add_button("Swap", swap, 100)
b_add = frame.add_button("Add", add, 100)
b_sub = frame.add_button("Sub", sub, 100)
b_mult = frame.add_button("Mult", mult, 100)
b_div = frame.add_button("Div", div, 100)
# get frame rolling
frame.start()