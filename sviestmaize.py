# Sviestmaizes pagatavošana

maize_jagrauzde = True
pievienot_pildijumu = True
vel_ir_piedevas = True
sagriezt = True

print("Paņem 2 maizes šķēles")

if maize_jagrauzde:
    print("Ieliec maizi tosterī")
    print("Gaidīt līdz maize gatava")

print("Uzsmērē sviestu vai mērci")

if pievienot_pildijumu:
    print("Uzliec sieru")
    print("Uzliec desu")
    print("Uzliec dārzeņus")

    while vel_ir_piedevas:
        print("Pievieno papildu sastāvdaļu")
        vel_ir_piedevas = False

print("Uzliek otru maizes šķēli")

if sagriezt:
    print("Sagriezt sviestmaizi uz pusēm")

print("Sviestmaize gatava!")