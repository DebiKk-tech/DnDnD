from time import sleep
from PyQt5.QtWidgets import QWidget, QInputDialog


def get_form(getform):
    global form
    form = getform


def input_two(spis, list_of_funcs):
    for btn in form.grp_three.buttons():
        btn.setVisible(False)
    for btn in form.grp_four.buttons():
        btn.setVisible(False)
    for n, btn in enumerate(form.grp_two.buttons()):
        btn.disconnect()
        btn.setVisible(True)
        btn.clicked.connect(list_of_funcs[n])
        btn.setText(spis[n])


def input_three(spis, list_of_funcs):
    for btn in form.grp_two.buttons():
        btn.setVisible(False)
    for btn in form.grp_four.buttons():
        btn.setVisible(False)
    for n, btn in enumerate(form.grp_three.buttons()):
        btn.disconnect()
        btn.setVisible(True)
        btn.clicked.connect(list_of_funcs[n])
        btn.setText(spis[n])


def input_four(spis, list_of_funcs):
    for btn in form.grp_three.buttons():
        btn.setVisible(False)
    for btn in form.grp_two.buttons():
        btn.setVisible(False)
    for n, btn in enumerate(form.grp_four.buttons()):
        btn.disconnect()
        btn.setVisible(True)
        btn.clicked.connect(list_of_funcs[n])
        btn.setText(spis[n])


def dialog_list_input(name, text, list):
    okay_pressed = False
    while not okay_pressed:
        choice, okay_pressed = QInputDialog.getItem(form, name, text,
                                                    list, 0, False)
    return choice


def dialog_int_input(name, text, start=0, minim=0, max=999, step=1):
    okay_pressed = False
    while not okay_pressed:
        choice, okay_pressed = QInputDialog.getInt(form, name, text,
                                                   start, minim, max, step)
    return choice


def output(text):
    wastext = form.pln_output.toPlainText()
    text = '\n' + text + '\n'
    for i in range(len(text)):
        form.pln_output.setPlainText(text[:i] + wastext)
        form.repaint()
        sleep(0.01)
    wastext = '\n' + form.pln_output.toPlainText()
    form.pln_output.setPlainText(wastext)


def profile_update():
    print('Профиль пользователя обновлен')  # СДЕЛАТЬ ПОЗЖЕ

