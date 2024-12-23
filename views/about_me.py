import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()

col1, col2, col3, col4 = st.columns(4, gap="small", vertical_alignment="center")

with col1:
    st.image("./assets/MigrantCoin.gif",)

    with col2:
        st.title(" Owner 🧨🧨 💣Tuturas Cosmin", anchor=False)
        st.write("Senior Data Analyst,  assisting enterprises by supporting data-driven decision-making.")
        
        
        with col3:
                st.image("./assets/Mig2.png")
                st.title("Don't miss up ours")
                 
                with col4:
                     st.image("./assets/Screenshot_1.png")
                     st.title("Back in Time !")

if st.button("📢 Contact Me"):
                         show_contact_form()


st.link_button("My X", "https://x.com/Migrantcoinof")

            


