import json
from pathlib import Path
import streamlit as st

DATA = Path(__file__).parent / "data"

@st.cache_data
def load():
    playbooks = json.loads((DATA / "playbooks.json").read_text())
    cases = json.loads((DATA / "sample_cases.json").read_text())["cases"]
    return playbooks, cases

playbooks, cases = load()
pb_by_id = {p["id"]: p for p in playbooks["playbooks"]}

st.title("SOC Case Review Scorer (demo, fictional data)")

case_id = st.sidebar.selectbox("Select a case", [c["case_id"] for c in cases])
case = next(c for c in cases if c["case_id"] == case_id)
pb = pb_by_id[case["playbook_id"]]

st.header(f'{case["case_id"]}: {case["title"]}')
st.write(f'Playbook: {pb["name"]} | Severity: {case["severity"]} | Analyst: {case["analyst"]}')

st.subheader("Timeline")
for t in case["timeline"]:
    st.write("- " + t)

st.subheader("Analyst notes")
st.write(case["analyst_notes"])

st.subheader("Evidence check")
attached = set(case["evidence_attached"])
for e in pb["required_evidence"]:
    st.write(("✅ " if e in attached else "❌ ") + e)

st.subheader("Verdict")
st.write(case["verdict"])