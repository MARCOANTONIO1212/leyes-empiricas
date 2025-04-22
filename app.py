import streamlit as st
st.image("quimica2.jpeg")


st.set_page_config(page_title="Leyes Empíricas de los Gases Ideales", layout="centered")

st.title("🌡️ Leyes Empíricas de los Gases Ideales")
st.write("Selecciona una ley y proporciona los datos conocidos. Deja en blanco el que deseas calcular.")

ley = st.selectbox("Selecciona la ley de los gases", [
    "Ley de Boyle-Mariotte (P·V = constante)",
    "Ley de Charles (V/T = constante)",
    "Ley de Gay-Lussac (P/T = constante)"
])

def resolver_boyle(p1, v1, p2, v2):
    if p1 is None:
        return round(p2 * v2 / v1, 2)
    if v1 is None:
        return round(p2 * v2 / p1, 2)
    if p2 is None:
        return round(p1 * v1 / v2, 2)
    if v2 is None:
        return round(p1 * v1 / p2, 2)

def resolver_charles(v1, t1, v2, t2):
    if v1 is None:
        return round(v2 * t1 / t2, 2)
    if t1 is None:
        return round(t2 * v1 / v2, 2)
    if v2 is None:
        return round(v1 * t2 / t1, 2)
    if t2 is None:
        return round(t1 * v2 / v1, 2)

def resolver_gay_lussac(p1, t1, p2, t2):
    if p1 is None:
        return round(p2 * t1 / t2, 2)
    if t1 is None:
        return round(t2 * p1 / p2, 2)
    if p2 is None:
        return round(p1 * t2 / t1, 2)
    if t2 is None:
        return round(t1 * p2 / p1, 2)

if ley == "Ley de Boyle-Mariotte (P·V = constante)":
    st.subheader("Presión en mmHg, Volumen en mL")
    p1 = st.number_input("P₁ (mmHg)", format="%.2f", step=0.1, key="p1") or None
    v1 = st.number_input("V₁ (mL)", format="%.2f", step=0.1, key="v1") or None
    p2 = st.number_input("P₂ (mmHg)", format="%.2f", step=0.1, key="p2") or None
    v2 = st.number_input("V₂ (mL)", format="%.2f", step=0.1, key="v2") or None

    if st.button("Calcular"):
        resultado = resolver_boyle(p1, v1, p2, v2)
        st.success(f"Resultado: {resultado}")

elif ley == "Ley de Charles (V/T = constante)":
    st.subheader("Volumen en mL, Temperatura en K")
    v1 = st.number_input("V₁ (mL)", format="%.2f", step=0.1, key="cv1") or None
    t1 = st.number_input("T₁ (K)", format="%.2f", step=0.1, key="ct1") or None
    v2 = st.number_input("V₂ (mL)", format="%.2f", step=0.1, key="cv2") or None
    t2 = st.number_input("T₂ (K)", format="%.2f", step=0.1, key="ct2") or None

    if st.button("Calcular"):
        resultado = resolver_charles(v1, t1, v2, t2)
        st.success(f"Resultado: {resultado}")

elif ley == "Ley de Gay-Lussac (P/T = constante)":
    st.subheader("Presión en mmHg, Temperatura en K")
    p1 = st.number_input("P₁ (mmHg)", format="%.2f", step=0.1, key="gp1") or None
    t1 = st.number_input("T₁ (K)", format="%.2f", step=0.1, key="gt1") or None
    p2 = st.number_input("P₂ (mmHg)", format="%.2f", step=0.1, key="gp2") or None
    t2 = st.number_input("T₂ (K)", format="%.2f", step=0.1, key="gt2") or None

    if st.button("Calcular"):
        resultado = resolver_gay_lussac(p1, t1, p2, t2)
        st.success(f"Resultado: {resultado}")
