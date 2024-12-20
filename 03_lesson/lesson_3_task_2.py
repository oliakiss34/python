from smartphone import Smartphone
phone1 = Smartphone ("Apple", "5s", "+7999455587")
phone2 = Smartphone ("Lenovo", "20", "+79125696753")
phone3 = Smartphone ("Honor", "Deluxe", "+7908769898")
phone4 = Smartphone ("Samsung", "Galaxy", "+79757543211")
phone5 = Smartphone ("Redmi", "Note", "+79505676569")

catalog = [phone1, phone2, phone3, phone4, phone5]
for phones in catalog:
    print(phones.mm + "-" + phones.m + "." + phones.n)