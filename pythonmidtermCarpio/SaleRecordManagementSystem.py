def add_sale_record():
    print("Add Sale Record")

    item_name = input("Item Name: ").strip()

def displaymenu():

    print("========================================")
    print("SALES RECORD MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add Sale Record")
    print("2. View All Records & Summary Statistics")
    print("3. Clear All Sales Data")
    print("4. Exit System")
    print("========================================")


def main():

    while True:
        displaymenu()

        try:
            choice = input("Select an option (1-4): ").strip()

            if choice == "1":
                add_sale_record()

            elif choice == "2":
                view_records()

            elif choice == "3":
                clear_sales_data()

            elif choice == "4":
                print('Thank you for using the Sales Record Management System')
                break

            else:
                print("Invalid option. Please select 1-4.")

        except ValueError:
            print("Input interrupted. Exiting system.")
            print('Thank you for using the Sales Record Management System')

            break