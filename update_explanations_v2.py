import json
import os
import re

files = ["lab2_assignment (2).ipynb", "LAB_3 (1) (1).ipynb", "lab4_assignment.ipynb"]

for f in files:
    if not os.path.exists(f):
        print(f"File {f} not found.")
        continue
        
    with open(f, 'r', encoding='utf-8') as file:
        nb = json.load(file)
    
    new_cells = []
    for cell in nb.get('cells', []):
        # Remove the previously added markdown explanations
        if cell['cell_type'] == 'markdown':
            source = "".join(cell.get('source', []))
            if '<div style="background: rgba(255,255,255,0.4)' in source and '🔍 คำอธิบายโค้ดส่วนนี้' in source:
                # Skip adding this cell (i.e. delete it)
                continue
                
        # For code cells, let's try to append some simple line-by-line comments if they don't exist
        # But to be safe and avoid corrupting complex code, we will just keep them as they are
        # unless we specifically match certain known opencv functions.
        if cell['cell_type'] == 'code':
            source_lines = cell.get('source', [])
            new_source = []
            for line in source_lines:
                # Add basic line-by-line explanation for common lines if it lacks a comment
                if '#' not in line:
                    if 'cv2.imread' in line:
                        line = line.rstrip('\n') + ' # ใช้คำสั่ง cv2.imread เพื่อโหลดรูปภาพเข้ามาในหน่วยความจำ\n'
                    elif 'plt.imshow' in line:
                        line = line.rstrip('\n') + ' # แสดงผลรูปภาพบนกราฟของ matplotlib\n'
                    elif 'cv2.cvtColor' in line:
                        line = line.rstrip('\n') + ' # แปลงสเปซสี (Color Space) ของภาพ เช่น BGR เป็น RGB หรือ Grayscale\n'
                    elif 'plt.show()' in line:
                        line = line.rstrip('\n') + ' # สั่งเรนเดอร์และแสดงกราฟทั้งหมดออกทางหน้าจอ\n'
                    elif 'np.clip' in line:
                        line = line.rstrip('\n') + ' # ใช้ np.clip จำกัดค่าพิกเซลไม่ให้ต่ำกว่า 0 หรือเกิน 255\n'
                    elif 'cv2.filter2D' in line:
                        line = line.rstrip('\n') + ' # ใช้ cv2.filter2D นำเคอร์เนลมาคอนโวลูชันกับภาพ\n'
                    elif 'cv2.calcHist' in line:
                        line = line.rstrip('\n') + ' # คำนวณค่าฮิสโตแกรมความถี่ของพิกเซลแต่ละระดับสี\n'
                new_source.append(line)
            cell['source'] = new_source
            
        new_cells.append(cell)
    
    nb['cells'] = new_cells
    
    with open(f, 'w', encoding='utf-8') as file:
        json.dump(nb, file, ensure_ascii=False, indent=1)

print("Old generic explanations removed from all notebooks, and basic inline comments added.")
