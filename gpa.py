import streamlit as st

def get_theory_gpa(marks):
    if 86 <= marks <= 100:
        return 4.00
    elif 80 <= marks <= 85:
        return 3.66
    elif 75 <= marks <= 79:
        return 3.33
    elif 70 <= marks <= 74:
        return 3.00
    elif 67 <= marks <= 69:
        return 2.66
    elif 63 <= marks <= 66:
        return 2.33
    elif 60 <= marks <= 62:
        return 2.00
    elif 57 <= marks <= 59:
        return 1.66
    elif 54 <= marks <= 56:
        return 1.30
    elif 50 <= marks <= 53:
        return 1.00
    else:
        return 0.00

def get_lab_gpa(marks):
    if 43 <= marks <= 50:
        return 4.00
    elif 40 <= marks <= 42:
        return 3.66
    elif 38 <= marks <= 39:
        return 3.33
    elif 35 <= marks <= 37:
        return 3.00
    elif 33 <= marks <= 34:
        return 2.66
    elif 31 <= marks <= 32:
        return 2.33
    elif marks == 30:
        return 2.00
    elif 28 <= marks <= 29:
        return 1.66
    elif 26 <= marks <= 27:
        return 1.30
    elif marks == 25:
        return 1.00
    else:
        return 0.00

def get_valid_marks(prompt, min_val, max_val, key):
    marks_input = st.text_input(prompt, key=key, placeholder=f"Enter marks ({min_val}-{max_val})")
    if marks_input == "":
        return None
    try:
        marks = float(marks_input)
        if marks < min_val or marks > max_val:
            st.error(f"⚠️ Marks must be between {min_val} and {max_val}")
            return None
        return marks
    except ValueError:
        st.error("❌ Please enter a valid number")
        return None

def main():
    st.set_page_config(page_title="SSUET GPA Calculator", page_icon="🎓", layout="centered")

    st.markdown("""
    <style>
    /* Global font & background */
    body, .reportview-container, .main {
        background: #FAFAFA;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Container */
    .container {
        max-width: 680px;
        margin: 2.5rem auto 3rem auto;
        padding: 2rem 2.5rem 2.5rem 2.5rem;
        background: #fff;
        border-radius: 20px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.08);
    }
    /* Heading */
    h1 {
        font-weight: 900;
        font-size: 2.8rem;
        color: #5B3E8B;
        text-align: center;
        margin-bottom: 0.2rem;
        letter-spacing: 1.3px;
    }
    /* Subtitle */
    .subtitle {
        color: #708238;
        font-size: 1.25rem;
        font-weight: 600;
        text-align: center;
        margin-bottom: 2rem;
        letter-spacing: 0.5px;
        font-style: italic;
    }
    /* Section Headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #5B3E8B;
        border-bottom: 3px solid #5B3E8B;
        padding-bottom: 8px;
        margin-top: 2.2rem;
        margin-bottom: 1.2rem;
        letter-spacing: 0.8px;
    }
    /* Input boxes */
    input[type="text"] {
        border: 2.5px solid #708238;
        border-radius: 10px;
        padding: 12px;
        font-size: 1.1rem;
        transition: border-color 0.3s ease;
        width: 100%;
        box-sizing: border-box;
        margin-bottom: 0.8rem;
    }
    input[type="text"]:focus {
        border-color: #5B3E8B;
        outline: none;
        box-shadow: 0 0 12px rgba(91,62,139,0.5);
    }
    /* Select boxes */
    div[role="listbox"] {
        border: 2.5px solid #708238 !important;
        border-radius: 10px !important;
        padding-left: 10px !important;
        font-size: 1.1rem !important;
        width: 100% !important;
        box-sizing: border-box;
        margin-bottom: 0.9rem;
    }
    /* Buttons */
    div.stButton {
        text-align: center !important;
        margin-top: 2.8rem;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #5B3E8B, #7A58B3) !important;
        color: white !important;
        font-size: 1.25rem !important;
        font-weight: 700 !important;
        padding: 0.85rem 3.2rem !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 8px 20px rgba(123,88,179,0.45);
        cursor: pointer;
        transition: all 0.35s ease;
        display: inline-block !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }
    div.stButton > button:hover {
        background: linear-gradient(135deg, #7A58B3, #5B3E8B) !important;
        box-shadow: 0 10px 30px rgba(123,88,179,0.6);
        transform: scale(1.05);
    }
    /* Footer creative styling */
    footer {
        margin-top: 3.2rem;
        text-align: center;
        font-style: italic;
        font-weight: 600;
        color: #708238;
        font-size: 1rem;
        border-top: 1.7px solid #d1d1d6;
        user-select:none;
        letter-spacing: 0.6px;
        padding: 0.8rem 1rem;
        background: #f0f5e8;
        border-radius: 15px 15px 0 0;
        box-shadow: 0 -2px 8px rgba(112,130,56,0.2);
        opacity: 0;
        animation: fadeInUp 1s ease forwards;
    }
    .footer-content {
        display: inline-block;
    }
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    /* Expander headers */
    .streamlit-expanderHeader {
        font-weight: 700 !important;
        font-size: 1.35rem !important;
        color: #5B3E8B !important;
        letter-spacing: 0.8px !important;
    }
    /* Warnings & errors */
    .stError, .stWarning {
        font-weight: 600;
        font-size: 1rem;
        color: #B00020 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="container">', unsafe_allow_html=True)

    st.markdown("<h1>Sir Syed University GPA Calculator</h1>", unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Calculate your overall GPA based on multiple theory and lab courses.</p>', unsafe_allow_html=True)

    total_weighted_gpa_points = 0.0
    total_credit_hours = 0

    with st.expander("Theory Courses", expanded=True):
        n_theory = st.number_input("Number of theory courses", min_value=0, step=1, key="n_theory")
        for i in range(int(n_theory)):
            st.markdown(f'<div class="section-header">Theory Course {i+1}</div>', unsafe_allow_html=True)

            credit_options = [0, 2, 3]
            credit_hr = st.selectbox(
                f"Credit hour for Theory Course {i+1}",
                options=credit_options,
                format_func=lambda x: "Select" if x == 0 else str(x),
                key=f"credit_{i}"
            )
            if credit_hr == 0:
                st.warning("⚠️ Please select a valid credit hour (2 or 3).")
                continue

            marks = get_valid_marks(
                f"Marks obtained (0-100) for Theory Course {i+1}", 0, 100, key=f"marks_{i}"
            )
            if marks is None:
                st.warning("⚠️ Enter valid marks to calculate GPA for this course.")
                continue

            gpa = get_theory_gpa(marks)
            weighted_gpa = gpa * credit_hr
            total_weighted_gpa_points += weighted_gpa
            total_credit_hours += credit_hr

    st.write("---")

    with st.expander("Lab Courses", expanded=False):
        n_lab = st.number_input("Number of lab courses", min_value=0, step=1, key="n_lab")
        for i in range(int(n_lab)):
            st.markdown(f'<div class="section-header">Lab Course {i+1}</div>', unsafe_allow_html=True)

            marks = get_valid_marks(
                f"Marks obtained (0-50) for Lab Course {i+1}", 0, 50, key=f"lab_marks_{i}"
            )
            if marks is None:
                st.warning("⚠️ Enter valid marks to calculate GPA for this lab course.")
                continue

            gpa = get_lab_gpa(marks)
            weighted_gpa = gpa * 1
            total_weighted_gpa_points += weighted_gpa
            total_credit_hours += 1

    if st.button("Calculate GPA", key="calculate_btn"):
        if total_credit_hours == 0:
            st.error("❌ Please enter at least one valid course with proper credit hours and marks.")
        else:
            final_gpa = total_weighted_gpa_points / total_credit_hours
            st.success(f"🎉 Your Overall GPA is: {final_gpa:.2f}")
            st.write(f"• Total Weighted GPA Points: {total_weighted_gpa_points:.2f}")
            st.write(f"• Total Credit Hours: {total_credit_hours}")

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
        <footer>
          <div class="footer-content">
            &copy; 2025 Sir Syed University GPA Calculator | Made by Ammar Ahmed ✨
          </div>
        </footer>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
