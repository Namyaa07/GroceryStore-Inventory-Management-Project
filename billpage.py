import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Window setup
root = tk.Tk()
root.geometry("500x400")
root.title("Grocery Store Billing System")
tk.Label(root, text='BILLING SYSTEM', font=("Helvetica", 16)).grid(row=0, column=1, pady=10)

# Database connection
conn = mysql.connector.connect(
    host='localhost',
    user="root",
    password='@ntifr@gile',
    database='grocery_store'
)
cursor = conn.cursor()

# Dropdown (item list)
cursor.execute("SELECT code, name FROM items")
items = cursor.fetchall()
item_dict = {f"{code} - {name}": code for code, name in items}
item_code_var = tk.StringVar(root)
item_code_var.set("Select item")


def update_item_code(*args):
    selected = item_code_var.get()
    if selected != 'Select item':
        code = item_dict[selected]
        item_code_entry.delete(0, tk.END)
        item_code_entry.insert(0, code)


item_dropdown = tk.OptionMenu(root, item_code_var, *list(item_dict.keys()))
item_dropdown.grid(row=1, column=2, padx=10, pady=5)
item_code_var.trace_add("write", update_item_code)

# Item code and quantity
tk.Label(root, text='Item Code:').grid(row=1, column=0, padx=10)
item_code_entry = tk.Entry(root)
item_code_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="Quantity:").grid(row=2, column=0, padx=10, pady=5)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=2, column=1, padx=10, pady=5)

# Bill summary
bill_listbox = tk.Listbox(root, width=50)
bill_listbox.grid(row=4, column=0, columnspan=3, padx=10)

# Total amount
total_amt = tk.Label(root, text='Total Amount: ₹0', font=('Helvetica', 12))
total_amt.grid(row=5, column=1, pady=10)
total_cost = 0
total_quantity = 0


# Adding items
def add_item():
    global total_cost, total_quantity
    item_code = item_code_entry.get()
    quantity = quantity_entry.get()

    if not quantity.isdigit():
        messagebox.showerror("Error", "Enter a valid quantity.")
        return

    cursor.execute("SELECT name, price FROM items WHERE code=%s", (item_code,))
    result = cursor.fetchone()

    if result:
        item_name, price_per_unit = result
        quantity = int(quantity)
        total_price = float(price_per_unit) * quantity
        bill_listbox.insert(tk.END, f"{item_name} - {item_code} - Qty: {quantity} - Total: ₹{total_price:.2f}")
        total_cost += total_price
        total_quantity+=quantity
        total_amt.config(text=f"Total Amount: ₹{total_cost:.2f}")
    else:
        messagebox.showerror("Error", 'Item not found. Please check the item code.')

    item_code_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)


# Deleting items
def delete_item():
    global total_cost
    selected_index = bill_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Warning", "Select an item to delete.")
        return

    item_text = bill_listbox.get(selected_index[0])
    item_price = float(item_text.split("Total: ₹")[-1])
    total_cost -= item_price
    total_amt.config(text=f"Total Amount: ₹{total_cost:.2f}")
    bill_listbox.delete(selected_index)


# Modifying item quantity


# Generate bill
def generate_bill():
    global total_cost, total_quantity
    if total_cost > 0:
        bill_content = "--- Grocery Store Bill ---\n"
        bill_content += f"{'Item':<15}{'Qty':<5}{'Total':<10}\n"
        bill_content += "-" * 40 + "\n"

        for item in bill_listbox.get(0, tk.END):
            bill_content += f"{item}\n"

        bill_content += "-" * 40 + "\n"
        bill_content += f"Total Cost: ₹{total_cost:.2f}\n"

        # Display bill
        bill_window = tk.Toplevel(root)
        bill_window.title("Generated Bill")
        bill_window.geometry("400x400")

        bill_text = tk.Text(bill_window, font=("Courier", 12), wrap='none')
        bill_text.insert('1.0', bill_content)
        bill_text.configure(state="disabled")
        bill_text.pack(expand=True, fill="both", padx=10, pady=10)

        close_button = tk.Button(bill_window, text="Close", command=bill_window.destroy)
        close_button.pack(pady=10)

        # Update sales table
        try:
            insert_query = "INSERT INTO sales (quantity, total_cost) VALUES (%s, %s)"
            cursor.execute(insert_query, (total_quantity, total_cost))
            conn.commit()
            messagebox.showinfo("Success", "Bill generated and sales table updated!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Failed to update sales table: {err}")


        bill_listbox.delete(0, tk.END)
        total_amt.config(text='Total Amount: ₹0')
        total_cost = 0
    else:
        messagebox.showwarning("Warning", "No items to bill.")




tk.Button(root, text='Add Item', command=add_item).grid(row=3, column=1, pady=5)
tk.Button(root, text='Delete Item', command=delete_item).grid(row=3, column=2, pady=5)
tk.Button(root, text="Generate Bill", command=generate_bill).grid(row=6, column=1, pady=10)
#tk.Button(root, text="Update Sales Table", command=update_sales).grid(row=7, column=1, pady=13)

root.mainloop()
