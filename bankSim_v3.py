import numpy as np

# --- ایجاد حساب‌ها ---
num = int(input("چند حساب بانکی می‌خواهید ایجاد کنید؟ "))

names = []
balances = np.zeros(num)

for i in range(num):
    name = input(f"نام صاحب حساب {i+1} را وارد کنید: ")
    balance = float(input("موجودی اولیه: "))
    names.append(name)
    balances[i] = balance

# --- منوی عملیات ---
while True:
    print("\n===== منوی عملیات بانکی =====")
    print("1. نمایش موجودی همه حساب‌ها")
    print("2. سپرده‌گذاری در حساب")
    print("3. برداشت از حساب")
    print("4. نمایش حساب‌هایی با موجودی بیشتر از میانگین")
    print("5. خروج از برنامه")
    
    choice = input("انتخاب کنید: ")

    # 1️⃣ نمایش لیست حساب‌ها با شماره درست
    if choice == "1":
        print("\n--- لیست حساب‌ها ---")
        for index, (name, balance) in enumerate(zip(names, balances), start=1):
            print(f"{index}. نام: {name} --> موجودی: {balance}")

    # 2️⃣ سپرده‌گذاری
    elif choice == "2":
        print("\nبرای سپرده گذاری شماره حساب را وارد کنید:")
        for index, name in enumerate(names, start=1):
            print(f"{index}. {name}")
            
        idx = int(input("شماره حساب: ")) - 1
        amount = float(input("مبلغ سپرده: "))
        balances[idx] += amount
        print("سپرده‌گذاری انجام شد.")

    # 3️⃣ برداشت
    elif choice == "3":
        print("\nبرای برداشت شماره حساب را وارد کنید:")
        for index, name in enumerate(names, start=1):
            print(f"{index}. {name}")
            
        idx = int(input("شماره حساب: ")) - 1
        amount = float(input("مبلغ برداشت: "))
        if balances[idx] >= amount:
            balances[idx] -= amount
            print("برداشت انجام شد.")
        else:
            print("موجودی کافی نیست!")

    # 4️⃣ نمایش حساب‌های بیشتر از میانگین
    elif choice == "4":
        avg = np.mean(balances)
        print(f"\nمیانگین موجودی: {avg}")
        print("🏦 حساب‌هایی با موجودی بیش از میانگین:")
        for index, (name, balance) in enumerate(zip(names, balances), start=1):
            if balance > avg:
                print(f"{index}. نام: {name} --> موجودی: {balance}")

    # 5️⃣ خروج
    elif choice == "5":
        print("برنامه پایان یافت.")
        break

    else:
        print("گزینه اشتباه است!")
