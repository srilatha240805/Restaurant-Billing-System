# ---------------------------------------------------------
#              PRIME RESTAURANT BILLING SYSTEM
# ---------------------------------------------------------

# ---------------- MENU DICTIONARY ----------------
menu = {
    "ChickenBiryani": 300, "FishBiryani": 350, "MuttonBiryani": 400,
    "EggBiryani": 250, "PrawnBiryani": 310, "ChickenManchurian": 200,
    "ChickenCurry": 220, "MuttonCurry": 360, "PrawnCurry": 370,
    "ChickenFry": 280,

    "Chepatikurma": 100, "Vegetablepulao": 150, "ButterNaan": 152,
    "RumaalRoti": 120, "Paneer&Parota": 130, "PaneerBiryani": 200,
    "MushroomBiryani": 220, "PaneerTikka": 180, "GobiManchurian": 110,
    "CheesyPizza": 160
}

# CATEGORY SPLITTING
non_veg_items = list(menu.items())[:10]
veg_items = list(menu.items())[10:]

# ---------------- DISPLAY MENU ----------------
def display_menu():
    print("\n  ---------------------- MENU ----------------------------")
    print("  |  NON VEG ITEMS           | Price |   VEG ITEMS         | Price |")
    print("  ---------------------------------------------------------")

    for i in range(10):
        left = non_veg_items[i][0].ljust(22) + "| ₹" + str(non_veg_items[i][1]).ljust(5)
        right = veg_items[i][0].ljust(20) + "| ₹" + str(veg_items[i][1]).ljust(5)
        print("  | " + left + " | " + right + " |")

    print("  ---------------------------------------------------------\n")


# ---------------- BILL NUMBER HANDLING ----------------
def get_bill_number():
    filename = "billno.txt"
    try:
        with open(filename, "r") as f:
            billno = int(f.read().strip())
    except:
        billno = 100  # default starting bill number

    try:
        with open(filename, "w") as f:
            f.write(str(billno + 1))
    except:
        print("⚠ Could not update bill number.")
        billno += 1

    return billno


# ---------------- TAKE ORDER ----------------
def take_order():
    name, price, qty, total = [], [], [], []

    while True:
        item = input("Enter item name: ").strip()

        if item not in menu:
            print("❌ Item not found, try again.\n")
            continue

        name.append(item)
        price.append(menu[item])

        while True:
            q = input(f"Enter quantity for {item}: ")
            if q.isdigit() and int(q) > 0:
                qty.append(int(q))
                break
            print("❌ Quantity must be a positive number.")

        total.append(price[-1] * qty[-1])
        print(f"✔ Total for {item}: ₹{total[-1]}\n")

        # Add more items?
        choice = input("Add another item? (y/n): ").lower()
        if choice != "y":
            break

    return name, price, qty, total


# ---------------- BILL PRINTING ----------------
def print_bill(date, table, billno, name, price, qty, total):
    sum1 = sum(total)
    gst = round(sum1 * 0.05, 2)           # 5% GST
    service = round(sum1 * 0.03, 2)       # 3% service charge
    discount = 0

    # Optional discount
    d_choice = input("Apply discount? (y/n): ").lower()
    if d_choice == "y":
        d_percent = float(input("Enter discount %: "))
        discount = round(sum1 * d_percent / 100, 2)

    final_total = round(sum1 + gst + service - discount, 2)

    # ---------------- PRINT BILL ----------------
    print("\n------------------ PRIME RESTAURANT ------------------")
    print("               Banjara Hills, Hyderabad")
    print("                    Phone: 23867544")
    print("------------------------------------------------------")
    print(f"Date: {date}     Table No: {table}     Bill No: {billno}")
    print("------------------------------------------------------")
    print("Item".ljust(20) + "Qty".rjust(5) + "Price".rjust(10) + "Total".rjust(10))
    print("------------------------------------------------------")

    for i in range(len(name)):
        print(name[i].ljust(20), str(qty[i]).rjust(5),
              str(price[i]).rjust(10), str(total[i]).rjust(10))

    print("------------------------------------------------------")
    print("Item Total".ljust(30), "₹", sum1)
    print("GST (5%)".ljust(30), "₹", gst)
    print("Service Charge (3%)".ljust(30), "₹", service)
    print("Discount".ljust(30), "₹", discount)
    print("GRAND TOTAL".ljust(30), "₹", final_total)
    print("------------------------------------------------------")
    print("         Thank you for dining with us! 😊")
    print("------------------------------------------------------")

    save_bill(billno, date, table, final_total)


# ---------------- SAVE BILL TO FILE ----------------
def save_bill(billno, date, table, total_amount):
    filename = f"bill_{billno}.txt"
    with open(filename, "w") as f:
        f.write(f"BILL NUMBER: {billno}\nDATE: {date}\nTABLE: {table}\nTOTAL: ₹{total_amount}")
    print(f"\n💾 Bill saved as {filename}")


# ---------------- MAIN PROGRAM ----------------
def main():
    display_menu()

    billno = get_bill_number()
    date = input("Enter date (DD/MM/YYYY): ")
    table = input("Enter table number: ")

    name, price, qty, total = take_order()
    print_bill(date, table, billno, name, price, qty, total)


# Run Program
main()
