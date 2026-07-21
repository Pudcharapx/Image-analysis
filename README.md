# Image Analysis Lab

คลังเก็บโค้ด (Repository) นี้รวบรวมงานปฏิบัติการและแบบทดลองเกี่ยวกับ **Image Analysis** (การวิเคราะห์และประมวลผลภาพดิจิทัล) โดยใช้ Python, OpenCV และ 라이บรารีต่างๆ ที่เกี่ยวข้องกับ Data Science และ Computer Vision

## 🌟 จุดเด่นของโปรเจกต์
- รวบรวมงานปฏิบัติการต่างๆ ในรูปแบบ **Jupyter Notebook (`.ipynb`)** พร้อมแสดงผลเป็น **HTML** ที่สามารถเปิดอ่านผ่านเบราว์เซอร์ได้ทันที
- หน้าต่างแสดงผลหลัก (`index.html`) ออกแบบด้วย UI สไตล์ **Glassmorphism** ที่มีความสวยงาม ทันสมัย และอ่านง่าย
- ภายในหน้ารายงาน Lab แต่ละส่วน มีการแทรก **คำอธิบายโค้ด** (Code Explanations) ไว้อย่างละเอียด เพื่อให้ง่ายต่อการทำความเข้าใจการทำงานของแต่ละชุดคำสั่ง

## 📂 โครงสร้างของ Lab และเนื้อหา

โปรเจกต์นี้ประกอบด้วยงานปฏิบัติการหลัก 3 ส่วน ได้แก่:

### 1. Lab 2: พื้นฐานภาพและพิกเซล (Image Basics)
- **ไฟล์:** `lab2_assignment (2).ipynb` / `lab2.html`
- **เนื้อหา:** 
  - การอ่านและแสดงผลไฟล์ภาพสี/Grayscale
  - การเข้าถึงและการแก้ไขค่าพิกเซลแบบตรงๆ (Pixel manipulation)
  - การกำหนดพื้นที่สนใจ (Region of Interest - ROI)
  - การประยุกต์ใช้ Image Thresholding พื้นฐาน

### 2. Lab 3: ฮิสโตแกรมและการปรับความสว่าง (Histograms & Contrast)
- **ไฟล์:** `LAB_3 (1) (1).ipynb` / `lab3.html`
- **เนื้อหา:**
  - การประมวลผล Gamma Correction เพื่อปรับความสว่างภาพ
  - การคำนวณและวิเคราะห์กราฟฮิสโตแกรม (Histogram) และฟังก์ชันการแจกแจงสะสม (CDF)
  - การทำ Contrast Stretching และ Histogram Equalization

### 3. Lab 4: การกรองสัญญาณรบกวนและความคมชัด (Filtering & Sharpening)
- **ไฟล์:** `lab4_assignment.ipynb` / `lab4.html`
- **ไฟล์วิเคราะห์:** `Lab4 discussion report.md`
- **เนื้อหา:**
  - การใช้งานตัวกรอง Box Filter และ Median Filter เพื่อลดสัญญาณรบกวน (Salt & Pepper Noise)
  - การทำ Laplacian Sharpening เพื่อเน้นขอบและความคมชัดของภาพ
  - การจัดการปัญหาค่าพิกเซลล้น (Overflow) ด้วยฟังก์ชัน `numpy.clip()`

## 🛠️ โครงสร้างไฟล์ในโปรเจกต์
- `index.html`: หน้าหลักสำหรับการนำทาง (Navigation Page) ที่ถูกออกแบบสไตล์ Glassmorphism
- `add_explanations.py`: สคริปต์ Python อรรถประโยชน์สำหรับใช้วิเคราะห์โค้ดในไฟล์ Notebook และแทรกบล็อกคำอธิบาย (Markdown) ให้อัตโนมัติ ก่อนที่จะแปลงเป็น HTML
- `*.ipynb`: ไฟล์ซอร์สโค้ด Jupyter Notebook ดั้งเดิม
- `*.html`: ไฟล์ Notebook ที่ถูกแปลงเป็น HTML สำหรับแสดงผลบนเว็บ

## 🚀 วิธีการรันและแสดงผล

1. **เปิดอ่านแบบเว็บไซต์:** 
   คุณสามารถดับเบิลคลิกไฟล์ `index.html` เพื่อเปิดหน้าหลักบนเบราว์เซอร์ และสามารถคลิกนำทางไปยัง Lab ต่างๆ ได้ทันที
2. **แก้ไขและรันโค้ด:**
   - ติดตั้ง Jupyter Notebook หรือ JupyterLab
   - รันคำสั่ง `jupyter notebook` ในโฟลเดอร์นี้
   - เปิดไฟล์ `.ipynb` ที่ต้องการเพื่อแก้ไขและรันโค้ด
3. **อัปเดตคำอธิบายและสร้าง HTML ใหม่:**
   หากคุณแก้ไขโค้ดในไฟล์ `.ipynb` และต้องการสร้างไฟล์ `.html` ใหม่ที่มีคำอธิบายแทรกอยู่ ให้รันคำสั่งต่อไปนี้ใน Terminal:
   ```bash
   python add_explanations.py
   jupyter nbconvert --to html "lab2_assignment (2).ipynb" --output lab2.html
   jupyter nbconvert --to html "LAB_3 (1) (1).ipynb" --output lab3.html
   jupyter nbconvert --to html "lab4_assignment.ipynb" --output lab4.html
   ```

---
*© 2026 Image Analysis Lab.*
