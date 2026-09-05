import streamlit as st
from difflib import SequenceMatcher

# ==========================================
# 1. ข้อมูลโจทย์ออร์แกเนลล์
# ==========================================
CELL_DATA = [
    {
        "question": "ข้อที่ 1: ออร์แกเนลล์ศูนย์กลางของเซลล์ บรรจุสารพันธุกรรม (DNA) ไว้ภายใน",
        "hint": "คำใบ้: ทำหน้าที่ควบคุมการทำงานของเซลล์และการถ่ายทอดลักษณะทางพันธุกรรม",
        "link": "https://th.wikipedia.org/wiki/นิวเคลียส_(ชีววิทยา)",
        "answer": "นิวเคลียส"
    },
    {
        "question": "ข้อที่ 2: ออร์แกเนลล์ที่มีเยื่อหุ้ม 2 ชั้น เปรียบเสมือน \"โรงไฟฟ้าของเซลล์\"",
        "hint": "คำใบ้: ทำหน้าที่สร้างพลังงาน ATP ผ่านกระบวนการหายใจระดับเซลล์",
        "link": "https://th.wikipedia.org/wiki/ไมโทคอนเดรีย",
        "answer": "ไมโทคอนเดรีย"
    },
    {
        "question": "ข้อที่ 3: ออร์แกเนลล์สีเขียวพบเฉพาะในเซลล์พืชและสาหร่ายบางชนิด",
        "hint": "คำใบ้: บรรจุคลอโรฟิลล์ ทำหน้าที่สังเคราะห์ด้วยแสงเพื่อสร้างอาหารให้พืช",
        "link": "https://th.wikipedia.org/wiki/คลอโรพลาสต์",
        "answer": "คลอโรพลาสต์"
    },
    {
        "question": "ข้อที่ 4: ออร์แกเนลล์ขนาดเล็กที่ไม่มีเยื่อหุ้ม อาจลอยอิสระหรือเกาะบน ER",
        "hint": "คำใบ้: ทำหน้าที่สังเคราะห์โปรตีนเพื่อนำไปใช้ภายในและภายนอกเซลล์",
        "link": "https://th.wikipedia.org/wiki/ไรโบโซม",
        "answer": "ไรโบโซม"
    },
    {
        "question": "ข้อที่ 5: โครงสร้างแข็งแรงภายนอกเยื่อหุ้มเซลล์ พบในเซลล์พืช แต่ไม่พบในเซลล์สัตว์",
        "hint": "คำใบ้: มีเซลลูโลสเป็นองค์ประกอบหลัก ช่วยค้ำจุนและให้ความแข็งแรงแก่เซลล์",
        "link": "https://th.wikipedia.org/wiki/ผนังเซลล์",
        "answer": "ผนังเซลล์"
    },
    {
        "question": "ข้อที่ 6: ถุงบรรจุสารที่มีขนาดใหญ่มากในเซลล์พืช ใช้เก็บสะสมน้ำและสารต่าง ๆ",
        "hint": "คำใบ้: ในเซลล์พืชเรียกว่า Central Vacuole ช่วยรักษาแรงดันเต่งของเซลล์",
        "link": "https://th.wikipedia.org/wiki/แวคิวโอล",
        "answer": "แวคิวโอล"
    },
    {
        "question": "ข้อที่ 7: ออร์แกเนลล์ถุงบรรจุเอนไซม์ย่อยอาหาร ทำหน้าที่ย่อยสิ่งแปลกปลอมและเซลล์ที่หมดอายุ",
        "hint": "คำใบ้: เปรียบเสมือนระบบกำจัดขยะของเซลล์ (พบมากในเซลล์สัตว์)",
        "link": "https://th.wikipedia.org/wiki/ไลโซโซม",
        "answer": "ไลโซโซม"
    },
    {
        "question": "ข้อที่ 8: ออร์แกเนลล์ที่มีลักษณะเป็นถุงแบนซ้อนกัน ทำหน้าที่ปรับแต่งและแพ็กโปรตีนส่งออกนอกเซลล์",
        "hint": "คำใบ้: เปรียบเสมือนไปรษณีย์หรือระบบขนส่งของเซลล์ (Golgi Body / Golgi Complex)",
        "link": "https://th.wikipedia.org/wiki/กอลจิแอปพาราตัส",
        "answer": "กอลจิบอดี"
    }
]

# ==========================================
# 2. ฟังก์ชันระบบตรวจคำตอบแบบยืดหยุ่น
# ==========================================
def is_answer_correct(user_answer: str, correct_answer: str, threshold: float = 0.70) -> bool:
    clean_user = user_answer.strip().lower()
    clean_correct = correct_answer.strip().lower()

    if clean_user == clean_correct or clean_correct in clean_user:
        return True

    similarity = SequenceMatcher(None, clean_user, clean_correct).ratio()
    return similarity >= threshold

# ==========================================
# 3. จัดการ State และ Web UI
# ==========================================
st.set_page_config(page_title="เกมทายออร์แกเนลล์ของเซลล์", page_icon="🧪")

if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False

st.title("🧪 เกมทายออร์แกเนลล์ของเซลล์ 🔬")

if not st.session_state.game_over:
    q_idx = st.session_state.current_index
    current_q = CELL_DATA[q_idx]

    st.subheader(current_q["question"])
    st.info(current_q["hint"])
    st.markdown(f"🌐 [กดตรงนี้เพื่ออ่านหน้าที่ของออร์แกเนลล์แบบละเอียด]({current_q['link']})")

    # ช่องกรอกคำตอบ
    user_input = st.text_input("พิมพ์คำตอบของคุณที่นี่:", key=f"input_{q_idx}")

    if st.button("ส่งคำตอบ"):
        if not user_input.strip():
            st.warning("กรุณาพิมพ์คำตอบก่อนส่งครับ!")
        else:
            if is_answer_correct(user_input, current_q["answer"]):
                st.session_state.score += 1
                st.success(f"ถูกต้อง! 🎉 (คำตอบมาตรฐาน: {current_q['answer']})")
            else:
                st.error(f"ยังไม่ถูกนะ! คำตอบที่ถูกต้องคือ: {current_q['answer']}")

            if q_idx + 1 < len(CELL_DATA):
                st.session_state.current_index += 1
                st.button("ทำข้อถัดไป ➡️")
            else:
                st.session_state.game_over = True
                st.button("ดูสรุปคะแนน 🏁")

    st.caption(f"คะแนนปัจจุบัน: {st.session_state.score} / {len(CELL_DATA)}")

else:
    st.balloons()
    st.header("🎉 จบเกมเรียบร้อยแล้ว!")
    st.subheader(f"คุณทำคะแนนได้ทั้งหมด: {st.session_state.score} / {len(CELL_DATA)} คะแนน")
    
    if st.button("เริ่มเล่นใหม่อีกครั้ง 🔄"):
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.game_over = False
        st.rerun()