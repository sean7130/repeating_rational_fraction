import sys
import re
import repeat_finder_interactive
from math import gcd

from PySide2.QtWidgets import QApplication, QMainWindow

from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.decimal_input.textChanged.connect(self.handle_decimal_input)
        self.current_decimal_input_text = self.ui.decimal_input.text()

        self.ui.latex_checkbox.stateChanged.connect(self.latex_checkbox_toggle)

        self.ui.n_input.textChanged.connect(self.determine_user_input_repeats)
        self.ui.d_input.textChanged.connect(self.determine_user_input_repeats)

    def _sanitize_decimal_input(self, input_field):
        text = input_field.text()
        if not re.fullmatch(r"[0-9.]*", text):
            corrected_text = re.sub(r"[^0-9.]", "", text)
            input_field.blockSignals(True)
            input_field.setPlainText(corrected_text)
            input_field.blockSignals(False)

    def _clear_decimal_input_and_repeat_finder(self):
        repeat_finder_interactive.clear()

        self.ui.decimal_input.blockSignals(True)
        self.ui.decimal_input.setText("")
        self.current_decimal_input_text = self.ui.decimal_input.text()
        self.ui.decimal_input.blockSignals(False)

    def determine_user_input_repeats(self):
        self._sanitize_decimal_input(self.ui.d_input)
        self._sanitize_decimal_input(self.ui.n_input)
        d = self.ui.d_input.text()
        n = self.ui.n_input.text()
        
        if d != "" and n != "":
            d = int(d)
            n = int(n)
            self.ui.eval_2.setText(str(n/d))
            repeats = repeating_decimal_length(n, d)
            self.ui.digit_repeat_label.setText(f"Total repeated digits: {repeats}")
        else:
            self.ui.eval_2.setText("NaN")
            self.ui.digit_repeat_label.setText("Total repeated digits: <invalid input>")



    def latex_checkbox_toggle(self):
        frac, n, d = repeat_finder_interactive.produce_fraction()
        self.update_copy_box(n, d)

    def update_copy_box(self, n, d):
        if self.ui.latex_checkbox.isChecked():
            self.ui.fraction_text.setText(f"\\frac{{{n}}}{{{d}}}")
        else:
            self.ui.fraction_text.setText(f"{n}/{d}")

    def reset_copy_box(self):
        self.ui.fraction_text.setText("NaN")

    def update_calculated_fraction(self, n, d):
        self.ui.numerator.setText(str(n))
        self.ui.denominator.setText(str(d))
        self.ui.eval.setText(str(n/d))

        self.update_copy_box(n, d)

    def reset_default_render(self):
        n_text, d_text, eval_text = get_default_dne_text()
        self.ui.numerator.setText(str(n_text))
        self.ui.denominator.setText(str(d_text))
        self.ui.eval.setText(str(eval_text))

        self.reset_copy_box()

    def update_ui_with_fraction(self, frac, n , d):
        if d != -1:
            self.update_calculated_fraction(n, d)
        else: 
            self.reset_default_render()

    def handle_decimal_input(self):
        self._sanitize_decimal_input(self.ui.decimal_input)
        new_text = self.ui.decimal_input.text()
        if new_text != self.current_decimal_input_text:
            if new_text[:-1] == self.current_decimal_input_text:
                repeat_finder_interactive.register_input(new_text[-1])
                frac, n, d = repeat_finder_interactive.produce_fraction()
                self.update_ui_with_fraction(frac, n, d)

            # elif len(new_text) < len(self.current_decimal_input_text):
            #     # TODO: repeat_finder_interactive.perform_backspace()
            #     self._clear_decimal_input_and_repeat_finder()
            #     new_text = self.ui.decimal_input.text()
                
            else:
                # it appears the user did an edit in the middle of the number: reclaculate everything
                repeat_finder_interactive.clear()
                for c in new_text:
                    repeat_finder_interactive.register_input(c)
                frac, n, d = repeat_finder_interactive.produce_fraction()
                self.update_ui_with_fraction(frac, n, d)

            self.current_decimal_input_text = new_text


def get_default_dne_text():
    """
    Text order: N, D, Eval
    """
    ret = (u"<html><head/><body><p><span style=\" font-size:26pt;\">N</span><span style=\" font-size:12pt;\">umerator</span></p></body></html>",
           u"<html><head/><body><p><span style=\" font-size:26pt;\">D</span><span style=\" font-size:12pt;\">enominator</span></p></body></html>",
           u"<html><head/><body><p align=\"center\">No repeats so far: keep typing</p></body></html>")
    return ret


def repeating_decimal_length(n, d):
    """
    Bonus function to find the repeating length when provided with two integers n, d
    where n/d
    """
    g = gcd(n, d)
    d //= g

    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5

    if d == 1:
        return 0

    length = 1
    remainder = 10 % d

    while remainder != 1:
        remainder = (remainder * 10) % d
        length += 1

    return length


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
