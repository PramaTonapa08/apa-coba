# Sebuah toko memberikan diskon berdasarkan total belanja pelanggan.
# Buatlah program yang menerima input total belanja.
# Jika total belanja lebih dari atau sama dengan Rp500.000:
    # pelanggan berhak mendapatkan diskon 20%.
# Jika kurang dari itu, tidak ada diskon (0%).
# Tampilkan total akhir yang harus dibayar setelah dikurangi diskon (jika ada).

total_purchase = float(input('Please enter your total purchase: Rp '))

if total_purchase >= 500000:
    discount = 0.20 * total_purchase
    persent_discount = 20

else:
    discount = 0
    persent_discount = 0

total = total_purchase - discount

print(f"\nTotal Belanja: Rp {total_purchase:,.2f}")
print(f"Diskon ({persent_discount}%): Rp {discount:,.2f}")
print(f"Total Bayar: Rp {total:,.2f}")