print("เงินในบัญชีของน้อง : 1,000,000")
inp = 1000000
try:
    ic = "Income to Bank"  # ภาษาอังกฤษ
    ou = "Outcome from Bank"  # ภาษาอังกฤษ
    tf = "Tranfer To P'Kanyok"  # ภาษาอังกฤษ
    wd = "Withdraw To Yourself"  # ภาษาอังกฤษ

    '''
    หากทดลอง formatเป็นภาษาไทยแาจจะทำไม่ได้ เพราะในภาษาไทยมีสระ/วรรณยุกต์ที่ห้อยหัวหรือท้ายตัวอักษร
    จึงทำให้บางกรณีที่ format string แล้วยังไม่ตรงตามต้องการ
    '''

    inc = (input(f"{ic:-^40}\n(THB) -> "))
    ouc = (input(f"{ou:-^40}\n(THB) -> "))  # รับดาต้าเงิน
    trf = (input(f"{tf:-^40}\n(THB) -> "))  # รับดาต้าเงิน
    wdrw = (input(f"{wd:-^40}\n(THB) -> "))  # รับดาต้าเงิน
    inc = float(inc)
    ouc = float(ouc)
    trf = float(trf)
    wdrw = float(wdrw)
    id_count = 1  # นับเลขรายการ
    income = "INCOME"  # ชื่อรายการ
    outcome = "OUTCOME"  # ชื่อรายการ
    transfer = "TRANSFER"  # ชื่อรายการ
    withdraw = "WITHDRAW"  # ชื่อรายการ

    # ------------------------------------------------------------------------
    now = inp + inc
    if  now - ouc < 0 or \
        now - ouc - trf < 0 or \
        now - ouc - trf - wdrw < 0:
        print("\nจำนวนเงินผิดพลาด")
        exit()
    if  now < 0 or now > 1_000_000_000 or \
        inc < 0 or inc > 1_000_000_000 or \
        ouc < 0 or ouc > 1_000_000_000 or \
        trf < 0 or trf > 1_000_000_000 or \
        wdrw < 0 or wdrw > 1_000_000_000:
        print("\nเงินเยอะเกิน / เงินติดลบไม่ไหวๆ")
        exit()

    '''
    เป็นการตรวจสอบ Error ที่โปรแกรมไม่อยากให้มี คือระบบธนาคารนี้ต้องถูกต้องตามเป็นจริงโดยที่ไม่ให้เงิน
    ติดลบ
    ซึ่งหากเลขการถอนตังหรือรายจ่ายมากกว่าเงินที่มีอยู่ จะปิดโปรแกรมทันทีด้วนคำสั่ง exit()
    '''

    # ------------------------------------------------------------------------
    print(f'='*57)
    print(f'| {"ID":<2} | {"Type":^10} | {"Amount":>16} | {"Current":>16} |')
    print(f'='*57)
    print(f"| {id_count:<2} | {income:^10} | {inp:>16,.2f} | {inp:>16,.2f} |")
    id_count += 1
    inp += inc
    print(f"| {id_count:<2} | {income:^10} | {inc:>16,.2f} | {inp:>16,.2f} |")
    id_count += 1
    inp -= ouc
    print(f"| {id_count:<2} | {outcome:^10} | {ouc:>16,.2f} | {inp:>16,.2f} |")
    id_count += 1
    inp -= trf
    print(f"| {id_count:<2} | {transfer:^10} | {trf:>16,.2f} | {inp:>16,.2f} |")
    id_count += 1
    inp -= wdrw
    print(f"| {id_count:<2} | {withdraw:^10} | {wdrw:>16,.2f} | {inp:>16,.2f} |")
    print(f'='*57)

    '''
    การแสดงผลข้อมูลตามช่องว่าง (whitespace) ที่ต้องการเพื่อง่ายต่อการอ่าน
    '''

except ValueError:
    print("\n\nกรุณากรอกข้อมูลให้ถูกต้อง")
except TypeError:
    print("\n\nเกิดข้อผิดพลาดทางประเภทข้อมูล")
except OverflowError:
    print("\n\nเกิดข้อผิดพลาดทางการคำนวณ")
except KeyboardInterrupt:
    print("\n\nการทำงานถูกยกเลิกโดยผู้ใช้")
except EOFError:
    print("\n\nสิ้นสุดการรับข้อมูลกะทันหัน")
    '''
    ใน except สามารถ ใส่ข้อมูลได้ด้วยว่า Error ตามประเภทไหนต้องการให้บอกอะไร
    แต่ก็สามารใช้ except แบบไม่มีข้อมูลไปเลยก็ได้ (สามารถดูตัวอย่างอีกวิธีในข้อถัดไป)
    '''
finally:
    print("\nขอบคุณที่ใช้บริการ")
    '''
    ไม่ว่าจะกรณี Error หรือ Bestcase (ไม่Error) ก็จะทำตามคำสั่งใน finally ในตอนท้ายที่สุด
    '''
