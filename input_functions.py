from time import sleep
from PyQt5.QtWidgets import  QInputDialog


def get_form(getform):
    global form, pl
    form = getform
    pl = form.pl


def enable_buttons(grp, wrong_grp_1, wrong_grp_2):
    for btn in grp.buttons():
        btn.setVisible(True)
    for btn2 in list(wrong_grp_1.buttons()) + list(wrong_grp_2.buttons()):
        btn2.setVisible(False)


def input_two(spis, list_of_funcs):
    enable_buttons(form.grp_two, form.grp_three, form.grp_four)
    for n, btn in enumerate(form.grp_two.buttons()):
        btn.disconnect()
        btn.clicked.connect(list_of_funcs[n])
        btn.setText(spis[n])


def input_three(spis, list_of_funcs):
    enable_buttons(form.grp_three, form.grp_two, form.grp_four)
    for n, btn in enumerate(form.grp_three.buttons()):
        btn.disconnect()
        btn.clicked.connect(list_of_funcs[n])
        btn.setText(spis[n])


def input_four(spis, list_of_funcs):
    enable_buttons(form.grp_four, form.grp_two, form.grp_three)
    for n, btn in enumerate(form.grp_four.buttons()):
        btn.disconnect()
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


def labels_update():
    form.lbl_money.setText(f'Ваши монеты: {pl.money}')
    form.lbl_health.setText(f'Ваше здоровье: {pl.health}/{pl.maxhealth}')

