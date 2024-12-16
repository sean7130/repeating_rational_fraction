import sys
import re
import repeat_finder_interactive

from PySide2.QtWidgets import QApplication, QMainWindow

from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.decimal_input.textChanged.connect(self.handle_decimal_input)
        self.current_decimal_input_text = self.ui.decimal_input.toPlainText()

    def _sanitize_decimal_input(self):
        text = self.ui.decimal_input.toPlainText()
        if not re.fullmatch(r"[0-9.]*", text):
            corrected_text = re.sub(r"[^0-9.]", "", text)
            self.ui.decimal_input.blockSignals(True)
            self.ui.decimal_input.setPlainText(corrected_text)
            self.ui.decimal_input.blockSignals(False)

    def _clear_decimal_input_and_repeat_finder(self):
        repeat_finder_interactive.clear()

        self.ui.decimal_input.blockSignals(True)
        self.ui.decimal_input.clear()
        self.current_decimal_input_text = self.ui.decimal_input.toPlainText()
        self.ui.decimal_input.blockSignals(False)

    def update_fraction(self, n, d):
        self.ui.numerator.setText(str(n))
        self.ui.denominator.setText(str(d))
        self.ui.eval.setText(str(n/d))

    def handle_decimal_input(self):
        self._sanitize_decimal_input()
        new_text = self.ui.decimal_input.toPlainText()
        if new_text != self.current_decimal_input_text:
            # TODO: handle case where someone edits value from the middle.
            if len(new_text) < len(self.current_decimal_input_text):
                # repeat_finder_interactive.perform_backspace()
                self._clear_decimal_input_and_repeat_finder()
            elif len(new_text) != 0:
                repeat_finder_interactive.register_input(new_text[-1])
                frac, n, d = repeat_finder_interactive.produce_fraction()

                self.update_fraction(n, d)

            self.current_decimal_input_text = new_text



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
