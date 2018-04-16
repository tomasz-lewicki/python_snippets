import threading
import time
import random

class BankAccount(threading.Thread):

    account_balance = 100

    def __init__(self, name, money_request):
        threading.Thread.__init__(self)

        self.name=name
        self.money_request = money_request

    def run(self):
        account_lock.acquire()

        BankAccount.get_money(self)

        account_lock.release()


    @staticmethod
    def get_money(customer):
        print("{} tries to withdraw ${} at {}".format(customer.name,
                                                      customer.money_request,
                                                      time.strftime("%H:%M:%S",time.gmtime())))

        if BankAccount.account_balance - customer.money_request > 0:
            BankAccount.account_balance -= customer.money_request
            print("Refreshed account balance: PLN{}".format(BankAccount.account_balance))

        else:
            print("No money")
            print("Current balance is PLN {}".format(BankAccount.account_balance))

        time.sleep(3)


account_lock = threading.Lock()

adams_account = BankAccount("Adam", 1)
beatas_account = BankAccount("Beata", 100)
celinas_account = BankAccount("Celina", 50)

adams_account.start()
beatas_account.start()
celinas_account.start()

adams_account.join()
beatas_account.join()
celinas_account.join()

print("end of program")
