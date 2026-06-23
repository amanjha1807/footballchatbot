import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage


from chainbuilder import chain



from typing import List, Optional, Literal
from pydantic import BaseModel


class FootballResponse(BaseModel):
    response_type: Literal["chat", "player"]

    answer: str

    player_name: Optional[str] = None
    club: Optional[str] = None
    position: Optional[str] = None
    achievements: Optional[List[str]] = None

# chain_builder.py


from llm import llm
from template import prompt
from schema import FootballResponse

structured_llm = llm.with_structured_output(FootballResponse)

chain = prompt | structured_llm



# app.py

import streamlit as st
from chainbuilder import chain
from langchain_core.messages import HumanMessage, AIMessage


st.set_page_config(
    page_title="Football Expert AI",
    page_icon="⚽",
    layout="wide"
)


st.markdown("""
<style>

.stApp{
background-color:#0E1117;
}

.block-container{
padding-top:2rem;
}

.hero{
padding:25px;
border-radius:20px;
background:linear-gradient(135deg,#1d2671,#c33764);
text-align:center;
color:white;
}

.player-card{
background:#1B1E23;
padding:20px;
border-radius:20px;
border:1px solid #333;
}

.summary-card{
background:#161A1F;
padding:20px;
border-radius:20px;
}

</style>
""", unsafe_allow_html=True)


with st.sidebar:

    st.title("⚽ Football Expert AI")

    st.markdown("---")

    st.markdown("""
### 🌟 Features

✅ Memory

✅ Player Profiles

✅ World Cup Discussion

✅ Achievements

✅ AI Analyst

---
Built using Gemini + LangChain ❤️
""")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages=[]
        st.session_state.history=[]
        st.rerun()

# =====================
# Hero Section
# =====================
st.markdown("""
<div class='hero'>
<h1>⚽ Football Expert AI</h1>
<p>Your Personal Football Analyst 🏆</p>
</div>
""",unsafe_allow_html=True)

st.write("")

# =====================
# Session State
# =====================
if "messages" not in st.session_state:
    st.session_state.messages=[]

if "history" not in st.session_state:
    st.session_state.history=[]

# =====================
# Display old chats
# =====================
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =====================
# Chat Input
# =====================
query=st.chat_input(
"Ask about players, tactics, World Cup, clubs..."
)

# =====================
# Response
# =====================
if query:

    with st.chat_message("user"):
        st.markdown(query)

    st.session_state.messages.append(
        {
            "role":"user",
            "content":query
        }
    )

    with st.spinner("⚽ Thinking..."):

        response=chain.invoke(
        {
            "history":st.session_state.history,
            "query":query
        })

    with st.chat_message("assistant"):

        # PLAYER CARD
        if response.response_type=="player":

            st.markdown("## ⚽ Player Profile")

            c1,c2,c3=st.columns(3)

            with c1:
                st.metric(
                    "⚽ Player",
                    response.player_name
                )

            with c2:
                st.metric(
                    "🏟 Club",
                    response.club
                )

            with c3:
                st.metric(
                    "📍 Position",
                    response.position
                )

            if response.achievements:

                st.markdown("### 🏆 Achievements")

                for ach in response.achievements:
                    st.success(ach)

        st.markdown("### BOT")
        st.info(response.answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":response.answer
        }
    )

    st.session_state.history.append(
        HumanMessage(content=query)
    )

    st.session_state.history.append(
        AIMessage(content=response.answer)
    )
