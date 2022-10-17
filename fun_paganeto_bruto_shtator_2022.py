def paga_neto_bruto(pagaNeto:float):
    pagaMinimale = 34_000
    pagaMaxKonShoq = 149_954  # Paga Maksimale per kontributet shoqerore
    sigShoqPerqind = 9.5 / 100  # Sigurimet Shoqerore te punemarresit
    sigShenPerqind = 1.7 / 100  # Sigurimet shendetesore te punedhenesit
    tapKufiri40_000 = 40_000  # Kufiri prej 40_000 lekesh per TAP
    tapKufiri30_000 = 30_000  # Kufiri prej 30_000 lekesh per TAP
    tapKufiri20mil = 200_000  # Kufiri prej 200_000  lekesh per TAP
    tapKufiri50_000 = 50_000  # Kufiri prej 50_000  lekesh per TAP
    tap13Perqind = 13 / 100  # Tatimi prej 13% per TAP
    tap23Perqind = 23 / 100  # Tatimi prej 23% per TAP
    tap6Pike5Perqind = 6.5 / 100  # Tatimi pre 6.5% per TAP
    pagaBruto = pagaNeto / (1 - sigShoqPerqind - sigShenPerqind)
    if pagaBruto <= tapKufiri40_000: return pagaBruto
    pagaBruto = (pagaNeto - tapKufiri30_000 * tap6Pike5Perqind) / (
                    1 - sigShoqPerqind - sigShenPerqind - tap6Pike5Perqind)
    if pagaBruto <= tapKufiri50_000: return pagaBruto
    pagaBruto = (pagaNeto - tapKufiri30_000 * tap13Perqind) / (1 - sigShoqPerqind - sigShenPerqind - tap13Perqind)
    if pagaBruto <= pagaMaxKonShoq: return pagaBruto
    pagaBruto = (pagaNeto - tapKufiri30_000 * tap13Perqind + pagaMaxKonShoq * sigShoqPerqind) / \
                        (1 - sigShenPerqind - tap13Perqind)
    if pagaBruto <= tapKufiri20mil:return pagaBruto
    return (pagaNeto + pagaMaxKonShoq * sigShoqPerqind - tapKufiri20mil * tap23Perqind + \
                                 (tapKufiri20mil - tapKufiri30_000) * tap13Perqind) / (
                                            1 - sigShenPerqind - tap23Perqind)
l = [77481.33,79700.0, 38985.0, 43316.0,168622.27,117604.37]
for paga in l:
    print("Paga Neto, ", paga, "Paga Bruto", round(paga_neto_bruto(paga),0))
