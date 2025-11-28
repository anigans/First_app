# File: app.py
# Run:  streamlit run app.py
# Purpose: Practice adding up to 3-digit numbers (kid-friendly, simple)

import random
import streamlit as st

# ---------------- Page setup ----------------
st.set_page_config(page_title="Add Up to 3 Digits", page_icon="➕")
st.title("➕ Add Up to 3-Digit Numbers")
st.caption("Pick difficulty, solve the problem, and check your answer!")

# ---------------- Sidebar controls ----------------
st.sidebar.header("Settings")
digits = st.sidebar.selectbox("Number of digits", [1, 2, 3], index=2)
no_carry = st.sidebar.checkbox("Make problems with NO carrying", value=False)
show_work = st.sidebar.checkbox("Show vertical addition (hint)", value=True)

# ---------------- Helpers ----------------
def has_carry(a: int, b: int) -> bool:
    """Return True if any column (ones/tens/hundreds) causes a carry."""
    x, y = a, b
    for _ in range(3):  # check up to hundreds place
        if (x % 10) + (y % 10) >= 10:
            return True
        x //= 10
        y //= 10
    return False

def make_problem(digs: int, need_no_carry: bool) -> tuple[int, int]:
    """Make two random numbers of the chosen digit length.
    If need_no_carry=True, ensure there is no carrying."""
    lo = 1 if digs == 1 else 10 ** (digs - 1)
    hi = (10 ** digs) - 1
    # Try a few times to find a no-carry pair if requested
    for _ in range(500):
        a = random.randint(lo, hi)
        b = random.randint(lo, hi)
        if need_no_carry and has_carry(a, b):
            continue
        return a, b
    # Fallback: return whatever we got
    return random.randint(lo, hi), random.randint(lo, hi)

def vertical_addition(a: int, b: int) -> str:
    """Return a simple vertical addition layout as a string."""
    s_a, s_b = str(a), str(b)
    width = max(len(s_a), len(s_b)) + 2  # padding for the + sign
    top = s_a.rjust(width)
    bottom = ("+ " + s_b).rjust(width)
    line = "-" * width
    return f"```\n{top}\n{bottom}\n{line}\n```"

# ---------------- Session state ----------------
if "a" not in st.session_state:
    st.session_state.a, st.session_state.b = make_problem(digits, no_carry)
if "score" not in st.session_state:
    st.session_state.score = 0
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

# If settings change, make a fresh problem that matches them
if st.sidebar.button("🔄 New Problem"):
    st.session_state.a, st.session_state.b = make_problem(digits, no_carry)

# ---------------- Problem display ----------------
a, b = st.session_state.a, st.session_state.b
st.subheader("Solve this:")
st.write(f"**{a} + {b} = ?**")

if show_work:
    st.markdown(vertical_addition(a, b))

# ---------------- Answer input + Check ----------------
user_answer = st.text_input("Your answer (numbers only):", value="", placeholder="Type your sum here")
check = st.button("✅ Check Answer")

if check:
    try:
        ans = int(user_answer.strip())
        correct = a + b
        st.session_state.attempts += 1
        if ans == correct:
            st.session_state.score += 1
            st.success(f"🎉 Correct! {a} + {b} = {correct}")
            # Auto-generate a fresh problem for next attempt
            st.session_state.a, st.session_state.b = make_problem(digits, no_carry)
        else:
            st.error(f"Not quite. Try again!")
            with st.expander("See the answer"):
                st.info(f"Correct answer: **{correct}**")
    except ValueError:
        st.warning("Please enter whole numbers only (e.g., 247).")

# ---------------- Progress ----------------
st.divider()
st.caption(f"Score: **{st.session_state.score}** correct out of **{st.session_state.attempts}** checks.")
st.caption("Tip: Use the sidebar to change difficulty or to get a new problem.")
