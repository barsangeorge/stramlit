import streamlit as st

about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,

)

project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)





#st.link_button("Go to gallery", "https://streamlit.io/gallery")



# pg = st.navigation(pages=[about_page, project_1_page,project_2_page])

pg = st.navigation(
    
    {
        "info": [about_page],
        "projects": [project_2_page,] 
        
   }    

)


st.logo("assets/T1.jpg",size="large",)
st.sidebar.markdown("Support the transfer foreign !!!")



pg.run()