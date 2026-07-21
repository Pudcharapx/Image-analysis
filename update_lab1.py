import json

with open('lab1_assignment.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Insert the Q&A for task 1 after the first code cell
qa1 = {
 "cell_type": "markdown",
 "metadata": {},
 "source": [
  "### คำถามท้ายการทดลองข้อที่ 1\n",
  "**อภิปรายว่าเมื่อนำค่าความสว่างที่แปลงด้วยสูตร `0.299·R + 0.587·G + 0.114·B` ไปเทียบกับ ฟังก์ชันสำเร็จรูปของ OpenCV แล้ว ผลลัพธ์มีความแตกต่างกันในระดับสายตาและในเชิงค่าตัวเลขข้อมูลพิกเซลหรือไม่ย่างไร?**\n",
  "\n",
  "**ตอบ:** ไม่เห็นความแตกต่างระดับสายตา แต่ละระดับเชิงค่าตัวเลขมีต่างกันเล็กน้อย +- ไม่เกิน 1-2 พิกเซล"
 ]
}

# Insert the Q&A for task 2 after the second code cell
qa2 = {
 "cell_type": "markdown",
 "metadata": {},
 "source": [
  "### คำถามท้ายการทดลองข้อที่ 2\n",
  "**อธิบายว่าการสับเปลี่ยนสัญกรณ์แชนเนลสีจาก BGR เป็น RGB ส่งผลกระทบอย่างไรต่องานประเภทสกัดวัตถุที่มีสีเฉพาะเจาะจง?**\n",
  "\n",
  "**ตอบ:** การสับเปลี่ยนสัญกรณ์แชนเนลสีจาก BGR เป็น RGB ส่งผลกระทบต่องานสกัดวัตถุที่มีสีเฉพาะเจาะจงอย่างมีนัยสำคัญ เนื่องจาก OpenCV อ่านภาพในรูปแบบ BGR ตามค่าเริ่มต้น หากผู้อ้างอิง index แชนเนลโดยไม่แปลงรูปแบบก่อน จะทำให้การ threshold ผิดแชนเนล"
 ]
}

# Add qa1 after the first code cell (which is at index 1)
# Add qa2 after the second code cell (which will be at index 3)

new_cells = []
code_cell_count = 0
for cell in nb['cells']:
    new_cells.append(cell)
    if cell['cell_type'] == 'code':
        code_cell_count += 1
        if code_cell_count == 1:
            new_cells.append(qa1)
        elif code_cell_count == 2:
            new_cells.append(qa2)

nb['cells'] = new_cells

with open('lab1_assignment.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("Lab 1 updated with Q&A")
