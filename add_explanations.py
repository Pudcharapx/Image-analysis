import json
import re
import os

files = ["lab2_assignment (2).ipynb", "LAB_3 (1) (1).ipynb", "lab4_assignment.ipynb"]

for f in files:
    if not os.path.exists(f):
        print(f"File {f} not found.")
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        nb = json.load(file)
    
    new_cells = []
    for cell in nb.get('cells', []):
        if cell['cell_type'] == 'code':
            source = "".join(cell.get('source', []))
            if source.strip():
                # Analyze source to give a decent explanation
                explanation = "<div style=\"background: rgba(255,255,255,0.4); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.5); padding: 15px; border-radius: 12px; margin-bottom: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.05);\">\n"
                explanation += "<b>🔍 คำอธิบายโค้ดส่วนนี้:</b><ul>\n"
                
                added = False
                if "cv2.imread" in source:
                    explanation += "<li><b>อ่านรูปภาพ:</b> โหลดไฟล์ภาพเข้ามาในรูปแบบอาร์เรย์เพื่อเตรียมประมวลผล</li>\n"
                    added = True
                if "plt.hist" in source or "calcHist" in source:
                    explanation += "<li><b>วิเคราะห์ฮิสโตแกรม (Histogram):</b> คำนวณและพล็อตการกระจายตัวของค่าความสว่างพิกเซล</li>\n"
                    added = True
                if "cv2.filter2D" in source or "blur" in source or "medianBlur" in source:
                    explanation += "<li><b>กรองสัญญาณรบกวน (Filtering):</b> ใช้ Filter (เช่น Box หรือ Median) เพื่อทำ smoothing หรือลด noise ในภาพ</li>\n"
                    added = True
                if "Laplacian" in source or "sharpen" in source:
                    explanation += "<li><b>ปรับภาพให้คมชัด (Sharpening):</b> ใช้ Laplacian filter หรือ mask ในการเน้นขอบและรายละเอียดของภาพให้ชัดเจนขึ้น</li>\n"
                    added = True
                if "cv2.cvtColor" in source:
                    explanation += "<li><b>แปลงสเปซสี (Color Space):</b> เปลี่ยนรูปแบบสีของภาพ (เช่น จาก BGR เป็น RGB หรือ Grayscale)</li>\n"
                    added = True
                if "np.clip" in source:
                    explanation += "<li><b>จัดการค่าพิกเซลล้น (Overflow):</b> ใช้ numpy.clip เพื่อจำกัดค่าพิกเซลไม่ให้เกินช่วง [0, 255] ก่อนที่จะแสดงผล</li>\n"
                    added = True
                if "plt.subplot" in source or "plt.imshow" in source:
                    explanation += "<li><b>แสดงผลภาพ (Visualization):</b> ใช้ matplotlib เพื่อแสดงผลภาพหรือกราฟเปรียบเทียบ</li>\n"
                    added = True
                if "def " in source:
                    explanation += "<li><b>สร้างฟังก์ชัน (Function):</b> นิยามฟังก์ชันใหม่เพื่อนำไปเรียกใช้งานซ้ำลดความซ้ำซ้อนของโค้ด</li>\n"
                    added = True
                
                if not added:
                    explanation += "<li>โค้ดส่วนนี้รับหน้าที่คำนวณประมวลผลคำสั่ง, กำหนดตัวแปร, หรือจัดการข้อมูลอาร์เรย์สำหรับการวิเคราะห์ภาพเบื้องต้น</li>\n"
                
                explanation += "</ul></div>\n"
                
                md_cell = {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [explanation]
                }
                new_cells.append(md_cell)
        new_cells.append(cell)
    
    nb['cells'] = new_cells
    
    with open(f, 'w', encoding='utf-8') as file:
        json.dump(nb, file, ensure_ascii=False, indent=1)

print("Explanations added to all notebooks.")
