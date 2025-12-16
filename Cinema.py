rows = int(input("تعداد ردیف‌ها را وارد کنید: "))
cols = int(input("تعداد ستون‌ها را وارد کنید: "))

hall = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)
    hall.append(row)

def show_seats():
    print("\nوضعیت سالن:")
    for row in hall:
        for seat in row:
            print(seat, end=" ")
        print()

def book_ticket():
    r = int(input("شماره ردیف: ")) - 1
    c = int(input("شماره ستون: ")) - 1

    if hall[r][c] == 0:
        hall[r][c] = 1
        print("✅ صندلی با موفقیت رزرو شد.")
    else:
        print("❌ این صندلی قبلاً رزرو شده است.")

def cancel_ticket():
    r = int(input("شماره ردیف: ")) - 1
    c = int(input("شماره ستون: ")) - 1

    if hall[r][c] == 1:
        hall[r][c] = 0
        print("🔄 رزرو صندلی لغو شد.")
    else:
        print("⚠️ این صندلی از قبل خالی است.")

def show_seats_count():
    empty = 0
    booked = 0

    for row in hall:
        for seat in row:
            if seat == 0:
                empty += 1
            else:
                booked += 1

    print(f"🟢 صندلی‌های خالی: {empty}")
    print(f"🔴 صندلی‌های رزرو شده: {booked}")

def calculate_income():
    price = 120000
    booked = 0

    for row in hall:
        for seat in row:
            if seat == 1:
                booked += 1

    total = booked * price
    print(f"💰 درآمد کل: {total:,} تومان")

# ====== Main Menu ======
while True:
    print("\n🎥 منوی مدیریت سینما")
    print("1- Show seats")
    print("2- Book a ticket")
    print("3- Cancel a ticket")
    print("4- Show seats count")
    print("5- Calculate income")
    print("6- Exit")

    choice = input("انتخاب شما: ")

    if choice == "1":
        show_seats()

    elif choice == "2":
        book_ticket()

    elif choice == "3":
        cancel_ticket()

    elif choice == "4":
        show_seats_count()

    elif choice == "5":
        calculate_income()

    elif choice == "6":
        print("👋 خروج از برنامه")
        break

    else:
        print("❌ گزینه نامعتبر")
