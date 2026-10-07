# SOC Case Review Scorer

A demo tool that reviews closed security cases against a playbook checklist,
flags missing evidence, and routes weak or ambiguous cases to human QC review.

**All data is fictional.** Nothing here comes from any real organisation.

## Run it
    python3 -m venv venv
    source venv/bin/activate
    pip install streamlit
    python -m streamlit run app.py

## Status
- [x] Fictional playbooks and 12 sample cases
- [x] Case viewer with evidence check
- [ ] AI scoring of each checklist item
- [ ] Human review queue
- [ ] Database storage
