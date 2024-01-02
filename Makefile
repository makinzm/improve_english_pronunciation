lint:
	rye run ruff src --fix

streamlit:
	rye run streamlit run src/improve_english_pronunciation/main.py
