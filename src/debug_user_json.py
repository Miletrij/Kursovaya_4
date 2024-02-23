from src.user_form import UserForm


class DebugUserJson(UserForm):
    payment = None
    city = None

    def user_input_int(self):
        self.payment = input("Введите минимальную зарплату цифрами: ")
        if self.payment.isalpha():
            raise ValueError("Неверно указана зарплата")
        if self.payment == "":
            self.payment = 0
        return int(self.payment)

    def user_input_str(self):
        self.city = input("Введите интересующий Вас город: ").title()
        if self.city.isdigit():
            raise TypeError("Город не должен содержать числа")
        return self.city


if __name__ == '__main__':
    r = DebugUserJson()
    print(r.user_input_str())
