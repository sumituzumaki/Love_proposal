import streamlit as st
from streamlit.components.v1 import html

# Page config
st.set_page_config(page_title="Pyaar Bhara Proposal ❤️", layout="centered")

# Injecting full HTML + CSS + JS
html("""
<style>
body {
    background-color: #001d3d;
    color: white;
    overflow: hidden;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
.firefly {
    position: absolute;
    width: 6px;
    height: 6px;
    background: yellow;
    border-radius: 50%;
    box-shadow: 0 0 20px yellow;
    animation: fly 10s linear infinite;
    z-index: 0;
}
@keyframes fly {
    0% { transform: translate(0, 0); opacity: 1; }
    100% { transform: translate(500px, -500px); opacity: 0; }
}
.heart {
    font-size: 48px;
    animation: pulse 1s infinite;
    text-align: center;
    margin-bottom: 10px;
}
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.3); }
    100% { transform: scale(1); }
}
.container {
    position: relative;
    height: 100vh;
    text-align: center;
    padding-top: 20vh;
    z-index: 1;
    padding-left: 5vw;
    padding-right: 5vw;
}
.button-style {
    background-color: #ffafcc;
    border: none;
    padding: 10px 20px;
    font-size: 20px;
    margin: 10px;
    border-radius: 8px;
    cursor: pointer;
    transition: 0.3s ease-in-out;
}
#no-button {
    position: absolute;
}
@media only screen and (max-width: 600px) {
    .heart { font-size: 36px; }
    .button-style { font-size: 18px; padding: 8px 16px; }
    h2, h3 { font-size: 18px; }
}
</style>

<div class="container">
    <div class="heart">❤️</div>
    <h2 style="margin-bottom: 10px;">Hii.. mai tumhara naam janta hoon but naam nahi lunga...</h2>
    <h3 style="margin-bottom: 20px;">baat ye hi ki mai tumse bahut pasand karta hoon kya tum mujhe apna banaogi?</h3>
    <button onclick="handleYes()" class="button-style">YES ❤️</button>
    <button id="no-button" class="button-style" onmouseover="runAway()">NO 😅</button>
</div>

<script>
function runAway() {
    const btn = document.getElementById("no-button");
    btn.style.left = Math.random() * 80 + "%";
    btn.style.top = Math.random() * 80 + "%";
}
function handleYes() {
    const msg = document.createElement("div");
    msg.innerHTML = "<h3 style='color: #ffccff; margin-top: 20px;'>Thanks you meri jaan 💘 , Welcome Naruto ki hinata 💘</h3>";
    document.querySelector(".container").appendChild(msg);
}
for (let i = 0; i < 60; i++) {
    let f = document.createElement("div");
    f.className = "firefly";
    f.style.top = Math.random() * 100 + "vh";
    f.style.left = Math.random() * 100 + "vw";
    f.style.animationDelay = Math.random() * 10 + "s";
    f.style.animationDuration = (5 + Math.random() * 5) + "s";
    document.body.appendChild(f);
}
</script>
""", height=700)
