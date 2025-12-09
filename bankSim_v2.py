import numpy as np
# --- ایجاد حساب‌ها ---
num = int(input("چند حساب بانکی می‌خواهید ایجاد کنید؟ "))

names = []
balances = np.zeros(num)  # لیست موجودی‌ها با numpy

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

    # نمایش موجودی همه
    if choice == "1":
        print("\n--- لیست حساب‌ها ---")
        for i in range(num):
            print(f"{names[i]} --> موجودی: {balances[i]}")

    # سپرده‌گذاری
    elif choice == "2":
        name = input("نام حساب برای سپرده‌گذاری: ")
        if name in names:
            idx = names.index(name)
            amount = float(input("مبلغ سپرده: "))
            balances[idx] += amount
            print("سپرده‌گذاری انجام شد.")
        else:
            print("حساب یافت نشد!")

    # برداشت
    elif choice == "3":
        name = input("نام حساب برای برداشت: ")
        if name in names:
            idx = names.index(name)
            amount = float(input("مبلغ برداشت: "))
            if balances[idx] >= amount:
                balances[idx] -= amount
                print("برداشت انجام شد.")
            else:
                print("موجودی کافی نیست!")
        else:
            print("حساب یافت نشد!")

    # نمایش حساب‌های بالاتر از میانگین
    elif choice == "4":
        avg = np.mean(balances)
        print(f"\nمیانگین موجودی: {avg}")
        print("🏦 حساب‌هایی با موجودی بیش از میانگین:")
        for i in range(num):
            if balances[i] > avg:
                print(f"{names[i]} --> موجودی: {balances[i]}")

    # خروج
    elif choice == "5":
        print("برنامه پایان یافت.")
        break

    else:
        print("گزینه اشتباه است!")
